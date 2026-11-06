---
name: 4mat-state-anchor
description: "Presenter preparation and delivery coaching: associated mental rehearsal with success criteria, a short state routine (breathing, posture, resource cue, wide-angle gaze), optional stage map for past/present/future and objections, and optional gesture vocabulary, injected as process cues into script and speaker notes."
---

# Presenter state and stage use (`4mat-state-anchor`)

Grounding:
- **Training handout**: mental rehearsal / future pace with evidence of success; state and resource anchoring; breathing and posture; peripheral vision.
- **Research synthesis** (practitioner tradition): stage spatial anchoring; Satir categories used as a gesture vocabulary.

**Target problem**: nerves, reading from notes, flat delivery, stage movement that contradicts the structure.

**Evidence status**:
- Mental practice has supportive performance research, but "programming the outcome" does not.
- Wide-angle gaze helps the presenter scan the room. Claims that it silences internal dialogue or opens "unconscious resources" are unsupported.
- Consistent left-to-right timelines match research on mental timelines in left-to-right reading cultures. "Anchor contamination" effects are unsupported, so present stage zones as theatrical clarity.

Prompts: `knowledge/NLP_POCKET_EXERCISES.md` §6. Resolve the path under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

## 1. Preparation

1. **Mental rehearsal**: run through the talk from your own point of view. Define what success looks, sounds and feels like (attentive faces, real questions, steady breathing). Rehearse the hardest question and the demo failure, not only the ideal run.
2. **State routine** (60–90 seconds): slow breathing, an upright and grounded posture, a personal resource cue (a memory of being calm and competent, chosen by the presenter), and a wide gaze across the room before the first word.

## 2. Stage map (optional; live stage with room to move)

From the audience's point of view, in left-to-right reading cultures:
- **Audience-left**: past, problem, *what if not*.
- **Centre**: Mini What, model, demo.
- **Audience-right**: future, vision, upside.
- **Side spot**: voicing objections, then return to centre to answer.

Mirror the map for right-to-left reading audiences. Skip it entirely for lectern-bound, online or recorded talks.

## 3. Gesture vocabulary (optional)

- Default to **levelling**: open, symmetrical and calm.
- Use warmer, open-palm gestures for empathy moments, and stiller, precise gestures for explaining models.
- In Satir's model, placating, blaming, computing and distracting are *stress stances*. If they are used at all, use them as conscious, brief contrasts, and never direct blaming energy at people.

## Output

A **delivery blueprint**: the rehearsal script, the state routine, the stage map (if used), and concise `[STAGE | GESTURE | PAUSE | TONE]` cues placed in `process_notes` or bracketed in `script.md`, never inside the spoken words.
