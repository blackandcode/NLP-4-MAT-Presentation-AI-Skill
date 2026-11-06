import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_dist
import validate_repo

CFG = json.loads((ROOT / "distribution/config.json").read_text(encoding="utf-8"))
NAME = CFG["name"]
RESERVED = re.compile(r"^(claude-|anthropic-|anthropics-|cc-plugin-)|^(claude|anthropic|anthropics|claude-code|claude-mods)$")
AGENT_PLUGIN_KEYS = {"$schema", "name", "version", "description", "author", "homepage", "repository",
                     "license", "keywords", "extensions"}
FORBIDDEN_IN_SKILLS = ("${CLAUDE_PLUGIN_ROOT}", ".4mat-studio", "knowledge/")
LOCAL_REF = re.compile(r"\b(references/[A-Za-z0-9_.-]+\.md|scripts/[a-z_]+\.py)")


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", path
    return struct.unpack(">II", head[16:24])


def frontmatter_keys(skill_md):
    header, _ = build_dist.split_frontmatter(skill_md.read_text(encoding="utf-8"))
    return {line.split(":", 1)[0].strip() for line in header if ":" in line}, header


class DistTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)
        cls.claude, cls.openai = build_dist.build(cls.out, zips=True)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_dist_is_current(self):
        self.assertEqual(build_dist.compare(ROOT / "dist", self.out), [],
                         "dist/ is stale: run python scripts/build_dist.py")

    def test_skills_are_self_contained(self):
        for plugin in (self.claude, self.openai):
            for skill in sorted((plugin / "skills").iterdir()):
                for f in sorted(p for p in skill.rglob("*.md")):
                    text = f.read_text(encoding="utf-8")
                    for bad in FORBIDDEN_IN_SKILLS:
                        self.assertNotIn(bad, text, f"{f.relative_to(self.out)} mentions {bad}")
                    for ref in set(LOCAL_REF.findall(text)):
                        self.assertTrue((skill / ref).is_file(), f"{f.relative_to(self.out)} -> missing {ref}")
                    self.assertNotIn("`examples/", text, f"{f} has an unlinked examples/ path")

    def test_portable_skill_frontmatter(self):
        names = set()
        for skill in sorted((self.openai / "skills").iterdir()):
            keys, header = frontmatter_keys(skill / "SKILL.md")
            self.assertEqual(keys, {"name", "description"}, skill.name)
            hdr = dict(line.split(":", 1) for line in header)
            self.assertEqual(hdr["name"].strip(), skill.name)
            self.assertLessEqual(len(hdr["description"].strip().strip('"')), 200, skill.name)
            names.add(skill.name)
        self.assertIn(NAME, names)
        self.assertEqual(len(names), 14)

    def test_single_command_with_subcommands(self):
        for plugin in (self.claude, self.openai):
            body = (plugin / "skills" / "nlp-4-mat" / "SKILL.md").read_text(encoding="utf-8")
            for syntax in ("`/nlp-4-mat`", "`@nlp-4-mat`", "`$nlp-4-mat`"):
                self.assertIn(syntax, body)
            for cmd in ("help", "new", "status", "review", "pitch", "workshop", "talk", "rehearse",
                        "retarget", "revise", "route", "perspectives", "disney", "objections"):
                self.assertIn(f"`{cmd}", body, cmd)
            self.assertTrue((plugin / "skills" / "nlp-4-mat" / "references" / "routes.md").is_file())
        self.assertFalse((self.claude / "skills" / "4mat-start").exists())
        self.assertFalse((self.claude / "skills" / "4mat-route").exists())

    def test_claude_plugin_layout(self):
        manifest = json.loads((self.claude / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], NAME)
        self.assertIsNone(RESERVED.search(manifest["name"]))
        self.assertEqual(manifest["version"], CFG["version"])
        for key in ("homepage", "documentationUrl", "supportUrl", "privacyPolicyUrl", "termsOfServiceUrl"):
            self.assertTrue(manifest[key].startswith("https://"), key)
        self.assertTrue((self.claude / manifest["icon"]).is_file())
        self.assertEqual(len(list((self.claude / "skills").iterdir())), 14)
        self.assertEqual(len(list((self.claude / "agents").glob("*.md"))), 6)
        for agent in (self.claude / "agents").glob("*.md"):
            self.assertNotIn(".4mat-studio", agent.read_text(encoding="utf-8"))
        for name in ("README.md", "LICENSE", "PRIVACY.md", "knowledge/AGENT_CONTRACT.md"):
            self.assertTrue((self.claude / name).is_file(), name)

    def test_openai_manifest_constraints(self):
        manifest = json.loads((self.openai / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["$schema"], build_dist.AGENT_PLUGINS_SCHEMA)
        self.assertLessEqual(set(manifest), AGENT_PLUGIN_KEYS)
        self.assertRegex(manifest["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(manifest["name"]), 64)
        self.assertLessEqual(set(manifest["author"]), {"name", "email", "url"})
        self.assertIsInstance(manifest["repository"], str)
        ui = manifest["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(ui["displayName"]), 30)
        self.assertLessEqual(len(ui["shortDescription"]), 30)
        self.assertLessEqual(len(ui["longDescription"]), 4000)
        self.assertLessEqual(len(ui["developerName"]), 80)
        self.assertLessEqual(len(ui["defaultPrompt"]), 3)
        self.assertTrue(all(len(p) <= 128 for p in ui["defaultPrompt"]))
        self.assertRegex(ui["brandColor"], r"^#[0-9A-Fa-f]{6}$")
        for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
            self.assertTrue(ui[key].startswith("https://") and len(ui[key]) <= 1024, key)
        for key in ("composerIcon", "logo"):
            w, h = png_size(self.openai / ui[key])
            self.assertEqual(w, h)
            self.assertGreaterEqual(w, 48)
            self.assertLessEqual(w, 4096)
            self.assertLess((self.openai / ui[key]).stat().st_size, 5 * 1024 * 1024)
        self.assertNotIn("apps", manifest["extensions"]["com.openai"])
        self.assertNotIn("hooks", manifest["extensions"]["com.openai"])
        self.assertFalse((self.openai / "agents").exists())

    def test_marketplaces_point_at_builds(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(market["plugins"][0]["source"], f"./dist/claude/{NAME}")
        oa = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(oa["plugins"][0]["source"]["path"], f"./dist/openai/{NAME}")
        personal = json.loads((self.out / "openai/personal-marketplace.json").read_text(encoding="utf-8"))
        src = personal["plugins"][0]["source"]
        self.assertEqual(src["source"], "git-subdir")
        self.assertEqual(src["url"], CFG["repository"] + ".git")

    def test_no_personal_content_in_packages(self):
        errors = []
        for plugin in (self.claude, self.openai):
            for f in plugin.rglob("*.md"):
                hits = validate_repo.PERSONAL_TERMS.findall(f.read_text(encoding="utf-8"))
                if hits:
                    errors.append(f"{f.relative_to(self.out)}: {hits}")
        self.assertEqual(errors, [])

    def test_zip_layouts(self):
        zips = self.out / "zips"
        tag = f"{NAME}-{CFG['version']}"
        with zipfile.ZipFile(zips / f"claude-plugin-{tag}.zip") as zf:
            self.assertIn(".claude-plugin/plugin.json", zf.namelist())
        with zipfile.ZipFile(zips / f"openai-plugin-{tag}.zip") as zf:
            self.assertIn("plugin.json", zf.namelist())
            self.assertIn(f"skills/{NAME}/SKILL.md", zf.namelist())
        skill_zips = sorted((zips / "claude-skills").glob("*.zip"))
        self.assertEqual(len(skill_zips), 14)
        for z in skill_zips:
            with zipfile.ZipFile(z) as zf:
                tops = {n.split("/", 1)[0] for n in zf.namelist()}
                self.assertEqual(tops, {z.stem}, z.name)
                self.assertIn(f"{z.stem}/SKILL.md", zf.namelist())

    def test_bundled_scripts_run_standalone(self):
        scripts = self.openai / "skills" / "4mat-produce" / "scripts"
        deck = ROOT / "examples/wonderland/presentation.json"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, str(scripts / "render_deck.py"), str(deck), "--out", str(Path(d) / "x.html")],
                               capture_output=True, text=True, cwd=d, env=env)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((Path(d) / "x.html").is_file())
            r = subprocess.run([sys.executable, str(scripts / "audit_deck.py"), str(deck), "--strict"],
                               capture_output=True, text=True, cwd=d, env=env)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
