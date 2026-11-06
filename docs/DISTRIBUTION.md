# Distribution guide: use the 4MAT studio everywhere

One source of truth (`skills/`, `agents/`, `knowledge/`, `scripts/`, `assets/`, `distribution/config.json`) is built into two self-contained packages:

| Package | Path | For |
|---|---|---|
| Claude plugin | `dist/claude/nlp-4-mat/` | Claude Code, claude.ai (web, desktop, mobile), Cowork |
| Agent Plugins package | `dist/openai/nlp-4-mat/` | ChatGPT (web, desktop, mobile) and Codex |

```bash
python scripts/build_dist.py --zips   # rebuild packages + upload ZIPs in dist/zips/
python scripts/build_dist.py --check  # fails if committed dist/ is stale
```

Every skill in both packages is **self-contained**: it carries its own `references/` and `scripts/`. claude.ai, Cowork and ChatGPT load skills individually, and the vendor docs don't confirm that a skill can read a shared folder elsewhere in the plugin.

**How users call it after installing** (the same sub-commands everywhere, e.g. `help`, `review`, `pitch`, `rehearse`):

| Host | Syntax |
|---|---|
| Claude Code | `/nlp-4-mat …`, or `/nlp-4-mat:nlp-4-mat …` if another command has the same name |
| ChatGPT | `@nlp-4-mat …` |
| Codex | `$nlp-4-mat …` |
| claude.ai and Cowork | "use nlp-4-mat to …" (no slash menu for skills is documented there) |

## 1. Which route should I use?

| Goal | Route | Section | Who can do it | Status |
|---|---|---|---|---|
| Claude Code on any computer | Your GitHub marketplace | §2 | Anyone | Ready once `dist/` is pushed |
| claude.ai web, Desktop, mobile and Cowork, for yourself | Upload the plugin ZIP (or skill ZIPs) to your account | §3 | Any plan with skills and code execution | Ready (upload not yet tried) |
| Your whole Claude team or company | Org provisioning | §3.3 | Team/Enterprise owner | Ready |
| **Everyone on Claude** (the global directory) | Anthropic directory submission | §4 | A paid claude.ai plan | Needs your submission and Anthropic review |
| ChatGPT desktop / Codex, for yourself | Personal or repo marketplace | §5 | Anyone with the ChatGPT desktop app or the Codex CLI | Ready (not yet tried) |
| Your ChatGPT Business/Enterprise workspace | Admin publish or GitHub import | §5.3 | Workspace admin | Ready |
| **Everyone on ChatGPT** (web, desktop, mobile) | OpenAI Plugin Directory submission | §6 | A verified OpenAI platform org | Needs your submission and OpenAI review |
| Gemini CLI | Copy-install | §7 | Anyone | Ready |

**Recommended order:**
1. Push `dist/` (§2).
2. Install on all your devices (§2 + §3).
3. Submit to Anthropic (§4) and OpenAI (§6).

The directory listings are what make it available to everyone without any setup.

**Not offered: custom GPTs.** OpenAI is transitioning custom GPTs to plugins (learn.chatgpt.com/docs/migrate-custom-gpts), so the plugin route replaces them.

## 2. Claude Code on every machine (GitHub marketplace)

The repository is itself a marketplace (`.claude-plugin/marketplace.json`). It points at the self-contained build in `dist/claude/…`.

```bash
# once per machine
claude plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
claude plugin install nlp-4-mat@nlp-4-mat
# later, after you publish a new version
claude plugin update nlp-4-mat@nlp-4-mat
```

Inside a session, `/plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill` works too. Then type `/nlp-4-mat` (or `/nlp-4-mat help`). If another command uses the same name, the namespaced `/nlp-4-mat:nlp-4-mat` always works. Auto-update is off by default for third-party marketplaces, so **bump `version` on every release**, or users keep the old copy.

## 3. claude.ai, Claude Desktop, mobile and Cowork (your account)

### 3.1 As one plugin (recommended)

1. Run `python scripts/build_dist.py --zips`.
2. In claude.ai, go to **Customize → Plugins → Upload plugin**, and choose `dist/zips/claude-plugin-nlp-4-mat-<version>.zip`. The limit is 5,000 files and 200 MB.
3. Make sure code execution is on: **Settings → Capabilities** on Free/Pro/Max, or the org policy on Team/Enterprise.

What loads where (Anthropic's platform-support table):

| Component | Chat (web, desktop, mobile) | Cowork | Claude Code |
|---|---|---|---|
| 14 skills | ✅ | ✅ | ✅ |
| 6 agents | ❌ ignored. The orchestrator falls back to sequential lens passes. | ✅ | ✅ |
| Bundled Python scripts | Run in the code-execution sandbox | ✅ | ✅ |

The ZIP has `.claude-plugin/plugin.json` at its root. If the uploader rejects that layout, rezip the `dist/claude/nlp-4-mat` *folder* itself and try again, and tell us which one worked.

### 3.2 As individual skills (fallback)

Go to **Customize → Skills → + → Upload a skill**, once per ZIP in `dist/zips/claude-skills/` (14 skills). Each ZIP has the skill folder at its root, the folder name matches the skill name, the description is 200 characters or fewer, and the frontmatter has only `name` and `description`.

**Sync to Claude Code:** skills you enable on claude.ai also load in Claude Code when you sign in with the same account (Claude Code v2.1.273+; one-way; not with an API key or Bedrock). Plugins added from the directory load as `<name>@synced`. Turn the sync off with `syncClaudeAiSkills: false` if you already installed via §2, to avoid duplicates.

### 3.3 Team or Enterprise: provision for everyone

1. Go to **Organization settings → Plugins & skills → Policy** and enable *Cloud code execution and file creation* and *Skills*.
2. Click **Add → Upload a skill** for each skill ZIP. Provisioned skills appear immediately for all users, who can switch them off.
3. Enterprise can also assign the plugin to groups (Manage plugins).

## 4. Publish to the Anthropic directory (global listing for Claude)

One approved listing reaches **claude.ai, Cowork and Claude Code**, and appears in the community marketplace (`claude plugin marketplace add anthropics/claude-plugins-community`, then install `…@claude-community`). The official `claude-plugins-official` marketplace does **not** take submissions.

**Prerequisites:**
- a paid claude.ai plan (Pro, Max or Ultra on your own account; Team or Enterprise needs an Owner);
- a public GitHub repo (already true for `blackandcode/NLP-4-MAT-Presentation-AI-Skill`);
- `dist/` committed and pushed.

**Before submitting:**

```bash
claude plugin validate .                                                   # marketplace
claude plugin validate --strict ./dist/claude/nlp-4-mat    # plugin; --strict fails on warnings
```

**Submit:**
1. Go to **claude.ai/directory/manage → Submit new → Plugin bundle**.
2. **Source**: repo `blackandcode/NLP-4-MAT-Presentation-AI-Skill`, plugin path `dist/claude/nlp-4-mat`, tracked branch `main`. Then click **Validate**.
3. **Listing details** are prefilled from `plugin.json`: `displayName`, `description`, `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl`.
4. **Data handling**: the plugin collects no data and has no MCP server, connector or network calls (see `PRIVACY.md`).
5. **Compliance**: a contact email plus four acknowledgements.
6. **Review and submit.** Each version gets automated validation and a security scan, and a person reviews a new listing before it goes live. Review time isn't fixed.

The portal allows 10 submissions per 24 hours.

**Updates**: merge to `main` with a bumped `version`, and the directory picks up the commit, scans it and publishes it according to your publish setting. **Delist** stops further updates for existing users.

**Reserved names**: names starting `claude-`, `anthropic-` or `cc-plugin-` are refused. `nlp-4-mat` is fine (checked in `tests/test_dist.py`).

## 5. ChatGPT desktop and Codex (yourself or your workspace)

The ChatGPT/Codex package uses the open **Agent Plugins** format:
- a root `plugin.json` with `"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"`;
- OpenAI listing fields under `extensions["com.openai"].interface`.

It **validates against the official schema** (checked during this build). Agents aren't included, because ChatGPT and Codex don't use Claude agent files. The orchestrator runs the specialist lenses as sequential passes instead.

### 5.1 ChatGPT desktop app, personal install

1. Copy `dist/openai/personal-marketplace.json` to `~/.agents/plugins/marketplace.json`, or merge its `plugins` entry into your existing file. It pulls `./dist/openai/nlp-4-mat` from GitHub (`git-subdir`, ref `main`).
2. Restart the ChatGPT desktop app, open **Plugins**, and install **4MAT Presentation Studio**.
3. Offline alternative: copy the `dist/openai/nlp-4-mat` folder to `~/.codex/plugins/` and use a `"source": {"source": "local", "path": "…"}` entry instead.

### 5.2 Codex CLI

```bash
codex plugin marketplace add blackandcode/NLP-4-MAT-Presentation-AI-Skill
```

The repo ships `.agents/plugins/marketplace.json`, pointing at `dist/openai/…`, and also `.claude-plugin/marketplace.json`. OpenAI's docs don't say which of the two the command reads, so confirm with the plugin list after adding. Skills-only fallback: `python scripts/install.py --target codex`.

### 5.3 Business / Enterprise workspace

A workspace admin can publish the plugin to the workspace (**Personal → ⋯ → Publish**) or **import and sync it from GitHub** (learn.chatgpt.com/docs/enterprise/plugin-management). It then reaches members on web, desktop and mobile, inside the workspace boundary.

## 6. Publish to the OpenAI Plugin Directory (global listing for ChatGPT and Codex)

There is one universal directory: an approved plugin is discoverable in ChatGPT (web, desktop, mobile) and in Codex.

**Prerequisites:**
- an OpenAI platform organization, where you are the owner or have *Apps Management Write*;
- **individual or business verification** completed in the organization settings.

**Submit:**
1. Run `python scripts/build_dist.py --zips`.
2. Go to **platform.openai.com/plugins → Upload new or existing plugin**, and upload `dist/zips/openai-plugin-nlp-4-mat-<version>.zip` (with `plugin.json` at the ZIP root).
3. Resolve the automated **Metadata & Skills** checks. The listing comes from `extensions.com.openai.interface`:

   | Field | Value |
   |---|---|
   | displayName | "4MAT Presentation Studio" (30 characters or fewer) |
   | shortDescription | "Plan evidence-based 4MAT talks" (30 characters or fewer) |
   | longDescription | — |
   | developerName | — |
   | category | Productivity |
   | defaultPrompt | 3 prompts |
   | brandColor | — |
   | composerIcon / logo | Square PNGs at 512 and 1024 px |
   | Website, support, privacy and terms URLs | — |

   This is a **skills-only** plugin, so there is no MCP review and no test credentials.
4. Click **Submit for review**, with the policy attestations. Only one review can be active per plugin. After approval, **you choose when to publish**.

Not eligible for submission: lifecycle hooks or `.app.json` apps. This package has neither, and the tests guard that.

## 7. Gemini CLI

```bash
python scripts/install.py --target gemini --scope user        # ~/.gemini/skills + ~/.4mat-studio
```

Alternatively, run `gemini skills install https://github.com/blackandcode/NLP-4-MAT-Presentation-AI-Skill --path dist/openai/nlp-4-mat/skills/<skill>` for **each** of the 14 skill folders. The orchestrator relies on the other skills being installed too. These self-contained copies don't need `.4mat-studio`.

## 8. Release checklist (every version)

1. Edit the sources only, never `dist/`.
2. Bump `version` in **both** `distribution/config.json` and `.claude-plugin/plugin.json`. The validator enforces that they match.
3. Run:
   ```bash
   python scripts/build_dist.py --zips
   python scripts/validate_repo.py
   python -m unittest discover -s tests
   python scripts/build_dist.py --check
   ```
4. `claude plugin validate --strict ./dist/claude/nlp-4-mat`
5. Commit, including `dist/claude` and `dist/openai`. The ZIPs are gitignored.
6. Push to `main`. Claude Code marketplace users get the update with `claude plugin update`, and the Anthropic directory picks it up automatically.
7. `gh release create v<version> dist/zips/*.zip dist/zips/claude-skills/*.zip`, so people can download the upload ZIPs.
8. OpenAI directory: upload the new ZIP as a new version of the existing plugin.

## 9. Still to confirm in the products

These points aren't fully documented, so verify each one on your first try:

- **claude.ai plugin ZIP layout**: manifest at the ZIP root vs. the plugin folder at the root.
- **claude.ai skill ZIPs**: Anthropic's articles disagree on `skill.md` vs. `SKILL.md`. We ship `SKILL.md`, the standard name.
- **Codex CLI**: whether `codex plugin marketplace add owner/repo` reads `.agents/plugins/…` or `.claude-plugin/…`.
- **ChatGPT desktop**: whether a plugin from a personal marketplace also appears on ChatGPT web and mobile. OpenAI documents web and mobile availability for directory and workspace plugins.
- **ChatGPT web**: whether bundled skill scripts (`audit_deck.py`, `render_deck.py`) execute there. If they don't, the skills still work; you just lose the automated deck audit and HTML rendering.
- **Anthropic directory rules** beyond the CLI's `--strict` check: README, license and naming rules on the pre-submission checklist page, which wasn't reviewed for this guide.

## Sources (checked 2026-11-06)

- **Claude Code**:
  - Publish and distribute a plugin: https://code.claude.com/docs/en/plugins/publish
  - Anthropic's marketplaces: https://code.claude.com/docs/en/plugins/anthropic-marketplaces
  - Plugins reference: https://code.claude.com/docs/en/plugins-reference
- **Claude directory**:
  - https://claude.com/docs/directory/publish
  - https://claude.com/docs/plugins/submit
  - https://claude.com/docs/plugins/platform-support
- **Community marketplace**: https://github.com/anthropics/claude-plugins-community
- **claude.ai skills**:
  - https://support.claude.com/en/articles/12512180-use-skills-in-claude
  - https://support.claude.com/en/articles/12512198-creating-custom-skills
  - https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
- **OpenAI**:
  - https://developers.openai.com/plugins/build/plugins
  - https://developers.openai.com/plugins/build/skills
  - https://developers.openai.com/plugins/deploy/submission
  - https://learn.chatgpt.com/docs/plugins
  - https://learn.chatgpt.com/docs/build-skills
  - https://learn.chatgpt.com/docs/migrate-custom-gpts
- **Agent Plugins**: https://agent-plugins.org and https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
