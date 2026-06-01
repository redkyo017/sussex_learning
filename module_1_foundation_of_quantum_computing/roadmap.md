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
