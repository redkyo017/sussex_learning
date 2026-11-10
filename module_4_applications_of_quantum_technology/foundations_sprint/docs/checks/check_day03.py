"""Numeric answers stated in content/day03.md, recomputed from their inputs.
Each entry: (label, computed, stated, rel_tol)."""
import math

h = 6.62607015e-34
e = 1.602176634e-19
c = 299792458.0
YEAR = 3.156e7
DAY = 86400.0

nu_cs = 9192631770.0
nu_sr = 4.29228e14
nu_rb = 6.834682611e9
nu_yb = 518.295836e12
gamma_rb = 7.0          # Hz/nT, 87Rb ground state F=2
gamma_nv = 28.0         # MHz/mT
D_nv = 2870.0           # MHz
phi0 = h / (2 * e)


def lorentz(d, w):
    return 1.0 / (1.0 + (2.0 * d / w) ** 2)


def rabi_p(f_rabi, t):
    return math.sin(2 * math.pi * f_rabi * t / 2) ** 2


sig_cs = 1 / (nu_cs * 1000)
sig_sr = 1 / (nu_sr * 30)

CHECKS = [
    # M4.1 worked clone
    ("M4.1 E_Cs J", h * nu_cs, 6.09e-24, 0.01),
    ("M4.1 E_Cs eV", h * nu_cs / e, 3.80e-5, 0.01),
    ("M4.1 E_Sr J", h * nu_sr, 2.84e-19, 0.01),
    ("M4.1 E_Sr eV", h * nu_sr / e, 1.78, 0.01),
    ("M4.1 Q_Cs 1 Hz", nu_cs / 1.0, 9.2e9, 0.01),
    ("M4.1 Q_Sr 1 Hz", nu_sr / 1.0, 4.3e14, 0.01),
    ("M4.1 Q ratio", nu_sr / nu_cs, 4.67e4, 0.01),
    # M4.2 worked clone
    ("M4.2 t_pi 50 kHz (us)", 1 / (2 * 50e3) * 1e6, 10, 0.01),
    ("M4.2 t_pi/2 50 kHz (us)", 1 / (4 * 50e3) * 1e6, 5, 0.01),
    ("M4.2 Ramsey width T=0.5", 1 / (2 * 0.5), 1.0, 0.01),
    ("M4.2 pi/2 pulse P1", rabi_p(1.0, 0.25), 0.5, 1e-9),
    # M4.3 worked clone
    ("M4.3 P(-0.4)", lorentz(-0.4, 1), 0.610, 0.005),
    ("M4.3 P(+0.6)", lorentz(0.6, 1), 0.410, 0.005),
    ("M4.3 error", lorentz(-0.4, 1) - lorentz(0.6, 1), 0.200, 0.005),
    ("M4.3 linear estimate", 2 * 0.1 / 1, 0.2, 0.01),
    # M4.4 worked clone
    ("M4.4 comb nu (MHz)", 1716912 * 250 + 35 + 40, 429228075, 1e-12),
    # M1 revisited worked clone
    ("M1rev L159 fractional", 1 / (3e8 * YEAR), 1.06e-16, 0.01),
    ("M1rev L195 years", 1 / (1e-18 * YEAR), 3.17e10, 0.01),
    ("M1rev 1e-16 day ps", 1e-16 * DAY * 1e12, 8.64, 0.01),
    ("M1rev 1e-16 day mm", 1e-16 * DAY * c * 1e3, 2.6, 0.02),
    ("M1rev 1 ns metres", 1e-9 * c, 0.30, 0.01),
    ("M1rev 1 us phase deg", 360 * 50 * 1e-6, 0.018, 0.01),
    # M5.1 worked clone
    ("M5.1 Larmor 50 uT kHz", gamma_rb * 50000 / 1e3, 350, 0.01),
    # M5.2 worked clone
    ("M5.2 Phi0", phi0, 2.07e-15, 0.01),
    ("M5.2 B per Phi0 1 cm2 pT", phi0 / 1e-4 * 1e12, 20.7, 0.01),
    ("M5.2 1 fT in Phi0", 1e-15 * 1e-4 / phi0, 4.8e-5, 0.01),
    # M5.3 worked clone
    ("M5.3 low dip 1 mT", D_nv - gamma_nv * 1, 2842, 1e-9),
    ("M5.3 high dip 1 mT", D_nv + gamma_nv * 1, 2898, 1e-9),
    ("M5.3 splitting 1 mT", 2 * gamma_nv * 1, 56, 1e-9),
    # M5.4 table
    ("M5.4 NV L82/L137 ratio", 1e-6 / 100e-9, 10, 1e-9),
    ("M5.4 OPM/SQUID MEG ratio", 10 / 1, 10, 1e-9),
    # Ex 3.1
    ("3.1 E_Rb J", h * nu_rb, 4.53e-24, 0.01),
    ("3.1 E_Rb eV", h * nu_rb / e, 2.83e-5, 0.01),
    ("3.1 E_Yb J", h * nu_yb, 3.43e-19, 0.01),
    ("3.1 E_Yb eV", h * nu_yb / e, 2.14, 0.01),
    ("3.1 Q_Rb", nu_rb / 2, 3.42e9, 0.01),
    ("3.1 Q_Yb", nu_yb / 2, 2.59e14, 0.01),
    ("3.1 ratio", nu_yb / nu_rb, 7.58e4, 0.01),
    # Ex 3.2
    ("3.2 t_pi us", 1 / (2 * 25e3) * 1e6, 20, 0.01),
    ("3.2 t_pi/2 us", 1 / (4 * 25e3) * 1e6, 10, 0.01),
    ("3.2 Omega t (rad)", 2 * math.pi * 25e3 * 5e-6, math.pi / 4, 1e-9),
    ("3.2 P1 at 5 us", rabi_p(25e3, 5e-6), 0.146, 0.005),
    ("3.2 Ramsey width T=0.25", 1 / (2 * 0.25), 2, 0.01),
    ("3.2 Q", nu_rb / (1 / (2 * 0.25)), 3.42e9, 0.01),
    # Ex 3.3
    ("3.3 P(-0.85)", lorentz(-0.85, 2), 0.581, 0.005),
    ("3.3 P(+1.15)", lorentz(1.15, 2), 0.431, 0.005),
    ("3.3 error", lorentz(-0.85, 2) - lorentz(1.15, 2), 0.150, 0.005),
    ("3.3 linear", 2 * 0.15 / 2, 0.150, 0.005),
    # Ex 3.4
    ("3.4 n*frep MHz", 2591479 * 200, 518295800, 1e-12),
    ("3.4 nu MHz", 2591479 * 200 + 15 + 62, 518295877, 1e-12),
    ("3.4 offset from Yb MHz", 2591479 * 200 + 15 + 62 - nu_yb / 1e6, 41, 0.01),
    # Ex 3.5
    ("3.5 sigma Cs 1 s", sig_cs, 1.09e-13, 0.01),
    ("3.5 sigma Sr 1 s", sig_sr, 7.8e-17, 0.01),
    ("3.5 ratio", sig_cs / sig_sr, 1400, 0.01),
    ("3.5 tau Cs s", (sig_cs / 1e-17) ** 2, 1.18e8, 0.01),
    ("3.5 tau Cs years", (sig_cs / 1e-17) ** 2 / YEAR, 3.7, 0.03),
    ("3.5 tau Sr s", (sig_sr / 1e-17) ** 2, 60, 0.02),
    ("3.5 SNR factor", 1000 / 30, 33, 0.02),
    ("3.5 ratio squared", (sig_cs / sig_sr) ** 2, 2e6, 0.03),
    # Ex 3.6
    ("3.6 quartz holdover s", 1e-6 / 1e-9, 1000, 0.01),
    ("3.6 quartz holdover min", 1e-6 / 1e-9 / 60, 17, 0.03),
    ("3.6 Rb holdover s", 1e-6 / 5e-12, 2e5, 0.01),
    ("3.6 Rb holdover days", 1e-6 / 5e-12 / DAY, 2.3, 0.02),
    ("3.6 optical holdover years", 1e-6 / 1e-15 / YEAR, 32, 0.02),
    ("3.6 8 h in s", 8 * 3600, 28800, 0),
    ("3.6 quartz 8 h us", 1e-9 * 28800 * 1e6, 28.8, 0.01),
    ("3.6 quartz fails by", 1e-9 * 28800 / 1e-6, 29, 0.01),
    ("3.6 Rb 8 h us", 5e-12 * 28800 * 1e6, 0.144, 0.01),
    ("3.6 Rb 8 h us answer", 5e-12 * 28800 * 1e6, 0.14, 0.03),
    ("3.6 Rb margin", 1e-6 / (5e-12 * 28800), 6.9, 0.01),
    ("3.6 holdover ratio", (1e-6 / 5e-12) / (1e-6 / 1e-9), 200, 0.01),
    ("3.6 phase deg", 360 * 50 * 1e-6, 0.018, 0.01),
    ("3.6 distance m", c * 1e-6, 300, 0.01),
    # Ex 3.7
    ("3.7 Larmor 48 uT kHz", gamma_rb * 48000 / 1e3, 336, 0.01),
    ("3.7 shift 20 nT Hz", gamma_rb * 20, 140, 0.01),
    ("3.7 B per Phi0 9 mm2 pT", phi0 / 9e-6 * 1e12, 230, 0.01),
    ("3.7 n for 10 nT", 1e-8 * 9e-6 / phi0, 43.5, 0.01),
    ("3.7 pi hbar / e", math.pi * (h / (2 * math.pi)) / e, 2.07e-15, 0.01),
    ("3.7 loop ratio", (phi0 / 9e-6) / (phi0 / 1e-4), 11, 0.02),
    # Ex 3.8
    ("3.8 shift 0.5 mT MHz", gamma_nv * 0.5, 14, 1e-9),
    ("3.8 low dip", D_nv - gamma_nv * 0.5, 2856, 1e-9),
    ("3.8 high dip", D_nv + gamma_nv * 0.5, 2884, 1e-9),
    ("3.8 B from 196 MHz", 196 / (2 * gamma_nv), 3.5, 1e-9),
    ("3.8 NV disagreement", 1e-6 / 100e-9, 10, 1e-9),
    # Ex 3.9 model paragraph (reuses 3.6)
    ("3.9 quartz 8 h us", 1e-9 * 28800 * 1e6, 28.8, 0.01),
    ("3.9 Rb 8 h us", 5e-12 * 28800 * 1e6, 0.144, 0.01),
    ("3.9 margin sevenfold", 1e-6 / (5e-12 * 28800), 7, 0.02),
    ("3.9 quartz holdover min", 1e-6 / 1e-9 / 60, 17, 0.03),
    ("3.9 Rb holdover days", 1e-6 / 5e-12 / DAY, 2.3, 0.02),
    ("3.9 holdover ratio", 1e-9 / 5e-12, 200, 0.01),
    # Ex 3.10
    ("3.10 B at 2 m pT", 4 * math.pi * 1e-7 * 5e-3 / (2 * math.pi * 2) * 1e12, 500, 0.01),
    ("3.10 fluxgate noise pT", 100 * math.sqrt(10), 316, 0.01),
    ("3.10 fluxgate SNR", 500 / (100 * math.sqrt(10)), 1.6, 0.02),
    ("3.10 Larmor shift Hz", gamma_rb * 0.5, 3.5, 0.01),
    ("3.10 Larmor carrier 50 uT kHz", gamma_rb * 50000 / 1e3, 350, 0.01),
    ("3.10 OPM noise pT", 1 * math.sqrt(10), 3.2, 0.02),
    ("3.10 OPM SNR", 500 / (1 * math.sqrt(10)), 160, 0.02),
    ("3.10 gain", (500 / math.sqrt(10)) / (500 / (100 * math.sqrt(10))), 100, 0.01),
    # Done when
    ("DW Ramsey 0.1 s Hz", 1 / (2 * 0.1), 5, 0.01),
    ("DW 1e-15 day ps", 1e-15 * DAY * 1e12, 86.4, 0.01),
    ("DW 1e-15 day cm", 1e-15 * DAY * c * 100, 2.6, 0.02),
    # Spaced review
    ("SR1 noise fT", 10 * math.sqrt(100), 100, 0.01),
    ("SR2 factor", math.sqrt(100), 10, 0.01),
    ("SR3 shot", 1 / math.sqrt(1e6), 1e-3, 0.01),
    ("SR3 Heisenberg", 1 / 1e6, 1e-6, 0.01),
    ("SR4 halve distance", (2 / 1) ** 2, 4, 0.01),
    ("SR6 Earth fT", 50e-6 / 1e-15, 5e10, 0.01),
]
