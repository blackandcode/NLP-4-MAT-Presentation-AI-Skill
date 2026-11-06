---
name: 4mat-logical-levels
description: "Align a talk across Dilts' logical levels (environment to purpose) and, only on request, braid a personal story with a model at the ratio the user picks."
---

# Logical levels and story-to-model blend (`4mat-logical-levels`)

Robert Dilts' logical levels ([SkillsYouNeed overview](https://www.skillsyouneed.com/lead/logical-levels.html)).

**Target problem**: a talk stuck at feature level (environment and behaviour) that never reaches why it matters, or personal stories that float free of the model or method being presented.

**Evidence status**: craft. This is a reflection scaffold; the hierarchy itself is not empirically validated.

Prompts: `knowledge/NLP_POCKET_EXERCISES.md` §3. Resolve the path under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

## 1. Alignment protocol

Map the topic, and when relevant the presenter's own journey, across the levels, citing a source pointer for every concrete item:

1. **Environment**: where and when does this happen?
2. **Behaviour**: what does someone actually do?
3. **Capabilities**: which strategies, skills or models make it work?
4. **Beliefs and values**: why does it matter? What is assumed to be true?
5. **Identity**: who is the presenter in this story? Who could the user or audience become?
6. **Purpose**: for whom, and in service of what larger aim?

Look for **gaps**, such as a purpose with no demonstrated behaviour, or features with no stated value. These become storyboard fixes.

## 2. Story-to-model blend (only on request)

- The **user sets the ratio**. Common options are model-led (about 20% story), balanced (about 50%) and story-led (about 70% story). There is no default. Recommend based on the audience; for example, academic panels usually need the model to stay clearly visible.
- **Braid inside each phase** instead of putting the biography first and the theory last. Use the beat sequence *lived moment → reflection → named model or demonstration → what it means for the audience*.
- **Fidelity**: use only experiences the presenter supplied or confirmed, in their words. Don't add sensory, emotional or biographical detail without their approval. Don't present plans as experiences.

## Output

A **level-alignment table**: level | content | source pointer | 4MAT phase or slide.

If a blend was requested, add a per-phase table showing the story beat, the model beat and the share of time each gets.
