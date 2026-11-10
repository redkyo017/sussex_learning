"""Numeric answers in content/companions/week02_companion.md, sections 4-6."""
import math

h = 6.62607015e-34
e = 1.602176634e-19
hbar = h / (2 * math.pi)
c = 299792458.0
YEAR = 3.156e7
DAY = 86400.0

CHECKS = [
    # §4.1 bandwidth
    ("4.1 -3 dB point", 20 * math.log10(1 / math.sqrt(2)), -3.01, 1e-3),
    ("4.1 amplitude at bandwidth 71%", 1 / math.sqrt(2), 0.71, 1e-2),
    # §4.2 noise in a bandwidth
    ("4.2 SQUID 1 fT x sqrt(100 Hz)", 1e-15 * math.sqrt(100), 10e-15, 1e-9),
    ("4.2 OPM 10 fT x sqrt(100 Hz)", 10e-15 * math.sqrt(100), 100e-15, 1e-9),
    ("4.2 SNR SQUID on 100 fT", 100e-15 / (1e-15 * math.sqrt(100)), 10, 1e-9),
    ("4.2 SNR OPM on 100 fT", 100e-15 / (10e-15 * math.sqrt(100)), 1, 1e-9),
    ("4.2 SQUID over 1 kHz", 1e-15 * math.sqrt(1000), 31.6e-15, 2e-3),
    # §4.3 distance
    ("4.3 halve distance -> 4x", (2 / 1) ** 2, 4, 1e-9),
    ("4.3 r2/r1 for 10x signal", 1 / math.sqrt(10), 0.316, 2e-3),
    # §4.4 flux quantum
    ("4.4 pi*hbar/e = h/2e", math.pi * hbar / e, 2.07e-15, 2e-3),
    ("4.4 B per flux quantum, 1 cm^2", (h / (2 * e)) / 1e-4, 2.07e-11, 2e-3),
    ("4.4 fraction of Phi0 for 1 fT", 1e-15 / ((h / (2 * e)) / 1e-4), 4.8e-5, 1e-2),
    # §4.5 E = h nu
    ("4.5 E Cs (J)", h * 9192631770, 6.09e-24, 2e-3),
    ("4.5 E Cs (eV)", h * 9192631770 / e, 3.80e-5, 2e-3),
    ("4.5 E Sr (J)", h * 429e12, 2.84e-19, 2e-3),
    ("4.5 E Sr (eV)", h * 429.228e12 / e, 1.78, 5e-3),
    ("4.5 Sr/Cs frequency ratio", 429.228e12 / 9192631770, 4.67e4, 2e-3),
    # §4.7 Q
    ("4.7 Q Cs at 1 Hz", 9192631770 / 1.0, 9.19e9, 1e-3),
    ("4.7 Q Sr at 1 Hz", 429e12 / 1.0, 4.29e14, 1e-3),
    ("4.7 Q ratio Sr/Cs", 429.228e12 / 9192631770, 4.7e4, 1e-2),
    # §4.8 Allan
    ("4.8 tau to 1e-16 from 1e-13", (1e-13 / 1e-16) ** 2, 1e6, 1e-9),
    ("4.8 1e6 s in days", 1e6 / DAY, 11.6, 3e-3),
    # §4.9 fractional conversions
    ("4.9 300 My in s", 300e6 * YEAR, 9.47e15, 1e-3),
    ("4.9 1 s per 300 My", 1 / (300e6 * YEAR), 1.06e-16, 5e-3),
    ("4.9 1e-18 in years", 1e18 / YEAR, 3.17e10, 2e-3),
    ("4.9 1e-19 in years", 1e19 / YEAR, 3.2e11, 1e-2),
    ("4.9 1e-16 per day (s)", 1e-16 * DAY, 8.64e-12, 1e-9),
    ("4.9 1e-16 per day (m)", 1e-16 * DAY * c, 2.6e-3, 1e-2),
    # C2.1
    ("C2.1 noise P", 20e-12 * math.sqrt(500), 4.47e-10, 1e-3),
    ("C2.1 noise Q", 50e-15 * math.sqrt(50), 3.54e-13, 5e-3),
    ("C2.1 SNR P", 5e-9 / (20e-12 * math.sqrt(500)), 11.2, 2e-3),
    ("C2.1 SNR Q", 5e-9 / (50e-15 * math.sqrt(50)), 1.41e4, 5e-3),
    ("C2.1 noise ratio", (20e-12 * math.sqrt(500)) / (50e-15 * math.sqrt(50)), 1.26e3, 5e-3),
    ("C2.1 check 400 x sqrt(10)", 400 * math.sqrt(10), 1265, 1e-3),
    # C2.2
    ("C2.2 signal ratio", (4.5 / 1.5) ** 2, 9, 1e-9),
    ("C2.2 SNR ratio", (4.5 / 1.5) ** 2 / (12 / 3), 2.25, 1e-9),
    ("C2.2 averaging time", ((4.5 / 1.5) ** 2 / (12 / 3)) ** 2, 5.06, 1e-3),
    # C2.3 (Harrowmere fact sheet: quartz 1e-9, Rb 5e-12, 8 h outage design case)
    ("C2.3 8 h in s", 8 * 3600, 28800, 0),
    ("C2.3 quartz 8 h error", 1e-9 * 28800, 28.8e-6, 1e-9),
    ("C2.3 Rb 8 h error", 5e-12 * 28800, 0.144e-6, 1e-9),
    ("C2.3 Rb 8 h error 2 s.f.", 5e-12 * 28800, 0.14e-6, 0.03),
    ("C2.3 quartz phase deg", 360 * 50 * 1e-9 * 28800, 0.518, 5e-3),
    ("C2.3 quartz phase deg 2 s.f.", 360 * 50 * 1e-9 * 28800, 0.52, 1e-2),
    ("C2.3 Rb phase deg", 360 * 50 * 5e-12 * 28800, 0.00259, 2e-3),
    ("C2.3 Rb phase deg 2 s.f.", 360 * 50 * 5e-12 * 28800, 0.0026, 1e-2),
    ("C2.3 quartz holdover s", 1e-6 / 1e-9, 1000, 1e-9),
    ("C2.3 quartz holdover min", 1e-6 / 1e-9 / 60, 17, 0.03),
    ("C2.3 Rb holdover h", 1e-6 / 5e-12 / 3600, 55.6, 1e-3),
    ("C2.3 Rb error as distance", 5e-12 * 28800 * 3.00e8, 43, 5e-3),
    ("C2.3 output ratio", 28.8 / 0.144, 200, 1e-9),
    ("C2.3 quartz fails by", 1e-9 * 28800 / 1e-6, 29, 0.01),
    ("C2.3 Rb margin", 1e-6 / (5e-12 * 28800), 7, 0.02),
    # C2.4 model paragraph (fictional figures)
    ("C2.4 old kit noise in 25 Hz", 30e-12 * math.sqrt(25), 150e-12, 1e-9),
    ("C2.4 old kit SNR on 0.5 nT", 0.5e-9 / (30e-12 * math.sqrt(25)), 3.33, 1e-2),
    ("C2.4 new kit noise in 25 Hz", 80e-15 * math.sqrt(25), 0.4e-12, 1e-9),
    ("C2.4 noise ratio", 30e-12 / 80e-15, 375, 1e-9),
    ("C2.4 new kit SNR on 0.5 nT", 0.5e-9 / (80e-15 * math.sqrt(25)), 1250, 1e-9),
    # C2.5 cold attempt
    ("C2.5 Q microwave", 6.8e9 / 2, 3.4e9, 1e-9),
    ("C2.5 Q optical", 518e12 / 4, 1.295e14, 1e-9),
    ("C2.5 Q ratio", (518e12 / 4) / (6.8e9 / 2), 3.81e4, 1e-3),
    ("C2.5 tau microwave s", (2e-13 / 1e-15) ** 2, 4e4, 1e-9),
    ("C2.5 tau microwave h", (2e-13 / 1e-15) ** 2 / 3600, 11.1, 2e-3),
    ("C2.5 tau optical s", (3e-16 / 1e-17) ** 2, 900, 1e-9),
    ("C2.5 1e-17 in years", 1e17 / YEAR, 3.17e9, 2e-3),
    ("C2.5 frequency ratio", 518e12 / 6.8e9, 7.6e4, 3e-3),
]
