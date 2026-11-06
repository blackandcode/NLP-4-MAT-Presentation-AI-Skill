# Cross-platform support matrix

| Feature | Claude Code plugin | Gemini CLI copied skills | Codex / ChatGPT environments |
|---|---|---|---|
| Discover SKILL.md | Yes (`skills/`) | Yes (`.gemini/skills`) | Codex `.agents/skills`; ChatGPT/plugin support depends on environment |
| `/4mat-start` invocation | `/4mat-nlp:4mat-start` when plugin-installed; `/4mat-start` when copied | Natural language activation or CLI skill flow | Instruct agent to load skill; project/API setup dependent |
| Native select/pick UI | AskUserQuestion **if exposed** | CLI-specific interaction, may differ | Interface-dependent; fallback numbered choices |
| Native 6-agent files | Yes (`agents/`) | Not automatically compatible | Not automatically compatible |
| Sequential specialist lenses | Yes | Yes, via skill text | Yes, via skill text |
| Slide JSON generator script | Python (local) | Python (local) | Python where file execution is available |
| HTML slides and notes | Yes with Python | Yes with Python | Yes with Python |
| PowerPoint export | Not bundled | Not bundled | Not bundled |

The skills are a portable **instruction standard**, not a guarantee that every UI exposes the same orchestration, tools or installation method. Claude native plugin installer is the intended full-feature path. The source reference files are not embedded for privacy/copyright reasons; supply them when working on your own material.

## OpenAI Codex / Agents API

The `.codex-plugin/plugin.json` manifest declares `skills: ./skills/` and can be used as a starting point for OpenAI Agents API plugin packaging. Follow current OpenAI plugin upload and sandbox registration documentation; this repository has not been submitted to any plugin directory. The same agent team requires redesign using the OpenAI environment's own subagent orchestration and question/approval mechanisms.

## ChatGPT note

Uploading this repository to a conversation as a file does not install a Claude subagent system. If ChatGPT's available plugin/skill system permits importing SKILL.md workflows, use it under those constraints. For ordinary chat, provide `skills/4mat-start/SKILL.md` and the source materials and request the exact 4MAT process with explicit choice rounds; the assistant can simulate sequential specialist perspectives, not spawn Claude plugin agents.

## Gemini CLI

Install via this repo's copying script or from a published Git URL using `gemini skills install`. On copy, Gemini's standard skill discovery includes `.gemini/skills`. Verify with `/skills list` or `gemini skills list`. Use natural-language prompt: `Use the 4mat-start skill to interview me about my academic defense using the attached sources.`
