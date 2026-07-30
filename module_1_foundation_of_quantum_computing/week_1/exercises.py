# Week 1 — Boolean Logic, Reversible Computation, Randomised Computation
# Run: python exercises.py
# Requires: numpy

import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1.1: Binary encoding
# Encode the integers 0–15 as 4-bit strings.
# Verify the encoding of 11 is '1011'.
# ---------------------------------------------------------------------------

def to_binary(n, bits=4):
    return format(n, f'0{bits}b')

print("Exercise 1.1: Binary encoding")
for i in range(16):
    print(f"  {i:2d} → {to_binary(i)}")

assert to_binary(0) == '0000', "1.1a failed"
assert to_binary(11) == '1011', "1.1b failed: 8+2+1=11 → 1011"
assert to_binary(15) == '1111', "1.1c failed"
print("Exercise 1.1 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.2: Truth tables for NOT, AND, OR, XOR
# For all combinations of a,b in {0,1}, compute and verify each operator.
# ---------------------------------------------------------------------------

print("Exercise 1.2: Truth tables")
print(f"  {'a':>2} {'b':>2} | {'NOT a':>5} {'AND':>5} {'OR':>5} {'XOR':>5}")
print("  " + "-" * 34)
for a in [0, 1]:
    for b in [0, 1]:
        not_a = 1 - a
        and_ab = a & b
        or_ab  = a | b
        xor_ab = a ^ b
        print(f"  {a:>2} {b:>2} | {not_a:>5} {and_ab:>5} {or_ab:>5} {xor_ab:>5}")

# Spot-check key values
assert (1 & 0) == 0,  "AND(1,0) should be 0"
assert (1 | 0) == 1,  "OR(1,0) should be 1"
assert (1 ^ 1) == 0,  "XOR(1,1) should be 0 — addition mod 2"
assert (1 ^ 0) == 1,  "XOR(1,0) should be 1"
print("Exercise 1.2 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.3: CNOT gate (reversible computation)
# CNOT maps (x, y) → (x, x XOR y).
# Verify: applying CNOT twice returns to original input.
# ---------------------------------------------------------------------------

print("Exercise 1.3: CNOT gate")

def cnot(x, y):
    return (x, x ^ y)

print(f"  CNOT(0,0) = {cnot(0,0)}")
print(f"  CNOT(0,1) = {cnot(0,1)}")
print(f"  CNOT(1,0) = {cnot(1,0)}")
print(f"  CNOT(1,1) = {cnot(1,1)}")

# CNOT is self-inverse: apply twice = identity
for x in [0, 1]:
    for y in [0, 1]:
        x2, y2 = cnot(*cnot(x, y))
        assert (x2, y2) == (x, y), f"CNOT not self-inverse at ({x},{y})"

print("Exercise 1.3 passed: CNOT is self-inverse.\n")

# ---------------------------------------------------------------------------
# Exercise 1.4: Stochastic matrix and probability vector
# Represent a biased coin (P(H)=0.7, P(T)=0.3) as a probability vector.
# Apply a fair-flip stochastic matrix and verify the result is still valid.
# ---------------------------------------------------------------------------

print("Exercise 1.4: Stochastic matrix")

coin = np.array([0.7, 0.3])   # [P(heads), P(tails)]

# A "fair flip" matrix: regardless of current state, output is 50/50
fair_flip = np.array([[0.5, 0.5],
                      [0.5, 0.5]])

result = fair_flip @ coin
print(f"  Initial coin state: {coin}")
print(f"  After one fair flip: {result}")

# Result must still be a valid probability vector
assert np.isclose(result.sum(), 1.0), "1.4: probabilities must sum to 1"
assert all(result >= 0),              "1.4: probabilities must be non-negative"
assert np.allclose(result, [0.5, 0.5]), "1.4: fair flip should give 50/50"
print("Exercise 1.4 passed.\n")

# ---------------------------------------------------------------------------
# Exercise 1.5: Ket notation for probability vectors
# Write the coin state in ket notation as a NumPy linear combination.
# ---------------------------------------------------------------------------

print("Exercise 1.5: Ket notation")

ket_0 = np.array([1, 0])   # |0⟩ = heads basis vector
ket_1 = np.array([0, 1])   # |1⟩ = tails basis vector

# coin = 0.7|0⟩ + 0.3|1⟩
coin_ket = 0.7 * ket_0 + 0.3 * ket_1
assert np.allclose(coin_ket, coin), "1.5: ket reconstruction should match original"
print(f"  0.7|0⟩ + 0.3|1⟩ = {coin_ket}  ✓")
print("Exercise 1.5 passed.\n")

print("All Week 1 exercises passed.")
