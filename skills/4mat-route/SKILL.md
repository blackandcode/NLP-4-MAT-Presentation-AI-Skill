---
name: 4mat-route
description: "Recommend the shortest 4MAT skill path for the user's situation: new presentation, adapting a deck, retargeting to a new audience or format, review only, rehearsal only, or a single NLP technique."
disable-model-invocation: true
---

# /4mat-route — choose the shortest path

Read `$ARGUMENTS`, the conversation and any referenced files before suggesting anything. Recommend **one path** and **one alternative**, each with a one-line reason, then let the user choose. To run a full path, hand over to the `4-mat-to-nlp-presentation` orchestrator.

| Situation | Recommended path |
|---|---|
| Idea or documents → a new presentation | `4-mat-to-nlp-presentation` (full orchestration) |
| Quick outline only, low stakes | `4mat-interview` (one round) → `4mat-storyboard` |
| Source-heavy academic defense | `4mat-interview` → `4mat-evidence` → `4mat-storyboard` → `4mat-produce` → `4mat-review` → `4mat-rehearse` |
| Investor or funding pitch (≤7 min) | `4mat-interview` → `4mat-evidence` (traction must be measured) → `4mat-storyboard` (pitch shape) → `4mat-produce` → `4mat-rehearse` (Q&A on the ask) |
| Interactive workshop or course | `4mat-interview` → `4mat-storyboard` (nested cycles) → `4mat-produce` (facilitator guide) |
| Speech without slides | `4mat-interview` → `4mat-storyboard` → `4mat-produce` (script + cue cards) → `4mat-rehearse` |
| Improve an existing deck or script | `4mat-review` → targeted fixes → `4mat-review` again |
| Same project, new audience or format | the orchestrator's **retarget** mode (reuse evidence; rebuild story with `knowledge/FORMATS.md`) |
| Change one earlier decision | the orchestrator's **revise** mode (only stale artifacts are regenerated) |
| Personal story combined with a model or method | `4mat-interview` (the user sets the blend) → `4mat-logical-levels` → `4mat-storyboard` |
| Expected scepticism or hard Q&A | `4mat-evidence` → `4mat-sleight-of-mouth` → `4mat-rehearse` |
| Vision with no concrete HOW | `4mat-disney-strategy` → `4mat-storyboard` |
| Talk trapped in the speaker's view | `4mat-perceptual-positions` |
| Flat script; long talk with no thread | `4mat-nested-loops` |
| Nerves or delivery coaching | `4mat-state-anchor` → `4mat-rehearse` |

Never launch a long questionnaire when the outcome, audience, time and format are already clear from the prompt or the files.
