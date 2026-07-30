# Week 7 — Hamiltonians, Adiabatic Algorithm, Trotterisation, and QAOA
# Run: python exercises.py
# Requires: numpy, scipy
# NOTE: Week 7 topics are NOT assessed in the portfolio (per course PDF).

import numpy as np
from scipy.linalg import expm
from numpy.linalg import matrix_power

I2    = np.eye(2, dtype=complex)
X     = np.array([[0, 1], [1, 0]], dtype=complex)
Z     = np.array([[1, 0], [0, -1]], dtype=complex)
ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 7.1: Matrix exponential for time evolution under H = Z
# ---------------------------------------------------------------------------
print("Exercise 7.1: Matrix exponential for time evolution")

# Hamiltonian: H = Z (Pauli-Z), eigenvalues ±1
# Time: t = π/4
# U(t) = e^{−iHt} = e^{−iZt}
H_z = Z
t = np.pi / 4

U = expm(-1j * H_z * t)

# 1. Unitarity: U†U = I
UdagU = U.conj().T @ U
assert np.allclose(UdagU, I2), "7.1: U†U should equal I"

# 2. Action on |0⟩: eigenstate with eigenvalue +1, so U|0⟩ = e^{-it}|0⟩
expected_0 = np.exp(-1j * t) * ket_0
assert np.allclose(U @ ket_0, expected_0), "7.1: U|0⟩ should equal e^{-it}|0⟩"

# 3. Action on |1⟩: eigenstate with eigenvalue -1, so U|1⟩ = e^{+it}|1⟩
expected_1 = np.exp(1j * t) * ket_1
assert np.allclose(U @ ket_1, expected_1), "7.1: U|1⟩ should equal e^{+it}|1⟩"

# 4. Norm preservation: |U|ψ⟩| = 1 for any normalised |ψ⟩
psi = (ket_0 + ket_1) / np.sqrt(2)
assert np.isclose(np.linalg.norm(U @ psi), 1.0), "7.1: norm should be preserved"

print(f"  H = Z,  t = π/4")
print(f"  U = e^{{-iZt}}:")
print(f"    {np.round(U[0], 4)}")
print(f"    {np.round(U[1], 4)}")
print(f"  U†U = I: ✓")
print(f"  U|0⟩ = e^{{-it}}|0⟩: ✓   U|1⟩ = e^{{+it}}|1⟩: ✓")
print("Exercise 7.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 7.2: Trotterisation — (e^{-iH_A t/N} e^{-iH_B t/N})^N → e^{-i(H_A+H_B)t}
# as N increases, for non-commuting H_A and H_B.
# ---------------------------------------------------------------------------
print("Exercise 7.2: Trotterisation approximation")

# H_A = X,  H_B = Z  (single-qubit, non-commuting: [X,Z] != 0)
H_A = X
H_B = Z
H_total = H_A + H_B

t = 1.0   # evolution time

# Exact: e^{-i(H_A+H_B)t}
U_exact = expm(-1j * H_total * t)

# Trotterised approximation for increasing N
errors = []
N_values = [1, 2, 5, 20, 100]

for N in N_values:
    step = expm(-1j * H_A * t / N) @ expm(-1j * H_B * t / N)
    U_trotter = matrix_power(step, N)
    # Frobenius norm of difference
    error = np.linalg.norm(U_trotter - U_exact, 'fro')
    errors.append(error)
    print(f"  N={N:4d}: Trotter error = {error:.6f}")

# Errors must be monotonically decreasing as N increases
for i in range(len(errors) - 1):
    assert errors[i + 1] < errors[i], \
        f"7.2: error should decrease with N: errors[{i+1}]={errors[i+1]:.6f} >= errors[{i}]={errors[i]:.6f}"

# For large N=100 the error should be very small
assert errors[-1] < 0.01, f"7.2: Trotter error for N=100 should be < 0.01, got {errors[-1]:.6f}"

print("Exercise 7.2 passed.\n")

print("All Week 7 exercises passed.")
