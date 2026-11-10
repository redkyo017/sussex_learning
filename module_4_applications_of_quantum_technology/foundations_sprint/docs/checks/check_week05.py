"""Numeric checks for content/companions/week05_companion.md (sections 4-6).
Each tuple: (label, computed, stated, rel_tol)."""
from itertools import product
from math import exp, log, pi, sqrt

h = 6.62607015e-34
hbar = h / (2 * pi)
kB = 1.380649e-23
u = 1.66053907e-27

m_rb = 86.909184 * u
m_k41 = 40.9618253 * u
m_k39 = 38.96370649 * u


def lam_T(m, T):
    return h / sqrt(2 * pi * m * kB * T)


def T_c(m, n):
    return 2 * pi * hbar**2 / (m * kB) * (n / 2.612) ** (2 / 3)


def J_over_Er(s):
    return 4 / sqrt(pi) * s**0.75 * exp(-2 * sqrt(s))


# ---- section 4 ----
lam_rb = lam_T(m_rb, 100e-9)
nc_rb = 2.612 / lam_rb**3
n_air = 101325 / (kB * 293)
n_gas = n_air / 1e6
frust = [s[0] * s[1] + s[1] * s[2] + s[0] * s[2] for s in product([1, -1], repeat=3)]

# ---- sections 5-6 ----
lam_k = lam_T(m_k41, 300e-9)
# C5.3: K-39 in a 1550 nm lattice, a_s = 5.0 nm (fictional Feshbach setting), 20 ms flight
lam_l = 1550e-9
d_l = lam_l / 2
Er_k39 = h / (2 * m_k39 * lam_l**2)  # recoil energy / h, Hz
k_l = 2 * pi / lam_l
a_s = 5.0e-9


def J_k39(s):
    return J_over_Er(s) * Er_k39


def U_k39(s):
    return sqrt(8 / pi) * k_l * a_s * s**0.75 * Er_k39


v_peak = h / (m_k39 * d_l)  # = 2 hbar k / m

# C5.4: 8x8 Fermi-Hubbard lattice, 64 fermions in 128 spin-orbitals
from math import comb
conf = comb(128, 64)

CHECKS = [
    # 4A
    ("4A dense H N=20 bytes", 8 * 4**20, 8.8e12, 0.01),
    ("4A dense H N=30 bytes", 8 * 4**30, 9.2e18, 0.01),
    ("4A diag ops N=20", (2**20) ** 3, 1.2e18, 0.05),
    ("4A state N=20 MB", 8 * 2**20 / 1e6, 8.4, 0.01),
    # 4B
    ("4B three spins amplitudes", 2**3, 8, 0),
    ("4B three spins bytes", 8 * 2**3, 64, 0),
    # 4C table
    ("4C N=3", 8 * 2**3, 64, 0),
    ("4C N=10 kB", 8 * 2**10 / 1e3, 8.2, 0.01),
    ("4C N=20 exact", 8 * 2**20, 8388608, 0),
    ("4C N=20 MB", 8 * 2**20 / 1e6, 8.4, 0.01),
    ("4C N=30 GB", 8 * 2**30 / 1e9, 8.6, 0.01),
    ("4C N=40 TB", 8 * 2**40 / 1e12, 8.8, 0.01),
    ("4C N=50 TB", 8 * 2**50 / 1e12, 9000, 0.01),
    ("4C 2^30", 2**30, 1.07e9, 0.01),
    ("4C 2^40", 2**40, 1.10e12, 0.01),
    ("4C 2^50", 2**50, 1.13e15, 0.01),
    ("4C lecture N=20 off by 10", (8 * 2**20) / 840e3, 10, 0.01),
    ("4C lecture N=40 off by 10", (8 * 2**40) / 880e9, 10, 0.01),
    ("4C double N=50 PB", 16 * 2**50 / 1e15, 18, 0.01),
    ("4C x1024 per ten", 2**10, 1024, 0),
    # 4D
    ("4D shots for 0.01", 1 / 0.01**2, 1e4, 1e-9),
    ("4D 3^50 settings", 3**50, 7.2e23, 0.01),
    # 4F counting
    ("4F Li-6", 3 + 3 + 3, 9, 0),
    ("4F Li-7", 3 + 4 + 3, 10, 0),
    ("4F Rb-87", 37 + 50 + 37, 124, 0),
    ("4F Na-23", 11 + 12 + 11, 34, 0),
    ("4F K-40", 19 + 21 + 19, 59, 0),
    # 4G BEC
    ("4G Rb mass kg", m_rb, 1.44e-25, 0.01),
    ("4G lambda_T Rb 100 nK um", lam_rb * 1e6, 0.59, 0.01),
    ("4G critical density Rb", nc_rb, 1.3e19, 0.05),
    ("4G spacing at n_c um", nc_rb ** (-1 / 3) * 1e6, 0.43, 0.01),
    ("4G air density", n_air, 2.5e25, 0.01),
    ("4G T_c at air/1e6 nK", T_c(m_rb, n_gas) * 1e9, 160, 0.03),
    # 4H lattice
    ("4H spacing 813 nm", 813 / 2, 406.5, 0),
    ("4H E_r/h Rb 813 kHz", h / (2 * m_rb * 813e-9**2) / 1e3, 3.5, 0.02),
    ("4H J(5)/J(20)", J_over_Er(5) / J_over_Er(20), 31, 0.02),
    # 4I
    ("4I (U/J)_c mean field 5.83z, z=6", 5.83 * 6, 35, 0.001),
    # 4K
    ("4K initial P_upup", (1 / sqrt(2)) ** 4, 0.25, 1e-9),
    ("4K final P_upup", (1 / sqrt(2)) ** 2, 0.5, 1e-9),
    ("4K frustration high energy", max(frust), 3, 0),
    ("4K frustration low energy", min(frust), -1, 0),
    ("4K frustration degeneracy", frust.count(-1), 6, 0),
    # 4L temperatures
    ("4L -269 C in K", -269 + 273.15, 4, 0.05),
    ("4L -196 C in K", -196 + 273.15, 77, 0.01),
    ("4L -183 C in K", -183 + 273.15, 90, 0.01),
    # C5.1
    ("C5.1 3^10", 3**10, 59049, 0),
    ("C5.1 N=10 bytes", 16 * 3**10, 944784, 0),
    ("C5.1 3^20", 3**20, 3.49e9, 0.01),
    ("C5.1 N=20 GB", 16 * 3**20 / 1e9, 56, 0.01),
    ("C5.1 3^30", 3**30, 2.06e14, 0.01),
    ("C5.1 N=30 PB", 16 * 3**30 / 1e15, 3.3, 0.01),
    ("C5.1 budget amplitudes", 1e12 / 16, 6.25e10, 1e-9),
    ("C5.1 spin-1 N max (real)", log(1e12 / 16) / log(3), 22.6, 0.01),
    ("C5.1 spin-1 N max", int(log(1e12 / 16) / log(3)), 22, 0),
    ("C5.1 spin-half N max (real)", log(1e12 / 16) / log(2), 35.9, 0.01),
    ("C5.1 spin-half N max", int(log(1e12 / 16) / log(2)), 35, 0),
    ("C5.1 dense H N=10 GB", 16 * (3**10) ** 2 / 1e9, 56, 0.01),
    ("C5.1 ratio N=20", 16 * 3**20 / (8 * 2**20), 6.7e3, 0.01),
    ("C5.1 3^10 factor", 3**10, 5.9e4, 0.01),
    ("C5.1 particles earlier", int(log(1e12 / 16) / log(2)) - int(log(1e12 / 16) / log(3)), 13, 0),
    # C5.2
    ("C5.2 K-41 mass", m_k41, 6.81e-26, 0.01),
    ("C5.2 K-41 count", 19 + 22 + 19, 60, 0),
    ("C5.2 K-40 count", 19 + 21 + 19, 59, 0),
    ("C5.2 lambda_T m", lam_k, 5.0e-7, 0.01),
    ("C5.2 n_c", 2.612 / lam_k**3, 2.1e19, 0.02),
    ("C5.2 n lambda^3", 5e19 * lam_k**3, 6.2, 0.01),
    ("C5.2 T_c nK", T_c(m_k41, 5e19) * 1e9, 530, 0.01),
    # C5.3
    ("C5.3 K-39 mass", m_k39, 6.47e-26, 0.01),
    ("C5.3 K-39 count", 19 + 20 + 19, 58, 0),
    ("C5.3 spacing nm", d_l * 1e9, 775, 0),
    ("C5.3 E_r/h Hz", Er_k39, 2.1e3, 0.02),
    ("C5.3 J/h s=6", J_k39(6), 137, 0.01),
    ("C5.3 J/h s=14", J_k39(14), 19.6, 0.01),
    ("C5.3 J/h s=20", J_k39(20), 5.9, 0.01),
    ("C5.3 U/h s=6", U_k39(6), 264, 0.01),
    ("C5.3 U/h s=14", U_k39(14), 499, 0.01),
    ("C5.3 U/h s=20", U_k39(20), 652, 0.01),
    ("C5.3 U/J 6", 264 / 137, 1.9, 0.02),
    ("C5.3 U/J 14", 499 / 19.6, 25.5, 0.01),
    ("C5.3 U/J 20", 652 / 5.9, 110, 0.01),
    ("C5.3 no ratio in [29, 35]", sum(29 <= r <= 35 for r in (264 / 137, 499 / 19.6, 652 / 5.9)), 0, 0),
    ("C5.3 h/(md) m/s", v_peak, 1.32e-2, 0.01),
    ("C5.3 h/(md) = 2 hbar k/m", 2 * hbar * k_l / m_k39, v_peak, 1e-9),
    ("C5.3 distance m", v_peak * 0.020, 2.6e-4, 0.02),
    ("C5.3 distance mm", v_peak * 0.020 * 1e3, 0.26, 0.02),
    ("C5.3 J drop 6->20", 137 / 5.9, 23, 0.02),
    ("C5.3 U rise 6->20", 652 / 264, 2.5, 0.02),
    # C5.4 (writing, fictional/hypothetical figures)
    ("C5.4 C(128,64)", conf, 2.4e37, 0.01),
    ("C5.4 bytes", 8 * conf, 1.9e38, 0.01),
    ("C5.4 ratio to 10 PB", 8 * conf / 1e16, 2e22, 0.05),
    ("C5.4 1% of 40 M GBP (M)", 0.01 * 40, 0.4, 1e-9),
    ("C5.4 partnership total GBP", 3 * 120000, 360000, 0),
    ("C5.4 spend fraction %", 360000 / 40e6 * 100, 0.9, 1e-9),
    # C5.5
    ("C5.5 2^46", 2**46, 7.04e13, 0.01),
    ("C5.5 single bytes", 8 * 2**46, 5.6e14, 0.01),
    ("C5.5 single TB", 8 * 2**46 / 1e12, 563, 0.01),
    ("C5.5 double bytes", 16 * 2**46, 1.13e15, 0.01),
    ("C5.5 double TB", 16 * 2**46 / 1e12, 1126, 0.01),
    ("C5.5 double PB", 16 * 2**46 / 1e15, 1.1, 0.03),
    ("C5.5 sweep s", 2**46 / 1e11, 704, 0.01),
    ("C5.5 1000 steps s", 1000 * 2**46 / 1e11, 7.0e5, 0.01),
    ("C5.5 1000 steps days", 1000 * 2**46 / 1e11 / 86400, 8.1, 0.01),
    ("C5.5 runs", 1 / 0.02**2, 2500, 1e-9),
    ("C5.5 run time s", (1 / 0.02**2) / 5, 500, 1e-9),
    ("C5.5 N=47 single PB", 8 * 2**47 / 1e15, 1.1, 0.03),
    ("C5.5 N=47 days", 1000 * 2**47 / 1e11 / 86400, 16, 0.02),
    ("C5.5 check 8.8 TB x 64", 8.8 * 2**6, 563, 0.01),
    ("C5.5 check 9000 TB / 16", 9000 / 2**4, 563, 0.01),
]
