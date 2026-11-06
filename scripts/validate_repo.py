#!/usr/bin/env python3
"""Run fast static structural checks; does not replace `claude plugin validate`."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "4-mat-to-nlp-presentation",
    "4mat-start",
    "4mat-route",
    "4mat-interview",
    "4mat-evidence",
    "4mat-storyboard",
    "4mat-nlp",
    "4mat-produce",
    "4mat-review",
    "4mat-rehearse",
    "4mat-perceptual-positions",
    "4mat-disney-strategy",
    "4mat-logical-levels",
    "4mat-sleight-of-mouth",
    "4mat-nested-loops",
    "4mat-state-anchor",
}
EXPECTED_AGENTS = {
    "audience-strategist",
    "evidence-librarian",
    "nlp-coach",
    "story-architect",
    "experience-designer",
    "devils-advocate",
    "perspective-explorer",
    "disney-strategist",
}


def parse_header(path):
    data = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", data, re.S)
    if not match:
        raise ValueError(f"Missing YAML frontmatter in {path}")
    header = match.group(1)
    fields = {}
    for line in header.splitlines():
        if re.match(r"^[\w-]+:", line):
            key, value = line.split(":", 1)
            fields[key] = value.strip().strip('"').strip("'")
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"Missing name/description in {path}")
    return fields, data[match.end():]


def main():
    errors = []
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        if plugin.get("name") not in ("4-mat-to-nlp-presentation", "4mat-nlp"):
            errors.append("Incorrect plugin name")
        if market.get("plugins", [{}])[0].get("source") != "./":
            errors.append("Marketplace source must refer to the plugin root")
        if market.get("plugins", [{}])[0].get("name") != plugin.get("name"):
            errors.append("Plugin and marketplace names differ")
    except (OSError, ValueError, IndexError) as exc:
        errors.append(str(exc))
    skills = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if skills != EXPECTED_SKILLS:
        errors.append(f"Skill mismatch: expected {EXPECTED_SKILLS}, got {skills}")
    agents = {p.stem for p in (ROOT / "agents").glob("*.md")}
    if agents != EXPECTED_AGENTS:
        errors.append(f"Agent mismatch: expected {EXPECTED_AGENTS}, got {agents}")
    for sk in skills:
        try:
            hdr, body = parse_header(ROOT / "skills" / sk / "SKILL.md")
            if hdr["name"] != sk:
                errors.append(f"Name mismatch in skill {sk}")
            if len(body.strip()) < 180:
                errors.append(f"Skill {sk} appears empty")
        except ValueError as exc:
            errors.append(str(exc))
    for name in agents:
        try:
            hdr, body = parse_header(ROOT / "agents" / (name + ".md"))
            if hdr["name"] != name:
                errors.append(f"Name mismatch in agent {name}")
            if not hdr.get("tools"):
                errors.append(f"No tools in agent {name}")
        except ValueError as exc:
            errors.append(str(exc))
    from audit_deck import audit
    for ex_dir in ("examples/wonderland", "examples/danilo-wonderland-70-30"):
        ex_path = ROOT / ex_dir / "presentation.json"
        if ex_path.is_file():
            example = json.loads(ex_path.read_text(encoding="utf-8"))
            deck_errors, deck_warnings = audit(example)
            errors.extend(f"{ex_dir}: {e}" for e in deck_errors)
        else:
            errors.append(f"Missing presentation.json in {ex_dir}")
    print(f"Static repository validation: {len(skills)} skills, {len(agents)} agents, {len(errors)} errors")
    for e in errors:
        print("ERROR", e)
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
