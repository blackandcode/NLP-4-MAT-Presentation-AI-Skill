# Claude Code instructions — 4MAT NLP Skills

For any task to design, adapt, retarget, rehearse, audit or render a 4MAT presentation, start from the orchestrator skill `nlp-4-mat` (users type `/nlp-4-mat [command]`, and `/nlp-4-mat help` lists the commands), or from a narrower skill when the user asks for one step only.
Use the project files under `skills/`, `agents/` and `knowledge/` when they are available.
When tools permit, use AskUserQuestion for interactive single- or multiple-choice decisions. Never assume that a question tool is present.
Parallel agents can research and critique independently, but they must not make irreversible decisions for the user. Review all agent disagreements in the main conversation.
Source claims in the academic example must distinguish an existing early prototype, a future vision and untested research hypotheses.
`examples/` are fixed test inputs: report problems found in them, but do not edit them. Keep `skills/`, `agents/` and `knowledge/` generic; personal stories belong only in examples.
`dist/` is generated: never edit it by hand. After changing `skills/`, `agents/`, `knowledge/`, `scripts/`, `assets/` or `distribution/config.json`, run `python scripts/build_dist.py` and commit the result (`--check` detects a stale build). Keep every skill description at 200 characters or fewer, because claude.ai rejects longer ones. See `docs/DISTRIBUTION.md`.
