---
name: 4mat-review
description: "Adversarially audit a draft talk, script, slide deck or 4MAT storyboard for sequencing, evidence, authenticity, audience fit, timing, demo and ethics; propose fixes."
---

# The 4MAT quality gate

Critique the *actual* artifacts. Don't mark PASS without inspection. Score 0–2 on each of 12 dimensions (24 max), citing slide/paragraph evidence:

1. Mini-What previews expectations in a few sentences.
2. WHY addresses *this audience* and its actual goals without fabricated empathy.
3. WHAT has precise, source-backed claims and a clear mental model.
4. HOW contains a reproducible demonstration, walkthrough or exercise.
5. WHAT IF includes upside, limitations/what-if-not, and a meaningful next action.
6. Sequence and transitions preserve 4MAT (or explicitly justified variant).
7. Timings fit total duration, including demonstration and questions.
8. Evidence statuses distinguish fact, hypothesis, demo, aspiration and invented metaphor.
9. Format and information density fit audience, medium and accessibility.
10. Content/process cues are useful, honest, opt-in and not covertly manipulative.
11. Story and imagery clarify the subject instead of overshadowing it.
12. Q&A anticipates strongest skepticism and includes explicit limitations.

Scoring: `0 = absent or misleading`, `1 = partial / needs revision`, `2 = demonstrated`. This is a **team editorial rubric**, not a validated psychometric scale. Prioritize these **blocking failures**: fabricated stats, invented research outcomes, inaccessible medium, no practical HOW, no WHAT IF, time overrun, unconsented personal story.

If `slides.json` exists, run `python scripts/audit_deck.py path --strict` (or `.4mat-studio/scripts/audit_deck.py` after manual installation) and report deterministic output separately from editorial ratings. Where tools permit, ask `devils-advocate` as a read-only independent reviewer, then integrate its strongest objections.

Output `review.md` with score by dimension, citations to content IDs, 3 highest-impact revisions, corrected phrases, residual risks and final recommendation (`READY / REVISE / NOT EVIDENCE-READY`). Do not claim 24/24 without rehearsing and external feedback.
