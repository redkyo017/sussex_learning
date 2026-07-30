# Week 5 — Grover's Algorithm and Amplitude Amplification

**PDF:** Foundations of Quantum Computing — Week 5 Study
**Sections:** 5.1 Oracle model and search problem · 5.2 Grover's search (unique marked element) · 5.3 Search without uniqueness

---

## Core Topics

### 5.1 Oracle Model and Search Problem

**The search problem:**
- Given a function f:{0,1}ⁿ → {0,1}, find x such that f(x)=1
- The "marked" elements are those satisfying f(x)=1

**Oracle encoding:**
- Oracle O_f encodes f as a phase kick: `O_f|x⟩ = (−1)^{f(x)}|x⟩`
- Marked elements (f(x)=1) gain a phase of −1; unmarked elements (f(x)=0) are unchanged
- This is the standard phase-oracle model in quantum query complexity

**Classical lower bound:**
- Any classical algorithm requires Θ(2ⁿ) queries in the worst case
- Grover's algorithm achieves O(√(2ⁿ)) — a quadratic improvement

### 5.2 Grover's Search (Unique Marked Element)

**Setup (M=1 marked element, N=2ⁿ total):**
- Start with uniform superposition: `|u⟩ = H^⊗n|0ⁿ⟩ = (1/√N) Σ_x |x⟩`

**Reduction to 2D geometry:**
- Let |β⟩ be the unique marked state
- Let |a⟩ be the normalised sum of all unmarked states: `|a⟩ = (1/√(N−1)) Σ_{x≠β} |x⟩`
- G_f stays within the 2D plane span{|a⟩, |β⟩} for all iterations
- Initial angle θ satisfies `sin(θ) = 1/√(2ⁿ)` (small angle for large n)

**The two reflections that make up the Grover iterator:**
- **R_f (phase-kick oracle):** reflects about the |a⟩ axis — flips the sign of the |β⟩ component
- **R_u (diffusion operator):** `R_u = H^⊗n (2|0ⁿ⟩⟨0ⁿ| − I) H^⊗n` — reflects about the |u⟩ axis

**Grover iterator:**
- `G_f = R_u R_f` — composition of two reflections = a rotation
- Each application rotates the state by 2θ toward |β⟩ in the span{|a⟩, |β⟩} plane

**Optimal number of iterations:**
- `t_opt = floor(π/(4θ)) ≈ (π/4)√(2ⁿ)`
- After t_opt steps the state is approximately |β⟩; measuring yields the marked element with high probability
- **Quadratic speedup:** O(√N) quantum queries vs O(N) classical queries, where N=2ⁿ

### 5.3 Search Without Uniqueness

**Case M=0 (no marked elements):**
- The algorithm always fails — there is no marked element to find
- The state rotates indefinitely without approaching any target

**Case M>1 marked elements:**
- Angle generalises: `sin(θ) = √(M/2ⁿ)`
- Optimal iterations: `t_opt = floor(π/(4θ))`
- The speedup becomes O(√(N/M)) queries

**Unknown M — QuantumSearch:**
- When M is unknown, use a randomised number of iterations
- Succeeds with probability ≥ 1/2 regardless of M
- Converts Grover's algorithm into a practical search primitive

**Amplitude amplification:**
- General framework that generalises Grover's algorithm beyond pure search
- Replaces the uniform superposition with any starting state produced by a known circuit A
- Replaces the search oracle with any Boolean test on the amplitude components
- Achieves quadratic speedup over classical Monte Carlo in many settings

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Oracle | Unitary O_f encoding f via phase kick: O_f\|x⟩ = (−1)^{f(x)}\|x⟩ |
| Marked element | An x with f(x)=1; the target of the search |
| Phase kick | Mechanism by which a phase is applied to a basis state via an oracle |
| Uniform superposition | \|u⟩ = H^⊗n\|0ⁿ⟩; equal amplitude on all 2ⁿ basis states |
| Grover iterator | G_f = R_u R_f; rotates state by 2θ toward the marked state each step |
| Amplitude amplification | Generalisation of Grover's algorithm to arbitrary starting circuits |
| Spectral gap | The separation between eigenvalues of G_f; related to θ and convergence speed |
| Quadratic speedup | O(√N) quantum queries achieving what requires O(N) classical queries |

---

## What This Unlocks

- Shor's algorithm (Week 6) uses phase estimation, a technique related to amplitude amplification
- Grover search is a subroutine in many quantum algorithms beyond pure search
- The oracle model is the standard way to define quantum query complexity

---

## Common Confusion Points

**"Does R_f reflect about |β⟩ or about |a⟩?"**
R_f reflects *about* |a⟩ — it flips the sign of the |β⟩ component, not the |a⟩ component. The axis of reflection is the unmarked subspace.

**"Why is t_opt a floor (round down), not a round?"**
Because overshooting rotates the state past |β⟩ and reduces the success probability. The floor gives the last iteration before the state goes beyond |β⟩.

**"Why does the 2D geometric picture work?"**
The 2D picture only works because G_f stays in the span{|a⟩, |β⟩} plane for all iterations — this is a consequence of G_f's structure as two reflections within that plane.

---

## Prerequisite Links

- Week 4: Phase estimation uses a similar ancilla + controlled-unitary structure (`../week_4/study_notes.md`)
- Week 3: Hadamard gate H^⊗n creates the uniform superposition |u⟩ (`../week_3/study_notes.md`)
