"""Numeric answers stated in content/day06.md (quantum communication: M8, M9, M10).

Each tuple: (label, computed, stated, rel_tol). `stated` is the number as written in the markdown.
"""
import math

h_planck = 6.62607015e-34
e_charge = 1.602176634e-19
c = 299792458.0
g = 9.81
DAY = 86400


def H2(q):
    """Binary entropy in bits."""
    return -q * math.log2(q) - (1 - q) * math.log2(1 - q)


def eta(L, alpha=0.2):
    """Fibre transmission for length L km at alpha dB/km."""
    return 10 ** (-alpha * L / 10)


def plob(e):
    """Repeaterless (PLOB) bound, secret bits per channel use."""
    return -math.log2(1 - e)


def cosd(x):
    return math.cos(math.radians(x))


def E(t1, t2):
    """Polarisation correlation for (|HH>+|VV>)/sqrt2."""
    return math.cos(math.radians(2 * (t1 - t2)))


def S(a, A, b, B, corr=E):
    """Lecture Eq 4.3 form: <ab> + <AB> + <aB> - <Ab>."""
    return corr(a, b) + corr(A, B) + corr(a, B) - corr(A, b)


def b92_enumerate():
    """Enumerate B92 under random-basis intercept-resend.

    Alice: bit 0 -> H (0 deg), bit 1 -> D (+45 deg), equal priors.
    Eve: measures in R (0/90) or D (45/-45) at random, resends the state she sees.
    Bob: measures in R or D at random; V (90) => bit 1, A (-45) => bit 0, else inconclusive.
    Returns (conclusive fraction without Eve, conclusive fraction with Eve, wrong fraction with Eve).
    """
    alice = {0: 0.0, 1: 45.0}
    bases = [(0.0, 90.0), (45.0, -45.0)]
    conclusive = {90.0: 1, -45.0: 0}

    def malus(x, y):
        return cosd(x - y) ** 2

    no_eve = with_eve = wrong = 0.0
    for bit, ang in alice.items():
        for bb in bases:
            for out in bb:
                if out in conclusive:
                    no_eve += 0.5 * 0.5 * malus(ang, out)
        for eb in bases:
            for e in eb:
                pe = 0.5 * 0.5 * malus(ang, e)
                for bb in bases:
                    for out in bb:
                        if out in conclusive:
                            p = pe * 0.5 * malus(e, out)
                            with_eve += p
                            if conclusive[out] != bit:
                                wrong += p
    return no_eve, with_eve, wrong


b92_no, b92_eve, b92_wrong = b92_enumerate()

# ---------- Core concepts: worked clones ----------
CHECKS = [
    # M8.1 weather-station link 9.6 kbit/s
    ("M8.1 OTP key per day at 9.6 kbit/s (MB)", 9600 * DAY / 8 / 1e6, 104, 0.01),
    ("M8.1 OTP key per day at 9.6 kbit/s (bytes)", 9600 * DAY / 8, 1.04e8, 0.01),
    ("M8.1 AES-256 rekey every 300 s (bit/s)", 256 / 300, 0.85, 0.01),
    ("M8.1 OTP/AES ratio ~1e4", 9600 / (256 / 300), 1e4, 0.15),
    ("M8.1 Grover on AES-256 effective bits", 256 / 2, 128, 1e-9),
    # M8.2 Mosca clone
    ("M8.2 Mosca x+y (10+4)", 10 + 4, 14, 1e-9),
    ("M8.2 Mosca exposure 14-12", 10 + 4 - 12, 2, 1e-9),
    # M9.1 Malus clone, photon at 10 deg
    ("M9.1 P(H) at 10 deg", cosd(10) ** 2, 0.97, 0.01),
    ("M9.1 P(D) at 10 deg (cos^2 35)", cosd(35) ** 2, 0.67, 0.01),
    ("M9.1 wrong-basis probability cos^2 45", cosd(45) ** 2, 0.5, 1e-9),
    # M9.3 BB84 clone: 6 of 10 matched
    ("M9.3 sifted fraction in clone run", 6 / 10, 0.60, 1e-9),
    ("M9.3 P(exactly 6 of 10 matches)", math.comb(10, 6) / 2**10, 0.21, 0.03),
    # M9.4 intercept-resend
    ("M9.4 QBER full intercept-resend", 0.5 * 0.5, 0.25, 1e-9),
    ("M9.4 detection n=10", 1 - 0.75**10, 0.944, 0.001),
    ("M9.4 n for survival 1e-6 (threshold)", math.log(1e-6) / math.log(0.75), 48.0, 0.01),
    ("M9.4 n for survival 1e-6 (rounded up)", math.ceil(math.log(1e-6) / math.log(0.75)), 49, 1e-9),
    ("M9.4 BB84 threshold: r=1-2h(0.11) ~ 0", 1 - 2 * H2(0.11), 0.0, 0.0),  # abs check below
    # M9.5 B92 conclusive yield
    ("M9.5 B92 conclusive fraction", 0.5 * 0.5, 0.25, 1e-9),
    ("M9.5 B92 conclusive fraction (enumerated, no Eve)", b92_no, 1 / 4, 1e-9),
    ("M9.5 B92 conclusive fraction under intercept-resend", b92_eve, 3 / 8, 1e-9),
    ("M9.5 B92 wrong kept bits under intercept-resend (fraction of kept)", b92_wrong / b92_eve, 1 / 3, 1e-9),
    ("M9.5 B92 per-checked-bit survival 1 - 1/3", 1 - b92_wrong / b92_eve, 2 / 3, 1e-9),
    ("M9.5 BB84 per-bit survival the lecture's 3/4", 1 - 0.5 * 0.5, 3 / 4, 1e-9),
    # M10.1 CHSH
    ("M10.1 cos 45", cosd(45), 0.707, 0.001),
    ("M10.1 S ideal (a=22.5,A=67.5,b=0,B=45)", S(22.5, 67.5, 0, 45), 2.83, 0.002),
    ("M10.1 S equals 2 sqrt2", S(22.5, 67.5, 0, 45), 2 * math.sqrt(2), 1e-9),
    ("M10.1 visibility threshold 1/sqrt2", 2 / (2 * math.sqrt(2)), 0.707, 0.001),
    ("M10.1 S at V=0.9", 2 * math.sqrt(2) * 0.9, 2.55, 0.002),
    # M10.2 fibre loss
    ("M10.2 3 dB length at 0.2 dB/km (km)", 3 / 0.2, 15, 1e-9),
    ("M10.2 eta 50 km", eta(50), 0.1, 1e-9),
    ("M10.2 eta 100 km", eta(100), 0.01, 1e-9),
    ("M10.2 eta 1000 km", eta(1000), 1e-20, 1e-9),
    ("M10.2 seconds per photon at 1e9/s over 1000 km", 1 / (1e9 * eta(1000)), 1e11, 1e-9),
    ("M10.2 years per photon over 1000 km", 1 / (1e9 * eta(1000)) / (365.25 * DAY), 3200, 0.02),
    ("M10.2 PLOB 100 km (bits/use)", plob(eta(100)), 0.0145, 0.01),
    ("M10.2 PLOB 100 km at 1 GHz (Mbit/s)", plob(eta(100)) * 1e9 / 1e6, 14.5, 0.01),
    ("M10.2 PLOB small-eta slope 1/ln2", 1 / math.log(2), 1.44, 0.01),
    # M10.4 free-space doubling
    ("M10.4 free-space doubling factor 1/4 in dB", 10 * math.log10(4), 6, 0.01),
    ("M10.4 fibre 1000 km loss (dB)", 0.2 * 1000, 200, 1e-9),
]

# ---------- Exercises ----------
aes_site = 256 / 60
CHECKS += [
    # 6.1
    ("6.1 AES key rate per site (bit/s)", aes_site, 4.3, 0.01),
    ("6.1 AES key bits per day per site", 256 * 1440, 368640, 1e-9),
    ("6.1 AES key per day (kB)", 256 * 1440 / 8 / 1000, 46, 0.01),
    ("6.1 AES four sites (bit/s)", 4 * aes_site, 17, 0.01),
    ("6.1 10 kbit/s over AES need", 10000 / aes_site, 2.3e3, 0.02),
    ("6.1 Mosca x+y", 15 + 5, 20, 1e-9),
    ("6.1 exposure window at z=10", 15 + 5 - 10, 10, 1e-9),
    # 6.2
    ("6.2 P(H) at 30 deg", cosd(30) ** 2, 0.75, 1e-9),
    ("6.2 P(V) at 30 deg", 1 - cosd(30) ** 2, 0.25, 1e-9),
    ("6.2 P(D) at 30 deg (cos^2 15)", cosd(15) ** 2, 0.93, 0.01),
    ("6.2 P(A) at 30 deg", 1 - cosd(15) ** 2, 0.07, 0.05),
    ("6.2 |<H|D>|^2", (1 / math.sqrt(2)) ** 2, 0.5, 1e-9),
    # 6.3
    ("6.3 sifted fraction 5/10", 5 / 10, 0.5, 1e-9),
    ("6.3 raw agreement 6/10", 6 / 10, 0.6, 1e-9),
    ("6.3 sifted bits from 2e6 detections", 2e6 * 0.5, 1e6, 1e-9),
    ("6.3 after 5% test", 2e6 * 0.5 * 0.95, 9.5e5, 1e-9),
    # 6.4
    ("6.4 wrong-basis error", cosd(45) ** 2, 0.5, 1e-9),
    ("6.4 QBER at f=0.4", 0.4 / 4, 0.10, 1e-9),
    ("6.4 detection n=20", 1 - 0.75**20, 0.997, 0.001),
    ("6.4 n for 99.9% (threshold)", math.log(1e-3) / math.log(0.75), 24.0, 0.01),
    ("6.4 0.75^24", 0.75**24, 0.0010, 0.01),
    ("6.4 n for 99.9% full attack (rounded up)", math.ceil(math.log(1e-3) / math.log(0.75)), 25, 1e-9),
    ("6.4 n for 99.9% at f=0.4 (threshold)", math.log(1e-3) / math.log(0.9), 65.6, 0.01),
    ("6.4 n for 99.9% at f=0.4 (rounded up)", math.ceil(math.log(1e-3) / math.log(0.9)), 66, 1e-9),
    # 6.5
    ("6.5 S ideal", S(22.5, 67.5, 0, 45), 2.83, 0.002),
    ("6.5 S at V=0.85", 0.85 * S(22.5, 67.5, 0, 45), 2.40, 0.002),
    ("6.5 V threshold", 1 / math.sqrt(2), 0.707, 0.001),
    ("6.5 S careless angles a=b=0, A=B=45", S(0, 45, 0, 45), 2.0, 1e-9),
    ("6.5 S Eve measures H/V", S(22.5, 67.5, 0, 45, corr=lambda x, y: math.cos(math.radians(2 * x)) * math.cos(math.radians(2 * y))), 1.41, 0.003),
    # 6.6 Harrowmere sites (12, 38, 95, 160 km), box 10 kbit/s at 40 km
    ("6.6 loss 12 km (dB)", 0.2 * 12, 2.4, 1e-9),
    ("6.6 loss 38 km (dB)", 0.2 * 38, 7.6, 1e-9),
    ("6.6 loss 95 km (dB)", 0.2 * 95, 19, 1e-9),
    ("6.6 loss 160 km (dB)", 0.2 * 160, 32, 1e-9),
    ("6.6 eta 12 km", eta(12), 0.58, 0.01),
    ("6.6 eta 38 km", eta(38), 0.17, 0.03),
    ("6.6 eta 95 km", eta(95), 0.013, 0.04),
    ("6.6 eta 160 km", eta(160), 6.3e-4, 0.01),
    ("6.6 rate 12 km (kbit/s)", 10 * eta(12) / eta(40), 36, 0.02),
    ("6.6 rate 38 km (kbit/s)", 10 * eta(38) / eta(40), 11, 0.02),
    ("6.6 rate 95 km (kbit/s)", 10 * eta(95) / eta(40), 0.79, 0.01),
    ("6.6 rate 160 km on paper (kbit/s)", 10 * eta(160) / eta(40), 0.040, 0.01),
    ("6.6 hop loss 80 km (dB)", 0.2 * 80, 16, 1e-9),
    ("6.6 rate per 80 km hop (kbit/s)", 10 * eta(80) / eta(40), 1.6, 0.02),
    ("6.6 95 km rate over AES need", 10 * eta(95) / eta(40) * 1000 / aes_site, 180, 0.04),
    ("6.6 PLOB 95 km (bits/pulse)", plob(eta(95)), 0.018, 0.02),
    ("6.6 PLOB 95 km at 1 GHz (Mbit/s)", plob(eta(95)) * 1e3, 18, 0.02),
    # 6.7
    ("6.7 h(0.01)", H2(0.01), 0.081, 0.01),
    ("6.7 r(0.01)", 1 - 2 * H2(0.01), 0.84, 0.01),
    ("6.7 h(0.04)", H2(0.04), 0.242, 0.01),
    ("6.7 r(0.04)", 1 - 2 * H2(0.04), 0.52, 0.02),
    ("6.7 h(0.11)", H2(0.11), 0.500, 0.01),
    ("6.7 sifted rate (kbit/s)", 40 * 0.5, 20, 1e-9),
    ("6.7 h(0.025)", H2(0.025), 0.169, 0.01),
    ("6.7 2h(0.025)", 2 * H2(0.025), 0.337, 0.01),
    ("6.7 r(0.025)", 1 - 2 * H2(0.025), 0.66, 0.01),
    ("6.7 secure rate (kbit/s)", 20 * (1 - 2 * H2(0.025)), 13, 0.02),
]

# ---------- Writing exercises: figures inside model paragraphs ----------
CHECKS += [
    ("6.8 Mosca x+y", 15 + 5, 20, 1e-9),
    ("6.8 exposure at z=10 (years)", 20 - 10, 10, 1e-9),
    ("6.8 intercept-resend error fraction (a quarter)", 0.25, 0.25, 1e-9),
    ("6.8 rate at 38 km (kbit/s)", 10 * eta(38) / eta(40), 11, 0.02),
    ("6.8 AES need (bit/s)", aes_site, 4.3, 0.01),
    ("6.9 rate at 38 km (kbit/s)", 10 * eta(38) / eta(40), 11, 0.02),
    ("6.9 rate at 95 km (kbit/s)", 10 * eta(95) / eta(40), 0.79, 0.01),
    ("6.9 rate per hop to 160 km (kbit/s)", 10 * eta(80) / eta(40), 1.6, 0.02),
    ("6.9 box pairs: 1+1+1+2", 1 + 1 + 1 + 2, 5, 1e-9),
    ("6.9 QKD hardware cost (GBP k)", 5 * 120, 600, 1e-9),
    ("6.9 extra 10 dB splice loss = tenfold cut", 10 ** (-1.0), 0.1, 1e-9),
    ("6.10 tenfold per 50 km", eta(50), 0.1, 1e-9),
]

# ---------- Spaced review answers ----------
CHECKS += [
    ("SR Day05 40 uGal/rtHz over 400 s", 40 / math.sqrt(400), 2, 1e-9),
    ("SR Day05 Phi k_eff g T^2 (rad)", 1.6e7 * g * 0.05**2, 3.9e5, 0.01),
    ("SR Day03 Q 5e14/0.5", 5e14 / 0.5, 1e15, 1e-9),
    ("SR Day03 flux quantum (Wb)", h_planck / (2 * e_charge), 2.07e-15, 0.01),
    ("SR Day03 flux quanta in 1 mm^2 at 1 nT", 1e-9 * 1e-6 / (h_planck / (2 * e_charge)), 0.48, 0.01),
    ("SR Day01 time error 1e-14 over a day (s)", 1e-14 * DAY, 8.6e-10, 0.01),
    ("SR Day01 distance (m)", 1e-14 * DAY * c, 0.26, 0.01),
]

# The BB84 11% threshold: r is zero to within 2e-4 there; make it an absolute check.
CHECKS = [
    (lab, comp, st, tol) if lab != "M9.4 BB84 threshold: r=1-2h(0.11) ~ 0"
    else ("M9.4 BB84 threshold: 1-2h(0.11) < 1e-3 (1 = true)", float(abs(comp) < 1e-3), 1.0, 1e-9)
    for lab, comp, st, tol in CHECKS
]
