# Routes: the shortest path for each situation

Used by `/nlp-4-mat route` and `/nlp-4-mat help`. Recommend **one** path and **one** alternative, each with a one-line reason, and let the user choose. Never launch a long questionnaire when the outcome, audience, time and format are already clear.

| Situation | Type this | Stages run |
|---|---|---|
| Idea or documents → a new presentation | `/nlp-4-mat <describe it>` | Full orchestration, depth chosen automatically |
| Quick outline only, low stakes | `/nlp-4-mat brief`, then `story` | Interview (one round) → storyboard |
| Source-heavy academic defense | `/nlp-4-mat defense <files>` | Interview → evidence → storyboard → produce → review → rehearse |
| Investor or funding pitch (7 min or less) | `/nlp-4-mat pitch <files>` | Interview → evidence (traction must be measured) → storyboard → produce → rehearse (Q&A on the ask) |
| Interactive workshop or course | `/nlp-4-mat workshop <topic>` | Interview → storyboard with nested cycles → facilitator guide |
| Speech without slides | `/nlp-4-mat talk <topic>` | Interview → storyboard → script + cue cards → rehearse |
| Improve an existing deck or script | `/nlp-4-mat review <file>` | Review → targeted fixes → review again |
| Same project, new audience or format | `/nlp-4-mat retarget <audience/format>` | Reuse the evidence; rebuild the storyboard |
| Change one earlier decision | `/nlp-4-mat revise <decision>` | Regenerate only the stale files |
| Personal story combined with a model or method | `/nlp-4-mat brief`, then `levels` | The user sets the blend; logical levels; storyboard |
| Expected scepticism or hard Q&A | `/nlp-4-mat evidence`, then `objections`, then `qa` | Ledger → objection matrix → drills |
| A vision with no concrete HOW | `/nlp-4-mat disney` | Dreamer / Realist / Critic → storyboard |
| A talk trapped in the speaker's own view | `/nlp-4-mat perspectives` | Four perspectives |
| A flat script, or a long talk with no thread | `/nlp-4-mat loops` | Narrative and language pass |
| Nerves or delivery coaching | `/nlp-4-mat stage`, then `rehearse` | State routine → drills |

In ChatGPT, use `@nlp-4-mat …` instead of `/nlp-4-mat …`. In Codex, use `$nlp-4-mat …`.
