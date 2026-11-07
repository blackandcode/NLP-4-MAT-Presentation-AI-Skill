# Installation and updates

How to install **nlp-4-mat** on each AI tool, keep it updated, and remove it. To *use* it, see [USAGE.md](USAGE.md). To publish it to the global directories, see [docs/DISTRIBUTION.md](docs/DISTRIBUTION.md).

| Tool | Install | Update | Remove |
|---|---|---|---|
| **Claude Code** (CLI, VS Code, JetBrains, desktop "Code" tab), global | Plugin from GitHub (§1) | `claude plugin marketplace update nlp-4-mat` + `claude plugin update nlp-4-mat@nlp-4-mat` | `claude plugin uninstall nlp-4-mat@nlp-4-mat` |
| Claude Code, without a plugin | Copy into `~/.claude/skills` (§2) | `git pull` + reinstall with `--force` | Delete the copied folders |
| **claude.ai** web, Claude Desktop, mobile, **Cowork** | Upload the plugin ZIP (§3) | Upload the new ZIP | Customize → Plugins → remove |
| **ChatGPT** desktop app | Personal marketplace (§4) | Restart the app; it pulls from `main` | Remove the entry from `~/.agents/plugins/marketplace.json` |
| ChatGPT web and mobile | After directory approval, install from **Plugins**. A Business/Enterprise admin can publish it to the workspace earlier (§4.3). | Automatic | Plugins → uninstall |
| **Codex CLI** | `codex plugin marketplace add …` (§5) | Re-add or update the marketplace | Remove the marketplace |
| Gemini CLI | `scripts/install.py --target gemini` (§6) | Reinstall with `--force` | Delete the copied folders |

## Requirements

- **An AI host** from the table above. Claude Code needs plugin support (any 2026 version).
- **Python 3.9+** on your computer, *only* for the two helper scripts: the deck checker and the HTML slide renderer. Without Python the skill still interviews, plans and writes every file, but it can't render `presentation.html`. On claude.ai and in ChatGPT these scripts run in the host's own sandbox.
  - Windows: `winget install Python.Python.3.12`, then reopen your terminal and check that `python --version` works.
  - macOS: `brew install python`.
  - Linux: your package manager.
- **Code execution enabled** on claude.ai: Settings → Capabilities. (Team/Enterprise: the owner's organisation policy.)

## 1. Claude Code — global install as a plugin (recommended)

This installs once for **your user account on this computer**. It then works in every project folder, in the terminal, in VS Code and in JetBrains.

**Inside any Claude Code session** (VS Code chat or terminal):

```text
/plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
/plugin install nlp-4-mat@nlp-4-mat
```

**Or from a terminal:**

```bash
claude plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
claude plugin install nlp-4-mat@nlp-4-mat
```

**Check that it worked:**
1. Start a **new** Claude Code session.
2. Type `/nlp-4-mat help`. You should see the command table.
3. If the bare name doesn't appear, use the always-available namespaced form, `/nlp-4-mat:nlp-4-mat help`. The bare name is hidden when another command has the same name.
4. `/plugin` opens the plugin manager, where you can see what is installed and enabled.

**Update when a new version is published:**

```bash
claude plugin marketplace update nlp-4-mat     # refresh the catalogue from GitHub
claude plugin update nlp-4-mat@nlp-4-mat       # install the newer version
```

Auto-update is off by default for third-party marketplaces; you can switch it on in `/plugin`. A new version only arrives when the maintainer bumps `version`.

**Remove:** `claude plugin uninstall nlp-4-mat@nlp-4-mat`, then `claude plugin marketplace remove nlp-4-mat`.

**Other computers:** run the same two commands on each machine. If you also upload the skills to claude.ai (§3), they sync into Claude Code automatically when you sign in with the same account. In that case, use only one of the two routes to avoid duplicates, or set `syncClaudeAiSkills: false`.

## 2. Claude Code — copy the skills into your user folder (alternative)

Use this if you can't use plugins, or if you want a guaranteed bare `/nlp-4-mat` command:

```bash
git clone https://github.com/blackandcode/NLP-4-MAT-Presentation-AI-Skill.git
cd NLP-4-MAT-Presentation-AI-Skill
python scripts/install.py --target claude --scope user          # → ~/.claude/skills, ~/.claude/agents, ~/.4mat-studio
```

**Update:**

```bash
git pull
python scripts/install.py --target claude --scope user --force
```

**Remove:** delete `~/.claude/skills/nlp-4-mat`, `~/.claude/skills/4mat-*`, the six agent files in `~/.claude/agents/`, and `~/.4mat-studio`.

## 3. claude.ai (web, Claude Desktop, mobile) and Cowork

The plugin is uploaded to your **Claude account**, so it follows you to every device signed in to that account.

1. Get the plugin ZIP. Either:
   - download `claude-plugin-nlp-4-mat-<version>.zip` from the repository's GitHub **Releases** (when one is published); or
   - build it yourself:
     ```bash
     python scripts/build_dist.py --zips        # → dist/zips/claude-plugin-nlp-4-mat-<version>.zip
     ```
     Without Python, on Windows PowerShell, from the repository folder:
     ```powershell
     Compress-Archive -Path dist\claude\nlp-4-mat\* -DestinationPath nlp-4-mat-claude.zip
     ```
2. In claude.ai, go to **Customize → Plugins → Upload plugin** and select the ZIP.
3. Make sure **code execution** is on (Settings → Capabilities).
4. Use it in a chat: *"Use nlp-4-mat to …"*. claude.ai has no documented slash menu for skills, so ask for it by name.

**If the plugin upload isn't available on your plan**, upload the skills one by one instead: **Customize → Skills → + → Upload a skill**, once for each ZIP in `dist/zips/claude-skills/` (14 files).

**Update:** upload the newer ZIP. **Remove:** Customize → Plugins (or Skills) → delete.

**What's different from Claude Code:** in a claude.ai chat, the six specialist agents are ignored. The skill runs their reviews one after another instead. In Cowork, the agents run.

**Team or Enterprise:** the owner can provision the skills for everyone under **Organization settings → Plugins & skills**. See [docs/DISTRIBUTION.md §3.3](docs/DISTRIBUTION.md).

## 4. ChatGPT

### 4.1 ChatGPT desktop app (personal, works today)

1. Create or open `~/.agents/plugins/marketplace.json`. On Windows this is `C:\Users\<you>\.agents\plugins\marketplace.json`.
2. Paste the content of [dist/openai/personal-marketplace.json](dist/openai/personal-marketplace.json). If the file already has a `plugins` list, add the entry to it.
3. Restart the ChatGPT desktop app → **Plugins** → install **NLP-4MAT Presentation Studio**.
4. Use it: `@nlp-4-mat help`.

### 4.2 ChatGPT web and mobile (everyone)

These become available once the plugin is approved in the OpenAI Plugin Directory: **Plugins → search "NLP-4MAT"**. The submission steps are in [docs/DISTRIBUTION.md §6](docs/DISTRIBUTION.md).

### 4.3 ChatGPT Business / Enterprise

A workspace admin can publish the plugin to the workspace, or import it from GitHub. It then appears for members on web, desktop and mobile.

Custom GPTs are not offered, because OpenAI is moving them to plugins.

## 5. Codex CLI

```bash
codex plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
```

Use it as `$nlp-4-mat help`.

Skills-only alternative: `python scripts/install.py --target codex --scope user`, which copies to `~/.agents/skills`.

## 6. Gemini CLI

```bash
python scripts/install.py --target gemini --scope user        # → ~/.gemini/skills + ~/.4mat-studio
gemini skills list                                            # verify
```

Ask for it by name ("use the nlp-4-mat skill to …"). The agents are not adapted for Gemini, so the reviews run one after another.

## Troubleshooting

| Problem | Fix |
|---|---|
| `/nlp-4-mat` not found in Claude Code | Start a new session. Try `/nlp-4-mat:nlp-4-mat`. Check `/plugin` that it is enabled. |
| It answers generically, without asking questions | Call it explicitly with `/nlp-4-mat …` (or "use nlp-4-mat") instead of a general request |
| "python not found" when rendering slides | Install Python (see Requirements). Everything except the HTML render still works. |
| claude.ai upload rejected | Try the other ZIP layout (the folder at the root rather than its contents), or upload the individual skill ZIPs. Report it in an issue. |
| Old behaviour after an update | `claude plugin marketplace update nlp-4-mat`, then `claude plugin update …`, then start a new session |
