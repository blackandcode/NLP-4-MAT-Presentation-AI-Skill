---
name: 4mat-disney-strategy
description: "Dreamer, Realist and Critic pass for a talk: expand the vision, turn it into a concrete timed HOW demo (a T.O.T.E. loop) and stress-test risks without killing the idea."
---

# Disney creative strategy (`4mat-disney-strategy`)

Robert Dilts' model of Walt Disney's creative process ([NLP University](https://www.nlpu.com/Articles/article7.htm)). It separates **imagining**, **planning** and **critiquing** into distinct "rooms".

**Target problem**: either an inspiring vision with no credible HOW and no WHAT IF NOT, or an idea criticised to death before it has taken shape.

**Evidence status**: craft. Separating idea generation from evaluation is standard ideation practice; this specific method has not been tested for presentation outcomes. Treat the roles as thinking modes, not personality types.

Prompts: `knowledge/NLP_POCKET_EXERCISES.md` §2. Resolve the path under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root.

## Protocol

Keep a strict boundary between the rooms, and ask the presenter to switch position or posture between them.

1. **Dreamer**: "If there were no constraints, what is the most valuable version of this?" "What single image captures it?" No feasibility talk is allowed in this room. → WHY horizon; WHAT IF upside.
2. **Realist**:
   - "What can we actually show or practise in the time available?"
   - "Walk through one **T.O.T.E.** loop: goal (Test) → attempt (Operate) → compare (Test) → continue or stop (Exit)."
   - "What is the fallback if the demo fails?"

   → WHAT model; HOW demonstration.
3. **Critic** (critiques the plan, never the person):
   - "Where could the audience confuse vision with what exists or is proven?"
   - "Who could be harmed, excluded or overruled?"
   - "What will the most sceptical person in the room ask?"

   → WHAT IF NOT; safeguards; `qa.md`.
4. **Synthesis**: take the Critic's points back to the Realist and the Dreamer, and show how honest boundaries make the vision *more* credible.

## Output

A **Disney matrix**: the Dreamer horizon; the Realist steps and one HOW demo blueprint (steps, minutes, fallback); the Critic's safeguards and honest boundaries, with claim IDs; and the role-switch cues the presenter can use on stage.
