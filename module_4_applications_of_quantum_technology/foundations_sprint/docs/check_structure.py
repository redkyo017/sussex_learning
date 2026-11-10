#!/usr/bin/env python3
"""Enforce the day and companion skeletons and the hint + sketch rule.
Usage: python3 check_structure.py [file ...]   (default: every content file)"""
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
DAY_SECTIONS = ["## Why this matters", "## Core concepts", "## Exercises",
                "## Anti-patterns / Common mistakes", "## Done when", "## Read next"]
COMP_SECTIONS = [f"## {i}." for i in range(1, 8)]


def check_exercises(path, text, fails):
    blocks = re.split(r"(?m)^### Exercise ", text)[1:]
    if not blocks:
        fails.append(f"FAIL {path}: no '### Exercise' blocks")
    for b in blocks:
        b = re.split(r"(?m)^#{1,3} (?!#)", b)[0]  # stop at the next heading of level <= 3
        name = b.splitlines()[0].strip()
        if "**Hint:**" not in b:
            fails.append(f"FAIL {path}: Exercise {name} missing **Hint:**")
        sketch = "**Solution sketch:**" in b
        model = "**Model paragraph:**" in b and "**What a weak answer misses:**" in b
        if not (sketch or model):
            fails.append(f"FAIL {path}: Exercise {name} missing sketch or model paragraph + weak-answer note")


def check(path, fails):
    text = path.read_text(encoding="utf-8")
    if path.name.startswith("day"):
        need = list(DAY_SECTIONS)
        if path.name != "day01.md":
            need.append("## Spaced review")
    elif path.name.endswith("_companion.md"):
        need = COMP_SECTIONS
    else:
        return
    for s in need:
        if not re.search(rf"(?m)^{re.escape(s)}", text):
            fails.append(f"FAIL {path}: missing section '{s}'")
    check_exercises(path, text, fails)


def main(argv):
    files = [Path(a) for a in argv] or sorted(CONTENT.glob("day*.md")) + sorted((CONTENT / "companions").glob("*.md"))
    fails = []
    for f in files:
        check(f, fails)
    print("\n".join(fails) if fails else f"{len(files)} files OK")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
