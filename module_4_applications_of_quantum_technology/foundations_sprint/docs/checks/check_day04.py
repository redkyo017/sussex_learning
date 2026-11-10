"""Numeric answers stated in content/day04.md (Interferometry -> atom interferometry).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
"""
import math

# Constants (SI, CODATA exact or standard)
h = 6.62607015e-34
hbar = h / (2 * math.pi)
c = 299792458.0
u = 1.66053906660e-27
G = 6.674e-11
g = 9.81
GAL = 1e-2                 # 1 Gal = 1e-2 m/s^2
UGAL = 1e-6 * GAL          # 1 uGal = 1e-8 m/s^2

m_rb = 86.909180527 * u    # Rb-87
m_cs = 132.905451933 * u   # Cs-133

# ---------- Core concepts: worked clones ----------
# M6.1 Mach-Zehnder, 633 nm, L = 2 cm, dn = 3e-5
phi_mz = 3e-5 * (2 * math.pi / 633e-9) * 0.02
# M6.2 de Broglie for Rb-87
ldb_rb_300 = h / (m_rb * 300)
ldb_rb_cold = h / (m_rb * 0.01)
# M7.1 recoil, Rb-87, 780 nm
k_rb = 2 * math.pi / 780e-9
v_rec_rb = hbar * k_rb / m_rb
keff_rb = 4 * math.pi / 780e-9
# M7.3 phase, Rb, T = 0.1 s
Phi_rb = keff_rb * g * 0.1**2
sep_rb = 2 * v_rec_rb * 0.1
# M7.4 chirp null, Rb
alpha_rb = keff_rb * g / (2 * math.pi)
# M7.5 shot-noise sensitivity, Rb, N = 1e6, T = 0.1 s
dg_rb = (1 / math.sqrt(1e6)) / (keff_rb * 0.1**2)
# lecture check: 20 uGal/sqrtHz averaged 60 s; time to reach 5 uGal
avg60 = 20 / math.sqrt(60)
t5 = (20 / 5) ** 2
# M7.6 ground vs space
gain_01 = (10 / 0.1) ** 2
gain_03 = (10 / 0.3) ** 2
# M7.7 Sagnac ratio, Rb
h_over_m_rb = h / m_rb
sag_rb = 780e-9 * c / h_over_m_rb
area_pen = 1e3 / 1e-4
flux_pen = math.sqrt(1e19 / 1e7)
resp_after_area = sag_rb / area_pen
# M7.8 units and lecture numbers
ugal_in_g = UGAL / g
cc_5ugal_g = 5 * UGAL / g          # 5 uGal/sqrtHz as a fraction of g
cc_5e8_ugal = 5e-8 * g / UGAL      # 5e-8 g/sqrtHz in uGal/sqrtHz

CHECKS = [
    ("M6.1 MZ phase 633nm 2cm dn=3e-5 (rad)", phi_mz, 5.96, 0.01),
    ("M6.1 k at 633 nm (1/m)", 2 * math.pi / 633e-9, 9.93e6, 0.01),
    ("M6.1 MZ output fraction cos^2(phi/2)", math.cos(phi_mz / 2) ** 2, 0.97, 0.01),
    ("M6.2 lambda_dB Rb 300 m/s (m)", ldb_rb_300, 1.5e-11, 0.03),
    ("M6.2 lambda_dB Rb 1 cm/s (m)", ldb_rb_cold, 4.6e-7, 0.02),
    ("M7.1 k Rb 780nm (1/m)", k_rb, 8.06e6, 0.01),
    ("M7.1 recoil velocity Rb (m/s)", v_rec_rb, 5.9e-3, 0.01),
    ("M7.1 k_eff Rb (1/m)", keff_rb, 1.61e7, 0.01),
    ("M7.1 two-photon kick Rb (m/s)", 2 * v_rec_rb, 11.8e-3, 0.01),
    ("M7.3 Phi Rb T=0.1 s (rad)", Phi_rb, 1.58e6, 0.01),
    ("M7.3 fringes Phi/2pi Rb (quarter million)", Phi_rb / (2 * math.pi), 2.5e5, 0.02),
    ("M7.3 arm separation Rb T=0.1 s (m)", sep_rb, 1.18e-3, 0.01),
    ("M7.4 lecture convention factor (2T)^2/T^2", (2 * 0.1) ** 2 / 0.1**2, 4, 1e-9),
    ("M7.4 chirp null Rb (Hz/s)", alpha_rb, 25.2e6, 0.01),
    ("M7.5 shot-noise dg Rb N=1e6 T=0.1 (m/s^2)", dg_rb, 6.2e-9, 0.01),
    ("M7.5 shot-noise dg Rb in uGal", dg_rb / UGAL, 0.62, 0.01),
    ("M7.5 lecture 20 uGal/rtHz after 60 s (uGal)", avg60, 2.6, 0.01),
    ("M7.5 time to 5 uGal at 20 uGal/rtHz (s)", t5, 16, 1e-9),
    ("M7.6 T^2 gain 10 s vs 0.1 s", gain_01, 1e4, 1e-9),
    ("M7.6 T^2 gain 10 s vs 0.3 s", gain_03, 1.1e3, 0.02),
    ("M7.7 h/m Rb (m^2/s)", h_over_m_rb, 4.6e-9, 0.01),
    ("M7.7 Sagnac ratio Rb m*lambda*c/h", sag_rb, 5.1e10, 0.01),
    ("M7.7 area penalty", area_pen, 1e7, 1e-9),
    ("M7.7 response after area", resp_after_area, 5.1e3, 0.01),
    ("M7.7 sqrt flux penalty", flux_pen, 1e6, 1e-9),
    ("M7.7 net shot-noise ratio after area and flux", resp_after_area / flux_pen, 5.1e-3, 0.01),
    ("M7.8 1 uGal as fraction of g", ugal_in_g, 1.02e-9, 0.01),
    ("M7.8 atom 20 uGal/rtHz as g/rtHz", 20 * UGAL / g, 2e-8, 0.03),
    ("M7.8 corner cube 5 uGal/rtHz as g/rtHz", cc_5ugal_g, 5.1e-9, 0.01),
    ("M7.8 corner cube 5e-8 g/rtHz in uGal/rtHz", cc_5e8_ugal, 49, 0.01),
]

# ---------- Exercises ----------
# 4.1 MZ, 1550 nm, L = 5 cm
dn_dark = 1550e-9 / (2 * 0.05)
phi_41 = 5e-6 * (2 * math.pi / 1550e-9) * 0.05
CHECKS += [
    ("4.1 dn for first dark fringe", dn_dark, 1.55e-5, 0.01),
    ("4.1 phase at dn=5e-6 (rad)", phi_41, 1.01, 0.01),
    ("4.1 output fraction", math.cos(phi_41 / 2) ** 2, 0.76, 0.01),
]

# 4.2 Cs-133 recoil and de Broglie
k_cs = 2 * math.pi / 852e-9
v_rec_cs = hbar * k_cs / m_cs
CHECKS += [
    ("4.2 k Cs 852nm (1/m)", k_cs, 7.37e6, 0.01),
    ("4.2 recoil velocity Cs (m/s)", v_rec_cs, 3.5e-3, 0.01),
    ("4.2 two-photon kick Cs (m/s)", 2 * v_rec_cs, 7.0e-3, 0.01),
    ("4.2 lambda_dB Cs 200 m/s (m)", h / (m_cs * 200), 1.5e-11, 0.01),
    ("4.2 lambda_dB Cs 2 cm/s (m)", h / (m_cs * 0.02), 1.5e-7, 0.01),
]

# 4.3 Phi for Cs, T = 0.2 s
keff_cs = 4 * math.pi / 852e-9
Phi_cs = keff_cs * g * 0.2**2
CHECKS += [
    ("4.3 k_eff Cs (1/m)", keff_cs, 1.47e7, 0.01),
    ("4.3 Phi Cs T=0.2 (rad)", Phi_cs, 5.79e6, 0.01),
    ("4.3 fringes Phi/2pi", Phi_cs / (2 * math.pi), 9.2e5, 0.01),
    ("4.3 lecture-convention Phi (rad)", keff_cs * g * (2 * 0.2) ** 2, 2.32e7, 0.01),
    ("4.3 arm separation at T (m)", 2 * v_rec_cs * 0.2, 1.4e-3, 0.01),
    ("4.3 z(0)-2z(T)+z(2T) for T=0.2 (m)", 0 - 2 * (0.3 * 0.2 - 0.5 * g * 0.2**2) + (0.3 * 0.4 - 0.5 * g * 0.4**2), -0.392, 0.01),
]

# 4.4 chirp null, Cs
alpha_cs = keff_cs * g / (2 * math.pi)
dg_per_hz = 2 * math.pi * 1.0 / keff_cs
CHECKS += [
    ("4.4 chirp null Cs (Hz/s)", alpha_cs, 23.0e6, 0.01),
    ("4.4 lambda/2 = 2pi/k_eff (m)", 2 * math.pi / keff_cs, 426e-9, 0.01),
    ("4.4 dg per 1 Hz/s (m/s^2)", dg_per_hz, 4.26e-7, 0.01),
    ("4.4 dg per 1 Hz/s (uGal)", dg_per_hz / UGAL, 42.6, 0.01),
    ("4.4 dg per 0.01 Hz/s (uGal)", 0.01 * dg_per_hz / UGAL, 0.43, 0.01),
]

# 4.5 shot-noise sensitivity, Cs, N = 4e5, T = 0.15 s, cycle 0.8 s
dphi_45 = 1 / math.sqrt(4e5)
dg_45 = dphi_45 / (keff_cs * 0.15**2)
dens_45 = dg_45 * math.sqrt(0.8)
CHECKS += [
    ("4.5 dphi per shot (rad)", dphi_45, 1.58e-3, 0.01),
    ("4.5 dg per shot (m/s^2)", dg_45, 4.8e-9, 0.01),
    ("4.5 dg per shot (uGal)", dg_45 / UGAL, 0.48, 0.01),
    ("4.5 noise density (uGal/rtHz)", dens_45 / UGAL, 0.43, 0.01),
    ("4.5 time to 0.1 uGal (s)", (dens_45 / UGAL / 0.1) ** 2, 18, 0.02),
    ("4.5 ratio measured 20 uGal/rtHz to shot limit", 20 / (dens_45 / UGAL), 47, 0.02),
]

# 4.6 ground vs space
CHECKS += [
    ("4.6 T^2 gain 8 s vs 0.25 s", (8 / 0.25) ** 2, 1024, 1e-9),
    ("4.6 drop distance 2gT^2 at T=0.25 (m)", 2 * g * 0.25**2, 1.23, 0.01),
    ("4.6 atom-number factor (T ratio)^4", (8 / 0.25) ** 4, 1.05e6, 0.01),
    ("4.6 drop distance at T=8 s (m)", 2 * g * 8**2, 1256, 0.01),
    ("4.6 fountain apex 0.5 g T^2 at T=0.25 (m)", 0.5 * g * 0.25**2, 0.31, 0.02),
    ("4.6 fountain apex at T=8 s (m)", 0.5 * g * 8**2, 314, 0.01),
    ("4.6 drop / fountain height ratio", (0.5 * g * (2 * 0.25) ** 2) / (g * (2 * 0.25) ** 2 / 8), 4, 1e-9),
]

# 4.7 Sagnac ratio, Cs (stretch)
h_over_m_cs = h / m_cs
sag_cs = 852e-9 * c / h_over_m_cs
resp_47 = sag_cs * 2e-4 / 500
flux_47 = math.sqrt(1e18 / 5e6)
CHECKS += [
    ("4.7 h/m Cs (m^2/s)", h_over_m_cs, 3.0e-9, 0.01),
    ("4.7 Sagnac ratio Cs", sag_cs, 8.5e10, 0.01),
    ("4.7 area factor 500/2e-4", 500 / 2e-4, 2.5e6, 1e-9),
    ("4.7 response after area", resp_47, 3.4e4, 0.01),
    ("4.7 sqrt flux factor", flux_47, 4.5e5, 0.01),
    ("4.7 net shot-noise ratio", resp_47 / flux_47, 0.076, 0.02),
    ("4.7 light ahead by factor", flux_47 / resp_47, 13, 0.02),
    ("4.7 lecture thermal-beam gyro (rad/s/rtHz, L151)", 6e-10, 6e-10, 1e-9),
]

# 4.8 classical gravimeters, units, void signal
s04 = 0.4**2 / (4 * math.pi**2)
s4 = 4.0**2 / (4 * math.pi**2)
void = 4 / 3 * math.pi * G * 1900 * 1.5**3 / 6.0**2
CHECKS += [
    ("4.8 spring stretch per 10 uGal, T=0.4 s (m)", s04 * 10 * UGAL, 4.1e-10, 0.02),
    ("4.8 spring stretch per 10 uGal, T=4 s (m)", s4 * 10 * UGAL, 4.1e-8, 0.02),
    ("4.8 ratio of the two", s4 / s04, 100, 1e-9),
    ("4.8 dg_min ratio at fixed dL_min (falls 100x)", (4 * math.pi**2 / 0.4**2) / (4 * math.pi**2 / 4.0**2), 100, 1e-9),
    ("4.8 gradient 25 E over 0.5 m (uGal)", 25e-9 * 0.5 / UGAL, 1.25, 1e-9),
    ("4.8 3e-8 g in uGal", 3e-8 * g / UGAL, 29, 0.02),
    ("4.8 void peak signal (m/s^2)", void, 5.0e-8, 0.01),
    ("4.8 void peak signal (uGal)", void / UGAL, 5.0, 0.01),
]

# 4.9 / 4.10 writing: figures inside the model paragraphs
# 4.10: fact sheet only (fictional): 5 uGal target, 150 stations, spring 8 uGal/rtHz 30 uGal/day 14 kg,
# atom 30 uGal/rtHz 110 kg. Change between two surveys at SNR 3.
sig_410 = 5 / (3 * math.sqrt(2))
t_atom_410 = (30 / sig_410) ** 2
t_spring_410 = (8 / sig_410) ** 2
CHECKS += [
    ("4.9 spring 8 uGal/rtHz after 60 s (uGal)", 8 / math.sqrt(60), 1.0, 0.04),
    ("4.9 spring drift per hour (uGal)", 30 / 24, 1.25, 1e-9),
    ("4.9 hourly drift / 5 uGal signal (a quarter)", (30 / 24) / 5, 0.25, 1e-9),
    ("4.9 atom 30 uGal/rtHz after 60 s (uGal)", 30 / math.sqrt(60), 3.9, 0.01),
    ("4.9 SNR on void after 60 s, atom", 5 / (30 / math.sqrt(60)), 1.3, 0.01),
    ("4.10 per-survey sigma for 5 uGal change at SNR 3 (uGal)", sig_410, 1.2, 0.02),
    ("4.10 spring time per station (s)", t_spring_410, 46, 0.01),
    ("4.10 spring 150 stations (h, 'under 2')", 150 * t_spring_410 / 3600, 1.92, 0.01),
    ("4.10 spring drift over a year (uGal)", 30 * 365, 1.1e4, 0.01),
    ("4.10 year drift / signal ('over 2,000')", 30 * 365 / 5, 2190, 0.01),
    ("4.10 atom time per station (s)", t_atom_410, 648, 0.01),
    ("4.10 atom time per station (min)", t_atom_410 / 60, 10.8, 0.01),
    ("4.10 atom 150 stations (h)", 150 * t_atom_410 / 3600, 27, 0.01),
    ("4.10 mass ratio 110/14 ('nearly 8')", 110 / 14, 7.9, 0.01),
    ("4.10 atom 20 stations (h)", 20 * t_atom_410 / 3600, 3.6, 0.01),
    ("4.10 noise ratio atom/spring ('about 4')", 30 / 8, 3.75, 0.01),
]

# ---------- Spaced review answers ----------
CHECKS += [
    ("SR Day03 Q ratio 429 THz / 9.19 GHz", 429e12 / 9.19e9, 4.7e4, 0.01),
    ("SR Day03 flux quantum h/2e (Wb)", h / (2 * 1.602176634e-19), 2.07e-15, 0.01),
    ("SR Day02 30 uGal/rtHz over 100 s (uGal)", 30 / math.sqrt(100), 3, 1e-9),
    ("SR Day02 shot noise N=1e4 (rad)", 1 / math.sqrt(1e4), 1e-2, 1e-9),
    ("SR Day02 Heisenberg N=1e4 (rad)", 1 / 1e4, 1e-4, 1e-9),
    ("SR Day01 1 uGal in m/s^2", UGAL, 1e-8, 1e-9),
]
