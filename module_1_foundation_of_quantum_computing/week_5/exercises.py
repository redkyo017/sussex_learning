# Week 5 — Grover's Algorithm and Amplitude Amplification
# Run: python exercises.py
# Requires: numpy

import numpy as np

# Standard gates
I    = np.eye(2, dtype=complex)
X    = np.array([[0, 1], [1,  0]], dtype=complex)
H    = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

# ---------------------------------------------------------------------------
# Exercise 5.1: Oracle phase kick (n=2, marked state |11⟩ = index 3)
# Construct the 2-qubit phase oracle that flips the sign of the marked state.
# ---------------------------------------------------------------------------

print("Exercise 5.1: Oracle phase kick")

n = 2
N = 2**n  # = 4

# Uniform superposition: |u⟩ = H^⊗2 |00⟩
H2 = np.kron(H, H)
ket_00 = np.array([1, 0, 0, 0], dtype=complex)
u = H2 @ ket_00  # uniform superposition

# Phase oracle: flip sign of component at index 3 (|11⟩)
oracle = np.eye(N, dtype=complex)
marked = 3  # |11⟩
oracle[marked, marked] = -1

# Apply oracle to |u⟩
after_oracle = oracle @ u

# The marked component should have flipped sign
assert np.isclose(after_oracle[marked], -u[marked]), "5.1: marked amplitude should be negated"
# Unmarked components unchanged
for i in range(N):
    if i != marked:
        assert np.isclose(after_oracle[i], u[i]), f"5.1: unmarked amplitude {i} should be unchanged"

print(f"  Before oracle: {np.round(u, 4)}")
print(f"  After oracle:  {np.round(after_oracle, 4)}")
print("Exercise 5.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 5.2: Grover iterator (n=2, marked state index 3)
# One full Grover step G = D·Oracle where D = 2|u⟩⟨u| − I.
# After t=1 step the marked state is amplified; after t=2 it over-rotates.
# ---------------------------------------------------------------------------

print("Exercise 5.2: Grover iterator simulation")

n = 2
N = 2**n  # = 4, t_opt = floor(pi/(4*arcsin(1/2))) = 1

H2 = np.kron(H, H)
ket_00_4 = np.array([1, 0, 0, 0], dtype=complex)
u = H2 @ ket_00_4

# Phase oracle: mark index 3 (|11⟩)
oracle = np.eye(N, dtype=complex)
oracle[3, 3] = -1

# Diffusion operator: D = 2|u⟩⟨u| − I
D = 2 * np.outer(u, np.conj(u)) - np.eye(N, dtype=complex)

# Grover iterator: G = D · oracle
G = D @ oracle

# Apply t=1 step
state_1 = G @ u
prob_1 = np.abs(state_1[3])**2

# Apply t=2 steps (over-rotation)
state_2 = G @ state_1
prob_2 = np.abs(state_2[3])**2

# After 1 step: probability of marked state is 1.0 (perfect for n=2)
assert np.isclose(prob_1, 1.0, atol=1e-10), f"5.2: prob after 1 step should be 1.0, got {prob_1:.6f}"
# After 2 steps: over-rotated, probability drops
assert prob_2 < prob_1, f"5.2: over-rotation should reduce probability"

print(f"  t=1 step: P(|11⟩) = {prob_1:.4f}")
print(f"  t=2 steps (over-rotation): P(|11⟩) = {prob_2:.4f}")
print("Exercise 5.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 5.3: Optimal iteration count for multiple n
# For each n, compute t_opt = floor(π/(4θ)) where sin(θ) = 1/√(2ⁿ),
# simulate Grover's algorithm, and verify success probability exceeds 0.9.
# ---------------------------------------------------------------------------

print("Exercise 5.3: Optimal iteration count")

def grover_optimal(n):
    """
    Simulate Grover's algorithm for n qubits with marked state at index 0.
    Returns the success probability after t_opt iterations.
    """
    N = 2**n
    theta = np.arcsin(1 / np.sqrt(N))
    t_opt = int(np.floor(np.pi / (4 * theta)))

    # Build system: H^⊗n on |0^n⟩
    Hn = np.array([[1]], dtype=complex)
    for _ in range(n):
        Hn = np.kron(Hn, H)
    ket_zero_n = np.zeros(N, dtype=complex)
    ket_zero_n[0] = 1.0
    u = Hn @ ket_zero_n

    # Phase oracle: mark index 0
    oracle = np.eye(N, dtype=complex)
    oracle[0, 0] = -1

    # Diffusion operator: D = 2|u⟩⟨u| − I
    D = 2 * np.outer(u, np.conj(u)) - np.eye(N, dtype=complex)

    # Grover iterator
    G = D @ oracle

    # Apply t_opt steps
    state = u.copy()
    for _ in range(t_opt):
        state = G @ state

    prob = np.abs(state[0])**2
    return prob, t_opt

for n in [2, 3, 4, 6]:
    prob, t_opt = grover_optimal(n)
    assert prob > 0.9, f"5.3: n={n}: success prob {prob:.4f} should exceed 0.9 (t_opt={t_opt})"
    print(f"  n={n}: t_opt={t_opt}, P(success)={prob:.4f}")

print("Exercise 5.3 passed.\n")

print("All Week 5 exercises passed.")
