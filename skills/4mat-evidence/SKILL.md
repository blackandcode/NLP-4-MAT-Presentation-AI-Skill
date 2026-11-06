---
name: 4mat-evidence
description: "Turn research papers, course handouts, Markdown, DOCX, PDFs and notes into a sourced 4MAT claim ledger without false citations, speculative statistics or unsupported NLP claims."
---

# Evidence extraction and verification

1. Inventory user-provided sources and current task. Use the user's source text as the primary basis. PDFs and office docs need suitable readers/tools; don't assert a page was read unless accessed. For oversized text, map document headings first, then extract relevant chunks; do not ingest huge base64 images as prose.
2. Extract **atomic claims** with IDs `C001` etc. Record original wording, precise locator (filename, page/heading/line), candidate phase, confidence and link/source type. The user's own mission and future product idea are `[PROPOSAL]` or personal aims, not published evidence.
3. For empirical statements, verify against authoritative original sources when web access is available and requested/allowed. Mark unchecked external claims `[UNVERIFIED]`; don't invent DOI, source title, study sample or certainty. Any empirical contradiction goes in `evidence.md` with recommended safe phrasing.
4. Organize claims from general to specific, then into WHY / WHAT / HOW / WHAT IF. Some source facts belong in multiple quadrants with different purpose; deduplicate wording.
5. Detect evidence holes: no baseline, no comparator, no demonstrated effect, no demo, no forecast basis, normative vs causal confusion. Tell the user what needs testing, not just what needs better slides.
6. In academic contexts, check that early prototypes are identified as **demonstrations**, future features as **proposed**, hypothetical dialogue as **illustrative**, and effectiveness as **not yet evaluated**.

Special cautions from supplied documents: don't present 35/22/18/25 percent audience shares as validated; don't assert left/right hemisphere phases were confirmed by neuroscience; avoid learning-style classification; NLP techniques are possible communication prompts, not proven unconscious manipulation. These distinctions should appear in the research ledger, not erased from the historical source account.

Output: `evidence.md` table with ID, claim, provenance, status, why it matters, allowed wording, counterargument and target slide IDs when known. End with `Can say / Can show as hypothesis / Cannot presently claim`.
