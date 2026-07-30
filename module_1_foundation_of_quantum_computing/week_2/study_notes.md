# Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits

**PDF:** Foundations of Quantum Computing — Week 2 Study
**Sections:** 2.1 Algebra and geometry of the 2D plane · 2.2 Basics of complex numbers · 2.3 Eigenvectors, eigenvalues and normal matrices · 2.4 Single-qubit states and measurements

> **Warning:** This is the hardest week. Do not skip the linear algebra and complex numbers prerequisites. Read one section, then do the matching exercise before moving on.

---

## Core Topics

### 2.1 Algebra and Geometry of the 2D Plane
- A vector in R² is written in ket notation as `a|0⟩ + b|1⟩` where `|0⟩ = [1,0]^T` and `|1⟩ = [0,1]^T`.
- **Inner product:** `⟨u|v⟩ = u^T v = u₁v₁ + u₂v₂ + ... + uₙvₙ`
- **Norm (length):** `‖v‖ = √⟨v,v⟩`
- **Unit vector:** `‖v‖ = 1`. All kets `|ψ⟩` in this course are unit vectors.
- **Bra notation:** `⟨v| = |v⟩^T` (row vector). The inner product is the "bracket": `⟨u|v⟩`.
- **Unit circle:** All unit vectors in R² lie on a circle of radius 1. Parameterised by angle θ as `cos(θ)|0⟩ + sin(θ)|1⟩`.

### 2.2 Complex Numbers
- A complex number: `z = a + bi` where `i² = −1`, `a = Re(z)`, `b = Im(z)`.
- **Conjugate:** `z* = a − bi`
- **Modulus:** `|z| = √(a² + b²)`
- **Polar form:** `z = r·e^{iθ} = r(cos θ + i sin θ)` — Euler's formula. Multiplying two complex numbers adds their angles and multiplies their moduli.
- **Complex inner product:** For complex vectors, `⟨u|v⟩ = u†v` where `u†` is the conjugate-transpose (dagger): `u† = (u*)^T`. This is crucial — do NOT use plain transpose for complex vectors.

### 2.3 Eigenvectors, Eigenvalues, Normal Matrices
- **Eigenvector/eigenvalue:** `M|v⟩ = λ|v⟩` — the matrix only scales the vector, doesn't rotate it.
- **Normal matrix:** `M†M = MM†`. Has an orthonormal eigenbasis (eigenvectors are orthogonal and unit length).
- **Hermitian matrix:** `M† = M`. Eigenvalues are real. (Observables in quantum mechanics are Hermitian.)
- **Unitary matrix:** `U†U = I`. Eigenvalues have modulus 1. (Quantum gates are unitary.)
- Every unitary matrix is normal; every Hermitian matrix is normal.

### 2.4 Single-Qubit States and Measurements
- A **qubit state** is a unit vector `|ψ⟩ = α|0⟩ + β|1⟩` where `α, β ∈ ℂ` and `|α|² + |β|² = 1`.
- `α` and `β` are **amplitudes**. Squaring the modulus gives the probability.
- **Born rule:** Measuring `|ψ⟩` in the `{|0⟩, |1⟩}` basis gives outcome 0 with probability `|α|²` and outcome 1 with probability `|β|²`.
- **Bloch sphere:** Every single-qubit state can be written as `cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩`. Points on the unit sphere in 3D (θ = polar, φ = azimuthal angle).
- After measurement, the state **collapses** to the outcome: measuring and getting 0 leaves the qubit in `|0⟩`.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| `⟨u\|v⟩` | Inner product (complex: conjugate-transpose of u, then dot with v) |
| `‖v‖` | Norm = `√⟨v,v⟩` |
| Unit vector | Vector with norm 1. All kets are unit vectors. |
| Bra `⟨v\|` | Row vector = conjugate-transpose of ket `\|v⟩` |
| Dagger `†` | Conjugate-transpose: `A† = (A*)^T` |
| Unitary `U` | `U†U = I`: preserves norms, preserves inner products |
| Hermitian `H` | `H† = H`: real eigenvalues |
| Normal matrix | `M†M = MM†`: has orthonormal eigenbasis |
| Qubit | Two-level quantum system; state = unit vector in ℂ² |
| Amplitude | Complex coefficient in `α\|0⟩ + β\|1⟩` |
| Born rule | P(outcome i) = (modulus of amplitude for i)² |
| Bloch sphere | 3D unit sphere where every single-qubit state corresponds to one point |

---

## What This Unlocks

Week 2 builds the entire mathematical language of quantum mechanics:
- Complex inner products → measuring overlap between quantum states
- Unitary matrices → quantum gates (week 3)
- Eigenvectors → what a measurement does to a state
- Born rule + amplitudes → all quantum probability predictions

---

## Common Confusion Points

**"Why conjugate-transpose, not just transpose?"**
Because `⟨v|v⟩` must equal `‖v‖² ≥ 0`. With complex entries, plain transpose gives `v^T v = Σ vᵢ²` which can be negative if entries are imaginary. Conjugate-transpose gives `Σ |vᵢ|² ≥ 0`.

**"Is |ψ⟩ = -|ψ⟩?"**
Yes, in terms of measurement outcomes. A global phase factor `e^{iφ}` has no physical effect. But a *relative* phase between `|0⟩` and `|1⟩` amplitudes does matter.

**"What's the difference between a normal matrix and a unitary one?"**
Unitary is a special case of normal. All unitary matrices are normal, but not all normal matrices are unitary. Unitary additionally preserves norm (`U†U = I`).

---

## Prerequisite Links

- Need to review linear algebra? → `prerequisites/crash_courses.md` § 1
- Need to review complex numbers? → `prerequisites/crash_courses.md` § 2
- Need to review trig (sin/cos for unit circle)? → `prerequisites/crash_courses.md` § 4
