# Development notes

## Plugin packaging

The repository root is the **development** plugin (`claude --plugin-dir .`). Its skills reach the shared folders through `${CLAUDE_PLUGIN_ROOT}/knowledge/` and `${CLAUDE_PLUGIN_ROOT}/scripts/`.

**Distribution** uses the generated, self-contained builds in `dist/`:
- the marketplace `source` points at `./dist/claude/nlp-4-mat`;
- ChatGPT and Codex use `dist/openai/…`.

Rebuild with `python scripts/build_dist.py` after any source change. Publishing steps are in `docs/DISTRIBUTION.md`.

```sh
claude plugin validate .
claude plugin marketplace add .
claude plugin install nlp-4-mat@nlp-4-mat
```

`python scripts/validate_repo.py` is not the Claude CLI validator.

## Adding a skill or technique

1. Create `skills/<name>/SKILL.md` with the frontmatter fields `name` (matching the folder, lowercase and hyphenated) and `description` (1024 characters or fewer; say *when* to use it).
2. Keep it single-purpose and under about 80 lines. Put detail in `knowledge/` or in the skill's own `references/` folder.
3. Reference shared files as `knowledge/<FILE>.md`, using the standard resolution line (`${CLAUDE_PLUGIN_ROOT}/` → `.4mat-studio/` → repository root).
4. For a new NLP technique, add a row to `knowledge/NLP_TECHNIQUES.md` with *use when*, *skip when* and its *evidence status*. Create a pocket skill only if the technique needs an interactive protocol.
5. Add the name to `EXPECTED_SKILLS` in `scripts/validate_repo.py`, then run the checks below.
6. Keep generic files free of any one presenter's personal material; the validator lints for this.

## Tests

```sh
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/audit_deck.py examples/wonderland/presentation.json --strict --evidence examples/wonderland/evidence.md
python scripts/render_deck.py examples/wonderland/presentation.json --out /tmp/wonderland-4mat.html
```

The unit tests cover:
- the deck auditor: phase order, nested cycles, time, evidence cross-check, speaking-rate overrun, Mini What share;
- the renderer: escaping, cycle labels;
- the installer;
- repository validation: spec-compliant names, references, personal-content lint, the orchestrator command table;
- the e2e scenario decks in `tests/e2e/`.

## Still manual (needs a real Claude Code account)

1. `claude plugin validate`, then install.
2. Natural-language triggering of the orchestrator; the bare `/nlp-4-mat` vs. `/nlp-4-mat:nlp-4-mat` in a plugin install; sub-command dispatch (`help`, `review`, `pitch` …).
3. AskUserQuestion rendering and round behaviour.
4. Native subagent delegation, namespacing (`nlp-4-mat:<agent>`) and permissions.
5. A full user-led session with real sources, compared against a single-prompt baseline. The protocol is in `IMPLEMENTATION_ROADMAP.md`.
6. Accessibility of the rendered HTML with a screen reader.
