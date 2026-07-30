# Assignment 1 — Study Guide

A plain-English companion to the solutions. Read this after submission to consolidate
what each question was really testing.

---

## Q1 — Gate Composition on 3 Qubits

**What it tests:** Ability to apply a sequence of quantum gates step by step on a multi-qubit state.

**Recipe:**
1. Read the expression right-to-left — the rightmost gate applies first.
2. For each gate, act only on the qubit(s) it targets; leave the rest unchanged.
3. Apply the gate to each term of the superposition individually (linearity).
4. Z rule: `Z|0⟩ = |0⟩`, `Z|1⟩ = −|1⟩` — only flips the sign of `|1⟩`.
5. H rule: `H|0⟩ = (|0⟩+|1⟩)/√2`, `H|1⟩ = (|0⟩−|1⟩)/√2`.
6. CX(control c, target t): flip target iff control = `|1⟩`. Otherwise unchanged.

**Why it works:** Every quantum gate is a linear map — you apply it term by term
to a superposition and collect the results.

**What this circuit actually builds:** After step 3 you get the GHZ state
`(1/√2)(|000⟩ + |111⟩)`. The two Z gates at the end cancel each other's sign
changes on the `|111⟩` term (Z on qubit 1 gives −, Z on qubit 2 gives another −,
and (−1)(−1) = +1), so the final state is the same GHZ state.

**Common mistakes:**
- Applying gates left-to-right instead of right-to-left.
- Forgetting to leave uninvolved qubits unchanged when applying a single-qubit gate.
- Missing the sign flip from Z on `|1⟩`.

---

## Q2 — Hadamard on an Entangled Superposition

**What it tests:** Recognising when a mixture of Bell states simplifies to a product state.

**Recipe:**
1. Expand every Bell state using its definition into the computational basis.
2. Collect like terms — many cancel or double.
3. Factor the result as a product state if possible: `|ψ₁⟩ ⊗ |ψ₂⟩`.
4. Apply H to the target qubit using `H|+⟩ = |0⟩` (H is its own inverse: H² = I).

**Why it works:** The equal superposition `½|Φ+⟩ + ½|Φ−⟩ + ½|Ψ+⟩ + ½|Ψ−⟩`
might look entangled but when you expand it the cross-terms cancel and you're left with
`|0⟩ ⊗ |+⟩` — a completely separable (product) state. Then `H|+⟩ = |0⟩` and you
get `|00⟩`.

**Intuition:** The four Bell states together span the full 2-qubit space equally. Their
equal mixture "washes out" all entanglement — it simplifies as if you reset to a
computational basis state.

**Common mistakes:**
- Trying to apply H directly to each Bell state without simplifying first (much harder).
- Forgetting that H is its own inverse: `H|+⟩ = |0⟩`, not `|+⟩`.

---

## Q3 — Partial Measurement (Computational Basis)

**What it tests:** How measuring one qubit collapses a multi-qubit entangled state.

**Recipe:**
1. Write the 2-qubit state as `Σ aₖ |outcome_qubit1⟩ |state_qubit2⟩`.
2. Discard all terms where qubit 1 ≠ measured outcome.
3. The surviving second-qubit vector (after stripping the first-qubit ket) is the
   unnormalised post-measurement state.
4. Divide by its norm to normalise. The norm² equals the probability of that outcome.

**Why it works:** Measurement is a projection. The Born rule says
`P(outcome) = sum of |amplitude|²` for all terms matching the outcome.
After projection, you renormalise because the remaining state must still be a
unit vector.

**Common mistakes:**
- Forgetting to normalise after projecting.
- Getting confused about which qubit is being measured.

---

## Q4 — Partial Measurement (Hadamard / {+, −} Basis)

**What it tests:** Measuring in a non-computational basis.

**Recipe:**
1. Compute the inner product of the measurement outcome ket with each factor:
   - `⟨−|0⟩ = 1/√2`  (because `|−⟩ = (|0⟩ − |1⟩)/√2`, so `⟨−|0⟩ = 1/√2`)
   - `⟨−|1⟩ = −1/√2`
2. Apply these scalars term by term to the 2-qubit state, acting on qubit 1 only.
3. Collect what remains as an unnormalised qubit-2 state.
4. Normalise.

**Key formula:** Post-measurement state of qubit 2 ∝ `₁⟨outcome|ψ₁₂⟩`

**Why it works:** Measuring in the {+, −} basis is the same as projecting onto those
basis vectors. The algebra is identical to Q3 but with different inner products.

**Common mistakes:**
- Using the *ket* `|−⟩` instead of the *bra* `⟨−|` when projecting.
- Forgetting to conjugate when converting `|−⟩` to `⟨−|` (matters for complex states).

---

## Q5 — Partial Measurement (Y Basis / {+i, −i})

**What it tests:** Measurement with complex-valued basis states; correctly conjugating bras.

**Recipe:**
1. Write the bra by conjugating the ket:
   `|+i⟩ = (|0⟩ + i|1⟩)/√2` → `⟨+i| = (⟨0| − i⟨1|)/√2`
   Note: `i` becomes `−i`.
2. Compute inner products:
   - `⟨+i|0⟩ = 1/√2`
   - `⟨+i|1⟩ = −i/√2`
3. Apply term by term as in Q4.
4. Normalise. Factor out any global phase (`i`, `−1`, `e^{iφ}`, etc.) and discard it.

**Global phase rule:** If the normalised state is `e^{iφ}|ψ⟩` for some real φ,
the physical state is just `|ψ⟩`. Global phases are unobservable.

**Why it works:** The Y-basis `{|+i⟩, |−i⟩}` is the eigenbasis of the Pauli-Y gate.
The maths is the same as Q4; the only new subtlety is careful conjugation of `i`.

**Common mistakes:**
- Writing `⟨+i| = (⟨0| + i⟨1|)/√2` (forgot the conjugation — it must be `−i`).
- Not recognising the global phase: `i|−i⟩` is physically equivalent to `|−i⟩`.

---

## Q6 — Rotation Gate Composition

**What it tests:** 2×2 complex matrix multiplication; carrying global phases through.

**Recipe:**
1. Write out the matrices for `Rz(φ)`, `Ry(θ)`, `Rz(−φ)` explicitly.
2. Multiply right-to-left: first `Ry(θ) · Rz(φ)`, then `Rz(−φ) · (result)`.
3. For each matrix product, multiply row × column.
4. Any scalar factor (like `e^{iθ/2}`) commutes with matrix multiplication — carry it outside.

**Result:** `U(θ,φ) = e^{iθ/2} [[cos(θ/2), −e^{iφ}sin(θ/2)], [e^{−iφ}sin(θ/2), cos(θ/2)]]`

**Why it works:** Sandwiching `Ry(θ)` between `Rz(φ)` and `Rz(−φ)` effectively rotates
the Y-rotation axis by angle φ around the Z-axis. This is a standard decomposition used
in real quantum hardware to implement arbitrary single-qubit gates with just two
native rotation types.

**Why the global phase matters here:** Unlike in state measurement, global phases DO
matter when a gate is used as the target of a controlled gate (Q7) — the phase becomes
a relative phase in the 2-qubit space.

**Common mistakes:**
- Multiplying in the wrong order (left-to-right instead of right-to-left).
- Dropping the global phase `e^{iθ/2}` — it affects the controlled version in Q7.

---

## Q7 — Controlled Gates

**What it tests:** How a single-qubit gate becomes a 2-qubit controlled gate.

**Recipe:**
1. A controlled-V gate has a 2×2 block structure:
   ```
   CV = [ I  0 ]   (as 2×2 blocks of 2×2 matrices)
        [ 0  V ]
   ```
   Top-left: identity (control = |0⟩, do nothing).
   Bottom-right: V (control = |1⟩, apply V to target).
2. Substitute V = U(1,1) from Q6 (θ=1, φ=1 — leave trig unevaluated as instructed).
3. Entries (3,3), (3,4), (4,3), (4,4) of the 4×4 matrix are exactly V's four entries.

**Formal expression:** `CV = |0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ V`

**Why it works:** The projector `|0⟩⟨0|` picks out the part of the state where the
control is |0⟩ and leaves the target alone; `|1⟩⟨1|` picks out the part where the
control is |1⟩ and applies V to the target.

**Common mistakes:**
- Placing V in the top-left block (control = |0⟩ applies V, which is backwards).
- Evaluating `cos(1/2)` or `sin(1/2)` numerically — the question explicitly says not to.

---

## Q8 — Bell Basis Measurement and Probability Distribution

**What it tests:** Computing measurement probabilities when the measurement basis is
not the computational basis.

**Recipe:**
1. Expand the state `|+i, +i⟩` into the computational basis (tensor product).
2. For each Bell state `|Bₖ⟩`, compute `⟨Bₖ|ψ⟩` using the computational-basis expansion.
3. `P(Bₖ) = |⟨Bₖ|ψ⟩|²`. Note: `|i|² = 1`, not `i²`.
4. Verify your probabilities sum to 1.

**Key inner product trick:** Since the Bell states are expressed in the computational
basis, the inner product `⟨Bₖ|ψ⟩` reduces to picking out specific amplitudes:
e.g. `⟨Φ+|ψ⟩ = (1/√2)(amplitude of |00⟩ + amplitude of |11⟩)`.

**Why it works:** The Born rule applies in *any* orthonormal basis — probability of
each outcome = squared modulus of the component of the state along that basis vector.

**Common mistakes:**
- Forgetting the modulus squared: `|i/√2|² = 1/2`, not `i/2` or `−1/2`.
- Sign errors when evaluating `i² = −1` in the expansion of `|+i,+i⟩`.

---

## Q9 — Toffoli Gate and Measurement Probability

**What it tests:** Multi-qubit gate application (CCX) followed by a probability calculation.

**Recipe:**
1. Expand the input `|+,+,0⟩` into computational basis states (tensor product).
2. Apply CCX to each basis state: flip qubit 3 if and only if qubits 1 AND 2 are both |1⟩.
3. Identify which output states have the measured qubit in the desired outcome.
4. Sum the |amplitude|² of those terms.

**CCX truth table:**
- `|0,0,t⟩ → |0,0,t⟩` (no flip)
- `|0,1,t⟩ → |0,1,t⟩` (no flip)
- `|1,0,t⟩ → |1,0,t⟩` (no flip)
- `|1,1,t⟩ → |1,1, t⊕1⟩` (flip! both controls are |1⟩)

**Why it works:** CCX is the quantum AND gate — reversible by design (Toffoli's
contribution was showing any classical computation can be made reversible).
Measurement probability = total squared amplitude of states consistent with the outcome.

**Common mistakes:**
- Flipping qubit 3 when only *one* control qubit is |1⟩ (requires BOTH).
- Summing amplitudes instead of |amplitudes|² — this is the probability, not amplitude.

---

## Q10 — Sequential Conditional Measurement

**What it tests:** Computing conditional probabilities from a quantum state after a
first measurement has already collapsed part of the state.

**Recipe — Method A (conditional probability formula):**
```
P(A | B) = P(A and B) / P(B)
```
Here: `P(first two = |10⟩ | third = |0⟩) = P(|10,0⟩) / P(third = |0⟩) = (1/4) / (3/4) = 1/3`

**Recipe — Method B (post-measurement state):**
1. After measuring third qubit = |0⟩, keep only terms with third qubit = |0⟩.
2. Normalise by dividing by √(probability of that outcome) = √(3/4) = √3/2.
3. In the normalised state, `P(first two = |10⟩) = |amplitude of |10,0⟩|²`.

**Why they give the same answer:** Both methods are equivalent — Method A is the
Bayesian conditional probability formula; Method B is the quantum mechanical state
update rule. They're the same thing expressed differently.

**Why this matters conceptually:** Sequential measurements are not independent.
The first measurement changes the state, which changes the probabilities for the
second measurement. This is a core feature of quantum mechanics with no classical analogue.

**Common mistakes:**
- Reporting `P(|10,0⟩) = 1/4` as the final answer without conditioning on the first outcome.
- Normalising by `P(B)` instead of `√P(B)` — you divide the *state vector* by the norm,
  not the probability.
