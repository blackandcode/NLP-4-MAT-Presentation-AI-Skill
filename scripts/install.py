#!/usr/bin/env python3
"""Install portable 4MAT skills into Claude Code, Gemini CLI or Codex; no network/deps."""
import argparse
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SUBDIR={"claude":Path(".claude/skills"),"gemini":Path(".gemini/skills"),"codex":Path(".agents/skills")}


def install(target,scope="project",destination=None,force=False,dry_run=False):
    if target not in SUBDIR:
        raise ValueError(f"Unknown target {target!r}")
    if scope not in ("project","user"):
        raise ValueError(f"Unknown scope {scope!r}")
    base=Path(destination).expanduser().resolve() if destination else (Path.cwd() if scope=="project" else Path.home())
    if scope=="user" and destination is None:
        base=Path.home()
    skills_dest=base/SUBDIR[target]
    operations=[]
    for skill in sorted((ROOT/"skills").iterdir()):
        if skill.is_dir() and (skill/"SKILL.md").is_file():
            operations.append((skill,skills_dest/skill.name))
    for support in ("knowledge", "scripts"):
        operations.append((ROOT/support, base/".4mat-studio"/support))
    if target=="claude":
        for agent in sorted((ROOT/"agents").glob("*.md")):
            operations.append((agent,base/".claude/agents"/agent.name))
    existing=[str(dest) for _,dest in operations if dest.exists()]
    if existing and not force:
        raise FileExistsError("Refusing to overwrite existing files/directories; use --force after review:\n"+"\n".join(existing))
    for src,dest in operations:
        print(f"{'WOULD COPY' if dry_run else 'COPY'} {src.relative_to(ROOT)} → {dest}")
        if not dry_run:
            dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.is_dir(): shutil.rmtree(dest)
            elif dest.exists(): dest.unlink()
            if src.is_dir(): shutil.copytree(src,dest)
            else: shutil.copy2(src,dest)
    if not dry_run:
        print(f"Installed {len(operations)} items for {target}. Start/restart the target agent to refresh discovery.")
    return len(operations)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--target",required=True,choices=sorted(SUBDIR))
    p.add_argument("--scope",choices=("project","user"),default="project")
    p.add_argument("--destination",type=Path,help="Project dir, or home-like base for --scope user")
    p.add_argument("--force",action="store_true",help="Overwrite identically named skill directories/agent files")
    p.add_argument("--dry-run",action="store_true")
    a=p.parse_args(argv)
    try:
        return 0 if install(a.target,a.scope,a.destination,a.force,a.dry_run) else 1
    except (OSError,ValueError) as e:
        p.error(str(e))


if __name__=="__main__":
    sys.exit(main())
