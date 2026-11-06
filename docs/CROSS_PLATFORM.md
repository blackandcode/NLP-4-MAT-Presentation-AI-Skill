# Cross-platform support matrix

Status key: **Implemented** (the files exist), **Verified** (checked against official documentation on 2026-11-06), **Tested** (exercised end to end on that platform), **Not tested**.

| Capability | Claude Code | Gemini CLI | Codex CLI | ChatGPT (chat) |
|---|---|---|---|---|
| SKILL.md discovery | Implemented; Verified (`skills/<name>/SKILL.md` in a plugin, or `.claude/skills`) | Implemented; Verified (`.gemini/skills` or `.agents/skills`; `.agents` takes precedence) | Implemented; Verified (`.agents/skills`, repo or user scope) | No skill discovery; paste the skill text |
| Orchestrator from natural language | Implemented (model-invocable); **Not tested** in a live session | Not tested | Not tested | Manual |
| Slash invocation | `/4-mat-to-nlp-presentation:4mat-start` (plugin) or `/4mat-start` (copied); Not tested | Not tested | Not tested | n/a |
| Multiple-choice picker | `AskUserQuestion` when exposed; Not tested here | `ask_user` exists (Verified); Not tested | Not verified | Numbered options |
| Custom subagents | 6 agent files; Verified format; **Not tested** live | Gemini has `.gemini/agents/*.md` (Verified), but these files have not been adapted or tested | Not verified | No; sequential lenses |
| Sequential-lens fallback | Yes (skill text) | Yes | Yes | Yes |
| Shared files | `${CLAUDE_PLUGIN_ROOT}` (Verified substitution in skill and agent bodies) or `.4mat-studio/` | `.4mat-studio/` | `.4mat-studio/` | Upload |
| Deck audit / render | Python 3 standard library; Tested (unit tests) | same | same | Where code execution is available |
| PPTX / PDF export | Not bundled (print to PDF from the browser) | same | same | same |

## Platform notes

- **Frontmatter portability**: the Agent Skills spec allows `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. This repository also uses the Claude-specific `disable-model-invocation` and `argument-hint` fields on `4mat-start`, `4mat-route` and the orchestrator. Claude ignores unknown fields; other hosts may ignore them or warn. Names follow the spec (lowercase, hyphens, 64 characters or fewer, matching the directory) and descriptions stay at 1024 characters or fewer. `scripts/validate_repo.py` enforces both.
- **Codex plugins**: `.codex-plugin/plugin.json` is documented as a *compatibility fallback*; the portable manifest is a root `plugin.json` with `$schema`. This repository has not been packaged or tested as a Codex plugin.
- **Gemini CLI**: install by copying (`scripts/install.py --target gemini`) or with `gemini skills install <git-url> --path skills/<name>`. Verify with `gemini skills list`. Google's documentation notes that some Gemini CLI tiers moved to Antigravity CLI on 2026-06-18; that environment is not tested.
- **ChatGPT**: uploading this repository does not install anything. Provide `skills/4-mat-to-nlp-presentation/SKILL.md`, its `references/` and your sources, and ask it to follow the process with explicit choice rounds. It can simulate the specialist lenses one after another; it cannot run the Claude agents.
