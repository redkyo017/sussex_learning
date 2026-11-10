"""Numeric checks for content/companions/week04_companion.md (sections 4-6 and 9).
Each tuple: (label, computed, stated, rel_tol)."""
from math import cos, radians, sqrt, log, log2, ceil


def E(ta, tb):
    """CHSH correlation for |Phi+> with polariser angles in degrees."""
    return cos(2 * radians(ta - tb))


def T_fibre(km, db_per_km=0.2):
    return 10 ** (-db_per_km * km / 10)


def b92_intercept_resend():
    """Return (P conclusive correct, P conclusive wrong) per photon under random-basis
    intercept-resend. 0 = H, 1 = +45. Bob: R->V gives 1, D->(-45) gives 0."""
    r = 2 ** -0.5
    H, V, P, M = (1, 0), (0, 1), (r, r), (r, -r)
    dot = lambda a, b: a[0] * b[0] + a[1] * b[1]
    corr = err = 0.0
    for bit, s in ((0, H), (1, P)):
        for eb in ((H, V), (P, M)):
            for e in eb:
                pe = 0.5 * dot(s, e) ** 2
                for out, dec in ((V, 1), (M, 0)):
                    p = 0.5 * pe * 0.5 * dot(e, out) ** 2
                    if dec == bit:
                        corr += p
                    else:
                        err += p
    return corr, err


b92_c, b92_e = b92_intercept_resend()


def H2(q):
    return -q * log2(q) - (1 - q) * log2(1 - q)


S_mis = E(15, 0) + E(45, 30) + E(15, 30) - E(45, 0)
src, eff = 1e9, 0.25
sift = lambda T: 0.5 * src * T * eff

CHECKS = [
    # ---- section 3 conversions ----
    ("S3 50 km dB", 0.2 * 50, 10, 0.01),
    ("S3 100 km T", T_fibre(100), 0.01, 0.01),
    ("S3 600 km T", T_fibre(600), 1e-12, 0.01),
    # ---- section 4 ----
    ("4B Table 4.1 sifted fraction", 3 / 6, 0.5, 0.01),
    ("4C Table 4.2 sifted QBER", 2 / 3, 0.67, 0.01),
    ("4D QBER intercept-resend", 0.5 * 0.5, 0.25, 0.01),
    ("4D (3/4)^6", 0.75 ** 6, 0.178, 0.01),
    ("4D detection n=6", 1 - 0.75 ** 6, 0.82, 0.01),
    ("4D (3/4)^20", 0.75 ** 20, 0.0032, 0.02),
    ("4D detection n=20", 1 - 0.75 ** 20, 0.997, 0.01),
    ("4E B92 conclusive no Eve", 0.5 * 0.5, 0.25, 0.01),
    ("4E B92 conclusive with Eve", b92_c + b92_e, 0.375, 0.01),
    ("4E B92 wrong per photon", b92_e, 0.125, 0.01),
    ("4E B92 QBER with Eve", b92_e / (b92_c + b92_e), 1 / 3, 0.01),
    ("4G <ab>", E(22.5, 0), 0.707, 0.01),
    ("4G <AB>", E(67.5, 45), 0.707, 0.01),
    ("4G <aB>", E(22.5, 45), 0.707, 0.01),
    ("4G <Ab>", E(67.5, 0), -0.707, 0.01),
    ("4G S", E(22.5, 0) + E(67.5, 45) + E(22.5, 45) - E(67.5, 0), 2.83, 0.01),
    ("4G rotated set gives same S", E(0, -22.5) + E(45, 22.5) + E(0, 22.5) - E(45, -22.5), 2.83, 0.01),
    ("4E B92 per-check survival 2/3", 1 - b92_e / (b92_c + b92_e), 2 / 3, 0.01),
    ("4G 2sqrt2", 2 * sqrt(2), 2.83, 0.01),
    ("4G min visibility", 1 / sqrt(2), 0.71, 0.01),
    ("4I 2000 km dB", 0.2 * 2000, 400, 0.01),
    ("4I 2000 km T", T_fibre(2000), 1e-40, 0.01),
    ("4I 45 km dB", 0.2 * 45, 9, 0.01),
    ("4I 45 km T", T_fibre(45), 0.126, 0.01),
    ("4J 100 km dB", 0.2 * 100, 20, 0.01),
    ("4J 600 km dB", 0.2 * 600, 120, 0.01),
    ("4J TF sqrt T", sqrt(T_fibre(600)), 1e-6, 0.01),
    ("4J PLOB slope", 1 / log(2), 1.44, 0.01),
    ("4J 70 km dB", 0.2 * 70, 14, 0.01),
    ("4J 70 km T", T_fibre(70), 0.04, 0.01),
    # ---- C4.1 (fresh run: Alice 10111100, DDRRDRRD; Bob DRRDRRDD) ----
    ("C4.1 matches counted", sum(a == b for a, b in zip("DDRRDRRD", "DRRDRRDD")), 4, 0.0),
    ("C4.1 sifted fraction", 4 / 8, 0.5, 0.01),
    ("C4.1 expected errors", 4 * 0.25, 1, 0.01),
    ("C4.1 pass 2 tests", 0.75 ** 2, 0.5625, 0.01),
    ("C4.1 catch 2 tests", 1 - 0.75 ** 2, 0.44, 0.01),
    ("C4.1 n for 99% (real)", log(0.01) / log(0.75), 16.0, 0.01),
    ("C4.1 n integer", 17, 17, 0.0),
    ("C4.1 0.75^17", 0.75 ** 17, 0.0075, 0.02),
    ("C4.1 0.75^16", 0.75 ** 16, 0.010, 0.01),
    # ---- C4.2 ----
    ("C4.2 150 km dB", 0.2 * 150, 30, 0.01),
    ("C4.2 150 km T", T_fibre(150), 1e-3, 0.01),
    ("C4.2 150 km sifted", sift(T_fibre(150)), 1.25e5, 0.01),
    ("C4.2 300 km dB", 0.2 * 300, 60, 0.01),
    ("C4.2 300 km sifted", sift(T_fibre(300)), 125, 0.01),
    ("C4.2 100 km sifted", sift(T_fibre(100)), 1.25e6, 0.01),
    ("C4.2 bound per use 150 km", -log2(1 - T_fibre(150)), 1.44e-3, 0.01),
    ("C4.2 bound rate 150 km", -log2(1 - T_fibre(150)) * src, 1.44e6, 0.01),
    ("C4.2 rate ratio 150/300", sift(T_fibre(150)) / sift(T_fibre(300)), 1000, 0.01),
    ("C4.2 node gain", sift(T_fibre(100)) / sift(T_fibre(300)), 1e4, 0.01),
    # ---- C4.3 (b = 0 reference; misaligned a=15, A=45, B=30) ----
    ("C4.3 <ab>", E(15, 0), 0.866, 0.01),
    ("C4.3 <AB>", E(45, 30), 0.866, 0.01),
    ("C4.3 <aB>", E(15, 30), 0.866, 0.01),
    ("C4.3 <Ab>", E(45, 0), 0.0, 0.01),
    ("C4.3 S", S_mis, 2.60, 0.01),
    ("C4.3 gap to 2sqrt2", 2 * sqrt(2) - S_mis, 0.23, 0.02),
    ("C4.3 S optimal at V=0.8", 0.8 * (E(22.5, 0) + E(67.5, 45) + E(22.5, 45) - E(67.5, 0)), 2.26, 0.01),
    ("C4.3 V threshold misaligned", 2 / S_mis, 0.770, 0.01),
    ("C4.3 V threshold optimal", 1 / sqrt(2), 0.707, 0.01),
    # ---- C4.4 (fictional Harrowmere + hypothetical depot node) ----
    ("C4.4 hop 1 loss 70 km dB", 0.2 * 70, 14, 0.01),
    ("C4.4 hop 2 loss 90 km dB", 0.2 * 90, 18, 0.01),
    ("C4.4 hops sum to route", 70 + 90, 160, 0.0),
    ("C4.4 capex GBP k", 2 * 110 + 40, 260, 0.0),
    ("C4.4 10-year cost GBP k", 2 * 110 + 40 + 10 * 25, 510, 0.0),
    ("C4.4 ratio to PQC", (2 * 110 + 40 + 10 * 25) / 10, 50, 0.03),
    # ---- C4.5 cold attempt (65 km, intrinsic 2.5%, f = 0.3) ----
    ("C4.5 65 km dB", 0.2 * 65, 13, 0.01),
    ("C4.5 65 km T", T_fibre(65), 0.050, 0.01),
    ("C4.5 Eve QBER", 0.3 * 0.25, 0.075, 0.01),
    ("C4.5 total QBER (additive)", 0.025 + 0.3 * 0.25, 0.10, 0.01),
    ("C4.5 total QBER (exact combination)", 0.025 * 0.925 + 0.075 * 0.975, 0.096, 0.01),
    ("C4.5 h(0.10)", H2(0.10), 0.469, 0.01),
    ("C4.5 2h(0.10)", 2 * H2(0.10), 0.938, 0.01),
    ("C4.5 r at 10%", 1 - 2 * H2(0.10), 0.062, 0.02),
    ("C4.5 r ratio to no-Eve r(0.025) ~ a tenth", (1 - 2 * H2(0.10)) / (1 - 2 * H2(0.025)), 0.1, 0.10),
    ("C4.5 n (real)", log(0.001) / log(1 - 0.075), 88.6, 0.01),
    ("C4.5 n integer", ceil(log(0.001) / log(1 - 0.075)), 89, 0.0),
    # ---- section 9 ----
    ("S9 Q1 sifted of 200", 200 * 0.5, 100, 0.01),
    ("S9 Q2 expected errors", 20 * 0.25, 5, 0.01),
    ("S9 Q2 P none", 0.75 ** 20, 0.0032, 0.02),
    ("S9 Q3 half intercept QBER", 0.5 * 0.25, 0.125, 0.01),
    ("S9 Q3 tests ratio", log(0.01) / log(1 - 0.125) / (log(0.01) / log(0.75)), 2.0, 0.10),
]
