"""Numeric answers stated in content/day09.md (Computing II: speed-ups, noise, error correction).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
"""
import math


def nfs_ln(n_bits):
    """Natural log of the NFS cost exp((64/9)^(1/3) (ln N)^(1/3) (ln ln N)^(2/3))."""
    ln_n = n_bits * math.log(2)
    return (64 / 9) ** (1 / 3) * ln_n ** (1 / 3) * math.log(ln_n) ** (2 / 3)


def order(a, n):
    x, r = a % n, 1
    while x != 1:
        x, r = (x * a) % n, r + 1
    return r


def grover_k(n_items):
    return math.floor(math.pi / (4 * math.asin(1 / math.sqrt(n_items))))


def g_half(f):
    return math.log(0.5) / math.log(f)


def surface(p, p_th=1e-2, target=1e-12, a=0.1):
    """Smallest k=(d+1)/2 with a*(p/p_th)^k <= target; returns (d, 2d^2)."""
    k = 1
    while a * (p / p_th) ** k > target * (1 + 1e-9):
        k += 1
    d = 2 * k - 1
    return d, 2 * d * d


CHECKS = []

# ---------- Core concepts ----------
# M13.1 RSA-1024
CHECKS += [
    ("M13.1 ln N n=1024", 1024 * math.log(2), 709.8, 0.001),
    ("M13.1 ln ln N n=1024", math.log(1024 * math.log(2)), 6.565, 0.001),
    ("M13.1 (64/9)^(1/3)", (64 / 9) ** (1 / 3), 1.923, 0.001),
    ("M13.1 NFS exponent n=1024", nfs_ln(1024), 60.1, 0.005),
    ("M13.1 NFS cost n=1024", math.exp(nfs_ln(1024)), 1.3e26, 0.03),
    ("M13.1 NFS cost n=1024 as log2", nfs_ln(1024) / math.log(2), 87, 0.01),
    ("M13.1 trial division log10 n=1024", 512 * math.log10(2), 154, 0.01),
    ("M13.1 Shor n^3 n=1024", 1024 ** 3, 1.1e9, 0.03),
]

# M13.2 Shor N=21, a=2
r = order(2, 21)
y = pow(2, r // 2, 21)
CHECKS += [
    ("M13.2 order of 2 mod 21", r, 6, 0),
    ("M13.2 2^5 mod 21", pow(2, 5, 21), 11, 0),
    ("M13.2 y = 2^3 mod 21", y, 8, 0),
    ("M13.2 -1 mod 21", 21 - 1, 20, 0),
    ("M13.2 gcd(7,21)", math.gcd(y - 1, 21), 7, 0),
    ("M13.2 gcd(9,21)", math.gcd(y + 1, 21), 3, 0),
]

# M13.3 Grover N=1e6
th = math.asin(1e-3)
k = grover_k(1e6)
CHECKS += [
    ("M13.3 Grover k N=1e6", k, 785, 0),
    ("M13.3 P_785", math.sin((2 * k + 1) * th) ** 2, 1.0, 0.001),
    ("M13.3 classical average N/2", 1e6 / 2, 5e5, 0),
    ("M13.3 ratio 5e5/785", 5e5 / 785, 640, 0.01),
    ("M13.3 P_1570 below 1e-6 (~0)", float(math.sin((2 * 1570 + 1) * th) ** 2 < 1e-6), 1.0, 0),
    ("M13.3 crossover N", ((math.pi / 2) * 1e3) ** 2, 2.5e6, 0.02),
    ("M13.3 classical time N=1e6 (ms)", 5e5 * 1e-9 * 1e3, 0.5, 1e-9),
    ("M13.3 quantum time N=1e6 (ms)", 785 * 1e-6 * 1e3, 0.785, 1e-9),
]

# M13.4 fidelity to depth
CHECKS += [
    ("M13.4 g_half F=0.995", g_half(0.995), 138, 0.005),
    ("M13.4 1-F effective ln F=0.995", -math.log(0.995), 0.00501, 0.002),
    ("M13.4 g_half F=0.999", g_half(0.999), 693, 0.001),
    ("M13.4 g_half F=0.98", g_half(0.98), 34, 0.01),
    ("M13.4 gates until below 0.5 at F=0.90 (ceil)", math.ceil(g_half(0.90)), 7, 0),
]

# M13.5 surface code
d1, q1 = surface(1e-3)
d2, q2 = surface(5e-3)
CHECKS += [
    ("M13.5 d at p=1e-3", d1, 21, 0),
    ("M13.5 phys/logical at p=1e-3", q1, 882, 0),
    ("M13.5 d at p=5e-3", d2, 73, 0),
    ("M13.5 phys/logical at p=5e-3", q2, 1.1e4, 0.04),
]

# M13.6 ZNE clone
CHECKS += [("M13.6 ZNE E(0) = 2E(1)-E(2)", 2 * -1.00 - (-0.90), -1.10, 1e-9)]

# ---------- Exercises ----------
# 9.1 RSA-2048 / 4096
CHECKS += [
    ("9.1 ln N n=2048", 2048 * math.log(2), 1419.6, 0.001),
    ("9.1 ln ln N n=2048", math.log(2048 * math.log(2)), 7.258, 0.001),
    ("9.1 trial division log10 n=2048", 1024 * math.log10(2), 308, 0.01),
    ("9.1 NFS exponent n=2048", nfs_ln(2048), 81.0, 0.002),
    ("9.1 NFS cost n=2048", math.exp(nfs_ln(2048)), 1.5e35, 0.03),
    ("9.1 NFS log2 n=2048", nfs_ln(2048) / math.log(2), 117, 0.005),
    ("9.1 Shor n^3 n=2048", 2048 ** 3, 8.6e9, 0.01),
    ("9.1 ln N n=4096", 4096 * math.log(2), 2839.2, 0.001),
    ("9.1 ln ln N n=4096", math.log(4096 * math.log(2)), 7.951, 0.001),
    ("9.1 NFS exponent n=4096", nfs_ln(4096), 108.5, 0.002),
    ("9.1 NFS cost n=4096", math.exp(nfs_ln(4096)), 1.3e47, 0.02),
    ("9.1 NFS log2 n=4096", nfs_ln(4096) / math.log(2), 156, 0.005),
    ("9.1 NFS growth factor", math.exp(nfs_ln(4096) - nfs_ln(2048)), 8.4e11, 0.01),
    ("9.1 Shor n^3 n=4096", 4096 ** 3, 6.9e10, 0.01),
    ("9.1 Shor growth factor", (4096 / 2048) ** 3, 8, 0),
]

# 9.2 Shor runs
CHECKS += [
    ("9.2a order of 4 mod 21", order(4, 21), 3, 0),
    ("9.2b order of 5 mod 21", order(5, 21), 6, 0),
    ("9.2b 5^3 mod 21", pow(5, 3, 21), 20, 0),
    ("9.2c gcd(2,39)", math.gcd(2, 39), 1, 0),
    ("9.2c order of 2 mod 39", order(2, 39), 12, 0),
    ("9.2c 2^6 mod 39", pow(2, 6, 39), 25, 0),
    ("9.2c -1 mod 39", 39 - 1, 38, 0),
    ("9.2c gcd(24,39)", math.gcd(pow(2, 6, 39) - 1, 39), 3, 0),
    ("9.2c gcd(26,39)", math.gcd(pow(2, 6, 39) + 1, 39), 13, 0),
    ("9.2c product 3*13", 3 * 13, 39, 0),
    ("9.2d gcd(21,21)", math.gcd(21, 21), 21, 0),
    ("9.2d gcd(19,21)", math.gcd(19, 21), 1, 0),
    ("9.2 gcd(4,21)", math.gcd(4, 21), 1, 0),
    ("9.2 gcd(5,21)", math.gcd(5, 21), 1, 0),
]

# 9.3 Grover
CHECKS += [
    ("9.3a k N=1e6", grover_k(1e6), 785, 0),
    ("9.3c sqrt N at crossover", (math.pi / 2) * 1e3, 1571, 0.001),
    ("9.3d k N=2^40", (math.pi / 4) * 2 ** 20, 8.2e5, 0.01),
]

# 9.4 depth
CHECKS += [
    ("9.4a 0.995^138", 0.995 ** 138, 0.501, 0.002),
    ("9.4a 0.995^139", 0.995 ** 139, 0.498, 0.002),
    ("9.4a 1-F effective ln F=0.999", -math.log(0.999), 0.0010005, 0.0001),
    ("9.4b g_half 0.9 unrounded", g_half(0.9), 6.6, 0.01),
    ("9.4c layers at 25 gates/layer", g_half(0.995) / 25, 5.5, 0.01),
    ("9.4d error for 1e4 gates", 1 - 0.5 ** 1e-4, 6.9e-5, 0.01),
    ("9.4 g_half 0.9995 (~1380)", g_half(0.9995), 1380, 0.01),
]

# 9.5 QEC overhead
CHECKS += [
    ("9.5a k at p=1e-3", (d1 + 1) / 2, 11, 0),
    ("9.5b k unrounded at p=5e-3", math.log(1e-11) / math.log(0.5), 36.5, 0.002),
    ("9.5b 73^2", 73 ** 2, 5329, 0),
    ("9.5b phys/logical", q2, 10658, 0),
    ("9.5c physical qubits RSA-2048", 4099 * q1, 3.6e6, 0.01),
    ("9.5c logical qubits 2n+3", 2 * 2048 + 3, 4099, 0),
    ("9.5d ratio to several thousand", 4099 * q1 / 3e3, 1e3, 0.25),
    ("9.5 overhead ratio 5e-3 vs 1e-3", q2 / q1, 12, 0.02),
]

# 9.6 coherence and ZNE
slope = (-0.62 - -0.84) / 2
CHECKS += [
    ("9.6a gate times in T2", 3e-4 / 5e-8, 6000, 0),
    ("9.6b circuit time (us)", 100 * 50e-9 * 1e6, 5, 1e-9),
    ("9.6b coherence factor", math.exp(-5 / 300), 0.98, 0.005),
    ("9.6c 0.995^100", 0.995 ** 100, 0.61, 0.01),
    ("9.6d slope", slope, 0.11, 1e-9),
    ("9.6d E(0)", -0.84 - slope, -0.95, 1e-9),
]

# 9.7 pump scheduling (fact-sheet figures, fictional); baseline arithmetic lives in Day 08 (8.8)
grover_880 = (math.pi / 4) * 2.0 ** 440
age_universe_s = 13.8e9 * 365.25 * 86400
CHECKS += [
    ("9.7 log10 2^880", 880 * math.log10(2), 264.9, 0.001),
    ("9.7 2^880 mantissa (x1e264)", 2.0 ** 880 / 1e264, 8, 0.02),
    ("9.7 Grover iterations (pi/4) 2^440", grover_880, 2e132, 0.12),
    ("9.7 Grover time at 1 us/iteration (s)", grover_880 * 1e-6, 2e126, 0.12),
    ("9.7 seconds since the Big Bang", age_universe_s, 4e17, 0.1),
    ("9.7 g_half 0.995", g_half(0.995), 138, 0.005),
]

# 9.8 RSA migration (fact-sheet figures, fictional)
CHECKS += [
    ("9.8 NFS log2 RSA-2048", nfs_ln(2048) / math.log(2), 117, 0.005),
    ("9.8 logical qubits", 4099, 4100, 0.001),
    ("9.8 phys per logical", q1, 880, 0.005),
    ("9.8 physical qubits", 4099 * q1, 3.6e6, 0.01),
    ("9.8 Shor n^3 ~1e10", 2048 ** 3, 1e10, 0.15),
    ("9.8 x+y", 15 + 5, 20, 0),
    ("9.8 overhead rise at 99.5%", q2 / q1, 12, 0.02),
    ("9.8 AES-256 effective bits under Grover", 256 / 2, 128, 0),
]

# 9.9 board note: >= 50% success over 1e4 steps needs p_L <= ln2/1e4
pl_target = math.log(2) / 1e4
d3, q3 = surface(5e-3, target=pl_target)
d19_pl = 0.1 * 0.5 ** 10  # d = 19 misses the target
CHECKS += [
    ("9.9 success at p_L=1e-4 over 1e4 steps", (1 - 1e-4) ** 1e4, 0.37, 0.01),
    ("9.9 e^-1", math.exp(-1), 0.37, 0.01),
    ("9.9 target p_L ln2/1e4", pl_target, 7e-5, 0.02),
    ("9.9 target p_L 1-0.5^(1e-4)", 1 - 0.5 ** 1e-4, 6.9e-5, 0.01),
    ("9.9 d=19 misses target (flag)", float(d19_pl > pl_target), 1.0, 0),
    ("9.9 d for p_L ln2/1e4 at p=5e-3", d3, 21, 0),
    ("9.9 phys per logical", q3, 880, 0.005),
    ("9.9 logical qubits from 1000", 1000 // q3, 1, 0),
    ("9.9 10000/138", 1e4 / 138, 72, 0.01),
]

# Done when item 2: N = 35, a = 2
CHECKS += [
    ("DW order of 2 mod 35", order(2, 35), 12, 0),
    ("DW 2^6 mod 35", pow(2, 6, 35), 29, 0),
    ("DW gcd(28,35)", math.gcd(28, 35), 7, 0),
    ("DW gcd(30,35)", math.gcd(30, 35), 5, 0),
]

# ---------- Spaced review ----------
CHECKS += [
    ("SR Day06 detection 1-(3/4)^20", 1 - 0.75 ** 20, 0.997, 0.001),
    ("SR Day06 loss 0.2 dB/km x 100 km (dB)", 0.2 * 100, 20, 0),
    ("SR Day06 transmission 20 dB", 10 ** (-20 / 10), 1e-2, 1e-9),
    ("SR Day02 noise 2 pT/rtHz in 100 Hz (pT)", 2 * math.sqrt(100), 20, 1e-9),
    ("SR Day02 shot noise N=1e6", 1 / math.sqrt(1e6), 1e-3, 1e-9),
    ("SR Day02 Heisenberg N=1e6", 1 / 1e6, 1e-6, 1e-9),
    ("SR Day08 Bell amplitude 1/sqrt2", 1 / math.sqrt(2), 0.7071, 0.001),
]
