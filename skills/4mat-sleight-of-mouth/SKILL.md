---
name: 4mat-sleight-of-mouth
description: "Objection and limiting-belief workshop for presentations: list this audience's strongest objections from the evidence gaps, separate legitimate concerns (answer honestly) from misunderstandings and limiting beliefs (where Sleight of Mouth reframing patterns may help), and write spoken answers with claim IDs for WHAT, HOW, WHAT IF and Q&A."
---

# Objections and reframing (`4mat-sleight-of-mouth`)

Draws on Robert Dilts' *Sleight of Mouth* patterns and on content and context reframing from NLP practitioner training.

**Target problem**: sounding defensive when challenged; overclaiming to cover a limitation; ignoring predictable scepticism.

**Evidence status**: craft. **Never use reframing to dismiss a legitimate safety, privacy, ethics or evidence concern.** Those get a direct, honest answer.

Prompts: `knowledge/NLP_POCKET_EXERCISES.md` §4. Resolve the path under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

## Protocol

1. **Collect objections** from the audience lens (`knowledge/FORMATS.md` §3), the "Cannot claim yet" list in `evidence.md` and its counter-arguments, and anything the presenter fears. Keep the five strongest.
2. **Triage** each one:
   - **Legitimate concern** → answer with evidence, a limitation or a validation plan.
   - **Misunderstanding** → clarify.
   - **Limiting belief or framing problem** → a reframe may help.
3. **Choose one pattern** per reframe-able item:
   - *Redefine*: replace a loaded label with an accurate description.
   - *Positive intention*: acknowledge the protective motive behind the objection, then answer it.
   - *Chunk down*: turn "it can't work" into the smallest testable step.
   - *Counterexample*: a real case where the generalisation fails, and only a real one.
   - *Higher criterion*: appeal to a value both sides share.
   - *Meta-frame*: explain why acknowledging a limitation increases credibility.
4. **Write the spoken answer**: 2–4 sentences with claim IDs, ending with the honest limit where one applies.

**Optional stage cue** (live stage only): voice the objection from a side position, then step back to centre to answer. Present this as theatrical clarity, not as an unconscious "anchor".

## Output

An **objection matrix**: objection | triage | pattern (or "direct answer") | spoken answer | claim IDs | honest limit.

It feeds `qa.md` and the WHAT IF NOT segment.
