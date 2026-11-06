# Gemini CLI guidance

Use the installed 4MAT skills (in `.gemini/skills` or `.agents/skills`) when asked to prepare, adapt or review a presentation. Begin with the `nlp-4-mat` skill. Shared knowledge and scripts are in `.4mat-studio/`.

Gemini CLI has its own `ask_user` tool and its own custom subagents (`.gemini/agents/*.md`). The agent files in this repository are written for Claude Code and have **not** been tested on Gemini CLI, so apply the specialist lenses as separate sequential passes (see `.4mat-studio/knowledge/AGENT_CONTRACT.md` §6). Offer choices with `ask_user` when it is available; otherwise use numbered options. Never imply that Claude-specific tools ran.
