"""Numeric answers stated in content/day07.md (Quantum simulation, M11).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
Decimal prefixes throughout (1 kB = 1e3 B, 1 TB = 1e12 B).
"""
import math

h = 6.62607015e-34
hbar = h / (2 * math.pi)
kB = 1.380649e-23
u = 1.66053906660e-27
g = 9.81

m_na = 22.98976928 * u
m_rb = 86.909180527 * u


def sp(N):  # single-precision complex state, bytes
    return 8 * 2**N


def dp(N):  # double-precision complex state, bytes
    return 16 * 2**N


def lth(m, T):
    return h / math.sqrt(2 * math.pi * m * kB * T)


def tc(m, n):
    return 2 * math.pi * hbar**2 / (m * kB) * (n / 2.612) ** (2 / 3)


# ---------- M11.1 corrected Table 5.2 ----------
# ---------- M11.2 one-spin clone ----------
p_clone = math.sin(math.pi / 8) ** 2
# ---------- M11.3 MPS clone ----------
mps60 = 2 * 128**2 * 60
# ---------- M11.6 Na clone ----------
lam_na = lth(m_na, 1e-6)
d20 = 1e20 ** (-1 / 3)
# ---------- M11.7 Na lattice clone ----------
v_na = h / (m_na * 426e-9)

# ---------- Exercise 7.2 ----------
n_node = math.floor(math.log2(2e12 / 16))
n_mach = math.floor(math.log2(1e16 / 16))
# ---------- Exercise 7.4 ----------
M_runs = 1 / 0.005**2
# ---------- Exercise 7.5 ----------
n_trot = 10**2 * 4 / (2 * 0.01)
g_budget = math.log(0.5) / math.log(0.999)
# ---------- Exercise 7.6 ----------
lam2u = lth(m_rb, 2e-6)
lam200 = lth(m_rb, 200e-9)
psd2u = 1e20 * lam2u**3
psd200 = 1e20 * lam200**3
# ---------- Exercise 7.7 ----------
sites_side = 25 / 0.532
sites = sites_side**3
v_rb = h / (m_rb * 532e-9)
# Deep-lattice approximations behind the stated J, U table (judgement), Rb-87, 1064 nm lattice
Er = h / (2 * m_rb * (1064e-9) ** 2)  # recoil energy / h, in Hz
k_l = 2 * math.pi / 1064e-9
a_s = 5.3e-9


def J_of(s):
    return 4 / math.sqrt(math.pi) * s**0.75 * math.exp(-2 * math.sqrt(s)) * Er


def U_of(s):
    return math.sqrt(8 / math.pi) * k_l * a_s * s**0.75 * Er


# ---------- Exercise 7.10 ----------
conf = math.comb(60, 30)
mem_conf = 8 * conf

CHECKS = [
    # M11.1 table (corrected)
    ("T5.2 N=3 bytes", sp(3), 64, 0.001),
    ("T5.2 N=10 kB", sp(10) / 1e3, 8.2, 0.01),
    ("T5.2 N=20 2^N", 2**20, 1.05e6, 0.01),
    ("T5.2 N=20 MB", sp(20) / 1e6, 8.4, 0.01),
    ("T5.2 N=30 2^N", 2**30, 1.07e9, 0.01),
    ("T5.2 N=30 GB", sp(30) / 1e9, 8.6, 0.01),
    ("T5.2 N=40 2^N", 2**40, 1.10e12, 0.01),
    ("T5.2 N=40 TB", sp(40) / 1e12, 8.8, 0.01),
    ("T5.2 N=50 2^N", 2**50, 1.13e15, 0.01),
    ("T5.2 N=50 PB", sp(50) / 1e15, 9.0, 0.01),
    ("T5.2 lecture N=20 off by", sp(20) / 840e3, 10, 0.01),
    ("T5.2 lecture N=40 off by", sp(40) / 880e9, 10, 0.01),
    ("M11.1 clone N=25 amplitudes", 2**25, 3.36e7, 0.01),
    ("M11.1 clone N=25 single MB", sp(25) / 1e6, 268, 0.01),
    ("M11.1 clone N=25 double MB", dp(25) / 1e6, 537, 0.01),
    ("M11.1 clone N=45 bytes", sp(45), 2.8e14, 0.02),
    ("M11.1 clone N=45 TB", sp(45) / 1e12, 281, 0.01),
    # M11.2
    ("M11.2 clone P_down", p_clone, 0.146, 0.01),
    # M11.3
    ("M11.3 MPS chi=128 N=60 complex numbers", mps60, 1.97e6, 0.01),
    ("M11.3 MPS memory MB", mps60 * 8 / 1e6, 16, 0.02),
    ("M11.3 full N=60 bytes", sp(60), 9.2e18, 0.01),
    # M11.4
    ("M11.4 clone Trotter slices", 5**2 * 2 / (2 * 0.01), 2500, 0.001),
    # M11.5
    ("M11.5 He-3 count", 2 + 2 + 1, 5, 0),
    ("M11.5 He-4 count", 2 + 2 + 2, 6, 0),
    ("M11.5 Li-6 count", 3 + 3 + 3, 9, 0),
    # M11.6
    ("M11.6 BEC lambda/d threshold", 2.612 ** (1 / 3), 1.38, 0.01),
    ("M11.6 Na mass kg", m_na, 3.82e-26, 0.01),
    ("M11.6 Na lambda_th 1uK", lam_na, 3.6e-7, 0.02),
    ("M11.6 spacing n=1e20", d20, 2.2e-7, 0.03),
    ("M11.6 Na n lambda^3", 1e20 * lam_na**3, 4.8, 0.02),
    ("M11.6 Na Tc uK", tc(m_na, 1e20) * 1e6, 1.5, 0.02),
    ("M11.6 Na lambda_th 300K", lth(m_na, 300), 2.1e-11, 0.02),
    # M11.7
    ("M11.7 clone d nm", 852 / 2, 426, 0.001),
    ("M11.7 clone h/(md) m/s", v_na, 4.1e-2, 0.02),
    ("M11.7 clone peaks mm", v_na * 0.010 * 1e3, 0.41, 0.02),
    # M11.8
    ("M11.8 9 ions amplitudes", 2**9, 512, 0),
    ("M11.8 9 ions kB", sp(9) / 1e3, 4, 0.03),
    ("M11.8 16 ions kB", sp(16) / 1e3, 524, 0.01),
    # Ex 7.1
    ("7.1a N=20 bytes", sp(20), 8.39e6, 0.01),
    ("7.1a N=40 bytes", sp(40), 8.80e12, 0.01),
    ("7.1b N=30 double", dp(30), 1.7e10, 0.02),
    ("7.1b N=30 double GB", dp(30) / 1e9, 17, 0.02),
    ("7.1b N=50 double", dp(50), 1.8e16, 0.01),
    ("7.1b N=50 double PB", dp(50) / 1e15, 18, 0.01),
    ("7.1c 3 copies N=34", 3 * dp(34), 8.2e11, 0.01),
    ("7.1c GB", 3 * dp(34) / 1e9, 820, 0.01),
    ("7.1 check ratio per 10 spins", sp(30) / sp(20), 1024, 0),
    # Ex 7.2
    ("7.2a log2 node", math.log2(2e12 / 16), 36.9, 0.01),
    ("7.2a 1.25e11", 2e12 / 16, 1.25e11, 0.001),
    ("7.2a N node", n_node, 36, 0),
    ("7.2a N=36 bytes", dp(36), 1.1e12, 0.01),
    ("7.2a N=37 bytes", dp(37), 2.2e12, 0.01),
    ("7.2b log2 machine", math.log2(1e16 / 16), 49.2, 0.01),
    ("7.2b N machine", n_mach, 49, 0),
    ("7.2b N=49 bytes", dp(49), 9.0e15, 0.01),
    ("7.2c extra spins", n_mach - n_node, 13, 0),
    ("7.2c log2 5000", math.log2(5000), 12.3, 0.01),
    ("7.2c 2^12.3", 2**12.3, 5000, 0.02),
    # Ex 7.3
    ("7.3a Omega", 2 * math.pi * 250, 1571, 0.001),
    ("7.3a N=16 dense bytes", 16 * 4**16, 6.9e10, 0.01),
    ("7.3a N=16 dense GB", 16 * 4**16 / 1e9, 69, 0.01),
    ("7.3a N=16 ops", 8**16, 2.8e14, 0.01),
    ("7.3a N=20 dense bytes", 16 * 4**20, 1.8e13, 0.03),
    ("7.3a N=20 dense TB", 16 * 4**20 / 1e12, 18, 0.03),
    ("7.3a N=20 ops", 8**20, 1.2e18, 0.05),
    ("7.3 dense/state ratio N=20", (16 * 4**20) / dp(20), 2**20, 0),
    ("7.3 double state N=20 MB", dp(20) / 1e6, 16.8, 0.01),
    ("7.3b P_down", math.sin(2 * math.pi * 250 * 1e-3 / 2) ** 2, 0.50, 0.01),
    ("7.3b flip time ms", math.pi / (2 * math.pi * 250) * 1e3, 2, 0.001),
    # Ex 7.4
    ("7.4a MPS bytes", 2 * 256**2 * 100 * 8, 1.05e8, 0.01),
    ("7.4a full bytes", sp(100), 1.0e31, 0.02),
    ("7.4b runs", M_runs, 4.0e4, 0.001),
    ("7.4c cold atom s", M_runs * 20, 8.0e5, 0.001),
    ("7.4c cold atom h", M_runs * 20 / 3600, 222, 0.01),
    ("7.4c cold atom days", M_runs * 20 / 86400, 9.3, 0.01),
    ("7.4c ion s", M_runs * 0.01, 400, 0.001),
    ("7.4c ion min", M_runs * 0.01 / 60, 6.7, 0.01),
    # Ex 7.5
    ("7.5a slices", n_trot, 2.0e4, 0.001),
    ("7.5b gates", n_trot * 99, 1.98e6, 0.001),
    ("7.5c gate budget", g_budget, 693, 0.002),
    ("7.5 check ratio", n_trot * 99 / g_budget, 2900, 0.02),
    # Ex 7.6
    ("7.6a Li-7", 3 + 3 + 4, 10, 0),
    ("7.6a K-40", 19 + 19 + 21, 59, 0),
    ("7.6a Rb-87", 37 + 37 + 50, 124, 0),
    ("7.6a Na-23", 11 + 11 + 12, 34, 0),
    ("7.6a Sr-87", 38 + 38 + 49, 125, 0),
    ("7.6b Rb mass", m_rb, 1.443e-25, 0.001),
    ("7.6b spacing", d20, 2.15e-7, 0.01),
    ("7.6b lambda 2uK", lam2u, 1.32e-7, 0.01),
    ("7.6b psd 2uK", psd2u, 0.23, 0.02),
    ("7.6b lambda 200nK", lam200, 4.19e-7, 0.01),
    ("7.6b psd 200nK", psd200, 7.3, 0.02),
    ("7.6c Tc scaled", 2e-6 * (psd2u / 2.612) ** (2 / 3) * 1e6, 0.40, 0.02),
    ("7.6c Tc formula", tc(m_rb, 1e20) * 1e9, 400, 0.02),
    ("7.6 check 10^1.5", 10**1.5, 31.6, 0.01),
    ("7.6 check psd ratio", psd200 / psd2u, 31.6, 0.01),
    # Ex 7.7
    ("7.7a d nm", 1064 / 2, 532, 0),
    ("7.7b sites per side", sites_side, 47.0, 0.01),
    ("7.7b sites", sites, 1.04e5, 0.01),
    ("7.7b filling", 1.2e5 / sites, 1.16, 0.01),
    ("7.7c table J5 Hz", J_of(5), 175, 0.02),
    ("7.7c table U5 Hz", U_of(5), 340, 0.02),
    ("7.7c table J10 Hz", J_of(10), 46, 0.02),
    ("7.7c table U10 Hz", U_of(10), 570, 0.02),
    ("7.7c table J15 Hz", J_of(15), 15, 0.02),
    ("7.7c table U15 Hz", U_of(15), 770, 0.02),
    ("7.7c table J20 Hz", J_of(20), 5.6, 0.02),
    ("7.7c table U20 Hz", U_of(20), 960, 0.02),
    ("7.7c U/J 5", 340 / 175, 1.9, 0.03),
    ("7.7c U/J 10", 570 / 46, 12.4, 0.01),
    ("7.7c U/J 15", 770 / 15, 51, 0.01),
    ("7.7c U/J 20", 960 / 5.6, 171, 0.01),
    ("7.7 check J drop", 175 / 5.6, 30, 0.05),
    # Mott boundary: QMC 29.3 (working value 29) vs mean field 5.83z; no 7.7 ratio lies between them
    ("M11.7 mean-field (U/J)_c 5.83z, z=6", 5.83 * 6, 35, 0.001),
    ("7.7c no ratio in [29, 35]", sum(29 <= r <= 35 for r in (340 / 175, 570 / 46, 770 / 15, 960 / 5.6)), 0, 0),
    ("7.7d h/(md)", v_rb, 8.6e-3, 0.01),
    ("7.7d peak spacing m", v_rb * 0.015, 1.3e-4, 0.01),
    ("7.7d peak spacing um", v_rb * 0.015 * 1e6, 129, 0.01),
    # Ex 7.8 model paragraph (reuses 7.2: 36, 49, 13, 5000)
    ("7.8 node N", n_node, 36, 0),
    ("7.8 machine N", n_mach, 49, 0),
    # Ex 7.9 model paragraph
    ("7.9 K-40 neutrons", 40 - 19, 21, 0),
    ("7.9 K-40 count", 59, 59, 0),
    ("7.9 lattice spacing nm", 1064 / 2, 532, 0),
    # Ex 7.10 model paragraph
    ("7.10 C(60,30)", conf, 1.2e17, 0.02),
    ("7.10 memory PB", mem_conf / 1e15, 940, 0.01),
    ("7.10 ratio to 10 PB", mem_conf / 1e16, 94, 0.01),
    ("7.10 Ex7.5 gates", n_trot * 99, 2e6, 0.01),
    ("7.10 budget fraction %", 180000 / 40e6 * 100, 0.45, 0.001),
    # Spaced review
    ("SR2 (3/4)^20", 0.75**20, 3.2e-3, 0.01),
    ("SR3 fibre 50 km 0.2 dB/km", 10 ** (-0.2 * 50 / 10), 0.10, 0.001),
    ("SR4 CHSH quantum", 2 * math.sqrt(2), 2.83, 0.001),
    ("SR5 Mosca x+y", 10 + 5, 15, 0),
    ("SR6 keff Rb 780", 4 * math.pi / 780e-9, 1.61e7, 0.01),
    ("SR6 Phi", 4 * math.pi / 780e-9 * g * 0.01, 1.58e6, 0.01),
    ("SR7 2 fT x sqrt(100)", 2 * math.sqrt(100), 20, 0),
    ("SR8 shot", 1 / math.sqrt(1e6), 1e-3, 0),
    ("SR8 Heisenberg", 1 / 1e6, 1e-6, 0),
]
