# Week 3 — Single-Qubit Gates, Bloch Sphere, Multi-Qubit Systems
# Run: python exercises.py
# Requires: numpy

import numpy as np

# Standard gates (defined once, used throughout)
I    = np.eye(2, dtype=complex)
X    = np.array([[0, 1], [1,  0]], dtype=complex)
Y    = np.array([[0,-1j],[1j, 0]], dtype=complex)
Z    = np.array([[1, 0], [0, -1]], dtype=complex)
H    = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CNOT = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,0,1],
                 [0,0,1,0]], dtype=complex)

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 3.1: Verify standard gates are unitary (U†U = I)
# ---------------------------------------------------------------------------

print("Exercise 3.1: Unitarity check")

def is_unitary(U, tol=1e-10):
    return np.allclose(U.conj().T @ U, np.eye(len(U)), atol=tol)

for name, gate in [('X', X), ('Y', Y), ('Z', Z), ('H', H)]:
    result = is_unitary(gate)
    print(f"  {name} unitary: {result}")
    assert result, f"3.1: {name} must be unitary"

print("Exercise 3.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.2: Hadamard maps |0⟩ → |+⟩ and |1⟩ → |−⟩
# ---------------------------------------------------------------------------

print("Exercise 3.2: Hadamard action")

ket_plus  = np.array([1,  1], dtype=complex) / np.sqrt(2)
ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)

assert np.allclose(H @ ket_0, ket_plus),  "3.2: H|0⟩ = |+⟩"
assert np.allclose(H @ ket_1, ket_minus), "3.2: H|1⟩ = |−⟩"
# H is self-inverse: H² = I
assert np.allclose(H @ H, I), "3.2: H² = I"

print(f"  H|0⟩ = {np.round(H @ ket_0, 4)}")
print(f"  H|1⟩ = {np.round(H @ ket_1, 4)}")
print("Exercise 3.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.3: Tensor products for 2-qubit basis states
# ---------------------------------------------------------------------------

print("Exercise 3.3: Tensor products")

ket_00 = np.kron(ket_0, ket_0)
ket_01 = np.kron(ket_0, ket_1)
ket_10 = np.kron(ket_1, ket_0)
ket_11 = np.kron(ket_1, ket_1)

# Standard basis vectors in ℂ⁴
assert np.allclose(ket_00, [1,0,0,0]), "3.3: |00⟩ = [1,0,0,0]"
assert np.allclose(ket_01, [0,1,0,0]), "3.3: |01⟩ = [0,1,0,0]"
assert np.allclose(ket_10, [0,0,1,0]), "3.3: |10⟩ = [0,0,1,0]"
assert np.allclose(ket_11, [0,0,0,1]), "3.3: |11⟩ = [0,0,0,1]"

print(f"  |00⟩ = {ket_00}")
print(f"  |11⟩ = {ket_11}")
print("Exercise 3.3 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.4: Construct Bell state |Φ+⟩ via H⊗I then CNOT
# ---------------------------------------------------------------------------

print("Exercise 3.4: Bell state |Φ+⟩")

H_kron_I = np.kron(H, I)
state = H_kron_I @ ket_00        # |+⟩|0⟩ = (1/√2)(|00⟩ + |10⟩)
bell_plus = CNOT @ state          # (1/√2)(|00⟩ + |11⟩)

expected_bell = (ket_00 + ket_11) / np.sqrt(2)
assert np.allclose(bell_plus, expected_bell), "3.4: Bell state construction failed"

# Verify norm is 1
assert np.isclose(np.linalg.norm(bell_plus), 1.0), "3.4: Bell state must have norm 1"

print(f"  |Φ+⟩ = {np.round(bell_plus, 4)}")
print("Exercise 3.4 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 3.5: Verify |Φ+⟩ is entangled (cannot be written as product state)
# Show that no (a,b,c,d) satisfies (a|0⟩+b|1⟩)⊗(c|0⟩+d|1⟩) = |Φ+⟩
# by checking the separability condition: (ac)(bd) = (ad)(bc)
# For |Φ+⟩ = [1/√2, 0, 0, 1/√2]: ac=1/√2, ad=0, bc=0, bd=1/√2
# (ac)(bd) = 1/2 but (ad)(bc) = 0 → entangled
# ---------------------------------------------------------------------------

print("Exercise 3.5: Entanglement check")

b_state = bell_plus
ac = b_state[0]  # coefficient of |00⟩
ad = b_state[1]  # coefficient of |01⟩
bc = b_state[2]  # coefficient of |10⟩
bd = b_state[3]  # coefficient of |11⟩

# Separability condition: ac * bd == ad * bc
separable = np.isclose(ac * bd, ad * bc)
assert not separable, "3.5: |Φ+⟩ must NOT be separable"
print(f"  ac·bd = {ac*bd:.4f}, ad·bc = {ad*bc:.4f} → entangled: {not separable}")
print("Exercise 3.5 passed.\n")

print("All Week 3 exercises passed.")
