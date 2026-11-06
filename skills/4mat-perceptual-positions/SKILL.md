---
name: 4mat-perceptual-positions
description: "Interactive NLP perceptual-positions exercise (1st presenter, 2nd each audience or stakeholder, 3rd neutral observer, 4th wider system) to research a presentation topic from several perspectives, sharpen an audience-specific WHY, surface objections and plan the ecology check in WHAT IF."
---

# Perceptual positions (`4mat-perceptual-positions`)

**Target problem**: a talk written from only one point of view. It is either trapped in the speaker's enthusiasm (1st position) or stuck in detached abstraction (3rd position), and it misses how the audience experiences the topic (2nd) or the wider consequences (4th).

**Evidence status**: craft built on general perspective-taking. Second-position statements are **hypotheses** about the audience. Check them with real audience members where possible, and never present them as known feelings.

Prompts: `knowledge/NLP_POCKET_EXERCISES.md` §1. Resolve the path under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

## Protocol

Read the topic and the sources first. Then either guide the presenter through one or two positions per turn, or draft all four from their material and ask them to correct the draft.

1. **1st — presenter**: what made this topic matter to them, *in their own words only*; their outcome; what they fear will be misunderstood. → WHY motive, voice.
2. **2nd — each audience group or stakeholder**: one row per group (for example examiners, investors, teachers, end users). What they already know, care about and doubt; what would make them lean in or pull back. → WHY relevance, objections, HOW usability.
3. **3rd — neutral observer**: which claims are demonstrated, which are proposed, which are hoped for; where the logic jumps; what an independent reviewer would ask. → WHAT structure, limitations.
4. **4th — wider system**: who else is affected over time; unintended consequences; the safeguards needed. → WHAT IF / ecology check.

## Output

A **perceptual-positions table**: position | insight | source pointer, or `HYPOTHESIS` | 4MAT phase it feeds.

Add 2–3 perspective-shifting questions the presenter could ask the audience, worded in plain language without NLP jargon unless the audience is an NLP audience.

Write it to `nlp-plan.md` or show it inline.
