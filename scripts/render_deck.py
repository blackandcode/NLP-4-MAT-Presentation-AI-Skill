#!/usr/bin/env python3
"""Render a portable, keyboard-accessible HTML deck plus Markdown speaker notes."""
import argparse
import html
import json
from pathlib import Path

from audit_deck import audit, PHASES

LABELS = {
    "mini-what": "MINI WHAT / ORIENTATION",
    "why": "WHY / MEANING",
    "what": "WHAT / UNDERSTANDING",
    "how": "HOW / APPLICATION",
    "what-if": "WHAT IF / FUTURE",
}

CSS = r"""
:root {color-scheme:dark;--bg:#0b1020;--paper:#131e33;--ink:#e9eef7;--muted:#a5b4cc;--line:#34445e;--accent:#829dff;--w:1120px}
*{box-sizing:border-box} body{margin:0;background:radial-gradient(circle at 72% 10%,#1d2f58,#0b1020 58%);color:var(--ink);font:17px/1.65 system-ui,-apple-system,Segoe UI,Arial,sans-serif}
a{color:#abd1ff} .shell{max-width:var(--w);margin:auto;padding:28px 24px 44px}.top{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:18px}
.brand{font-size:12px;letter-spacing:.18em;font-weight:700;color:var(--muted)} .deck-title{font-size:15px;font-weight:650;max-width:65ch}
.stage{min-height:70vh;display:grid;place-items:center;padding:50px 0}.slide{display:none;width:100%;min-height:530px;border-radius:26px;background:linear-gradient(140deg,#17233b,#0f172a);border:1px solid #33435e;box-shadow:0 28px 70px #05091380;padding:clamp(32px,6vw,76px);position:relative;overflow:hidden}
.slide::before{content:"";position:absolute;top:-150px;right:-150px;width:400px;height:400px;border-radius:50%;background:var(--accent);filter:blur(130px);opacity:.22;pointer-events:none}.slide.active{display:flex;flex-direction:column;justify-content:center}
.phase{color:var(--accent);letter-spacing:.17em;font-size:12px;font-weight:750;position:relative}h1{font-size:clamp(2rem,5vw,4.6rem);line-height:1.12;max-width:17ch;letter-spacing:-.055em;margin:18px 0}h2{font-size:clamp(1.1rem,2vw,1.55rem);max-width:46ch;font-weight:450;color:#c5d3e9;margin:0 0 24px}
ul{margin:12px 0 0;padding-left:22px;max-width:68ch}li{margin:8px 0}.visual{margin-top:22px;padding:13px 17px;border-left:3px solid var(--accent);background:#ffffff08;color:#cbd5e1;font-size:.95rem;max-width:65ch}
.diagram{margin-top:26px;display:flex;gap:14px;align-items:center;flex-wrap:wrap;max-width:880px}.diagram .node{flex:1 1 130px;min-width:120px;padding:14px 15px;border:1px solid color-mix(in srgb,var(--accent) 45%,#34445e);border-radius:14px;background:color-mix(in srgb,var(--accent) 12%,#101828);font-size:14px;font-weight:650;text-align:center;line-height:1.35}.diagram.cycle .node{border-radius:999px}.diagram.layers{flex-direction:column;align-items:stretch;max-width:650px}.diagram.roadmap .node{border-bottom:4px solid var(--accent)}.diagram .arrow{font-size:22px;color:var(--accent);line-height:1}.prompt{margin-top:18px;color:#dceeff;font-size:.95rem;font-weight:600}.meta{position:absolute;bottom:19px;right:28px;color:var(--muted);font-size:12px}
.controls{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}.buttons{display:flex;gap:10px}button{font:inherit;font-size:14px;background:#223555;color:var(--ink);border:1px solid #486185;border-radius:12px;padding:9px 20px;cursor:pointer}button:hover,button:focus-visible{background:#304b70;outline:2px solid #aad8ff;outline-offset:2px}.counter{color:var(--muted);font-size:14px}.bar{height:5px;background:#17243a;margin-top:14px;border-radius:5px;overflow:hidden}.bar>div{height:100%;background:var(--accent);transition:width .2s} .help{font-size:12px;color:var(--muted);margin-top:12px}
.mini-what{--accent:#94a3b8}.why{--accent:#6ba8ff}.what{--accent:#c4a2ff}.how{--accent:#70d8b3}.what-if{--accent:#ffca80}
@media(max-width:700px){.shell{padding:16px}.stage{padding:20px 0;min-height:68vh}.slide{padding:30px;min-height:510px;border-radius:18px}h1{font-size:2.4rem}h2{font-size:1.1rem}.meta{position:static;margin-top:16px}}
@media print{body{background:#fff;color:#000}.shell{max-width:none;padding:0}.top,.controls,.bar,.help{display:none!important}.stage{display:block;padding:0}.slide{display:flex!important;min-height:95vh;page-break-after:always;box-shadow:none;border:0;border-radius:0;background:white!important;color:black!important}.phase,.visual,.prompt,h2{color:#2a415f!important}h1{color:#000}li{color:#222}.slide::before{display:none}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""
JS = r"""
(() => {
 const slides=[...document.querySelectorAll('.slide')]; const counter=document.getElementById('counter'); const progress=document.getElementById('progress');
 let current=0;
 function show(i){current=Math.max(0,Math.min(i,slides.length-1));slides.forEach((s,n)=>{const active=n===current;s.classList.toggle('active',active);s.setAttribute('aria-hidden',String(!active));});counter.textContent=`${current+1} / ${slides.length}`;progress.style.width=`${((current+1)/slides.length)*100}%`;location.hash=`slide-${current+1}`;}
 document.getElementById('prev').addEventListener('click',()=>show(current-1));document.getElementById('next').addEventListener('click',()=>show(current+1));
 document.addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)&&!['INPUT','TEXTAREA','BUTTON'].includes(document.activeElement.tagName)){e.preventDefault();show(current+1)} else if(['ArrowLeft','PageUp'].includes(e.key)&&!['INPUT','TEXTAREA','BUTTON'].includes(document.activeElement.tagName)){e.preventDefault();show(current-1)} else if(e.key==='Home'){show(0)}else if(e.key==='End'){show(slides.length-1)}});
 const fromHash=Number((location.hash.match(/^#slide-(\d+)$/)||[])[1]||1)-1;show(fromHash);
})();
"""


def esc(value):
    return html.escape(str(value), quote=True)


def render(data):
    title = esc(data.get("title", "4MAT Presentation"))
    audience = esc(data.get("audience", ""))
    body = []
    for i, s in enumerate(data["slides"], 1):
        phase = s["phase"]
        bullets = "".join(f"<li>{esc(x)}</li>" for x in s.get("body", []))
        prompt = f'<div class="prompt">Audience: {esc(s["audience_prompt"])}</div>' if s.get("audience_prompt") else ""
        visual = ""
        diagram=s.get("diagram")
        if diagram:
            shape=diagram["type"]
            nodes=[]
            for j,label in enumerate(diagram["nodes"]):
                nodes.append(f'<div class="node">{esc(label)}</div>')
                if shape in ("steps", "roadmap") and j < len(diagram["nodes"])-1:
                    nodes.append('<span class="arrow" aria-hidden="true">→</span>')
            if shape=="cycle":
                nodes.append('<span class="arrow" aria-hidden="true">↺</span>')
            visual = f'<div class="diagram {shape}" role="group" aria-label="{esc(shape)} diagram">{"".join(nodes)}</div>'
        cycle = f" · {esc(s['cycle'])}" if s.get("cycle") else ""
        body.append(f'''<section class="slide {esc(phase)}" id="slide-{i}" role="group" aria-roledescription="slide" aria-label="Slide {i}: {esc(s['title'])}">
<div class="phase">{LABELS[phase]}</div><h1>{esc(s['title'])}</h1><h2>{esc(s['headline'])}</h2>
<ul>{bullets}</ul>{visual}{prompt}<div class="meta">{i:02d}{cycle} · {esc(s['minutes'])} min</div></section>''')
    return f'''<!doctype html><html lang="{esc(data.get('language','en'))}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b1020"><title>{title}</title><style>{CSS}</style></head>
<body><main class="shell"><header class="top"><div><div class="brand">4MAT / PRESENTATION STUDIO</div><div class="deck-title">{title}</div></div><div class="counter">{audience}</div></header>
<div class="stage">{''.join(body)}</div><nav class="controls" aria-label="Slides navigation"><div class="buttons"><button type="button" id="prev" aria-label="Previous slide">Previous</button><button type="button" id="next" aria-label="Next slide">Next</button></div><div class="counter" id="counter" aria-live="polite"></div></nav><div class="bar" aria-hidden="true"><div id="progress"></div></div><div class="help">Keyboard: ← / → · Space · Home / End. Print to PDF from your browser. Notes are in the companion Markdown file.</div></main><script>{JS}</script></body></html>'''


def speaker_notes(data):
    out = [f"# {data['title']} — speaker notes", "", f"Audience: {data['audience']} | Duration: {data['duration_minutes']} minutes | Medium: {data['medium']}", ""]
    for i, s in enumerate(data["slides"], 1):
        cycle = f" [{s['cycle']}]" if s.get("cycle") else ""
        out += [f"## {i:02d}. {s['title']} — {LABELS[s['phase']]}{cycle} ({s['minutes']} min)", "", s['speaker_notes'], ""]
        if s.get("process_notes"):
            out += ["**Process cue:** " + s["process_notes"], ""]
        if s.get("visual"):
            out += ["**Visual production direction:** " + s["visual"], ""]
        if s.get("audience_prompt"):
            out += ["**Audience prompt:** " + s["audience_prompt"], ""]
        if s.get("evidence_ids"):
            out += ["**Evidence IDs:** " + ", ".join(s["evidence_ids"]), ""]
    out += ["## Notes", "", "Verify evidence IDs against your evidence.md and rehearse the actual talk. HTML slide bullets are not a substitute for source documentation.", ""]
    return "\n".join(out)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--out",type=Path,default=None)
    a=p.parse_args(argv)
    data=json.loads(a.input.read_text(encoding="utf-8"))
    errors,warnings=audit(data)
    if errors:
        p.error("Invalid presentation: " + "; ".join(errors))
    output=a.out or a.input.with_suffix(".html")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(render(data),encoding="utf-8")
    notes=output.with_name("speaker-notes.md")
    notes.write_text(speaker_notes(data),encoding="utf-8")
    print("Slides:",output)
    print("Notes:",notes)
    if warnings:
        print("Editorial warnings: " + "; ".join(warnings))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
