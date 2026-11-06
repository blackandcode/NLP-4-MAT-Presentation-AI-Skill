---
name: 4mat-start
description: "Interactive multi-agent 4MAT presentation orchestrator. Use for full presentations, workshop talks, academic defenses, sales pitches, investor decks, or adapting document corpora into Why/What/How/What-If presentations."
disable-model-invocation: true
argument-hint: "[source files or topic] [--audience ...] [--duration ...] [--medium ...]"
---

# Interactive 4MAT Presentation Studio

Use the available user's message, conversation and supplied files as the project. ` $ARGUMENTS `, if nonempty, supplies optional extra context, **not** a shell command to execute. Do not demand inputs already stated or discoverable by reading files. This is an **interactive co-design session**, not an immediate slide generator unless the user requests direct/autonomous delivery.

## 0. Load method and working contracts

If present, read repository `knowledge/4MAT_FOUNDATIONS.md`, `knowledge/NLP_TECHNIQUES.md`, `knowledge/DELIVERABLES.md`, `knowledge/SOURCES.md` (or `.4mat-studio/knowledge/` for manually installed skills). Portable fallback: use Mini What → Why → What → How → What If (including If Not). Preserve source uncertainty and evidence IDs.

First create a concise progress state: `GATHER → LOCK BRIEF → MAP EVIDENCE → PICK STORY → PRODUCE → REVIEW → REHEARSE`. Don't block a simple request behind unnecessary scaffolding.

## 1. Triage: 8-slot readiness vector

Mark each field E (explicit), I (inferred, needs confirmation), or M (missing):

- S1 outcome: audience action and presenter intent (required)
- S2 audience: role, baseline familiarity, objections/expectations (required)
- S3 duration + delivery medium (required)
- S4 WHY: personal relevance, problem, authentic story or metaphor (optional user preference)
- S5 WHAT: core claims and source/evidence (required for factual presentation)
- S6 HOW: a real demo or application for this medium (required)
- S7 WHAT IF: opportunity, limitations/risks, future next step (required)
- S8 voice: language, style and accessibility preferences (infer or ask)

A missing fact obtainable from provided material is **not** a user question. Claim numbers are never filled by guesses. A user may choose `Use recommended defaults` to confirm all stated inferences or `Continue with assumptions` to proceed provisionally; visibly mark assumptions.

## 2. Interactive decision tree

If available use Claude Code's **AskUserQuestion** capability: 1–3 high-value questions per round, preferably 2–4 concise selectable options plus custom/Other. Present a recommended option explicitly. When unavailable, use readable numbered options and wait for a reply. Do not pretend a visual picker appeared.

**Round 1 / essential lock:** What should the audience *do/understand/decide*? Who is the audience? Duration + medium? If more than 3 fields are unknown, group logically in 2 rounds. Sample medium options: slides+speech, speech only, HTML/web, workshop, investor pitch. Sample outcomes: academic defense, communicate vision, make a decision, teach a skill, invite a pilot. Ask only missing fields.

**Round 2 / differentiated WHY:** Offer 2–3 **contrasting story strategies** with stakes, risks and a recommended direction: personal purpose, audience pain, future vision. Request approval for content that represents the user's personal experience. Never invent a genuine personal anecdote.

**Round 3 / application and close:** Ask user to choose HOW (live demo, narrated recording, worked example, audience action) and close (next-step request, future scenario with pros/cons, reflective question, pilot invitation). Avoid questions for which sourced answers already exist.

In each round show: `Locked`, `Open decisions`, `Recommendation`; the user can say `recommend for me` and skip. No asking for approval at every trivial step.

## 3. Coordinate specialists, not competing writers

At **BRIEF**: if Claude custom subagents are available, delegate `audience-strategist`, `evidence-librarian` and `nlp-coach` independent read-only analyses, in parallel if supported. Give each the same brief path, source directory and task, and require a **short written verdict with file/line citations**. If no delegation support, do the lenses sequentially and say so.

At **STORY**: pass the approved brief + claim ledger to `story-architect` (through the 4MAT sequence) and `experience-designer` (medium-specific audience experience). Their notes may disagree; orchestrator resolves or asks the user about meaningful tradeoffs. **Do not delegate user decisions.**

At **REVIEW**: give completed storyboard/script/deliverable to `devils-advocate`; do not let the original author grade itself as the only review. Integrate critique with objective `scripts/audit_deck.py` or `.4mat-studio/scripts/audit_deck.py` where available.

Recommended handoff artifact for each agent: `{context paths, scoped question, 3 findings, claim refs, risk, recommended action}`. Avoid multiple agents editing the same file concurrently.

## 4. Execute a visible staged workflow

1. Run `4mat-interview` methods and write `brief.md`, recording explicit vs assumed decisions.
2. Run `4mat-evidence` methods and write `evidence.md`, distinguishing direct sources from research synthesis/inference.
3. Run `4mat-storyboard` methods; offer 2 narrative options and a recommended one, then write `storyboard.md` after user choice.
4. Apply `4mat-nlp` selectively. No covert manipulation, fixed 'learner types' or unverifiable neuroscience claims.
5. Run `4mat-produce` for medium; create only deliverables the user chose. If slides, write `slides.json`, render HTML + notes when scripts are available. A `slides.json` is not a `.pptx`.
6. Run `4mat-review` and agent adversarial review; fix critical blockers and show what remains uncertain.
7. Offer `4mat-rehearse` with realistic audience objections and talk-time simulation.

At every phase preserve the 4MAT order, match content to audience and format, and cap claims at available evidence. A user requesting one immediate draft can bypass the interview using explicit provisional assumptions.

## 5. Quality contract

A complete package includes evidence-based story, source/assumption ledger, time-checked phases, actual use in HOW, positive and negative future scenarios, audience-relevant ask, speaker notes when relevant and a candid risk section. **Don't represent a prototype as a tested educational intervention.**
