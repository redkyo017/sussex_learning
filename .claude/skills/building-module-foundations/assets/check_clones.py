"""Flag foundation-sprint exercises that reuse course problems.

Usage:
    python3 check_clones.py <course_dir_or_glob>... <foundations_content_dir>
    python3 check_clones.py --entities <forbidden_entities.txt> <foundations_content_dir>
    python3 check_clones.py --selftest

Qualitative modules have no LaTeX, so the maths detectors pass vacuously there. For those,
phase 0 writes `foundations_sprint/docs/clone_forbidden_entities.txt` - one per line, the
firms, named cases, datasets and worked examples the course's own tasks use as instances.
`--entities` flags any foundations file that mentions one. Framework and author names
(Teece, Pavitt) are the subject matter, not instances - they do not belong in that list.

The LAST argument is the foundations content directory; everything before it is
course material (week_*/ folders, or the files inside them).

Course side = PROBLEM STATEMENTS ONLY: the Problem/Question blocks of week_*_content.md
plus the hint and model-answer files. Lecture files are excluded on purpose - standard
notation (sigma_z, omega = sqrt(k/m)) legitimately recurs everywhere and is not a clone.

Two detectors, both deliberately simple:
  1. Function instances: every concrete object inside the math of a course problem -
     exp(...), e^{...}, sin(...), frac{..}{..}, sqrt{..}, pmatrix blocks - normalised.
     A foundations file that contains the SAME instance is flagged. These are precisely the
     things a clone must change; bare notation (kets, <x^2>) is never an instance. A self-test
     that planted Assessment 1's B exp(beta x) was missed by whole-snippet matching and is
     caught by this.
  2. Number-set reuse: for each course problem (split on '#### Problem' / 'Question N'
     headings), the multiset of numeric literals it contains. A foundations exercise
     block that contains the same multiset (size >= MIN_NUMBERS) is flagged.

Exit code 1 if anything is flagged. Zero flags is the pass condition. A flag is a review
item: one on a standard definition the problem merely restates is a false positive to
dismiss in writing; one on a worked example is a real collision to fix.
"""

import re
import sys
from collections import Counter
from pathlib import Path

MIN_NUMBERS = 3          # distinct numeric literals a block needs before its number set counts
GENERIC = {"0", "1", "2"}   # a number set drawn only from these is not a fingerprint

# Standard definitions that a problem statement may restate and a primer may legitimately
# repeat. Extend when a flag is a definition, not a worked example - and say so in the commit.
KNOWN_DEFINITIONS = {
    r"\begin{pmatrix}0&1\\1&0\end{pmatrix}",      # sigma_x
    r"\begin{pmatrix}0&-i\\i&0\end{pmatrix}",     # sigma_y
    r"\begin{pmatrix}1&0\\0&-1\end{pmatrix}",     # sigma_z
    r"\begin{pmatrix}1&0\\0&1\end{pmatrix}",      # identity
    r"\begin{pmatrix}1\\0\end{pmatrix}", r"\begin{pmatrix}0\\1\end{pmatrix}",   # basis kets
}

MATH = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)
NUM = re.compile(r"(?<![A-Za-z\\])(?:\d+\.\d+|\d+)(?![A-Za-z])")
PROBLEM_SPLIT = re.compile(r"^#{2,5}\s*(?:Problem|Question|Exercise)\s*\d+", re.M | re.I)
EXERCISE_SPLIT = re.compile(r"^(?:#{2,5}\s*.*(?:Exercise|Problem|Clone|Cold attempt).*|\d+\.\s)", re.M | re.I)


def norm(s):
    return re.sub(r"\s+", "", s)


INSTANCE = re.compile(
    r"\\(?:exp|sin|cos|tan|sinh|cosh|ln|log)\s*\((?:[^()]|\([^()]*\))*\)"   # \exp( ... ) one nesting level
    r"|e\^\{[^{}]+\}"                                                          # e^{...}
    r"|\\frac\{(?:[^{}]|\{[^{}]*\})+\}\{(?:[^{}]|\{[^{}]*\})+\}"   # \frac{..}{..}, one nesting level
    r"|\\sqrt\{[^{}]+\}"                                                      # \sqrt{..}
    r"|\\begin\{[pbv]matrix\}.*?\\end\{[pbv]matrix\}",                      # matrices
    re.S,
)
MIN_INSTANCE = 10
# Ubiquitous instances that identify nothing. Extend with care, and say why in the commit.
GENERIC_INSTANCES = {
    r"\frac{1}{2}", r"\frac{1}{\sqrt{2}}", r"\frac{\sqrt{2}}{2}", r"\sqrt{2}", r"\sqrt{3}",
    r"e^{i\theta}", r"e^{-i\theta}", r"e^{ikx}", r"e^{-ikx}", r"\frac{\hbar}{i}",
    r"\frac{\hbar^2}{2m}", r"\frac{1}{\sqrt{N}}", r"\frac{d}{dx}", r"\frac{\partial}{\partialx}",
    r"\frac{\hbar}{2}", r"\frac{1}{2}\hbar\omega", r"\sqrt{\frac{m\omega}{\hbar}}",
    r"e^{-iE_nt/\hbar}", r"e^{-iEt/\hbar}", r"e^{-i\omegat}", r"e^{i(kx-\omegat)}",   # universal phases
}


CONCRETE_NUM = re.compile(r"[3-9]|\d\.\d|\d{2,}")
MATRIX_ENTRY_GENERIC = re.compile(r"^[+-]?(0|1|i)$")


def is_identifying(i):
    """Would a clone have to change this? Functional forms: yes. Symbolic fractions: no."""
    if i.startswith("\\begin{"):
        body = re.sub(r"\\begin\{[pbv]matrix\}|\\end\{[pbv]matrix\}", "", i)
        entries = re.split(r"&|\\\\", body)
        return any(not MATRIX_ENTRY_GENERIC.match(e) for e in entries if e)
    if i.startswith("\\frac") or i.startswith("\\sqrt"):
        return bool(CONCRETE_NUM.search(i))
    return True                                   # \exp(...), e^{...}, \sin(...): always


def math_snippets(text):
    """Concrete instances found inside the math of `text`, whitespace-normalised."""
    out = set()
    for a, b in MATH.findall(text):
        for inst in INSTANCE.findall(a or b):
            i = norm(inst)
            if (len(i) >= MIN_INSTANCE and i not in GENERIC_INSTANCES
                    and i not in KNOWN_DEFINITIONS and is_identifying(i)):
                out.add(i)
    return out


def number_sets(text, splitter):
    blocks = splitter.split(text)
    sets = []
    for blk in blocks:
        nums = NUM.findall(blk)
        distinct = set(nums)
        if len(distinct) >= MIN_NUMBERS and not distinct <= GENERIC:
            sets.append(frozenset(Counter(nums).items()))
    return sets


def files_under(arg):
    p = Path(arg)
    if p.is_dir():
        return [f for f in p.rglob("*.md")]
    return [p] if p.suffix == ".md" else []


def entities_main(entities_file, found_arg):
    names = [l.strip() for l in Path(entities_file).read_text(encoding="utf-8").splitlines()
             if l.strip() and not l.startswith("#")]
    found_files = files_under(found_arg)
    flags = 0
    for f in found_files:
        t = f.read_text(encoding="utf-8", errors="ignore")
        low = t.lower()
        for n in names:
            if n.lower() in low:
                flags += 1
                print(f"ENTITY    {f}  mentions forbidden entity: {n}")
    print(f"\n{len(names)} forbidden entities, {len(found_files)} foundations files, {flags} flag(s)")
    return 1 if flags else 0


def main(argv):
    if len(argv) == 4 and argv[1] == "--entities":
        return entities_main(argv[2], argv[3])
    if len(argv) < 3:
        print(__doc__)
        return 2
    *course_args, found_arg = argv[1:]
    course_files = [f for a in course_args for f in files_under(a)]
    found_files = files_under(found_arg)
    if not course_files or not found_files:
        print("no files to compare")
        return 2

    course_snips, course_numsets = {}, {}
    for f in course_files:
        if "lecture" in f.name:
            continue                                   # notation, not problems
        t = f.read_text(encoding="utf-8", errors="ignore")
        if "content" in f.name:
            parts = PROBLEM_SPLIT.split(t)
            t = "\n".join(parts[1:]) if len(parts) > 1 else ""   # drop intro/explore prose
        for s in math_snippets(t):
            course_snips.setdefault(s, f)
        for ns in number_sets(t, PROBLEM_SPLIT):
            course_numsets.setdefault(ns, f)

    flags = 0
    for f in found_files:
        t = f.read_text(encoding="utf-8", errors="ignore")
        for s in math_snippets(t):
            if s in course_snips:
                flags += 1
                print(f"INSTANCE  {f}  reuses {s[:70]}  from {course_snips[s]}")
        for ns in number_sets(t, EXERCISE_SPLIT):
            if ns in course_numsets:
                flags += 1
                nums = sorted(n for n, _ in ns)
                print(f"NUMBERS   {f}  reuses number set {nums} from {course_numsets[ns]}")

    print(f"\n{len(course_files)} course files, {len(found_files)} foundations files, {flags} flag(s)")
    return 1 if flags else 0


# ---------------------------------------------------------------------
# Self-test: the detector must keep catching the lazy clone and passing the
# honest one. Run after any edit to this file:
#     python3 check_clones.py --selftest
# ---------------------------------------------------------------------
COURSE_FIXTURE = r"""
### Question 1 (8 pts)
Consider $\hat{A} = \begin{pmatrix} -3 & 2i \\ -2i & -3 \end{pmatrix}$. Prove it is Hermitian.
### Question 2 (7 pts)
$$\psi(x) = \begin{cases} B \exp(\beta x) & x < 0 \\ B \exp(-2\beta x) & x \ge 0 \end{cases}$$
### Question 10 (8 pts)
$$|\psi\rangle = \frac{1}{\sqrt{3}}|\phi_1\rangle - \frac{\sqrt{2}}{\sqrt{3}}|\phi_2\rangle + \frac{i}{\sqrt{3}}|\phi_3\rangle$$
"""
LAZY_CLONE = r"""Exercise 1. Normalise $\psi(x) = B \exp(\beta x)$ for $x<0$ and $B\exp(-2\beta x)$ for $x \ge 0$.
Exercise 2. Show $\begin{pmatrix} -3 & 2i \\ -2i & -3 \end{pmatrix}$ is Hermitian.
Exercise 3. State $\frac{1}{\sqrt{3}}|a\rangle - \frac{\sqrt{2}}{\sqrt{3}}|b\rangle$.
"""
HONEST_CLONE = r"""Exercise 1. Normalise $\phi(x) = C \exp(3\gamma x)$ for $x<0$ and $C\exp(-\gamma x)$ for $x \ge 0$.
Exercise 2. Show $\begin{pmatrix} 2 & -5i \\ 5i & 2 \end{pmatrix}$ is Hermitian.
Exercise 3. State $\frac{1}{\sqrt{5}}|a\rangle - \frac{2}{\sqrt{5}}|b\rangle$. Also $\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$.
"""


def selftest():
    import tempfile, io, contextlib
    with tempfile.TemporaryDirectory() as d:
        course = Path(d, "course"); course.mkdir()
        (course / "Assessment_1_Problem_Set.md").write_text(COURSE_FIXTURE)
        found = Path(d, "found"); found.mkdir()
        results = {}
        for name, text in [("lazy", LAZY_CLONE), ("honest", HONEST_CLONE)]:
            (found / "day01.md").write_text(text)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = main(["x", str(course), str(found)])
            flags = sum(1 for l in buf.getvalue().splitlines() if l.startswith(("INSTANCE", "NUMBERS")))
            results[name] = (rc, flags)
        ent = Path(d, "forbidden.txt"); ent.write_text("# course instances\nAcme Quantum Ltd\nthe Bristol clock case\n")
        (found / "day01.md").write_text("Apply the model to Acme Quantum Ltd, then to a fictional firm.")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ent_lazy = main(["x", "--entities", str(ent), str(found)])
        (found / "day01.md").write_text("Apply the model to LattisTime Ltd, a fictional firm.")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ent_honest = main(["x", "--entities", str(ent), str(found)])
    lazy_rc, lazy_flags = results["lazy"]
    honest_rc, honest_flags = results["honest"]
    ok = (lazy_rc == 1 and lazy_flags >= 4 and honest_rc == 0
          and ent_lazy == 1 and ent_honest == 0)
    print(f"  entity reuse : {'PASS' if ent_lazy == 1 else 'FAIL'} (lazy flagged)   {'PASS' if ent_honest == 0 else 'FAIL'} (fictional case passes)")
    print(f"  lazy clone   : {lazy_flags} flags (want >= 4: exp x2, matrix, state x2)  {'PASS' if lazy_rc == 1 and lazy_flags >= 4 else 'FAIL'}")
    print(f"  honest clone : {honest_flags} flags (want 0)                             {'PASS' if honest_rc == 0 else 'FAIL'}")
    print("SELFTEST " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    sys.exit(main(sys.argv))
