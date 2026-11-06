---
name: 4mat-produce
description: "Produce the chosen 4MAT deliverable from an approved storyboard: HTML slides with notes, script, cue cards, workshop guide, pitch, demo run sheet, web outline or qa.md."
---

# Presentation production (format first)

**Supporting files** are bundled in this skill's `references/` and `scripts/` folders. Schema and gates: `references/DELIVERABLES.md`. Format shapes: `references/FORMATS.md`.

Load the approved `brief.md`, `evidence.md` and `storyboard.md`. **Do not invent a new narrative here.** Keep the 4MAT order and the bridge sentences. Use the author's voice samples from the brief. Cite claim IDs on every factual, personal or numeric statement.

## Delivery contracts (produce only what the user chose)

- **Slides + speech**: `presentation.json` (one headline insight per slide, at most a few bullets, an optional projected `diagram`, a `visual` production note that is *not* projected, timed `speaker_notes`, `evidence_ids`). Render with `python scripts/render_deck.py presentation.json --out presentation.html`. That produces HTML web slides plus `speaker-notes.md`, not a PPTX. Validate with `python scripts/audit_deck.py presentation.json --strict --evidence evidence.md`.
- **Speech without slides**: a natural spoken `script.md` plus `cue-cards.md` (one card per phase: opening line, three beats, transition line, closing line). Signpost every phase aloud. No forced slide count.
- **Academic defense**: trace thesis → research questions → theory → method → demonstrator (labelled) → limitations → validation plan. Critical reflection is more credible than overstated effects.
- **Investor pitch**: separate measured traction from market hypotheses. Include who decides, the specific ask, use of funds, milestones and risks. No imaginary market size or ROI.
- **Workshop**: a facilitator guide with a timed agenda per `cycle`, activity instructions, materials, expected variations, debrief questions and a transfer task.
- **Live demo**: a run sheet with the scripted click path, prepared data, a time box, the pre-frame ("watch for…"), and a fallback (video or screenshots) with the exact line to say if the demo fails.
- **Web / interactive**: section structure (one 4MAT job each), interaction states, accessibility notes, and a no-JavaScript fallback.
- **Recorded / async**: chunked scripts (8 minutes or less each), on-screen signposts, caption-ready text, "pause and try" prompts, and a link-based call to action.

## Speaker notes and process

- `speaker_notes` are the words to say. If they are only cues, label them `CUE NOTES`.
- `process_notes` hold optional presenter actions, such as `[pause]`, `[ask for a show of hands]`, or `[fallback: screenshot 3]`.
- `audience_prompt` holds participation, which is always voluntary.
- Mark hypothetical scenarios and illustrative dialogues as such where the audience can see or hear the label.

## Checks before handing over

1. **Time**: the minutes sum to the duration. Verbatim text ≈ minutes × 130 words, minus demo and activity time. `audit_deck.py` warns about overruns.
2. **Fidelity**: every personal anecdote, prototype capability and result matches its claim ID in tense and modality, with no embellishment.
3. **Q&A**: write `qa.md` containing the hardest questions this audience will ask, honest answers with claim IDs, and explicit limits.
4. **Honest file list**: tell the user exactly which files exist and how to preview them. Never claim a PDF, PPTX or video was created unless it exists.
