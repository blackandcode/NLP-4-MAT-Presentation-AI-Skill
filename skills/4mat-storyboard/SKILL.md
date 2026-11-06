---
name: 4mat-storyboard
description: "Plan and time a 4MAT talk backward from the audience outcome: two narrative options, explicit bridges, a format-specific shape (incl. nested workshop cycles), realistic minutes."
---

# 4MAT storyboard

**Shared files**: resolve `knowledge/…` under `${CLAUDE_PLUGIN_ROOT}/`, then `.4mat-studio/`, then the repository root. Use `knowledge/4MAT_FOUNDATIONS.md` and `knowledge/FORMATS.md`.

**Inputs**: an approved `brief.md` and `evidence.md` (or visibly marked assumptions). Start from the **final audience outcome** and plan backward.

1. **Post-its**: list independent ideas, facts, examples, demos, limitations, questions and possible closes. Tag each with a claim ID or `PROPOSAL`.
2. **Chunk** from pillars down to examples. Find the single point that connects each pillar to the outcome. Move everything else to a **parking lot** (appendix or Q&A backup).
3. **Two contrasting narratives.** Examples: story-first vs. problem-first; vision-led vs. decision-led; demo-first vs. theory-first. Each one needs a Mini What, an audience-specific WHY, an evidenced WHAT, an actionable HOW and a two-sided WHAT IF. Recommend one, state the trade-off, and let the user choose unless they delegated the choice.
4. **Shape for the format** (see `knowledge/FORMATS.md`):
   - Academic defense: research questions, method, a labelled prototype, limitations, validation plan.
   - Pitch: problem, solution, measured traction, ask, milestones, risks.
   - Workshop: an outer frame plus one mini 4MAT per module (`cycle`), with at least 40% hands-on.
   - No slides: cue cards, spoken signposts, one recurring image.
   - Demo: what to watch for, plus a fallback.
   - Web: one section per 4MAT job.
   - Recorded: chunks of 8 minutes or less.
5. **Storyboard table**: phase (and cycle) | segment | the audience's question | content | claim IDs | HOW activity or visual | minutes | **bridge sentence into the next segment** | signal that it worked.
6. **Time budget.** Start from the 5 / 25 / 30 / 25 / 15 % heuristic and adjust it for the format. Budget speech at about 130 words per minute (110–150) and subtract demo, activity and pause time. Keep Q&A and demo setup inside the total, or state that they sit outside it. Flag any duration that is impossible for the amount of material.
7. **Coherence checks**:
   - Every transition answers the previous phase's question.
   - WHY is re-anchored after heavy WHAT sections.
   - Any personal story serves the subject rather than overshadowing it.
   - The close is a decision, a next step or a reflective question, not only a slogan.

**Output**: `storyboard.md` containing both options (with the chosen one marked), the table, a one-minute phase map, the exact total minutes, and a list of open assumptions.
