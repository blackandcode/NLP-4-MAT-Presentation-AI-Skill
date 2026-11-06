---
name: 4mat-evidence
description: "Turn theses, papers, notes or PDFs into a traceable claim ledger: what exists, what is planned, what is illustrative or hypothetical, with locators, tense checks and gaps."
---

# Evidence extraction and verification

**Supporting files** are bundled in this skill's `references/` and `scripts/` folders. Status vocabulary: `references/4MAT_FOUNDATIONS.md`.

1. **Inventory** the sources: path, type, length, date or version, and whether each one is primary (the author's own work) or external. Only assert you read a page if you actually accessed it. For long documents, map the headings first and then extract the relevant sections. Skip embedded base64 images.
2. **Extract atomic claims** as `C001`, `C002`, …. For each claim record:
   - the original wording (quote short phrases in the source language);
   - an exact locator (file + section/page/heading);
   - the candidate 4MAT phase;
   - the status: `SOURCE`, `INTERPRETATION`, `PROPOSAL`, `HYPOTHESIS` or `UNVERIFIED`.
3. **Separate the layers explicitly**, especially for projects and theses:
   - **Exists now**: what the current prototype or work actually does, in the source's own terms.
   - **Planned or proposed**: future features, programmes, studies.
   - **Illustrative**: imagined dialogues, example scenarios.
   - **Hypothesised effect**: anything about impact or effectiveness that has not been tested.
   - **Personal history**: only what the author wrote or confirmed.
4. **Tense and modality check.** Flag every place where a downstream draft turns "could / would / plan / imagine" into "did / does / proved". Flag any personal anecdote enriched with details the source doesn't contain. These are blocking errors in a defense or pitch.
5. **External claims**: verify against authoritative originals when web access is available and allowed. Otherwise mark them `UNVERIFIED`. Never invent a DOI, title, sample size or effect size.
6. **Contradictions and staleness**: note conflicting statements between sources or versions, and state which one wins and why.
7. **Gaps**: no baseline, no comparator, no demonstrated effect, no working demo, no basis for a forecast, or normative claims confused with causal ones. Say what would need *testing*, not just what needs better wording.
8. **Map to 4MAT**: order the claims from general to specific, then assign them to WHY / WHAT / HOW / WHAT IF. One fact may serve several phases.

**Standing cautions**:
- The 4MAT handout's 35 / 22 / 18 / 25 % audience shares and any hemisphere-phase mapping are historical practitioner claims, not established findings.
- Learning-style matching is unsupported.
- NLP techniques are communication prompts, not proven mechanisms.

## Output: `evidence.md`

A table with columns ID | claim | locator | layer | status | allowed wording | counter-argument | target slides.

After the table, add: source gaps; contradictions; and three closing lists:
- **Can say**
- **Can show as hypothesis or illustration**
- **Cannot claim yet**
