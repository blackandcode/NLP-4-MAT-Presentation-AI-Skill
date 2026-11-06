# Implementation roadmap

Ordered by impact on the vision. User experience, correctness and output quality come before breadth. No new dependencies are planned unless an item says so.

```
R3 plugin smoke test ──► R1 live acceptance + baseline ──► R7 web-verifying evidence agent
        │                         │
        └──────► R2 fidelity checker ◄┘ (R1 measures its effect)
R4 presenter view / a11y   R5 PDF-DOCX ingestion   R6 platform adapters (after R1)
R8–R10 optional
```

## Done in v0.3.0 (for reference)

- Single orchestrator plus alias.
- De-personalised skills and knowledge.
- Optional, evidence-tagged NLP.
- Agent contract and proportional delegation.
- Decision log with resume, revise and retarget.
- `FORMATS.md`.
- Nested cycles, ledger cross-check and speaking-rate checks.
- Validator lints.
- 24 tests.
- 4 e2e scenarios.

See `GAP_ANALYSIS.md` for the full list.

## R1 — Live acceptance session and single-prompt baseline (P0)

**Goal:** observe the real collaboration, and show that it beats a generic prompt.

**Steps:**
1. Install the plugin (after R3). Start a fresh session in an empty folder that holds copies of the Wonderland sources.
2. Paste the vision's S1 prompt verbatim. Record the full transcript.
3. **Baseline:** in a separate fresh session *without* the plugin, give the same prompt and sources and ask for "an excellent 4MAT presentation".
4. Repeat steps 2–3 for S2 (pitch) and S4 (no slides).
5. Have the presenter, plus one examiner-like reviewer who doesn't know which output is which, score both outputs with the `4mat-review` rubric and the fidelity check.

**Acceptance criteria:**
- The orchestrator triggers from natural language.
- At most 4 questions per round, and none whose answer is in the sources.
- A strategy screen appears before production.
- Zero fidelity blockers in the final output.
- The plugin output beats the baseline by at least 3 rubric points *and* has fewer fidelity errors, in at least 2 of the 3 scenarios.
- Subagents run at Deep depth, and their findings appear in a synthesis table.

**Verification:** commit the transcripts to `tests/live/` with the user's consent, along with a scoring sheet.

## R2 — `scripts/fidelity_check.py` (P0/P1)

**Goal:** deterministic support against plans or illustrations being presented as facts, and against embellished personal stories (G03).

**Design (standard library only):**
- Parse the `evidence.md` table, reading the ID → layer mapping.
- Split `script.md` and the `speaker_notes` into sentences, keeping their `[Cxxx]` tags.
- Flag:
  - (a) a sentence with first-person past-tense or present-capability phrasing tagged with a `planned` or `illustrative` claim;
  - (b) a first-person sentence with no claim ID;
  - (c) an ID with no matching ledger row;
  - (d) optionally, words in an "embellishment watch-list" that the user confirms.
- Language packs: start with an English verb list plus a short Montenegrin/Serbian list (e.g. *posmatrao/la sam*, *uradio sam*, *testirali smo*).

**Acceptance criteria:** it flags issues #1, #2 and #4 from `END_TO_END_TEST_RESULTS.md` §4 on the frozen 70/30 example, and raises no blocker on S1–S4.

**Verification:** unit tests built from those fixtures; `4mat-review` calls it when it is present.

## R3 — Plugin install smoke test (P0)

**Steps:**
1. `claude plugin validate .`
2. `claude plugin marketplace add .`
3. Install.
4. List the skills and agents and confirm all 16 and all 6 are present.
5. Run `/4-mat-to-nlp-presentation:4mat-start` and confirm the alias loads the orchestrator.
6. In the orchestrator, confirm that `${CLAUDE_PLUGIN_ROOT}/knowledge/FORMATS.md` resolves and is read.

**Acceptance criteria:** every step passes; any validator warnings are fixed or documented.

**Verification:** a CI job (GitHub Actions) that runs `validate_repo.py` and the unit tests on every push, plus `claude plugin validate` if the CLI is available in CI.

## R4 — Presenter view, visual assets, accessibility (P2)

- A key toggle in the generated HTML that shows the notes, a phase timer, and the next-slide title. No dependencies.
- An optional `image` field (a local path plus alt text) that is projected, with `audit_deck` requiring alt text.
- An accessibility pass: contrast, focus order, `aria-live` behaviour, `prefers-reduced-motion`.

**Acceptance criteria:** unit tests for alt text and escaping; manual checks with NVDA or VoiceOver documented.

## R5 — PDF/DOCX ingestion (P2)

- Document the supported routes in `4mat-evidence`: the host's PDF reader; DOCX via the host's document skill; or a user-exported Markdown version.
- Test on `Wonderland_NLP_Master - Verzija 1.2.pdf` and `.docx`.

**Acceptance criteria:** the ledger locators cite page numbers for PDFs, and section headings for DOCX.

## R6 — Platform adapters (P2, after R1)

- **Gemini**: an installer option that writes `.gemini/agents/*.md` with mapped tool names. Test it with `gemini skills list` and one session that uses `ask_user`.
- **Codex**: a root `plugin.json` with `$schema`, following the current Codex docs. Test skill discovery from `.agents/skills`.
- **Frontmatter portability**: confirm that Gemini and Codex accept or ignore `disable-model-invocation`. If not, move the flag to a Claude-only overlay.

**Acceptance criteria:** the `docs/CROSS_PLATFORM.md` rows move from "Not tested" to "Tested".

## R7 — Web-verifying evidence agent (P2, after R1)

Add `WebFetch, WebSearch` to the `evidence-librarian` tools, and record in the ledger the URL and the access date for any external claim that was checked.

**Acceptance criteria:** the verified external claims show URLs, and the permission prompts are acceptable in a live session.

## R8–R10 — Optional (P3)

- **R8**: add outcome type, interaction and Q&A placement to `brief_wizard.py`.
- **R9**: Montenegrin/Serbian versions of `FORMATS.md` and the interview prompts.
- **R10**: PPTX export through a host pptx skill when available, keeping JSON as the source of truth.

## Definition of "production-ready"

1. R1–R3 pass.
2. R2 is enforced in `4mat-review`.
3. Two real presenters have used the system end to end, with their rehearsal feedback recorded.
4. The CI is green.
