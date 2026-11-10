"""Numeric answers stated in content/day10.md (maturity, comparison and the capstone).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
"""
import math

H = 6.626e-34
E = 1.602e-19
C = 3.00e8
G = 9.81
PHI0 = H / (2 * E)


def order(a, n):
    x, r = a % n, 1
    while x != 1:
        x, r = (x * a) % n, r + 1
    return r


def ev(p, b, c):
    return p * b - c


CHECKS = []

# ---------- Core concepts: M14.1 worked clone (hypothetical, £k) ----------
B0, C0 = 150 * 5, 200
CHECKS += [
    ("M14.1 B = 150k x 5", B0, 750, 0),
    ("M14.1 EV central p=0.3", ev(0.3, B0, C0), 25, 1e-9),
    ("M14.1 EV p=0.1", ev(0.1, B0, C0), -125, 1e-9),
    ("M14.1 EV p=0.5", ev(0.5, B0, C0), 175, 1e-9),
    ("M14.1 p* = 200/750", C0 / B0, 0.27, 0.02),
    ("M14.1 EV saving 100k", ev(0.3, 100 * 5, C0), -50, 1e-9),
    ("M14.1 EV saving 200k", ev(0.3, 200 * 5, C0), 100, 1e-9),
    ("M14.1 B low", 100 * 5, 500, 0),
    ("M14.1 B high", 200 * 5, 1000, 0),
    ("M14.1 swing p", ev(0.5, B0, C0) - ev(0.1, B0, C0), 300, 1e-9),
    ("M14.1 swing saving", ev(0.3, 1000, C0) - ev(0.3, 500, C0), 150, 1e-9),
    ("M14.2 R = 225/200", 0.3 * B0 / C0, 1.1, 0.03),
    ("M14.2 expected benefit 225", 0.3 * B0, 225, 1e-9),
]

# ---------- Exercise 10.1: corrosion candidate (£M) ----------
R_SPEND, KM = 40.0, 2400
B1 = 10 * 0.05 * R_SPEND
CHECKS += [
    ("10.1a spend per km per year (GBP)", R_SPEND * 1e6 / KM, 16_700, 0.005),
    ("10.1b annual saving", 0.05 * R_SPEND, 2, 1e-9),
    ("10.1b B 10 years", B1, 20, 1e-9),
    ("10.1c expected benefit", 0.02 * B1, 0.4, 1e-9),
    ("10.1c EV_P central", ev(0.02, B1, 0.5), -0.1, 1e-6),
    ("10.1c EV_P p=0.005", ev(0.005, B1, 0.5), -0.4, 1e-6),
    ("10.1c EV_P p=0.05", ev(0.05, B1, 0.5), 0.5, 1e-6),
    ("10.1c B at s=2%", 10 * 0.02 * R_SPEND, 8, 1e-9),
    ("10.1c B at s=10%", 10 * 0.10 * R_SPEND, 40, 1e-9),
    ("10.1c EV_P s=2%", ev(0.02, 8, 0.5), -0.34, 1e-6),
    ("10.1c EV_P s=10%", ev(0.02, 40, 0.5), 0.3, 1e-6),
    ("10.1d p* P", 0.5 / B1, 0.025, 1e-9),
    ("10.1d R P", 0.02 * B1 / 0.5, 0.8, 1e-9),
    ("10.1d p* B", 3 / B1, 0.15, 1e-9),
    ("10.1d R B", 0.02 * B1 / 3, 0.13, 0.03),
    ("10.1d EV_B", ev(0.02, B1, 3), -2.6, 1e-6),
    ("10.1e swing p", ev(0.05, B1, 0.5) - ev(0.005, B1, 0.5), 0.9, 1e-6),
    ("10.1e swing s", ev(0.02, 40, 0.5) - ev(0.02, 8, 0.5), 0.64, 1e-6),
    ("10.1f break-even fee", 0.02 * B1, 0.4, 1e-9),
    ("10.1 check B p* / top of range", 0.15 / 0.05, 3, 1e-9),
]

# ---------- Exercise 10.2: vendor slide audit (£k) ----------
DIGS = 300 * 4  # £k a year
ben = 0.6 * 0.4 * DIGS
CHECKS += [
    ("10.2 dry-dig spend", DIGS, 1200, 0),
    ("10.2a expected benefit", ben, 288, 1e-9),
    ("10.2a R central", ben / 150, 1.9, 0.02),
    ("10.2a R central (3 s.f.)", ben / 150, 1.92, 0.005),
    ("10.2a benefit f=0.2", 0.6 * 0.2 * DIGS, 144, 1e-9),
    ("10.2a R f=0.2", 0.6 * 0.2 * DIGS / 150, 0.96, 1e-9),
    ("10.2a benefit f=0.6", 0.6 * 0.6 * DIGS, 432, 1e-9),
    ("10.2a R f=0.6", 0.6 * 0.6 * DIGS / 150, 2.9, 0.01),
    ("10.2a net central", ben - 150, 138, 1e-9),
    ("10.2a slide ratio", DIGS / 100, 12, 0),
    ("10.2a overstatement", (DIGS / 100) / (ben / 150), 6.25, 1e-9),
    ("10.2b p*", 150 / (0.4 * DIGS), 0.31, 0.01),
    ("10.2b p* exact", 150 / (0.4 * DIGS), 0.3125, 1e-9),
    ("10.2c B at 1.0 m (uT)", 2e-7 * 100 / 1.0 * 1e6, 20, 1e-9),
    ("10.2c B at 2.0 m (uT)", 2e-7 * 100 / 2.0 * 1e6, 10, 1e-9),
    ("10.2c fluxgate noise 1 Hz (pT)", 10 * math.sqrt(1), 10, 0),
    ("10.2c SNR at 2 m", (2e-7 * 100 / 2.0) / 10e-12, 1e6, 1e-9),
]

# ---------- Exercise 10.3: fact sheet numbers ----------
CHECKS += [
    ("10.3 memory 8*2^50 (PB)", 8 * 2 ** 50 / 1e15, 9, 0.01),
    ("10.3 physical qubits 100 x 880", 100 * 880, 88_000, 0),
    ("10.3 Day09 ratio 2*21^2", 2 * 21 ** 2, 880, 0.005),
]

# ---------- Capstone ----------
# 10.6 M1
dt = 3e-11 * 6 * 3600
CHECKS += [
    ("10.6a 250 pT in fT", 250e-12 / 1e-15, 2.5e5, 1e-9),
    ("10.6b 18 uGal in m/s2", 18e-8, 1.8e-7, 1e-9),
    ("10.6b fraction of g", 18e-8 / G, 1.8e-8, 0.02),
    ("10.6c 6 h in s", 6 * 3600, 21_600, 0),
    ("10.6c time error (s)", dt, 6.5e-7, 0.01),
    ("10.6c time error (us)", dt * 1e6, 0.65, 0.01),
    ("10.6c distance (m)", C * dt, 194, 0.005),
]
# 10.7 M2
CHECKS += [
    ("10.7a 45 fT x sqrt(25)", 45 * math.sqrt(25), 225, 1e-9),
    ("10.7b Allan at 400 s", 4e-13 / math.sqrt(400), 2e-14, 1e-9),
    ("10.7 check sqrt(400)", math.sqrt(400), 20, 1e-9),
]
# 10.8 M3
CHECKS += [
    ("10.8a 1/sqrt(9e6) = 1/3000", math.sqrt(9e6), 3000, 1e-9),
    ("10.8a shot noise N=9e6", 1 / math.sqrt(9e6), 3.3e-4, 0.02),
    ("10.8a Heisenberg N=9e6", 1 / 9e6, 1.1e-7, 0.02),
    ("10.8a ratio sqrt(N)", math.sqrt(9e6), 3000, 1e-9),
    ("10.8 check 3.3e-4/1.1e-7", 3.3e-4 / 1.1e-7, 3000, 1e-6),
    ("10.8b dipole 1/r^3 (1.5->0.5 m)", (1.5 / 0.5) ** 3, 27, 1e-9),
    ("10.8b current dipole 1/r^2", (1.5 / 0.5) ** 2, 9, 1e-9),
]
# 10.9 M4, M5
CHECKS += [
    ("10.9a Q 411 THz / 0.5 Hz", 411e12 / 0.5, 8.2e14, 0.005),
    ("10.9b Ramsey 1/(2T)", 1 / (2 * 0.25), 2, 1e-9),
    ("10.9c Larmor 35 uT (kHz)", 7 * 35_000 / 1e3, 245, 1e-9),
    ("10.9d Phi0/A (nT)", PHI0 / 0.25e-6 * 1e9, 8.3, 0.01),
    ("10.9d Phi0", PHI0, 2.07e-15, 0.005),
]
# 10.10 M6, M7
k_eff = 4 * math.pi / 671e-9
phi = k_eff * G * 0.15 ** 2
CHECKS += [
    ("10.10a k_eff 671 nm", k_eff, 1.87e7, 0.005),
    ("10.10b T^2", 0.15 ** 2, 0.0225, 1e-9),
    ("10.10b Phi", phi, 4.13e6, 0.005),
    ("10.10b fringes", phi / (2 * math.pi), 6.6e5, 0.01),
    ("10.10c tau=2T phase", k_eff * G * (2 * 0.15) ** 2, 1.65e7, 0.005),
    ("10.10d cos^2(pi/5)", math.cos(math.pi / 5) ** 2, 0.655, 0.001),
    ("10.10d about 65%", math.cos(math.pi / 5) ** 2 * 100, 65, 0.01),
]
# 10.11 M8, M9
CHECKS += [
    ("10.11a x+y", 8 + 6, 14, 0),
    ("10.11b QBER 30% intercept", 0.3 * 0.25, 0.075, 1e-9),
    ("10.11c 0.75^12", 0.75 ** 12, 0.032, 0.02),
    ("10.11c detection 12 bits", 1 - 0.75 ** 12, 0.968, 0.001),
]
# 10.12 M10
CHECKS += [
    ("10.12a loss dB 65 km", 0.2 * 65, 13, 1e-9),
    ("10.12a transmission", 10 ** (-13 / 10), 0.050, 0.01),
    ("10.12b hop length", 65 / 2, 32.5, 0),
    ("10.12b hop loss dB", 0.2 * 32.5, 6.5, 1e-9),
    ("10.12b hop transmission", 10 ** (-6.5 / 10), 0.22, 0.02),
    ("10.12c 2 sqrt2", 2 * math.sqrt(2), 2.83, 0.002),
    ("10.12c 2.6 / 2sqrt2", 2.6 / (2 * math.sqrt(2)), 0.92, 0.005),
]
# 10.13 M11
CHECKS += [
    ("10.13a 2^42", 2 ** 42, 4.40e12, 0.002),
    ("10.13a 8*2^42 bytes", 8 * 2 ** 42, 3.5e13, 0.01),
    ("10.13a in TB", 8 * 2 ** 42 / 1e12, 35, 0.01),
    ("10.13b 512 GB / 8", 5.12e11 / 8, 6.4e10, 1e-9),
    ("10.13b log2", math.log2(5.12e11 / 8), 35.9, 0.002),
    ("10.13b largest N", math.floor(math.log2(5.12e11 / 8)), 35, 0),
    ("10.13b 8*2^35 bytes", 8 * 2 ** 35, 2.7e11, 0.02),
    ("10.13b 8*2^35 GB", 8 * 2 ** 35 / 1e9, 275, 0.001),
    ("10.13b 8*2^36 GB", 8 * 2 ** 36 / 1e9, 550, 0.001),
]
# 10.14 M12
amp = 1 / math.sqrt(2)
CHECKS += [
    ("10.14b P(01)", amp ** 2, 0.5, 1e-9),
    ("10.14b P(10)", amp ** 2, 0.5, 1e-9),
]
# 10.15 M13: Shor N=51, a=2
r = order(2, 51)
y = pow(2, r // 2, 51)
CHECKS += [
    ("10.15a gcd(2,51)", math.gcd(2, 51), 1, 0),
    ("10.15a order of 2 mod 51", r, 8, 0),
    ("10.15a 2^6 mod 51", pow(2, 6, 51), 13, 0),
    ("10.15a 2^7 mod 51", pow(2, 7, 51), 26, 0),
    ("10.15a y = 2^4 mod 51", y, 16, 0),
    ("10.15a -1 mod 51", 51 - 1, 50, 0),
    ("10.15a gcd(y-1,51)", math.gcd(y - 1, 51), 3, 0),
    ("10.15a gcd(y+1,51)", math.gcd(y + 1, 51), 17, 0),
    ("10.15a 256 = 5*51+1", 5 * 51 + 1, 256, 0),
    ("10.15b sqrt(4e8)", math.sqrt(4e8), 2e4, 1e-9),
    ("10.15b Grover iterations", math.pi / 4 * math.sqrt(4e8), 15_708, 1e-4),
    ("10.15b classical N/2", 4e8 / 2, 2e8, 0),
    ("10.15b query ratio", (4e8 / 2) / (math.pi / 4 * math.sqrt(4e8)), 13_000, 0.03),
    ("10.15c g_half F=0.9975", math.log(0.5) / math.log(0.9975), 277, 0.003),
    ("10.15c rule of thumb", 0.693 / 0.0025, 277, 0.003),
]

# 10.16 model paragraph reuses 10.1 and 10.3 numbers (checked above)

# ---------- Spaced review ----------
CHECKS += [
    ("SR1 Grover N=2.5e7", math.pi / 4 * math.sqrt(2.5e7), 3927, 1e-3),
    ("SR1 sqrt(2.5e7)", math.sqrt(2.5e7), 5000, 1e-9),
    ("SR2 g_half F=0.996", math.log(0.5) / math.log(0.996), 173, 0.005),
    ("SR5 8*2^33 bytes", 8 * 2 ** 33, 6.9e10, 0.01),
    ("SR5 8*2^33 GB", 8 * 2 ** 33 / 1e9, 69, 0.01),
    ("SR8 1e-14 x 1 day (s)", 1e-14 * 86_400, 8.6e-10, 0.01),
    ("SR8 distance (m)", C * 1e-14 * 86_400, 0.26, 0.01),
    ("SR9 Larmor 50 uT (kHz)", 7 * 50_000 / 1e3, 350, 1e-9),
    ("SR10 Phi0", PHI0, 2.07e-15, 0.005),
]
