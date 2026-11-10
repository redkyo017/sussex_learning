"""Numeric answers stated in content/day08.md (Quantum computing I: circuits, interference, Deutsch-Jozsa).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
State vectors are computed with plain complex lists (stdlib only); basis order |00>,|01>,|10>,|11>,
first qubit = left bit.
"""
import cmath
import math

r2 = 1 / math.sqrt(2)
I2 = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Z = [[1, 0], [0, -1]]
Y = [[0, -1j], [1j, 0]]
H = [[r2, r2], [r2, -r2]]
CNOT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(len(v))) for i in range(len(a))]


def kron(a, b):
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def kron_n(m, n):
    out = [[1]]
    for _ in range(n):
        out = kron(out, m)
    return out


def maxdiff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def bits(x, n):
    return [(x >> (n - 1 - i)) & 1 for i in range(n)]


def dj(f, n, ancilla_one=True):
    """Full Deutsch-Jozsa simulation on n inputs + 1 ancilla; returns P(output z) for the input register."""
    dim = 2 ** (n + 1)
    psi = [0] * dim
    psi[1 if ancilla_one else 0] = 1          # |0..0>|1> or |0..0>|0>
    psi = mv(kron_n(H, n + 1), psi)
    Uf = [[0] * dim for _ in range(dim)]
    for x in range(2 ** n):
        for y in range(2):
            Uf[(x << 1) | (y ^ f(x))][(x << 1) | y] = 1
    psi = mv(Uf, psi)
    psi = mv(kron(kron_n(H, n), I2), psi)
    return [sum(abs(psi[(z << 1) | y]) ** 2 for y in range(2)) for z in range(2 ** n)]


def amp_z(f, n, z):
    return sum((-1) ** (f(x) + sum(a * b for a, b in zip(bits(x, n), bits(z, n)))) for x in range(2 ** n)) / 2 ** n


CHECKS = []

# ---------- M12.1 Bloch worked clone: theta=pi/3, phi=pi/2 ----------
th, ph = math.pi / 3, math.pi / 2
CHECKS += [
    ("M12.1 alpha cos(pi/6)", math.cos(th / 2), 0.866, 0.01),
    ("M12.1 |beta| sin(pi/6)", math.sin(th / 2), 0.5, 1e-9),
    ("M12.1 P(0)", math.cos(th / 2) ** 2, 0.75, 1e-9),
    ("M12.1 P(1)", math.sin(th / 2) ** 2, 0.25, 1e-9),
    ("M12.1 Bloch y", math.sin(th) * math.sin(ph), 0.866, 0.01),
    ("M12.1 Bloch z", math.cos(th), 0.5, 1e-9),
]

# ---------- M12.2 gate identities (residual should be 0; stated 0 checked as 1 + residual vs 1) ----------
CHECKS += [
    ("M12.2 Y = iXZ (1+residual)", 1 + maxdiff(Y, [[1j * e for e in row] for row in mm(X, Z)]), 1, 1e-9),
    ("M12.2 H^2 = I (1+residual)", 1 + maxdiff(mm(H, H), I2), 1, 1e-9),
    ("M12.2 HZH = X (1+residual)", 1 + maxdiff(mm(H, mm(Z, H)), X), 1, 1e-9),
    ("M12.2 uniform amplitude n=2", 2 ** -1, 0.5, 1e-9),
]

# ---------- M12.3 Bell state ----------
bell = mv(CNOT, mv(kron(H, I2), [1, 0, 0, 0]))
CHECKS += [
    ("M12.3 Bell amp |00>", bell[0].real, r2, 1e-9),
    ("M12.3 Bell amp |11>", bell[3].real, r2, 1e-9),
    ("M12.3 Bell P(00)", abs(bell[0]) ** 2, 0.5, 1e-9),
    ("M12.3 Bell P(11)", abs(bell[3]) ** 2, 0.5, 1e-9),
    ("M12.3 product test c00*c11", (bell[0] * bell[3]).real, 0.5, 1e-9),
]

# ---------- M12.4 H-Z-H and H-H ----------
hzh = mv(H, mv(Z, mv(H, [1, 0])))
hh = mv(H, mv(H, [1, 0]))
CHECKS += [
    ("M12.4 HZH amp |1>", hzh[1], 1, 1e-9),
    ("M12.4 HZH P(0) (1+P)", 1 + abs(hzh[0]) ** 2, 1, 1e-9),
    ("M12.4 HH amp |0>", hh[0], 1, 1e-9),
]

# ---------- M12.6 Deutsch amp(0) for constant ----------
CHECKS += [("M12.6 Deutsch amp(0) constant f=0", amp_z(lambda x: 0, 1, 0), 1, 1e-9)]

# ---------- M12.7 DJ n=2 worked clones ----------
f_x1 = lambda x: (x >> 1) & 1
f_one = lambda x: 1
p_x1 = dj(f_x1, 2)
p_one = dj(f_one, 2)
k10 = 10
CHECKS += [
    ("M12.7 amp(00) f=x1 (1+amp)", 1 + amp_z(f_x1, 2, 0), 1, 1e-9),
    ("M12.7 amp(10) f=x1", amp_z(f_x1, 2, 0b10), 1, 1e-9),
    ("M12.7 sim P(10) f=x1", p_x1[0b10], 1, 1e-9),
    ("M12.7 amp(00) f=1", amp_z(f_one, 2, 0), -1, 1e-9),
    ("M12.7 sim P(00) f=1", p_one[0], 1, 1e-9),
    ("M12.7 deterministic queries n=2", 2 ** 1 + 1, 3, 1e-9),
    ("M12.7 randomised error k=10", 2 ** (1 - k10), 1 / 512, 1e-9),
    ("M12.7 randomised error k=10 (percent)", 100 * 2 ** (1 - k10), 0.2, 0.03),
]

# ---------- M12.8 teleportation ----------
CHECKS += [
    ("M12.8 Bell-measurement outcome prob", 1 / 4, 0.25, 1e-9),
    ("M12.8 classical bits per qubit", 2, 2, 1e-9),
]

# ---------- Exercise 8.1 ----------
th, ph = 2 * math.pi / 3, math.pi / 4
bx, by, bz = math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)
theta_09 = 2 * math.acos(math.sqrt(0.9))
CHECKS += [
    ("8.1 alpha", math.cos(th / 2), 0.5, 1e-9),
    ("8.1 |beta|", math.sin(th / 2), 0.866, 0.01),
    ("8.1 P(0)", math.cos(th / 2) ** 2, 0.25, 1e-9),
    ("8.1 P(1)", math.sin(th / 2) ** 2, 0.75, 1e-9),
    ("8.1 Bloch x", bx, 0.612, 0.01),
    ("8.1 Bloch y", by, 0.612, 0.01),
    ("8.1 Bloch z", bz, -0.5, 1e-9),
    ("8.1 Bloch length", math.sqrt(bx ** 2 + by ** 2 + bz ** 2), 1, 1e-9),
    ("8.1 P(0)=(1+z)/2", (1 + bz) / 2, 0.25, 1e-9),
    ("8.1(b) theta for P(0)=0.9 (rad)", theta_09, 0.644, 0.01),
    ("8.1(b) theta for P(0)=0.9 (deg)", math.degrees(theta_09), 36.9, 0.01),
]

# ---------- Exercise 8.2 ----------
CHECKS += [
    ("8.2 ZX = -XZ (1+residual)", 1 + maxdiff(mm(Z, X), [[-e for e in row] for row in mm(X, Z)]), 1, 1e-9),
    ("8.2 HXH = Z (1+residual)", 1 + maxdiff(mm(H, mm(X, H)), Z), 1, 1e-9),
    ("8.2 amp n=3", mv(kron_n(H, 3), [1] + [0] * 7)[0b101], 0.354, 0.01),
    ("8.2 P n=3", 1 / 8, 0.125, 1e-9),
    ("8.2 P n=30", 2 ** -30, 9.3e-10, 0.01),
]

# ---------- Exercise 8.3 ----------
circ = mm(CNOT, kron(H, I2))
out10 = mv(circ, [0, 0, 1, 0])
out01 = mv(circ, [0, 1, 0, 0])
out11 = mv(circ, [0, 0, 0, 1])
CHECKS += [
    ("8.3 |10> -> amp|00>", out10[0], r2, 1e-9),
    ("8.3 |10> -> amp|11>", out10[3], -r2, 1e-9),
    ("8.3 |01> -> amp|01>", out01[1], r2, 1e-9),
    ("8.3 |01> -> amp|10>", out01[2], r2, 1e-9),
    ("8.3 |11> -> amp|01>", out11[1], r2, 1e-9),
    ("8.3 |11> -> amp|10>", out11[2], -r2, 1e-9),
    ("8.3 P(00) for |10> input", abs(out10[0]) ** 2, 0.5, 1e-9),
    ("8.3 P(01) for |01> input", abs(out01[1]) ** 2, 0.5, 1e-9),
    ("8.3 product test c00*c11", out10[0] * out10[3], -0.5, 1e-9),
    ("8.3 X then H then CNOT on |00> equals |10> output (1+residual)",
     1 + max(abs(a - b) for a, b in zip(mv(mm(circ, kron(X, I2)), [1, 0, 0, 0]), out10)), 1, 1e-9),
]

# ---------- Exercise 8.4 ----------
def hph_p0(phi):
    P = [[1, 0], [0, cmath.exp(1j * phi)]]
    return abs(mv(H, mv(P, mv(H, [1, 0])))[0]) ** 2


harm8 = sum(1 / k for k in range(1, 9))
CHECKS += [
    ("8.4 P(0) phi=pi (1+P)", 1 + hph_p0(math.pi), 1, 1e-9),
    ("8.4 P(0) phi=pi/2", hph_p0(math.pi / 2), 0.5, 1e-9),
    ("8.4 P(0) phi=pi/3", hph_p0(math.pi / 3), 0.75, 1e-9),
    ("8.4 P(0) = cos^2(phi/2) at phi=1", hph_p0(1.0), math.cos(0.5) ** 2, 1e-9),
    ("8.4 P(0) phi=0", hph_p0(0), 1, 1e-9),
    ("8.4(b) P(see x=101)", 1 / 8, 0.125, 1e-9),
    ("8.4(b) harmonic H_8", harm8, 2.718, 0.001),
    ("8.4(b) coupon collector runs", 8 * harm8, 21.7, 0.01),
    ("8.4(b) classical evaluations", 8, 8, 1e-9),
]

# ---------- Exercise 8.5 Deutsch for all four f ----------
fa, fb, fc, fd = (lambda x: 0), (lambda x: 1), (lambda x: x), (lambda x: 1 - x)
CHECKS += [
    ("8.5 amp(0) f_a", amp_z(fa, 1, 0), 1, 1e-9),
    ("8.5 amp(0) f_b", amp_z(fb, 1, 0), -1, 1e-9),
    ("8.5 amp(0) f_c (1+amp)", 1 + amp_z(fc, 1, 0), 1, 1e-9),
    ("8.5 amp(0) f_d (1+amp)", 1 + amp_z(fd, 1, 0), 1, 1e-9),
    ("8.5 sim P(1) f_c", dj(fc, 1)[1], 1, 1e-9),
    ("8.5 sim P(0) f_b", dj(fb, 1)[0], 1, 1e-9),
    ("8.5 classical queries n=1", 2, 2, 1e-9),
]

# ---------- Exercise 8.6 DJ n=2 ----------
f_par = lambda x: ((x >> 1) ^ x) & 1
f_zero = lambda x: 0
f_and = lambda x: 1 if x == 0b11 else 0
p_par = dj(f_par, 2)
p_and = dj(f_and, 2)
p_par_broken = dj(f_par, 2, ancilla_one=False)
CHECKS += [
    ("8.6(a) parity is balanced: count of 1s", sum(f_par(x) for x in range(4)), 2, 1e-9),
    ("8.6(a) amp(00) parity (1+amp)", 1 + amp_z(f_par, 2, 0), 1, 1e-9),
    ("8.6(a) amp(11) parity", amp_z(f_par, 2, 0b11), 1, 1e-9),
    ("8.6(a) sim P(11) parity", p_par[0b11], 1, 1e-9),
    ("8.6(b) amp(00) f=0", amp_z(f_zero, 2, 0), 1, 1e-9),
    ("8.6(c) amp(00) AND", amp_z(f_and, 2, 0), 0.5, 1e-9),
    ("8.6(c) sim P(00) AND", p_and[0], 0.25, 1e-9),
    ("8.6(c) P(non-zero outputs) AND", 1 - p_and[0], 0.75, 1e-9),
    ("8.6(d) ancilla |0>: sim P(00) parity", p_par_broken[0], 1, 1e-9),
]

# ---------- Exercise 8.7 query counts ----------
k_needed = next(k for k in range(1, 100) if 2 ** (1 - k) < 1e-6)
CHECKS += [
    ("8.7 deterministic n=2", 2 ** 1 + 1, 3, 1e-9),
    ("8.7 deterministic n=10", 2 ** 9 + 1, 513, 1e-9),
    ("8.7 deterministic n=30 exact", 2 ** 29 + 1, 536870913, 1e-12),
    ("8.7 deterministic n=30 approx", 2 ** 29 + 1, 5.4e8, 0.01),
    ("8.7 randomised error k=10", 2 ** -9, 1.95e-3, 0.01),
    ("8.7 randomised error k=10 = 1/512", 2 ** -9, 1 / 512, 1e-9),
    ("8.7 6*log2(10)", 6 * math.log2(10), 19.9, 0.01),
    ("8.7 smallest k for 1e-6", k_needed, 21, 1e-9),
    ("8.7 error at k=21", 2 ** -20, 9.5e-7, 0.01),
    ("8.7 error at k=20", 2 ** -19, 1.9e-6, 0.01),
]

# ---------- Exercise 8.8 pump schedules (fictional fact sheet: 220 pumps, 4 bands, GBP 18m, 6%) ----------
bill = 18e6
CHECKS += [
    ("8.8 2^220 patterns", 2 ** 220, 1.7e66, 0.01),
    ("8.8 four bands 2^880 (log10)", 880 * math.log10(2), 265, 0.002),
    ("8.8 prob of one pattern", 2 ** -220, 6e-67, 0.02),
    ("8.8 Grover sqrt(2^220)", math.sqrt(2 ** 220), 1.3e33, 0.01),
    ("8.8 sqrt(2^220) = 2^110", math.sqrt(2 ** 220), 2 ** 110, 1e-9),
    # GBP 18m is the bill WITH the optimiser, which saves 6% against an unoptimised schedule
    ("8.8 unoptimised bill, prose 'about 19.1 m' (GBP)", bill / 0.94, 19.1e6, 0.005),
    ("8.8 today's saving 18m/0.94 - 18m (GBP)", bill / 0.94 - bill, 1.15e6, 0.001),
    ("8.8 one further point of today's bill (GBP/yr)", 0.01 * bill, 180000, 1e-9),
]

# ---------- Exercise 8.9 ----------
CHECKS += [
    ("8.9 amp(00) f=x1 (1+amp)", 1 + amp_z(f_x1, 2, 0), 1, 1e-9),
    ("8.9 deterministic n=10", 2 ** 9 + 1, 513, 1e-9),
    ("8.9 randomised k=10 error (percent)", 100 * 2 ** -9, 0.2, 0.03),
]

# ---------- Exercise 8.10 teleportation over 160 km fibre ----------
CHECKS += [
    ("8.10 one-way delay 160 km at 2e8 m/s (ms)", 160e3 / 2e8 * 1e3, 0.8, 1e-9),
]

# ---------- Spaced review ----------
CHECKS += [
    ("SR Day07 8*2^30 bytes", 8 * 2 ** 30, 8.6e9, 0.01),
    ("SR Day07 8*2^40 bytes", 8 * 2 ** 40, 8.8e12, 0.01),
    ("SR Day04 T^2 gain 0.2->2 s", (2 / 0.2) ** 2, 100, 1e-9),
    ("SR Day02 time to 1 uGal at 20 uGal/rtHz (s)", (20 / 1) ** 2, 400, 1e-9),
    ("SR Day01 2^40 order of magnitude", 2 ** 40, 1e12, 0.1),
    ("SR Day01 2^40 exact", 2 ** 40, 1.1e12, 0.01),
]
