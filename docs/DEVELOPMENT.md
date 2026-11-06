# Development notes / tests

## Plugin packaging and discovery

Claude Code accepts a plugin root containing `.claude-plugin/plugin.json`, `skills/<name>/SKILL.md` and `agents/<name>.md`. A local plugin marketplace is declared in `.claude-plugin/marketplace.json` with its plugin `source` set to `./`. Use the installed `claude` CLI to run:

```sh
claude plugin validate .
claude plugin marketplace add .
claude plugin install 4mat-nlp@4mat-studio-marketplace
```

Do not mistake `python scripts/validate_repo.py` for the Claude CLI validator. The Python tests check only file/metadata and example structure.

For manual skill installation, Python copies `skills/` to `.claude/skills`, `.gemini/skills` or `.agents/skills`, and helper resources to `.4mat-studio/`. Claude agents are copied only for target `claude`. If the destination already has identically named skills, default behavior refuses to overwrite; use `--force` after review.

## Project state and human gates

Run `4mat-start` for full interactions. Before `brief.md` lock, don't draft a production deck. Before `storyboard.md` approval, provide two alternatives. Ask for approval at meaningful decisions, not every file operation. Specialist agents analyze distinct facets and send findings back to the orchestrator; they should not race to write shared files. If a harness cannot spawn subagents, apply their prompts as sequential lenses and state the difference.

## Tests

```sh
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/audit_deck.py examples/wonderland/presentation.json --strict
python scripts/render_deck.py examples/wonderland/presentation.json --out /tmp/wonderland-4mat.html
```

Manual tests with a real Claude Code account still needed: (1) plugin validation, (2) slash-command discovery, (3) AskUserQuestion picker, (4) subagent delegation/permissions, (5) actual user-led presentation with sources, and (6) delivery preview accessibility.

## Extensibility

A later production version could add PPTX generation, media assets, a local browser preview server, CI schema validation, multiple speakers, cross-source citation tooling, and user research. Those are not claimed as current features.
