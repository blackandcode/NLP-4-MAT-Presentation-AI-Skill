#!/usr/bin/env python3
"""Build self-contained distribution packages from the single source (skills/, agents/, knowledge/, scripts/).

Outputs under --out (default: dist/):
  claude/<name>/                   Claude plugin: Claude Code, claude.ai web/desktop/mobile, Cowork
  openai/<name>/                   Agent Plugins package for ChatGPT and Codex (root plugin.json)
  openai/personal-marketplace.json template for ~/.agents/plugins/marketplace.json (ChatGPT desktop / Codex)
  GENERATED.md                     reminder not to edit generated files
With --zips, also (gitignored):
  zips/claude-plugin-<name>-<version>.zip   claude.ai / Cowork: Customize > Plugins > Upload plugin
  zips/openai-plugin-<name>-<version>.zip   platform.openai.com/plugins: Upload new or existing plugin
  zips/claude-skills/<skill>.zip            claude.ai: Customize > Skills > Upload a skill (folder at ZIP root)
--check rebuilds into a temporary folder and exits 1 if the committed dist/ is out of date.

Every skill is made self-contained: the knowledge/ files and scripts it references (transitively) are
copied into its own references/ and scripts/ folders, and path instructions are rewritten, because
claude.ai, Cowork and ChatGPT load skills individually. Standard library only.
"""
import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "distribution" / "config.json"
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
KNOWLEDGE_RE = re.compile(r"knowledge/([A-Za-z0-9_]+\.md)")
SCRIPT_RE = re.compile(r"scripts/([a-z_]+\.py)")
EXAMPLES_RE = re.compile(r"`(examples/[A-Za-z0-9_./-]+?)`")
SCRIPT_DEPS = {"render_deck.py": ["audit_deck.py"]}
PORTABLE_KEYS = ("name", "description")
TEXT_SUFFIXES = {".md", ".json", ".py", ".svg", ".txt"}
ZIP_DATE = (1980, 1, 1, 0, 0, 0)
RESOLUTION_SUBS = [
    (re.compile(r"\*\*Shared files\*\*: resolve [^\n]*?the repository root\."),
     "**Supporting files** are bundled in this skill's `references/` and `scripts/` folders."),
    (re.compile(r" ?Resolve the path under [^\n]*?the repository root\."), ""),
    (re.compile(r" ?\(resolve under [^)\n]*\)"), ""),
]
AGENT_SUBS = [(re.compile(r"\(look under [^)\n]*\)"), "(in this plugin: `${CLAUDE_PLUGIN_ROOT}/knowledge/`)")]


def load_config():
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def write_json(path, data):
    write_text(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def split_frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        raise ValueError("missing frontmatter")
    return match.group(1).splitlines(), text[match.end():]


def portable_header(lines):
    return [line for line in lines if line.split(":", 1)[0].strip() in PORTABLE_KEYS]


def examples_link(cfg, match):
    path = match.group(1).rstrip("/")
    kind = "blob" if Path(path).suffix else "tree"
    return f"[{path}]({cfg['repository']}/{kind}/main/{path})"


def rewrite_skill_text(cfg, text):
    for pattern, repl in RESOLUTION_SUBS:
        text = pattern.sub(repl, text)
    text = KNOWLEDGE_RE.sub(r"references/\1", text)
    return EXAMPLES_RE.sub(lambda m: examples_link(cfg, m), text)


def dependencies(texts):
    """Transitive closure of knowledge/*.md and scripts/*.py referenced by the given texts."""
    knowledge, scripts, queue = set(), set(), list(texts)
    while queue:
        text = queue.pop()
        for name in KNOWLEDGE_RE.findall(text):
            if name not in knowledge and (ROOT / "knowledge" / name).is_file():
                knowledge.add(name)
                queue.append((ROOT / "knowledge" / name).read_text(encoding="utf-8"))
        for name in SCRIPT_RE.findall(text):
            for dep in [name] + SCRIPT_DEPS.get(name, []):
                if (ROOT / "scripts" / dep).is_file():
                    scripts.add(dep)
    return knowledge, scripts


def build_skill(cfg, src, dest, portable):
    text = (src / "SKILL.md").read_text(encoding="utf-8")
    header, body = split_frontmatter(text)
    own_refs = sorted((src / "references").glob("*.md")) if (src / "references").is_dir() else []
    knowledge, scripts = dependencies([body] + [p.read_text(encoding="utf-8") for p in own_refs])
    if portable:
        header = portable_header(header)
    write_text(dest / "SKILL.md", "---\n" + "\n".join(header) + "\n---\n" + rewrite_skill_text(cfg, body))
    for ref in own_refs:
        write_text(dest / "references" / ref.name, rewrite_skill_text(cfg, ref.read_text(encoding="utf-8")))
    for name in sorted(knowledge):
        write_text(dest / "references" / name,
                   rewrite_skill_text(cfg, (ROOT / "knowledge" / name).read_text(encoding="utf-8")))
    for name in sorted(scripts):
        write_text(dest / "scripts" / name, (ROOT / "scripts" / name).read_text(encoding="utf-8"))


def skill_dirs():
    return sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())


def common_files(dest):
    for name in ("LICENSE", "PRIVACY.md"):
        write_text(dest / name, (ROOT / name).read_text(encoding="utf-8"))


def plugin_readme(cfg, channel):
    lines = [f"# {cfg['displayName']} (`{cfg['name']}`) v{cfg['version']}", "", cfg["description"], "",
             f"This package is generated for **{channel}** from {cfg['repository']}.",
             "Edit the sources there, not these files. The full installation and publishing guide is "
             f"[docs/DISTRIBUTION.md]({cfg['repository']}/blob/main/docs/DISTRIBUTION.md).", "",
             "Start by asking in plain language, for example: "
             f"\"{cfg['defaultPrompts'][0]}\"", "",
             "Privacy: no data collection; see PRIVACY.md. License: MIT.", ""]
    return "\n".join(lines)


def build_claude(cfg, out):
    dest = out / "claude" / cfg["name"]
    manifest = {
        "name": cfg["name"], "displayName": cfg["displayName"], "version": cfg["version"],
        "description": cfg["description"], "author": cfg["author"], "homepage": cfg["homepage"],
        "repository": cfg["repository"], "license": cfg["license"], "keywords": cfg["keywords"],
        "icon": "./assets/icon.png", "documentationUrl": cfg["documentationUrl"],
        "supportUrl": cfg["supportUrl"], "privacyPolicyUrl": cfg["privacyPolicyUrl"],
        "termsOfServiceUrl": cfg["termsOfServiceUrl"],
    }
    write_json(dest / ".claude-plugin" / "plugin.json", manifest)
    for src in skill_dirs():
        build_skill(cfg, src, dest / "skills" / src.name, portable=False)
    for agent in sorted((ROOT / "agents").glob("*.md")):
        text = agent.read_text(encoding="utf-8")
        for pattern, repl in AGENT_SUBS:
            text = pattern.sub(repl, text)
        write_text(dest / "agents" / agent.name, text)
    for path in sorted((ROOT / "knowledge").glob("*.md")):
        text = EXAMPLES_RE.sub(lambda m: examples_link(cfg, m), path.read_text(encoding="utf-8"))
        write_text(dest / "knowledge" / path.name, text)
    (dest / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "assets" / "icon.png", dest / "assets" / "icon.png")
    write_text(dest / "README.md", plugin_readme(cfg, "Claude (Claude Code, claude.ai, Claude Desktop, mobile, Cowork)"))
    common_files(dest)
    return dest


def build_openai(cfg, out):
    dest = out / "openai" / cfg["name"]
    manifest = {
        "$schema": AGENT_PLUGINS_SCHEMA, "name": cfg["name"], "version": cfg["version"],
        "description": cfg["description"], "author": cfg["author"], "homepage": cfg["homepage"],
        "repository": cfg["repository"], "license": cfg["license"], "keywords": cfg["keywords"],
        "extensions": {"com.openai": {"interface": {
            "displayName": cfg["displayName"], "shortDescription": cfg["shortDescription"],
            "longDescription": cfg["longDescription"], "developerName": cfg["developerName"],
            "category": cfg["category"], "websiteURL": cfg["homepage"], "supportURL": cfg["supportUrl"],
            "privacyPolicyURL": cfg["privacyPolicyUrl"], "termsOfServiceURL": cfg["termsOfServiceUrl"],
            "defaultPrompt": cfg["defaultPrompts"][:3], "brandColor": cfg["brandColor"],
            "composerIcon": "./assets/icon.png", "logo": "./assets/logo.png",
        }}},
    }
    write_json(dest / "plugin.json", manifest)
    for src in skill_dirs():
        if src.name not in cfg["claudeOnlySkills"]:
            build_skill(cfg, src, dest / "skills" / src.name, portable=True)
    (dest / "assets").mkdir(parents=True, exist_ok=True)
    for name in ("icon.png", "logo.png"):
        shutil.copyfile(ROOT / "assets" / name, dest / "assets" / name)
    write_text(dest / "README.md", plugin_readme(cfg, "ChatGPT and Codex (Agent Plugins format)"))
    common_files(dest)
    write_json(out / "openai" / "personal-marketplace.json", {
        "name": "nlp-4-mat",
        "plugins": [{
            "name": cfg["name"],
            "source": {"source": "git-subdir", "url": cfg["repository"] + ".git",
                       "path": f"./dist/openai/{cfg['name']}", "ref": "main"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": cfg["category"],
        }],
    })
    return dest


def _zip_dir(src, zip_path, prefix=""):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(p for p in src.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
            info = zipfile.ZipInfo(prefix + path.relative_to(src).as_posix(), ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())


def build_zips(cfg, out, claude_dir, openai_dir):
    zips = out / "zips"
    if zips.exists():
        shutil.rmtree(zips)
    tag = f"{cfg['name']}-{cfg['version']}"
    _zip_dir(claude_dir, zips / f"claude-plugin-{tag}.zip")
    _zip_dir(openai_dir, zips / f"openai-plugin-{tag}.zip")
    for skill in sorted((openai_dir / "skills").iterdir()):
        _zip_dir(skill, zips / "claude-skills" / f"{skill.name}.zip", prefix=f"{skill.name}/")
    return zips


def build(out, zips=False):
    cfg = load_config()
    for sub in ("claude", "openai"):
        if (out / sub).exists():
            shutil.rmtree(out / sub)
    claude_dir = build_claude(cfg, out)
    openai_dir = build_openai(cfg, out)
    write_text(out / "GENERATED.md",
               "# Generated distribution packages\n\nEverything in `claude/` and `openai/` is generated by "
               "`python scripts/build_dist.py` from `skills/`, `agents/`, `knowledge/`, `scripts/`, `assets/` and "
               "`distribution/config.json`. Edit those sources, rebuild, and commit the result. "
               "`python scripts/build_dist.py --check` fails when this folder is stale.\n")
    if zips:
        build_zips(cfg, out, claude_dir, openai_dir)
    return claude_dir, openai_dir


def _tree(base):
    files = {}
    for sub in ("claude", "openai", "GENERATED.md"):
        root = base / sub
        paths = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file()) if root.exists() else []
        for p in paths:
            if "__pycache__" in p.parts or p.suffix == ".pyc":
                continue
            data = p.read_bytes()
            if p.suffix in TEXT_SUFFIXES or p.name == "LICENSE":
                data = data.replace(b"\r\n", b"\n")
            files[p.relative_to(base).as_posix()] = data
    return files


def compare(committed, fresh):
    """Return a list of differences between two dist trees (ignoring zips and line endings)."""
    a, b = _tree(committed), _tree(fresh)
    diffs = [f"missing in committed dist: {k}" for k in sorted(b.keys() - a.keys())]
    diffs += [f"stale file in committed dist: {k}" for k in sorted(a.keys() - b.keys())]
    diffs += [f"content differs: {k}" for k in sorted(a.keys() & b.keys()) if a[k] != b[k]]
    return diffs


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", type=Path, default=ROOT / "dist")
    p.add_argument("--zips", action="store_true", help="also build upload ZIPs under <out>/zips/")
    p.add_argument("--check", action="store_true", help="fail if the committed dist/ is out of date")
    args = p.parse_args(argv)
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            build(Path(tmp))
            diffs = compare(ROOT / "dist", Path(tmp))
        for d in diffs:
            print("DRIFT", d)
        print("dist/ is up to date." if not diffs else f"dist/ is stale ({len(diffs)} differences). Run: python scripts/build_dist.py")
        return 1 if diffs else 0
    claude_dir, openai_dir = build(args.out, zips=args.zips)
    print("Claude plugin:", claude_dir)
    print("OpenAI plugin:", openai_dir)
    if args.zips:
        for z in sorted((args.out / "zips").rglob("*.zip")):
            print("ZIP:", z)
    return 0


if __name__ == "__main__":
    sys.exit(main())
