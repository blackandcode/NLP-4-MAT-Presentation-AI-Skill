# Gap analysis

**Priorities:** P0 = a fundamental failure or broken critical workflow · P1 = blocks high-quality presentations · P2 = a valuable improvement · P3 = optional.

**Status:** **Fixed** (changed in v0.3.0 and covered by tests where possible) · **Fixed, unverified live** · **Mitigated** · **Open**.

## P0 — Fundamental

| ID | Gap | Evidence (v0.2.0) | Status | Where addressed |
|---|---|---|---|---|
| G01 | Natural-language requests reached the NLP-maximal pipeline, not the documented orchestrator | `4mat-start` had `disable-model-invocation: true`; `4-mat-to-nlp-presentation` lines 48/55/63 forced the pocket exercises, a 70/30 slot and a 10-file package | **Fixed** | `skills/4-mat-to-nlp-presentation/SKILL.md` (sole orchestrator), `skills/4mat-start/SKILL.md` (alias); validator rule |
| G02 | Plugin-installed skills could not find `knowledge/` or `scripts/` | Bare relative paths; the docs require `${CLAUDE_PLUGIN_ROOT}` | **Fixed, unverified live** | A resolution line in every skill and agent; `validate_repo.py` checks that referenced files exist |
| G03 | Plans and illustrations were turned into facts; personal memories were embellished; the example certified itself | `examples/danilo-wonderland-70-30` items 1–9 in `VISION_QA_REPORT.md` §4.8 | **Mitigated**: tense/modality and fidelity rules in `4mat-evidence`, `4mat-review`, the agents and `4MAT_FOUNDATIONS.md`. **Open**: a tool-based checker (R2). The example stays unedited by request. | — |
| G04 | No live verification of the picker, subagents, plugin install, or the end-to-end session | No `claude` CLI on the test machine; no session transcripts | **Open** | Roadmap R1, R3 |

## P1 — Important

| ID | Gap | Status | Where addressed |
|---|---|---|---|
| G05 | One author's family, career and memories were hard-coded into six generic skills and the knowledge files; privacy and reuse risk | **Fixed** | Pocket skills and `knowledge/` generalised; `validate_repo.py` personal-content lint plus test |
| G06 | NLP was treated as mandatory; the 70/30 blend was a readiness slot and a gate | **Fixed** | `NLP_TECHNIQUES.md` selection rules ("0–4; none is valid"); the blend is optional with no default (`4mat-interview`, `4mat-logical-levels`) |
| G07 | Mechanism claims stated as fact in the pocket skills (peripheral vision "quiets internal dialogue", the "U-shaped trough", Zeigarnik, "anchor contamination", Satir placater as "warmth") | **Fixed** | Evidence-status line in each pocket skill; hard exclusions |
| G08 | Stage zones, Satir and LIFO loops attributed to the handout, although they come from the research synthesis | **Fixed** | `knowledge/SOURCES.md` attribution rule; pocket-skill grounding lines |
| G09 | Two orphan agents (`perspective-explorer`, `disney-strategist`), never invoked and overlapping others | **Fixed** (merged into `nlp-coach`, per the owner's decision) | `agents/nlp-coach.md` lenses |
| G10 | No shared agent contract, proportionality or reconciliation procedure | **Fixed, unverified live** | `knowledge/AGENT_CONTRACT.md`; orchestrator §5 |
| G11 | No decision persistence; no way to resume, revise one decision, or retarget | **Fixed, unverified live** | Decision log and STALE protocol in `knowledge/DELIVERABLES.md`; orchestrator §6; S2–S4 exercised retargeting |
| G12 | Nested 4MAT cycles were impossible: the auditor rejected any non-monotonic order | **Fixed** | `cycle` field in `audit_deck.py` and the renderer; four unit tests; S3 |
| G13 | No playbook for how audience and format change content | **Fixed** | `knowledge/FORMATS.md`; S1–S4 |
| G14 | Docs gave the wrong plugin name and namespace (`4mat-nlp`) and stale counts ("nine skills, six agents") | **Fixed** | `docs/*.md`, `README.md` |
| G15 | The review rubric could be swapped to favour the draft; the author reviewed their own work | **Fixed** (instruction level) | `4mat-review`: fixed dimensions, devil's advocate before self-scoring, blocking failures |
| G16 | Never compared with a single-prompt baseline | **Open** | Roadmap R1 |
| G17 | The academic-defense shape omitted the research questions (both examples) | **Fixed** | `FORMATS.md` defense row; `4mat-storyboard`; `4mat-produce`; S1 slide 4 |

## P2 — Valuable

| ID | Gap | Status |
|---|---|---|
| G18 | Speaking-time realism was not checked | **Fixed**: `--max-wpm` overrun warning. Limitation: only meaningful for verbatim notes. |
| G19 | Slide evidence IDs were not cross-checked against the ledger | **Fixed**: `--evidence` plus tests |
| G20 | The HTML has no presenter view (notes, timer, next slide) | Open (R4) |
| G21 | `visual` is a text direction only; no image or asset pipeline | Open (R4) |
| G22 | PDF and DOCX ingestion is untested (the author's DOCX and PDF versions exist) | Open (R5) |
| G23 | Claude-only frontmatter (`disable-model-invocation`, `argument-hint`) is outside the Agent Skills spec | Documented in `docs/CROSS_PLATFORM.md`; Open (R6) |
| G24 | The agents are not adapted to Gemini's `.gemini/agents` tool names | Open (R6) |
| G25 | `brief_wizard.py` lacks the outcome type (know/feel/do), interaction and Q&A fields | Open (minor) |
| G26 | The Codex manifest uses the fallback location (`.codex-plugin/`) | Documented; Open (R6) |
| G27 | No accessibility check of the generated HTML (contrast, screen reader) | Open (R4) |
| G28 | "Calibration / audience feedback" was missing from the techniques | **Fixed** (`NLP_TECHNIQUES.md`) |

## P3 — Optional

| ID | Idea |
|---|---|
| G29 | PPTX export, for example via a pptx skill where the host provides one |
| G30 | Multiple speakers and handovers in the storyboard schema |
| G31 | Local-language versions of `FORMATS.md` and the prompts (the author works in Montenegrin) |
| G32 | Audio rehearsal timing from a recording |
| G33 | An interactive web-presentation template beyond the slide deck |

## Complexity that was removed or avoided

- The forced 10-file package. Deliverables are now chosen per request.
- `nlp-pocket-analysis.md` as a default artifact. It is now an optional `nlp-plan.md`.
- Two duplicated orchestration descriptions, now one.
- Two overlapping agents, now six with distinct lanes.
- No new frameworks or dependencies. All tooling is still standard-library Python.

## Deviations from the vision that remain by design

- The six pocket skills stay separate, as the composability principle intends. `4mat-state-anchor` and `4mat-rehearse` could merge later if usage shows they are always used together.
- The examples are frozen test inputs (the owner's decision). Their known issues are documented, not fixed.
