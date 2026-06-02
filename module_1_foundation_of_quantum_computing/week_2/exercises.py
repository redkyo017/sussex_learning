# Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits
# Run: python exercises.py
# Requires: numpy

import numpy as np

# ---------------------------------------------------------------------------
# Exercise 2.1: Inner products and norms in ket notation
# Verify orthonormality of |0⟩ and |1⟩, and that |+⟩ is a unit vector.
# ---------------------------------------------------------------------------

print("Exercise 2.1: Inner products and norms")

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)
ket_plus  = np.array([1, 1], dtype=complex) / np.sqrt(2)   # |+⟩
ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)  # |−⟩

def inner(u, v):
    return np.conj(u) @ v   # ⟨u|v⟩ = u†·v

def norm(v):
    return np.sqrt(np.real(inner(v, v)))

assert np.isclose(inner(ket_0, ket_0), 1),  "2.1: ⟨0|0⟩ = 1"
assert np.isclose(inner(ket_1, ket_1), 1),  "2.1: ⟨1|1⟩ = 1"
assert np.isclose(inner(ket_0, ket_1), 0),  "2.1: ⟨0|1⟩ = 0 (orthogonal)"
assert np.isclose(norm(ket_plus),  1.0),    "2.1: |+⟩ is a unit vector"
assert np.isclose(norm(ket_minus), 1.0),    "2.1: |−⟩ is a unit vector"
assert np.isclose(inner(ket_plus, ket_minus), 0), "2.1: |+⟩ and |−⟩ are orthogonal"

print(f"  ⟨0|0⟩ = {inner(ket_0, ket_0).real:.1f}")
print(f"  ⟨0|1⟩ = {inner(ket_0, ket_1).real:.1f}")
print(f"  ‖|+⟩‖ = {norm(ket_plus):.4f}")
print("Exercise 2.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.2: Complex number arithmetic
# Practice conjugates, modulus, and Euler's formula.
# ---------------------------------------------------------------------------

print("Exercise 2.2: Complex numbers")

z1 = 1 + 2j
z2 = 3 - 1j

product = z1 * z2
assert np.isclose(product, (1*3 - 2*(-1)) + (1*(-1) + 2*3)*1j), "2.2: multiplication"
assert np.isclose(abs(z1), np.sqrt(5)),  "2.2: modulus of 1+2i = √5"
assert np.isclose(z1.conjugate(), 1 - 2j), "2.2: conjugate of 1+2i = 1-2i"

# Euler's formula: e^{iπ/2} = i
euler = np.exp(1j * np.pi / 2)
assert np.isclose(euler, 1j), "2.2: e^{iπ/2} = i"

# e^{iπ} = -1  (Euler's identity)
assert np.isclose(np.exp(1j * np.pi), -1), "2.2: e^{iπ} = -1"

print(f"  (1+2i)(3-i) = {product}")
print(f"  |1+2i| = {abs(z1):.4f}")
print(f"  e^{{iπ/2}} = {euler:.4f}")
print("Exercise 2.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.3: Eigenvalues and eigenvectors of Pauli Z and X
# Verify eigenvectors by checking M|v⟩ = λ|v⟩.
# ---------------------------------------------------------------------------

print("Exercise 2.3: Eigenvalues and eigenvectors")

Z = np.array([[1, 0], [0, -1]], dtype=complex)
X = np.array([[0, 1], [1,  0]], dtype=complex)

evals_Z, evecs_Z = np.linalg.eigh(Z)  # eigh for Hermitian matrices (sorted, real evals)
evals_X, evecs_X = np.linalg.eigh(X)

# Z eigenvalues should be {-1, +1}, eigenvectors should be |0⟩ and |1⟩
assert set(np.round(evals_Z).astype(int)) == {-1, 1}, "2.3: Z eigenvalues are ±1"

# X eigenvalues should be {-1, +1}, eigenvectors are |+⟩ and |−⟩
assert set(np.round(evals_X).astype(int)) == {-1, 1}, "2.3: X eigenvalues are ±1"

# Verify M|v⟩ = λ|v⟩ for each (eigenvalue, eigenvector) pair of Z
for i in range(2):
    lam, vec = evals_Z[i], evecs_Z[:, i]
    assert np.allclose(Z @ vec, lam * vec), f"2.3: Z eigenvector {i} check failed"

print(f"  Z eigenvalues: {np.round(evals_Z).astype(int)}")
print(f"  X eigenvalues: {np.round(evals_X).astype(int)}")
print("Exercise 2.3 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 2.4: Single-qubit Bloch sphere state and Born rule
# Construct |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩.
# Verify it is a unit vector and compute Born-rule measurement probabilities.
# ---------------------------------------------------------------------------

print("Exercise 2.4: Bloch sphere states and Born rule")

def bloch_state(theta, phi):
    return np.array([
        np.cos(theta / 2),
        np.exp(1j * phi) * np.sin(theta / 2)
    ], dtype=complex)

# θ=π/2, φ=0 gives |+⟩ = (1/√2)(|0⟩ + |1⟩)
psi_plus = bloch_state(np.pi / 2, 0)
assert np.isclose(norm(psi_plus), 1.0), "2.4: Bloch state must be unit vector"
assert np.isclose(abs(psi_plus[0])**2, 0.5), "2.4: P(0) for |+⟩ = 0.5"
assert np.isclose(abs(psi_plus[1])**2, 0.5), "2.4: P(1) for |+⟩ = 0.5"

# θ=π/3, φ=π/4 — a generic state
psi = bloch_state(np.pi / 3, np.pi / 4)
p0 = abs(psi[0])**2   # Born rule: P(0) = |α|²
p1 = abs(psi[1])**2   # Born rule: P(1) = |β|²
assert np.isclose(p0 + p1, 1.0), "2.4: probabilities must sum to 1"

print(f"  |+⟩ = {np.round(psi_plus, 4)}")
print(f"  P(0) = {p0:.4f}, P(1) = {p1:.4f}, sum = {p0+p1:.4f}")
print("Exercise 2.4 passed.\n")

print("All Week 2 exercises passed.")
