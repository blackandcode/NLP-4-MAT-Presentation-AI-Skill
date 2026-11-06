# Vision QA report — 4MAT NLP presentation skills

**Date:** 2026-11-06
**Reviewed:** v0.2.0 as found (commit `3793872`) → v0.3.0 working tree after this review
**Companion files:** `GAP_ANALYSIS.md`, `ARCHITECTURE_IMPROVEMENTS.md`, `END_TO_END_TEST_RESULTS.md`, `IMPLEMENTATION_ROADMAP.md`

## 1. Summary

**As found (v0.2.0)**, the repository had the right ingredients:
- a faithful 4MAT sequence;
- a strong epistemic vocabulary (`SOURCE / PROPOSAL / HYPOTHESIS`);
- honest platform caveats, a working renderer and auditor;
- a genuinely moving worked example.

But it did **not** yet fulfil the vision, for three structural reasons:

1. **The front door led to the wrong room.** Plain-language requests could only reach `4-mat-to-nlp-presentation`, because `4mat-start` was user-only. That skill forced all the NLP pocket exercises, made one presenter's 70/30 story ratio a readiness slot, and prescribed a fixed 10-file package. The result was an NLP-maximalist pipeline instead of a strategist that chooses what each talk needs.
2. **The generic skills were overfitted to one person.** Six "reusable" pocket skills used the author's grandfather's workshop, children, partner and career as their *protocol*, not as an example. Every user's talk would have been pulled toward that template, and the author's family details shipped in an MIT plugin.
3. **Integrity failed in the flagship example.** Measured against the author's own sources, the 70/30 package presents a *planned* parent observation as already done, presents an *imagined* Lumi dialogue as current prototype behaviour, adds sensory memories that are not in the source, and certifies itself `READY` at 24/24 on a rubric whose dimensions were swapped. This is exactly what the vision says must never happen. (The example is kept unchanged as a test input, at the user's request.)

**After this review (v0.3.0):**
- There is one orchestrator, and every skill is generic.
- NLP selection is optional and evidence-tagged.
- There is a decision log with resume, revise and retarget.
- Plugin-safe resource paths follow the official docs.
- The auditor has gained nested cycles, a ledger cross-check and speaking-rate checks.
- There are 24 unit tests and four contrasting end-to-end scenarios built from the real Wonderland sources.

**The biggest remaining risk** is that nothing has been exercised in a *live* Claude Code session. That covers the picker, native subagents, plugin install, and comparison against a single-prompt baseline. Those rows are marked **Not Verified** below.

## 2. Scores (0–5, conservative)

Basis: repository evidence plus the scenario walkthroughs in `END_TO_END_TEST_RESULTS.md`. The walkthroughs were run by the same model that edited the skills, with simulated user answers, which weakens them as evidence.

| Dimension | v0.2.0 | v0.3.0 | Evidence and caveat |
|---|:-:|:-:|---|
| Original vision alignment | 2 | 3 | NLP-first pipeline and overfitting removed; still unverified with a real user |
| 4MAT methodological fidelity | 3 | 4 | Sequence was correct before; now transitions, nested cycles (tooling plus tests) and format shapes too. The S1–S4 decks show this. |
| Interactive interview quality | 2 | 3 | Decision frontier, facts vs. decisions, recommended-first, skip, "not sure" all designed. **Live picker behaviour Not Verified.** |
| Audience and outcome modeling | 2 | 4 | Know/feel/believe/decide/do, primary/secondary audiences, `FORMATS.md` lenses; S1–S4 change materially by audience and format |
| Skill modularity and composition | 2 | 4 | One orchestrator plus alias; standalone skills; file handoffs; spec-valid names enforced |
| Multi-agent collaboration | 1 | 2 | Contract, proportionality and merged orphans. **No native subagent run, Not Verified.** No baseline comparison. |
| NLP integration and scientific integrity | 2 | 4 | Selection matrix with "skip when" and evidence status; hard exclusions; source misattributions fixed |
| Research ingestion and traceability | 3 | 4 | Layered ledger, tense/modality check, `--evidence` cross-check; a 29-claim ledger built from the real thesis. PDF/DOCX ingestion not exercised. |
| Storytelling and presentation quality | 3 | 3 | The 70/30 script is vivid but not faithful to its sources; the new decks are faithful but less vivid. Audience impact needs rehearsal. |
| Output and artifact usefulness | 3 | 3 | JSON → HTML + notes, cue cards, facilitator guide, Q&A. No PPTX; visuals are directions, not assets. |
| Claude Code integration | 2 | 3 | Fixed `${CLAUDE_PLUGIN_ROOT}` paths, invocation flags, namespacing. **Plugin install Not Verified** (no `claude` CLI on this machine). |
| Cross-platform portability | 2 | 3 | Claims now checked against official docs; copy-install tested for Codex and Gemini layouts; behaviour on those hosts Not Verified |
| Testability and maintainability | 3 | 4 | 9 → 24 tests; validator lints spec names, references, personal content and the alias wiring; e2e fixtures |
| **Total** | **30/65** | **44/65** | |

### Critical failures (independent of the totals)

| # | Failure | Severity | Status |
|---|---|---|---|
| CF1 | Natural language routed to a forced, NLP-maximal 70/30 pipeline (`skills/4-mat-to-nlp-presentation/SKILL.md` v0.2.0 lines 48, 55, 63; `skills/4mat-start` line 4 `disable-model-invocation`) | P0 | **Fixed**: single orchestrator; NLP optional; no default ratio |
| CF2 | In a plugin install, skills pointed at bare `knowledge/…` and `scripts/…` paths that resolve against the user's project, not the plugin | P0 | **Fixed** per the official plugins reference (`${CLAUDE_PLUGIN_ROOT}`); live check pending |
| CF3 | The flagship example misrepresents plans and illustrations as facts and self-certifies (details in §4.8) | P0 for real use | **Reported, not edited** (user decision). The new review and evidence skills target this failure class. |
| CF4 | The author's family names and personal history were embedded in generic, distributable skills | P1 (privacy, reuse) | **Fixed**, and lint-guarded by `validate_repo.py` |
| CF5 | Multi-agent collaboration never executed; two agents were orphans (`perspective-explorer`, `disney-strategist`) | P1 | Merged into `nlp-coach`; **execution still Not Verified** |

## 3. Method

1. Read all 70 repository files, then the author's sources: `Wonderland_NLP_Master - Verzija 1.2.md`, `nlp-writing-feedback-motivation-about-danilo-journey.md`, `4MAT_OCR_kompletno.md`, and the relevant sections of `4MAT Model and NLP Research.md`.
2. Checked platform claims against the official documentation: Claude Code skills, sub-agents and plugins reference; the Agent Skills spec; Gemini CLI skills, tools and subagents; Codex skills and plugins. Studied mattpocock/skills (README plus four SKILL.md files).
3. Ran all Python tooling in a disposable `python:3.12-slim` container, because no host Python is installed.
4. Executed the orchestrator workflow on the real sources for four contrasting scenarios. Audited the outputs with the tools and recorded which steps were simulated.
5. Asked the owner four architecture questions before making structural changes (entry point, personal data, orphan agents, example handling) and followed the answers.

## 4. Findings by vision area

### 4.1 The 4MAT requirement (vision §2)

| Check | v0.2.0 | v0.3.0 |
|---|---|---|
| Understands 4MAT beyond labels | Yes: purpose per phase, storyboarding post-its, backward planning (`knowledge/4MAT_FOUNDATIONS.md`) | Plus explicit transition semantics ("each phase answers the previous one's question") |
| Distinguishes Mini What from WHAT | Yes | Plus a warning when Mini What takes more than 15% of the time (`audit_deck.py`) |
| Starts from the audience outcome | Yes (storyboard step "plan backward") | Plus a know/feel/believe/decide/do outcome in the interview |
| Short and long formats | Heuristic only | `FORMATS.md` shapes; tested at 5, 6, 18 and 45 min |
| Nested cycles for workshops | Mentioned in text, but **the auditor rejected any non-monotonic deck**, so a nested workshop couldn't pass `--strict` | `cycle` field supported, checked per cycle, rendered and tested (S3) |
| No learning-style or hemisphere claims | Good in `knowledge/`; partly undermined in the pocket skills | Hard exclusions; pocket skills corrected |

The **eight-step cycle** is offered as planning vocabulary, which is correct. The handout's 35 / 22 / 18 / 25 % shares are correctly treated as historical claims.

### 4.2 Skills ecosystem (vision §3)

| Finding | Severity | Evidence | Action |
|---|---|---|---|
| Two competing entry points; the one CLAUDE.md names was not model-invocable | P0 | README "Primary entry point" vs. CLAUDE.md "start from /4mat-start"; `4mat-start` `disable-model-invocation: true` | Owner chose `4-mat-to-nlp-presentation` as the orchestrator; `4mat-start` became a 10-line alias |
| Workflow duplicated in two skills, and the copies had drifted | P1 | `4-mat-to-nlp-presentation` and `4mat-start` described different steps | One copy remains |
| Skills reference absent source files by page ("Grounded directly in `4MAT_OCR_kompletno.md` pp. 12–15") | P1 | v0.2.0 `4mat-state-anchor` line 8 | Attribution rewritten; `SOURCES.md` documents which source supports what |
| Misattribution: stage zones, Satir postures and LIFO loops are cited to the handout but come from the AI-style research synthesis | P1 | The handout has no Satir or stage-zone content | Fixed in `SOURCES.md` and the pocket skills |
| No resume, revise or retarget | P1 | No decision log anywhere | Decision log, STALE propagation and retarget mode (`knowledge/DELIVERABLES.md`) |
| No investor, workshop or speech routes in `4mat-route` | P2 | v0.2.0 route list | Added |

Skill sizes (14–69 lines) were already in line with mattpocock/skills (roughly 7–70 lines).

### 4.3 Interactive experience (vision §4)

The v0.2.0 instructions were already good on paper: they read before asking, never re-ask, ask at most 3 questions per round, recommend an option, accept "skip", and fall back to numbered options. What was missing:
- the **facts vs. decisions** split (Pocock's "finding facts is your job");
- a **decision frontier** that lets later questions depend on earlier answers;
- "not sure — recommend";
- a strategy approval screen before production;
- persistence of decisions.

All of these are now specified, and the S1 log shows 9 decisions in 3 rounds with 7 categories of fact *not* asked. **Whether Claude actually renders `AskUserQuestion` well with these instructions is Not Verified.**

### 4.4 Audience and format (vision §5)

v0.2.0 had audience slots and an audience-strategist, but there was no playbook for *how* the content should change. v0.3.0 adds `knowledge/FORMATS.md`: eight format contracts and seven audience lenses, plus a "same project, four audiences" table.

The end-to-end scenarios show material change. The S2 pitch moves 35% of its time into WHAT IF/ask and states "no traction yet". S3 is 62% hands-on, with nested cycles. S4 replaces slides with spoken signposts and a guided imagination exercise.

### 4.5 NLP integration (vision §6)

- **Strength (v0.2.0):** `knowledge/NLP_TECHNIQUES.md` and `LITERATURE_TRIAGE.md` already rejected covert commands, hemisphere claims and learning styles, and cited Pashler 2008 and Sturt 2012.
- **Weakness (v0.2.0):** the pocket skills repeated mechanism claims as fact:
  - "peripheral vision … quiets internal dialogue, opens access to your unconscious" (`4mat-state-anchor` line 24);
  - "the U-shaped attention trough" (`4mat-nested-loops` line 8; the triage file itself says that comes from LLM research);
  - Satir's *placater* stance recommended as "warm empathy".

  NLP was mandatory: "Before locking WHY and WHAT IF … run or offer" (`DELIVERABLES.md` line 18).
- **v0.3.0:** a selection matrix (*use when / skip when / evidence status*), "0–4 techniques; none is valid", a transparency test, hard exclusions, and Satir correctly described as stress stances. The vision's missing topic, **calibration**, has been added.

### 4.6 Multi-agent collaboration (vision §7)

| Check | v0.2.0 | v0.3.0 |
|---|---|---|
| Distinct responsibilities | 6 core plus 2 overlapping | 6 distinct lanes (`docs/ARCHITECTURE.md` table) |
| Actually invoked | Only described; 2 agents referenced nowhere | Invocation points defined per depth; **never executed natively** |
| Compact contracts | Each agent had its own ad-hoc format | Shared request and report contract (`knowledge/AGENT_CONTRACT.md`) |
| Concurrency and dependencies | Described | Described, including the parallel-safe sets |
| Conflict reconciliation | "Orchestrator resolves" | Specialist synthesis table; evidence wins on facts; the user decides trade-offs |
| No invention | Partly | An explicit rule plus a tense/modality rule in every agent |
| Proportional overhead | No | Light: 0 agents · Standard: 2 · Deep: 6 |
| Fallback | Sequential lenses | Same, with fresh-read passes and disclosure |

Whether collaboration *improves on a single-agent baseline* has **not been tested**. `IMPLEMENTATION_ROADMAP.md` R1 defines that experiment.

### 4.7 Research and knowledge (vision §8)

The claim-ledger design was the strongest part of v0.2.0. v0.3.0 adds:
- explicit **layers** (exists / planned / illustrative / hypothesis / personal);
- a **tense and modality check**;
- contradiction handling;
- author **voice samples**;
- the `--evidence` cross-check.

S1 built a 29-claim ledger from the real thesis. It detected the T-vs-R scope tension and the C025 "not a startup" conflict, which surfaced before S2. PDF and DOCX ingestion was not exercised; the sources used were Markdown.

### 4.8 The flagship example as a test input (vision §10)

These were checked against the author's sources. The example is frozen, so nothing was edited.

| # | Issue | Location | Source says |
|---|---|---|---|
| 1 | Plan presented as past | `examples/danilo-wonderland-70-30/script-70-30-emotivni-govor.md:131` "Posmatrao sam šta se desi…" | R/HOW: "Mogu posmatrati…" (*I can observe*, future) |
| 2 | Illustration presented as prototype behaviour | `script…:138` "…izgleda u prvom prototipu…" plus Lumi's T.O.T.E. questions | T §3.1 illustration; prototype = voice → drawing (T abstract, §5.1); dialogues imagined |
| 3 | Embellished memory | `script…:52` "miris drveta i piljevine… zvuka alata, toplote…" | R: only "posmatrao kako od komada drveta nastaje nešto novo" |
| 4 | Plans presented as activities | `brief.md:12` "daily experiments at home… and offline parent-child workshops" | R: workshops are a possibility; no experiments described |
| 5 | Layer merge | `evidence.md:14` (C008) puts the prototype and the adaptive VAKOG/metaprogram Lumi under one `SOURCE` | T §§2.4, 4.1, 6.4: adaptation is a future wish |
| 6 | Audience asserted | `brief.md:8` "parents/educators … Explicit (1.0)" | Not in the sources |
| 7 | Self-certification | `review.md:18,23` swaps rubric dimensions for "70/30 weave", "LIFO loops", "Process cues"; READY at 24/24 | `4mat-review`: "Do not claim 24/24 without rehearsing" |
| 8 | Academic gap | The deck never states the thesis's four research questions | T §1.3 |
| 9 | Time risk | 2,313 spoken words = 16.5–19.3 min at 140–120 wpm, *before* the audience micro-exercise and the demo, in a 20-minute slot | — |

The `examples/wonderland/` (English) fixture is far more faithful: the dialogue is labelled hypothetical, there are no outcome claims, and it reviews itself as REVISE at 21/24. Its main gap is #8, the missing research questions.

### 4.9 Production (vision §9)

- Slides go JSON → accessible HTML (keyboard navigation, ARIA, print CSS) plus Markdown notes.
- Speaker notes are kept separate from slide text, and "visual" is clearly a production note.
- The renderer is honest about not producing PPTX.
- The workshop, cue-card, demo run sheet and recorded-video contracts were added.
- The renderer still has no presenter view and no real image assets (P2).

### 4.10 Technical and platform (vision §11)

The fixed defects are in `GAP_ANALYSIS.md` (P0/P1 rows marked **Fixed**). Platform statements now distinguish *Implemented / Verified against docs / Tested / Not tested* (`docs/CROSS_PLATFORM.md`).

Notable corrections:
- the wrong plugin names in the docs (`4mat-nlp@…`, `/4mat-nlp:4mat-start`);
- stale counts ("nine skills, six agents");
- Gemini CLI *does* have `ask_user` and custom subagents;
- `.codex-plugin/plugin.json` is only a compatibility fallback.

## 5. The final question

> *If an experienced NLP trainer, an excellent storytelling professional, an instructional designer and an expert presentation consultant collaborated to help someone prepare an important presentation, how close is this skill ecosystem to reproducing the quality of that collaboration?*

**About 55–60% of the way, on paper. Unproven in live use.**

The ecosystem now encodes much of what that team would bring:
- the instructional designer's backward planning and phase logic;
- the consultant's audience and format adaptation and Q&A preparation;
- the trainer's toolbox, now applied selectively;
- an evidence discipline stricter than most humans apply.

What it can't yet reproduce:
- a storyteller's *judgement* about which true detail makes a moment land. The 70/30 example shows the model reaching for invented detail instead.
- live calibration with the presenter: rehearsal, voice, presence.
- actual visual design.

And none of the collaboration has been observed in a real session.

**Three strongest aspects**
1. **Epistemic discipline**: the claim ledger with layers, tense checks, evidence IDs on every slide, and a deterministic cross-check.
2. **Faithful, flexible 4MAT method**: backward planning, explicit bridges, format shapes, and nested cycles that are actually enforced by tooling.
3. **Honest tooling**: an auditor, renderer, validator and installer with tests, plus documentation that says what isn't done.

**Five most important weaknesses**
1. No live verification of interaction, subagents or plugin install.
2. Collaboration value is unmeasured: no single-prompt baseline comparison.
3. Story craft drifts toward invented vividness. This was observed in the 70/30 example and, mildly, in the reviewer's own S2 draft.
4. There are no real visual assets and no presenter mode; "visual" is only a text direction.
5. Fidelity checking is instruction-only. No tool compares script sentences with the sources.

**The single highest-impact improvement:** a mandatory, tool-assisted **source-fidelity gate**. Every personal, prototype or result sentence in a script must map to a claim ID whose layer and tense match. This addresses the failure that most damages credibility with examiners and investors.

**The missing capability that most directly blocks the vision:** a **verified live interactive loop**. The vision is a *collaboration*, and until the frontier interview, strategy approval and specialist reconciliation have been observed working in a real Claude Code session, the core promise is unverified.

**What to implement next:** roadmap items R1 (live session test protocol with a baseline comparison), R2 (the fidelity checker script), R3 (plugin install smoke test) and R4 (presenter view and visual assets). See `IMPLEMENTATION_ROADMAP.md`.

**The ultimate acceptance criterion**: *can a user collaborate interactively and emerge with an audience-specific, evidence-grounded, memorable, professional 4MAT presentation that is meaningfully better than a generic prompt?* The answer is **plausibly yes, but not yet demonstrated**. The scenario outputs are clearly more audience-specific and better grounded than a generic prompt typically produces. "Memorable" and "meaningfully better" still need a real presenter, a real audience and a side-by-side comparison.
