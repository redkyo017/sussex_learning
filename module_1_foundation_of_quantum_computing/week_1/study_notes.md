# Week 1 — Boolean Logic, Reversible Computation, Randomised Computation

**PDF:** Foundations of Quantum Computing — Week 1 Study
**Sections:** 1.1 Boolean logic · 1.2 Reversible computation · 1.3 Randomised computation

---

## Core Topics

### 1.1 Boolean Logic
- **Binary encoding:** Any finite set can be encoded as n-bit strings `{0,1}^n`. The number of n-bit strings is `2^n`.
- **Logical operators:** NOT (`¬x`), AND (`x & y`), OR (`x ∨ y`), XOR (`x ⊕ y`). XOR = addition mod 2.
- **Algebraic form:** `A & B = AB`, `A ∨ B = A + B − AB`, `A ⊕ B = A + B − 2AB`
- **Universality:** Every boolean function `f: {0,1}^m → {0,1}` can be expressed using only NOT, AND, OR. Key technique: express `f` as an OR of indicator functions `δ_a(x)` for each input `a` where `f(a) = 1`.

### 1.2 Reversible Computation
- A computation is **reversible** if you can recover the input from the output.
- AND, OR, XOR on their own are **not** reversible — e.g., `AND(1,0) = AND(0,1) = 0`, so you can't recover which inputs gave output 0.
- **CNOT gate:** maps `(x, y) → (x, x ⊕ y)`. Reversible: apply it twice to get back the original.
- **Toffoli gate (CCNOT):** maps `(a, b, c) → (a, b, c ⊕ (a & b))`. Universal for reversible computation.
- **Why this matters for quantum:** All quantum gates are unitary, and unitary transformations are reversible. Classical reversible circuits are a special case of quantum circuits.

### 1.3 Randomised Computation
- A **probability vector** over `n` outcomes is a column vector `p` where each entry `p_i ≥ 0` and `Σ p_i = 1`.
- **Ket notation:** `p = Σ p_i |i⟩` where `|i⟩` is the i-th standard basis vector. This is the same notation used later for quantum states.
- A **stochastic matrix** `M` has columns that are probability vectors (each column sums to 1). Applying `M` to `p` gives `Mp` — a new probability distribution.
- **Why this matters:** Quantum states are like probability vectors, but with complex amplitudes that can be negative and interfere. The ket notation carries over directly.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Bit string | A sequence of 0s and 1s, written `x_1 x_2 ... x_n` |
| `{0,1}^n` | The set of all n-bit strings (has `2^n` elements) |
| XOR (`⊕`) | Addition mod 2: `0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0` |
| Reversible gate | A gate where input is recoverable from output |
| CNOT | Controlled-NOT: `(x,y) → (x, x⊕y)` |
| Toffoli | `(a,b,c) → (a, b, c⊕(a&b))` — universal reversible gate |
| Probability vector | Column vector with non-negative entries summing to 1 |
| Stochastic matrix | Matrix whose columns are probability vectors |
| Ket `\|i⟩` | Standard basis vector (column with 1 in position i, 0 elsewhere) |

---

## What This Unlocks

Week 1 establishes the classical foundations that quantum computing extends:
- Binary encoding → qubits encode information in superpositions of `|0⟩` and `|1⟩`
- Reversible gates → all quantum gates are reversible (unitary)
- Probability vectors + ket notation → quantum state vectors use the same notation, but with complex amplitudes

---

## Common Confusion Points

**"Why does reversibility matter if quantum gates are just matrices?"**
It matters because unitarity (the quantum requirement) *implies* reversibility. Understanding reversible classical gates is the bridge.

**"What's the difference between XOR and addition?"**
XOR is addition mod 2 — it ignores any carry. `1 ⊕ 1 = 0`, not 2.

**"Why does the stochastic matrix apply to the column vector on the left?"**
Convention: column vectors represent states, and matrices act on them from the left: `M|p⟩`. This is consistent with how quantum gates act on quantum state vectors.

---

## Prerequisite Links

- Struggling with probability vectors? → `prerequisites/crash_courses.md` § 3 (Probability Theory)
- Struggling with ket notation algebra? → re-read section 1.3 of the PDF alongside § 1 of crash courses (Linear Algebra)
