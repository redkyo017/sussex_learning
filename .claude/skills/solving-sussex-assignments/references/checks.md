# Checks: sources, answers, admin

Three mechanical passes. None takes long; each has caught a real problem.

## 1. Diff the sources (phase 1)

Assignment materials arrive in more than one copy: a Canvas markdown export, an instructor LaTeX
template, a PDF, the module intro. **They disagree, and the export is usually the corrupted one.**

Real instance: a Canvas markdown export silently dropped every `\sqrt` command. `\frac{1}{\sqrt{7}}`
became `\frac{1}{7}` and `\sqrt{2}` became `2`, in three separate places. The answers changed.

Do not rely on spotting this by physics intuition. It worked in that case only because the damaged
state was visibly un-normalised; a dropped exponent or flipped sign gives no such tell. Diff
mechanically instead:

```bash
# pull the same question from each source and compare side by side
grep -A6 "A system is prepared" assignment_1/Assessment_Problem_Set.md
grep -A6 "A system is prepared" latex_tutorial/*template*.tex
```

**Precedence: instructor-authored originals (.tex, .pdf, .docx) beat platform exports.** The export
is a lossy rendering of the original.

Then check internal consistency, which catches corruption with no visual tell:

- Do the per-question marks sum to the stated total?
- Is a state that should be normalised actually normalised?
- Does the question count match the number of questions?
- Do two files quote the same deadline?

### Compute every reading. Never judge by inspection whether it matters.

**Work each variant through to a number and put every number in `NOTES.md`.** Do not reason about
whether a discrepancy affects the answer - compute it. This is not a formality; a GREEN-phase test
agent skipped it and wrote a false reassurance into the student's notes.

Its reasoning: *"This does not change the numerical answer to Question 1, because the coefficient
of |phi2> (the one the question asks about) is 1/2 in both versions."*

That is wrong, and the trap is worth internalising. The coefficient asked about was indeed
identical. But probability is

```
P(b_i) = |c_i|^2 / <psi|psi>
```

and the two sources differed in a *different* coefficient, which changes the **norm in the
denominator**:

| Source | c2 | <psi\|psi> | P(b2) |
|---|---|---|---|
| Canvas export | 1/2 | 3/4 | **1/3** |
| Instructor template | 1/2 | 1 | **1/4** |

Same numerator, different answer. Had the live quiz shown the export's version, the student would
have submitted 1/4 against a correct answer of 1/3 - while their notes told them the discrepancy
was harmless and there was no need to check.

**The rule: any change anywhere in a state changes the norm, so it changes every probability
derived from that state.** The same holds for any normalised quantity - expectation values,
densities. Compute both, record both, and tell the student exactly what to verify on the live
platform. Never silently pick one reading, and never declare a discrepancy immaterial.

## 2. Verify answers independently (phase 4)

**A check that re-runs the same algebra is not a check.** Use a different mechanism:

| Result type | Independent check |
|---|---|
| Definite integral | Numerical quadrature |
| Operator identity, commutator | Finite differences on a sample function |
| Eigenvalues, Hermiticity | `numpy.linalg` |
| Probability set | Sums to 1, each in [0,1] |
| Any physical quantity | Dimensional analysis; a limiting case |
| General result | Must reproduce the special case computed earlier |

`assets/verify_template.py` is the working pattern - adapt it per assignment and keep it beside the
solutions so the numbers can be re-checked after any edit.

Also verify the document, not just the maths:

```bash
tectonic -X compile --keep-logs solutions.tex
grep -cE "Overfull \\\\hbox" solutions.log         # want 0
grep -cE "Reference.*undefined" solutions.log      # want 0
```

Then **read every rendered page**. Structural checks pass on documents that look wrong: a label
glued to a command, a mark tag broken across lines, a figure caption colliding with a curve. All
three were found by looking, after automated checks reported clean.

## 3. Admin sweep before handing off

Cheap, and baseline agents missed these while concentrating on the physics.

- [ ] **Deadline** - check *every* file. Real instance: a Canvas page said 23:00, the module intro
      said 17:00 UK the same week. Treat the earlier as real and say so.
- [ ] **Lateness policy** - typically a 24-hour window at a flat 5 percentage-point penalty.
- [ ] **Candidate number, not name** - marking is anonymous. A template ships with a placeholder
      like `123456`; it must be replaced, and "still a placeholder" is a blocking finding.
- [ ] **Word count and what counts toward it** - read the brief's phrasing precisely. "4 worksheets
      *equivalent to 500 words*" meant the worksheets *were* the word count; adding an essay would
      have doubled the assessed length.
- [ ] **Submission mechanics** - how many boxes, which accept files, what format.
- [ ] **Numbering mismatch** - if the platform splits questions differently from the document,
      cross-reference both ways so a marker entering at any number lands in the right place.
