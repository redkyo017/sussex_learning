# Week 3 — Single-Qubit Unitaries, Bloch Sphere, Multi-Qubit Systems

**PDF:** Foundations of Quantum Computing — Week 3 Study
**Sections:** 3.1 Single-qubit unitary transformations · 3.2 Multi-qubit states and transformations · 3.3 Measurement and multi-qubit states

---

## Core Topics

### 3.1 Single-Qubit Unitary Transformations
- A **quantum gate** acting on a single qubit is a 2×2 unitary matrix `U`: satisfies `U†U = I`.
- Unitary maps unit vectors to unit vectors → it preserves valid qubit states.
- **Standard gates:**
  - `X` (Pauli X / NOT): `[[0,1],[1,0]]` — flips `|0⟩ ↔ |1⟩`
  - `Y` (Pauli Y): `[[0,−i],[i,0]]`
  - `Z` (Pauli Z): `[[1,0],[0,−1]]` — flips the phase of `|1⟩`
  - `H` (Hadamard): `(1/√2)[[1,1],[1,−1]]` — maps `|0⟩ → |+⟩` and `|1⟩ → |−⟩`
  - `S` (Phase): `[[1,0],[0,i]]` — quarter-turn around Z axis
  - `T` (π/8): `[[1,0],[0,e^{iπ/4}]]`

- **Bloch sphere interpretation:** Any single-qubit unitary is a rotation of the Bloch sphere about some axis. `Rₙ(α)` denotes rotation by angle α about axis `n`.
  - `Rx(α) = e^{−iαX/2} = cos(α/2)I − i·sin(α/2)X`
  - `Rz(α) = e^{−iαZ/2} = cos(α/2)I − i·sin(α/2)Z`

### 3.2 Multi-Qubit States and Transformations
- A **2-qubit system** has a state space of dimension 4: basis states `|00⟩, |01⟩, |10⟩, |11⟩`.
- **Tensor product:** `|a⟩ ⊗ |b⟩` (written `|a,b⟩` or `|ab⟩`) — the joint state of two independent qubits. In NumPy: `np.kron(a, b)`.
- A **separable state** can be written as `|ψ⟩ ⊗ |φ⟩`. An **entangled state** cannot.
- **Bell states** (maximally entangled 2-qubit states):
  - `|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)`
  - `|Φ−⟩ = (1/√2)(|00⟩ − |11⟩)`
  - `|Ψ+⟩ = (1/√2)(|01⟩ + |10⟩)`
  - `|Ψ−⟩ = (1/√2)(|01⟩ − |10⟩)`
- **CNOT gate:** 4×4 unitary. Maps `|x,y⟩ → |x, x⊕y⟩`. First qubit is control.
- **Creating Bell state |Φ+⟩:** Apply `H` to first qubit (in state `|0⟩`), then CNOT: `H⊗I → CNOT`.

### 3.3 Measurement and Multi-Qubit States
- Measuring one qubit of an entangled pair collapses the joint state.
- If `|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)` and you measure the first qubit and get 0, the second immediately collapses to `|0⟩` — regardless of distance.
- **Born rule for multi-qubit states:** `P(outcome x) = |⟨x|ψ⟩|²`

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Unitary `U` | `U†U = I`; quantum gate; preserves norms |
| Hadamard `H` | Creates superposition: `|0⟩ → (|0⟩+|1⟩)/√2` |
| Pauli X/Y/Z | Fundamental single-qubit gates; rotations by π about x/y/z Bloch axes |
| `Rn(α)` | Rotation by angle α about axis n on Bloch sphere |
| Tensor product `⊗` | Combines two qubit states into a joint state: `np.kron` |
| Separable state | Joint state expressible as `\|ψ⟩⊗\|φ⟩` |
| Entangled state | Joint state NOT expressible as a product |
| Bell states | Four maximally entangled 2-qubit states: `\|Φ±⟩`, `\|Ψ±⟩` |
| CNOT | `\|x,y⟩ → \|x, x⊕y⟩`; creates entanglement from superposition |

---

## What This Unlocks

- Gates + entanglement are the two quantum resources that enable quantum algorithms
- Quantum teleportation (week 4) uses a Bell state + CNOT + Hadamard
- Grover's algorithm (week 7) uses Hadamard on n qubits to create uniform superposition

---

## Common Confusion Points

**"Why does H on |0⟩ give (|0⟩+|1⟩)/√2 but H on |1⟩ give (|0⟩−|1⟩)/√2?"**
Matrix multiplication: `H|0⟩ = (1/√2)[1,1]` and `H|1⟩ = (1/√2)[1,-1]`. The minus sign is a relative phase — physically real and important.

**"Is |00⟩ + |11⟩ really not separable?"**
Yes. Try to write `(a|0⟩ + b|1⟩) ⊗ (c|0⟩ + d|1⟩) = ac|00⟩ + ad|01⟩ + bc|10⟩ + bd|11⟩`. For this to equal `|00⟩ + |11⟩` you'd need `ad=0` and `bc=0` but `ac=bd=1/√2` — impossible simultaneously.

---

## Prerequisite Links

- Struggling with matrix multiplication? → `prerequisites/crash_courses.md` § 1 (Linear Algebra — matrix multiplication section)
- Struggling with tensor products? → `week_2/study_notes.md` inner product section (same idea, different operation)
