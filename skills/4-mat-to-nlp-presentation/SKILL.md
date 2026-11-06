---
name: 4-mat-to-nlp-presentation
description: "Composable NLP pocket toolkit and interactive 4MAT presentation studio (Mini What -> Why -> What -> How -> What If/If Not). Use whenever designing, researching, storyboarding, scripting, or rehearsing a 4MAT presentation with NLP tools (3+1 Perceptual Positions, Walt Disney Creative Strategy, Dilts' Logical Levels & 70/30 personal-story weaving, Sleight of Mouth reframing, Nested Loops, Yes-Sets, VAKOG cycling, Spatial Stage Anchoring, and Satir postures)."
---

# 4-MAT-to-NLP Presentation Studio (`4-mat-to-nlp-presentation`)

This skill is the primary entry point and composable pocket-skill router for building high-impact, emotionally resonant **4MAT presentations** powered by **Neuro-Linguistic Programming (NLP)**.

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills) ([architecture guide](https://hoangyell.com/matt-pocock-skills-explained/)), this toolkit avoids dumping one rigid, monolithic prompt onto every presentation. Instead, it gives you **small, composable, interactive NLP pocket skills** under the user's explicit control—each targeting a specific cognitive or delivery failure mode across the 4MAT sequence (**Mini What → Why → What → How → What If / What If Not**).

Read `references/nlp-pocket-tools.md` and `references/4mat-architecture.md` (or repository `knowledge/NLP_POCKET_EXERCISES.md`, `knowledge/4MAT_FOUNDATIONS.md`, and `knowledge/NLP_TECHNIQUES.md` when running inside the full repository) for complete exercise protocols and output schemas.

---

## 1. Core Design Principles (The Matt Pocock NLP Pocket Philosophy)

1. **Small, Composable Pocket Skills Over Monoliths:** Every NLP technique is encapsulated as a modular lens that can be triggered standalone (e.g., *"Run the 3 Perspectives tool on my topic"*, *"Run the Disney Strategy on my demo"*) or chained into a full 4MAT pipeline.
2. **User-in-the-Loop Socratic Gates (`/grill-me` style):** Ask 1–3 high-leverage questions at a time to resolve missing decisions (`S1–S8` readiness slots) rather than guessing the speaker's personal stories, audience stakes, or personal-to-methodology ratio.
3. **Dual-Track Separation (Content vs. Process):** Always distinguish **Content (*Sadržaj*)**—what is claimed and its evidence status (`[SOURCE]`, `[INTERPRETATION]`, `[PROPOSAL]`, `[HYPOTHESIS]`, `[UNVERIFIED]`)—from **Process (*Proces*)**—how the presenter manages state, group rapport, spatial stage anchors, nested loops, and sensory language.
4. **Configurable Story-to-Model Ratio (e.g., 70% Personal Journey / 30% Methodology):** When a presenter wants to merge their lived personal journey with a technical or academic model (such as a **70% personal journey / 30% NLP Master model** blend), weave the personal narrative and the formal methodology inside every quadrant rather than segregating them into disconnected halves.

---

## 2. The Composable NLP Pocket Skills Menu

Route to or apply the exact pocket skill needed for the current stage:

| Pocket Skill | Primary NLP Tool & Exercise | Target Failure Mode Fixed | Primary 4MAT Phase(s) |
| :--- | :--- | :--- | :--- |
| **`4mat-perceptual-positions`** | **3+1 Perceptual Positions** (1st: Speaker, 2nd: Listener/Child/Parent, 3rd: Observer/Reviewer, 4th: Systemic Ecology) | Single-perspective blindness; disconnect from audience's lived world | Research, **WHY**, **HOW**, **WHAT IF** |
| **`4mat-disney-strategy`** | **Walt Disney Creative Strategy** (Dreamer / *Sanjar* → Realist / *Realizator* → Constructive Critic / *Analitičar*) | Premature self-criticism killing vision OR ungrounded fantasy lacking a real HOW | Ideation, **WHAT**, **HOW**, **WHAT IF** |
| **`4mat-logical-levels`** | **Dilts' Neuro-Logical Levels** (Environment → Behavior → Capability → Values/Beliefs → Identity → Mission) + **70/30 Weave** | Dry lower-level feature dumps that fail to touch the heart or connect identity to mission | **WHY**, **WHAT**, **WHAT IF** |
| **`4mat-sleight-of-mouth`** | **Sleight of Mouth & Reframing** (Redefine, Intention, Chunk Down, Counterexample, Hierarchy of Criteria) | Defensive Q&A, unaddressed skepticism, or getting stuck on *"Ne mogu / It won't work"* | **WHAT**, **HOW**, **WHAT IF / Q&A** |
| **`4mat-nested-loops`** | **LIFO Nested Story Loops**, **5-Statement Yes-Sets**, Isomorphic Metaphors, Milton vs. Meta-Model, **VAKOG Cycling** | Mid-presentation attention trough (U-shaped curve) and monotone auditory-digital lecturing | **WHY** (open loops) → **WHAT/HOW** → **WHAT IF** (close loops) |
| **`4mat-state-anchor`** | **High Performance State (HPS)**, **Future Pace** Mental Rehearsal, **Peripheral Vision**, **4-Zone Stage Anchoring**, **Satir Postures** | Stage anchor contamination, nervous tunnel vision, and incongruent body language | Pre-talk rehearsal & live stage choreography |

 Alongside the 6 NLP pocket skills, the studio includes the core 4MAT workflow skills: `4mat-start`, `4mat-route`, `4mat-interview`, `4mat-evidence`, `4mat-storyboard`, `4mat-nlp`, `4mat-produce`, `4mat-review`, and `4mat-rehearse`.

---

## 3. Staged Execution Workflow

### Step 1: Triage the 8-Slot Readiness Vector & Blend Ratio
Read all user-supplied documents first. Score each slot as **E** (Explicit), **I** (Inferred—confirm with user), or **M** (Missing—ask user):
- **S1 Outcome (*Ishod*):** Audience observable action/feeling + Presenter personal intention.
- **S2 Audience Profile:** Who is listening, what they care about, and what skepticism they bring.
- **S3 Container & Blend Ratio:** Duration (e.g., 5m, 15m, 20m, 45m), medium (`slides+speech`, `speech only`, `workshop`, `web`), language, and **Personal Journey vs. Core Model ratio** (e.g., 70% personal journey / 30% NLP model).
- **S4 WHY Hook & Open Loops:** Authentic personal stories, metaphors, and 5-statement Yes-Set.
- **S5 WHAT Core Models & Evidence:** Key concepts, visual schema (*Image*), and verified claims (`evidence.md`).
- **S6 HOW Demonstration / Exercise:** Step-by-step live walkthrough, T.O.T.E. loop, or audience micro-exercise.
- **S7 WHAT IF / IF NOT Consequences:** *Towards (KA)* upside, *Away-From (OD)* risks/limits, 6-month Future Pace, and Ecology Check.
- **S8 Voice & Stage Persona:** Tonal warmth, cultural idiom, and stage/delivery setup.

### Step 2: Run the Interactive NLP Pocket Exercises
Before locking the storyboard, run (or present the synthesized output of) the core NLP pocket exercises on the user's material:
1. **Perceptual Positions (`4mat-perceptual-positions`):** Map the topic across 1st, 2nd, 3rd, and 4th positions.
2. **Disney Strategy (`4mat-disney-strategy`):** Separate the Dreamer vision, Realist T.O.T.E. demonstration, and Constructive Critic safeguards.
3. **Logical Levels & 70/30 Bridge (`4mat-logical-levels`):** Map how every personal story (Environment/Behavior/Values/Identity/Mission) bridges into a specific NLP principle (30%) without losing emotional warmth.
4. **Nested Loops & Stage Map (`4mat-nested-loops` + `4mat-state-anchor`):** Design 2–3 open story loops (opened in WHY, closed LIFO in WHAT IF) and assign the 4 physical stage zones (Audience-Left = Past/Problem/*OD*; Center = Present/Model/Demo; Audience-Right = Future/Vision/*KA*; Isolated Flank = Critic).

### Step 3: Build & Verify the 4MAT Presentation Package
Produce the synchronized deliverables (`brief.md`, `nlp-pocket-analysis.md`, `evidence.md`, `storyboard.md`, `script.md`, `presentation.json`, `presentation.html`, `speaker-notes.md`, `qa.md`, and `review.md`):
- Enforce the canonical sequence: **Mini What (5%) → Why (25%) → What (30%) → How (25%) → What If / What If Not (15%)**.
- When `scripts/audit_deck.py` and `scripts/render_deck.py` are available, validate `presentation.json` with `--strict` and render the accessible HTML slide deck and speaker notes.
