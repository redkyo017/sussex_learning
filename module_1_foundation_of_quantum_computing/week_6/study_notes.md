# Week 6 — Shor's Algorithm: RSA, Order Finding, and the Quantum Fourier Transform

**PDF:** Foundations of Quantum Computing — Week 6 Study
**Sections:** 6.1 RSA cryptosystem · 6.2 Factorisation and order finding · 6.3 Order finding via phase estimation

> **Portfolio note:** The Week 6 PDF states: "This is by far the most technical Study material encountered so far. You are not expected to remember it in fine detail."

---

## Core Topics

### 6.1 RSA Cryptosystem

**Public/private key structure:**
- Public key: (N, e) where N = p·q (product of two large primes), e coprime to (p−1)(q−1)
- Private key: d such that e·d ≡ 1 (mod (p−1)(q−1))
- Encryption: c = mᵉ mod N; Decryption: m = c^d mod N
- Security assumption: factoring N into p and q is computationally hard classically
- Shor's algorithm breaks RSA by efficiently factoring N

### 6.2 Factorisation and Order Finding

**Number theory background:**
- gcd and Euclid's algorithm
- If u² ≡ 1 (mod N) and u ≢ ±1 (mod N), then gcd(u−1, N) gives a non-trivial factor of N (the factorSplitting claim)
- This reduces factoring to finding u

**Order finding:**
- For a coprime to N, the order of a mod N is the smallest t > 0 such that aᵗ ≡ 1 (mod N)
- Choose random a coprime to N; find t = ord_N(a); compute u = a^{t/2} mod N
- Reduction: if t is even and a^{t/2} ≢ −1 (mod N), then u² ≡ 1 (mod N) with u ≢ ±1 (mod N) — apply factorSplitting

### 6.3 Order Finding via Phase Estimation

**QFT structure:**
- QFT on n qubits (N=2ⁿ): unitary matrix F_{2ⁿ} with entries (F)_{j,k} = ω^{jk}/√N where ω = e^{2πi/2ⁿ}
- Rows of F are the eigenstates |f_{ωᵏ}⟩ of the shift operator
- Inverse QFT reverses the transformation: `invQFT[n]`

**Phase estimation approach:**
- Modular multiplication unitary U_a: |x⟩ ↦ |ax mod N⟩
- Eigenvalues of U_a are roots of unity ω^k where t is the order of a
- Phase estimation on U_a samples x ≈ h/t for random h
- Apply inverse QFT to estimate x, then use continued fractions to recover t from h/t
- Combined quantum subroutine: `Phase_Estimation_Mul[n]`

**Input preparation:**
- Starting with |1⟩ gives a uniform mix of all eigenstates of U_a — no need to prepare individual eigenstates

---

## Key Vocab

| Term | Meaning |
|------|---------|
| RSA | Public-key cryptosystem whose security rests on the hardness of integer factorisation |
| Public key | The pair (N, e) broadcast openly; used to encrypt messages |
| Private key | The exponent d satisfying e·d ≡ 1 (mod (p−1)(q−1)); used to decrypt |
| Coprime | Two integers whose gcd equals 1; a must be coprime to N for order finding |
| Modular arithmetic | Arithmetic modulo N; aᵗ mod N cycles with period t (the order) |
| Order | Smallest positive t such that aᵗ ≡ 1 (mod N); the key quantity Shor's algorithm finds |
| factorSplitting | If u² ≡ 1 (mod N) and u ≢ ±1 (mod N), then gcd(u−1, N) is a non-trivial factor |
| QFT (Quantum Fourier Transform) | Unitary F_{2ⁿ} mapping computational basis to Fourier basis; analogue of the DFT |
| Inverse QFT | The adjoint of QFT; used to read out phase information after phase estimation |
| Continued fractions | Classical algorithm to extract a rational p/q from a decimal approximation |
| Modular exponentiation | Computing aˣ mod N efficiently; implemented as the unitary U_a in Shor's circuit |
| Phase estimation | Quantum subroutine that estimates the eigenphase of a unitary; core of Shor's algorithm |
| Roots of unity | Complex numbers ω^k with ω = e^{2πi/t}; the eigenvalues of U_a |

---

## What This Unlocks

- Post-quantum cryptography is motivated by Shor's algorithm — most of quantum-resistant cryptography is built to defend against it
- Understanding phase estimation here connects to Week 4's phase estimation (same subroutine, different unitary)
- QFT is a fundamental building block beyond factoring (quantum signal processing, chemistry simulations)

---

## Common Confusion Points

**"Why does starting with |1⟩ work for phase estimation?"**
Because |1⟩ can be written as a uniform superposition of all eigenstates of U_a, so the QFT samples from them uniformly — no eigenstate preparation required.

**"Why does order finding give a factor?"**
Via the factorSplitting claim: u² ≡ 1 (mod N) with u ≢ ±1 means (u−1)(u+1) ≡ 0 mod N, but neither factor is 0 mod N, so gcd reveals the prime factor.

**"What does the QFT matrix do geometrically?"**
It transforms between the computational basis and the Fourier basis (eigenstates of the shift operator), analogous to DFT but on quantum amplitudes.

---

## Prerequisite Links

- Week 4: Phase estimation is the quantum subroutine at the heart of Shor's algorithm (`../week_4/study_notes.md`)
- Week 5: Oracle model and quantum speedup framework — Shor is another quadratic-to-polynomial speedup (`../week_5/study_notes.md`)
