#!/usr/bin/env python3
"""Run fast static structural checks; does not replace `claude plugin validate`.

Checks: plugin/marketplace manifests, skill and agent inventory, Agent Skills frontmatter rules
(name format/length/directory match, description length), that every referenced knowledge/,
scripts/ and references/ file exists, that generic skills/agents/knowledge contain no
example-specific personal content, the orchestrator/alias wiring, and example deck structure.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATOR = "4-mat-to-nlp-presentation"
ALIAS = "4mat-start"
EXPECTED_SKILLS = {
    ORCHESTRATOR, ALIAS, "4mat-route", "4mat-interview", "4mat-evidence", "4mat-storyboard",
    "4mat-nlp", "4mat-produce", "4mat-review", "4mat-rehearse",
    "4mat-perceptual-positions", "4mat-disney-strategy", "4mat-logical-levels",
    "4mat-sleight-of-mouth", "4mat-nested-loops", "4mat-state-anchor",
}
EXPECTED_AGENTS = {
    "audience-strategist", "evidence-librarian", "nlp-coach",
    "story-architect", "experience-designer", "devils-advocate",
}
# Agent Skills spec (agentskills.io): 1-64 chars, lowercase alphanumerics and single hyphens.
SKILL_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_DESCRIPTION = 1024
# Generic, reusable files must not carry one presenter's personal story or family names.
# Those belong in examples/ only (see examples/danilo-wonderland-70-30/ as a fixed test input).
PERSONAL_TERMS = re.compile(
    r"\b(Ogi|Ogij\w*|Aleks[ae]\w*|Vesn\w*|Danilo\w*|djedov\w*|Grandfather|Kreativni geni|"
    r"200 (?:engineers|inženjera)|novi početak)\b")
REFERENCE = re.compile(r"\b(knowledge/[A-Za-z0-9_]+\.md|scripts/[a-z_]+\.py|references/[a-z0-9-]+\.md)")


def parse_header(path):
    data = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", data, re.S)
    if not match:
        raise ValueError(f"Missing YAML frontmatter in {path}")
    fields = {}
    for line in match.group(1).splitlines():
        if re.match(r"^[\w-]+:", line):
            key, value = line.split(":", 1)
            fields[key] = value.strip().strip('"').strip("'")
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"Missing name/description in {path}")
    return fields, data[match.end():]


def check_references(path, text, errors):
    for ref in sorted(set(REFERENCE.findall(text))):
        target = (path.parent / ref) if ref.startswith("references/") else (ROOT / ref)
        if not target.is_file():
            errors.append(f"{path.relative_to(ROOT)}: referenced file {ref} does not exist")


def check_generic(path, text, errors):
    hits = sorted(set(m.group(0) for m in PERSONAL_TERMS.finditer(text)))
    if hits:
        errors.append(f"{path.relative_to(ROOT)}: example-specific personal content in a generic file: {', '.join(hits)}")


def main():
    errors = []
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        if plugin.get("name") != ORCHESTRATOR:
            errors.append("Incorrect plugin name")
        entry = market.get("plugins", [{}])[0]
        if entry.get("source") != "./":
            errors.append("Marketplace source must refer to the plugin root")
        if entry.get("name") != plugin.get("name"):
            errors.append("Plugin and marketplace names differ")
        if codex.get("version") != plugin.get("version"):
            errors.append("Claude and Codex manifest versions differ")
    except (OSError, ValueError, IndexError) as exc:
        errors.append(str(exc))

    skills = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if skills != EXPECTED_SKILLS:
        errors.append(f"Skill mismatch: missing {sorted(EXPECTED_SKILLS - skills)}, unexpected {sorted(skills - EXPECTED_SKILLS)}")
    agents = {p.stem for p in (ROOT / "agents").glob("*.md")}
    if agents != EXPECTED_AGENTS:
        errors.append(f"Agent mismatch: missing {sorted(EXPECTED_AGENTS - agents)}, unexpected {sorted(agents - EXPECTED_AGENTS)}")

    headers = {}
    for sk in sorted(skills):
        path = ROOT / "skills" / sk / "SKILL.md"
        try:
            hdr, body = parse_header(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        headers[sk] = hdr
        if hdr["name"] != sk:
            errors.append(f"Name mismatch in skill {sk}")
        if not SKILL_NAME.match(sk) or len(sk) > 64:
            errors.append(f"Skill name {sk!r} violates the Agent Skills naming rule")
        if len(hdr["description"]) > MAX_DESCRIPTION:
            errors.append(f"Skill {sk} description is {len(hdr['description'])} chars (> {MAX_DESCRIPTION})")
        if len(body.strip()) < 180:
            errors.append(f"Skill {sk} appears empty")
        if len(body.splitlines()) > 500:
            errors.append(f"Skill {sk} exceeds 500 lines; move detail into references")
        check_references(path, body, errors)
        check_generic(path, body + hdr["description"], errors)
        for ref in (ROOT / "skills" / sk).glob("references/*.md"):
            text = ref.read_text(encoding="utf-8")
            check_references(ref, text, errors)
            check_generic(ref, text, errors)

    if ORCHESTRATOR in headers and headers[ORCHESTRATOR].get("disable-model-invocation") == "true":
        errors.append(f"{ORCHESTRATOR} must stay model-invocable: it is the natural-language front door")
    if ALIAS in headers:
        alias_body = (ROOT / "skills" / ALIAS / "SKILL.md").read_text(encoding="utf-8")
        if ORCHESTRATOR not in alias_body:
            errors.append(f"{ALIAS} must delegate to {ORCHESTRATOR}")

    for name in sorted(agents):
        path = ROOT / "agents" / f"{name}.md"
        try:
            hdr, body = parse_header(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if hdr["name"] != name:
            errors.append(f"Name mismatch in agent {name}")
        if not hdr.get("tools"):
            errors.append(f"No tools in agent {name}")
        if "Write" in hdr.get("tools", "") or "Edit" in hdr.get("tools", ""):
            errors.append(f"Agent {name} must stay read-only")
        check_references(path, body, errors)
        check_generic(path, body + hdr["description"], errors)

    for path in sorted((ROOT / "knowledge").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        check_references(path, text, errors)
        check_generic(path, text, errors)

    sys.path.insert(0, str(ROOT / "scripts"))
    from audit_deck import audit
    for ex_dir in ("examples/wonderland", "examples/danilo-wonderland-70-30"):
        ex_path = ROOT / ex_dir / "presentation.json"
        if ex_path.is_file():
            deck_errors, _ = audit(json.loads(ex_path.read_text(encoding="utf-8")))
            errors.extend(f"{ex_dir}: {e}" for e in deck_errors)
        else:
            errors.append(f"Missing presentation.json in {ex_dir}")

    print(f"Static repository validation: {len(skills)} skills, {len(agents)} agents, {len(errors)} errors")
    for e in errors:
        print("ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
