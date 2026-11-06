# Coordination architecture and executable project contract

## What is implemented

This package defines **nine composable SKILL.md instructions**, **six named, read-only Claude Code custom agents**, two plugin manifests, an interactive terminal fallback, a static slide renderer and deterministic validators. It **does not** include a bespoke multi-agent runtime, a server, an automatic PowerPoint generator or a native web form. Claude Code controls actual agent invocation and optional visual question-picker UI.

## Coordinator state machine

```
NEW REQUEST
   |
   v
S0  Read files, determine goal and available facts
   |  If only review requested, route directly to REVIEW
   v
S1  Interview for essential *decisions*, not discoverable facts
   |  User can choose recommendation, edit, skip with stated assumption
   v
S2  Brief locked (S1/S2/S3/S5/S6/S7 of readiness vector satisfied)
   |  Independent, read-only research lenses (parallel if available)
   v
S3  Evidence ledger: supported facts / hypotheses / proposals / gaps
   |
   v
S4  Story choices → meaningful user selection → approved storyboard
   |  Story architect and experience designer produce scoped proposals
   v
S5  Draft in selected medium, preserve source IDs and time contract
   |
   v
S6  Deterministic audit + independent devil's-advocate report
   |  Must repair severe blockers before claiming readiness
   v
S7  Rehearsal choices (optional) + delivery instructions
```

### Readiness vector

| Slot | Needed? | Default | Decision owner |
|---|---|---|---|
| S1 audience outcome + speaker intent | required | none; ask | user |
| S2 target audience and knowledge | required | unknown until user/source | user |
| S3 medium and duration | required | 15m + slide/talk **only if accepted** | user |
| S4 WHY hook / metaphor / story | flexible | provide 2–3 options | user |
| S5 factual core and evidence | required | extract source or label unknown | evidence agent |
| S6 HOW activity/demo | required | offer medium-specific options | user |
| S7 WHAT IF consequences + decision | required | mark forecast as hypothetical | user + evidence |
| S8 tone/language/accessibility | infer safely | prompt language | user |

**Interactive fallback:** The controller asks through Claude Code's supported picker tool when available, or plain numbered questions. This is intentional rather than implementing a custom UI that other harnesses cannot call.

## Agent contracts and arbitration

`audience-strategist`, `evidence-librarian` and `nlp-coach` can begin together because their scopes do not depend on one another's output. `story-architect` and `experience-designer` begin after approved brief/claims, and their different story vs. medium constraints produce a tradeoff the user can decide. `devils-advocate` starts only after a complete draft exists.

Each agent must return **findings + claim/source pointers + uncertainties + recommendation**; none can approve an audience action, create unsupported statistics, or overwrite a shared artifact. In a Claude Code session the coordinator may invoke them in parallel; on other platforms it applies the same analytic lenses in sequence. The main agent reconciles contradictions explicitly, prioritizing verifiable facts over presentation polish.

For illustrative Wonderland work:

- The audience strategist might recommend opening with the importance of child agency rather than showing the software logo.
- The evidence librarian should reject the statement that children's creativity improved, because no child study has been completed.
- The NLP coach should advise the transparent Meta Model clarification and a TOTE iteration demo, not covert suggestions.
- The story architect orders the WHY/WHAT/HOW/WHAT IF progression around the desired scholarly outcome.
- The experience designer plans a live demo and screenshot fallback.
- The devil's advocate asks how effects will be measured independently and what happens if the tool generates too much itself.

## Runtime and quality limitations

- The declarative skill content depends on the host model following instructions. Static validation of metadata does not demonstrate that it will ask ideal questions.
- Native question UI exists only where the chosen host exposes it; the agent must degrade gracefully.
- A deck can pass deterministic phase/timing checks while still being boring, wrong or inaccessible. Human rehearsal and a source audit are always needed.
- This is an independent skills project, not an official 4MAT or NLP certification.
