# End-to-end test results

**Date:** 2026-11-06
**Environment:**
- Windows 11, with Python 3.12.16 in a `python:3.12-slim` Docker container (the host has no Python);
- no `claude` CLI on the PATH;
- Claude Code running inside the VS Code extension.

## How to read this

| Kind of evidence | What it proves | What it doesn't |
|---|---|---|
| **Automated** (unit tests, validator, auditor) | Structure, schema, timing arithmetic, ledger coverage, packaging | Whether the model asks good questions or writes a good talk |
| **Walkthrough** (S1–S4) | The skills, followed step by step on the real sources, produce audience-specific, auditable outputs | The model that ran them also revised the skills (a bias); the user's answers were **simulated** (recommended options accepted); no native subagents; no picker UI |
| **Test-input audit** (the two frozen examples) | What v0.2.0 actually produced, measured against its sources | — |

## 1. Automated checks (after the changes)

| Check | Command | Result |
|---|---|---|
| Repository validation | `python scripts/validate_repo.py` | **PASS**: 16 skills, 6 agents, 0 errors |
| Unit tests | `python -m unittest discover -s tests` | **PASS**: 24 tests, OK (v0.2.0 had 9) |
| Strict deck audit, S1 | `python scripts/audit_deck.py tests/e2e/s1-examiners-defense/presentation.json --strict --evidence …/evidence.md` | **PASS**: exit 0, 0 errors, 0 warnings |
| All six decks (4 scenarios + 2 examples) | `audit()` + `crosscheck_evidence()` | **PASS**: 0 errors, 0 warnings, 0 missing ledger IDs |
| Render with nested cycles | `render_deck.py` on S3 and S1 | **PASS**: 11 slides rendered; 4 slides labelled `m1-ask` |
| Installer | `install.py --target claude --dry-run`; `--target codex` | **PASS**: 24 items for Claude (16 skills + 2 support folders + 6 agents); 18 for Codex (16 skills in `.agents/skills`) |
| Negative tests | Out-of-order phase inside a cycle; non-contiguous cycle; session not closing with WHAT IF; unknown evidence ID; 400-word notes in 1 min; Mini What at 3 of 7 min; personal names in a generic file; a missing referenced file; invalid skill names | **PASS**: each one is detected |

**Not executed:**
- `claude plugin validate` (no CLI available);
- loading the skills in a fresh Claude Code session;
- Gemini or Codex runtime behaviour;
- a screen-reader check of the HTML.

## 2. Primary acceptance scenario: S1, NLP Master examiners, 15–20 min

Artifacts: `tests/e2e/s1-examiners-defense/` (`session.md`, `brief.md`, `evidence.md`, `storyboard.md`, `presentation.json`, `qa.md`, `review.md`).

| Expected (vision §10) | Observed | Verdict |
|---|---|---|
| Extracts the core vision accurately | The ledger's 29 claims carry thesis/reflection locators; the core is "modeling creative strategies, not the app" (C004) | Pass |
| Recognises the audience | Examiners → defense shape (WHAT 33%, research questions, labelled demo) | Pass |
| Separates theory, prototype and future | Layers exists / planned / illustrative / hypothesis; slide 9 is literally "Exists · planned · hoped" | Pass |
| Meaningful outcomes | Know (the RQs and the model) · believe (honest separation) · do (critique the indicators) | Pass |
| Asks only unresolved questions | 9 decisions in 3 rounds; 7 fact categories found, not asked | Pass (walkthrough) · **live behaviour Not Verified** |
| Compelling WHY | The "That can't work" reflex, then the research question, then the life goal and the modeling insight | Pass (editorial judgement) |
| Explains the NLP method in WHAT | Disney roles as an *assumption*; Meta/Milton; T.O.T.E.; logical levels | Pass |
| Convincing Wonder Creator demo in HOW | Live voice → drawing (C003), "watch who decides", a 60 s fallback, an explicit "does not yet do" line | Pass on paper · **the build itself Not Verified** |
| Opportunities, limits and future in WHAT IF | Roadmap, risks, validation ladder, critique ask | Pass |
| Preserves personal motivation | Life goal (C001), the 200-engineers modeling insight (C020), the workshop close (C024), in the author's own words | Pass |
| Visuals, notes, timing | Projected diagrams on 6 of 11 slides, visual directions on 2 more; cue notes; 18.0 min | Partial: cue notes, not a script; visuals are directions |
| Challenging academic questions | 7, derived from the ledger gaps | Pass |
| No unsupported impact claims | Fidelity table in `review.md` is clean | Pass |
| Independent critical review | A devil's-advocate *lens pass* in the same session | **Partial**: not independent (same model) |

**Detected before drafting** (this is the system working as intended):
- the scope tension between the thesis (child + Lumi) and the reflection (parents and environment), resolved by D006;
- C022 is a plan ("Mogu posmatrati…") and must never become "I observed".

## 3. Contrasting scenarios

| Scenario | Shape | What changed materially from S1 | Notable observation |
|---|---|---|---|
| **S2: 5-min investor pitch** (`tests/e2e/s2-investor-pitch/`) | 6 slides; shares 5/20/20/20/**35**; recorded demo; ask with milestones | WHAT is "what exists today plus no traction yet"; WHAT IF becomes an ask plus risks plus "if not funded" | **Conflict surfaced before drafting**: the author says "not a startup" (C025) and the sources contain no traction. Recommended reframe: a validation-stage funder. **The funding amount was not supplied**, so the deck carries a flagged placeholder rather than an invented figure. |
| **S3: 45-min workshop** (`tests/e2e/s3-workshop/`) | Nested cycles frame → m1 → m2 → close; **62% hands-on** | HOW becomes participant practice; ethics moves into the frame; the close becomes transfer plus limits | First real use of `cycle`: the auditor validates order per cycle and the renderer labels the slides |
| **S4: speech without slides, 6 min** (`tests/e2e/s4-speech-no-slides/`) | 5 cue cards; verbatim script of **574 words** (about 96 wpm over the slot) | Spoken signposts, one recurring image, a guided imagination exercise instead of a demo, no numbers | The overrun check passes; the personal lines use only source wording |

**Adaptability verdict:** **Pass, in walkthrough form.** Audience and format changed the time shares, the evidence emphasis, the HOW mode, the ask and the use of personal material, not just the theme.

### Failure observed during the walkthroughs (kept on record)

The **first draft of S2 slide 2** contained two unsupported market generalisations, "Most AI drawing tools make the picture" and "Families and educators lack tools…". The ledger cross-reading caught them, and they were replaced with C012 and a statement explicitly labelled as an untested hypothesis.

This matters. Even with the rules in context, the generating model drifts toward plausible pitch language, so the fidelity gate must be enforced, ideally by a tool (roadmap R2).

## 4. Frozen test inputs: what v0.2.0 produced

These were checked against `Wonderland_NLP_Master - Verzija 1.2.md` (T) and `nlp-writing-feedback-motivation-about-danilo-journey.md` (R). Nothing in `examples/` was edited.

| # | Finding in `examples/danilo-wonderland-70-30/` | Detected by | Severity |
|---|---|---|---|
| 1 | `script…:131` "Posmatrao sam…": a plan (R "Mogu posmatrati…") presented as a past observation | Manual fidelity check; string probe | Blocking for a defense |
| 2 | `script…:138`: imagined Lumi T.O.T.E. questions presented as first-prototype behaviour | Manual; string probe | Blocking |
| 3 | `script…:52`: sensory memory ("miris drveta i piljevine", "zvuka alata", "toplote") not in R | Manual; string probe (the "zvuka" inflection was confirmed by reading) | Major (needs the author's consent) |
| 4 | `brief.md:12`: "daily experiments at home… offline parent-child workshops" are not in the sources | Manual; string probe | Major |
| 5 | `evidence.md:14` C008: prototype and adaptive future Lumi merged under `SOURCE` | Manual | Major |
| 6 | `brief.md:8`: audience "parents/educators" marked Explicit 1.0 without a source | Manual | Minor |
| 7 | `review.md:18,23`: rubric dimensions swapped; self-certified READY at 24/24 | Manual; string probe | Major (process) |
| 8 | No research questions anywhere in the deck (T §1.3) | String probe | Major for examiners |
| 9 | 2,313 spoken words = 16.5–19.3 min at 140–120 wpm, before the micro-exercise and the demo, in a 20-minute slot | Word count | Major (time risk) |

The `audit_deck.py` checks (structure, ledger IDs, overrun) **pass** for this example. Its JSON notes are short summaries, and its IDs exist in its own ledger.

That is the key lesson. **Deterministic structure checks cannot catch fidelity failures.** Catching them needs the new review/evidence instructions plus a future checker (R2).

`examples/wonderland/` (English): faithful labelling, a self-review of 21/24 REVISE; missing the research questions (#8).

## 5. Before/after comparison of skill behaviour (by inspection)

| Behaviour | v0.2.0 | v0.3.0 |
|---|---|---|
| "Help me make my thesis presentation" (natural language) | Loads the NLP studio: all 4 pocket exercises plus a 70/30 slot plus a 10-file package | Loads the orchestrator: classify → depth → frontier → only the needed stages |
| A 45-min nested workshop deck | `audit_deck --strict` **fails** ("Slides must follow… order") | Passes with `cycle`s |
| An investor pitch without traction data | No guidance; risk of a fabricated market | Conflict surfaced; UNKNOWN placeholders; reframe options |
| Plugin install reads the knowledge files | Path unresolvable | `${CLAUDE_PLUGIN_ROOT}/knowledge/…` (per the docs; not run live) |

## 6. Remaining unverified behaviour

1. Plugin validation and install in a real `claude` CLI, and discovery of all 16 skills.
2. Natural-language triggering of the orchestrator over the narrower skills (description competition).
3. `AskUserQuestion` rendering, the round length, and the user experience of "skip" and "not sure".
4. Native subagent execution, namespacing, parallelism and reconciliation quality.
5. Quality compared with a single-prompt baseline (roadmap R1).
6. A real presenter rehearsal and audience response.
7. Gemini CLI and Codex runtime behaviour; ChatGPT manual use.
8. PDF/DOCX ingestion (the author's `.docx` and `.pdf` versions exist but weren't used).
9. Accessibility of the rendered HTML with assistive technology.
