# Audience and format adaptation playbook

Changing the audience or the delivery format must change **what is said, in what order, with what proof and what ask** — not just the visual theme. Use this file at the storyboard and production stages, and whenever the user retargets an existing presentation.

## 1. Decide in this order

1. **Audience outcome**: what should they *know, feel, believe, decide or do* afterwards? Keep the presenter's goal separate.
2. **Primary audience** (the people whose decision or learning defines success). Note any secondary audiences.
3. **Container**: minutes, format, whether interaction is possible, whether Q&A is inside or outside the time, the room or technology available, language and cultural register.
4. **Evidence depth** the audience expects (see §3).
5. **Story strategy** and **HOW mode**, chosen last because they depend on all of the above.

## 2. Format contracts

Phase shares are starting heuristics, not rules. Always state when Q&A falls outside the stated time.

| Format | Typical shape (Mini What / Why / What / How / What If) | HOW looks like | Must include | Main failure mode |
|---|---|---|---|---|
| **Conventional slides + speech** (10–30 min) | 5 / 25 / 30 / 25 / 15 % | Demo, worked example or short audience exercise | One headline per slide; speaker notes kept separate from slide text | Text-heavy slides read aloud |
| **Academic defense** (15–20 min, Q&A after) | 5 / 15–20 / 30–35 / 20–25 / 15–20 % | A demonstration labelled as *prototype*, *illustration* or *tested result* | Research question(s), theory and method, scope, limitations, validation plan | Vision or emotion substituting for argument; prototype presented as evidence |
| **Investor pitch** (3–7 min) | ~5 / 20 / 25 / 20 / 30 % | Product demo or one customer walkthrough | Problem, solution, *measured* traction only, team, risks, a specific ask, use of funds, milestones | Invented market size or traction; no ask |
| **Interactive workshop** (30–180 min) | Outer frame: Mini What + WHY (~10–15 %), then 1 module per ~20–25 min, each a mini 4MAT; outer WHAT IF close (~10 %) | Participants practise; ≥40 % of the time hands-on | Facilitator guide, timed activities, materials, debrief questions, transfer task | Lecture labelled "workshop"; too many modules |
| **Speech without slides** (any length) | Same phases; transitions spoken explicitly ("Here is why…", "Now, how…") | A vivid worked example, demonstration with objects, or a guided imagination exercise | Cue cards, one recurring image or metaphor, at most three numbers, a recap at each phase end | Listeners losing the structure because nothing is visible |
| **Live product demonstration** | WHAT frames *what to watch for* before the demo; HOW *is* the demo | Scripted click path using prepared ("golden path") data | Fallback video or screenshots; time box; "if it fails" line | Improvised features; demo outruns the time |
| **Web / interactive page** | One screen or section per 4MAT job; progressive disclosure | Interactive step, simulator or try-it panel | Keyboard access, headings, offline/no-JS fallback | Scroll fatigue; decorative interactivity |
| **Recorded / asynchronous** | Chunks of ≤6–8 min, each a mini 4MAT; total shorter than the live version | "Pause and try" prompts that replace live interaction | Captions, on-screen signposts, a link-based call to action | A live talk filmed without adaptation |

Nested cycles: mark each module's slides with `"cycle": "<module-id>"` in `presentation.json`. `scripts/audit_deck.py` then checks the phase order inside each cycle. The whole session must still open with Mini What or WHY and close with WHAT IF.

## 3. Audience lenses

| Audience | WHY must answer | WHAT evidence depth | HOW | WHAT IF / ask | Expect these objections | Avoid |
|---|---|---|---|---|---|---|
| **Academic examiners** | Why this question matters for the field and why it matters to the author | Theory, method, distinction between claim and evidence, cited sources | Demonstration explicitly labelled (prototype / illustration) | Limitations, validation design, contribution | "What is modeled vs. illustrated?", "Where is the evidence?", "Why this framework?" | Overclaiming; undefined jargon; emotion replacing argument |
| **Investors / funders** | A painful, urgent problem for an identifiable buyer, and why now | Only measured traction; unit economics if they exist; clearly labelled hypotheses | Product demo or customer story | Specific ask, milestones, risks, what happens with or without funding | "Why you? How big? What is proven? What could kill this?" | Invented market size, ROI or users; vision without milestones |
| **Teachers / educators** | A classroom or learner problem they recognise | Pedagogical rationale, curriculum fit, time cost | A lesson-ready activity they can run | Adoption steps, support, how to evaluate locally | "Do I have time? Does it fit the curriculum? Is there evidence?" | Technology-first framing; ignoring workload |
| **Parents / families** | The child's experience and wellbeing | Safety, privacy and plain-language rationale | A simple example they could try at home | What to try this week; what the tool will and will not do | "Screen time? Data? Is this right for my child?" | Jargon; fear appeals; implied guarantees |
| **Engineers / technical** | A real technical or product problem | Architecture, constraints, trade-offs, measured performance | A working demo or code walkthrough | Roadmap, open problems, where help is needed | "How does it work? How does it fail? Does it scale?" | Hand-waving; marketing language |
| **General public** | A human story or a situation they recognise | One clear idea with one example | A relatable demonstration | One takeaway they can act on | "Why should I care?" | Density; insider vocabulary |
| **Mixed audience** | Name the primary audience; pace the others explicitly | Main line pitched at the primary audience; brief asides for others | One HOW that works for both | Different next steps per group if needed | Depends on the groups | Trying to please everyone equally |

### Example: one project, four audiences

Take an educational-prototype project, such as a creativity tool for children:

| Audience | Opening WHY | Centre of WHAT | HOW | Close |
|---|---|---|---|---|
| Examiners | The research question and why it is open | Model, method and what the prototype can and cannot show | Prototype demonstration plus a labelled illustrative dialogue | Limitations and pilot design |
| Investors | Parent and teacher pain points with evidence | Product, current measured traction, differentiation | Live demo | Funding ask tied to validation milestones |
| Teachers | A classroom moment that shows the gap | Activity design and its pedagogical rationale | Run the activity with the audience | Try it in one lesson; what to observe |
| Engineers | The interaction-design problem | Architecture, latency, safety constraints | Code or system walkthrough | Open problems; collaboration ask |

## 4. Time and density rules

- **Speaking rate**: plan for 110–150 words per minute. Plan slower for formal settings, for non-native listeners, when interpreting is involved, and for technical content. A verbatim script for *N* minutes should contain roughly `N × 130` words *minus* the time taken by demos, activities and pauses. `audit_deck.py` warns when the speaker notes for a slide exceed its time at the configured maximum words per minute (`--max-wpm`).
- **Density**: a 5-minute pitch needs about 5–7 slides; a 15–20 minute talk, 8–14; a 45-minute workshop, at most two modules. Allow one core idea per 1–2 minutes in short talks.
- **Demos**: set a time box, pre-frame what the audience should notice, prepare a fallback, and write a scripted line for when the demo fails.
- **Q&A**: say whether it is inside the stated duration. If it is inside, reserve it explicitly in WHAT IF.

## 5. Interaction and culture

- **No interaction possible** (formal defense, recording): use rhetorical questions, a pause to reflect, or an imagined scenario instead of exercises.
- **Light interaction**: show of hands, a 30–60 second pair-share, or a one-word answer in chat.
- **Full interaction** (workshop): exercises, then a debrief, then transfer to the participants' own context.
- **Register and culture**: match formality (titles, formal "you"), how directly to critique, how humorous to be, and the language the audience will be addressed in. The left-to-right "past → future" stage layout assumes a left-to-right reading culture; mirror it where the audience reads right to left.
