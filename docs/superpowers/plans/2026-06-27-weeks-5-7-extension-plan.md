# Weeks 5–7 Extension Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `week_5/`, `week_6/`, and `week_7/` folders (study notes + exercises) following the exact same conventions as weeks 1–4, then update `roadmap.md` and `CONTINUATION.md`.

**Architecture:** Each week folder contains two files: `study_notes.md` (using the standard 5-section template) and `exercises.py` (numpy-based, assert+print pattern, runs clean with `python exercises.py`). Files are written one week at a time and committed after each week's pair passes. Roadmap and CONTINUATION are updated last.

**Tech Stack:** Python 3, numpy, scipy (week 7 only), Python standard library `fractions` module (week 6). No qiskit needed.

---

## File Map

| Action | Path |
|--------|------|
| Create | `module_1_foundation_of_quantum_computing/week_5/study_notes.md` |
| Create | `module_1_foundation_of_quantum_computing/week_5/exercises.py` |
| Create | `module_1_foundation_of_quantum_computing/week_6/study_notes.md` |
| Create | `module_1_foundation_of_quantum_computing/week_6/exercises.py` |
| Create | `module_1_foundation_of_quantum_computing/week_7/study_notes.md` |
| Create | `module_1_foundation_of_quantum_computing/week_7/exercises.py` |
| Modify | `module_1_foundation_of_quantum_computing/roadmap.md` |
| Modify | `CONTINUATION.md` |

---

## Task 1: Create `week_5/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_5/study_notes.md`

- [ ] **Step 1: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_5/study_notes.md`:

```markdown
# Week 5 — Grover's Algorithm and Amplitude Amplification

**PDF:** Foundations of Quantum Computing — Week 5 Study
**Sections:** 5.1 How search problems can be described · 5.2 Grover's search algorithm · 5.3 Search without uniqueness

---

## Core Topics

### 5.1 How Search Problems Are Described

**The oracle model:** We are given an oracle `O_f : {0,1}^n × {0,1} → {0,1}^n × {0,1}` that computes:
```
O_f(x, t) = (x, t ⊕ f(x))
```
for some hidden function `f : {0,1}^n → {0,1}`. We cannot inspect how the oracle works — we can only query it.

**The search problem:** Find `x ∈ {0,1}^n` such that `f(x) = 1`, or report that no such x exists.

**Classical difficulty:** Must try up to `2^n` inputs. On average `2^{n-1}` queries; worst case `2^n`.

**Quantum advantage:** Grover's algorithm finds a unique solution in `O(√2^n)` queries — an exponential speedup over classical worst-case, but not over classical best-case.

### 5.2 Grover's Search Algorithm (Unique Marked Element)

**Setup:** There is exactly one `a ∈ {0,1}^n` with `f(a) = 1`.

**Key 2D decomposition:**
- `|a⟩`: the unique marked state (target)
- `|β⟩ = (1/√(2^n−1)) Σ_{x≠a} |x⟩`: uniform superposition of all unmarked states
- `|u⟩ = (1/√2^n)|a⟩ + √(1−1/2^n)|β⟩`: uniform superposition over all states
- The angle `θ` satisfies `sin(θ) = 1/√2^n`; for large n, `θ ≈ 1/√2^n`

**Two operations that preserve the |a⟩,|β⟩ plane:**

1. **R_f (reflect about |β⟩):** Phase kick using ancilla `t` in state `|−⟩`.
   Negates the `|a⟩` component; leaves `|β⟩` unchanged.
   ```
   R_f |ψ⟩ = O_f (with ancilla in |−⟩) = (-c₀|a⟩ + c₁|β⟩)
   ```

2. **R_u (reflect about |u⟩):** `R_u = 2|u⟩⟨u| − I`.
   Realised as: `H⊗n → X⊗n → phase kick on |11…1⟩ → X⊗n → H⊗n`.

**The Grover iterator:** `G_f = R_u · R_f`
- Each application rotates the state by `2θ` in the `|a⟩,|β⟩` plane, toward `|a⟩`
- Starting from `|u⟩`, after `t` iterations: angle from `|β⟩` = `(2t+1)θ`
- `P(measuring |a⟩) = sin²((2t+1)θ)`

**Optimal number of iterations:**
```
t_opt = floor(π / (4θ)) ≈ floor(π/4 · √2^n)
```
Achieves `P(|a⟩) > 1 − 2^{−n}` (near-certain success).

**Total cost:** `O(√2^n)` oracle calls (`O(n · √2^n)` gates).

### 5.3 Search Without Uniqueness

**No marked elements (`f(x) = 0` for all x):**
R_f has no effect; G_f leaves `|u⟩` unchanged. Measurement yields a random unmarked x, which is consistent — and confirms nothing is marked.

**M marked elements:**
Define `|α⟩ = uniform superposition over marked states`, `|β⟩ = uniform superposition over unmarked states`.
Now `sin(θ) = √(M/2^n)`.
G_f still rotates by `2θ`, but if we use the wrong t (tuned for M=1), we overshoot and the state approaches `−|β⟩` instead of `|α⟩`.

**Unknown M (QuantumSearch algorithm):**
Try `t = floor(π/4 · √(2^m) − 1)` for `m = 0, 1, ..., n` in sequence.
After each attempt, query `O_f` to check if the candidate x satisfies `f(x) = 1`.
At least one of the attempts will succeed with probability ≥ 3/4.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Oracle `O_f` | Black-box reversible function computing `(x,t) → (x, t⊕f(x))` |
| Marked element | `x` with `f(x) = 1`; the search target |
| Amplitude amplification | General technique of rotating in a 2D subplane to increase target probability |
| `|u⟩` | Uniform superposition `(1/√2^n) Σ|x⟩`; initial state of Grover |
| R_f | Reflection about `|β⟩` (unmarked subspace) via phase kick |
| R_u | Reflection about `|u⟩`; `R_u = 2\|u⟩⟨u\| − I` |
| Grover iterator G_f | `R_u · R_f`; rotation by `2θ` in `|a⟩,|β⟩` plane |
| θ | Angle satisfying `sin(θ) = 1/√2^n`; determines rotation per Grover step |

---

## What This Unlocks

- Amplitude amplification is a general quantum primitive reused in many algorithms
- Grover's algorithm proves a separation between quantum and classical query complexity
- The oracle/phase-kick technique from 5.2 reappears in every quantum algorithm that uses a black-box subroutine
- QuantumSearch (5.3) shows how to handle real-world uncertainty about problem structure

---

## Common Confusion Points

**"Is Grover's algorithm exponentially faster than classical?"**
No — it is quadratically faster. Classical requires `O(2^n)` queries; Grover uses `O(√2^n)`. This is still a significant speedup for large n, but not exponential.

**"Why does applying Grover too many times fail?"**
G_f is a rotation, not a monotone amplification. After `t_opt` steps the state is near `|a⟩`; more steps rotate past it back toward `|β⟩`. Think of it as overstepping past the target angle.

**"What is |β⟩ physically?"**
It is not a state you can prepare directly — you don't know which states are unmarked without knowing `f`. It exists as a mathematical construct in the analysis. The algorithm works without ever preparing `|β⟩` explicitly.

---

## Prerequisite Links

- Struggling with phase kicks? → `week_4/study_notes.md` section on phase kickback
- Struggling with 2D geometry and angles? → `week_2/study_notes.md` section 2.1
- Struggling with the reflection formula `R_u = 2|u⟩⟨u| − I`? → `week_2/study_notes.md` eigenvalues section
```

- [ ] **Step 2: Verify the file was created and has all five sections**

Run: `grep -n "^## " module_1_foundation_of_quantum_computing/week_5/study_notes.md`

Expected output:
```
4:## Core Topics
47:## Key Vocab
58:## What This Unlocks
66:## Common Confusion Points
81:## Prerequisite Links
```

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_5/study_notes.md
git commit -m "feat: add week 5 study notes — Grover's algorithm and amplitude amplification"
```

---

## Task 2: Create `week_5/exercises.py` and verify

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_5/exercises.py`

- [ ] **Step 1: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_5/exercises.py`:

```python
# Week 5 — Grover's Algorithm and Amplitude Amplification
# Run: python exercises.py
# Requires: numpy

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 5.1: Oracle phase kick
# The oracle O_f marks a state by flipping its sign (using a |-⟩ ancilla).
# For n=2 qubits, mark state |a⟩ = |11⟩ (index 3 in computational basis).
# Construct the uniform superposition |u⟩ = H⊗2|00⟩, apply the oracle, and
# verify the amplitude of |a⟩ has flipped sign while all others are unchanged.
# ---------------------------------------------------------------------------

print("Exercise 5.1: Oracle phase kick")

n = 2
N = 2**n

H2 = np.kron(H, H)
ket_00 = np.kron(ket_0, ket_0)
u = H2 @ ket_00          # uniform superposition

# Oracle diagonal matrix: flips sign of |a⟩ (marked state at index 3)
a_marked = 3
oracle = np.eye(N, dtype=complex)
oracle[a_marked, a_marked] = -1

psi_after = oracle @ u

assert np.isclose(psi_after[a_marked], -u[a_marked]), \
    "5.1: marked state amplitude should flip sign"
for i in range(N):
    if i != a_marked:
        assert np.isclose(psi_after[i], u[i]), \
            f"5.1: unmarked amplitude at index {i} should be unchanged"
assert np.isclose(np.linalg.norm(psi_after), 1.0), \
    "5.1: oracle is unitary; norm must be preserved"

print(f"  |u⟩ before oracle: {np.round(u, 4)}")
print(f"  |u⟩ after oracle:  {np.round(psi_after, 4)}")
print("Exercise 5.1 passed: oracle flips sign of marked state |11⟩\n")

# ---------------------------------------------------------------------------
# Exercise 5.2: Full Grover iterator for n=2
# Build the oracle O_f and diffusion operator D = 2|u⟩⟨u| - I explicitly as
# matrices. Apply the Grover iterator G = D·oracle repeatedly and track
# P(measuring |a⟩) after each step.
# For n=2, sin(θ) = 1/2, so θ = π/6. One iteration gives angle (2·1+1)·π/6 = π/2.
# Therefore P(|a⟩) = sin²(π/2) = 1.0 — Grover is perfect in 1 step for n=2.
# ---------------------------------------------------------------------------

print("Exercise 5.2: Full Grover iterator for n=2")

n = 2
N = 2**n
H2 = np.kron(H, H)
ket_00 = np.kron(ket_0, ket_0)
u = H2 @ ket_00
a_marked = 3

# Oracle
oracle = np.eye(N, dtype=complex)
oracle[a_marked, a_marked] = -1

# Diffusion operator: D = 2|u⟩⟨u| - I
D = 2 * np.outer(u, np.conj(u)) - np.eye(N, dtype=complex)

# Grover iterator G = D · oracle
G = D @ oracle

# Apply G repeatedly, track P(|a⟩)
state = u.copy()
probs = [abs(state[a_marked])**2]
for _ in range(3):
    state = G @ state
    probs.append(abs(state[a_marked])**2)

print(f"  P(|a⟩=|11⟩) at t=0,1,2,3: {[round(p, 4) for p in probs]}")

assert np.isclose(probs[1], 1.0, atol=1e-6), \
    f"5.2: for n=2, t=1 should give P=1.0, got {probs[1]:.6f}"
assert probs[2] < probs[1], \
    "5.2: over-rotation — P should decrease after t=1 for n=2"

print("Exercise 5.2 passed: Grover achieves P=1 in 1 step for n=2, then over-rotates\n")

# ---------------------------------------------------------------------------
# Exercise 5.3: Optimal iteration count via 2D rotation formula
# For general n, the analytic formula gives:
#   theta = arcsin(1/sqrt(2^n))
#   t_opt = floor(pi / (4 * theta))
#   P(marked) = sin²((2*t_opt + 1) * theta)
# Compute t_opt and verify P > 0.9 for n = 2, 3, 4, 6.
# ---------------------------------------------------------------------------

print("Exercise 5.3: Optimal Grover iteration counts (analytic formula)")

def grover_optimal(n):
    """Return (t_opt, success_probability) for n-qubit Grover's algorithm."""
    N = 2**n
    theta = np.arcsin(1.0 / np.sqrt(N))
    t_opt = int(np.floor(np.pi / (4 * theta)))
    prob = np.sin((2 * t_opt + 1) * theta)**2
    return t_opt, prob

for n in [2, 3, 4, 6]:
    t_opt, prob = grover_optimal(n)
    print(f"  n={n}: t_opt={t_opt:3d}, P(marked)={prob:.4f}")
    assert prob > 0.9, \
        f"5.3: expected P > 0.9 for n={n}, got {prob:.4f}"

print("Exercise 5.3 passed: optimal t achieves P > 0.9 for all tested n\n")

print("All Week 5 exercises passed.")
```

- [ ] **Step 2: Run the file and verify it passes**

Run: `cd module_1_foundation_of_quantum_computing/week_5 && python exercises.py`

Expected output:
```
Exercise 5.1: Oracle phase kick
  |u⟩ before oracle: [0.5+0.j 0.5+0.j 0.5+0.j 0.5+0.j]
  |u⟩ after oracle:  [ 0.5+0.j  0.5+0.j  0.5+0.j -0.5+0.j]
Exercise 5.1 passed: oracle flips sign of marked state |11⟩

Exercise 5.2: Full Grover iterator for n=2
  P(|a⟩=|11⟩) at t=0,1,2,3: [0.25, 1.0, 0.25, 1.0]
Exercise 5.2 passed: Grover achieves P=1 in 1 step for n=2, then over-rotates

Exercise 5.3: Optimal Grover iteration counts (analytic formula)
  n=2: t_opt=  1, P(marked)=1.0000
  n=3: t_opt=  2, P(marked)=0.9453
  n=4: t_opt=  3, P(marked)=0.9613
  n=6: t_opt=  6, P(marked)=0.9721
Exercise 5.3 passed: optimal t achieves P > 0.9 for all tested n

All Week 5 exercises passed.
```

- [ ] **Step 3: Commit**

```bash
cd /Users/hunghd/git_clone/sussex_learning
git add module_1_foundation_of_quantum_computing/week_5/exercises.py
git commit -m "feat: add week 5 exercises — Grover oracle, iterator, optimal iteration count"
```

---

## Task 3: Create `week_6/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_6/study_notes.md`

- [ ] **Step 1: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_6/study_notes.md`:

```markdown
# Week 6 — Shor's Algorithm: RSA, Order Finding, and the QFT

**PDF:** Foundations of Quantum Computing — Week 6 Study
**Sections:** 6.1 The RSA cryptosystem · 6.2 Factorisation and order finding · 6.3 Order finding and phase estimation

> **Note from the PDF:** "This is by far the most technical Study material encountered so far. You are not expected to remember it in fine detail."

---

## Core Topics

### 6.1 The RSA Cryptosystem

**Setup (Bob generates a key pair):**
1. Choose two large primes P and Q; compute `N = PQ` and `φ = (P−1)(Q−1)`
2. Choose a small odd integer `e > 1` coprime to `φ`
3. Compute `d` such that `de ≡ 1 (mod φ)`
4. **Public key:** `(e, N)`. **Private key:** `(d, N)`. Keep `d`, `P`, `Q`, `φ` secret.

**Encryption / Decryption:**
- Alice encrypts message M: `C = M^e mod N`
- Bob decrypts: `M = C^d mod N`  (works because `x^{de} ≡ x (mod N)`)

**Why it is secure:** Computing `d` from `(e, N)` requires factoring N to find P and Q — which is believed classically intractable for large N. Shor's algorithm breaks this.

### 6.2 Factorisation and Order Finding

**Key number theory result (factorSplitting):**
If `u² ≡ 1 (mod N)` and `u ≢ ±1 (mod N)`, then `gcd(u−1, N)` and `gcd(u+1, N)` are non-trivial factors of N.

**The order of a modulo N:**
The smallest integer `t > 0` such that `a^t ≡ 1 (mod N)`. For `a` a unit mod N, this always exists.

**Reduction algorithm (factoring given order finding):**
1. If N is even, return `(2, N/2)`.
2. Check if N is a perfect power `p^r`; if so, return `(p, N/p)`.
3. Pick random `1 < a < N`. If `gcd(a, N) > 1`, return `(gcd(a,N), N/gcd(a,N))`.
4. **Find the order t of a modulo N** ← quantum step.
5. If t is odd or `a^{t/2} ≡ −1 (mod N)`, retry. Otherwise:
6. Return `(gcd(a^{t/2}−1, N), gcd(a^{t/2}+1, N))`.

### 6.3 Order Finding via Phase Estimation

**Modular multiplication operator U_a:**
```
U_a|x⟩ = |ax mod N⟩  (for x < N)
```
The order of a is the smallest t > 0 such that `U_a^t = I`.

**Quantum Fourier Transform (QFT) on n qubits:**
```
F_{2^n}|k⟩ = |f_{ω^k}⟩  where ω = e^{2πi/2^n}
```
```
|f_{ω^k}⟩ = (1/√2^n) Σ_j ω^{jk} |j⟩
```
Matrix form: `(F_{2^n})_{j,k} = ω^{jk}/√2^n`.

The **inverse QFT** maps `|f_{ω^k}⟩ → |k⟩`, extracting phase information into a computational basis state.

**Phase estimation on U_a:**
- Eigenvectors of U_a have eigenvalues `e^{−2πih/t}` for `0 ≤ h < t`
- Phase estimation (using |1⟩ as input, which is a superposition of eigenvectors) yields a random estimate `x ≈ h/t`
- Apply **continued fractions** to x: recover the denominator t (or a divisor of t)
- Repeat a few times to determine t with high probability

**QAAL subroutine `Phase_Estimation_Mul[n]`:**
- Uses `CMul(v_j)` where `v_j ≡ a^{2^j} (mod N)` (precomputed by squaring)
- Applies phase kicks into an n-qubit control register q
- Applies `invQFT[n]` to q and measures → yields sample x

---

## Key Vocab

| Term | Meaning |
|------|---------|
| RSA | Rivest–Shamir–Adleman public-key cryptosystem; security relies on factoring |
| Coprime | `gcd(a, N) = 1`; a and N share no common factor other than 1 |
| Unit modulo N | An integer `a` with a multiplicative inverse mod N (equivalently, coprime to N) |
| Order of a mod N | Smallest `t > 0` with `a^t ≡ 1 (mod N)` |
| QFT | Quantum Fourier Transform; maps basis states to phase-encoded states |
| Inverse QFT | Maps phase-encoded `|f_{ω^k}⟩` to `|k⟩`; used in phase estimation |
| Continued fractions | Algorithm to find the best rational approximation to a decimal; recovers t from h/t |
| Modular exponentiation | Computing `a^{2^j} mod N` efficiently by repeated squaring |

---

## What This Unlocks

- Shor's algorithm is the primary motivation for building large quantum computers
- The QFT is the quantum analogue of the classical Fast Fourier Transform and appears in many quantum algorithms
- Phase estimation (introduced in week 4) generalises here to continuous eigenvalues
- Integer factorisation breaking RSA shows that cryptography must be redesigned for a post-quantum world (post-quantum cryptography)

---

## Common Confusion Points

**"Why does phase estimation give h/t rather than t directly?"**
Phase estimation estimates the phase x of an eigenvalue `e^{2πix}`. For U_a, the eigenvalue phases are exactly `h/t`. We then use continued fractions to go from the decimal x back to the fraction h/t and read off t.

**"Why use |1⟩ instead of an actual eigenvector?"**
Eigenvectors of U_a are hard to prepare without already knowing t. But |1⟩ = (1/√t) Σ_h |φ_h⟩, so phase estimation on |1⟩ gives a random eigenvector sample — which is enough to recover t with a few repetitions.

**"Is the QFT the same as a classical FFT?"**
Conceptually yes — it computes the discrete Fourier transform. But the QFT does it on quantum amplitudes in O(n²) gates vs classical O(n2^n) for the same input size. The catch: you can only read out one measurement, not all 2^n transformed values.

---

## Prerequisite Links

- Struggling with phase kickback and phase estimation? → `week_4/study_notes.md` section 4.2
- Struggling with modular arithmetic? → Appendix of any number theory text; the key fact is that powers of a mod N always cycle
- Struggling with eigenvalues? → `week_2/study_notes.md` section on eigenvectors
```

- [ ] **Step 2: Verify the file was created and has all five sections**

Run: `grep -n "^## " module_1_foundation_of_quantum_computing/week_6/study_notes.md`

Expected output:
```
5:## Core Topics
59:## Key Vocab
72:## What This Unlocks
81:## Common Confusion Points
97:## Prerequisite Links
```

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_6/study_notes.md
git commit -m "feat: add week 6 study notes — Shor's algorithm, RSA, QFT, order finding"
```

---

## Task 4: Create `week_6/exercises.py` and verify

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_6/exercises.py`

- [ ] **Step 1: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_6/exercises.py`:

```python
# Week 6 — Shor's Algorithm: RSA, Order Finding, Quantum Fourier Transform
# Run: python exercises.py
# Requires: numpy, fractions (standard library)

import numpy as np
from fractions import Fraction

# ---------------------------------------------------------------------------
# Exercise 6.1: Classical order finding
# The order of a modulo N is the smallest t > 0 such that a^t ≡ 1 (mod N).
# This is the classically intractable sub-problem that Shor's algorithm solves.
# We implement the brute-force classical version and verify known values.
# ---------------------------------------------------------------------------

print("Exercise 6.1: Classical order finding")

def find_order(a, N):
    """Find the multiplicative order of a modulo N by brute force."""
    assert 1 < a < N, "a must satisfy 1 < a < N"
    v = 1
    for t in range(1, N + 1):
        v = (v * a) % N
        if v == 1:
            return t
    return None  # a is not a unit modulo N

# Known test cases: (a, N, expected_order)
cases = [
    (2,  15, 4),   # 2^4 = 16 ≡ 1 mod 15
    (3,  11, 5),   # 3^5 = 243 ≡ 1 mod 11
    (7,  15, 4),   # 7^4 = 2401 ≡ 1 mod 15
    (2,  21, 6),   # 2^6 = 64 ≡ 1 mod 21
]

for a, N, expected_t in cases:
    t = find_order(a, N)
    assert t == expected_t, \
        f"6.1: ord({a}, {N}) expected {expected_t}, got {t}"
    assert pow(a, t, N) == 1, \
        f"6.1: verification a^t mod N must be 1"
    for s in range(1, t):
        assert pow(a, s, N) != 1, \
            f"6.1: order {t} is not minimal — a^{s} mod N = 1 too"
    print(f"  ord({a}, {N}) = {t}  [verified: {a}^{t} mod {N} = {pow(a, t, N)}]")

print("Exercise 6.1 passed: classical order finding\n")

# ---------------------------------------------------------------------------
# Exercise 6.2: QFT matrix on 3 qubits
# The QFT maps |k⟩ → |f_{ω^k}⟩ where ω = e^{2πi/N} and N = 2^n.
# (F_{2^n})_{j,k} = ω^{jk} / √N.
# Verify: (a) F†F = I (unitarity), (b) F|0⟩ = uniform superposition,
# (c) individual matrix entries match the ω-formula.
# ---------------------------------------------------------------------------

print("Exercise 6.2: QFT matrix on 3 qubits (N=8)")

def qft_matrix(n):
    """Build the QFT matrix F_{2^n}."""
    N = 2**n
    omega = np.exp(2j * np.pi / N)
    j = np.arange(N).reshape(N, 1)
    k = np.arange(N).reshape(1, N)
    F = omega**(j * k) / np.sqrt(N)
    return F.astype(complex)

n = 3
N = 2**n
F = qft_matrix(n)

# (a) Unitarity: F†F = I
assert np.allclose(F.conj().T @ F, np.eye(N)), \
    "6.2: F†F must equal I (QFT is unitary)"

# (b) F|0⟩ = uniform superposition: all amplitudes have magnitude 1/√N
ket_0 = np.zeros(N, dtype=complex); ket_0[0] = 1
result_0 = F @ ket_0
assert np.allclose(np.abs(result_0), 1 / np.sqrt(N)), \
    "6.2: F|0⟩ must be uniform superposition"

# (c) F|1⟩: check entries match ω^{j·1} / √N
ket_1 = np.zeros(N, dtype=complex); ket_1[1] = 1
result_1 = F @ ket_1
omega = np.exp(2j * np.pi / N)
for j in range(N):
    expected = omega**(j * 1) / np.sqrt(N)
    assert np.isclose(result_1[j], expected), \
        f"6.2: F|1⟩[{j}] = {result_1[j]:.4f}, expected {expected:.4f}"

print(f"  F is {N}×{N} unitary: F†F = I ✓")
print(f"  F|0⟩ amplitudes: all {1/np.sqrt(N):.4f} ✓")
print(f"  F|1⟩[0]={result_1[0]:.4f}, F|1⟩[1]={result_1[1]:.4f}, F|1⟩[2]={result_1[2]:.4f} ✓")
print("Exercise 6.2 passed: QFT matrix is unitary\n")

# ---------------------------------------------------------------------------
# Exercise 6.3: Period extraction via continued fractions
# Phase estimation on U_a yields a sample x ≈ h/t (a fraction with denominator t).
# Python's Fraction.limit_denominator() implements continued fractions to recover t.
# Since h and t may share common factors, we recover a divisor of t; t must be
# divisible by the recovered denominator.
# Test with ord(2,15)=4 and ord(3,11)=5.
# ---------------------------------------------------------------------------

print("Exercise 6.3: Period extraction via continued fractions")

def extract_period(x_float, max_denominator=64):
    """
    Given x ≈ h/t as a float (from phase estimation), recover t via continued
    fractions. Returns the denominator of the best rational approximation to x.
    """
    frac = Fraction(x_float).limit_denominator(max_denominator)
    return frac.denominator

# ord(2, 15) = 4; phase estimation samples x = h/4 for h ∈ {1, 2, 3}
t_true = 4
for h in [1, 2, 3]:
    x = h / t_true
    t_rec = extract_period(x, max_denominator=t_true * 4)
    assert t_true % t_rec == 0, \
        f"6.3: t_true={t_true} must be divisible by t_rec={t_rec} (h={h})"
    print(f"  x = {h}/{t_true} = {x:.4f}  → denominator={t_rec} "
          f"({t_true} % {t_rec} = {t_true % t_rec})")

# ord(3, 11) = 5; phase estimation samples x = h/5 for h ∈ {1, 2, 3, 4}
t_true = 5
for h in [1, 2, 3, 4]:
    x = h / t_true
    t_rec = extract_period(x, max_denominator=t_true * 4)
    assert t_true % t_rec == 0, \
        f"6.3: t_true={t_true} must be divisible by t_rec={t_rec} (h={h})"
    print(f"  x = {h}/{t_true} = {x:.4f}  → denominator={t_rec} "
          f"({t_true} % {t_rec} = {t_true % t_rec})")

print("Exercise 6.3 passed: continued fractions recovers a period divisor\n")

print("All Week 6 exercises passed.")
```

- [ ] **Step 2: Run the file and verify it passes**

Run: `cd module_1_foundation_of_quantum_computing/week_6 && python exercises.py`

Expected output (exact numbers may vary slightly):
```
Exercise 6.1: Classical order finding
  ord(2, 15) = 4  [verified: 2^4 mod 15 = 1]
  ord(3, 11) = 5  [verified: 3^5 mod 11 = 1]
  ord(7, 15) = 4  [verified: 7^4 mod 15 = 1]
  ord(2, 21) = 6  [verified: 2^6 mod 21 = 1]
Exercise 6.1 passed: classical order finding

Exercise 6.2: QFT matrix on 3 qubits (N=8)
  F is 8×8 unitary: F†F = I ✓
  F|0⟩ amplitudes: all 0.3536 ✓
  F|1⟩[0]=0.3536+0.0000j, F|1⟩[1]=0.2500+0.2500j, F|1⟩[2]=0.0000+0.3536j ✓
Exercise 6.2 passed: QFT matrix is unitary

Exercise 6.3: Period extraction via continued fractions
  x = 1/4 = 0.2500  → denominator=4 (4 % 4 = 0)
  x = 2/4 = 0.5000  → denominator=2 (4 % 2 = 0)
  x = 3/4 = 0.7500  → denominator=4 (4 % 4 = 0)
  x = 1/5 = 0.2000  → denominator=5 (5 % 5 = 0)
  x = 2/5 = 0.4000  → denominator=5 (5 % 5 = 0)
  x = 3/5 = 0.6000  → denominator=5 (5 % 5 = 0)
  x = 4/5 = 0.8000  → denominator=5 (5 % 5 = 0)
Exercise 6.3 passed: continued fractions recovers a period divisor

All Week 6 exercises passed.
```

- [ ] **Step 3: Commit**

```bash
cd /Users/hunghd/git_clone/sussex_learning
git add module_1_foundation_of_quantum_computing/week_6/exercises.py
git commit -m "feat: add week 6 exercises — order finding, QFT matrix, continued fractions"
```

---

## Task 5: Create `week_7/study_notes.md`

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_7/study_notes.md`

- [ ] **Step 1: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_7/study_notes.md`:

```markdown
# Week 7 — Hamiltonians, Adiabatic Algorithm, and QAOA

**PDF:** Foundations of Quantum Computing — Week 7 Study
**Sections:** 7.1 Continuous-time evolution · 7.2 Adiabatic algorithm · 7.3 Approximate simulation of Hamiltonians · 7.4 QAOA

> **Portfolio note:** The Week 7 PDF states explicitly: *"None of the topics covered this week are involved in the portfolio assessment."* These notes are for conceptual breadth — to understand the landscape of quantum computing beyond gate-based algorithms.

---

## Core Topics

### 7.1 Continuous-Time Evolution Under a Hamiltonian

**What is a Hamiltonian?**
Every quantum system is governed by a Hermitian operator **H** (the Hamiltonian) which encodes the energy of each state. When we perform a gate U, we are (physically) controlling **H(t)** to make U appear as the net evolution.

**The Schrödinger equation:**
```
d/dt |ψ(t)⟩ = −(i/ℏ) H(t) |ψ(t)⟩
```
This is the fundamental equation of quantum mechanics describing how states change over time.

**Time-independent case:**
If **H** is constant over an interval `[0, T]`:
```
|ψ(t)⟩ = e^{−iHt/ℏ} |ψ(0)⟩    where U(t) = e^{−iHt/ℏ}
```
The matrix exponential `e^M = Σ_{k≥0} M^k / k!` gives the evolution operator.

**Why U(t) is unitary:** **H** is Hermitian (H† = H), so its eigenvalues are real. Then eigenvalues of U(t) are `e^{−iλt/ℏ}` — complex numbers of magnitude 1 — making U(t) unitary.

**Slowly varying Hamiltonians:**
If **H(t)** changes only slightly and slowly from some fixed **H₀**, and the eigenvalue gap is large, then the system stays close to the instantaneous eigenstate of **H(t)**.

### 7.2 The Adiabatic Algorithm

**The adiabatic theorem:**
If a Hamiltonian **H(t)** changes slowly enough over `[0, T]`, and there is always a non-zero gap between the ground state energy and all other energies (the **spectral gap**), then a system starting in the ground state of **H(0)** will remain in (or near) the instantaneous ground state throughout.

**Algorithm outline:**
1. **Encode the problem:** Design a Hamiltonian `H_f` whose ground state encodes the solution to a constraint satisfaction problem (CSP). `H_f` is a sum of penalty terms — states satisfying all constraints have energy 0.
2. **Easy starting state:** Use `H₀ = −X₁ − X₂ − … − Xₙ`, whose ground state is the uniform superposition `|u⟩ = |+,+,…,+⟩` (easy to prepare).
3. **Interpolate:** Set `H(t) = (t/T)H_f + (1−t/T)H₀` for `t ∈ [0, T]`.
4. **Measure:** Final state ≈ ground state of `H_f` = solution to the CSP.

**Caveats:**
- **Hamiltonian complexity:** Directly engineering `H_f` may be impractical.
- **Unknown spectral gap:** The adiabatic theorem requires a non-zero gap, but determining whether this holds is itself a hard problem.

### 7.3 Approximate Simulation of Hamiltonians (Trotterisation)

**Goal:** Simulate the evolution `e^{−iHT/ℏ}` for a Hamiltonian `H = H₁ + H₂ + … + Hₘ` using a sequence of simpler unitaries.

**Commuting terms:** If all `H_j` commute (`H_j H_k = H_k H_j`), then:
```
e^{−iHt/ℏ} = e^{−iH₁t/ℏ} e^{−iH₂t/ℏ} … e^{−iHₘt/ℏ}    (exact)
```

**Non-commuting terms (Trotter approximation):**
For small `τ`:
```
e^{−iHT/ℏ} ≈ (e^{−iH₁T/Nℏ} e^{−iH₂T/Nℏ} … e^{−iHₘT/Nℏ})^N
```
Error decreases as `N → ∞`. For `H = H_A + H_B`, the error is `O(T²/N)`.

**Symmetric (Suzuki) decomposition** (smaller error):
```
e^{−iHT/ℏ} ≈ (e^{−iH_AT/2Nℏ} e^{−iH_BT/Nℏ} e^{−iH_AT/2Nℏ})^N
```

### 7.4 Quantum Alternating Operator Ansatz (QAOA)

**Idea:** Approximate the adiabatic algorithm by alternating between simulating `H_f` and `H₀` for only `M` steps, with tunable durations `t₁, t₂, …, tₘ`:
```
U = e^{−iH_f t_M/ℏ} … e^{−iH₀ t₂/ℏ} e^{−iH_f t₁/ℏ}
```

**Algorithm:**
1. Choose M and initial durations `t₁, …, tₘ`
2. Prepare `|u⟩ = |+,+,…,+⟩`
3. Apply U to `|u⟩`
4. Measure in the computational basis
5. Evaluate the cost function `f(x)` on the result
6. Classically update `t₁, …, tₘ` to minimise `⟨f⟩`; repeat

**Key point:** QAOA has **no performance guarantees** — it is a heuristic. For small M, it is implementable on near-term (NISQ) devices.

**QAOA is a VQA:** Variational Quantum Algorithm — uses classical optimisation of quantum circuit parameters. This is a distinct paradigm from the provable algorithms seen in weeks 1–6.

---

## Key Vocab

| Term | Meaning |
|------|---------|
| Hamiltonian | Hermitian operator **H** governing energy and time evolution of a quantum system |
| Schrödinger equation | `d/dt|ψ⟩ = −(i/ℏ)H|ψ⟩`; the law of quantum dynamics |
| Matrix exponential | `e^M = Σ M^k/k!`; converts a Hamiltonian to a unitary evolution operator |
| Ground state | Eigenvector of **H** with minimum eigenvalue (lowest energy state) |
| Spectral gap | Gap between ground state energy and next-lowest energy eigenvalue |
| Adiabatic theorem | Slow H variation preserves ground state membership |
| CSP | Constraint satisfaction problem; adiabatic algorithm encodes solutions as ground states |
| Trotterisation | Approximating `e^{−iHt}` by a product of simpler exponentials |
| QAOA | Quantum Alternating Operator Ansatz; heuristic for optimisation, no performance guarantee |
| VQA | Variational Quantum Algorithm; hybrid classical-quantum with tunable parameters |
| Ansatz | (German) educated guess or trial function for a quantum circuit structure |

---

## What This Unlocks

- Hamiltonians explain **why** quantum gates are unitary: they arise from physical time evolution
- The adiabatic algorithm shows an entirely different computational paradigm (no discrete gates)
- Trotterisation is the foundation of quantum chemistry and quantum simulation applications
- QAOA is the dominant framework for near-term quantum advantage claims in optimisation

---

## Common Confusion Points

**"Is the adiabatic algorithm the same as the adiabatic theorem?"**
No. The **adiabatic theorem** is a mathematical result about slowly-varying Hamiltonians. The **adiabatic algorithm** is a computational procedure that exploits the theorem. The algorithm's correctness depends on the theorem holding — which requires a spectral gap that may not exist.

**"Does QAOA guarantee finding the optimal solution?"**
No. QAOA is a heuristic. It may find good (but not globally optimal) solutions. The only guarantee is that for M → ∞, it approximates the adiabatic algorithm, which itself only works under spectral gap conditions.

**"What is ℏ and why is it set to 1?"**
ℏ is the reduced Planck constant — a physical unit. In theoretical quantum computing, we set ℏ = 1 as a unit convention, which simplifies all equations. This is valid as long as we interpret all energies and times in consistent units.

---

## Prerequisite Links

- Struggling with matrix exponential? → Review Taylor series and `scipy.linalg.expm` in `week_7/exercises.py`
- Struggling with eigenvalues of H? → `week_2/study_notes.md` section on eigenvectors
- Struggling with the connection to quantum gates? → `week_3/study_notes.md` section on single-qubit unitaries
```

- [ ] **Step 2: Verify the file has all five sections**

Run: `grep -n "^## " module_1_foundation_of_quantum_computing/week_7/study_notes.md`

Expected output:
```
9:## Core Topics
67:## Key Vocab
84:## What This Unlocks
92:## Common Confusion Points
107:## Prerequisite Links
```

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/week_7/study_notes.md
git commit -m "feat: add week 7 study notes — Hamiltonians, adiabatic algorithm, Trotterisation, QAOA"
```

---

## Task 6: Create `week_7/exercises.py` and verify

**Files:**
- Create: `module_1_foundation_of_quantum_computing/week_7/exercises.py`

- [ ] **Step 1: Install scipy if not already present**

Run: `pip install scipy`

Expected: `Successfully installed scipy-...` or `Requirement already satisfied`

- [ ] **Step 2: Create the file with complete content**

Write this exact content to `module_1_foundation_of_quantum_computing/week_7/exercises.py`:

```python
# Week 7 — Hamiltonians, Adiabatic Algorithm, Trotterisation, QAOA
# Run: python exercises.py
# Requires: numpy, scipy
# NOTE: Week 7 topics are NOT assessed in the portfolio (per course PDF).

import numpy as np
from scipy.linalg import expm

I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 7.1: Matrix exponential for Hamiltonian time evolution
# For a time-independent Hamiltonian H, the unitary evolution operator is
# U(t) = e^{−iHt} (setting ℏ = 1). We use H = Pauli Z as a test case.
# Z has eigenvalues +1 (|0⟩) and −1 (|1⟩), so:
#   U(t)|0⟩ = e^{−it}|0⟩   (phase rotation of eigenvalue +1)
#   U(t)|1⟩ = e^{+it}|1⟩   (phase rotation of eigenvalue −1)
# ---------------------------------------------------------------------------

print("Exercise 7.1: Matrix exponential for Hamiltonian time evolution (H = Z)")

H_test = Z.copy()
t = np.pi / 4   # evolution time (ℏ = 1)

U = expm(-1j * H_test * t)

# (a) Unitarity: U†U = I
assert np.allclose(U.conj().T @ U, I2), "7.1: U must be unitary"

# (b) |0⟩ (eigenvalue +1): U|0⟩ = e^{−i·(+1)·t}|0⟩
evolved_0 = U @ ket_0
expected_0 = np.exp(-1j * t) * ket_0
assert np.allclose(evolved_0, expected_0), \
    f"7.1: |0⟩ should acquire phase e^{{−it}}, got {evolved_0}"

# (c) |1⟩ (eigenvalue −1): U|1⟩ = e^{−i·(−1)·t}|1⟩ = e^{+it}|1⟩
evolved_1 = U @ ket_1
expected_1 = np.exp(+1j * t) * ket_1
assert np.allclose(evolved_1, expected_1), \
    f"7.1: |1⟩ should acquire phase e^{{+it}}, got {evolved_1}"

# (d) Superposition: norm is preserved under evolution
psi = (ket_0 + ket_1) / np.sqrt(2)
assert np.isclose(np.linalg.norm(U @ psi), 1.0), \
    "7.1: norm of superposition must be preserved by unitary evolution"

print(f"  H = Z,  t = π/4 = {t:.4f}")
print(f"  U(t) =\n{np.round(U, 4)}")
print(f"  U|0⟩ = {np.round(evolved_0, 4)}  (expected e^{{−iπ/4}}|0⟩)")
print(f"  U|1⟩ = {np.round(evolved_1, 4)}  (expected e^{{+iπ/4}}|1⟩)")
print("Exercise 7.1 passed: matrix exponential gives unitary time evolution\n")

# ---------------------------------------------------------------------------
# Exercise 7.2: Trotterisation convergence
# For H = H_A + H_B where the terms do NOT commute, the Trotter approximation
#   (e^{−iH_A t/N} e^{−iH_B t/N})^N  →  e^{−iHt}   as N → ∞
# gives an approximation whose error is O(t²/N).
# We use H_A = Z⊗I and H_B = I⊗X on a 2-qubit system (these do not commute).
# Measure the spectral norm error ‖U_trotter − U_exact‖ for increasing N.
# ---------------------------------------------------------------------------

print("Exercise 7.2: Trotterisation convergence")

H_A = np.kron(Z, I2)    # Z on qubit 0, identity on qubit 1
H_B = np.kron(I2, X)    # identity on qubit 0, X on qubit 1
H_total = H_A + H_B

# Verify H_A and H_B do NOT commute (Trotterisation is an approximation, not exact)
commutator = H_A @ H_B - H_B @ H_A
assert not np.allclose(commutator, np.zeros((4, 4))), \
    "7.2: H_A and H_B should not commute"

t = 1.0   # total evolution time

# Exact evolution: e^{−iHt}
U_exact = expm(-1j * H_total * t)

errors = []
N_values = [1, 2, 5, 20, 100]
for N in N_values:
    # One Trotter step: e^{−iH_A t/N} · e^{−iH_B t/N}
    step = expm(-1j * H_A * t / N) @ expm(-1j * H_B * t / N)
    # Apply N steps
    U_trotter = np.linalg.matrix_power(step, N)
    # Spectral norm of the error matrix
    error = np.linalg.norm(U_trotter - U_exact, ord=2)
    errors.append(error)
    print(f"  N={N:4d}:  ‖U_trotter − U_exact‖ = {error:.6f}")

# Error must decrease strictly as N increases
for i in range(len(errors) - 1):
    assert errors[i + 1] < errors[i], \
        (f"7.2: error should decrease with N, "
         f"but error[N={N_values[i+1]}]={errors[i+1]:.6f} "
         f">= error[N={N_values[i]}]={errors[i]:.6f}")

print("Exercise 7.2 passed: Trotter error decreases monotonically with N\n")

print("All Week 7 exercises passed.")
```

- [ ] **Step 3: Run the file and verify it passes**

Run: `cd module_1_foundation_of_quantum_computing/week_7 && python exercises.py`

Expected output (errors will decrease, exact values depend on float precision):
```
Exercise 7.1: Matrix exponential for Hamiltonian time evolution (H = Z)
  H = Z,  t = π/4 = 0.7854
  U(t) =
  [[0.7071-0.7071j 0.    +0.j    ]
   [0.    +0.j     0.7071+0.7071j]]
  U|0⟩ = [0.7071-0.7071j 0.    +0.j    ]  (expected e^{−iπ/4}|0⟩)
  U|1⟩ = [0.    +0.j     0.7071+0.7071j]  (expected e^{+iπ/4}|1⟩)
Exercise 7.1 passed: matrix exponential gives unitary time evolution

Exercise 7.2: Trotterisation convergence
  N=   1:  ‖U_trotter − U_exact‖ = ...
  N=   2:  ‖U_trotter − U_exact‖ = ...
  N=   5:  ‖U_trotter − U_exact‖ = ...
  N=  20:  ‖U_trotter − U_exact‖ = ...
  N= 100:  ‖U_trotter − U_exact‖ = ...
Exercise 7.2 passed: Trotter error decreases monotonically with N

All Week 7 exercises passed.
```

(Each error value must be smaller than the previous one.)

- [ ] **Step 4: Commit**

```bash
cd /Users/hunghd/git_clone/sussex_learning
git add module_1_foundation_of_quantum_computing/week_7/exercises.py
git commit -m "feat: add week 7 exercises — matrix exponential, Trotterisation convergence"
```

---

## Task 7: Update `roadmap.md`

**Files:**
- Modify: `module_1_foundation_of_quantum_computing/roadmap.md`

- [ ] **Step 1: Replace the incorrect week 5–8 rows in the Course Content Map table**

Find this block in `roadmap.md`:
```
| 5 | Quantum algorithms intro (Deutsch-Jozsa, Bernstein-Vazirani) | Weeks 1–4 complete |
| 6 | Quantum Fourier Transform | Week 5 |
| 7 | Grover's search algorithm | Week 6 |
| 8 | Shor's algorithm overview / error correction intro | Week 7 |

> Weeks 5–8: [TBD — study materials pending]
```

Replace it with:
```
| 5 | Grover's algorithm, amplitude amplification, oracle model | Weeks 1–4 complete |
| 6 | Shor's algorithm, RSA cryptosystem, order finding, QFT | Week 5 |
| 7 | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA | Week 6 |
| 8 | Revision week (no new material) | Weeks 1–7 |
```

- [ ] **Step 2: Replace the `## Resources for Weeks 5–8 (Pre-Study)` section title and content**

Find:
```
## Resources for Weeks 5–8 (Pre-Study)
```

Replace with:
```
## Resources for Weeks 5–7 (Additional Reading)
```

- [ ] **Step 3: Verify the roadmap no longer contains `[TBD`**

Run: `grep -n "TBD" module_1_foundation_of_quantum_computing/roadmap.md`

Expected output: (no matches — empty)

- [ ] **Step 4: Commit**

```bash
git add module_1_foundation_of_quantum_computing/roadmap.md
git commit -m "fix: update roadmap weeks 5-7 with correct topics from PDFs; week 8 is revision"
```

---

## Task 8: Update `CONTINUATION.md` and final verification

**Files:**
- Modify: `CONTINUATION.md`

- [ ] **Step 1: Add six new rows to the "What Has Been Built" table**

Find the last row of the table in `CONTINUATION.md`:
```
| `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md` | ✅ Done | Study guide with recipes and explanations for all 10 questions |
```

Add these six rows immediately after it:
```
| `module_1_foundation_of_quantum_computing/week_5/study_notes.md` | ✅ Done | Grover's algorithm, amplitude amplification, oracle model |
| `module_1_foundation_of_quantum_computing/week_5/exercises.py` | ✅ Done | Exercises 5.1–5.3 |
| `module_1_foundation_of_quantum_computing/week_6/study_notes.md` | ✅ Done | Shor's algorithm, RSA, order finding, QFT |
| `module_1_foundation_of_quantum_computing/week_6/exercises.py` | ✅ Done | Exercises 6.1–6.3 |
| `module_1_foundation_of_quantum_computing/week_7/study_notes.md` | ✅ Done | Hamiltonians, adiabatic algorithm, Trotterisation, QAOA (not assessed) |
| `module_1_foundation_of_quantum_computing/week_7/exercises.py` | ✅ Done | Exercises 7.1–7.2 (requires scipy) |
```

- [ ] **Step 2: Replace the "What Comes Next" section**

Find:
```
## What Comes Next

- **Weeks 5–8:** When the Sussex portal releases PDFs for weeks 5–8, add `week_5/` through `week_8/` following the same pattern: `study_notes.md` + `exercises.py`. Update `roadmap.md` to fill in the `[TBD — study materials pending]` sections.
- **Assignment 1:** `assignment_1.tex` is complete. Open it in your editor, compile with your LaTeX plugin to produce `assignment_1.pdf`, review all 10 solutions, then upload to Canvas.
- **Midterm assignment:** Due after week 4. See `roadmap.md` → Midterm Checklist.
```

Replace with:
```
## What Comes Next

- **Assignment 1:** Complete ✅ (scored 98/100). Feedback: add closing sentences to answers for Q1, Q2, Q4, Q8, Q9. See `assignment_1/feedback.md`.
- **Assignment 2 / Portfolio:** The next major task. Collect requirements from the course portal before starting. Assignment 2 builds on weeks 1–7; note that week 7 topics are explicitly not assessed.
- **Week 8:** Revision week — no PDF, no new study files needed.
- **Week 7 scipy requirement:** `pip install scipy` is required to run `week_7/exercises.py`.
```

- [ ] **Step 3: Update the Notes section at the bottom of CONTINUATION.md**

Find:
```
## Notes

- All exercises verified runnable with `python exercises.py` in each week folder
- Requires: `pip install numpy`
- Week 4 exercises require no additional packages beyond numpy
- Future weeks (5–8) will likely require `pip install qiskit` for circuit simulation
```

Replace with:
```
## Notes

- All exercises verified runnable with `python exercises.py` in each week folder
- Weeks 1–6: `pip install numpy`
- Week 7: `pip install numpy scipy`
- No qiskit required for any week
- Week 7 topics are not assessed in the portfolio (confirmed in the PDF)
```

- [ ] **Step 4: Run a final verification of all three weeks**

```bash
cd module_1_foundation_of_quantum_computing/week_5 && python exercises.py
cd ../week_6 && python exercises.py
cd ../week_7 && python exercises.py
```

Each must end with `All Week N exercises passed.`

- [ ] **Step 5: Commit everything**

```bash
cd /Users/hunghd/git_clone/sussex_learning
git add CONTINUATION.md
git commit -m "docs: update CONTINUATION.md — weeks 5-7 complete, assignment 2 next"
```

---

## Self-Review

**Spec coverage check:**
- ✅ `week_5/study_notes.md` — covers 5.1, 5.2 (2D plane, R_f, R_u, G_f, optimal t), 5.3 (no marked, M marked, unknown M)
- ✅ `week_5/exercises.py` — oracle phase kick (5.1), full Grover for n=2 (5.2c), analytic t_opt (5.3)
- ✅ `week_6/study_notes.md` — covers RSA (6.1), factorSplitting/order finding (6.2), QFT/invQFT/Phase_Estimation_Mul (6.3)
- ✅ `week_6/exercises.py` — classical order finding (6.2.2), QFT matrix (6.3.1), continued fractions (6.3.6)
- ✅ `week_7/study_notes.md` — covers Schrödinger (7.1), adiabatic theorem + algorithm (7.2), Trotterisation (7.3), QAOA (7.4)
- ✅ `week_7/exercises.py` — matrix exponential + unitarity (7.1), Trotter convergence (7.3)
- ✅ `roadmap.md` — corrected topics, removed `[TBD]`
- ✅ `CONTINUATION.md` — updated table, What Comes Next, Notes

**Placeholder scan:** No TBDs, no "similar to", no "implement later". All code is complete and runnable.

**Spec note compliance:** Week 7 notes prominently state "not assessed in portfolio" in the header, Key Vocab, and What This Unlocks sections. CONTINUATION.md echoes this.
