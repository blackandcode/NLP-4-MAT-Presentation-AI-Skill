# Claude Code instructions — 4MAT NLP Skills

For any task to design, adapt, retarget, rehearse, audit or render a 4MAT presentation, start from the orchestrator skill `4-mat-to-nlp-presentation` (the slash alias is `/4mat-start`), or from a narrower skill when the user asks for one step only.
Use the project files under `skills/`, `agents/` and `knowledge/` when they are available.
When tools permit, use AskUserQuestion for interactive single- or multiple-choice decisions. Never assume that a question tool is present.
Parallel agents can research and critique independently, but they must not make irreversible decisions for the user. Review all agent disagreements in the main conversation.
Source claims in the academic example must distinguish an existing early prototype, a future vision and untested research hypotheses.
`examples/` are fixed test inputs: report problems found in them, but do not edit them. Keep `skills/`, `agents/` and `knowledge/` generic; personal stories belong only in examples.
