#!/usr/bin/env python3
"""Recompute every numeric answer stated in the sprint content.

Each content file content/<stem>.md (or content/companions/<stem>_companion.md)
has a sibling module docs/checks/check_<stem>.py defining
    CHECKS: list[tuple[str, float, float, float]]  # (label, computed, stated, rel_tol)
Usage: python3 verify_numbers.py [stem ...]
"""
import importlib.util
import math
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent
CONTENT = DOCS.parent / "content"


def content_stems():
    stems = [p.stem for p in CONTENT.glob("day*.md")]
    stems += [p.stem.replace("_companion", "") for p in (CONTENT / "companions").glob("week*_companion.md")]
    return sorted(stems)


def load(stem):
    path = DOCS / "checks" / f"check_{stem}.py"
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"check_{stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "CHECKS", None)


def main(argv):
    stems = argv or sorted(set(content_stems()) | {p.stem[6:] for p in (DOCS / "checks").glob("check_*.py")})
    total = bad = 0
    for stem in stems:
        checks = load(stem)
        if checks is None:
            print(f"MISSING   no CHECKS for {stem} (docs/checks/check_{stem}.py)")
            bad += 1
            continue
        for label, computed, stated, tol in checks:
            total += 1
            ok = math.isclose(computed, stated, rel_tol=tol, abs_tol=0 if stated else 1e-12)
            if not ok:
                bad += 1
                print(f"MISMATCH  {stem}: {label}  computed={computed:.6g}  stated={stated:.6g}")
    print(f"{total} checks, {bad} mismatches")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
