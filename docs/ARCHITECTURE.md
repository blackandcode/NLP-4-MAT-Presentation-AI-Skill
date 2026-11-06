# Architecture

## What is implemented

- **16 SKILL.md skills**:
  - one model-invocable orchestrator (`4-mat-to-nlp-presentation`);
  - two user-invoked commands (`4mat-start`, an alias; `4mat-route`, a path recommender);
  - eight workflow skills (`interview`, `evidence`, `storyboard`, `nlp`, `produce`, `review`, `rehearse`);
  - six optional NLP pocket skills.
- **6 read-only Claude Code agents** with a shared request/report contract (`knowledge/AGENT_CONTRACT.md`).
- **Shared knowledge**: method, formats, NLP selection, deliverables and protocol.
- **Python tools** (standard library only): `audit_deck.py`, `render_deck.py`, `validate_repo.py`, `install.py`, `brief_wizard.py`.

There is no bespoke runtime, server, PPTX generator or web form. The host model follows the skill text; Claude Code controls the question picker and subagent invocation.

## Composition rules

These are adapted from mattpocock/skills:

- The **orchestrator** is model-invocable, so plain-language requests reach it.
- **User-invoked commands** (`4mat-start`, `4mat-route`) may load model-invocable skills, but never another user-invoked one.
- **Workflow and pocket skills** are model-invocable, usable on their own, and communicate only through workspace files: `brief.md`, `evidence.md`, `storyboard.md`, and so on.
- **Facts** are found by the agent (or the `evidence-librarian`). **Decisions** are asked of the user, as a decision frontier.

## Orchestrator state machine

```
NEW / ADAPT / RETARGET / REVIEW / REHEARSE / RESUME / SINGLE TOOL
   │  classify, choose depth (Light / Standard / Deep), show stage tracker
   v
GATHER   read all sources; readiness map S1–S8 (E / I / M); facts ≠ decisions
   v
BRIEF    decision-frontier rounds (≤3–4 questions, recommended first) → brief.md + decision log
   │  Deep: audience-strategist ∥ evidence-librarian (∥ nlp-coach)
   v
EVIDENCE claim ledger: exists / planned / illustrative / hypothesis; tense & modality checks
   v
STORY    two narratives → user picks → storyboard.md (bridges, time budget, format shape)
   │  Deep: story-architect ∥ experience-designer → specialist synthesis → user trade-offs
   v
PRODUCE  only the chosen deliverables; audit_deck --strict --evidence
   v
REVIEW   devils-advocate first → fidelity check → rubric → review.md (READY FOR REHEARSAL / REVISE / NOT EVIDENCE-READY)
   v
REHEARSE optional drills
```

**Resume / revise / retarget** follow the protocol in `knowledge/DELIVERABLES.md`. Every artifact carries a status line and the decision IDs it depends on. Changing one decision marks only the dependent artifacts STALE.

## Agents

| Agent | Lane | Stage | Runs alongside |
|---|---|---|---|
| `audience-strategist` | relevance, outcomes, objections | BRIEF | evidence-librarian, nlp-coach |
| `evidence-librarian` | claims, locators, fidelity | BRIEF / REVIEW | audience-strategist |
| `nlp-coach` | technique selection; perceptual-positions, Disney and logical-levels lenses on request | BRIEF / STORY | audience-strategist |
| `story-architect` | two narratives, bridges, timing | STORY | experience-designer |
| `experience-designer` | format, density, interaction, fallbacks | STORY | story-architect |
| `devils-advocate` | independent challenge | REVIEW (before self-scoring) | none |

Specialists are used in proportion to the stakes: none for Light depth, two for Standard, the full set for Deep. The orchestrator reconciles their findings in a specialist synthesis table. Facts follow the ledger; trade-offs go to the user. Without subagents, the same lenses run as separate passes and the user is told.

## Known limits

- Static checks can't show that the model will ask good questions or write a moving talk. Only real sessions can (see `END_TO_END_TEST_RESULTS.md`).
- A native question UI exists only where the host exposes one.
- A deck can pass `audit_deck.py` and still be boring, wrong or inaccessible. Human rehearsal and a source audit are still needed.
- This is an independent project, not an official 4MAT or NLP certification.
