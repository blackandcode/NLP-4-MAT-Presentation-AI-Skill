#!/usr/bin/env python3
"""Deterministic baseline audit for 4MAT slide JSON. Editorial review is still required."""
import argparse
import json
import math
import re
import sys
from pathlib import Path

PHASES = ("mini-what", "why", "what", "how", "what-if")


def audit(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["Top-level JSON must be an object"], []
    for key in ("title", "audience", "medium"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"Missing non-empty string: {key}")
    minutes = data.get("duration_minutes")
    if isinstance(minutes, bool) or not isinstance(minutes, (int, float)) or not math.isfinite(minutes) or minutes <= 0:
        errors.append("duration_minutes must be a positive finite number")
        minutes = None
    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty array")
        return errors, warnings
    seen, total, phases = set(), 0.0, []
    identifiers = re.compile(r"^C\d{3,}$")
    for idx, slide in enumerate(slides, 1):
        tag = f"slide {idx}"
        if not isinstance(slide, dict):
            errors.append(f"{tag}: entry must be an object")
            continue
        phase = slide.get("phase")
        if phase not in PHASES:
            errors.append(f"{tag}: invalid phase {phase!r}")
        else:
            phases.append(phase)
            seen.add(phase)
        for key in ("title", "headline", "speaker_notes"):
            if not isinstance(slide.get(key), str) or not slide[key].strip():
                errors.append(f"{tag}: missing {key}")
        body = slide.get("body", [])
        if not isinstance(body, list) or any(not isinstance(x, str) for x in body):
            errors.append(f"{tag}: body must be string list")
        if isinstance(body, list) and len(body) > 5:
            warnings.append(f"{tag}: {len(body)} bullets; consider reducing text")
        t = slide.get("minutes")
        if isinstance(t, bool) or not isinstance(t, (int, float)) or not math.isfinite(t) or t <= 0:
            errors.append(f"{tag}: minutes must be positive finite number")
        else:
            total += t
        diagram = slide.get("diagram")
        if diagram is not None:
            if not isinstance(diagram, dict) or diagram.get("type") not in ("steps", "cycle", "layers", "roadmap") or not isinstance(diagram.get("nodes"), list) or not (2 <= len(diagram["nodes"]) <= 6) or not all(isinstance(x,str) and x.strip() for x in diagram["nodes"]):
                errors.append(f"{tag}: diagram must specify type steps/cycle/layers/roadmap and 2–6 text nodes")
        ids = slide.get("evidence_ids", [])
        if not isinstance(ids, list) or any(not isinstance(x, str) or not identifiers.match(x) for x in ids):
            errors.append(f"{tag}: evidence_ids must use C001-style strings")
        if phase == "how" and not slide.get("audience_prompt") and not slide.get("visual"):
            warnings.append(f"{tag}: HOW phase needs a demonstrated step, visual or practice")
        if phase == "what-if" and not any(str(s).strip() for s in (slide.get("body") or [])):
            warnings.append(f"{tag}: WHAT IF should show choices and consequences")
    missing = sorted(set(PHASES) - seen, key=PHASES.index)
    if missing:
        errors.append("Missing 4MAT phases: " + ", ".join(missing))
    order = [PHASES.index(p) for p in phases]
    if order != sorted(order):
        errors.append("Slides must follow mini-what → why → what → how → what-if order")
    if minutes is not None and abs(total-minutes) > 0.02:
        errors.append(f"Slide durations sum to {total:.2f} min, expected {minutes:.2f}")
    if "what-if" in seen:
        text = " ".join(str(x) for s in slides if isinstance(s, dict) and s.get("phase") == "what-if" for x in s.get("body", []) if isinstance(x, str)).lower()
        if not any(t in text for t in ("risk", "limit", "not ", "ako ne", "rizik", "ogranič", "ograničen", "ne usp")):
            warnings.append("WHAT IF lacks explicit downside, limitation or nonadoption framing")
    if not any(isinstance(s, dict) and s.get("phase") == "how" and (s.get("audience_prompt") or s.get("visual")) for s in slides):
        warnings.append("No practical HOW interaction/visual detected")
    return errors, warnings


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--strict", action="store_true", help="Return nonzero if any errors (warnings are advisory)")
    args = p.parse_args(argv)
    try:
        obj = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"Cannot read JSON: {exc}", file=sys.stderr)
        return 2
    errors, warnings = audit(obj)
    print(f"4MAT structure audit: {len(errors)} error(s), {len(warnings)} warning(s)")
    for issue in errors:
        print("ERROR:", issue)
    for issue in warnings:
        print("WARN:", issue)
    if not errors:
        print("Structural checks passed. Independent editorial / factual review is still required.")
    return 1 if errors and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
