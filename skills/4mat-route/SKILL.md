---
name: 4mat-route
description: "Recommend which 4MAT or NLP pocket skill sequence to use when the user has a topic, personal journey, manuscript, speech, slide deck, workshop, or existing presentation for review."
disable-model-invocation: true
---

Given `$ARGUMENTS` and the user's current task, inspect available sources before asking questions. Present **one recommended path** and one reasonable alternative, keeping the user in control at every gate.

## Composable Routing Paths

- **Full 4MAT + NLP Presentation Studio (Master Entry):** `4-mat-to-nlp-presentation` (or `4mat-start`).
- **70% Personal Journey / 30% Methodology Emotional Presentation:** `4mat-logical-levels` → `4mat-perceptual-positions` → `4mat-nested-loops` → `4mat-storyboard` → `4mat-produce` → `4mat-state-anchor`.
- **Deep Topic & Empathy Research (3+1 Perspectives):** `4mat-perceptual-positions`.
- **Vision Expansion & Practical HOW Design (Dreamer / Realist / Critic):** `4mat-disney-strategy`.
- **Objection Handling & Reframing Limiting Beliefs:** `4mat-sleight-of-mouth`.
- **Opening Hook, Yes-Sets, Metaphors & LIFO Story Loops:** `4mat-nested-loops`.
- **Stage Presence, HPS State, Spatial Anchoring & Satir Postures:** `4mat-state-anchor`.
- **Academic / Source-Heavy Defense:** `4mat-evidence` → `4mat-disney-strategy` → `4mat-storyboard` → `4mat-produce` → `4mat-review`.
- **Audit & Repair an Existing Deck:** `4mat-review` + `4mat-sleight-of-mouth`.
- **Live Rehearsal & Q&A Simulation:** `4mat-rehearse` + `4mat-state-anchor`.

Never automatically launch a long questionnaire if time, medium, outcome, and personal-to-model ratio are already clear from the prompt or files.
