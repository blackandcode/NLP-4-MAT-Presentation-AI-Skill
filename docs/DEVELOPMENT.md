# Development notes

## Plugin packaging

The Claude Code plugin root contains `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `skills/<name>/SKILL.md` and `agents/<name>.md`. Skills and agents reach the shared folders through `${CLAUDE_PLUGIN_ROOT}/knowledge/` and `${CLAUDE_PLUGIN_ROOT}/scripts/`.

```sh
claude plugin validate .
claude plugin marketplace add .
claude plugin install 4-mat-to-nlp-presentation@4mat-studio-marketplace
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
- repository validation: spec-compliant names, references, personal-content lint, orchestrator/alias wiring;
- the e2e scenario decks in `tests/e2e/`.

## Still manual (needs a real Claude Code account)

1. `claude plugin validate`, then install.
2. Natural-language triggering of the orchestrator, and `/4mat-start` alias resolution.
3. AskUserQuestion rendering and round behaviour.
4. Native subagent delegation, namespacing (`4-mat-to-nlp-presentation:<agent>`) and permissions.
5. A full user-led session with real sources, compared against a single-prompt baseline. The protocol is in `IMPLEMENTATION_ROADMAP.md`.
6. Accessibility of the rendered HTML with a screen reader.
