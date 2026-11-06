# NLP-4MAT Presentation Studio (`/nlp-4-mat`)

A set of composable agent skills that help someone turn an idea, documents or an existing deck into an **audience-specific, evidence-grounded 4MAT presentation**: **Mini What → Why → What → How → What If / What If Not**. NLP-informed communication tools are available, but they are optional.

The architecture is inspired by [mattpocock/skills](https://github.com/mattpocock/skills): small single-purpose skills, a decision-frontier interview ("grill me" style), facts gathered by the agent and decisions made by the user, and state kept in files so later skills (and later sessions) can pick it up.

**Status: v0.4.0.** One command, `/nlp-4-mat`, with sub-commands. 14 skills (the `nlp-4-mat` orchestrator, seven workflow skills, six NLP pocket skills), 6 read-only specialist agents, Claude Code plugin manifests, a portable installer (Claude Code / Gemini CLI / Codex), an HTML slide renderer, a deterministic deck auditor and repository validator, unit tests, and two worked examples that serve as fixed test inputs. See `VISION_QA_REPORT.md` for what has and hasn't been verified.

## Start here: one command

```text
/nlp-4-mat                                    start, or resume where you left off
/nlp-4-mat help                               show all commands
/nlp-4-mat 15-min defense from thesis.md      describe what you need; anything that isn't a command is a request
/nlp-4-mat review slides.pdf                  check an existing deck
/nlp-4-mat pitch | workshop | talk | defense  start with a format preset
/nlp-4-mat rehearse                           timing and hard-question drills
```

| Host | Syntax |
|---|---|
| Claude Code | `/nlp-4-mat …` |
| ChatGPT | `@nlp-4-mat …` |
| Codex | `$nlp-4-mat …` |
| claude.ai or Cowork | Just say "use nlp-4-mat to …" |

In a Claude Code plugin install, the bare `/nlp-4-mat` works unless another command has the same name. Then use `/nlp-4-mat:nlp-4-mat`. The full command list is in [skills/nlp-4-mat/SKILL.md](skills/nlp-4-mat/SKILL.md).

You can also just say what you need in plain language, for example *"Help me turn my thesis and these notes into a 15-minute defense for my examiners"*. The **`nlp-4-mat`** skill is the single entry point. It:

1. reads everything you supplied before asking anything;
2. asks only the decisions still open, in short rounds with a recommended option first;
3. builds a claim ledger that separates *what exists now*, *what is planned* and *what is hoped*;
4. offers two narrative options and lets you choose;
5. produces only the deliverables you ask for;
6. runs an independent critique before calling anything ready.

## Install

**The full guide covering every platform and both global directories is [docs/DISTRIBUTION.md](docs/DISTRIBUTION.md).**

| Where | How |
|---|---|
| Claude Code (any machine) | `claude plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill`, then `claude plugin install nlp-4-mat@nlp-4-mat` |
| claude.ai web, Desktop, mobile, Cowork | Customize → Plugins → Upload plugin: `dist/zips/claude-plugin-…zip` (build with `python scripts/build_dist.py --zips`). Skills you enable there also sync into Claude Code. |
| Everyone on Claude | Anthropic directory: claude.ai/directory/manage, plugin path `dist/claude/nlp-4-mat` |
| ChatGPT desktop / Codex | `dist/openai/personal-marketplace.json` → `~/.agents/plugins/marketplace.json`, or `codex plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill` |
| Everyone on ChatGPT (web, desktop, mobile) | OpenAI Plugin Directory: platform.openai.com/plugins → upload `dist/zips/openai-plugin-…zip` |

`dist/` is generated from the sources by `scripts/build_dist.py`. Every skill there is self-contained: it bundles its own references and scripts.

For a guaranteed bare `/nlp-4-mat` in Claude Code, you can also copy-install the skills into your user scope (`~/.claude/skills`) with `python scripts/install.py --target claude --scope user`.

### Copy into a project or user scope

```bash
python scripts/install.py --target claude --scope project --destination /path/to/project
python scripts/install.py --target gemini --scope project --destination /path/to/project   # .gemini/skills
python scripts/install.py --target codex  --scope project --destination /path/to/project   # .agents/skills
```

The installer copies skills, the shared `knowledge/` and `scripts/` folders (into `.4mat-studio/`), and, for the Claude target only, the agents. See `docs/CROSS_PLATFORM.md` for what each platform does and doesn't support.

## Skills

| Skill | Role |
|---|---|
| **`nlp-4-mat`** | The one command. Sub-commands (`help`, `new`, `status`, `review`, `pitch`, `workshop`, `rehearse`, `route` …) or free text. Orchestrates: classify → readiness map → decision-frontier interview → stages → specialists in proportion to the stakes → resume, revise or retarget |
| `4mat-interview` | Separates facts from decisions; progressive rounds; writes `brief.md` with a decision log |
| `4mat-evidence` | Claim ledger: locators, exists / planned / illustrative / hypothesis layers, tense and modality checks, gaps |
| `4mat-storyboard` | Backward planning from the outcome, two narratives, bridges, format shapes, time budget |
| `4mat-nlp` | Selects 0–4 transparent techniques for diagnosed problems ("none" is valid) |
| `4mat-produce` | Slides (JSON → HTML), script, cue cards, workshop guide, pitch, demo run sheet, web, recorded, `qa.md` |
| `4mat-review` | Independent challenge, source-fidelity check, fixed 12-dimension rubric, deterministic audit |
| `4mat-rehearse` | Timing estimate, audience-specific Q&A drills, demo-failure drills |

**NLP pocket skills**, each optional and each targeting one diagnosed problem:

| Pocket skill | Problem it targets |
|---|---|
| `4mat-perceptual-positions` | A one-sided talk |
| `4mat-disney-strategy` | A vision with no HOW, or an idea criticised too early |
| `4mat-logical-levels` | Features disconnected from meaning; optional story-to-model blend at the ratio you choose |
| `4mat-sleight-of-mouth` | Objections and a defensive Q&A |
| `4mat-nested-loops` | A flat script, or a long talk with no thread |
| `4mat-state-anchor` | Nerves and delivery |

**Agents** (read-only; used only when the stakes justify it): `audience-strategist`, `evidence-librarian`, `nlp-coach`, `story-architect`, `experience-designer`, `devils-advocate`. Their shared contract is in `knowledge/AGENT_CONTRACT.md`.

## Knowledge

| File | Purpose |
|---|---|
| `knowledge/4MAT_FOUNDATIONS.md` | Method, transitions, proof-status vocabulary |
| `knowledge/FORMATS.md` | Audience × format playbook: changing either one changes the content, not just the theme |
| `knowledge/NLP_TECHNIQUES.md` | Selection matrix with "skip when" and an honest evidence status |
| `knowledge/NLP_POCKET_EXERCISES.md` | Facilitation prompts for the pocket skills |
| `knowledge/DELIVERABLES.md` | Workspace files, decision log, resume and revise protocol, JSON schema, gates |
| `knowledge/SOURCES.md`, `knowledge/LITERATURE_TRIAGE.md` | Provenance and credibility triage |

## Examples (fixed test inputs, not templates)

- `examples/wonderland/`: a 15-minute English academic-defense fixture.
- `examples/danilo-wonderland-70-30/`: one presenter's real 20-minute defense package. The *70% personal / 30% model* blend was that talk's own goal; it is not a default.
- `tests/e2e/`: scenario outputs from the end-to-end evaluation (5-minute investor pitch, 45-minute workshop with nested cycles, speech without slides, 15-minute examiner defense).

## Local checks

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
python scripts/audit_deck.py examples/wonderland/presentation.json --strict --evidence examples/wonderland/evidence.md
python scripts/render_deck.py examples/wonderland/presentation.json --out /tmp/wonderland.html
```

`validate_repo.py` checks structure, spec-compliant names, file references and the absence of personal content in generic files. It does not replace `claude plugin validate`, and it cannot tell whether the model will ask good questions. See `END_TO_END_TEST_RESULTS.md`.
