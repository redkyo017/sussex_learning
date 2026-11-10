"""Numeric checks for content/companions/week06_companion.md (sections 4-6).
Each tuple: (label, computed, stated, rel_tol)."""
import builtins
from math import pi, sqrt, cos, log, exp, gcd

P = builtins.pow


def order(a, n):
    r = 1
    while P(a, r, n) != 1:
        r += 1
    return r


def powers(a, n, r):
    return [P(a, x, n) for x in range(1, r + 1)]


def dj_amp(f, z, n=2):
    s = 0
    for x in range(2 ** n):
        dot = bin(x & z).count("1") % 2
        s += (-1) ** (f(x) + dot)
    return s / 2 ** n


# x encoded as 2-bit integer with x1 (first qubit) as the high bit
f_c62 = lambda x: 1 ^ (x & 1)   # f(x1x2) = 1 XOR x2

# Shor numbers
r55 = order(2, 55)
h55 = P(2, r55 // 2, 55)
r33a = order(2, 33)
r33b = order(5, 33)
h33b = P(5, r33b // 2, 33)
r15 = order(7, 15)

# Grover / NFS
L2048 = 2048 * log(2)
nfs_log10 = (64 / 9) ** (1 / 3) * L2048 ** (1 / 3) * log(L2048) ** (2 / 3) / log(10)

# Harrowmere C6.4 (fictional): size the RSA-2048 attacker with the 4J heuristic
def surface_d(p, p_th=1e-2, target=1e-12, A=0.1):
    k = 1
    while A * (p / p_th) ** k > target * (1 + 1e-9):
        k += 1
    return 2 * k - 1

logical = 2 * 2048 + 3
d64 = surface_d(2e-3)
ppl64 = 2 * d64 ** 2 - 1
phys64 = logical * ppl64
d999 = surface_d(1e-3)

CHECKS = [
    # 4A Bloch
    ("4A P(0) theta=pi/3", cos(pi / 6) ** 2, 0.75, 0.001),
    # 4C Bell
    ("4C Bell amplitude", 1 / sqrt(2), 0.707, 0.001),
    ("4C Bell probability", (1 / sqrt(2)) ** 2, 0.5, 0.001),
    # 4E DJ classical queries and randomised error
    ("4E queries n=2", 2 ** 1 + 1, 3, 0),
    ("4E queries n=3", 2 ** 2 + 1, 5, 0),
    ("4E queries n=10", 2 ** 9 + 1, 513, 0),
    ("4E randomised error k=10", 2 * 2 ** -10, 0.002, 0.03),
    # 4F Grover
    ("4F Grover iterations N=1e8", pi / 4 * sqrt(1e8), 7854, 0.001),
    ("4F classical average N=1e8", 1e8 / 2, 5e7, 0),
    # 4G teleportation bits
    ("4G classical bits (4 outcomes)", log(4, 2), 2, 1e-9),
    # 4H Shor examples
    ("4H N=15 a=7 order", r15, 4, 0),
    ("4H 7^2 mod 15", P(7, 2, 15), 4, 0),
    ("4H gcd(3,15)", gcd(3, 15), 3, 0),
    ("4H gcd(5,15)", gcd(5, 15), 5, 0),
    ("4H NFS 2048-bit log10 ops", nfs_log10, 35, 0.02),
    ("4H 2048^3", 2048 ** 3, 8.6e9, 0.01),
    ("4H 2^2048 ~ 10^617 (log10)", 2048 * log(2, 10), 617, 0.002),
    # 4I fidelity -> depth
    ("4I 0.995^100", 0.995 ** 100, 0.61, 0.01),
    ("4I 0.98^100", 0.98 ** 100, 0.13, 0.03),
    ("4I 0.9^100", 0.9 ** 100, 2.7e-5, 0.02),
    ("4I g_half F=0.995", log(0.5) / log(0.995), 138, 0.01),
    ("4I g_half F=0.98", log(0.5) / log(0.98), 34, 0.02),
    ("4I g_half F=0.9", log(0.5) / log(0.9), 6.6, 0.01),
    ("4I 1/(1-F) 0.995", 1 / (1 - 0.995), 200, 0.001),
    ("4I 1/(1-F) 0.98", 1 / (1 - 0.98), 50, 0.001),
    ("4I 1/(1-F) 0.9", 1 / (1 - 0.9), 10, 0.001),
    # 4J surface code
    ("4J d=3 factor", 0.1 ** ((3 + 1) / 2), 1e-2, 1e-9),
    ("4J d=7 factor", 0.1 ** ((7 + 1) / 2), 1e-4, 1e-9),
    ("4J 2d^2-1 at d=7", 2 * 7 ** 2 - 1, 97, 0),
    # C6.1 Shor N=55, a=2
    ("C6.1 gcd(2,55)", gcd(2, 55), 1, 0),
    ("C6.1 order of 2 mod 55", r55, 20, 0),
    ("C6.1 powers list match", float(powers(2, 55, 20) == [2, 4, 8, 16, 32, 9, 18, 36, 17, 34, 13, 26, 52, 49, 43, 31, 7, 14, 28, 1]), 1, 0),
    ("C6.1 2^10 = 1024", 2 ** 10, 1024, 0),
    ("C6.1 1024 = 18*55 + 34", 18 * 55 + 34, 1024, 0),
    ("C6.1 2^10 mod 55", h55, 34, 0),
    ("C6.1 -1 mod 55", 55 - 1, 54, 0),
    ("C6.1 34 != 54 (test passes)", float(h55 != 54), 1, 0),
    ("C6.1 gcd(33,55)", gcd(h55 - 1, 55), 11, 0),
    ("C6.1 gcd(35,55)", gcd(h55 + 1, 55), 5, 0),
    ("C6.1 gcd(1023,55)", gcd(1023, 55), 11, 0),
    ("C6.1 gcd(1025,55)", gcd(1025, 55), 5, 0),
    ("C6.1 phi(55)", 4 * 10, 40, 0),
    ("C6.1 r divides phi", 40 % r55, 0, 0),
    # C6.2 DJ f = 1 XOR x2
    ("C6.2 truth table 1,0,1,0", float([f_c62(x) for x in range(4)] == [1, 0, 1, 0]), 1, 0),
    ("C6.2 balanced: count of ones", sum(f_c62(x) for x in range(4)), 2, 0),
    ("C6.2 A00", dj_amp(f_c62, 0b00), 0, 1e-9),
    ("C6.2 A01", dj_amp(f_c62, 0b01), -1, 1e-9),
    ("C6.2 A10", dj_amp(f_c62, 0b10), 0, 1e-9),
    ("C6.2 A11", dj_amp(f_c62, 0b11), 0, 1e-9),
    ("C6.2 sum |A|^2", sum(dj_amp(f_c62, z) ** 2 for z in range(4)), 1, 1e-9),
    ("C6.2 classical queries", 2 ** 1 + 1, 3, 0),
    # C6.3 depth from fidelity (fictional device)
    ("C6.3 g_half F=0.998", log(0.5) / log(0.998), 346.2, 0.001),
    ("C6.3 0.998^346", 0.998 ** 346, 0.500, 0.002),
    ("C6.3 1/(1-F)", 1 / (1 - 0.998), 500, 0.001),
    ("C6.3 0.998^500", 0.998 ** 500, 0.37, 0.01),
    ("C6.3 0.998^2000", 0.998 ** 2000, 0.018, 0.02),
    ("C6.3 e^-4", exp(-4), 0.018, 0.02),
    ("C6.3 required F", 0.5 ** (1 / 2000), 0.99965, 1e-5),
    ("C6.3 required error", 1 - 0.5 ** (1 / 2000), 3.5e-4, 0.02),
    ("C6.3 error ratio", 2e-3 / (1 - 0.5 ** (1 / 2000)), 6, 0.06),
    # C6.4 Harrowmere RSA-2048 attacker (fictional device at 99.8%)
    ("C6.4 NFS 2048-bit log10 ops", nfs_log10, 35, 0.02),
    ("C6.4 Shor 2048^3 ~1e10", 2048 ** 3, 1e10, 0.15),
    ("C6.4 logical qubits 2n+3", logical, 4099, 0),
    ("C6.4 p/p_th at 99.8%", 2e-3 / 1e-2, 0.2, 1e-9),
    ("C6.4 total failure 1e10 x 1e-12", 1e10 * 1e-12, 0.01, 1e-9),
    ("C6.4 distance at 99.8%", d64, 31, 0),
    ("C6.4 phys per logical 2d^2-1", ppl64, 1921, 0),
    ("C6.4 physical qubits", phys64, 7.9e6, 0.01),
    ("C6.4 ratio to several thousand (8000)", phys64 / 8000, 1000, 0.03),
    ("C6.4 Mosca x+y", 15 + 5, 20, 0),
    ("C6.4 99.9% comparison: phys per logical", 2 * d999 ** 2 - 1, 880, 0.002),
    # C6.5 cold attempt N=33
    ("C6.5 order of 2 mod 33", r33a, 10, 0),
    ("C6.5 2^5 mod 33 (= -1)", P(2, 5, 33), 32, 0),
    ("C6.5 trivial gcd(31,33)", gcd(31, 33), 1, 0),
    ("C6.5 trivial gcd(33,33)", gcd(33, 33), 33, 0),
    ("C6.5 powers of 2 match", float(powers(2, 33, 10) == [2, 4, 8, 16, 32, 31, 29, 25, 17, 1]), 1, 0),
    ("C6.5 order of 5 mod 33", r33b, 10, 0),
    ("C6.5 powers of 5 match", float(powers(5, 33, 10) == [5, 25, 26, 31, 23, 16, 14, 4, 20, 1]), 1, 0),
    ("C6.5 5^5 mod 33", h33b, 23, 0),
    ("C6.5 gcd(22,33)", gcd(h33b - 1, 33), 11, 0),
    ("C6.5 gcd(24,33)", gcd(h33b + 1, 33), 3, 0),
    ("C6.5 phi(33)", 2 * 10, 20, 0),
]
