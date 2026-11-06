#!/usr/bin/env python3
"""Deterministic baseline audit for 4MAT slide/segment JSON. Editorial review is still required.

Checks: required fields, phase vocabulary and order (optionally per nested `cycle`), time totals,
diagram schema, evidence-ID format, optional evidence-ledger cross-check (--evidence), and a
speaking-rate overrun estimate from `speaker_notes` word counts (--max-wpm).
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

PHASES = ("mini-what", "why", "what", "how", "what-if")
EVIDENCE_ID = re.compile(r"^C\d{3,}$")
LEDGER_ID = re.compile(r"\bC\d{3,}\b")
DEFAULT_MAX_WPM = 160  # generous upper bound for spoken delivery; most speakers sit at 110-150 wpm
DOWNSIDE_TERMS = ("risk", "limit", "not ", "if not", "cost", "ako ne", "rizik", "ograničen", "ne usp")


def _is_positive_number(value):
    return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value) and value > 0


def _check_order(slides, errors):
    """Phases must be non-decreasing; with `cycle` fields, non-decreasing inside each contiguous cycle."""
    uses_cycles = any(isinstance(s, dict) and s.get("cycle") for s in slides)
    valid = [s for s in slides if isinstance(s, dict) and s.get("phase") in PHASES]
    if not uses_cycles:
        order = [PHASES.index(s["phase"]) for s in valid]
        if order != sorted(order):
            errors.append("Slides must follow mini-what → why → what → how → what-if order "
                          "(use a `cycle` field to nest 4MAT cycles inside longer sessions)")
        return
    groups, seen_cycles = [], set()
    for s in valid:
        cid = str(s.get("cycle") or "main")
        if groups and groups[-1][0] == cid:
            groups[-1][1].append(s["phase"])
        else:
            if cid in seen_cycles:
                errors.append(f"cycle {cid!r} is not contiguous; keep each nested cycle's slides together")
            seen_cycles.add(cid)
            groups.append((cid, [s["phase"]]))
    for cid, phases in groups:
        order = [PHASES.index(p) for p in phases]
        if order != sorted(order):
            errors.append(f"cycle {cid!r}: phases must follow mini-what → why → what → how → what-if order")
    if valid and valid[0]["phase"] not in ("mini-what", "why"):
        errors.append("A nested session must still open with mini-what (or why)")
    if valid and valid[-1]["phase"] != "what-if":
        errors.append("A nested session must still close with what-if")


def audit(data, max_wpm=DEFAULT_MAX_WPM):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["Top-level JSON must be an object"], []
    for key in ("title", "audience", "medium"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"Missing non-empty string: {key}")
    minutes = data.get("duration_minutes")
    if not _is_positive_number(minutes):
        errors.append("duration_minutes must be a positive finite number")
        minutes = None
    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty array")
        return errors, warnings
    seen, total, phase_minutes = set(), 0.0, {p: 0.0 for p in PHASES}
    for idx, slide in enumerate(slides, 1):
        tag = f"slide {idx}"
        if not isinstance(slide, dict):
            errors.append(f"{tag}: entry must be an object")
            continue
        phase = slide.get("phase")
        if phase not in PHASES:
            errors.append(f"{tag}: invalid phase {phase!r}")
        else:
            seen.add(phase)
        for key in ("title", "headline", "speaker_notes"):
            if not isinstance(slide.get(key), str) or not slide[key].strip():
                errors.append(f"{tag}: missing {key}")
        body = slide.get("body", [])
        if not isinstance(body, list) or any(not isinstance(x, str) for x in body):
            errors.append(f"{tag}: body must be string list")
        elif len(body) > 5:
            warnings.append(f"{tag}: {len(body)} bullets; consider reducing text")
        t = slide.get("minutes")
        if not _is_positive_number(t):
            errors.append(f"{tag}: minutes must be positive finite number")
        else:
            total += t
            if phase in PHASES:
                phase_minutes[phase] += t
            notes = slide.get("speaker_notes")
            if max_wpm and isinstance(notes, str):
                words = len(re.findall(r"\w+", notes))
                if words / t > max_wpm:
                    warnings.append(f"{tag}: speaker_notes need ~{words / t:.0f} wpm for {t} min "
                                    f"(> {max_wpm}); likely overrun — cut text or add time")
        cycle = slide.get("cycle")
        if cycle is not None and (not isinstance(cycle, str) or not cycle.strip()):
            errors.append(f"{tag}: cycle must be a non-empty string when present")
        diagram = slide.get("diagram")
        if diagram is not None:
            nodes = diagram.get("nodes") if isinstance(diagram, dict) else None
            if (not isinstance(diagram, dict) or diagram.get("type") not in ("steps", "cycle", "layers", "roadmap")
                    or not isinstance(nodes, list) or not (2 <= len(nodes) <= 6)
                    or not all(isinstance(x, str) and x.strip() for x in nodes)):
                errors.append(f"{tag}: diagram must specify type steps/cycle/layers/roadmap and 2–6 text nodes")
        ids = slide.get("evidence_ids", [])
        if not isinstance(ids, list) or any(not isinstance(x, str) or not EVIDENCE_ID.match(x) for x in ids):
            errors.append(f"{tag}: evidence_ids must use C001-style strings")
        if phase == "how" and not slide.get("audience_prompt") and not slide.get("visual") and not slide.get("diagram"):
            warnings.append(f"{tag}: HOW phase needs a demonstrated step, visual or practice")
        if phase == "what-if" and not any(str(s).strip() for s in (slide.get("body") or [])):
            warnings.append(f"{tag}: WHAT IF should show choices and consequences")
    missing = sorted(set(PHASES) - seen, key=PHASES.index)
    if missing:
        errors.append("Missing 4MAT phases: " + ", ".join(missing))
    _check_order(slides, errors)
    if minutes is not None and abs(total - minutes) > 0.02:
        errors.append(f"Slide durations sum to {total:.2f} min, expected {minutes:.2f}")
    if minutes and phase_minutes["mini-what"] > 0.15 * minutes:
        warnings.append(f"MINI WHAT uses {phase_minutes['mini-what']:.1f} of {minutes} min (>15%); "
                        "it should be a short preview, not the WHY")
    if "what-if" in seen:
        text = " ".join(str(x) for s in slides if isinstance(s, dict) and s.get("phase") == "what-if"
                        for x in s.get("body", []) if isinstance(x, str)).lower()
        if not any(term in text for term in DOWNSIDE_TERMS):
            warnings.append("WHAT IF lacks explicit downside, limitation or nonadoption framing")
    if not any(isinstance(s, dict) and s.get("phase") == "how"
               and (s.get("audience_prompt") or s.get("visual") or s.get("diagram")) for s in slides):
        warnings.append("No practical HOW interaction/visual detected")
    return errors, warnings


def crosscheck_evidence(data, ledger_text):
    """Every evidence_id cited by a slide must exist in the claim ledger (evidence.md)."""
    known = set(LEDGER_ID.findall(ledger_text or ""))
    errors = []
    if not known:
        return ["Evidence ledger contains no C001-style claim IDs"]
    for idx, slide in enumerate(data.get("slides", []) if isinstance(data, dict) else [], 1):
        if not isinstance(slide, dict):
            continue
        for cid in slide.get("evidence_ids", []) or []:
            if isinstance(cid, str) and cid not in known:
                errors.append(f"slide {idx}: evidence ID {cid} not found in ledger")
    return errors


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", type=Path)
    p.add_argument("--strict", action="store_true", help="Return nonzero if any errors (warnings are advisory)")
    p.add_argument("--evidence", type=Path, help="evidence.md claim ledger to cross-check evidence_ids against")
    p.add_argument("--max-wpm", type=int, default=DEFAULT_MAX_WPM,
                   help=f"Speaking-rate ceiling for overrun warnings (default {DEFAULT_MAX_WPM}; 0 disables)")
    args = p.parse_args(argv)
    try:
        obj = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"Cannot read JSON: {exc}", file=sys.stderr)
        return 2
    errors, warnings = audit(obj, max_wpm=args.max_wpm)
    if args.evidence:
        try:
            errors += crosscheck_evidence(obj, args.evidence.read_text(encoding="utf-8"))
        except OSError as exc:
            errors.append(f"Cannot read evidence ledger: {exc}")
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
