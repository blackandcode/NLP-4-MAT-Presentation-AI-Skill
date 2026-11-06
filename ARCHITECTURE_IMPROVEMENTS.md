# Architecture improvements

> **Naming update (v0.4.0, 2026-11-07):** the orchestrator `4-mat-to-nlp-presentation` and the commands `/4mat-start` and `/4mat-route` were merged into one command, `/nlp-4-mat [command]`, and the plugin was renamed `nlp-4-mat`. This report keeps the names that were current when it was written.

This document records the changes made in v0.3.0 and the reasoning behind each one, plus the proposals that still need approval. The owner approved the four structural decisions on 2026-11-06:
- `4-mat-to-nlp-presentation` is the orchestrator;
- the generic skills are de-personalised;
- the orphan agents are merged into `nlp-coach`;
- the examples are frozen as test inputs.

## 1. Skill responsibilities

```
                    ┌──────────────────────────────────────────────┐
  plain language ─▶ │ 4-mat-to-nlp-presentation   (orchestrator)   │ ◀─ /4mat-start (alias)
                    │ classify · depth · frontier · stages · agents │ ◀─ /4mat-route (path advice)
                    └───────┬──────────────────────────────────────┘
                            │ applies the methods of, and hands off via files
   ┌────────────┬───────────┼────────────┬─────────────┬────────────┬────────────┐
 interview   evidence   storyboard      nlp        produce      review     rehearse
 brief.md   evidence.md storyboard.md nlp-plan.md  deck/script  review.md  drills
                                          │
               pocket skills (optional, diagnosed problem only):
               perceptual-positions · disney-strategy · logical-levels ·
               sleight-of-mouth · nested-loops · state-anchor
```

| Decision | Reasoning |
|---|---|
| **One model-invocable orchestrator**, with user-only commands for the alias and the router | The vision requires that a plain-language request starts the right workflow. The Pocock rule is that a user-invoked skill may call model-invoked skills, but not another user-invoked one. That works only if the workflow lives in a model-invocable skill. |
| **The workflow lives in exactly one file** | v0.2.0 had two diverging copies. The alias now holds no logic, so the two cannot drift again. |
| **Every narrower skill stands alone** and talks only through files | Users can run `4mat-review` on an existing deck, or `4mat-evidence` on a thesis, without the orchestrator. That gives composability without coupling. |
| **Pocket skills only run for a diagnosed problem** | The vision says NLP methods are "potential tools, not a mandatory checklist". Selecting 0–4 techniques keeps talks clean and makes each technique's purpose explicit. |
| **No default story-to-model ratio** | 70/30 was one talk's goal. A default would push every talk toward biography. |
| **Generic skills, with the personal content only in examples** | Reusability and privacy. The validator now lints for it, so it can't regress quietly. |

**Rejected alternatives:**
- Splitting the orchestrator into intake and production skills. That adds hand-off overhead without a demonstrated benefit.
- Turning each NLP technique into its own skill. That multiplies skills without improving outcomes. Techniques live as rows in `NLP_TECHNIQUES.md`, and only the ones that need an interactive protocol get a skill.

## 2. Interaction design

| Element | Design | Why |
|---|---|---|
| Facts vs. decisions | Facts come from reading the sources (or the `evidence-librarian`); decisions are asked | Pocock's grilling principle. It removes questions the documents already answer, and the S1 log shows 7 fact categories that were not asked. |
| Decision frontier | Each round asks only the decisions whose prerequisites are settled, at most 3–4 | Follows the decision tree naturally. Later rounds adapt to earlier answers (investor → traction/ask; workshop → interaction). |
| Option format | Recommended first with a reason, a trade-off when consequential, plus "Other", "not sure — recommend" and "skip" | Matches the vision's sample interaction and keeps the user in control |
| Locked / Assumed / Open after each round | Visible state | The user can see and revise any decision |
| Strategy approval screen | One screen before production | The vision requires inspecting the strategy before slides are produced |
| Decision log (`D001…`) with an `Affects` column | Persistent in `brief.md` | Lets the user revise one decision without losing other work, and resume across sessions |
| Depth levels | Light / Standard / Deep | Keeps simple talks fast |

## 3. Agent coordination

- **Six lanes**: audience, evidence, NLP (with three lenses on request), story, experience, sceptic. Each answers a question no other agent owns.
- **When they run**:
  - Light: none.
  - Standard: evidence + devil's advocate.
  - Deep: BRIEF (audience ∥ evidence ∥ nlp), STORY (story ∥ experience), REVIEW (devil's advocate *before* the self-review).
- **Contract** (`knowledge/AGENT_CONTRACT.md`):
  - one request block (task, stage, read paths, locked decisions, limit);
  - one report block (verdict, findings with pointers and confidence, unknowns, risks, recommendation, optional `CHALLENGE: Dxxx`);
  - a no-invention rule plus a tense/modality rule.
- **Reconciliation**: a specialist synthesis table. Facts follow the ledger; trade-offs go to the user; blockers are never dropped silently; the user is shown what changed because of the agents.
- **Fallback**: separate lens passes with fresh reads, disclosed to the user.

**Proposed next (needs a live test first):** give `evidence-librarian` the `WebFetch` and `WebSearch` tools so it can verify external claims. This was deliberately *not* changed yet: it alters permission prompts inside subagents and should be tried in a live session first.

## 4. Reusable knowledge

| File | New or changed | Role |
|---|---|---|
| `knowledge/FORMATS.md` | **New** | Format contracts × audience lenses; "same project, four audiences"; time and density; interaction and culture |
| `knowledge/AGENT_CONTRACT.md` | **New** | Delegation, request/report, rules, reconciliation, fallback |
| `knowledge/DELIVERABLES.md` | Rewritten | Files on demand; decision log; resume, revise, retarget; schema with `cycle`; gates without NLP |
| `knowledge/NLP_TECHNIQUES.md` | Rewritten | Selection rules; matrix with *use when / skip when / evidence status*; hard exclusions |
| `knowledge/NLP_POCKET_EXERCISES.md` | Rewritten | Generic facilitation prompts |
| `knowledge/4MAT_FOUNDATIONS.md` | Extended | Transition semantics; tense and modality check |
| `knowledge/SOURCES.md` | Rewritten | What each source supports, what is excluded, an attribution rule |

The orchestrator's `references/` folder holds portable summaries, so it still works when `knowledge/` is unavailable.

## 5. Platform adapters

| Concern | Design |
|---|---|
| Shared-file resolution | `${CLAUDE_PLUGIN_ROOT}/` (plugin) → `.4mat-studio/` (copied) → repository root → the skill's own `references/` |
| Claude-specific features | Confined to frontmatter (`disable-model-invocation`, `argument-hint`) and *conditional* instructions ("if `AskUserQuestion` exists…") |
| Gemini CLI | Copy-install to `.gemini/skills`; `ask_user` noted; agents run as sequential lenses until adapted (R6) |
| Codex | Copy-install to `.agents/skills`; plugin manifest documented as a fallback (R6) |
| ChatGPT | Paste the orchestrator plus its references; numbered choices; sequential lenses |

## 6. Tooling

| Tool | Change | Why |
|---|---|---|
| `audit_deck.py` | `cycle` support; `--evidence` cross-check; `--max-wpm` overrun warning; Mini What share warning; HOW also accepts a projected `diagram` | Workshops became possible; traceability and realistic timing became checkable |
| `render_deck.py` | Cycle label on slides and in the notes | Nested sessions stay navigable |
| `validate_repo.py` | Spec-valid names and description length; reference existence; personal-content lint; orchestrator/alias wiring; read-only agents; manifest version parity | Prevents every P0/P1 defect found in this review from returning silently |
| `tests/` | 9 → 24 tests, plus `tests/e2e/` scenario fixtures | Regression safety for the above |

## 7. Proposals awaiting approval (not implemented)

1. **`scripts/fidelity_check.py`** (R2): align each script sentence with its claim IDs, and flag past-tense verbs attached to `planned` or `illustrative` claims, plus any sentence with a personal pronoun but no ID. This deterministic support for G03 is the highest-impact next step.
2. **Presenter view in the HTML** (R4): notes, a timer and a next-slide preview behind a key toggle, still dependency-free.
3. **Gemini agent adapter** (R6): generate `.gemini/agents/*.md` with mapped tool names during install, but only after a live Gemini test.
4. **A possible merge of `4mat-state-anchor` into `4mat-rehearse`**, if usage data shows they are always used together. Not proposed now, because composability is the stated principle.
