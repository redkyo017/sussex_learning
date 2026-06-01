# Quantum Learning System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a committed, portable quantum computing learning system inside `module_1_foundation_of_quantum_computing/` with a master roadmap, prerequisite guides, and per-week study notes + runnable Python exercises for weeks 1–4.

**Architecture:** Flat per-week folder structure — each week folder contains exactly one `study_notes.md` (concepts, vocab, confusion points) and one `exercises.py` (runnable NumPy/Python practice with asserts). A top-level `roadmap.md` and `prerequisites/` folder serve as entry points. A `CONTINUATION.md` at the repo root captures session state for resuming on another machine.

**Tech Stack:** Python 3, NumPy, Qiskit (week 4+). Markdown for all documentation.

**Spec:** `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `module_1_foundation_of_quantum_computing/roadmap.md` | Master 8-week plan, midterm checklist, priority stack |
| Create | `module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md` | Ranked prerequisite resources with time estimates |
| Create | `module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md` | Day 1–10 sprint schedule |
| Create | `module_1_foundation_of_quantum_computing/week_1/study_notes.md` | Boolean logic, reversible, randomised computation notes |
| Create | `module_1_foundation_of_quantum_computing/week_1/exercises.py` | Exercises 1.1–1.3: binary encoding, truth tables, stochastic matrices |
| Create | `module_1_foundation_of_quantum_computing/week_2/study_notes.md` | 2D geometry, complex numbers, eigenvalues, single qubits |
| Create | `module_1_foundation_of_quantum_computing/week_2/exercises.py` | Exercises 2.1–2.4: inner products, complex arithmetic, eigenvectors, Bloch sphere |
| Create | `module_1_foundation_of_quantum_computing/week_3/study_notes.md` | Single-qubit gates, Bloch sphere, multi-qubit systems |
| Create | `module_1_foundation_of_quantum_computing/week_3/exercises.py` | Exercises 3.1–3.4: unitarity, tensor products, Bell state, rotations |
| Create | `module_1_foundation_of_quantum_computing/week_4/study_notes.md` | Quantum teleportation, Hadamard, phase estimation |
| Create | `module_1_foundation_of_quantum_computing/week_4/exercises.py` | Exercises 4.1–4.2: Bell states, teleportation algebra |
| Create | `CONTINUATION.md` | Resume-from-here prompt for new Claude Code session |
| Delete | `module_1_foundation_of_quantum_computing/rough_4w_plan.md` | Superseded by this system |

---

## Task 1: Scaffold directory structure

**Files:**
- Create dirs: `week_1/`, `week_2/`, `week_3/`, `week_4/`, `prerequisites/`
- Delete: `module_1_foundation_of_quantum_computing/rough_4w_plan.md`

- [ ] **Step 1.1: Create week and prerequisite directories**

```bash
cd module_1_foundation_of_quantum_computing
mkdir -p week_1 week_2 week_3 week_4 prerequisites
```

Expected: no output, directories created.

- [ ] **Step 1.2: Verify directories exist**

```bash
ls module_1_foundation_of_quantum_computing/
```

Expected output includes: `prerequisites/  week_1/  week_2/  week_3/  week_4/`

- [ ] **Step 1.3: Delete the superseded rough plan**

```bash
git rm module_1_foundation_of_quantum_computing/rough_4w_plan.md
```

Expected: `rm 'module_1_foundation_of_quantum_computing/rough_4w_plan.md'`

- [ ] **Step 1.4: Commit**

```bash
git add module_1_foundation_of_quantum_computing/
git commit -m "scaffold: add week_1-4 and prerequisites directories, remove rough plan"
```

---

## Task 2: Create `roadmap.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/roadmap.md`

- [ ] **Step 2.1: Write `roadmap.md`**

Create `module_1_foundation_of_quantum_computing/roadmap.md` with this exact content:

```markdown
# Foundations of Quantum Computing — 8-Week Roadmap
**Programme:** MSc Quantum Technology Applications and Management, Sussex
**Module:** Module 1 — Foundations of Quantum Computing

---

## Course Content Map

| Week | Core Topics | Prerequisites Needed |
|------|-------------|---------------------|
| 1 | Boolean logic, Reversible computation, Randomised computation | Probability basics |
| 2 | 2D algebra, Complex numbers, Eigenvectors/eigenvalues, Single-qubit states | **Linear algebra**, **complex numbers**, trig |
| 3 | Single-qubit unitaries, Bloch sphere, Multi-qubit states & transformations | Linear algebra (matrices, unitary), trig |
| 4 | Quantum teleportation, Bell states, Hadamard, Phase estimation | Everything from weeks 1–3 |
| 5 | Quantum algorithms intro (Deutsch-Jozsa, Bernstein-Vazirani) | Weeks 1–4 complete |
| 6 | Quantum Fourier Transform | Week 5 |
| 7 | Grover's search algorithm | Week 6 |
| 8 | Shor's algorithm overview / error correction intro | Week 7 |

> Weeks 5–8: [TBD — study materials pending]

---

## Priority Stack

```
NOW (before week 2):  3Blue1Brown Linear Algebra → Complex Numbers → Probability basics
WEEK 1 study:         Boolean/reversible/randomised — leans on CS background, focus on prob vectors
WEEK 2 study:         Hardest week — go slow, return to prerequisites after each section
WEEK 3 study:         Gates, Bloch sphere — run the Python exercises after each section
WEEK 4 study:         Teleportation — follow the algebra step by step, don't try to memorise
MIDTERM PREP:         3 days: work problems by hand, then verify with code
```

---

## Midterm Checklist (End of Week 4)

| Topic | Must be able to do |
|-------|-------------------|
| Boolean logic | Write truth tables; prove universality with AND/OR/NOT |
| Reversible gates | Draw a CNOT/Toffoli circuit; explain why AND is not reversible |
| Randomised computation | Multiply a stochastic matrix by a probability vector |
| Linear algebra | Inner products, matrix multiplication, prove U†U = I |
| Complex numbers | Polar form, conjugates, Euler's formula `e^{iθ} = cosθ + i sinθ` |
| Eigenvectors | Find eigenvalues/vectors of a 2×2 matrix by hand |
| Qubit states | Parameterise a Bloch sphere state; compute Born-rule probabilities |
| Multi-qubit | Write 2-qubit state as tensor product; construct |Φ+⟩ via H+CNOT |
| Teleportation | Explain all protocol steps; trace the algebra for one Bell outcome |

---

## Midterm Prep Drill (Last 3 Days Before Assignment)

1. Do all exercises in `week_1/` through `week_4/` **by hand on paper first**, then verify with Python
2. Re-read the Week 1–4 PDFs and complete any embedded exercises
3. Checkpoint: can you (a) construct |Φ+⟩ from scratch, (b) verify H is unitary, (c) multiply a stochastic matrix by a probability vector?

---

## Tools

```bash
pip install numpy scipy matplotlib qiskit
```

Qiskit provides a local quantum circuit simulator that mirrors the QAAL notation used in the course PDFs.

---

## Resources for Weeks 5–8 (Pre-Study)

- **IBM Qiskit Textbook** — free at learning.qiskit.org; chapters on Deutsch-Jozsa, Grover, QFT map directly to this course
- **Quantum Country** — quantumcountry.com; spaced-repetition quantum textbook by Andy Matuschak, excellent for retention
```

- [ ] **Step 2.2: Verify file has required sections**

```bash
grep -c "^##" module_1_foundation_of_quantum_computing/roadmap.md
```

Expected: `5` (five `##` headings)

- [ ] **Step 2.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/roadmap.md
git commit -m "docs: add 8-week roadmap with midterm checklist and priority stack"
```

---

## Task 3: Create `prerequisites/crash_courses.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md`

- [ ] **Step 3.1: Write `crash_courses.md`**

Create `module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md`:

```markdown
# Prerequisite Crash Courses

Work through these **in order** — each one unlocks the next week of the module.

---

## 1. Linear Algebra — HIGHEST PRIORITY

**Why:** Weeks 2–4 are built entirely on vectors, matrices, inner products, eigenvalues, and unitary transformations. Without this, you will memorise symbols without understanding what they mean. This is the single highest-ROI thing you can do before week 2.

**Crash course:** 3Blue1Brown — "Essence of Linear Algebra" (YouTube, free)
- 16 videos, ~10 min each ≈ 2.5 hrs total
- Search: `3Blue1Brown essence of linear algebra`

**Must-watch chapters (do not skip):**
- Vectors, what even are they?
- Linear combinations, span, and basis vectors
- Linear transformations and matrices
- Matrix multiplication as composition
- The determinant
- Dot products and duality
- Change of basis
- Eigenvectors and eigenvalues

**Supplementary (for computation practice):** Khan Academy → "Linear Algebra" section

**Must be able to do before Week 2:**
- Multiply two matrices by hand
- Compute the dot product (inner product) of two vectors
- Find eigenvalues and eigenvectors of a 2×2 matrix
- Explain what "change of basis" means geometrically

**Estimated time:** 3–4 days at 1 hr/day

---

## 2. Complex Numbers — HIGH PRIORITY

**Why:** Every quantum state vector has complex-number amplitudes. Week 2 introduces ket notation with complex entries; from week 3 onward all the math is complex-valued.

**Crash course (pick one):**
- Khan Academy → "Complex numbers" section (under Algebra 2 or Precalculus) — 1–2 hrs
- 3Blue1Brown — "Euler's formula with introductory group theory" — 24 min for the geometric intuition the course uses directly

**Must be able to do before Week 2:**
- Multiply complex numbers: `(a+bi)(c+di)`
- Compute the conjugate: `a+bi → a−bi`
- Convert to polar form: `re^{iθ} = r(cosθ + i sinθ)` — Euler's formula
- Compute the modulus: `|a+bi| = √(a²+b²)`

**Estimated time:** 1–2 days

---

## 3. Probability Theory — MEDIUM PRIORITY

**Why:** Week 1's randomised computation section uses probability vectors (stochastic vectors) and matrix–vector products where matrices are row-stochastic. Week 2 connects this notation directly to quantum amplitudes.

**Crash course:**
- Khan Academy → "Statistics & Probability" — focus on: basic probability, probability distributions, expected value
- Seeing Theory (seeing-theory.brown.edu) — browser-based visual intro, builds intuition in 1–2 hrs

**Must be able to do before Week 1:**
- Write a probability distribution over a finite set
- Compute expected value
- Multiply a stochastic (row-sum-to-1) matrix by a probability vector and interpret the result

**Estimated time:** 1–2 days

---

## 4. Trigonometry Refresher — LIGHT

**Why:** The course uses `cos(θ)` and `sin(θ)` for unit vectors and the Bloch sphere. You don't need deep trig — just the unit circle.

**Crash course:** Khan Academy → "Trigonometry" → "Unit circle" — 30–45 min

**Must be able to do before Week 2:**
- Convert between degrees and radians
- Read sin and cos from the unit circle at common angles (0, π/6, π/4, π/3, π/2, π)
- Use the identity `sin²(θ) + cos²(θ) = 1`

**Estimated time:** 30–45 min
```

- [ ] **Step 3.2: Verify four prerequisite sections exist**

```bash
grep -c "^## [0-9]" module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md
```

Expected: `4`

- [ ] **Step 3.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md
git commit -m "docs: add ranked prerequisite crash course guide"
```

---

## Task 4: Create `prerequisites/study_schedule.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md`

- [ ] **Step 4.1: Write `study_schedule.md`**

Create `module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md`:

```markdown
# 10-Day Prerequisite Sprint

Run this **in parallel with starting Week 1** — do not wait until you finish all prerequisites before touching the course material. The sprint is calibrated so each day's study unlocks the next day's course reading.

| Day | Activity | Est. Time | Unlocks |
|-----|----------|-----------|---------|
| 1 | 3B1B linear algebra: videos 1–4 (vectors, linear combinations, span, matrices) | ~45 min | Week 2 partial |
| 2 | 3B1B linear algebra: videos 5–8 (matrix multiplication, 3D transforms, determinant) | ~45 min | Week 2 partial |
| 3 | 3B1B linear algebra: videos 9–12 (dot products, change of basis, eigenvectors intro) | ~45 min | Week 2 full |
| 4 | 3B1B linear algebra: videos 13–16 (eigenvalues, abstract vector spaces, wrap-up) | ~45 min | Week 2 full |
| 5 | Complex numbers: Khan Academy arithmetic + 3B1B Euler's formula video | ~90 min | Week 2 |
| 6 | Trig refresher: unit circle, radians, sin/cos identities (Khan Academy, 45 min) | ~45 min | Week 2 |
| 6 | Probability distributions: Khan Academy basic probability + expected value | ~45 min | Week 1 |
| 7 | Stochastic matrices: Khan Academy Markov chains intro or textbook section 1.3 | ~60 min | Week 1 |
| 8 | Re-read Week 1 PDF (section 1.3 randomised computation) with prerequisites in place | ~60 min | Week 1 complete |
| 9 | Re-read Week 2 PDF (sections 2.1–2.2) with linear algebra + complex numbers in place | ~90 min | Week 2 partial |
| 10 | Re-read Week 2 PDF (sections 2.3–2.4) and run `week_2/exercises.py` | ~90 min | Week 2 complete |

---

## Daily Rhythm

```
Morning (30–45 min):  Prerequisite crash course
Evening (45–60 min):  Course PDF section + matching exercises.py
```

At the end of Day 10 you should be able to run all exercises in `week_1/` and `week_2/` cleanly.
```

- [ ] **Step 4.2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md
git commit -m "docs: add 10-day prerequisite sprint schedule"
```

---

## Task 5: Create `week_1/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_1/study_notes.md`

- [ ] **Step 5.1: Write `week_1/study_notes.md`**

Create `module_1_foundation_of_quantum_computing/week_1/study_notes.md`:

```markdown
# Week 1 — Boolean Logic, Reversible Computation, Randomised Computation

**PDF:** Foundations of Quantum Computing — Week 1 Study
**Sections:** 1.1 Boolean logic · 1.2 Reversible computation · 1.3 Randomised computation

---

## Core Topics

### 1.1 Boolean Logic
- **Binary encoding:** Any finite set can be encoded as n-bit strings `{0,1}^n`. The number of n-bit strings is `2^n`.
- **Logical operators:** NOT (`¬x`), AND (`x & y`), OR (`x ∨ y`), XOR (`x ⊕ y`). XOR = addition mod 2.
- **Algebraic form:** `A & B = AB`, `A ∨ B = A + B − AB`, `A ⊕ B = A + B − 2AB`
- **Universality:** Every boolean function `f: {0,1}^m → {0,1}` can be expressed using only NOT, AND, OR. Key technique: express `f` as an OR of indicator functions `δ_a(x)` for each input `a` where `f(a) = 1`.

### 1.2 Reversible Computation
- A computation is **reversible** if you can recover the input from the output.
- AND, OR, XOR on their own are **not** reversible — e.g., `AND(1,0) = AND(0,1) = 0`, so you can't recover which inputs gave output 0.
- **CNOT gate:** maps `(x, y) → (x, x ⊕ y)`. Reversible: apply it twice to get back the original.
- **Toffoli gate (CCNOT):** maps `(a, b, c) → (a, b, c ⊕ (a & b))`. Universal for reversible computation.
- **Why this matters for quantum:** All quantum gates are unitary, and unitary transformations are reversible. Classical reversible circuits are a special case of quantum circuits.

### 1.3 Randomised Computation
- A **probability vector** over `n` outcomes is a column vector `p` where each entry `p_i ≥ 0` and `Σ p_i = 1`.
- **Ket notation:** `p = Σ p_i |i⟩` where `|i⟩` is the i-th standard basis vector. This is the same notation used later for quantum states.
- A **stochastic matrix** `M` has columns that are probability vectors (each column sums to 1). Applying `M` to `p` gives `Mp` — a new probability distribution.
- **Why this matters:** Quantum states are like probability vectors, but with complex amplitudes that can be negative and interfere. The ket notation carries over directly.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Bit string | A sequence of 0s and 1s, written `x_1 x_2 ... x_n` |
| `{0,1}^n` | The set of all n-bit strings (has `2^n` elements) |
| XOR (`⊕`) | Addition mod 2: `0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0` |
| Reversible gate | A gate where input is recoverable from output |
| CNOT | Controlled-NOT: `(x,y) → (x, x⊕y)` |
| Toffoli | `(a,b,c) → (a, b, c⊕(a&b))` — universal reversible gate |
| Probability vector | Column vector with non-negative entries summing to 1 |
| Stochastic matrix | Matrix whose columns are probability vectors |
| Ket `\|i⟩` | Standard basis vector (column with 1 in position i, 0 elsewhere) |

---

## What This Unlocks

Week 1 establishes the classical foundations that quantum computing extends:
- Binary encoding → qubits encode information in superpositions of `|0⟩` and `|1⟩`
- Reversible gates → all quantum gates are reversible (unitary)
- Probability vectors + ket notation → quantum state vectors use the same notation, but with complex amplitudes

---

## Common Confusion Points

**"Why does reversibility matter if quantum gates are just matrices?"**
It matters because unitarity (the quantum requirement) *implies* reversibility. Understanding reversible classical gates is the bridge.

**"What's the difference between XOR and addition?"**
XOR is addition mod 2 — it ignores any carry. `1 ⊕ 1 = 0`, not 2.

**"Why does the stochastic matrix apply to the column vector on the left?"**
Convention: column vectors represent states, and matrices act on them from the left: `M|p⟩`. This is consistent with how quantum gates act on quantum state vectors.

---

## Prerequisite Links

- Struggling with probability vectors? → `prerequisites/crash_courses.md` § 3 (Probability Theory)
- Struggling with ket notation algebra? → re-read section 1.3 of the PDF alongside § 1 of crash courses (Linear Algebra)
```

- [ ] **Step 5.2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_1/study_notes.md
git commit -m "docs: add week 1 study notes (boolean logic, reversible, randomised)"
```

---

## Task 6: Create `week_1/exercises.py`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_1/exercises.py`

- [ ] **Step 6.1: Write `week_1/exercises.py`**

Create `module_1_foundation_of_quantum_computing/week_1/exercises.py`:

```python
# Week 1 — Boolean Logic, Reversible Computation, Randomised Computation
# Run: python exercises.py
# Requires: numpy

import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1.1: Binary encoding
# Encode the integers 0–15 as 4-bit strings.
# Verify the encoding of 11 is '1011'.
# ---------------------------------------------------------------------------

def to_binary(n, bits=4):
    return format(n, f'0{bits}b')

print("Exercise 1.1: Binary encoding")
for i in range(16):
    print(f"  {i:2d} → {to_binary(i)}")

assert to_binary(0) == '0000', "1.1a failed"
assert to_binary(11) == '1011', "1.1b failed: 8+2+1=11 → 1011"
assert to_binary(15) == '1111', "1.1c failed"
print("Exercise 1.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.2: Truth tables for NOT, AND, OR, XOR
# For all combinations of a,b in {0,1}, compute and verify each operator.
# ---------------------------------------------------------------------------

print("Exercise 1.2: Truth tables")
print(f"  {'a':>2} {'b':>2} | {'NOT a':>5} {'AND':>5} {'OR':>5} {'XOR':>5}")
print("  " + "-" * 34)
for a in [0, 1]:
    for b in [0, 1]:
        not_a = 1 - a
        and_ab = a & b
        or_ab  = a | b
        xor_ab = a ^ b
        print(f"  {a:>2} {b:>2} | {not_a:>5} {and_ab:>5} {or_ab:>5} {xor_ab:>5}")

# Spot-check key values
assert (1 & 0) == 0,  "AND(1,0) should be 0"
assert (1 | 0) == 1,  "OR(1,0) should be 1"
assert (1 ^ 1) == 0,  "XOR(1,1) should be 0 — addition mod 2"
assert (1 ^ 0) == 1,  "XOR(1,0) should be 1"
print("Exercise 1.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.3: CNOT gate (reversible computation)
# CNOT maps (x, y) → (x, x XOR y).
# Verify: applying CNOT twice returns to original input.
# ---------------------------------------------------------------------------

print("Exercise 1.3: CNOT gate")

def cnot(x, y):
    return (x, x ^ y)

print(f"  CNOT(0,0) = {cnot(0,0)}")
print(f"  CNOT(0,1) = {cnot(0,1)}")
print(f"  CNOT(1,0) = {cnot(1,0)}")
print(f"  CNOT(1,1) = {cnot(1,1)}")

# CNOT is self-inverse: apply twice = identity
for x in [0, 1]:
    for y in [0, 1]:
        x2, y2 = cnot(*cnot(x, y))
        assert (x2, y2) == (x, y), f"CNOT not self-inverse at ({x},{y})"

print("Exercise 1.3 passed: CNOT is self-inverse.\n")

# ---------------------------------------------------------------------------
# Exercise 1.4: Stochastic matrix and probability vector
# Represent a biased coin (P(H)=0.7, P(T)=0.3) as a probability vector.
# Apply a fair-flip stochastic matrix and verify the result is still valid.
# ---------------------------------------------------------------------------

print("Exercise 1.4: Stochastic matrix")

coin = np.array([0.7, 0.3])   # [P(heads), P(tails)]

# A "fair flip" matrix: regardless of current state, output is 50/50
fair_flip = np.array([[0.5, 0.5],
                      [0.5, 0.5]])

result = fair_flip @ coin
print(f"  Initial coin state: {coin}")
print(f"  After one fair flip: {result}")

# Result must still be a valid probability vector
assert np.isclose(result.sum(), 1.0), "1.4: probabilities must sum to 1"
assert all(result >= 0),              "1.4: probabilities must be non-negative"
assert np.allclose(result, [0.5, 0.5]), "1.4: fair flip should give 50/50"
print("Exercise 1.4 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.5: Ket notation for probability vectors
# Write the coin state in ket notation as a NumPy linear combination.
# ---------------------------------------------------------------------------

print("Exercise 1.5: Ket notation")

ket_0 = np.array([1, 0])   # |0⟩ = heads basis vector
ket_1 = np.array([0, 1])   # |1⟩ = tails basis vector

# coin = 0.7|0⟩ + 0.3|1⟩
coin_ket = 0.7 * ket_0 + 0.3 * ket_1
assert np.allclose(coin_ket, coin), "1.5: ket reconstruction should match original"
print(f"  0.7|0⟩ + 0.3|1⟩ = {coin_ket}  ✓")
print("Exercise 1.5 passed.\n")

print("All Week 1 exercises passed.")
```

- [ ] **Step 6.2: Run exercises and verify all pass**

```bash
cd module_1_foundation_of_quantum_computing/week_1
python exercises.py
```

Expected final line: `All Week 1 exercises passed.`

- [ ] **Step 6.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_1/exercises.py
git commit -m "exercises: add week 1 — binary encoding, truth tables, CNOT, stochastic matrices"
```

---

## Task 7: Create `week_2/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_2/study_notes.md`

- [ ] **Step 7.1: Write `week_2/study_notes.md`**

Create `module_1_foundation_of_quantum_computing/week_2/study_notes.md`:

```markdown
# Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits

**PDF:** Foundations of Quantum Computing — Week 2 Study
**Sections:** 2.1 Algebra and geometry of the 2D plane · 2.2 Basics of complex numbers · 2.3 Eigenvectors, eigenvalues and normal matrices · 2.4 Single-qubit states and measurements

> **Warning:** This is the hardest week. Do not skip the linear algebra and complex numbers prerequisites. Read one section, then do the matching exercise before moving on.

---

## Core Topics

### 2.1 Algebra and Geometry of the 2D Plane
- A vector in R² is written in ket notation as `a|0⟩ + b|1⟩` where `|0⟩ = [1,0]^T` and `|1⟩ = [0,1]^T`.
- **Inner product:** `⟨u|v⟩ = u^T v = u₁v₁ + u₂v₂ + ... + uₙvₙ`
- **Norm (length):** `‖v‖ = √⟨v,v⟩`
- **Unit vector:** `‖v‖ = 1`. All kets `|ψ⟩` in this course are unit vectors.
- **Bra notation:** `⟨v| = |v⟩^T` (row vector). The inner product is the "bracket": `⟨u|v⟩`.
- **Unit circle:** All unit vectors in R² lie on a circle of radius 1. Parameterised by angle θ as `cos(θ)|0⟩ + sin(θ)|1⟩`.

### 2.2 Complex Numbers
- A complex number: `z = a + bi` where `i² = −1`, `a = Re(z)`, `b = Im(z)`.
- **Conjugate:** `z* = a − bi`
- **Modulus:** `|z| = √(a² + b²)`
- **Polar form:** `z = r·e^{iθ} = r(cos θ + i sin θ)` — Euler's formula. Multiplying two complex numbers adds their angles and multiplies their moduli.
- **Complex inner product:** For complex vectors, `⟨u|v⟩ = u†v` where `u†` is the conjugate-transpose (dagger): `u† = (u*)^T`. This is crucial — do NOT use plain transpose for complex vectors.

### 2.3 Eigenvectors, Eigenvalues, Normal Matrices
- **Eigenvector/eigenvalue:** `M|v⟩ = λ|v⟩` — the matrix only scales the vector, doesn't rotate it.
- **Normal matrix:** `M†M = MM†`. Has an orthonormal eigenbasis (eigenvectors are orthogonal and unit length).
- **Hermitian matrix:** `M† = M`. Eigenvalues are real. (Observables in quantum mechanics are Hermitian.)
- **Unitary matrix:** `U†U = I`. Eigenvalues have modulus 1. (Quantum gates are unitary.)
- Every unitary matrix is normal; every Hermitian matrix is normal.

### 2.4 Single-Qubit States and Measurements
- A **qubit state** is a unit vector `|ψ⟩ = α|0⟩ + β|1⟩` where `α, β ∈ ℂ` and `|α|² + |β|² = 1`.
- `α` and `β` are **amplitudes**. Squaring the modulus gives the probability.
- **Born rule:** Measuring `|ψ⟩` in the `{|0⟩, |1⟩}` basis gives outcome 0 with probability `|α|²` and outcome 1 with probability `|β|²`.
- **Bloch sphere:** Every single-qubit state can be written as `cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩`. Points on the unit sphere in 3D (θ = polar, φ = azimuthal angle).
- After measurement, the state **collapses** to the outcome: measuring and getting 0 leaves the qubit in `|0⟩`.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| `⟨u\|v⟩` | Inner product (complex: conjugate-transpose of u, then dot with v) |
| `‖v‖` | Norm = `√⟨v,v⟩` |
| Unit vector | Vector with norm 1. All kets are unit vectors. |
| Bra `⟨v\|` | Row vector = conjugate-transpose of ket `\|v⟩` |
| Dagger `†` | Conjugate-transpose: `A† = (A*)^T` |
| Unitary `U` | `U†U = I`: preserves norms, preserves inner products |
| Hermitian `H` | `H† = H`: real eigenvalues |
| Normal matrix | `M†M = MM†`: has orthonormal eigenbasis |
| Qubit | Two-level quantum system; state = unit vector in ℂ² |
| Amplitude | Complex coefficient in `α\|0⟩ + β\|1⟩` |
| Born rule | P(outcome i) = (modulus of amplitude for i)² |
| Bloch sphere | 3D unit sphere where every single-qubit state corresponds to one point |

---

## What This Unlocks

Week 2 builds the entire mathematical language of quantum mechanics:
- Complex inner products → measuring overlap between quantum states
- Unitary matrices → quantum gates (week 3)
- Eigenvectors → what a measurement does to a state
- Born rule + amplitudes → all quantum probability predictions

---

## Common Confusion Points

**"Why conjugate-transpose, not just transpose?"**
Because `⟨v|v⟩` must equal `‖v‖² ≥ 0`. With complex entries, plain transpose gives `v^T v = Σ vᵢ²` which can be negative if entries are imaginary. Conjugate-transpose gives `Σ |vᵢ|² ≥ 0`.

**"Is |ψ⟩ = -|ψ⟩?"**
Yes, in terms of measurement outcomes. A global phase factor `e^{iφ}` has no physical effect. But a *relative* phase between `|0⟩` and `|1⟩` amplitudes does matter.

**"What's the difference between a normal matrix and a unitary one?"**
Unitary is a special case of normal. All unitary matrices are normal, but not all normal matrices are unitary. Unitary additionally preserves norm (`U†U = I`).

---

## Prerequisite Links

- Need to review linear algebra? → `prerequisites/crash_courses.md` § 1
- Need to review complex numbers? → `prerequisites/crash_courses.md` § 2
- Need to review trig (sin/cos for unit circle)? → `prerequisites/crash_courses.md` § 4
```

- [ ] **Step 7.2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_2/study_notes.md
git commit -m "docs: add week 2 study notes (2D geometry, complex numbers, qubits)"
```

---

## Task 8: Create `week_2/exercises.py`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_2/exercises.py`

- [ ] **Step 8.1: Write `week_2/exercises.py`**

Create `module_1_foundation_of_quantum_computing/week_2/exercises.py`:

```python
# Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits
# Run: python exercises.py
# Requires: numpy

import numpy as np

# ---------------------------------------------------------------------------
# Exercise 2.1: Inner products and norms in ket notation
# Verify orthonormality of |0⟩ and |1⟩, and that |+⟩ is a unit vector.
# ---------------------------------------------------------------------------

print("Exercise 2.1: Inner products and norms")

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)
ket_plus  = np.array([1, 1], dtype=complex) / np.sqrt(2)   # |+⟩
ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)  # |−⟩

def inner(u, v):
    return np.conj(u) @ v   # ⟨u|v⟩ = u†·v

def norm(v):
    return np.sqrt(np.real(inner(v, v)))

assert np.isclose(inner(ket_0, ket_0), 1),  "2.1: ⟨0|0⟩ = 1"
assert np.isclose(inner(ket_1, ket_1), 1),  "2.1: ⟨1|1⟩ = 1"
assert np.isclose(inner(ket_0, ket_1), 0),  "2.1: ⟨0|1⟩ = 0 (orthogonal)"
assert np.isclose(norm(ket_plus),  1.0),    "2.1: |+⟩ is a unit vector"
assert np.isclose(norm(ket_minus), 1.0),    "2.1: |−⟩ is a unit vector"
assert np.isclose(inner(ket_plus, ket_minus), 0), "2.1: |+⟩ and |−⟩ are orthogonal"

print(f"  ⟨0|0⟩ = {inner(ket_0, ket_0).real:.1f}")
print(f"  ⟨0|1⟩ = {inner(ket_0, ket_1).real:.1f}")
print(f"  ‖|+⟩‖ = {norm(ket_plus):.4f}")
print("Exercise 2.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.2: Complex number arithmetic
# Practice conjugates, modulus, and Euler's formula.
# ---------------------------------------------------------------------------

print("Exercise 2.2: Complex numbers")

z1 = 1 + 2j
z2 = 3 - 1j

product = z1 * z2
assert np.isclose(product, (1*3 - 2*(-1)) + (1*(-1) + 2*3)*1j), "2.2: multiplication"
assert np.isclose(abs(z1), np.sqrt(5)),  "2.2: modulus of 1+2i = √5"
assert np.isclose(z1.conjugate(), 1 - 2j), "2.2: conjugate of 1+2i = 1-2i"

# Euler's formula: e^{iπ/2} = i
euler = np.exp(1j * np.pi / 2)
assert np.isclose(euler, 1j), "2.2: e^{iπ/2} = i"

# e^{iπ} = -1  (Euler's identity)
assert np.isclose(np.exp(1j * np.pi), -1), "2.2: e^{iπ} = -1"

print(f"  (1+2i)(3-i) = {product}")
print(f"  |1+2i| = {abs(z1):.4f}")
print(f"  e^{{iπ/2}} = {euler:.4f}")
print("Exercise 2.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.3: Eigenvalues and eigenvectors of Pauli Z and X
# Verify eigenvectors by checking M|v⟩ = λ|v⟩.
# ---------------------------------------------------------------------------

print("Exercise 2.3: Eigenvalues and eigenvectors")

Z = np.array([[1, 0], [0, -1]], dtype=complex)
X = np.array([[0, 1], [1,  0]], dtype=complex)

evals_Z, evecs_Z = np.linalg.eigh(Z)  # eigh for Hermitian matrices (sorted, real evals)
evals_X, evecs_X = np.linalg.eigh(X)

# Z eigenvalues should be {-1, +1}, eigenvectors should be |0⟩ and |1⟩
assert set(np.round(evals_Z).astype(int)) == {-1, 1}, "2.3: Z eigenvalues are ±1"

# X eigenvalues should be {-1, +1}, eigenvectors are |+⟩ and |−⟩
assert set(np.round(evals_X).astype(int)) == {-1, 1}, "2.3: X eigenvalues are ±1"

# Verify M|v⟩ = λ|v⟩ for each (eigenvalue, eigenvector) pair of Z
for i in range(2):
    lam, vec = evals_Z[i], evecs_Z[:, i]
    assert np.allclose(Z @ vec, lam * vec), f"2.3: Z eigenvector {i} check failed"

print(f"  Z eigenvalues: {np.round(evals_Z).astype(int)}")
print(f"  X eigenvalues: {np.round(evals_X).astype(int)}")
print("Exercise 2.3 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.4: Single-qubit Bloch sphere state and Born rule
# Construct |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩.
# Verify it is a unit vector and compute Born-rule measurement probabilities.
# ---------------------------------------------------------------------------

print("Exercise 2.4: Bloch sphere states and Born rule")

def bloch_state(theta, phi):
    return np.array([
        np.cos(theta / 2),
        np.exp(1j * phi) * np.sin(theta / 2)
    ], dtype=complex)

# θ=π/2, φ=0 gives |+⟩ = (1/√2)(|0⟩ + |1⟩)
psi_plus = bloch_state(np.pi / 2, 0)
assert np.isclose(norm(psi_plus), 1.0), "2.4: Bloch state must be unit vector"
assert np.isclose(abs(psi_plus[0])**2, 0.5), "2.4: P(0) for |+⟩ = 0.5"
assert np.isclose(abs(psi_plus[1])**2, 0.5), "2.4: P(1) for |+⟩ = 0.5"

# θ=π/3, φ=π/4 — a generic state
psi = bloch_state(np.pi / 3, np.pi / 4)
p0 = abs(psi[0])**2   # Born rule: P(0) = |α|²
p1 = abs(psi[1])**2   # Born rule: P(1) = |β|²
assert np.isclose(p0 + p1, 1.0), "2.4: probabilities must sum to 1"

print(f"  |+⟩ = {np.round(psi_plus, 4)}")
print(f"  P(0) = {p0:.4f}, P(1) = {p1:.4f}, sum = {p0+p1:.4f}")
print("Exercise 2.4 passed.\n")

print("All Week 2 exercises passed.")
```

- [ ] **Step 8.2: Run exercises and verify all pass**

```bash
cd module_1_foundation_of_quantum_computing/week_2
python exercises.py
```

Expected final line: `All Week 2 exercises passed.`

- [ ] **Step 8.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_2/exercises.py
git commit -m "exercises: add week 2 — inner products, complex numbers, eigenvectors, Bloch sphere"
```

---

## Task 9: Create `week_3/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_3/study_notes.md`

- [ ] **Step 9.1: Write `week_3/study_notes.md`**

Create `module_1_foundation_of_quantum_computing/week_3/study_notes.md`:

```markdown
# Week 3 — Single-Qubit Unitaries, Bloch Sphere, Multi-Qubit Systems

**PDF:** Foundations of Quantum Computing — Week 3 Study
**Sections:** 3.1 Single-qubit unitary transformations · 3.2 Multi-qubit states and transformations · 3.3 Measurement and multi-qubit states

---

## Core Topics

### 3.1 Single-Qubit Unitary Transformations
- A **quantum gate** acting on a single qubit is a 2×2 unitary matrix `U`: satisfies `U†U = I`.
- Unitary maps unit vectors to unit vectors → it preserves valid qubit states.
- **Standard gates:**
  - `X` (Pauli X / NOT): `[[0,1],[1,0]]` — flips `|0⟩ ↔ |1⟩`
  - `Y` (Pauli Y): `[[0,−i],[i,0]]`
  - `Z` (Pauli Z): `[[1,0],[0,−1]]` — flips the phase of `|1⟩`
  - `H` (Hadamard): `(1/√2)[[1,1],[1,−1]]` — maps `|0⟩ → |+⟩` and `|1⟩ → |−⟩`
  - `S` (Phase): `[[1,0],[0,i]]` — quarter-turn around Z axis
  - `T` (π/8): `[[1,0],[0,e^{iπ/4}]]`

- **Bloch sphere interpretation:** Any single-qubit unitary is a rotation of the Bloch sphere about some axis. `Rₙ(α)` denotes rotation by angle α about axis `n`.
  - `Rx(α) = e^{−iαX/2} = cos(α/2)I − i·sin(α/2)X`
  - `Rz(α) = e^{−iαZ/2} = cos(α/2)I − i·sin(α/2)Z`

### 3.2 Multi-Qubit States and Transformations
- A **2-qubit system** has a state space of dimension 4: basis states `|00⟩, |01⟩, |10⟩, |11⟩`.
- **Tensor product:** `|a⟩ ⊗ |b⟩` (written `|a,b⟩` or `|ab⟩`) — the joint state of two independent qubits. In NumPy: `np.kron(a, b)`.
- A **separable state** can be written as `|ψ⟩ ⊗ |φ⟩`. An **entangled state** cannot.
- **Bell states** (maximally entangled 2-qubit states):
  - `|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)`
  - `|Φ−⟩ = (1/√2)(|00⟩ − |11⟩)`
  - `|Ψ+⟩ = (1/√2)(|01⟩ + |10⟩)`
  - `|Ψ−⟩ = (1/√2)(|01⟩ − |10⟩)`
- **CNOT gate:** 4×4 unitary. Maps `|x,y⟩ → |x, x⊕y⟩`. First qubit is control.
- **Creating Bell state |Φ+⟩:** Apply `H` to first qubit (in state `|0⟩`), then CNOT: `H⊗I → CNOT`.

### 3.3 Measurement and Multi-Qubit States
- Measuring one qubit of an entangled pair collapses the joint state.
- If `|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)` and you measure the first qubit and get 0, the second immediately collapses to `|0⟩` — regardless of distance.
- **Born rule for multi-qubit states:** `P(outcome x) = |⟨x|ψ⟩|²`

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Unitary `U` | `U†U = I`; quantum gate; preserves norms |
| Hadamard `H` | Creates superposition: `|0⟩ → (|0⟩+|1⟩)/√2` |
| Pauli X/Y/Z | Fundamental single-qubit gates; rotations by π about x/y/z Bloch axes |
| `Rn(α)` | Rotation by angle α about axis n on Bloch sphere |
| Tensor product `⊗` | Combines two qubit states into a joint state: `np.kron` |
| Separable state | Joint state expressible as `\|ψ⟩⊗\|φ⟩` |
| Entangled state | Joint state NOT expressible as a product |
| Bell states | Four maximally entangled 2-qubit states: `\|Φ±⟩`, `\|Ψ±⟩` |
| CNOT | `\|x,y⟩ → \|x, x⊕y⟩`; creates entanglement from superposition |

---

## What This Unlocks

- Gates + entanglement are the two quantum resources that enable quantum algorithms
- Quantum teleportation (week 4) uses a Bell state + CNOT + Hadamard
- Grover's algorithm (week 7) uses Hadamard on n qubits to create uniform superposition

---

## Common Confusion Points

**"Why does H on |0⟩ give (|0⟩+|1⟩)/√2 but H on |1⟩ give (|0⟩−|1⟩)/√2?"**
Matrix multiplication: `H|0⟩ = (1/√2)[1,1]` and `H|1⟩ = (1/√2)[1,-1]`. The minus sign is a relative phase — physically real and important.

**"Is |00⟩ + |11⟩ really not separable?"**
Yes. Try to write `(a|0⟩ + b|1⟩) ⊗ (c|0⟩ + d|1⟩) = ac|00⟩ + ad|01⟩ + bc|10⟩ + bd|11⟩`. For this to equal `|00⟩ + |11⟩` you'd need `ad=0` and `bc=0` but `ac=bd=1/√2` — impossible simultaneously.

---

## Prerequisite Links

- Struggling with matrix multiplication? → `prerequisites/crash_courses.md` § 1 (Linear Algebra — matrix multiplication section)
- Struggling with tensor products? → `week_2/study_notes.md` inner product section (same idea, different operation)
```

- [ ] **Step 9.2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_3/study_notes.md
git commit -m "docs: add week 3 study notes (quantum gates, Bloch sphere, multi-qubit)"
```

---

## Task 10: Create `week_3/exercises.py`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_3/exercises.py`

- [ ] **Step 10.1: Write `week_3/exercises.py`**

Create `module_1_foundation_of_quantum_computing/week_3/exercises.py`:

```python
# Week 3 — Single-Qubit Gates, Bloch Sphere, Multi-Qubit Systems
# Run: python exercises.py
# Requires: numpy

import numpy as np

# Standard gates (defined once, used throughout)
I    = np.eye(2, dtype=complex)
X    = np.array([[0, 1], [1,  0]], dtype=complex)
Y    = np.array([[0,-1j],[1j, 0]], dtype=complex)
Z    = np.array([[1, 0], [0, -1]], dtype=complex)
H    = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CNOT = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,0,1],
                 [0,0,1,0]], dtype=complex)

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 3.1: Verify standard gates are unitary (U†U = I)
# ---------------------------------------------------------------------------

print("Exercise 3.1: Unitarity check")

def is_unitary(U, tol=1e-10):
    return np.allclose(U.conj().T @ U, np.eye(len(U)), atol=tol)

for name, gate in [('X', X), ('Y', Y), ('Z', Z), ('H', H)]:
    result = is_unitary(gate)
    print(f"  {name} unitary: {result}")
    assert result, f"3.1: {name} must be unitary"

print("Exercise 3.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.2: Hadamard maps |0⟩ → |+⟩ and |1⟩ → |−⟩
# ---------------------------------------------------------------------------

print("Exercise 3.2: Hadamard action")

ket_plus  = np.array([1,  1], dtype=complex) / np.sqrt(2)
ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)

assert np.allclose(H @ ket_0, ket_plus),  "3.2: H|0⟩ = |+⟩"
assert np.allclose(H @ ket_1, ket_minus), "3.2: H|1⟩ = |−⟩"
# H is self-inverse: H² = I
assert np.allclose(H @ H, I), "3.2: H² = I"

print(f"  H|0⟩ = {np.round(H @ ket_0, 4)}")
print(f"  H|1⟩ = {np.round(H @ ket_1, 4)}")
print("Exercise 3.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.3: Tensor products for 2-qubit basis states
# ---------------------------------------------------------------------------

print("Exercise 3.3: Tensor products")

ket_00 = np.kron(ket_0, ket_0)
ket_01 = np.kron(ket_0, ket_1)
ket_10 = np.kron(ket_1, ket_0)
ket_11 = np.kron(ket_1, ket_1)

# Standard basis vectors in ℂ⁴
assert np.allclose(ket_00, [1,0,0,0]), "3.3: |00⟩ = [1,0,0,0]"
assert np.allclose(ket_01, [0,1,0,0]), "3.3: |01⟩ = [0,1,0,0]"
assert np.allclose(ket_10, [0,0,1,0]), "3.3: |10⟩ = [0,0,1,0]"
assert np.allclose(ket_11, [0,0,0,1]), "3.3: |11⟩ = [0,0,0,1]"

print(f"  |00⟩ = {ket_00}")
print(f"  |11⟩ = {ket_11}")
print("Exercise 3.3 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.4: Construct Bell state |Φ+⟩ via H⊗I then CNOT
# ---------------------------------------------------------------------------

print("Exercise 3.4: Bell state |Φ+⟩")

H_kron_I = np.kron(H, I)
state = H_kron_I @ ket_00        # |+⟩|0⟩ = (1/√2)(|00⟩ + |10⟩)
bell_plus = CNOT @ state          # (1/√2)(|00⟩ + |11⟩)

expected_bell = (ket_00 + ket_11) / np.sqrt(2)
assert np.allclose(bell_plus, expected_bell), "3.4: Bell state construction failed"

# Verify norm is 1
assert np.isclose(np.linalg.norm(bell_plus), 1.0), "3.4: Bell state must have norm 1"

print(f"  |Φ+⟩ = {np.round(bell_plus, 4)}")
print("Exercise 3.4 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.5: Verify |Φ+⟩ is entangled (cannot be written as product state)
# Show that no (a,b,c,d) satisfies (a|0⟩+b|1⟩)⊗(c|0⟩+d|1⟩) = |Φ+⟩
# by checking the separability condition: (ac)(bd) = (ad)(bc)
# For |Φ+⟩ = [1/√2, 0, 0, 1/√2]: ac=1/√2, ad=0, bc=0, bd=1/√2
# (ac)(bd) = 1/2 but (ad)(bc) = 0 → entangled
# ---------------------------------------------------------------------------

print("Exercise 3.5: Entanglement check")

b_state = bell_plus
ac = b_state[0]  # coefficient of |00⟩
ad = b_state[1]  # coefficient of |01⟩
bc = b_state[2]  # coefficient of |10⟩
bd = b_state[3]  # coefficient of |11⟩

# Separability condition: ac * bd == ad * bc
separable = np.isclose(ac * bd, ad * bc)
assert not separable, "3.5: |Φ+⟩ must NOT be separable"
print(f"  ac·bd = {ac*bd:.4f}, ad·bc = {ad*bc:.4f} → entangled: {not separable}")
print("Exercise 3.5 passed.\n")

print("All Week 3 exercises passed.")
```

- [ ] **Step 10.2: Run exercises and verify all pass**

```bash
cd module_1_foundation_of_quantum_computing/week_3
python exercises.py
```

Expected final line: `All Week 3 exercises passed.`

- [ ] **Step 10.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_3/exercises.py
git commit -m "exercises: add week 3 — gates, Hadamard, tensor products, Bell state, entanglement"
```

---

## Task 11: Create `week_4/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_4/study_notes.md`

- [ ] **Step 11.1: Write `week_4/study_notes.md`**

Create `module_1_foundation_of_quantum_computing/week_4/study_notes.md`:

```markdown
# Week 4 — Quantum Teleportation, Hadamard Operations, Phase Estimation

**PDF:** Foundations of Quantum Computing — Week 4 Study
**Sections:** 4.1 Quantum teleportation · 4.2 Hadamard operations and phase estimation

---

## Core Topics

### 4.1 Quantum Teleportation

**What it is:** A protocol to transfer an unknown qubit state `|α⟩` from Alice to Bob using a shared Bell state and 2 classical bits. Does NOT move matter — moves information.

**Set-up:**
- Alice has qubit `q` in unknown state `|α⟩ = α|0⟩ + β|1⟩`
- Alice and Bob share a Bell pair `|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)` — Alice holds qubit `a`, Bob holds `b`

**Protocol steps:**
1. Alice applies CNOT with `q` as control and `a` as target
2. Alice applies `H` to `q`
3. Alice measures `q` and `a` in the computational basis → gets classical bits `x` and `z`
4. Alice sends `x` and `z` to Bob over a classical channel
5. Bob applies `X` to `b` if `x = 1`, and `Z` to `b` if `z = 1`
6. Bob's qubit `b` is now in state `|α⟩`

**Why it works (the algebra):**
Before Alice's measurement, the joint state of `q`, `a`, `b` can be rewritten as:
```
(1/2)[|Φ+⟩(α|0⟩+β|1⟩) + |Φ−⟩(α|0⟩−β|1⟩) + |Ψ+⟩(α|1⟩+β|0⟩) + |Ψ−⟩(α|1⟩−β|0⟩)]
```
Each Bell measurement outcome leaves Bob's qubit in a version of `|α⟩` that can be fixed with at most one X and one Z.

**Bell states as measurement basis:**
- `|Φ+⟩ → 00`: Bob does nothing
- `|Φ−⟩ → 01`: Bob applies Z
- `|Ψ+⟩ → 10`: Bob applies X
- `|Ψ−⟩ → 11`: Bob applies X then Z

### 4.2 Hadamard Operations and Phase Estimation

- **n-qubit Hadamard `H⊗n`:** Apply H to each qubit independently. Maps `|0...0⟩` to the uniform superposition: `(1/√(2^n)) Σ|x⟩` over all n-bit strings x.
- **Phase kickback:** For an oracle `U|x⟩ = e^{iφ(x)}|x⟩`, applying `H⊗n`, then the oracle, then `H⊗n` again encodes phase information into amplitudes.
- **Quantum Phase Estimation (QPE):** Algorithm to estimate the eigenvalue `e^{2πiφ}` of a unitary `U` given its eigenvector. Uses `H⊗n` and controlled-U operations. Foundation for Shor's algorithm.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Quantum teleportation | Transferring an unknown qubit state using a Bell pair + 2 classical bits |
| Bell measurement | Measuring in the `{\|Φ±⟩, \|Ψ±⟩}` basis; identifies which Bell state two qubits are in |
| Classical control | Applying a quantum gate conditionally on a classical bit value |
| `H⊗n` | Hadamard applied to each of n qubits; creates uniform superposition |
| Phase kickback | Mechanism by which a phase from an oracle qubit "kicks back" to the control |
| QPE | Quantum Phase Estimation: estimates eigenvalue phase of a unitary |

---

## What This Unlocks

- Teleportation demonstrates quantum entanglement is a resource for communication
- Phase kickback + QPE is the core primitive of Shor's algorithm (week 8)
- `H⊗n` creating uniform superposition is the starting point for Grover's algorithm (week 7)

---

## Common Confusion Points

**"Does teleportation violate the no-cloning theorem?"**
No. After teleportation Alice's qubit is destroyed (collapsed by measurement). The state is not copied — it is moved.

**"Why do you need classical bits? Can't you just use quantum channels?"**
The Bell measurement outcome is random — Bob needs to know which of the 4 outcomes Alice got so he can apply the right correction. Without the 2 classical bits, Bob has a mixed state, not `|α⟩`.

**"Why can't teleportation transmit information faster than light?"**
Because Bob can't do anything useful with his qubit until he receives Alice's classical bits, which travel at most at the speed of light.

---

## Prerequisite Links

- Struggling with Bell states? → `week_3/study_notes.md` and `week_3/exercises.py` exercise 3.4
- Struggling with the algebra? → Trace through the state of all 3 qubits step by step with `week_4/exercises.py`
```

- [ ] **Step 11.2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_4/study_notes.md
git commit -m "docs: add week 4 study notes (teleportation, Hadamard, phase estimation)"
```

---

## Task 12: Create `week_4/exercises.py`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_4/exercises.py`

- [ ] **Step 12.1: Write `week_4/exercises.py`**

Create `module_1_foundation_of_quantum_computing/week_4/exercises.py`:

```python
# Week 4 — Quantum Teleportation, Hadamard Operations, Phase Estimation
# Run: python exercises.py
# Requires: numpy

import numpy as np

# Standard gates
I    = np.eye(2, dtype=complex)
X    = np.array([[0, 1], [1,  0]], dtype=complex)
Z    = np.array([[1, 0], [0, -1]], dtype=complex)
H    = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)

ket_0  = np.array([1, 0], dtype=complex)
ket_1  = np.array([0, 1], dtype=complex)
ket_00 = np.kron(ket_0, ket_0)
ket_11 = np.kron(ket_1, ket_1)

# ---------------------------------------------------------------------------
# Exercise 4.1: Construct and verify all four Bell states
# ---------------------------------------------------------------------------

print("Exercise 4.1: All four Bell states")

def make_bell(x, z):
    """
    Start from |00⟩, apply H⊗I then CNOT to get |Φ+⟩.
    Then apply X to second qubit if x=1, Z if z=1.
    Returns Bell state corresponding to measurement outcome (x, z).
    """
    # Build |Φ+⟩
    state = CNOT @ np.kron(H, I) @ ket_00
    if x:
        state = np.kron(I, X) @ state
    if z:
        state = np.kron(I, Z) @ state
    return state

bell = {
    (0,0): make_bell(0, 0),   # |Φ+⟩
    (0,1): make_bell(0, 1),   # |Φ−⟩
    (1,0): make_bell(1, 0),   # |Ψ+⟩
    (1,1): make_bell(1, 1),   # |Ψ−⟩
}

# All four must be unit vectors
for key, b in bell.items():
    assert np.isclose(np.linalg.norm(b), 1.0), f"4.1: Bell state {key} must have norm 1"

# All four must be mutually orthogonal
keys = list(bell.keys())
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        overlap = np.conj(bell[keys[i]]) @ bell[keys[j]]
        assert np.isclose(overlap, 0), f"4.1: Bell states {keys[i]} and {keys[j]} must be orthogonal"

print(f"  |Φ+⟩ = {np.round(bell[(0,0)], 3)}")
print(f"  |Φ−⟩ = {np.round(bell[(0,1)], 3)}")
print(f"  |Ψ+⟩ = {np.round(bell[(1,0)], 3)}")
print(f"  |Ψ−⟩ = {np.round(bell[(1,1)], 3)}")
print("Exercise 4.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 4.2: Teleportation — trace the algebra for one Bell outcome
# Show that if Alice measures (x=0, z=0), Bob's qubit ends up in state |α⟩.
# We verify all four outcomes by undoing the classical correction.
# ---------------------------------------------------------------------------

print("Exercise 4.2: Quantum teleportation trace")

def teleport_verify(alpha, beta):
    """
    Construct 3-qubit state |q,a,b⟩ = |α⟩ ⊗ |Φ+⟩ and trace through
    the teleportation protocol. Returns Bob's corrected state for each
    of the four Bell measurement outcomes.
    """
    assert np.isclose(abs(alpha)**2 + abs(beta)**2, 1.0), "Input must be normalised"

    psi_q = alpha * ket_0 + beta * ket_1        # Alice's qubit to teleport
    bell_ab = (ket_00 + ket_11) / np.sqrt(2)    # Shared Bell pair |Φ+⟩

    # Full 3-qubit initial state: |q⟩ ⊗ |Φ+⟩_{ab}
    state_3 = np.kron(psi_q, bell_ab)

    # Step 1: CNOT with q as control, a as target (qubits 0 and 1 of 3)
    CNOT_qa = np.kron(CNOT, I)   # acts on qubits (q,a), identity on b
    state_3 = CNOT_qa @ state_3

    # Step 2: H on q (qubit 0)
    H_q = np.kron(np.kron(H, I), I)
    state_3 = H_q @ state_3

    # Rewrite state_3 in the Bell basis for (q,a) to read off Bob's state.
    # Rather than doing the symbolic algebra, we project onto each Bell state
    # and extract Bob's (unnormalised) qubit.
    results = {}
    for (x, z), bell_state in bell.items():
        # Project (q,a) onto this Bell state; extract Bob's part
        # ⟨Bell_{qa}| ⊗ I_b applied to state_3 gives Bob's (unnormalised) state
        projector_qa = bell_state  # shape (4,)
        # Reshape state_3 to (4, 2): (qa, b)
        state_reshaped = state_3.reshape(4, 2)
        bob_unnorm = np.conj(projector_qa) @ state_reshaped  # shape (2,)

        # Normalise
        prob = np.linalg.norm(bob_unnorm)**2
        if prob > 1e-12:
            bob_state = bob_unnorm / np.sqrt(prob)
        else:
            bob_state = bob_unnorm

        # Apply classical correction: X if x=1, Z if z=1
        corrected = bob_state.copy()
        if x:
            corrected = X @ corrected
        if z:
            corrected = Z @ corrected

        results[(x, z)] = (prob, corrected)

    return results

# Test with |+⟩ = (1/√2)(|0⟩ + |1⟩)
alpha = 1 / np.sqrt(2)
beta  = 1 / np.sqrt(2)
psi_target = alpha * ket_0 + beta * ket_1

results = teleport_verify(alpha, beta)
print(f"  Teleporting |ψ⟩ = {np.round(psi_target, 3)}")
for (x, z), (prob, corrected) in results.items():
    # After correction, Bob's state must match the original (up to global phase)
    overlap = abs(np.conj(psi_target) @ corrected)
    assert np.isclose(overlap, 1.0, atol=1e-6), \
        f"4.2: Teleportation failed for outcome (x={x},z={z}): overlap={overlap:.4f}"
    print(f"  Outcome (x={x},z={z}): P={prob:.3f}, Bob after correction = {np.round(corrected,3)} ✓")

print("Exercise 4.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 4.3: n-qubit Hadamard creates uniform superposition
# Verify H⊗2 applied to |00⟩ gives (1/2)(|00⟩+|01⟩+|10⟩+|11⟩).
# ---------------------------------------------------------------------------

print("Exercise 4.3: n-qubit Hadamard")

H2 = np.kron(H, H)   # H⊗2
uniform = H2 @ ket_00

expected = np.ones(4, dtype=complex) / 2  # (1/2)[1,1,1,1]
assert np.allclose(uniform, expected), "4.3: H⊗2|00⟩ should be uniform superposition"

# Each amplitude is 1/2, each probability is 1/4
probs = np.abs(uniform)**2
assert np.allclose(probs, 0.25 * np.ones(4)), "4.3: uniform superposition has equal probabilities"

print(f"  H⊗2|00⟩ = {np.round(uniform, 4)}")
print(f"  Probabilities: {np.round(probs, 4)}")
print("Exercise 4.3 passed.\n")

print("All Week 4 exercises passed.")
```

- [ ] **Step 12.2: Run exercises and verify all pass**

```bash
cd module_1_foundation_of_quantum_computing/week_4
python exercises.py
```

Expected final line: `All Week 4 exercises passed.`

- [ ] **Step 12.3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_4/exercises.py
git commit -m "exercises: add week 4 — Bell states, teleportation trace, n-qubit Hadamard"
```

---

## Task 13: Create `CONTINUATION.md`

**Files:**
- Create: `CONTINUATION.md` (repo root)

- [ ] **Step 13.1: Write `CONTINUATION.md`**

Create `CONTINUATION.md` at the repo root:

```markdown
# Continuation Guide

This file lets you resume this project in a new Claude Code session on any machine.
Pull the repo, open this file, paste the resume prompt below into Claude Code.

---

## What Has Been Built

| File | Status | Description |
|------|--------|-------------|
| `module_1_foundation_of_quantum_computing/roadmap.md` | ✅ Done | 8-week plan, midterm checklist |
| `module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md` | ✅ Done | Ranked crash course guide |
| `module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md` | ✅ Done | 10-day sprint schedule |
| `module_1_foundation_of_quantum_computing/week_1/study_notes.md` | ✅ Done | Boolean logic, reversible, randomised |
| `module_1_foundation_of_quantum_computing/week_1/exercises.py` | ✅ Done | Exercises 1.1–1.5 |
| `module_1_foundation_of_quantum_computing/week_2/study_notes.md` | ✅ Done | 2D geometry, complex numbers, qubits |
| `module_1_foundation_of_quantum_computing/week_2/exercises.py` | ✅ Done | Exercises 2.1–2.4 |
| `module_1_foundation_of_quantum_computing/week_3/study_notes.md` | ✅ Done | Gates, Bloch sphere, multi-qubit |
| `module_1_foundation_of_quantum_computing/week_3/exercises.py` | ✅ Done | Exercises 3.1–3.5 |
| `module_1_foundation_of_quantum_computing/week_4/study_notes.md` | ✅ Done | Teleportation, phase estimation |
| `module_1_foundation_of_quantum_computing/week_4/exercises.py` | ✅ Done | Exercises 4.1–4.3 |
| `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md` | ✅ Done | Design spec |
| `docs/superpowers/plans/2026-06-02-quantum-learning-system-plan.md` | ✅ Done | Implementation plan |

---

## What Comes Next

- **Weeks 5–8:** When the Sussex portal releases PDFs for weeks 5–8, add `week_5/` through `week_8/` following the same pattern: `study_notes.md` + `exercises.py`. Update `roadmap.md` to fill in the `[TBD]` sections.
- **Midterm assignment:** Due after week 4. See `roadmap.md` → Midterm Checklist.

---

## Resume Prompt

Paste this into a new Claude Code session after pulling the repo:

---

> I'm continuing my quantum computing learning system for my Sussex MSc (Quantum Technology Applications and Management). The project is in `module_1_foundation_of_quantum_computing/`.
>
> The design spec is at: `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md`
> The implementation plan is at: `docs/superpowers/plans/2026-06-02-quantum-learning-system-plan.md`
>
> All tasks in the implementation plan are complete for weeks 1–4. The immediate next steps are:
> 1. When week 5–8 PDFs arrive, read them and add `week_N/study_notes.md` + `week_N/exercises.py` following the same pattern as weeks 1–4 (see any existing week folder as a template).
> 2. Update `module_1_foundation_of_quantum_computing/roadmap.md` to replace the `[TBD — materials pending]` sections with real content.
> 3. Update the "What Has Been Built" table in `CONTINUATION.md`.
>
> Please read the spec and plan files first, then ask me what I'd like to work on.

---

## Notes

- All exercises verified runnable with `python exercises.py` in each week folder
- Requires: `pip install numpy`
- Week 4 exercises require no additional packages beyond numpy
- Future weeks (5–8) will likely require `pip install qiskit` for circuit simulation
```

- [ ] **Step 13.2: Commit**

```bash
git add CONTINUATION.md
git commit -m "docs: add CONTINUATION.md for resuming work on another machine"
```

---

## Task 14: Final Integration Verification

**Files:** No changes — verification only.

- [ ] **Step 14.1: Run all exercise files**

```bash
cd module_1_foundation_of_quantum_computing
python week_1/exercises.py && echo "W1 OK"
python week_2/exercises.py && echo "W2 OK"
python week_3/exercises.py && echo "W3 OK"
python week_4/exercises.py && echo "W4 OK"
```

Expected output ends with:
```
All Week 1 exercises passed.
W1 OK
All Week 2 exercises passed.
W2 OK
All Week 3 exercises passed.
W3 OK
All Week 4 exercises passed.
W4 OK
```

- [ ] **Step 14.2: Verify directory structure is correct**

```bash
find module_1_foundation_of_quantum_computing -name "*.md" -o -name "*.py" | sort
```

Expected output:
```
module_1_foundation_of_quantum_computing/prerequisites/crash_courses.md
module_1_foundation_of_quantum_computing/prerequisites/study_schedule.md
module_1_foundation_of_quantum_computing/roadmap.md
module_1_foundation_of_quantum_computing/week_1/exercises.py
module_1_foundation_of_quantum_computing/week_1/study_notes.md
module_1_foundation_of_quantum_computing/week_2/exercises.py
module_1_foundation_of_quantum_computing/week_2/study_notes.md
module_1_foundation_of_quantum_computing/week_3/exercises.py
module_1_foundation_of_quantum_computing/week_3/study_notes.md
module_1_foundation_of_quantum_computing/week_4/exercises.py
module_1_foundation_of_quantum_computing/week_4/study_notes.md
```

- [ ] **Step 14.3: Final commit**

```bash
git add -A
git status   # verify nothing unexpected is staged
git commit -m "chore: final integration check — all 4 weeks complete"
```

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Task that covers it |
|-----------------|---------------------|
| `roadmap.md` with all sections | Task 2 |
| `prerequisites/crash_courses.md` ranked | Task 3 |
| `prerequisites/study_schedule.md` 10-day sprint | Task 4 |
| `week_N/study_notes.md` for weeks 1–4 | Tasks 5, 7, 9, 11 |
| `week_N/exercises.py` runnable for weeks 1–4 | Tasks 6, 8, 10, 12 |
| `CONTINUATION.md` with resume prompt | Task 13 |
| `rough_4w_plan.md` deleted | Task 1 |
| Exercises numbered `N.X` scheme | Applied in tasks 6, 8, 10, 12 |
| Exercises end with assert + print | Applied in all exercise tasks |
| Weeks 5–8 placeholder in roadmap | Task 2 (§ `[TBD — materials pending]`) |

**Placeholder scan:** No TBD/TODO in plan steps. The `[TBD — materials pending]` in roadmap.md is intentional design — it marks future work, not an incomplete plan step.

**Type consistency:** No shared function signatures across tasks — each file is self-contained. Gate matrix definitions are reproduced in each `exercises.py` (YAGNI — no shared module needed for a study system).

**Scope:** 14 tasks, 13 files. Single module, single learner. Appropriately scoped.
