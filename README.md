# 4-MAT-to-NLP Presentation Studio (`4-mat-to-nlp-presentation`)

A composable **NLP Pocket Skills & 4MAT Presentation Studio** for researching, designing, storyboarding, scripting, testing, and rehearsing emotionally resonant presentations using the 4MAT sequence: **Mini What → Why → What → How → What If / What If Not**.

Inspired architecturally by [mattpocock/skills](https://github.com/mattpocock/skills) ([explained by Hoang Yell](https://hoangyell.com/matt-pocock-skills-explained/)), this repository keeps skills **small, composable, interactive, and under the user's control**—targeting specific cognitive and presentation failure modes rather than forcing everything through one monolithic prompt.

**Status:** v0.2 (`4-mat-to-nlp-presentation`). Ships **16 composable Markdown skills** (including the primary `4-mat-to-nlp-presentation` orchestrator and 6 dedicated NLP pocket tools), **8 specialist subagents**, Claude and OpenAI-compatible plugin manifests, portable installers (`claude`, `gemini`, `codex`), a browser slide renderer, deterministic presentation checks, the English `examples/wonderland/` fixture, and the full **70% Personal Journey / 30% NLP Master** emotional presentation package (`examples/danilo-wonderland-70-30/`).

---

## Quick Start — Claude Code Plugin (Recommended)

```bash
# From this repository's parent directory after cloning/unzipping:
claude plugin validate ./4-mat-to-nlp-presentation
claude plugin marketplace add ./4-mat-to-nlp-presentation
claude plugin install 4-mat-to-nlp-presentation@4mat-studio-marketplace

# Inside a session:
/4-mat-to-nlp-presentation:4-mat-to-nlp-presentation
# or invoke any composable pocket skill directly:
/4-mat-to-nlp-presentation:4mat-perceptual-positions
/4-mat-to-nlp-presentation:4mat-disney-strategy
/4-mat-to-nlp-presentation:4mat-logical-levels
```

### Alternative — Copy Skills and Agents into a Project or User Scope

```bash
python scripts/install.py --target claude --scope project --destination /path/to/project
# or for Gemini CLI / Codex:
python scripts/install.py --target gemini --scope project --destination /path/to/project
python scripts/install.py --target codex --scope project --destination /path/to/project
```

---

## Composable Skill Inventory (16 Skills)

### Master Entry & Workflow Skills

| Skill | Invocation | Role |
| :--- | :--- | :--- |
| **`4-mat-to-nlp-presentation`** | `/4-mat-to-nlp-presentation` | Primary entry point & composable NLP pocket-skill studio |
| **`4mat-start`** | `/4mat-start` | Full interactive 8-slot Socratic orchestrator |
| **`4mat-route`** | `/4mat-route` | Recommend the minimal workflow or NLP pocket skill chain |
| **`4mat-interview`** | `/4mat-interview` | Elicit brief, audience, constraints, and personal-to-model ratio |
| **`4mat-evidence`** | `/4mat-evidence` | Source mapping and epistemic claim ledger (`C001`, etc.) |
| **`4mat-storyboard`** | `/4mat-storyboard` | 5-phase / 8-step 4MAT narrative and timing architecture |
| **`4mat-nlp`** | `/4mat-nlp` | Dual-track Content + Process NLP integration hub |
| **`4mat-produce`** | `/4mat-produce` | Produce slides JSON, HTML deck, verbatim script, workshop, or pitch |
| **`4mat-review`** | `/4mat-review` | 12-dimension quality gate & deterministic audit |
| **`4mat-rehearse`** | `/4mat-rehearse` | Speaker rehearsal, timing check, and skeptical Q&A |

### Composable NLP Pocket Skills (Matt Pocock Style)

| Pocket Skill | Core NLP Framework | Failure Mode Prevented |
| :--- | :--- | :--- |
| **`4mat-perceptual-positions`** | **3+1 Perceptual Positions** (1st: Speaker, 2nd: Listener/Child/Parent, 3rd: Observer, 4th: Ecology) ([Global NLP](https://globalnlptraining.com/simply/the-4th-perceptual-position-of-nlp/)) | Single-perspective blindness; disconnect from audience's lived world |
| **`4mat-disney-strategy`** | **Walt Disney Creative Strategy** (Dreamer / *Sanjar* → Realist / *Realizator* → Critic / *Analitičar*) ([NLP University](https://www.nlpu.com/Articles/article7.htm)) | Premature self-criticism killing vision OR ungrounded fantasy lacking a real HOW |
| **`4mat-logical-levels`** | **Dilts' Neuro-Logical Levels** + **70/30 Personal Story-to-Model Weave** ([SkillsYouNeed](https://www.skillsyouneed.com/lead/logical-levels.html)) | Dry lower-level technical talks that fail to touch the heart or connect identity to mission |
| **`4mat-sleight-of-mouth`** | **Sleight of Mouth & Reframing** (Redefine, Intention, Chunk Down, Counterexample, Hierarchy of Criteria) | Defensive Q&A, unaddressed skepticism, or getting stuck on *"Ne mogu / It won't work"* |
| **`4mat-nested-loops`** | **LIFO Nested Story Loops**, **5-Statement Yes-Sets**, Metaphors, Milton/Meta Balance & **VAKOG Cycling** | Mid-presentation attention collapse (U-shaped curve) and monotone lecturing |
| **`4mat-state-anchor`** | **High Performance State (HPS)**, **Future Pace**, **180° Peripheral Vision**, **4-Zone Stage Anchoring**, **Satir Postures** | Stage anchor contamination, nervous tunnel vision, and flat delivery |

---

## Worked Examples Included

1. **`examples/danilo-wonderland-70-30/` (70% Personal Journey / 30% NLP Master Emotional Presentation Package):**
   - Merges Danilo's personal journey (`nlp-writing-feedback-motivation-about-danilo-journey.md` — 70%: Grandfather's wooden workshop, mentoring ~200 engineers without making copies, parenting Ogi and Aleksa with Vesna and living *"Mapa nije teritorija"*, 2 years of parent conversations, *Kreativni geni* workshops, and gifting a child their preserved creative world at age 18) with his NLP Master thesis (`Wonderland_NLP_Master - Verzija 1.2.md` — 30%: Wonderland, Wonder Creator, Lumi the owl, Disney Strategy, T.O.T.E., 3 Perceptual Positions, Meta/Milton Models, Sleight of Mouth, and Dilts' Logical Levels).
   - Includes `brief.md`, `nlp-pocket-analysis.md`, `evidence.md`, `storyboard.md`, `script-70-30-emotivni-govor.md`, `presentation.json`, `presentation.html`, `speaker-notes.md`, `qa.md`, and `review.md`.
2. **`examples/wonderland/` (English Academic Defense Baseline Fixture):**
   - 15-minute, 10-slide baseline fixture used by automated regression tests.

---

## Local Generation and Testing

```bash
python scripts/validate_repo.py
python scripts/audit_deck.py examples/wonderland/presentation.json --strict
python scripts/audit_deck.py examples/danilo-wonderland-70-30/presentation.json --strict
python scripts/render_deck.py examples/danilo-wonderland-70-30/presentation.json --out examples/danilo-wonderland-70-30/presentation.html
python -m unittest discover -s tests -v
```
