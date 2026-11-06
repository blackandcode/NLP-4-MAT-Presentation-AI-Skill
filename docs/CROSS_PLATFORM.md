# Cross-platform support matrix

Status key:
- **Implemented**: the files exist.
- **Verified (docs)**: checked against the official documentation on 2026-11-06.
- **Tested**: exercised by this repository's tests.
- **Not tested**: not yet tried on the real platform.

Installation and publishing steps are in `docs/DISTRIBUTION.md`.

| Capability | Claude Code | claude.ai web / Desktop / mobile (Chat) | Cowork | ChatGPT (web, desktop, mobile) | Codex CLI | Gemini CLI |
|---|---|---|---|---|---|---|
| Package | `dist/claude/…` plugin | same plugin (upload or directory) | same plugin | `dist/openai/…` Agent Plugins package | same package | copied skills |
| Skills (14) | ✅ Verified (docs) | ✅ Verified (docs): skills load in Chat | ✅ Verified (docs) | ✅ plugin-bundled skills on web, desktop and mobile (Verified, docs) | ✅ Verified (docs) | ✅ Verified (docs) |
| Agents (6) | ✅ Verified (docs) | ❌ Ignored in Chat (Verified, docs); sequential lens fallback | ✅ Verified (docs) | ❌ Not used; sequential lens fallback | ❌ Not used | ❌ Not adapted |
| Bundled scripts | ✅ | Runs in the code-execution sandbox (scripts supported in skills; Not tested) | ✅ | Not documented whether they execute (Not tested) | ✅ | ✅ |
| Multiple-choice questions | `AskUserQuestion` (Not tested) | Not tested | Not tested | Not tested | Not verified | `ask_user` exists (Verified, docs) |
| Install for yourself | GitHub marketplace | Upload the plugin or skill ZIP; skills sync to Claude Code | Customize → Plugins | Desktop personal marketplace | `codex plugin marketplace add` | `install.py --target gemini` |
| Global listing | Anthropic directory (one listing covers all three Claude surfaces) | same | same | OpenAI Plugin Directory (one directory covers ChatGPT and Codex) | same | — |
| Manifest checks | `claude plugin validate --strict` (Not run: no CLI here) | — | — | Validates against agent-plugins.org 1.0.0 schema (**Tested**) | same | — |
| Self-contained skills | **Tested** (`tests/test_dist.py`) | **Tested** | **Tested** | **Tested** | **Tested** | **Tested** |

## Notes

- **Frontmatter portability.** The Claude plugin keeps the Claude Code-only fields (`disable-model-invocation`, `argument-hint`, `when_to_use`). The ChatGPT/Codex package and the claude.ai skill ZIPs keep only `name` and `description`. Every description is 200 characters or fewer, which is claude.ai's limit.
- **How to call it**: `/nlp-4-mat [command]` in Claude Code (bare name, or `/nlp-4-mat:nlp-4-mat` if another command has the same name); `@nlp-4-mat …` in ChatGPT; `$nlp-4-mat …` in Codex; "use nlp-4-mat to …" in claude.ai and Cowork, where no slash menu for skills is documented. The same sub-commands work everywhere, because the skill reads them from the message text.
- **Custom GPTs** are being transitioned to plugins by OpenAI. They are not offered as a route.
- **Gemini CLI**: Google's docs note that some tiers moved to Antigravity CLI on 2026-06-18. That environment has not been tested.
