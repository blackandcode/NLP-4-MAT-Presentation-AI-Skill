# S1 session log — NLP Master examiners, 15–20 min (orchestrator walkthrough)

**Prompt (from the QA brief):** "I need a 15–20 minute presentation for my NLP Master examiners about Wonderland. I have provided my theoretical work, research, and prototype description. I want the audience to understand why the idea matters, its connection to NLP, how the prototype demonstrates it, and what this could become in the future. Help me create an excellent 4MAT presentation."

**Sources read:**
- `Wonderland_NLP_Master - Verzija 1.2.md` (thesis, 15 pp.)
- `nlp-writing-feedback-motivation-about-danilo-journey.md` (later personal reflection)
- `4MAT_OCR_kompletno.md` (method)

**How it was run:** the same model that revised the skills followed `skills/4-mat-to-nlp-presentation/SKILL.md` in one session. The user's answers were **simulated**: the recommended option was accepted each time, and each such decision is marked `recommended-and-accepted (simulated)`. No native subagents ran; the lenses were run as separate passes.

## 1. Classification

NEW request, **Deep** depth (academic defense, large source set). The planned stages are GATHER → BRIEF → EVIDENCE → STORY → PRODUCE → REVIEW, with REHEARSE offered at the end.

## 2. Readiness map after reading (before any question)

| Slot | State | Found in sources (not asked) |
|---|---|---|
| S1 Outcome | I | The prompt gives the presenter's goals (why it matters, NLP link, prototype, future). The audience outcome must still be chosen. |
| S2 Audience | E | NLP Master examiners (prompt). The thesis is written in Montenegrin. |
| S3 Container | I | 15–20 min (prompt). The exact slot, Q&A placement and language are open. |
| S4 WHY | I | Strong candidates in the sources: the adult reflex "To ne može" vs. "Hajde da vidimo šta zamišljaš" (thesis §1.1); the life goal of leaving a better world (§7); the modeling insight from mentoring about 200 engineers (reflection, WHAT). |
| S5 WHAT | E | The four research questions (§1.3), the Disney roles plus Meta/Milton models, perceptual positions, T.O.T.E. and logical levels (§§2–4), and an explicit list of limits (§§1.3, 5.5). |
| S6 HOW | I | An existing demonstrator, voice → drawing (abstract, §5.1). The Lumi dialogues are explicitly *imagined* (abstract, §4.5). Whether a live demo is possible is unknown. |
| S7 WHAT IF | E | The roadmap (§§5.2, 6.4), the evaluation plan (§5.5), the ethics boundaries (§4.6, §6.1), and a parent/environment extension (reflection). |
| S8 Voice | E | Author phrases captured verbatim (see the brief). |

**Contradiction or scope tension detected:** the later reflection widens the scope to parents and the child's environment, while the thesis centres on the child and Lumi. Which scope to present is a user decision (Q6).

**Fidelity alert raised before drafting:** the reflection says "Mogu posmatrati kako se kreativni proces odvija kada roditelj odmah nudi rješenje…" ("I *can* observe…"). That is a *plan*, not a completed observation. Logged as claim C022 with layer *planned*.

## 3. Decision frontier

**Round A** (outcome, container, demo, language). These would be sent as one `AskUserQuestion` call.

| # | Question | Options (recommended first) | Answer |
|---|---|---|---|
| Q1 | What is the exact speaking slot? | **18 min talk + Q&A after** (a buffer inside 15–20) · 15 min · 20 min including Q&A | 18 + Q&A after — recommended-and-accepted (simulated) |
| Q2 | What should examiners be able to do afterwards? | **Understand and critically evaluate the model, the demo and the validation plan** · be moved by the vision · give pilot-design feedback only | Understand + evaluate (simulated) |
| Q3 | How will HOW be demonstrated? | **Live demo of the existing prototype with a recorded fallback** · recorded video only · screenshots + narration · no demo (illustrative dialogue only) | Live + fallback (simulated) |
| Q4 | Delivery language? | **Montenegrin (matches the examiners and the sources)** · English | *For this repository fixture: English* (simulated override; the real delivery would be in Montenegrin) |

**Round B** (unblocked by A: WHY strategy, scope, consent for personal stories).

| # | Question | Options | Answer |
|---|---|---|---|
| Q5 | WHY strategy? | **Question-led: the "To ne može" moment + the research question, then the personal life goal** (academic + authentic) · story-led personal journey (strong warmth, but less time for method with examiners) · problem-first (creativity as an educational value, OECD) | Question-led (simulated) |
| Q6 | The parent/environment extension from the later reflection? | **Future direction in WHAT IF** (keeps the thesis scope clean) · a WHY pillar · omit | WHAT IF (simulated) |
| Q7 | Which personal experiences may be used, in your own words? (multi-select) | **Mentoring ~200 engineers (modeling insight)** · **Grandfather's workshop (close)** · parenting two sons | The first two (simulated) |

**Round C** (close and deliverables).

| # | Question | Options | Answer |
|---|---|---|---|
| Q8 | Close? | **Invite examiners to critique the pilot indicators** · reflective question · vision statement | Critique invitation (simulated) |
| Q9 | Deliverables? | **Storyboard + deck + cue notes + Q&A** · add a full verbatim script · cue cards only | Storyboard + deck + Q&A (simulated) |

**Questions not asked, because the sources already answer them:** what the prototype does; the research questions; the NLP methods used; the evaluation indicators; the ethical limits; the author's motivation.

**Total: 9 decisions in 3 rounds.**

## 4. Specialist lenses (sequential passes; no native subagents)

| Lens | Key finding | Effect on output |
|---|---|---|
| audience-strategist | Examiners need to see *what is modeled* vs. *what is illustrated*, and why NLP rather than a conventional creativity framework. | Added the research-questions slide and the Q&A item "Why NLP?" |
| evidence-librarian | C022 (parent observation) is a plan; the Lumi dialogues are imagined; adaptive Lumi is future work; no outcome data exists. | Every HOW slide labels its layer; C013 and C014 are shown only in the roadmap. |
| nlp-coach | Two techniques are enough: a common-ground opening, and a T.O.T.E. structure for the demo. No stage-psychogeography for a seated panel. | No NLP pocket exercises were run. |
| story-architect | Option A (question-led) vs. Option B (story-led): A fits an evaluation outcome. | A chosen. |
| experience-designer | The demo is the highest risk. Pre-frame "watch who decides", time-box it to 2.5 min, and keep a 60-second recorded fallback. | Applied on slide 7. |
| devils-advocate | See `review.md`: no blockers, three major issues. | The major issues are recorded as revisions; no draft was rewritten. |
