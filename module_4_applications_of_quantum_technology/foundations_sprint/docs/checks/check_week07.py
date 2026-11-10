"""Numeric checks for content/companions/week07_companion.md (sections 4-6).
Each tuple: (label, computed, stated, rel_tol)."""

# ---- section 4 (lecture decode) ----
mem30 = 8 * 2**30          # bytes, 8*2^N convention (M11)
mem50 = 8 * 2**50
aT_in_fT = 100e-18 / 1e-15

# ---- C7.1 fibre loss at 0.2 dB/km (typical telecom fibre) ----
loss = lambda km: 0.2 * km
T160 = 10 ** (-loss(160) / 10)

# ---- C7.2 gravimeter, like for like at R = 2.5 uGal ----
R = 2.5
t_atom = (30 / R) ** 2
t_spring = (8 / R) ** 2
drift_h = 30 / 24

# ---- C7.3 rubidium holdover (fact sheet + hypothetical prices) ----
t8 = 8 * 3600
yq, yrb = 1e-9, 5e-12
extra = 38 * (20 - 2)
benefit = lambda p, c=150: 38 * p * c * 10

# ---- C7.5 pump scheduling ----
U = 18 / 0.94
s = 18 - 0.92 * U          # GBP M per year
B = 3 * s * 1000           # GBP k
C = 250

CHECKS = [
    # 4C memory and logical qubits
    ("4C 8*2^30 bytes", mem30, 8.6e9, 0.01),
    ("4C 8*2^50 bytes", mem50, 9.0e15, 0.01),
    ("4C logical at 1000:1", 1000 / 1000, 1, 1e-9),
    ("4C logical at 100:1", 1000 / 100, 10, 1e-9),
    # 4E units
    ("4E 100 aT in fT", aT_in_fT, 0.1, 1e-9),
    ("4E NG-CSAC factor", 10**3, 1000, 1e-9),
    # C7.1 fibre
    ("C7.1 loss 12 km dB", loss(12), 2.4, 1e-9),
    ("C7.1 loss 38 km dB", loss(38), 7.6, 1e-9),
    ("C7.1 loss 160 km dB", loss(160), 32, 1e-9),
    ("C7.1 transmission 160 km", T160, 6e-4, 0.06),
    ("C7.1 loss difference 160 vs 12 km dB", loss(160) - loss(12), 30, 0.02),
    # C7.2 gravimeter
    ("C7.2 atom s per station", t_atom, 144, 1e-9),
    ("C7.2 atom hours for 150 stations", 150 * t_atom / 3600, 6, 1e-9),
    ("C7.2 spring s per station", t_spring, 10, 0.03),
    ("C7.2 spring drift uGal/h", drift_h, 1.25, 1e-9),
    ("C7.2 spring drift hours to 2.5 uGal", R / drift_h, 2, 1e-9),
    # C7.3 clocks
    ("C7.3 quartz error 8 h us", yq * t8 * 1e6, 28.8, 1e-6),
    ("C7.3 Rb error 8 h us", yrb * t8 * 1e6, 0.144, 1e-6),
    ("C7.3 quartz time to 1 us s", 1e-6 / yq, 1000, 1e-9),
    ("C7.3 quartz time to 1 us min", 1e-6 / yq / 60, 16.7, 0.01),
    ("C7.3 Rb time to 1 us s", 1e-6 / yrb, 2e5, 1e-9),
    ("C7.3 Rb time to 1 us h", 1e-6 / yrb / 3600, 55.6, 0.01),
    ("C7.3 Rb margin vs design case", (1e-6 / yrb) / t8, 7, 0.02),
    ("C7.3 offset ratio", yq / yrb, 200, 1e-9),
    ("C7.3 extra cost k", extra, 684, 1e-9),
    ("C7.3 benefit p=0.02 k", benefit(0.02), 1140, 1e-9),
    ("C7.3 net p=0.02 k", benefit(0.02) - extra, 456, 1e-9),
    ("C7.3 net p=0.01 k", benefit(0.01) - extra, -114, 1e-9),
    ("C7.3 net p=0.04 k", benefit(0.04) - extra, 1596, 1e-9),
    ("C7.3 benefit p=0.01 k", benefit(0.01), 570, 1e-9),
    ("C7.3 benefit p=0.04 k", benefit(0.04), 2280, 1e-9),
    ("C7.3 break-even p", extra / (38 * 150 * 10), 0.012, 0.01),
    ("C7.3 benefit/risk ratio", benefit(0.02) / extra, 1.67, 0.01),
    ("C7.3 break-even breach cost k", extra / (38 * 0.02 * 10), 90, 1e-9),
    # C7.5 pump scheduling
    ("C7.5 unoptimised bill M", U, 19.15, 0.001),
    ("C7.5 vendor bill M", 0.92 * U, 17.62, 0.001),
    ("C7.5 incremental saving M/yr", s, 0.383, 0.002),
    ("C7.5 incremental saving % of bill", 100 * s / 18, 2.1, 0.02),
    ("C7.5 benefit 3 yr k", B, 1149, 0.001),
    ("C7.5 EV p=0.05 k", 0.05 * B - C, -192.6, 0.002),
    ("C7.5 EV p=0.02 k", 0.02 * B - C, -227.0, 0.002),
    ("C7.5 EV p=0.10 k", 0.10 * B - C, -135.1, 0.002),
    ("C7.5 break-even p", C / B, 0.22, 0.02),
    ("C7.5 check 2% of unoptimised M", 0.02 * U, 0.383, 0.002),
]
