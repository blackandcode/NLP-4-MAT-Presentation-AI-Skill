#!/usr/bin/env python3
"""Portable terminal choice wizard; Claude Code should prefer its native question picker."""
import argparse
import json
from pathlib import Path

OPTIONS={
    "outcome":("What should the audience do or understand?",[
        ("academic-defense","Understand and critically evaluate a thesis or project"),
        ("pilot-decision","Decide whether to approve a test/pilot"),
        ("investor-pitch","Decide whether to invest or open due diligence"),
        ("training","Learn a skill they can practice"),
        ("vision","Understand and discuss a vision"),
    ]),
    "audience":("Who is listening?",[
        ("nlp-examiners","NLP Master trainers and examiners"),
        ("education","Educators / parents / child development professionals"),
        ("investors","Investors / decision makers"),
        ("technical","Technical or research audience"),
        ("mixed","Mixed / general audience"),
    ]),
    "medium":("How will it be delivered?",[
        ("slides+speech","Slides with spoken narration"),
        ("speech","Speech only"),
        ("web","Interactive web/HTML presentation"),
        ("workshop","Workshop with audience exercises"),
        ("investor-pitch","Investor pitch deck"),
    ]),
    "why_strategy":("What should anchor the WHY opening?",[
        ("personal-purpose","Presenter's genuine personal mission"),
        ("audience-problem","A verifiable audience problem"),
        ("future-contrast","A clearly hypothetical future scenario"),
    ]),
    "how_strategy":("How should the audience experience HOW?",[
        ("live-demo","Live product/concept demonstration"),
        ("worked-example","A specific worked example with steps"),
        ("exercise","An audience exercise / choice"),
        ("recorded-demo","Narrated screen recording with fallback"),
    ]),
}


def choose(key,prompt,options):
    print("\n"+prompt)
    for i,(_,desc) in enumerate(options,1): print(f"  {i}. {desc}")
    print("  0. Other / type my own")
    while True:
        raw=input("Choice [Enter=1]: ").strip()
        if not raw: return options[0][0]
        if raw=="0": return input("Custom answer: ").strip() or "unspecified"
        if raw.isdigit() and 1<=int(raw)<=len(options): return options[int(raw)-1][0]
        print("Enter a number from the menu.")


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out",type=Path,default=Path("brief.json"))
    args=p.parse_args(argv)
    print("4MAT briefing wizard. Use Ctrl-C to cancel. All options are editable.")
    answers={key:choose(key,*detail) for key,detail in OPTIONS.items()}
    title=input("\nTopic/title: ").strip() or "Untitled presentation"
    language=input("Language [en]: ").strip() or "en"
    while True:
        raw=input("Duration in minutes [15]: ").strip() or "15"
        try:
            duration=float(raw)
            if not 0 < duration <= 10080: raise ValueError
            break
        except ValueError: print("Enter a positive number (maximum one week in minutes).")
    out={"title":title,"language":language,"duration_minutes":duration,**answers,"status":"user choices; research and content not yet verified","next_step":"Use /nlp-4-mat with this JSON as briefing context"}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("\nBrief saved:",args.out)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
