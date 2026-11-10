"""Numeric answers stated in content/day05.md (Sensing checkpoint).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
"""
import math

h = 6.62607015e-34
e = 1.602176634e-19
c = 299792458.0
g = 9.81
DAY = 86400.0
YEAR = 3.156e7
UGAL = 1e-8                # m/s^2
GAMMA_RB = 7.0             # Hz/nT
GAMMA_E = 28.0             # MHz/mT
D_NV = 2870.0              # MHz
PHI0 = h / (2 * e)

CHECKS = []

# 5.1 conversions
CHECKS += [
    ("5.1a 0.4 nT in fT", 0.4e-9 / 1e-15, 4e5, 1e-9),
    ("5.1b 35 uGal in m/s^2", 35 * UGAL, 3.5e-7, 1e-9),
    ("5.1b 35 uGal as fraction of g", 35 * UGAL / g, 3.6e-8, 0.02),
    ("5.1c 12 E x 0.8 m (m/s^2)", 12e-9 * 0.8, 9.6e-9, 1e-9),
    ("5.1c 12 E x 0.8 m (uGal)", 12e-9 * 0.8 / UGAL, 0.96, 1e-9),
    ("5.1d 7e-8 g in m/s^2", 7e-8 * g, 6.87e-7, 0.01),
    ("5.1d 7e-8 g in uGal", 7e-8 * g / UGAL, 69, 0.01),
]

# 5.2 noise density
df52 = (10 / 60) ** 2
CHECKS += [
    ("5.2a 60 fT/rtHz in 9 Hz (fT)", 60 * math.sqrt(9), 180, 1e-9),
    ("5.2b allowed bandwidth (Hz)", df52, 0.0278, 0.01),
    ("5.2c averaging time (s)", 1 / (2 * df52), 18, 1e-9),
    ("5.2 check bandwidth ratio 18^2", 18**2, 324, 1e-9),
]

# 5.3 Allan table
CHECKS += [
    ("5.3a slope 1-100 s", math.log10(6.0e-14 / 6.0e-13) / math.log10(100), -0.5, 1e-9),
    ("5.3 table 10 s white-noise value", 6.0e-13 / math.sqrt(10), 1.9e-13, 0.01),
    ("5.3b time to 3e-14 (s)", (6.0e-13 / 3e-14) ** 2, 400, 1e-9),
    ("5.3b white-noise value at 1000 s", 6.0e-13 / math.sqrt(1000), 1.9e-14, 0.01),
    ("5.3e time wander at floor (s)", 1.5e-14 * 1e4, 1.5e-10, 1e-9),
    ("5.3d 1e5 s is about a day (days)", 1e5 / DAY, 1.16, 0.01),
    ("5.3 1e4 s in hours (about 3 h)", 1e4 / 3600, 2.8, 0.01),
]

# 5.4 SQL vs Heisenberg
N54 = 6.4e5
CHECKS += [
    ("5.4a sqrt N", math.sqrt(N54), 800, 1e-9),
    ("5.4a SQL (rad)", 1 / math.sqrt(N54), 1.25e-3, 1e-9),
    ("5.4a Heisenberg (rad)", 1 / N54, 1.56e-6, 0.01),
    ("5.4b atoms for 2.5e-4 rad", 1 / 2.5e-4**2, 1.6e7, 1e-9),
    ("5.4c cycles for 1.25e-4 rad", (1.25e-3 / 1.25e-4) ** 2, 100, 1e-9),
    ("5.4 check 800 x HL = SQL", 800 * 1.5625e-6, 1.25e-3, 1e-9),
]

# 5.5 clocks
nu_opt = 1.0648e15
nu_h = 1.4204e9
tau55 = 30 * DAY
dt55 = 3e-17 * tau55
CHECKS += [
    ("5.5a E optical (J)", h * nu_opt, 7.06e-19, 0.01),
    ("5.5a E optical (eV)", h * nu_opt / e, 4.40, 0.01),
    ("5.5a wavelength (nm)", c / nu_opt * 1e9, 282, 0.01),
    ("5.5b Q optical", nu_opt / 0.5, 2.13e15, 0.01),
    ("5.5b Q maser", nu_h / 0.5, 2.84e9, 0.01),
    ("5.5b Q ratio", nu_opt / nu_h, 7.5e5, 0.01),
    ("5.5c Ramsey T for 0.5 Hz (s)", 1 / (2 * 0.5), 1, 1e-9),
    ("5.5d 30 days in s", tau55, 2.592e6, 1e-9),
    ("5.5d time error (s)", dt55, 7.8e-11, 0.01),
    ("5.5d distance (m)", c * dt55, 0.023, 0.02),
]

# 5.6 magnetometers
S56 = 2e-3 * 2e-3
CHECKS += [
    ("5.6b Larmor 44 uT (Hz)", GAMMA_RB * 44000, 308e3, 1e-9),
    ("5.6b shift 15 nT (Hz)", GAMMA_RB * 15, 105, 1e-9),
    ("5.6c Phi0 (Wb)", PHI0, 2.07e-15, 0.01),
    ("5.6c B per Phi0 2 mm loop (T)", PHI0 / S56, 5.2e-10, 0.01),
    ("5.6c check 25 x 20.7 pT", 25 * 20.7, 518, 0.01),
    ("5.6d NV field from 84 MHz (mT)", 84 / (2 * GAMMA_E), 1.5, 1e-9),
    ("5.6d lower dip (MHz)", D_NV - GAMMA_E * 1.5, 2828, 1e-9),
    ("5.6d upper dip (MHz)", D_NV + GAMMA_E * 1.5, 2912, 1e-9),
]

# 5.7 interferometer phase, Rb 780 nm, T = 0.06 s
keff57 = 4 * math.pi / 780e-9
T57 = 0.06
Phi57 = keff57 * g * T57**2
dphi57 = 1 / math.sqrt(3.6e5)
dg57 = dphi57 / (keff57 * T57**2)
CHECKS += [
    ("5.7a k_eff (1/m)", keff57, 1.61e7, 0.01),
    ("5.7a Phi (rad)", Phi57, 5.69e5, 0.01),
    ("5.7a fringes", Phi57 / (2 * math.pi), 9.06e4, 0.01),
    ("5.7b tau=2T convention (rad)", keff57 * g * (2 * T57) ** 2, 2.28e6, 0.01),
    ("5.7c phase for 5 uGal (rad)", keff57 * 5 * UGAL * T57**2, 2.9e-3, 0.01),
    ("5.7d SQL phase (rad)", dphi57, 1.67e-3, 0.01),
    ("5.7d dg per shot (m/s^2)", dg57, 2.87e-8, 0.01),
    ("5.7d dg per shot (uGal)", dg57 / UGAL, 2.87, 0.01),
    ("5.7d density (uGal/rtHz)", dg57 / UGAL * math.sqrt(0.5), 2.0, 0.03),
    ("5.7e cos^2(pi/3)", math.cos(math.pi / 3) ** 2, 0.25, 1e-9),
]

# 5.8 T^2 scaling
CHECKS += [
    ("5.8a T^2 gain 4 s vs 0.12 s", (4 / 0.12) ** 2, 1.11e3, 0.01),
    ("5.8b drop distance (m)", 2 * g * 0.12**2, 0.28, 0.02),
    ("5.8c atom factor T^4", (4 / 0.12) ** 4, 1.23e6, 0.01),
    ("5.8d max drop T in 1.5 m (s)", math.sqrt(1.5 / (2 * g)), 0.28, 0.02),
    ("5.8e fountain T in 1.5 m (s)", math.sqrt(2 * 1.5 / g), 0.55, 0.01),
    ("5.8e fountain phase gain", (math.sqrt(2 * 1.5 / g) / math.sqrt(1.5 / (2 * g))) ** 2, 4, 1e-9),
]

# 5.9 errata L74, L94
CHECKS += [
    ("5.9i 3 fT/rtHz in 25 Hz (fT)", 3 * math.sqrt(25), 15, 1e-9),
    ("5.9i wrong product 3 x 25", 3 * 25, 75, 1e-9),
    ("5.9ii ratio 36/16", 36 / 16, 2.25, 1e-9),
    ("5.9ii 1/r^2 gain", (36 / 16) ** 2, 5.1, 0.01),
    ("5.9iii 1/r^3 gain", (36 / 16) ** 3, 11.4, 0.01),
]

# 5.10 errata L105-110, L91, L135 (K-39 at 767 nm)
keff510 = 4 * math.pi / 767e-9
CHECKS += [
    ("5.10i convention factor", (2 * 1.0) ** 2 / 1.0**2, 4, 1e-9),
    ("5.10ii k_eff K (1/m)", keff510, 1.64e7, 0.01),
    ("5.10ii chirp null (Hz/s)", keff510 * g / (2 * math.pi), 2.56e7, 0.01),
    ("5.10iii spring displacement ratio", (2 / 0.5) ** 2, 16, 1e-9),
]

# 5.11 F3 like-for-like
cc_typ = 6e-8 * g / UGAL
CHECKS += [
    ("5.11a 6e-8 g/rtHz in uGal/rtHz", cc_typ, 58.9, 0.01),
    ("5.11b atom vs ideal (worse)", 12 / 6, 2, 1e-9),
    ("5.11b typical vs atom (better)", cc_typ / 12, 4.9, 0.01),
]

# 5.12 mixed errors
CHECKS += [
    ("5.12iii SQL 4e6 atoms (rad)", 1 / math.sqrt(4e6), 5e-4, 1e-9),
    ("5.12iii 1/N (rad)", 1 / 4e6, 2.5e-7, 1e-9),
    ("5.12iii sqrt N", math.sqrt(4e6), 2000, 1e-9),
    ("5.12iv 2e-15 x 1 day (s)", 2e-15 * DAY, 1.7e-10, 0.02),
]

# 5.13 F1 model paragraph (Greystock embankment, shared fact sheet, fictional)
CHECKS += [
    ("5.13 spring 8 uGal/rtHz over 300 s (uGal)", 8 / math.sqrt(300), 0.46, 0.01),
    ("5.13 spring drift 30 uGal/day over 8 h (uGal)", 30 * 8 / 24, 10, 1e-9),
    ("5.13 drift over 8 h vs 5 uGal target", 30 * 8 / 24 / 5, 2, 1e-9),
    ("5.13 atom 30 uGal/rtHz over 300 s (uGal)", 30 / math.sqrt(300), 1.7, 0.02),
    ("5.13 void SNR per station, atom (about 3)", 5 / (30 / math.sqrt(300)), 3.0, 0.05),
    ("5.13 atom vs spring noise ratio (nearly 4)", 30 / 8, 3.75, 1e-9),
]

# Spaced review
dt_sr = 4e-16 * YEAR
CHECKS += [
    ("SR1 k_eff 689 nm (1/m)", 4 * math.pi / 689e-9, 1.82e7, 0.01),
    ("SR4 Ramsey 0.4 s (Hz)", 1 / (2 * 0.4), 1.25, 1e-9),
    ("SR6 25 pT/rtHz in 64 Hz (pT)", 25 * math.sqrt(64), 200, 1e-9),
    ("SR8 4e-16 over a year (s)", dt_sr, 1.26e-8, 0.01),
    ("SR8 distance (m)", 3.00e8 * 1.26e-8, 3.8, 0.01),
]
