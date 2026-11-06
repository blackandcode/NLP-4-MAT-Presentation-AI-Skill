# Specialist agent contract

Specialists exist to add **distinct, independent perspectives**. They never make user decisions, never write shared files, and never fill gaps by inventing material.

## 1. Proportionality: when to delegate

| Situation | Specialists |
|---|---|
| Quick outline, short low-stakes talk, single question | None. The orchestrator applies the lenses inline. |
| Standard talk with supplied sources | `evidence-librarian` at BRIEF, `devils-advocate` at REVIEW |
| High stakes (defense, pitch, keynote, large source corpus) | BRIEF: `audience-strategist` ∥ `evidence-librarian` (∥ `nlp-coach` only when delivery or NLP coaching is wanted). STORY: `story-architect` ∥ `experience-designer`. REVIEW: `devils-advocate`. |
| Reviewing an existing deck | `devils-advocate` (∥ `evidence-librarian` if the deck makes factual claims) |

∥ means the agents can run in parallel: their inputs do not depend on each other's outputs. STORY agents need the locked brief and the evidence ledger, and `devils-advocate` needs a complete draft.

## 2. Request (orchestrator → agent)

```
TASK: <one scoped question>
STAGE: brief | story | review
READ: <paths: brief.md, evidence.md, storyboard.md, source files>
LOCKED DECISIONS: <D-IDs with one line each — do not reopen>
OPEN QUESTIONS: <what the orchestrator needs from this lens>
LIMIT: <=500 words, read-only
```

## 3. Report (agent → orchestrator)

```
VERDICT: <one sentence>
FINDINGS:
  1. <observation> — <pointer: path#section, slide ID or claim ID> — confidence H/M/L
  ...
UNKNOWNS: <facts the sources do not contain; never guessed>
RISKS: <what goes wrong if this is ignored>
RECOMMENDATION: <next action>; prefix with USER DECISION: when the choice belongs to the user
CHALLENGE: <optional — D-ID and reason, if a locked decision looks wrong>
```

## 4. Rules for every specialist

- **No invention.** Personal stories, numbers, quotes, study results and audience psychology come only from the supplied material, each with a pointer. Mark anything else `UNKNOWN`.
- **Tense and modality matter.** "I could observe", "we plan" and "imagine" are not "I observed", "we built" and "children did". Never upgrade a plan or illustration into a completed fact.
- **Stay in your lane.** Audience → relevance and outcomes; evidence → claims and sources; NLP → selected communication and delivery techniques; story → narrative and transitions; experience → medium and interaction; devil's advocate → weaknesses and objections.
- **Read-only.** Return findings; the orchestrator writes files.
- **Respect locked decisions.** Do not silently reopen them; use `CHALLENGE:` instead.

## 5. Reconciliation (orchestrator)

1. Build a short **specialist synthesis** table: finding / agents agreeing / conflict / resolution / owner.
2. Factual conflicts → the evidence ledger wins. Taste or strategy trade-offs → present 2–3 options with a recommendation and let the user decide. Record the outcome as a decision (`Dxxx`).
3. Never drop a devil's-advocate BLOCKER silently: fix it, or tell the user why it remains.
4. Show the user what changed because of the specialists. This makes their value visible and checkable.

## 6. Fallback when subagents are unavailable

Run each lens as a **separate pass** in the main conversation. Start each pass with `Lens: <agent-name>` and read the artifacts afresh rather than relying on the draft author's memory. Then tell the user that native subagents were not used. On Gemini CLI, custom subagents (`.gemini/agents/*.md`) exist, but these agent files are written for Claude Code and have not been tested there.
