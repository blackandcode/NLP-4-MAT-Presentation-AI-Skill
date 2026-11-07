# NLP-4MAT Presentation Studio (`/nlp-4-mat`)

Turn an idea, a thesis, research notes or an existing deck into an **audience-specific, evidence-grounded presentation** with the 4MAT sequence: **Mini What → Why → What → How → What If / What If Not**. NLP-informed communication tools are available, but optional.

It works like a presentation strategist:
1. It reads your material.
2. It asks only the decisions it can't answer, with a recommendation each time.
3. It keeps a claim ledger, so nothing planned or hoped-for is presented as done.
4. It offers two narrative options.
5. It produces only what you ask for: slides, a script, cue cards, a workshop guide, a pitch or Q&A prep.
6. It critiques the result independently before calling it ready.

```text
/nlp-4-mat                                   start, or resume where you left off
/nlp-4-mat help                              all commands
/nlp-4-mat 15-min defense from thesis.pdf    describe what you need
/nlp-4-mat review slides.pdf                 critique an existing deck
/nlp-4-mat pitch | workshop | talk           start with a format
/nlp-4-mat rehearse                          practise timing and hard questions
```

In ChatGPT use `@nlp-4-mat …`, in Codex `$nlp-4-mat …`, and on claude.ai "use nlp-4-mat to …".

## Documentation

| Read | For |
|---|---|
| **[INSTALLATION.md](INSTALLATION.md)** | Installing, updating and removing on Claude Code, claude.ai / Desktop / mobile / Cowork, ChatGPT, Codex and Gemini |
| **[USAGE.md](USAGE.md)** | Your first presentation in a new project folder, all commands, and 35+ use cases |
| [docs/DISTRIBUTION.md](docs/DISTRIBUTION.md) | Maintainers: building packages, publishing to the Anthropic and OpenAI directories, releases |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · [docs/CROSS_PLATFORM.md](docs/CROSS_PLATFORM.md) · [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | How it's built, what works where, how to extend it |
| [VISION_QA_REPORT.md](VISION_QA_REPORT.md) and the companion reports | The quality review: what is verified and what isn't |

## 30-second install (Claude Code, all projects)

Run these inside any Claude Code session:

```text
/plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
/plugin install nlp-4-mat@nlp-4-mat
```

Then start a new session and type `/nlp-4-mat help`. Other tools are covered in [INSTALLATION.md](INSTALLATION.md).

## What's inside

- **14 skills.**
  - `nlp-4-mat`: the single command and orchestrator.
  - Seven workflow skills: `4mat-interview`, `4mat-evidence`, `4mat-storyboard`, `4mat-nlp`, `4mat-produce`, `4mat-review`, `4mat-rehearse`.
  - Six optional NLP tools: `4mat-perceptual-positions`, `4mat-disney-strategy`, `4mat-logical-levels`, `4mat-sleight-of-mouth`, `4mat-nested-loops`, `4mat-state-anchor`.
- **6 read-only specialist agents**, used only when the stakes justify it: `audience-strategist`, `evidence-librarian`, `nlp-coach`, `story-architect`, `experience-designer`, `devils-advocate`.
- **Knowledge** (`knowledge/`): 4MAT method, audience × format playbook, NLP technique selection with evidence status, deliverables and decision-log protocol, agent contract, sources.
- **Tools** (`scripts/`, standard-library Python):
  - `audit_deck.py`: phase order, nested cycles, timing, evidence IDs;
  - `render_deck.py`: accessible HTML slides plus notes;
  - `build_dist.py`: the Claude and ChatGPT/Codex packages;
  - `validate_repo.py`;
  - `install.py`.
- **Packages** (`dist/`, generated): `dist/claude/nlp-4-mat` and `dist/openai/nlp-4-mat`.
- **Examples** (`examples/`): fixed test inputs, not templates. **`tests/e2e/`** has four end-to-end scenarios (an examiner defense, a 5-minute pitch, a 45-minute workshop, a talk without slides).

The architecture is inspired by [mattpocock/skills](https://github.com/mattpocock/skills): small single-purpose skills, a decision-frontier interview, facts gathered by the agent and decisions made by the user, and state kept in files.

## Developing

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/build_dist.py            # after any change to skills/, agents/, knowledge/, scripts/, assets/
python scripts/build_dist.py --check    # dist/ must be up to date before committing
```

License: MIT · Privacy: [PRIVACY.md](PRIVACY.md) (no data collection).
