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

- **Weeks 5–8:** When the Sussex portal releases PDFs for weeks 5–8, add `week_5/` through `week_8/` following the same pattern: `study_notes.md` + `exercises.py`. Update `roadmap.md` to fill in the `[TBD — study materials pending]` sections.
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
> 2. Update `module_1_foundation_of_quantum_computing/roadmap.md` to replace the `[TBD — study materials pending]` sections with real content.
> 3. Update the "What Has Been Built" table in `CONTINUATION.md`.
>
> Please read the spec and plan files first, then ask me what I'd like to work on.

---

## Notes

- All exercises verified runnable with `python exercises.py` in each week folder
- Requires: `pip install numpy`
- Week 4 exercises require no additional packages beyond numpy
- Future weeks (5–8) will likely require `pip install qiskit` for circuit simulation
