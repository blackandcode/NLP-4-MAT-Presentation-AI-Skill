---
name: 4mat-review
description: "Independent quality gate for a new or existing talk or deck: devil's-advocate challenge, source-fidelity check, fixed 12-point 4MAT rubric, deck audit and concrete fixes."
---

# The 4MAT quality gate

**Shared files**: resolve `knowledge/…` and `scripts/…` under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

Critique the **actual artifacts**. Never mark anything PASS without inspecting it. Do not let the author of a draft be its only reviewer.

## 1. Independent challenge first

Where tools allow, give the draft to the `devils-advocate` agent **before** writing your own scores, so its view is not anchored by them. Without subagents, run a separate `Lens: devils-advocate` pass that reads the artifacts afresh. Integrate its strongest objections.

## 2. Source-fidelity check (blocking for defenses, pitches and personal talks)

Compare every personal anecdote, prototype capability, result and number in the script and slides against `evidence.md` and the original sources:

- **Tense and modality**: was a plan or "could observe" turned into "observed"? Was an illustrative dialogue presented as a real session or as current product behaviour?
- **Embellishment**: are there sensory, emotional or biographical details the source doesn't contain?
- **Layer mixing**: is the prototype merged with the future vision, or a hypothesis stated as a result?

List each issue with its file and line, and suggest corrected wording. The author confirms or rejects each one.

## 3. Rubric (fixed — do not swap dimensions to suit a particular draft)

Score each dimension 0–2 and cite slide or paragraph evidence:

1. Mini What previews expectations in a few sentences.
2. WHY addresses *this* audience's actual goals without fabricated empathy.
3. WHAT has precise, source-backed claims and a clear mental model.
4. HOW contains a reproducible demonstration, walkthrough or exercise suited to the format.
5. WHAT IF includes upside, limitations or what-if-not, and a meaningful next action.
6. Sequence and transitions preserve 4MAT (or a justified variant), with explicit bridges.
7. Timing fits the duration at a realistic speaking rate, including demos and Q&A.
8. Evidence statuses separate fact, hypothesis, demonstration, aspiration and metaphor, and pass the fidelity check.
9. Format, information density and accessibility fit the audience and the medium.
10. Content and process cues are useful, honest, optional and not covertly manipulative.
11. Story and imagery clarify the subject instead of overshadowing it.
12. Q&A anticipates the strongest scepticism, with explicit limitations.

`0` = absent or misleading; `1` = partial, needs revision; `2` = demonstrated. This is an editorial rubric, not a validated psychometric scale.

**Blocking failures** (verdict at best REVISE): fabricated statistics or results; plans or illustrations presented as facts; unconsented or embellished personal story; no practical HOW; no WHAT IF; time overrun; an inaccessible medium.

## 4. Deterministic checks

If a deck JSON exists, run `python scripts/audit_deck.py <deck> --strict --evidence evidence.md` and report its output separately from the editorial scores.

## 5. Output: `review.md`

Include: scores by dimension with citations; the fidelity findings; the devil's-advocate blockers and how each was resolved; the three highest-impact revisions with corrected phrases; residual risks; and a recommendation of `READY FOR REHEARSAL`, `REVISE` or `NOT EVIDENCE-READY`.

Never claim 24/24 or "ready to deliver" without a rehearsal and outside feedback.
