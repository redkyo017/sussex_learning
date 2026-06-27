# Design: Weeks 5–7 Extension — Quantum Learning System
**Date:** 2026-06-27
**Module:** Foundations of Quantum Computing (Sussex MSc Quantum Technology Applications and Management)
**Status:** Approved — ready for implementation plan
**Extends:** `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md`

---

## 1. Context

Weeks 1–4, assignment 1, prerequisites, and the roadmap were built in the prior session (see parent design spec). Week 5, 6, and 7 PDFs have now arrived. Week 8 is a revision week with no PDF. This spec covers adding `week_5/`, `week_6/`, and `week_7/` following the exact same conventions as weeks 1–4.

---

## 2. Correction to Roadmap

The original roadmap predicted the wrong topics for weeks 5–7. The PDFs reveal:

| Week | Roadmap predicted | Actual PDF content |
|------|-------------------|--------------------|
| 5 | Deutsch-Jozsa / Bernstein-Vazirani | Grover's algorithm + amplitude amplification |
| 6 | Quantum Fourier Transform | Shor's algorithm (RSA, order finding, QFT as subsection) |
| 7 | Grover's search algorithm | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA |
| 8 | Shor's / error correction | Revision week — no PDF |

`roadmap.md` must be updated to reflect the actual topics.

---

## 3. Files to Create

### 3.1 `week_5/study_notes.md`

**PDF:** Week 5 — Section 5: Grover's algorithm and amplitude amplification

Sections to cover:
- **5.1** How search problems are described: oracle `O_f`, the search problem statement
- **5.2** Grover's search algorithm (unique element):
  - Reducing to 2D: the `|a⟩`, `|β⟩` plane, angle θ with sin(θ) = 1/√2ⁿ
  - R_f: reflection about `|β⟩` axis via phase kick with `|-⟩` ancilla
  - R_u: reflection about `|u⟩` via Hadamard + multiply-controlled-X
  - Grover iterator G_f = R_u R_f: rotation by 2θ
  - Number of iterations: t ≈ (π/4)·√2ⁿ
- **5.3** Search without uniqueness: no marked elements, M marked elements, unknown M (QuantumSearch)

Key vocab: oracle, amplitude amplification, marked element, Grover iterator, phase kick, spectral gap.

### 3.2 `week_5/exercises.py`

Three exercises:

| ID | Title | Concept |
|----|-------|---------|
| 5.1 | Oracle phase kick | Construct uniform superposition; show oracle flips phase of marked state |
| 5.2 | Grover iterator simulation | Simulate 2D rotation: track angle after t iterations, verify probability of measuring marked state |
| 5.3 | Optimal iteration count | Compute t = floor((π/4)·√2ⁿ − 1) for n=2,3,4; verify probability > 1 − 2⁻ⁿ |

---

### 3.3 `week_6/study_notes.md`

**PDF:** Week 6 — Section 6: Shor's algorithm (RSA, order finding, QFT)

Sections to cover:
- **6.1** RSA cryptosystem: public/private keys, encryption/decryption, why factorisation breaks it
- **6.2** Factorisation and order finding:
  - Number theory: prime factorisation, gcd, factorSplitting claim (u² ≡ 1 mod N)
  - Order finding: smallest t > 0 such that aᵗ ≡ 1 (mod N)
  - Reduction from factorisation to order finding
- **6.3** Order finding via phase estimation:
  - QFT on n qubits: the matrix F_{2ⁿ}, roots of unity, orthogonal states |f_{ωᵏ}⟩
  - Inverse QFT and QAAL subroutine `invQFT[n]`
  - Phase estimation on U_a eigenvalues to sample x = h/t
  - Modular exponentiation: `Phase_Estimation_Mul[n]`
  - Sampling from eigenvectors using |1⟩ as input

Key vocab: RSA, coprime, modular arithmetic, order, QFT, inverse QFT, continued fractions, modular exponentiation.

**Note from PDF:** "This is by far the most technical Study material encountered so far. You are not expected to remember it in fine detail."

### 3.4 `week_6/exercises.py`

Three exercises:

| ID | Title | Concept |
|----|-------|---------|
| 6.1 | Modular arithmetic and order | Compute powers of a mod N classically; find the order |
| 6.2 | QFT matrix on 3 qubits | Construct F_8 (ω = e^{2πi/8}) as numpy matrix; verify unitarity (F†F = I) |
| 6.3 | Continued fractions for period | Given sample x = h/t as float, apply continued fractions to recover t |

---

### 3.5 `week_7/study_notes.md`

**PDF:** Week 7 — Section 7: Hamiltonians, adiabatic algorithm, Trotterisation, QAOA

> **Portfolio note:** The Week 7 PDF states explicitly: "None of the topics covered this week are involved in the portfolio assessment." These notes are for conceptual breadth only.

Sections to cover:
- **7.1** Continuous-time evolution: Hamiltonian H, Schrödinger equation d/dt|ψ(t)⟩ = −(i/ℏ)H|ψ(t)⟩
  - Time-independent case: U(t) = e^{−iHt/ℏ}, matrix exponential
  - Slowly varying Hamiltonians: perturbation theory sketch
- **7.2** Adiabatic algorithm:
  - Adiabatic theorem: slowly varying H keeps system in ground state
  - Algorithm: encode CSP as H_f, start in easy ground state |u⟩, interpolate H(t) = (t/T)H_f + (1−t/T)H_0
- **7.3** Hamiltonian simulation:
  - Trotterisation: e^{−iHt/ℏ} ≈ (e^{−iH₁t/ℏ} e^{−iH₂t/ℏ} … )^{T/t} for H = H₁ + H₂ + …
  - Operator product formulas for time-dependent Hamiltonians
- **7.4** QAOA: alternating H_f and H_0 simulations for M steps; variational approach; no performance guarantees

Key vocab: Hamiltonian, Schrödinger equation, matrix exponential, ground state, spectral gap, adiabatic theorem, Trotterisation, CSP, QAOA, VQA, ansatz.

### 3.6 `week_7/exercises.py`

Two exercises (lighter, since not assessed):

| ID | Title | Concept |
|----|-------|---------|
| 7.1 | Matrix exponential for time evolution | Compute e^{−iHt} for a simple 2×2 Hamiltonian using scipy.linalg.expm; verify unitarity |
| 7.2 | Trotterisation approximation | Show that (e^{−iH_At/N} e^{−iH_Bt/N})^N → e^{−i(H_A+H_B)t} as N increases |

---

## 4. Updates to Existing Files

### 4.1 `roadmap.md`

Replace the Course Content Map rows for weeks 5–7 with correct topics. Replace the `[TBD — study materials pending]` block with:

```
| 5 | Grover's algorithm, amplitude amplification, oracle model | Weeks 1–4 complete |
| 6 | Shor's algorithm, RSA cryptosystem, order finding, QFT | Week 5 |
| 7 | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA | Week 6 |
| 8 | Revision week (no new material) | Weeks 1–7 |
```

Add a `## Weeks 5–7 Content` section with per-week summaries and a note that Week 7 is not assessed in the portfolio.

### 4.2 `CONTINUATION.md`

Add rows to the "What Has Been Built" table for all six new files (three `study_notes.md` + three `exercises.py`). Update "What Comes Next" to reflect that weeks 1–7 are complete and the next task is Assignment 2 (portfolio).

---

## 5. Conventions (unchanged from parent spec)

- Study notes template: Core Topics, Key Concepts & Vocab, What This Unlocks, Common Confusion Points, Prerequisite Links
- Exercises: numbered `N.X`, numpy-based, `assert` + `print`, final `"All Week N exercises passed."`
- Week 7 exercises also require `scipy` (for `scipy.linalg.expm`)

---

## 6. Out of Scope

- Week 8 (revision only, no PDF, no new study files)
- Assignment 2 / portfolio (separate session)
- Deutsch-Jozsa and Bernstein-Vazirani algorithms (not in any of the actual PDFs)

---

## 7. Success Criteria

- [ ] `python week_5/exercises.py` runs without errors, prints "All Week 5 exercises passed."
- [ ] `python week_6/exercises.py` runs without errors, prints "All Week 6 exercises passed."
- [ ] `python week_7/exercises.py` runs without errors, prints "All Week 7 exercises passed."
- [ ] `roadmap.md` shows correct topics for weeks 5–7 (no more `[TBD]`)
- [ ] `CONTINUATION.md` lists all six new files as Done and updates "What Comes Next"
- [ ] All files committed to git
