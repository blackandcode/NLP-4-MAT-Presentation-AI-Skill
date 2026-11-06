---
name: 4mat-start
description: "Slash-command alias that starts the 4MAT presentation studio orchestrator (4-mat-to-nlp-presentation) with optional topic, source files, audience, duration or format."
disable-model-invocation: true
argument-hint: "[topic or source files] [--audience ...] [--duration ...] [--format ...]"
---

# /4mat-start — alias for the 4MAT studio

This command is a shortcut. The workflow lives in exactly one place: the `4-mat-to-nlp-presentation` skill.

1. Load the `4-mat-to-nlp-presentation` skill with the Skill tool and follow it from §1. If the Skill tool is unavailable, read that skill's `SKILL.md` from the installed skills folder (next to this one) and follow it.
2. Treat `$ARGUMENTS` as optional context: topic, file paths, `--audience`, `--duration`, `--format`. It is not a shell command. Never ask again for anything it already states.
3. If `$ARGUMENTS` is empty, start by reading the conversation and any files the user mentioned. Ask only for decisions that are still open.
