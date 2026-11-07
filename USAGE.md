# Using nlp-4-mat

One command does everything: **`/nlp-4-mat`**, followed by a command or a plain description of what you need.

| Host | How to call it |
|---|---|
| Claude Code | `/nlp-4-mat …` |
| ChatGPT | `@nlp-4-mat …` |
| Codex | `$nlp-4-mat …` |
| claude.ai and Cowork | "use nlp-4-mat to …" |

The examples below use the Claude Code form; just swap the prefix for other hosts. Not installed yet? See [INSTALLATION.md](INSTALLATION.md).

## 1. How it works (60 seconds)

1. **It reads first.** Everything in your project folder, and every file you mention, is read before any question is asked.
2. **It asks only what it can't know.** Questions come in short rounds of up to four. Each has options with the recommended one first. You can answer `A`, `2`, `yes`, `skip` (accept the recommendation), `not sure — recommend`, or type your own answer.
3. **It writes files you can see and edit.** Everything goes into `outputs/<talk-name>/` inside your project folder:

| File | Contents |
|---|---|
| `brief.md` | Audience, goal, time, format and a **decision log** |
| `evidence.md` | Every claim with its source, marked as *exists*, *planned*, *illustrative* or *hypothesis* |
| `storyboard.md` | Two narrative options; the one you choose is timed minute by minute |
| `presentation.json` → `presentation.html` + `speaker-notes.md` | Slides, when you want slides |
| `script.md`, `cue-cards.md` | For a talk without slides |
| `qa.md` | Hard questions and honest answers |
| `review.md` | Independent critique and fixes |

4. **It shows you the strategy before producing anything.** You approve the outcome, audience, narrative, HOW and ask on one screen, or say "just go".
5. **You stay in control.** Edit any file yourself, change one decision with `revise`, or come back days later with `status`.

## 2. Your first presentation in a new project folder (Claude Code)

```text
my-defense/                      ← a new, empty folder
├── thesis.pdf                   ← drop your material here
├── notes.md
└── prototype-screenshots/
```

1. Create the folder and copy your material into it: documents, notes, an old deck, screenshots. Markdown, text and PDF work best. Export PowerPoint or Word files to PDF if they don't read well. Images are fine for reference.
2. Open the folder in Claude Code: `cd my-defense && claude` in a terminal, or **File → Open Folder** in VS Code and open the Claude panel.
3. Type what you need, in one line:
   ```text
   /nlp-4-mat 15-minute defense of thesis.pdf for my NLP Master examiners, slides plus a live demo
   ```
4. Answer the 2–3 rounds of questions. Reply `skip` to accept a recommendation.
5. Approve the one-screen strategy.
6. You'll get `outputs/<name>/` containing the brief, the claim ledger, the storyboard, the slides (`presentation.html`; open it in a browser and print to PDF if needed), the speaker notes, the Q&A and the review.
7. Practise: `/nlp-4-mat rehearse`.

**Tips:**
- If you want the files somewhere else, say so: `… and save everything in ./presentation`.
- Writing your instructions in your own language is fine. Say which language the presentation should be in, if it differs.
- Large PDF? Tell it which chapters matter, or add a short `notes.md` with your priorities.

**claude.ai version:** start a chat (or a *Project*, to keep files together), upload your files, and write *"Use nlp-4-mat to prepare a 15-minute defense from these files for NLP Master examiners."* The outputs appear as files in the chat.

## 3. Command reference

| Type | What happens |
|---|---|
| `/nlp-4-mat` | Resume the current workspace, or start by asking what you're preparing |
| `/nlp-4-mat <description>` | New presentation from your description |
| `help` | Show all commands |
| `new <topic or files>` | Start a new workspace (useful when one already exists) |
| `status` · `resume` | Where are we? Decisions locked, assumed or open; stale files |
| `brief` | Only the interview → `brief.md` |
| `evidence <files>` | Only the claim ledger → `evidence.md` |
| `story` | Two narrative options → `storyboard.md` |
| `make slides` · `script` · `cards` · `guide` · `pitch` · `demo` · `web` · `video` | Produce one deliverable |
| `review [file]` | Critique a new or **existing** talk or deck |
| `rehearse` · `qa` | Timing estimate and hard-question drills |
| `defense` · `pitch` · `workshop` · `talk` · `demo` · `web` · `video` + topic | Start with that format already chosen |
| `retarget <audience/format>` | Same project for a new audience or format |
| `revise <decision>` | Change one decision; only the affected files are regenerated |
| `route` | "Which path should I take?" |
| `nlp` | Suggest 0–4 communication techniques for real problems in your talk |
| `perspectives` · `disney` · `levels` · `objections` · `loops` · `stage` | Run one NLP tool directly (§5) |

## 4. Use cases

### Starting from scratch

| Situation | Type | What you get |
|---|---|---|
| Only an idea, no files | `/nlp-4-mat 10-minute talk on why our team should adopt code reviews, for developers` | Questions about audience and goal, then storyboard → slides |
| A quick outline, low stakes | `/nlp-4-mat quick outline only: 5-min team update on Q3 results` | One question round and a one-page phase map. No agents, no ceremony. |
| A thesis or research → academic defense | `/nlp-4-mat defense thesis.pdf, 20 min, examiners` | Research questions up front, theory and method, a demo labelled *prototype*, limitations, validation plan, tough Q&A |
| Research → conference talk | `/nlp-4-mat 12-min conference talk from paper.pdf, mixed technical audience` | One core idea, evidence slides, a concrete example, a clear takeaway |
| A business case → investor or funder pitch | `/nlp-4-mat pitch 5 min from business-plan.docx` | Problem → what exists → demo → **specific ask + milestones + risks**. Market or traction numbers it can't find are marked UNKNOWN, never invented. |
| An internal proposal → a decision from management | `/nlp-4-mat 10-min proposal to the leadership team to approve a pilot, from proposal.md` | A decision-led structure with options, costs, risks and an explicit decision request |
| Sales or customer presentation | `/nlp-4-mat 15-min customer presentation of our product to a hospital IT team` | Customer-specific WHY, proof, demo, objections handled honestly |
| Teaching a lesson or training | `/nlp-4-mat workshop 45 min teaching teachers to give feedback` | Nested 4MAT modules, at least 40% hands-on, a facilitator guide, a transfer task |
| A course or multi-hour training | `/nlp-4-mat workshop 3-hour training on X, 4 modules` | Outer 4MAT plus one mini-4MAT per module (`cycle`s in the deck) |
| Speech without slides (event, school, ceremony, toast) | `/nlp-4-mat talk 6 min for parents at a school evening, no projector` | A spoken script plus cue cards, signposts, one recurring image |
| A live product demo | `/nlp-4-mat demo 8 min of our app for new users` | A demo run sheet: click path, "watch for…", time box, a fallback video plan, the line to say if it fails |
| Web page or online explainer | `/nlp-4-mat web explain our method as an interactive page` | A section plan, one 4MAT job per section, accessibility |
| Recorded video or async course | `/nlp-4-mat video 3 short videos introducing the tool` | Chunks of 8 minutes or less, each a mini-4MAT, caption-ready text, "pause and try" prompts |
| Personal story plus your method | `/nlp-4-mat keynote mixing my personal journey with my coaching model, about half story` | You set the blend ratio. Your stories are woven into each phase, **only in your own words**. |

### Working with something that already exists

| Situation | Type | What you get |
|---|---|---|
| Critique a finished deck | `/nlp-4-mat review old-deck.pdf` | A 12-point rubric, a source-fidelity check, the top 3 fixes with rewritten lines |
| Improve a deck into 4MAT shape | Export the PowerPoint to PDF first, then `/nlp-4-mat review slides.pdf` and `/nlp-4-mat make slides` | Gaps found (no WHY, no HOW…), then a rebuilt version |
| Fix only the opening or closing | `/nlp-4-mat my opening is boring, here is script.md` | A stronger, truthful opening plus a bridge into the WHY |
| Check numbers and claims before a big meeting | `/nlp-4-mat evidence deck.pdf report.pdf` | Every claim traced to its source; "cannot claim yet" list |
| Too long for the slot | `/nlp-4-mat cut this 30-min talk to 15 min` | What to cut, what to park for Q&A, a re-timed storyboard |

### Changing, resuming, reusing

| Situation | Type |
|---|---|
| Come back tomorrow | `/nlp-4-mat status` (or just `/nlp-4-mat`) |
| The audience changed (examiners → investors) | `/nlp-4-mat retarget investors, 5 min` |
| The time changed (20 → 10 min) | `/nlp-4-mat revise duration 10 min` |
| You want the other narrative option | `/nlp-4-mat revise narrative: story-first` |
| Same material, a second presentation | `/nlp-4-mat new <other audience>`. The evidence is reused. |
| You edited `storyboard.md` yourself | `/nlp-4-mat make slides`. It uses your edits. |

### Preparing to deliver

| Situation | Type | What you get |
|---|---|---|
| Timing check | `/nlp-4-mat rehearse` → choose "timed run" | A word-count-based estimate per phase versus your slot |
| Tough-question practice | `/nlp-4-mat qa` | Questions asked one at a time; feedback on accuracy, brevity, honesty |
| The demo might fail | `/nlp-4-mat rehearse` → "demo failure drill" | A rehearsed fallback line and switch |
| Nervous before speaking | `/nlp-4-mat stage` | A short state routine, mental rehearsal, optional stage moves |
| Expecting sceptics | `/nlp-4-mat objections` | The strongest objections; honest answers vs. reframes; claim IDs |

### NLP tools, on demand (all optional)

| Command | Use when |
|---|---|
| `perspectives` | Your talk only sees *your* view. You get presenter / audience / observer / wider-system angles. |
| `disney` | A big vision with no concrete HOW, or an idea killed too early: Dreamer → Realist → Critic |
| `levels` | Features with no meaning. Connects environment → behaviour → skills → values → identity → purpose. |
| `objections` | Hard Q&A ahead |
| `loops` | A flat script, or a long talk with no thread: opening, story loops, concreteness |
| `stage` | Delivery and nerves |
| `nlp` | You don't know which tool you need. It diagnoses and picks 0–4 for you. |

The audience never hears NLP jargon unless the talk is *about* NLP. No manipulative techniques are used. See `knowledge/NLP_TECHNIQUES.md` for the evidence status of each.

## 5. Working on other hosts

- **ChatGPT**: `@nlp-4-mat defense from these files, 15 min`, after uploading the files to the chat. Files are created in the chat. The helper scripts may not run there; if so, you get the deck as JSON plus speaker notes, without the HTML render.
- **Codex CLI**: in your project folder, `$nlp-4-mat …` works like Claude Code.
- **claude.ai or Cowork**: "Use nlp-4-mat to …". In Cowork the specialist agents run; in a claude.ai chat the reviews run one after another.

## 6. Good habits

- **Give it your real material.** It won't invent personal stories, numbers or results. Anything missing is marked *UNKNOWN* or *assumption*.
- **Check `evidence.md`** before a high-stakes talk. Anything you planned but haven't done must never be presented as done.
- **Say "just go"** when you want a fast draft. It will proceed with visible assumptions.
- **Open `presentation.html`** in a browser and use the arrow keys. Print to PDF from the browser if you need a file. There is no PowerPoint export; copy from `presentation.json` if you need PPTX.
- **Rehearse aloud.** The timing estimate is word-based, not a stopwatch.

## 7. Limitations

- One speaker per presentation. Multi-speaker handovers aren't modelled yet.
- No PPTX or video files are produced. Visual suggestions are text directions, not images.
- Live behaviour (question pickers, specialist agents) depends on the host. See [docs/CROSS_PLATFORM.md](docs/CROSS_PLATFORM.md).
