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
