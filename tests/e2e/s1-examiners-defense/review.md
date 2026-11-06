# Review — S1 examiners defense

Status: REVISE before rehearsal (the user's answers were simulated; the live build is unverified).

## 1. Devil's-advocate pass (run before the self-scoring; a sequential lens, not a native subagent)

**Blockers**: none found. The lens specifically checked the two failure modes found in the `examples/danilo-wonderland-70-30` test input (see `END_TO_END_TEST_RESULTS.md`):

1. Prototype vs. design target: slide 7 states what the build does today (C003) and what it does not yet do (C013). Pass.
2. Embellished personal story: slide 11 uses only the author's wording about the workshop (C024). Pass.

Caveat: the same model wrote and reviewed this deck, with the failure modes already in mind. This pass is weaker evidence than an independent subagent run on a blind draft.

**Major**

1. The research-questions slide is dense: four long questions in 2 minutes. Suggest bolding the key term of each question.
2. The examiners may ask "Why NLP?" with nothing on the slides to answer it. Covered in `qa.md` #2 and kept off-slide on purpose.
3. The demo depends on the laptop and the network. A fallback exists, but the time box needs rehearsal.

**Minor**: the English fixture vs. the Montenegrin delivery (D004).

## 2. Source-fidelity check

| Item | Result |
|---|---|
| Personal anecdotes (C001, C020, C024) | Match the source wording; no embellishment |
| Prototype capability (slide 7) | Matches C003 |
| Illustrative dialogue (slide 8) | Labelled on screen and in the speaker notes |
| Plans presented as done | None. C022 is not used; C023 is labelled as a direction |

## 3. Rubric

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Mini What | 2 | Slide 1: four-step preview plus the "not a finished study" statement |
| 2 | Audience-specific WHY | 2 | Slides 2–3: research motivation plus the modeling insight relevant to NLP examiners |
| 3 | WHAT | 2 | Slides 4–6: research questions, model, T.O.T.E. and logical levels, each with a claim ID |
| 4 | HOW | 1 | Live demo plus a labelled illustration. Not rehearsed; the build is unverified. |
| 5 | WHAT IF | 2 | Slides 9–11: layers, risks, ladder, ask |
| 6 | Sequence and transitions | 2 | A bridge sentence for each segment in the storyboard |
| 7 | Timing | 1 | 18.0 min allocated; cue notes only; no timed run |
| 8 | Evidence statuses | 2 | Exists / planned / illustrative / hypothesis separated on slides 7–9 |
| 9 | Format and accessibility | 1 | Slide 4 is dense; visuals are not yet produced |
| 10 | Content/process ethics | 2 | Two transparent techniques; no stage tricks |
| 11 | Story serves the subject | 2 | Personal material is limited to motivation and the modeling insight |
| 12 | Q&A | 2 | Seven questions drawn from the evidence gaps |

**Total: 21/24.** This is an editorial rubric.

**Recommendation: REVISE**:
1. Verify the build and record the fallback clip.
2. Run a timed rehearsal.
3. Simplify slide 4.

**Deterministic audit:** `python scripts/audit_deck.py tests/e2e/s1-examiners-defense/presentation.json --strict --evidence tests/e2e/s1-examiners-defense/evidence.md`. The result is in `END_TO_END_TEST_RESULTS.md`.
