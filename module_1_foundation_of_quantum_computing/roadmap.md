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
| 5 | Grover's algorithm, amplitude amplification, oracle model | Weeks 1–4 complete |
| 6 | Shor's algorithm, RSA cryptosystem, order finding, QFT | Week 5 |
| 7 | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA | Week 6 |
| 8 | Revision week (no new material) | Weeks 1–7 |

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
pip install numpy scipy
```

All exercises (weeks 1–7) require only numpy and scipy. No circuit simulator required.

---

## Weeks 5–7 Content Summary

| Week | Title | Portfolio? | Notes |
|------|-------|-----------|-------|
| 5 | Grover's algorithm + amplitude amplification | ✅ Yes | Oracle model, 2D geometry, t_opt = floor(π/(4θ)) |
| 6 | Shor's algorithm (RSA, order finding, QFT) | ✅ Yes | Most technical week; "not expected in fine detail" |
| 7 | Hamiltonians, adiabatic, Trotterisation, QAOA | ❌ No | Explicitly excluded from portfolio assessment |

---

## Resources for Weeks 5–7 (Additional Reading)

- **Nielsen & Chuang Chapter 6** — Grover's algorithm with full mathematical treatment
- **Quantum Country** — quantumcountry.com; spaced-repetition quantum textbook, excellent for Grover/Shor retention
- **Scott Aaronson's lecture notes** — Shor's algorithm explained clearly with number theory background
