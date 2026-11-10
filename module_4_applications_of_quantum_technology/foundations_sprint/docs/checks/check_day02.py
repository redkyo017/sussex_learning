"""Numeric answers stated in content/day02.md, recomputed from their inputs."""
import math
import statistics

T = 0.05  # 2-3 significant-figure answers

# Exercise 2.1: precision vs accuracy
_P = [20.41, 20.39, 20.40, 20.42, 20.38]
_Q = [19.7, 20.3, 20.1, 19.8, 20.2]
_ref = 20.00
_sP, _sQ = statistics.stdev(_P), statistics.stdev(_Q)

# Exercise 2.8: Harrowmere cable survey (fictional)
_sig28 = 2e-7 * 0.5 / 2

CHECKS = [
    # Core concepts worked clones
    ("M2.1 clone bias uT", statistics.mean([10.21, 10.19, 10.20]) - 10.00, 0.20, T),
    ("M2.2 -3 dB in dB", 20 * math.log10(1 / math.sqrt(2)), -3.01, 0.01),
    ("M2.2 1/sqrt2", 1 / math.sqrt(2), 0.707, 0.01),
    ("M2.2 clone |H| fc=20, f=10", 1 / math.sqrt(1 + (10 / 20) ** 2), 0.894, 0.01),
    ("M2.2 clone dynamic range ratio", 1e-3 / 1e-9, 1e6, T),
    ("M2.2 clone dynamic range dB", 20 * math.log10(1e-3 / 1e-9), 120, 0.01),
    ("M2.3 clone noise pT", 200 * math.sqrt(25), 1000, T),
    ("M2.4 clone sigma(100 s)", 2e-11 / math.sqrt(100), 2e-12, T),
    ("M3.1 clone SQL N=1e4", 1 / math.sqrt(1e4), 1e-2, T),
    ("M3.1 clone HL N=1e4", 1 / 1e4, 1e-4, T),
    ("M3.1 clone ratio", math.sqrt(1e4), 100, T),
    ("M3.2 clone gain 40->10 mm", (40 / 10) ** 2, 16, T),
    # Exercise 2.1
    ("2.1 mean P", statistics.mean(_P), 20.40, 0.001),
    ("2.1 mean Q", statistics.mean(_Q), 20.02, 0.001),
    ("2.1 bias P", statistics.mean(_P) - _ref, 0.40, T),
    ("2.1 bias Q", statistics.mean(_Q) - _ref, 0.02, T),
    ("2.1 sigma P", _sP, 0.0158, T),
    ("2.1 sigma Q", _sQ, 0.259, T),
    ("2.1 sum sq dev P", sum((x - statistics.mean(_P)) ** 2 for x in _P), 0.0010, T),
    ("2.1 sum sq dev Q", sum((x - statistics.mean(_Q)) ** 2 for x in _Q), 0.268, T),
    ("2.1 n readings", (_sQ / _sP) ** 2, 268, T),
    ("2.1 sigma ratio", _sQ / _sP, 16, T),
    # Exercise 2.2
    ("2.2 |H| at 50 Hz", 1 / math.sqrt(1 + (50 / 100) ** 2), 0.894, 0.01),
    ("2.2 |H| at 150 Hz", 1 / math.sqrt(1 + (150 / 100) ** 2), 0.555, 0.01),
    ("2.2 dB at 150 Hz", 20 * math.log10(1 / math.sqrt(1 + 1.5 ** 2)), -5.1, 0.02),
    ("2.2 |H| at fc", 1 / math.sqrt(2), 0.707, 0.01),
    # Exercise 2.3
    ("2.3a noise fT", 30 * math.sqrt(40), 190, T),
    ("2.3a SNR before narrowing", 50 / (30 * math.sqrt(40)), 0.26, T),
    ("2.3b bandwidth Hz", (10 / 30) ** 2, 0.111, T),
    ("2.3b averaging s", 1 / (2 * (10 / 30) ** 2), 4.5, T),
    ("2.3 check noise factor", 30 * math.sqrt(40) / 10, 19, T),
    ("2.3 check bandwidth factor", 40 / (10 / 30) ** 2, 360, T),
    # Exercise 2.4
    ("2.4 2^24", 2 ** 24, 16777216, 1e-9),
    ("2.4a LSB T", 200e-6 / 2 ** 24, 1.19e-11, T),
    ("2.4b noise pT", 50 * math.sqrt(10), 158, T),
    ("2.4 noise in LSB", 50e-12 * math.sqrt(10) / (200e-6 / 2 ** 24), 13, T),
    ("2.4d DR ratio", 200e-6 / (50e-12 * math.sqrt(10)), 1.26e6, T),
    ("2.4d DR dB", 20 * math.log10(200e-6 / (50e-12 * math.sqrt(10))), 122, 0.01),
    # Exercise 2.5
    ("2.5a sigma(100 s)", 4e-12 / math.sqrt(100), 4e-13, T),
    ("2.5b tau for 1e-13", (4e-12 / 1e-13) ** 2, 1600, T),
    ("2.5c floor start s", (4e-12 / 6e-14) ** 2, 4400, T),
    ("2.5c floor start h", (4e-12 / 6e-14) ** 2 / 3600, 1.2, T),
    ("2.5c sqrt ratio", 4e-12 / 6e-14, 66.7, T),
    ("2.5b minutes", (4e-12 / 1e-13) ** 2 / 60, 27, T),
    # Exercise 2.6
    ("2.6 sqrt N", math.sqrt(2.5e5), 500, T),
    ("2.6a SQL rad", 1 / math.sqrt(2.5e5), 2e-3, T),
    ("2.6a HL rad", 1 / 2.5e5, 4e-6, T),
    ("2.6b ratio", (1 / math.sqrt(2.5e5)) / (1 / 2.5e5), 500, T),
    ("2.6c atoms", 2.5e5 * 10 ** 2, 2.5e7, T),
    ("2.6d cycles", 10 ** 2, 100, T),
    # Exercise 2.7
    ("2.7a signal gain", (50 / 20) ** 2, 6.25, T),
    ("2.7a SNR ratio", (50 / 20) ** 2 * 15 / 45, 2.08, T),
    ("2.7b B at 1.2 m nT", 2e-7 * 2 / 1.2 * 1e9, 333, T),
    ("2.7b B at 2.1 m nT", 2e-7 * 2 / 2.1 * 1e9, 190, T),
    ("2.7b ratio", 2.1 / 1.2, 1.75, T),
    ("2.7b wrong 1/r^2 ratio", (2.1 / 1.2) ** 2, 3.06, T),
    ("2.7 line-current A vs B", (50 / 20) * 15 / 45, 0.83, T),
    # Exercise 2.8 (fictional figures): detection bandwidth ~1 Hz (lock-in), not the 200 Hz sensor bandwidth
    ("2.8 signal nT", _sig28 * 1e9, 50, T),
    ("2.8 1% of signal nT", 0.01 * _sig28 * 1e9, 0.5, T),
    ("2.8 required S nT/rtHz in 1 Hz", 0.01 * _sig28 / math.sqrt(1.0) * 1e9, 0.5, T),
    ("2.8 dynamic range full scale / noise floor", 50e-6 / (0.01 * _sig28), 1e5, T),
    ("2.8 dynamic range dB", 20 * math.log10(50e-6 / (0.01 * _sig28)), 100, 0.01),
    ("2.8 required / fluxgate", (0.01 * _sig28 / math.sqrt(1.0)) / 1e-10, 5, 0.05),
    ("2.8 weak answer overstatement sqrt(200)", math.sqrt(200), 14, T),
    # Exercise 2.9 (fictional figures)
    ("2.9 holdover s", 8 * 3600, 28800, 1e-9),
    ("2.9 required y", 1e-6 / 28800, 3.5e-11, T),
    ("2.9 rough wander ns", 1e-12 * 28800 * 1e9, 29, T),
    # Done when
    ("DW3 noise pT", 80 * math.sqrt(16), 320, T),
    ("DW5 averaging factor", 5 ** 2, 25, T),
    ("DW7 sigma(400 s)", 3e-12 / math.sqrt(400), 1.5e-13, T),
    ("DW8 SQL N=1e6", 1 / math.sqrt(1e6), 1e-3, T),
    ("DW8 HL N=1e6", 1 / 1e6, 1e-6, T),
    ("DW9 gain 30->10 mm", (30 / 10) ** 2, 9, T),
    # Spaced review
    ("SR4 fT in 50 uT", 50e-6 / 1e-15, 5e10, T),
    ("SR5 3 uGal in m/s^2", 3e-6 * 1e-2, 3e-8, T),
    ("SR6 time gained s", 2e-15 * 3.156e7, 6.3e-8, T),
    ("SR6 light distance m", 2.998e8 * 2e-15 * 3.156e7, 19, T),
]
