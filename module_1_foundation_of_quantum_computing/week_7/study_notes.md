# Week 7 — Hamiltonians, Adiabatic Algorithm, Trotterisation, and QAOA

**PDF:** Foundations of Quantum Computing — Week 7 Study
**Sections:** 7.1 Hamiltonian dynamics · 7.2 Adiabatic algorithm · 7.3 Trotterisation · 7.4 QAOA

> **Portfolio note:** The Week 7 PDF states explicitly: "None of the topics covered this week are involved in the portfolio assessment." These notes are for conceptual breadth only — do not prioritise this week over assignment preparation.

---

## Core Topics

### 7.1 — Hamiltonian Dynamics and Time Evolution

- Schrödinger equation: d/dt|ψ(t)⟩ = −(i/ℏ)H|ψ(t)⟩ where H is the Hamiltonian (Hermitian operator encoding energy)
- Time-independent case: unitary time evolution U(t) = e^{−iHt/ℏ}
- The matrix exponential e^{−iHt} is computed via diagonalisation: if H = VΛV†, then e^{−iHt} = Ve^{−iΛt}V†
- Hermitian H guarantees U(t) is unitary, so quantum evolution preserves norm
- Slowly varying Hamiltonians: perturbation theory extends the time-independent picture

### 7.2 — Adiabatic Algorithm

- Adiabatic theorem: if H(t) changes slowly enough, a system starting in the ground state remains in the instantaneous ground state throughout evolution
- Condition: total time T ≫ (max gap)⁻² where the gap is the spectral gap (min distance between ground and first excited state energy)
- Algorithm:
  1. Choose easy initial Hamiltonian H_0 with known ground state (e.g., −∑X_i, ground state = |+⟩^⊗n)
  2. Encode the optimisation problem as final Hamiltonian H_f (e.g., −∑h_i Z_i − ∑J_{ij} Z_i Z_j for Ising model)
  3. Interpolate: H(t) = (1 − t/T)H_0 + (t/T)H_f for t ∈ [0, T]
  4. Evolve slowly; measure at t=T to get the ground state of H_f (solution to the optimisation problem)
- Limitation: T can be exponentially large if the spectral gap closes near t=T

### 7.3 — Hamiltonian Simulation and Trotterisation

- Problem: computing e^{−i(H_A+H_B)t} when H_A and H_B don't commute
- If [H_A, H_B] = 0: e^{−i(H_A+H_B)t} = e^{−iH_At} · e^{−iH_Bt} (exact)
- If [H_A, H_B] ≠ 0: use the Trotter product formula (first order):
  e^{−i(H_A+H_B)t} ≈ (e^{−iH_At/N} · e^{−iH_Bt/N})^N  
  Error scales as O(t²/N) — decreases as N increases
- Trotterisation enables quantum simulation of physical systems (chemistry, materials science)

### 7.4 — QAOA (Quantum Approximate Optimisation Algorithm)

- Variational quantum algorithm (VQA): a hybrid quantum-classical approach
- Algorithm:
  1. Choose problem Hamiltonian H_f (encodes cost function) and mixer Hamiltonian H_0
  2. Apply M alternating layers: e^{−iγ_k H_f} then e^{−iβ_k H_0} for k=1..M
  3. Optimise angles (γ₁,…,γ_M, β₁,…,β_M) classically to minimise ⟨ψ|H_f|ψ⟩
- QAOA with M=∞ recovers the adiabatic algorithm
- No performance guarantees for finite M on NP-hard problems
- The ansatz (circuit structure) is problem-specific

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Hamiltonian | Hermitian operator H encoding the total energy of a quantum system |
| Schrödinger equation | Differential equation d/dt|ψ⟩ = −(i/ℏ)H|ψ⟩ governing quantum state evolution |
| Matrix exponential | e^{−iHt}, the unitary operator implementing time evolution under H |
| Unitary evolution | Time evolution that preserves the norm of the quantum state; guaranteed by Hermitian H |
| Ground state | The lowest-energy eigenstate of a Hamiltonian; the target state in adiabatic algorithms |
| Spectral gap | Minimum energy difference between the ground state and first excited state; governs adiabatic runtime |
| Adiabatic theorem | If H(t) varies slowly enough, a system in the ground state remains in the instantaneous ground state |
| Trotterisation | Approximation technique splitting e^{−i(H_A+H_B)t} into alternating factors; error O(t²/N) |
| Product formula | The identity e^{A+B} ≈ (e^{A/N}e^{B/N})^N used in Trotterisation |
| Ising model | Spin system with Hamiltonian −∑h_i Z_i − ∑J_{ij} Z_i Z_j; used to encode optimisation problems |
| CSP (constraint satisfaction problem) | Combinatorial problem class encodable in Ising-type Hamiltonians |
| QAOA | Quantum Approximate Optimisation Algorithm; variational hybrid quantum-classical algorithm |
| VQA (variational quantum algorithm) | Class of hybrid algorithms that optimise circuit parameters classically |
| Ansatz | A parameterised trial circuit or state; QAOA uses a problem-specific ansatz |

---

## What This Unlocks

- Hamiltonian simulation is the original application Feynman proposed for quantum computers
- Trotterisation is used in quantum chemistry simulations on near-term hardware
- QAOA is one of the most studied near-term quantum algorithms, though its performance relative to classical methods is still an open research question
- Understanding adiabatic computation gives a different perspective on quantum speedup — it's not always about circuit gates

---

## Common Confusion Points

**"Is Trotterisation exact?"**
No. It is an approximation that improves as N (the number of Trotter steps) increases. The error is O(t²/N), so doubling N halves the error. For commuting terms it's exact.

**"Does QAOA outperform classical algorithms?"**
Unknown for finite M. QAOA has no proven performance guarantees on NP-hard problems for any finite number of layers M. This is an active research area.

**"Why does adiabatic evolution need to be slow?"**
The adiabatic theorem requires evolution slow enough that the system has time to track the instantaneous ground state. If evolution is too fast, the system can get excited into higher energy states and the final measurement won't give the optimum.

---

## Prerequisite Links

- Week 4: Quantum gates and circuits are the building blocks Trotterised simulation uses (`../week_4/study_notes.md`)
- Week 5/6: The oracle model (Grover, Shor) is a different paradigm — adiabatic and gate-based computation are equivalent in power but different in structure (`../week_5/study_notes.md`)
