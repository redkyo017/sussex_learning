# Assignment 1 Solution — Design Spec

**Date:** 2026-06-05
**Module:** Foundations of Quantum Computing (Sussex MSc)
**Assessment weight:** 30% of module grade
**Submission:** Single PDF via Canvas

---

## Goal

Produce two files:

1. `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex`
   — Submittable LaTeX document with all 10 questions answered in full, showing all mathematical workings. Compiles to PDF with `pdflatex`.

2. `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md`
   — Companion study guide: for each question, a plain-English explanation of what concept it tests, the technique/recipe used, and why it works. For personal review after submission.

---

## Document Structure (`assignment_1.tex`)

- **Document class:** `article`
- **Packages:** `amsmath`, `amssymb`, `braket`, `geometry`, `physics`
- **Sections:** Cover block → 10 numbered questions, each with:
  - Question restated verbatim (or summarised)
  - Full step-by-step working
  - Boxed final answer

---

## Question Map — Answers and Methods

| Q | Concept tested | Technique | Answer |
|---|---------------|-----------|--------|
| Q1 | Gate composition on 3 qubits | Apply gates right-to-left: H₂ → CX₂,₃ → CX₂,₁ → Z₂ → Z₁ | (1/√2)(\|000⟩ + \|111⟩) |
| Q2 | Hadamard on entangled superposition | Expand Bell-state mixture into computational basis, simplify, identify product state, apply H₂ | \|00⟩ |
| Q3 | Partial measurement (computational basis) | Project onto first qubit = \|0⟩, extract second qubit state, normalise | \|1⟩ |
| Q4 | Partial measurement (Hadamard basis) | Re-express \|Ψ⁻⟩ in {+,−} basis for qubit 1, project onto \|−⟩, normalise | \|+⟩ |
| Q5 | Partial measurement (Y basis) | Project \|Ψ⁻⟩ using conjugate inner product ⟨+i\|, normalise, identify global phase | \|−i⟩ |
| Q6 | Rotation gate composition | Multiply Rz(−φ)·Ry(θ)·Rz(φ) as 2×2 matrices step by step | e^{iθ/2}[[cos(θ/2), −e^{iφ}sin(θ/2)], [e^{−iφ}sin(θ/2), cos(θ/2)]] |
| Q7 | Controlled gates | Substitute V=U(1,1) into \|0⟩⟨0\|⊗I + \|1⟩⟨1\|⊗V structure | 4×4 matrix: identity block top-left, V(1,1) bottom-right |
| Q8 | Measurement in Bell basis | Expand \|+i,+i⟩, compute \|⟨Bₖ\|ψ⟩\|² for each Bell state | P(Φ⁺)=0, P(Φ⁻)=½, P(Ψ⁺)=½, P(Ψ⁻)=0 |
| Q9 | CCX (Toffoli) + probability | Expand CCX\|+,+,0⟩ term by term, sum amplitude² for 3rd qubit=\|0⟩ | P(\|0⟩) = 3/4 |
| Q10 | Sequential conditional measurement | Use conditional probability: P(\|10,0⟩) / P(third=\|0⟩) | P(\|10⟩) = 1/3 |

---

## Study Guide Structure (`assignment_1_study_guide.md`)

For each question:
- **What it tests** — the core concept in one sentence
- **Recipe** — numbered steps to solve this type of problem
- **Why it works** — the intuition behind the technique
- **Common mistakes** — pitfalls to avoid

---

## Workflow

1. Write `assignment_1.tex` — complete LaTeX with all 10 solutions
2. Write `assignment_1_study_guide.md` — companion explanations
3. User reviews both files, flags any corrections
4. Compile: `pdflatex assignment_1.tex` → produces `assignment_1.pdf`
5. Upload `assignment_1.pdf` to Canvas

---

## LaTeX Conventions

- Use `\ket{0}` (from `braket` package) for Dirac notation
- Use `\frac{1}{\sqrt{2}}` not `1/\sqrt{2}` inline for clarity
- Use `align*` environment for multi-step derivations
- Box final answers with `\boxed{}`
- Each question in its own `\section*{Question N}`
