# Portfolio (Assignment 2) — Design Spec

**Date:** 2026-06-27  
**Module:** Foundations of Quantum Computing (Sussex MSc)  
**Assessment weight:** 70% of module grade  
**Submission:** Single PDF via Canvas, due Week 8 Monday 10:00 UK  

---

## Goal

Produce `module_1_foundation_of_quantum_computing/assignment_2_portfolio/portfolio.tex` — a single LaTeX document covering all five weekly portfolio problems (Weeks 2–6), compiling to a submittable PDF.

---

## Document Structure

- **Document class:** `article`, 12pt, a4paper  
- **Packages:** `amsmath`, `amssymb`, `braket`, `geometry` (margin 2.5cm)  
- **Sections:** `\section*{Week N --- [Topic]}` per problem  
- **Sub-parts:** `\textbf{Part (a) --- ...}` with marks noted  
- **Style:** Intro sentence → step-by-step working → boxed final answer → closing sentence  

---

## Problem Map

| Week | Topic | Marks | Key method |
|------|-------|-------|-----------|
| 2 | Hadamard as reflection + eigendecomposition | 10 | H²=I; axis at π/8; spectral decomposition |
| 3 | SWAP gate: inverse, eigenvectors, measurement, CSWAP | 15 | SWAP²=I; {|00⟩,|11⟩,|01⟩+|10⟩,|01⟩-|10⟩}; projectors |
| 4 | Quantum teleportation (Alice/Bob, unknown |ψ⟩) | 25 | Circuit trace with |Φ+⟩; all 4 measurement branches |
| 5 | Grover's algorithm (f(01)=1, one iteration) | 25 | Oracle phase kickback; diffusion; amplitude analysis |
| 6 | Shor's algorithm (N=323, a=2, x₁=7/24, x₂=5/18) | 25 | Continued fractions → order s; gcd factoring |

**Total: 100 marks**

---

## Style Rules (from rubric + A1 feedback)

- Every sub-part: introduce what is being calculated, show working, close with "Thus…" / "Therefore…"
- Exposition counts for 30% of marks — never just a naked equation
- Q8 from A1 lost 2 marks for thin exposition — apply extra care to Week 4 and Week 5
- Human, varied prose — no formulaic repetition of "I begin by…" every time

---

## Implementation Plan

Write `portfolio.tex` in 5 passes (one per week) to stay within output token limits.
