---
name: 4mat-produce
description: "Produce the selected 4MAT delivery artifact (slide storyboard, narrated talk, HTML slides, investor pitch, website outline, or workshop) with speaker notes and evidence labels."
---

# Presentation production — medium-first

Load user-approved `brief.md`, `evidence.md` and `storyboard.md`. Don't invent a new narrative in this step. Follow the order Mini What → WHY → WHAT → HOW → WHAT IF. Adapt proof depth and diction to the audience; retain caution on claimed impacts.

**Delivery contracts**:
- `slides+speech`: write `slides.json` (schema in `knowledge/DELIVERABLES.md` or `.4mat-studio/knowledge/DELIVERABLES.md`), script/speaker notes and a source-key. Each slide has **one headline insight**, at most a few bullets, an optional `diagram` for a visual actually displayed in the HTML slide; the `visual` field gives a production direction only (it is not projected) and timed notes. Use `python scripts/render_deck.py <slides.json> --out <presentation.html>` (or `python .4mat-studio/scripts/render_deck.py ...` after manual installation) if the local renderer exists. This outputs web slides, not a PPTX.
- `speech only`: a full natural spoken script plus 1-page cue cards; include pauses and audience prompts, no forced slide count.
- `web/interactive`: responsive section structure with optional demo interactions, accessibility and fallback when JS/tools fail; every screen serves one 4MAT job.
- `investor pitch`: distinguish market hypothesis from measured traction, include who decides, a credible ask, milestones and risks; no imaginary TAM/ROI.
- `academic defense`: trace thesis to argument, theory, implemented demonstrator, evaluation limits, learning, future tests. Critical reflection is more credible than overstated efficacy.
- `workshop`: provide facilitator guide, timed audience activity, instructions, materials, expected variations, debrief and transfer.

**Dual track**: `speaker_notes` = words to say; `process_notes` = optional presenter actions, such as `[pause for question]` or `[live-demo fallback: screenshot]`; `audience_prompt` = voluntary participation. Clearly mark hypothetical scenarios.

Check exact session-time totals and evidence for all numbers. Create `qa.md` containing hard audience questions and verified/honest responses. Give user real preview files or clear instructions, never claim PDF/PPTX created unless it exists.
