# Design: Quantum Computing Learning System
**Date:** 2026-06-02
**Module:** Foundations of Quantum Computing (8-week, Sussex MSc Quantum Technology Applications and Management)
**Status:** Approved — ready for implementation plan

---

## 1. Problem Statement

The learner has a computer science background (Go, Python) but is missing the mathematical prerequisites for this module: linear algebra, complex numbers, probability theory, and trigonometry. The module is 8 weeks with a midterm assignment after week 4. Weeks 1–4 PDFs are available now; weeks 5–8 arrive later.

Without a structured system, there is a risk of:
- Hitting week 2 (linear algebra + complex numbers) without the prerequisites in place
- Having no runnable code to verify understanding of abstract quantum concepts
- Losing progress context when switching machines or resuming after a break

---

## 2. Goal

Produce a committed, portable learning system inside the existing `module_1_foundation_of_quantum_computing/` directory that contains:

1. **A master roadmap** (`roadmap.md`) — 8-week schedule, midterm checklist, tools, priority stack
2. **Prerequisites folder** — ranked crash course guide + 10-day sprint schedule
3. **Per-week folders** (weeks 1–4 now; 5–8 added as PDFs arrive) — each with a study notes doc and a runnable Python exercise file
4. **A continuation artifact** (`CONTINUATION.md`) — lets the learner resume in a new Claude Code session on any machine

---

## 3. Repository Structure

```
module_1_foundation_of_quantum_computing/
│
├── roadmap.md
├── prerequisites/
│   ├── crash_courses.md
│   └── study_schedule.md
├── week_1/
│   ├── study_notes.md
│   └── exercises.py
├── week_2/
│   ├── study_notes.md
│   └── exercises.py
├── week_3/
│   ├── study_notes.md
│   └── exercises.py
├── week_4/
│   ├── study_notes.md
│   └── exercises.py
└── [week_5/ … week_8/ added when PDFs arrive]

CONTINUATION.md                          ← repo root
docs/superpowers/specs/
  2026-06-02-quantum-learning-system-design.md  ← this file
```

Existing PDFs remain in place. `rough_4w_plan.md` is superseded by this system and will be deleted.

---

## 4. File Content Specifications

### 4.1 `roadmap.md`

The master entry point. Sections:

| Section | Content |
|---------|---------|
| Course content map | Table: week number, core topics, prerequisites needed |
| 8-week schedule | Week-by-week goals, daily targets for weeks 1–4 |
| Midterm checklist | Topic → what you must be able to do (9 topics) |
| Priority stack | "What to do right now" summary — one line per phase |
| Tools | `pip install numpy scipy matplotlib qiskit` |
| Weeks 5–8 | Placeholder section, marked `[TBD — materials pending]` |

### 4.2 `prerequisites/crash_courses.md`

One section per prerequisite, in priority order:

1. **Linear Algebra** (HIGHEST — affects weeks 2–4 and all later weeks)
   - Crash course: 3Blue1Brown "Essence of Linear Algebra" (YouTube, 16 videos ≈ 2.5 hrs)
   - Supplementary: Khan Academy "Linear Algebra"
   - Must cover: vectors, linear transformations, matrix multiplication, dot products, change of basis, eigenvalues/eigenvectors
   - Estimated time: 3–4 days at 1 hr/day

2. **Complex Numbers** (HIGH — starts week 2, never goes away)
   - Crash course: Khan Academy "Complex numbers" (1–2 hrs) or 3Blue1Brown "Euler's formula" (24 min)
   - Must cover: arithmetic, conjugates, polar form (`re^{iθ}`), Euler's formula, modulus
   - Estimated time: 1–2 days

3. **Probability Theory** (MEDIUM — needed from week 1 randomised computation)
   - Crash course: Khan Academy "Statistics & Probability"; Seeing Theory (seeing-theory.brown.edu)
   - Must cover: distributions over finite sets, expected value, stochastic matrices
   - Estimated time: 1–2 days

4. **Trigonometry** (LIGHT — unit circle and sin/cos, week 2 onwards)
   - Khan Academy "Trigonometry" → "Unit circle" (30–45 min)
   - Must cover: radians vs degrees, sin/cos definitions, `sin²(θ) + cos²(θ) = 1`

### 4.3 `prerequisites/study_schedule.md`

Day-by-day 10-day sprint table:

| Days | Activity | Time | Unlocks |
|------|----------|------|---------|
| 1–2 | 3B1B linear algebra videos 1–8 (vectors → dot product) | ~2 hrs | Week 2 partial |
| 3–4 | 3B1B linear algebra videos 9–16 (change of basis → eigenvalues) | ~2 hrs | Week 2 full |
| 5 | Complex numbers (Khan Academy + Euler's formula) | ~2 hrs | Week 2 |
| 6 | Trig refresher (unit circle) + probability distributions | ~2 hrs | Week 1, 2 |
| 7 | Stochastic matrices, transition matrices | ~1.5 hrs | Week 1 |
| 8–10 | Re-read Week 1 + Week 2 PDFs with new eyes | 3 hrs total | Midterm |

### 4.4 `week_N/study_notes.md` (template applied to each week)

```markdown
## Week N — [Title]

### Core Topics
[From the PDF — section headings and one-line summaries]

### Key Concepts & Vocab
[Definitions of terms introduced this week]

### What This Unlocks
[Why this week's content matters for subsequent weeks / quantum computing generally]

### Common Confusion Points
[Known hard spots flagged during the brainstorming session]

### Prerequisite Links
[Which crash course sections to review if struggling]
```

### 4.5 `week_N/exercises.py` (conventions applied to each week)

```python
# Week N — [Title]
# Run: python exercises.py
# Requires: numpy [+ qiskit for week 4+]

import numpy as np

# ---------------------------------------------------------------------------
# Exercise N.1: [Name matching PDF section]
# [Problem statement in a comment block]
# ---------------------------------------------------------------------------
# ... solution code ...
# Verify:
assert ..., "Exercise N.1 failed"
print("Exercise N.1 passed: ...")
```

- Exercises are numbered `Week.Exercise` (e.g., `1.1`, `2.3`)
- Each exercise targets the key skill from a specific PDF section concept
- Every exercise ends with an `assert` or `print` so the learner gets immediate feedback
- Running `python exercises.py` from the week folder should produce all-green output

---

## 5. Per-Week Content (Weeks 1–4)

### Week 1 — Boolean Logic, Reversible & Randomised Computation
**PDF sections:** 1.1 Boolean logic, 1.2 Reversible computation, 1.3 Randomised computation

**Study notes focus:**
- Why binary encoding → all computation reducible to bits
- Why AND/OR are NOT reversible; why CNOT/Toffoli are
- Probability vectors in ket notation as the bridge to quantum

**Exercises (12 numbered 1.1–1.3 across three themes):**
- `1.1`: Binary encoding for integers 0–15
- `1.2`: Truth tables for NOT/AND/OR/XOR
- `1.3`: Stochastic matrix applied to a probability vector (coin flip)

### Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits
**PDF sections:** 2.1 Algebra/geometry of 2D plane, 2.2 Complex numbers, 2.3 Eigenvectors/eigenvalues/normal matrices, 2.4 Single-qubit states and measurements

**Study notes focus:** This is the hardest week. Go slow; return to prerequisites after each section.

**Exercises (numbered 2.1–2.7):**
- `2.1`: Inner products and norms in ket notation
- `2.2`: Complex arithmetic and Euler's formula
- `2.3`: Eigenvalues/eigenvectors of Pauli Z and X
- `2.4`: Bloch sphere state construction and norm verification

### Week 3 — Single-Qubit Gates, Bloch Sphere, Multi-Qubit Systems
**PDF sections:** 3.1 Single-qubit unitary transformations, 3.2 Multi-qubit states and transformations, 3.3 Measurement and multi-qubit states

**Exercises (numbered 3.1–3.4):**
- `3.1`: Verify X/Y/Z/H are unitary (`U†U = I`)
- `3.2`: Tensor products for 2-qubit states
- `3.3`: Construct Bell state |Φ+⟩ via H⊗I then CNOT
- `3.4`: Apply rotation gates and verify Bloch sphere position

### Week 4 — Teleportation, Phase Estimation (Pre-Midterm)
**PDF sections:** 4.1 Quantum teleportation, 4.2 Hadamard operations and phase estimation

**Exercises (numbered 4.1–4.2):**
- `4.1`: Construct and verify all four Bell states
- `4.2`: Trace through teleportation protocol algebraically

---

## 6. Continuation Artifact (`CONTINUATION.md`)

Lives at the repo root. Contains:

1. **What has been built** — list of all files created and committed
2. **Implementation plan status** — which tasks from writing-plans are done/pending
3. **Resume prompt** — exact text to paste into a new Claude Code session:
   > "I'm continuing my quantum computing learning system for Sussex MSc. The design spec is at `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md` and the implementation plan is at `docs/superpowers/plans/2026-06-02-quantum-learning-system-plan.md`. [Remaining tasks here]. Please read both files and continue from task N."

---

## 7. Out of Scope

- Weeks 5–8 content (PDFs not yet available — placeholder only)
- Automated progress tracking or CI
- A web UI or dashboard
- Anki flashcard export
- Any content beyond what is derivable from the 4 PDFs already in the repo

---

## 8. Success Criteria

- [ ] `python week_N/exercises.py` runs without errors for weeks 1–4
- [ ] `roadmap.md` gives a complete picture of the 8-week plan in one read
- [ ] Prerequisite crash courses are actionable: platform + topic + estimated hours, no vague links
- [ ] Study notes for each week align with the corresponding PDF section headings
- [ ] `CONTINUATION.md` is sufficient to resume work in a fresh Claude Code session on a different machine
- [ ] All files are committed to git and pushable to GitHub
