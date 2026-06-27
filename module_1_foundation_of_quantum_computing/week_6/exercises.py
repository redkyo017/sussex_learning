# Week 6 — Shor's Algorithm: RSA, Order Finding, and the Quantum Fourier Transform
# Run: python exercises.py
# Requires: numpy, fractions (standard library)

import numpy as np
from fractions import Fraction

# ---------------------------------------------------------------------------
# Exercise 6.1: Modular arithmetic and order finding (classical)
# ---------------------------------------------------------------------------
print("Exercise 6.1: Modular arithmetic and order finding")

def find_order(a, N):
    """Find the smallest t > 0 such that a^t ≡ 1 (mod N)."""
    if a <= 0 or N <= 1:
        raise ValueError("Requires a > 0 and N > 1")
    val = a % N
    for t in range(1, N):
        if val == 1:
            return t
        val = (val * a) % N
    raise ValueError(f"No order found for a={a}, N={N}")

# Test cases: (a, N, expected_order)
test_cases = [
    (2, 15, 4),
    (3, 11, 5),
    (7, 15, 4),
    (2, 21, 6),
]

for a, N, expected in test_cases:
    t = find_order(a, N)
    assert t == expected, f"6.1: find_order({a}, {N}) = {t}, expected {expected}"
    # Verify the order: a^t ≡ 1 (mod N)
    assert pow(a, t, N) == 1, f"6.1: {a}^{t} mod {N} should be 1"
    # Verify it's minimal: a^(t-1) ≢ 1 (mod N) for t > 1
    if t > 1:
        assert pow(a, t - 1, N) != 1, f"6.1: {a}^{t-1} mod {N} should not be 1"
    print(f"  ord_{N}({a}) = {t}  (verified: {a}^{t} mod {N} = {pow(a, t, N)})")

print("Exercise 6.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 6.2: Quantum Fourier Transform matrix on 3 qubits (F_8)
# ---------------------------------------------------------------------------
print("Exercise 6.2: QFT matrix on 3 qubits (F_8)")

def qft_matrix(n):
    """
    Build the QFT matrix on n qubits (dimension N=2^n).
    F_{j,k} = omega^(j*k) / sqrt(N), where omega = exp(2*pi*i / N).
    """
    N = 2**n
    omega = np.exp(2j * np.pi / N)
    j = np.arange(N).reshape(N, 1)
    k = np.arange(N).reshape(1, N)
    F = omega**(j * k) / np.sqrt(N)
    return F

F = qft_matrix(3)   # 8×8 matrix

# Unitarity: F†F = I
FdagF = F.conj().T @ F
assert np.allclose(FdagF, np.eye(8)), "6.2: F†F should equal the identity"

# F applied to |0⟩ should give uniform superposition
ket_0_8 = np.zeros(8, dtype=complex)
ket_0_8[0] = 1.0
F_ket0 = F @ ket_0_8
assert np.allclose(np.abs(F_ket0), 1 / np.sqrt(8)), "6.2: F|0⟩ should have uniform amplitudes"

# F applied to |1⟩: entries should be omega^j / sqrt(8)
ket_1_8 = np.zeros(8, dtype=complex)
ket_1_8[1] = 1.0
F_ket1 = F @ ket_1_8
omega8 = np.exp(2j * np.pi / 8)
expected_F_ket1 = np.array([omega8**j for j in range(8)]) / np.sqrt(8)
assert np.allclose(F_ket1, expected_F_ket1), "6.2: F|1⟩ entries should match omega^j/sqrt(8)"

print(f"  F_8 shape: {F.shape}")
print(f"  F†F = I: ✓")
print(f"  F|0⟩ uniform: ✓  (amplitudes = {np.round(np.abs(F_ket0[0]), 4)} each)")
print(f"  F|1⟩ correct: ✓")
print("Exercise 6.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 6.3: Continued fractions to recover the period t from a sample h/t
# ---------------------------------------------------------------------------
print("Exercise 6.3: Continued fractions for period recovery")

def extract_period(x_float, max_denominator=64):
    """
    Given a float x ≈ h/t (the phase estimation output), recover t via
    continued fractions (best rational approximation).
    Returns the denominator of the best approximation.
    """
    frac = Fraction(x_float).limit_denominator(max_denominator)
    return frac.denominator

# t=4 (order of 2 mod 15): sample h/t for h=1,2,3
# t=5 (order of 3 mod 11): sample h/t for h=1,2,3,4
test_cases = [
    # (t_true, h values to test)
    (4, [1, 2, 3]),
    (5, [1, 2, 3, 4]),
]

for t_true, h_values in test_cases:
    for h in h_values:
        x = h / t_true
        t_rec = extract_period(x)
        # t_true must be a multiple of t_rec (since gcd(h,t) might reduce the fraction)
        assert t_true % t_rec == 0, \
            f"6.3: t={t_true}, h={h}: recovered {t_rec}, but {t_true} % {t_rec} = {t_true % t_rec}"
        print(f"  x = {h}/{t_true} = {x:.6f}  →  extracted denominator {t_rec}  (t_true={t_true}, t_true%t_rec={t_true%t_rec})")

print("Exercise 6.3 passed.\n")

print("All Week 6 exercises passed.")
