---
name: 4mat-interview
description: "Interview the presenter in short rounds: find facts in their material, ask only open decisions with a recommended option, and write brief.md with a decision log."
---

# 4MAT interview (decision frontier)

**Supporting files** are bundled in this skill's `references/` and `scripts/` folders.

## 1. Read first, then separate facts from decisions

- Read every supplied file and all earlier answers. Fill slots S1–S8 (the orchestrator's readiness map) as E / I / M, with a pointer for each E or I.
- **Facts** (what the project is, what exists, what the sources say) are yours to find. Never ask the user for them. If the material is large, extract facts with the evidence method or the `evidence-librarian` agent.
- **Decisions** (audience, outcome, emphasis, story, HOW, ask, tone) belong to the user. Ask only those that are still open.

## 2. The frontier, round by round

The frontier is the set of open decisions whose prerequisites are settled. Each round, ask the whole frontier, at most 3–4 questions.

**Round A — what success looks like.**
- *Audience outcome*: what they should know, feel, believe, decide or do. Example options: understand and critically evaluate; approve a pilot or investment; learn a skill they will use; be inspired to discuss and act.
- *Primary audience*: a concrete role and familiarity level, plus secondary audiences. Never "learner types".
- *Container*: minutes; format (slides + speech, speech only, workshop, pitch, live demo, web, recorded); whether interaction is possible; Q&A inside or outside the time; language and register.
- Keep the **presenter's goal** separate from the audience outcome.

**Round B — the WHY and the evidence boundary.** This round adapts to Round A:
- *Examiners*: research questions; what must be labelled prototype vs. vision vs. hypothesis.
- *Investors*: which traction is measured; what the ask is.
- *Educators or parents*: what problem they recognise; safety and privacy concerns.
- *Workshop*: participants' starting level; the materials available.

Story strategy options: the presenter's genuine purpose (requires their consent and their own words); an audience problem backed by a real example; a clearly hypothetical future contrast.

*Story-to-model blend*: ask only if the user wants a personal story woven into a model or method. Offer model-led, balanced and story-led options. **There is no default.**

**Round C — HOW and the close.**
- *HOW*: live demo (with fallback), narrated recording, worked example, audience exercise, or no-tool demonstration.
- *Close*: a decision request, a pilot invitation, a reflective question, or a future scenario covering both upside and downside.
- Add accessibility or tone questions only if they would change the output.

## 3. How to ask

- 2–4 concrete options per question, with the **recommended one first** and a one-sentence reason.
- Name the trade-off when the choice is consequential, for example: "a story-led opening builds connection but leaves less time for method — risky with examiners".
- Always accept "Other", "not sure — recommend", and "skip" (which keeps the recommendation as *assumed*). Terse answers such as `A`, `2`, `you decide` or `skip` are fine.
- Use `AskUserQuestion` when it exists: one call per round, each question self-contained. Otherwise show numbered options and wait.
- After each round, show `Locked / Assumed / Open`.
- Stop when the outcome, audience, container, WHAT evidence, HOW and close are locked or deliberately assumed. The number of questions asked is not the stopping rule.

## 4. Output: `brief.md`

Include: topic; primary and secondary audiences with prior knowledge; audience outcome (know / feel / believe / decide / do); presenter goal; container; must-include material; non-goals; story strategy; HOW mode; close/ask; accessibility; **voice samples** (3–5 short phrases quoted verbatim from the author's own writing, so their voice survives production); open assumptions; and the **decision log** table from `references/DELIVERABLES.md`.

The user can revise any row later. Silence is never consent to a controversial claim or to using a personal story.
