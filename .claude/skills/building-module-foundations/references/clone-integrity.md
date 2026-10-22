# Clone integrity

Companions and days teach by worked examples. Those examples must not be the course's own task,
portfolio or quiz problems, and must not be those problems with one number changed.

**Why it is strict:** in Module 3, several plan-suggested clones matched real course task
instances and had to be swapped after review. The assignment brief says the learner's workings
must be their own; a sprint that pre-solves the assessed problems undermines that and risks the
Turnitin match being *prose*, which is the only kind that matters.

## The rule

A clone shares the **type** (same move, same structure) and nothing else:

| May share | Must differ |
|---|---|
| The operation (normalise, find eigenvalues, expand in a basis) | Every numeric coefficient |
| The notation and write-up shape | The functional form (e^{-2x} vs e^{-x^2}, sin vs cos) |
| The physical setting at concept level | Operator entries, state vectors, limits of integration |

"Adapted from Week 3 Problem 2" is a red flag, not a citation.

## The mechanical check

```bash
python3 .claude/skills/building-module-foundations/assets/check_clones.py \
    module_N_<slug>/week_*/ module_N_<slug>/foundations_sprint/content/
```

Course side is **problem statements only** (the Problem/Question blocks of `week_K_content.md`,
plus hint and model-answer files); lectures are excluded, because standard notation recurs
everywhere and is not a clone. From those it extracts every *concrete instance* - `\exp(...)`,
`e^{...}`, `\sin(...)`, fractions and roots with concrete numbers, matrices with entries beyond
0, +-1, +-i - and flags any foundations file containing the same instance. A second detector
flags an exercise reusing a problem's whole set of numbers.

Zero flags is the pass condition; the real Module 3 sprint passes. Run it in phase 4 and after
any content edit. After editing the script itself, run `check_clones.py --selftest`. Self-tests it
has to keep passing: a planted copy of Assessment 1's
`B\exp(\beta x)`, its `-3, 2i` matrix and its `1/sqrt(3), sqrt(2)/sqrt(3)` state are flagged;
the same problems with a different function, matrix and state are not.

A flag is a review item. One on a standard definition a problem merely restates is a false
positive - add it to `KNOWN_DEFINITIONS` or `GENERIC_INSTANCES` and say why. One on a worked
example is a real collision: change the function, the numbers and the operator, not one of them.
The check cannot judge *type*; a clone that is structurally identical with everything concrete
changed is exactly what you want.

## Qualitative modules

There is no LaTeX to fingerprint, so the maths detectors pass vacuously - a GREEN-phase test
agent on Module 2 pointed this out. The instance of a business-module task is its **named
case**: the firm, the country programme, the dataset, the lecture's own worked example, and the
learner's chosen subsectors once known. Phase 0 lists them in
`foundations_sprint/docs/clone_forbidden_entities.txt`, one per line; framework and author names
(Teece, Pavitt, Tidd and Bessant) are the subject matter and do not go in. Then:

```bash
python3 .claude/skills/building-module-foundations/assets/check_clones.py \
    --entities module_N_<slug>/foundations_sprint/docs/clone_forbidden_entities.txt \
    module_N_<slug>/foundations_sprint/content/
```

Clones use a fictional running case instead, built once and reused across days.
