"""Numeric checks for content/companions/week03_companion.md (sections 4-6).
Each tuple: (label, computed, stated, rel_tol)."""
from math import pi, sqrt, sin

h = 6.62607015e-34
hbar = h / (2 * pi)
u = 1.66053907e-27
c = 2.99792458e8
g = 9.81
uGal = 1e-8

# ---- section 4 (lecture decode, Rb-87 at 780 nm as the typical case) ----
m_rb = 86.909184 * u
k_rb = 2 * pi / 780e-9
keff_rb = 2 * k_rb
T_l = 0.16
scale_rb = keff_rb * T_l**2
vr_rb = hbar * keff_rb / m_rb
hm_rb = h / m_rb
lc_rb = 780e-9 * c
sag_rb = lc_rb / hm_rb
shot_rb = 1e-3 / scale_rb

# ---- section 5-6 (clones) ----
m_cs = 132.905452 * u
k_cs = 2 * pi / 852e-9
keff_cs = 2 * k_cs
T_cs = 0.085
scale_cs = keff_cs * T_cs**2
dphi_c2 = 1 / sqrt(4e5)
shot_c2 = dphi_c2 / scale_cs
hm_cs = h / m_cs
lc_cs = 852e-9 * c
sag_cs = lc_cs / hm_cs
k_k = 2 * pi / 767e-9
keff_k = 2 * k_k

CHECKS = [
    # 4B Rabi
    ("4B pi/2 pulse P_b", sin(pi / 4) ** 2, 0.5, 0.01),
    ("4B pi pulse P_b", sin(pi / 2) ** 2, 1.0, 0.01),
    # 4C recoil
    ("4C k Rb 780", k_rb, 8.06e6, 0.01),
    ("4C k_eff Rb", keff_rb, 1.61e7, 0.01),
    ("4C two-photon kick velocity mm/s", vr_rb * 1e3, 11.8, 0.01),
    ("4C single-photon recoil mm/s", hbar * k_rb / m_rb * 1e3, 5.9, 0.01),
    ("4C arm separation mm at 160 ms", vr_rb * T_l * 1e3, 1.9, 0.02),
    # 4D chirp
    ("4D alpha Rb Hz/s", keff_rb * g / (2 * pi), 2.52e7, 0.01),
    # 4E Phi
    ("4E second difference coefficient of g", (0 - 2 * (-0.5) + (-0.5 * 4)), -1.0, 1e-9),
    ("4E scale factor k_eff T^2", scale_rb, 4.12e5, 0.01),
    ("4E Phi total rad", keff_rb * g * T_l**2, 4.05e6, 0.01),
    ("4E lecture tau=2T convention rad", keff_rb * g * (2 * T_l) ** 2, 1.62e7, 0.01),
    # 4G Sagnac area identity: 4 pi m A / h with A = L hbar keff T / m equals 2 keff L T (per unit Omega)
    ("4G area identity", 4 * pi * m_rb * (1.0 * hbar * keff_rb * 1.0 / m_rb) / h, 2 * keff_rb, 1e-9),
    # 4H Sagnac ratio
    ("4H h/m Rb", hm_rb, 4.59e-9, 0.01),
    ("4H lambda c", lc_rb, 234, 0.01),
    ("4H ideal ratio", sag_rb, 5.1e10, 0.02),
    ("4H after area 1e7", sag_rb / (1e3 / 1e-4), 5.1e3, 0.02),
    ("4H flux penalty", sqrt(1e19 / 1e7), 1e6, 0.01),
    ("4H after flux", sag_rb / 1e7 / 1e6, 5e-3, 0.05),
    ("4H lecture thermal-beam gyro rad/s/rtHz (L151)", 6e-10, 6e-10, 1e-9),
    # 4I resolution
    ("4I shot-noise phase N=1e6", 1 / sqrt(1e6), 1e-3, 0.01),
    ("4I per-shot dg m/s^2", shot_rb, 2.4e-9, 0.02),
    ("4I per-shot dg uGal", shot_rb / uGal, 0.24, 0.02),
    ("4I density uGal/rtHz", shot_rb * sqrt(1.5) / uGal, 0.30, 0.02),
    ("4I measured/floor ratio", 20 / (shot_rb * sqrt(1.5) / uGal), 70, 0.05),
    ("4I 20 uGal/rtHz after 60 s", 20 / sqrt(60), 2.6, 0.01),
    ("4I time to 5 uGal s", (20 / 5) ** 2, 16, 0.01),
    # 4J noise figures
    ("4J L139 corner cube uGal/rtHz", 5e-8 * g / uGal, 49, 0.01),
    ("4J sqrt(15)", sqrt(15), 3.9, 0.01),
    ("4J 5*sqrt(15)", 5 * sqrt(15), 19, 0.03),
    ("4J spring L135 uGal/rtHz", 5e-9 * g / uGal, 4.9, 0.01),
    ("4J superconducting uGal/rtHz", 1e-12 * g / uGal, 0.001, 0.02),
    # 4K spring
    ("4K dL/dg at T=1 s", 1 / (4 * pi**2), 0.025, 0.02),
    ("4K stretch for 1 uGal m", uGal / (4 * pi**2), 2.5e-10, 0.02),
    # 4L T^2 gain
    ("4L ground vs space gain", (10 / 0.3) ** 2, 1.1e3, 0.02),
    ("4L apex T=0.3 s m", 0.5 * g * 0.3**2, 0.44, 0.01),
    ("4L apex T=10 s m", 0.5 * g * 10**2, 490, 0.01),
    ("4L 10 m tower T s", sqrt(2 * 10 / g), 1.43, 0.01),
    # 4M
    ("4M gradiometer E/rtHz", 4e-9 * g / 1e-9, 39, 0.01),
    ("4M gradiometer s^-2/rtHz", 4e-9 * g, 3.9e-8, 0.01),
    ("4M 1e-9 g in uGal", 1e-9 * g / uGal, 1.0, 0.02),
    # C3.1
    ("C3.1 k Cs", k_cs, 7.37e6, 0.01),
    ("C3.1 k_eff Cs", keff_cs, 1.47e7, 0.01),
    ("C3.1 T^2", T_cs**2, 7.225e-3, 0.001),
    ("C3.1 scale factor", scale_cs, 1.07e5, 0.01),
    ("C3.1 Phi", scale_cs * g, 1.05e6, 0.01),
    ("C3.1 dPhi 50 uGal rad", scale_cs * 50 * uGal, 0.053, 0.01),
    ("C3.1 alpha Hz/s", keff_cs * g / (2 * pi), 2.30e7, 0.01),
    ("C3.1 tau=2T Phi", 4 * scale_cs * g, 4.18e6, 0.01),
    ("C3.1 Rb/Cs phase ratio ~4", (keff_rb * g * T_l**2) / (scale_cs * g), 4, 0.05),
    # C3.2
    ("C3.2 dPhi", dphi_c2, 1.58e-3, 0.01),
    ("C3.2 per-shot m/s^2", shot_c2, 1.48e-8, 0.01),
    ("C3.2 density uGal/rtHz", shot_c2 * sqrt(0.5) / uGal, 1.05, 0.01),
    ("C3.2 atom time to 5 uGal s", (40 / 5) ** 2, 64, 0.01),
    ("C3.2 spring time to 5 uGal s", (6 / 5) ** 2, 1.44, 0.01),
    ("C3.2 drift per hour", 15 / 24, 0.625, 0.01),
    ("C3.2 drift hours to 5 uGal", 5 / (15 / 24), 8, 0.01),
    ("C3.2 field/floor ratio", 40 / (shot_c2 * sqrt(0.5) / uGal), 38, 0.02),
    # C3.3
    ("C3.3 Cs mass kg", m_cs, 2.21e-25, 0.01),
    ("C3.3 h/m Cs", hm_cs, 3.00e-9, 0.01),
    ("C3.3 lambda c", lc_cs, 255, 0.01),
    ("C3.3 ideal ratio", sag_cs, 8.5e10, 0.01),
    ("C3.3 area ratio", 200 / 5e-5, 4e6, 0.01),
    ("C3.3 after area", sag_cs / 4e6, 2.1e4, 0.02),
    ("C3.3 flux penalty", sqrt(1e18 / 1e8), 1e5, 0.01),
    ("C3.3 after flux", sag_cs / 4e6 / 1e5, 0.21, 0.02),
    # C3.4 (fact-sheet figures, fictional; 7 h day and set-up times are exercise assumptions)
    ("C3.4 atom time per station to 2 uGal s", (30 / 2) ** 2, 225, 0.01),
    ("C3.4 spring time per station to 2 uGal s", (8 / 2) ** 2, 16, 0.01),
    ("C3.4 spring stations per day", 7 * 3600 / ((8 / 2) ** 2 + 300), 79, 0.02),
    ("C3.4 spring days for 150 stations", 150 / (7 * 3600 / ((8 / 2) ** 2 + 300)), 2, 0.07),
    ("C3.4 drift over 2 h uGal", 30 / 24 * 2, 2.5, 0.01),
    ("C3.4 max loop time for 2 uGal drift h", 2 / (30 / 24), 1.6, 0.01),
    ("C3.4 spring drift per month uGal", 30 * 30, 900, 0.01),
    ("C3.4 atom stations per day", 7 * 3600 / ((30 / 2) ** 2 + 900), 22, 0.02),
    ("C3.4 atom days for 150 stations", 150 / (7 * 3600 / ((30 / 2) ** 2 + 900)), 7, 0.05),
    # C3.5 cold attempt
    ("C3.5 k K", k_k, 8.19e6, 0.01),
    ("C3.5 k_eff K", keff_k, 1.64e7, 0.01),
    ("C3.5 scale ground", keff_k * 0.2**2, 6.55e5, 0.01),
    ("C3.5 scale microgravity", keff_k * 4**2, 2.62e8, 0.01),
    ("C3.5 gain", (4 / 0.2) ** 2, 400, 0.01),
    ("C3.5 fountain height m", 0.5 * g * 4**2, 78.5, 0.01),
    ("C3.5 phase ground rad", keff_k * 0.2**2 * 1e-9 * g, 6.4e-3, 0.01),
    ("C3.5 phase microgravity rad", keff_k * 4**2 * 1e-9 * g, 2.57, 0.01),
    ("C3.5 cycle ratio", 4 / 0.2, 20, 0.01),
]
