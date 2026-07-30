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
| `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex` | ✅ Done | Full LaTeX solution for all 10 assignment questions |
| `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md` | ✅ Done | Study guide with recipes and explanations for all 10 questions |
| `module_1_foundation_of_quantum_computing/week_5/study_notes.md` | ✅ Done | Grover's algorithm, amplitude amplification, oracle model |
| `module_1_foundation_of_quantum_computing/week_5/exercises.py` | ✅ Done | Exercises 5.1–5.3 (oracle, Grover iterator, optimal iterations) |
| `module_1_foundation_of_quantum_computing/week_6/study_notes.md` | ✅ Done | Shor's algorithm: RSA, order finding, QFT |
| `module_1_foundation_of_quantum_computing/week_6/exercises.py` | ✅ Done | Exercises 6.1–6.3 (order finding, QFT matrix, continued fractions) |
| `module_1_foundation_of_quantum_computing/week_7/study_notes.md` | ✅ Done | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA (not in portfolio) |
| `module_1_foundation_of_quantum_computing/week_7/exercises.py` | ✅ Done | Exercises 7.1–7.2 (matrix exponential, Trotterisation) |
| `docs/superpowers/specs/2026-06-27-weeks-5-7-extension-design.md` | ✅ Done | Design spec for weeks 5–7 extension |
| `docs/superpowers/plans/2026-06-27-weeks-5-7-extension-plan.md` | ✅ Done | Implementation plan for weeks 5–7 extension |
| `docs/superpowers/specs/2026-06-27-portfolio-design.md` | ✅ Done | Design spec for Assignment 2 portfolio |
| `module_1_foundation_of_quantum_computing/assignment_2_portfolio/portfolio.tex` | ✅ Done | Full LaTeX portfolio — all 5 weeks (Wks 2–6), 100 marks |

---

## What Comes Next

- **Assignment 1:** Complete — scored 98/100. Feedback: add closing sentences to Q1, Q2, Q4, Q8, Q9 for the portfolio.
- **Weeks 1–7:** All study notes and exercises complete. Week 8 is a revision week (no PDF, no new files).
- **Assignment 2 / Portfolio:** Submitted 2026-06-27. Turnitin returned 6% similarity — all matches were mathematical notation and problem-given constants, not prose. No risk; awaiting grade.
- **Revision (Week 8):** Use `week_1/` through `week_6/` exercises for revision. Run `python exercises.py` in each folder.

---

## Resume Prompt

Paste this into a new Claude Code session after pulling the repo:

---

> I'm continuing my quantum computing learning system for my Sussex MSc (Quantum Technology Applications and Management). The project is in `module_1_foundation_of_quantum_computing/`.
>
> Study notes and exercises are complete for weeks 1–7. Assignment 1 is done (98/100). Week 8 is a revision week with no new files.
>
> The next task is **Assignment 2 / Portfolio** (covers weeks 1–6; week 7 is explicitly excluded). Please read `CONTINUATION.md` and the design specs in `docs/superpowers/specs/` for context, then help me work on the portfolio.
>
> Key specs:
> - Original system design: `docs/superpowers/specs/2026-06-02-quantum-learning-system-design.md`
> - Weeks 5–7 extension design: `docs/superpowers/specs/2026-06-27-weeks-5-7-extension-design.md`

---

## Lessons Learned

### Turnitin similarity in STEM/maths assignments (2026-06-29)

**Context:** Assignment 2 portfolio returned 6% overall similarity.

**Finding:** For maths-heavy assignments, Turnitin will always flag some similarity — but nearly all of it will be false positives:
- Mathematical notation (`cos(π/8)|0⟩`, ket notation, tensor products) cannot be rephrased — Turnitin flags it anyway.
- Problem parameters given in the question sheet (N=323, a=2, specific function definitions) will appear identically in every student's submission — that is expected and not misconduct.
- Standard textbook derivations (phase kickback, Shor's `(u−1)(u+1)` argument) are shared across the field.

**Rule of thumb:**
- Under 10% with all matches on notation/formulae: safe, no action needed.
- Over 15%: check whether matches are prose or notation. Only prose matches to student papers require attention.
- Do NOT try to rephrase mathematical notation to reduce the score — it makes the work look unnatural and does not help.

**What matters to the professor:** Is the expository prose original? In this portfolio, every explanation and closing sentence was original — that is the only thing that counts.

---

## Notes

- All exercises verified runnable with `python exercises.py` in each week folder
- Weeks 1–6 require: `pip install numpy`
- Week 7 additionally requires: `pip install scipy` (for `scipy.linalg.expm`)
- No qiskit required — all exercises use numpy/scipy only
- Week 7 topics are NOT assessed in the portfolio (per course PDF)
