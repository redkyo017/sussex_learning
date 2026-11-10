"""Numeric checks for content/day01.md. (label, computed, stated, rel_tol)."""
import math

C = 299_792_458.0          # m/s
DAY = 86_400.0             # s
YR = 3.156e7               # s, as stated in Exercise 1.4
GAL = 1e-2                 # m/s^2
UGAL = 1e-8                # m/s^2
MGAL = 1e-5                # m/s^2
EOTVOS = 1e-9              # s^-2
g = 9.81
R = 6.371e6

grad = 2 * g / R
y_p = 1 / (30e9 * YR)

CHECKS = [
    # Warm-up
    ("warm-up P(0) = (3/5)^2", (3 / 5) ** 2, 0.36, 1e-9),
    ("warm-up P(1) = (4/5)^2", (4 / 5) ** 2, 0.64, 1e-9),
    ("warm-up amplitudes for 3 qubits", 2 ** 3, 8, 0),

    # F1 worked clone: grid timing (Harrowmere fact sheet: quartz 1e-9, Rb 5e-12, 8 h outage)
    ("F1 phase error deg for 1 us at 50 Hz", 360 * 50 * 1e-6, 0.018, 1e-9),
    ("F1 quartz holdover s", 1e-6 / 1e-9, 1e3, 1e-9),
    ("F1 quartz holdover min", 1e-6 / 1e-9 / 60, 17, 0.03),
    ("F1 quartz error after 8 h us", 1e-9 * 8 * 3600 * 1e6, 28.8, 1e-9),
    ("F1 8 h in s", 8 * 3600, 28_800, 0),
    ("F1 Rb holdover s", 1e-6 / 5e-12, 2e5, 1e-9),
    ("F1 Rb holdover days", 1e-6 / 5e-12 / DAY, 2.3, 0.02),
    ("F1 Rb error after 8 h us", 5e-12 * 8 * 3600 * 1e6, 0.144, 1e-9),
    ("F1 gain ratio", 1e-9 / 5e-12, 200, 1e-9),
    ("F1 Rb margin after 8 h", 1e-6 / (5e-12 * 8 * 3600), 7, 0.02),

    # F3 worked clone: magnetometer
    ("F3 lab vs field ratio", 20e-12 / 50e-15, 400, 1e-9),
    ("F3 field vs field ratio", 20e-12 / 1e-12, 20, 1e-9),

    # M1 worked clone
    ("M1 one week in s", 7 * DAY, 604_800, 0),
    ("M1 clone dt s", 2e-14 * 7 * DAY, 1.2e-8, 0.02),
    ("M1 clone dx m", 2e-14 * 7 * DAY * C, 3.6, 0.02),
    ("M1 g in Gal", g / GAL, 981, 1e-9),

    # Exercise 1.1
    ("1.1(a) 0.03 uT in nT", 0.03e-6 / 1e-9, 30, 1e-9),
    ("1.1(b) 200 fT in T", 200e-15, 2e-13, 1e-9),
    ("1.1(c) Earth/200 fT", 50e-6 / 200e-15, 2.5e8, 1e-9),
    ("1.1(c) orders of magnitude", math.log10(50e-6 / 200e-15), 8.4, 0.01),

    # Exercise 1.2
    ("1.2(a) g in Gal", g / GAL, 981, 1e-9),
    ("1.2(b) 10 uGal in m/s^2", 10 * UGAL, 1e-7, 1e-9),
    ("1.2(c) 10 uGal / g", 10 * UGAL / g, 1.0e-8, 0.03),
    ("1.2(d) 0.1 mGal in m/s^2", 0.1 * MGAL, 1e-6, 1e-9),
    ("1.2(d) ratio of specs", (0.1 * MGAL) / 1e-6, 1, 1e-9),

    # Exercise 1.3
    ("1.3(a) gradient s^-2", grad, 3.08e-6, 0.005),
    ("1.3(a) gradient E", grad / EOTVOS, 3080, 0.005),
    ("1.3(b) uGal per cm", grad * 0.01 / UGAL, 3.08, 0.005),
    ("1.3(c) height for 10 uGal, cm", 10 * UGAL / grad * 100, 3.2, 0.02),
    ("1.3 check vs 3086 E (within 0.2%)", abs(grad / EOTVOS - 3086) / 3086, 0.002, 0.1),

    # Exercise 1.4
    ("1.4 A dt us", 1e-9 * DAY / 1e-6, 86.4, 1e-9),
    ("1.4 A dx m", 1e-9 * DAY * C, 2.59e4, 0.005),
    ("1.4 A dx km", 1e-9 * DAY * C / 1e3, 26, 0.01),
    ("1.4 B dt ns", 1e-12 * DAY / 1e-9, 86.4, 1e-9),
    ("1.4 B dx m", 1e-12 * DAY * C, 25.9, 0.005),
    ("1.4 C dt s", 1e-17 * DAY, 8.64e-13, 1e-9),
    ("1.4 C dt ps", 1e-17 * DAY / 1e-12, 0.864, 1e-9),
    ("1.4 C dx m", 1e-17 * DAY * C, 2.6e-4, 0.01),
    ("1.4 C dx mm", 1e-17 * DAY * C * 1e3, 0.26, 0.01),
    ("1.4(b) seconds for 1 s error", 1 / 1e-17, 1e17, 1e-9),
    ("1.4(b) years for 1 s error", 1 / 1e-17 / YR, 3.2e9, 0.02),

    # Exercise 1.5
    ("1.5(a) tau_P s", 30e9 * YR, 9.47e17, 0.001),
    ("1.5(a) y_P", y_p, 1.06e-18, 0.005),
    ("1.5 answer y_P rounded", y_p, 1.1e-18, 0.05),
    ("1.5(b) P/Q", y_p / 8e-19, 1.3, 0.03),
    ("1.5(c) lab vs field", 8 / 2, 4, 1e-9),
    ("1.5(c) field vs field", 8 / 10, 0.8, 1e-9),

    # Exercise 1.6 model paragraph
    ("1.6 256-bit keys per s at 10 kbit/s", 10_000 / 256, 39, 0.01),
    ("1.6 needed rate bit/s (256 bits per 60 s)", 256 / 60, 4.3, 0.01),
    ("1.6 margin", 10_000 / (256 / 60), 2300, 0.02),
    ("1.6 confidentiality + migration years", 15 + 5, 20, 0),

    # Exercise 1.7 model paragraph
    ("1.7 20 uGal in m/s^2", 20 * UGAL, 2e-7, 1e-9),
    ("1.7 field figure / void signal", 20 / 5, 4, 1e-9),

    # Exercise 1.8 model paragraph
    ("1.8 8*2^50 bytes", 8 * 2 ** 50, 9e15, 0.01),
    ("1.8 in PB", 8 * 2 ** 50 / 1e15, 9, 0.01),

    # Done when answers
    ("DW5 30 uGal in m/s^2", 30 * UGAL, 3e-7, 1e-9),
    ("DW5 30 uGal / g", 30 * UGAL / g, 3e-8, 0.03),
    ("DW6 0.5 pT in T", 0.5e-12, 5e-13, 1e-9),
    ("DW6 50 uT / 0.5 pT", 50e-6 / 0.5e-12, 1e8, 1e-9),
    ("DW7 gradient 1 s.f.", grad, 3e-6, 0.05),
    ("DW8 dt s", 5e-15 * DAY, 4.3e-10, 0.01),
    ("DW8 dx m", 5e-15 * DAY * C, 0.13, 0.01),
]
