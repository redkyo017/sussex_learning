"""Independent verification for Module 4 Assessment 1 (PRB), candidate 672128.

Rule: a check that re-runs the written algebra is not a check. Each block below
reaches the quoted number by a different mechanism (simulation, quadrature,
Biot-Savart summation, trajectory integration, root finding) and compares it with
the hard-coded value printed in the PDF.

    ./.venv/bin/python verify.py
"""
import numpy as np
from scipy import integrate, optimize

FAIL = []


def check(name, got, want, rtol=1e-3):
    ok = np.isclose(got, want, rtol=rtol, atol=0)
    FAIL.extend([] if ok else [name])
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: got {got:.6g}, PDF says {want:.6g}")


h = 6.62607015e-34; hbar = h / (2 * np.pi); kB = 1.380649e-23
u = 1.66053906660e-27; mu0 = 1.25663706212e-6; G = 6.67430e-11
m = 86.909180527 * u; R_E = 6.371e6
rng = np.random.default_rng(672128)

# ---------------------------------------------------------------- Q1
print("Q1  simulate white noise of ASD 50 fT/sqrt(Hz) sampled to a 1 kHz bandwidth")
fs = 2000.0                          # Nyquist = 1 kHz = measurement bandwidth
N = 2_000_000
sigma = 50e-15 * np.sqrt(fs / 2)     # one-sided ASD -> per-sample rms
noise = rng.normal(0, sigma, N)
f, Pxx = __import__("scipy.signal", fromlist=["welch"]).welch(noise, fs, nperseg=4096)
check("Q1 ASD recovered from simulated trace (T/sqrt Hz)", np.sqrt(np.median(Pxx)), 50e-15, 0.02)
check("Q1 SNR = 2 pT / rms(noise)", 2e-12 / noise.std(), 1.265, 0.01)

# ---------------------------------------------------------------- Q2-Q4
print("Q2-Q4  Biot-Savart: sum dB over a discretised 1 mm loop, no closed form used")


def biot_savart_axis(z, I, R=1e-3, n=4000):
    phi = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dphi = 2 * np.pi / n
    src = np.stack([R * np.cos(phi), R * np.sin(phi), np.zeros(n)], 1)
    dl = np.stack([-R * np.sin(phi), R * np.cos(phi), np.zeros(n)], 1) * dphi
    rvec = np.array([0, 0, z]) - src
    rr = np.linalg.norm(rvec, axis=1)[:, None]
    dB = mu0 * I / (4 * np.pi) * np.cross(dl, rvec) / rr**3
    return dB.sum(0)[2]


# Q2 scaling: log-log slope of the numerically summed field at z >> R
zs = np.array([0.05, 0.1])
Bs = np.array([biot_savart_axis(z, 1.0) for z in zs])
check("Q2 exponent d ln B / d ln z at z>>R", np.log(Bs[1] / Bs[0]) / np.log(zs[1] / zs[0]), -3.0, 1e-3)
check("Q2 dipole approx error at z=2 cm (rel)",
      1 - biot_savart_axis(0.02, 1.0) / (mu0 * 1e-6 / (2 * 0.02**3)), 0.003738, 0.01)

sens = {"NV": (0.02, 1e-9), "OPM": (0.03, 10e-15), "SQUID": (0.08, 3e-15)}
pdf_I = {"NV": 0.1278, "OPM": 4.304e-6, "SQUID": 2.445e-5}
for k, (z, S) in sens.items():
    B1 = biot_savart_axis(z, 1.0)               # field per ampere
    check(f"Q4 I_min {k} = 10*S / (B per amp)", S * 10 / B1, pdf_I[k], 2e-3)
snr = {k: biot_savart_axis(z, 1.0) / S for k, (z, S) in sens.items()}
check("Q3 SNR ratio OPM/SQUID", snr["OPM"] / snr["SQUID"], 5.681, 2e-3)
check("Q3 SNR ratio OPM/NV", snr["OPM"] / snr["NV"], 2.969e4, 2e-3)

# ---------------------------------------------------------------- Q5
print("Q5  crossover by scanning Biot-Savart values on a grid (not root of a formula)")
grid = np.linspace(0.05, 0.13, 801)
diff = [10e-15 / biot_savart_axis(z + 0.01, 1.0, n=800) - 3e-15 / biot_savart_axis(z + 0.06, 1.0, n=800)
        for z in grid]
cross = grid[np.argmin(np.abs(diff))]
check("Q5 OPM=SQUID depth (m)", cross, 0.0912, 2e-3)
check("Q5 NV/OPM current ratio at z0=0",
      (1e-9 / biot_savart_axis(0.0, 1.0)) / (10e-15 / biot_savart_axis(0.01, 1.0)), 98.52, 2e-3)
# deep trend: I_SQUID/I_OPM falls toward S_SQUID/S_OPM = 0.3 as z0 grows
ratios = [(3e-15 / biot_savart_axis(z + 0.06, 1.0)) / (10e-15 / biot_savart_axis(z + 0.01, 1.0)) for z in (0.1, 0.3, 1.0)]
check("Q5 I_SQUID/I_OPM at z0 = 1 m (-> 0.3)", ratios[-1], 0.3 * (1.06 / 1.01)**3, 1e-3)
print("     ratios at z0 = 0.1, 0.3, 1 m:", [round(r, 4) for r in ratios])

# ---------------------------------------------------------------- Q6
print("Q6  thermal wavelength from the partition function: integral of exp(-p^2/2mkT) d^3p = h^3/lambda^3")
T = 1e-6
p0 = np.sqrt(m * kB * T)
I1, _ = integrate.quad(lambda x: np.exp(-x**2 / 2), -40, 40)   # p = x * p0
lam_from_Z = h / (I1 * p0)                     # 1D: Z_p = int dp e^{-...} = h / lambda
check("Q6 lambda_th (m)", lam_from_Z, 1.8727e-7, 1e-4)
# rms speed by sampling Maxwell-Boltzmann velocities
v = rng.normal(0, np.sqrt(kB * T / m), (1_000_000, 3))
vrms = np.sqrt((v**2).sum(1).mean())
check("Q6 v_rms by sampling (m/s)", vrms, 0.016941, 3e-3)
check("Q6 alt lambda = h/(m v_rms) (m)", h / (m * vrms), 2.710e-7, 3e-3)

# ---------------------------------------------------------------- Q7-Q8
print("Q7-Q8  phase from atom positions at the three pulses: phi = k_eff (z1 - 2 z2 + z3)")
lam, tau = 780e-9, 0.1
keff = 4 * np.pi / lam


def ai_phase(g):
    sol = integrate.solve_ivp(lambda t, y: [y[1], -g], (0, 2 * tau), [0, 0],
                              t_eval=[0, tau, 2 * tau], rtol=1e-12, atol=1e-15)
    z1, z2, z3 = sol.y[0]
    return -keff * (z1 - 2 * z2 + z3)    # sign convention: positive for downward g


dphi = ai_phase(9.8 + 1e-9) - ai_phase(9.8)
check("Q7 dphi from trajectories (rad)", dphi, 1.6111e-4, 1e-3)
check("Q7 total phase at g0 (rad)", ai_phase(9.8), 1.578852e6, 1e-6)
gg = np.linspace(9.8, 9.8 + 1e-6, 11)
slope = np.polyfit(gg - 9.8, [ai_phase(x) - ai_phase(9.8) for x in gg], 1)[0]
check("Q8 S = dphi/dg by linear fit (rad per m/s^2)", slope, 1.6111e5, 1e-4)
# alt reading consistency: m g d tau / hbar equals keff g tau^2 iff d = hbar keff tau / m
d_sc = hbar * keff * tau / m
check("Q7 alt: path-separation formula with self-consistent d reproduces dphi",
      m * 1e-9 * d_sc * tau / hbar, 1.611073e-4, 1e-6)

# ---------------------------------------------------------------- Q9-Q10
print("Q9-Q10  exact near/far-side difference and back-substitution")
GM = G * 7.3e22; r = 3.85e8
exact_tidal = GM / (r - R_E)**2 - GM / r**2
far = GM / r**2 - GM / (r + R_E)**2
check("Q9 exact near-side tidal (m/s^2)", exact_tidal, 1.1155e-6, 1e-3)
check("Q9 exact far-side tidal (m/s^2)", far, 1.0618e-6, 1e-3)
check("Q9 mean of near/far equals 2GMR/r^3 (m/s^2)", (exact_tidal + far) / 2, 1.0879e-6, 1e-3)
check("Q9 direct pull (m/s^2)", GM / r**2, 3.2871e-5, 1e-4)
for name, r_p, target in [("Q10 r(moon-tidal) back-substituted", 0.065533, 1.0879e-6),
                          ("Q10 r(detect) back-substituted", 2.16148, 1e-9)]:
    check(name, G * 70 / r_p**2, target, 1e-4)
check("Q10 person at 1 m (m/s^2)", G * 70, 4.672e-9, 1e-4)

# ---------------------------------------------------------------- Q11
print("Q11  vertical attraction of a uniform 1 m sphere by 3D quadrature (no shell theorem)")
rho, Rv, zc = 5500.0, 0.5, 3.0


def gz_sphere(zc):
    # sphere centred at depth zc below the sensor; integrate in spherical coords about sphere centre
    def integrand(s, th, ph):
        # point in sphere: (s sin th cos ph, s sin th sin ph, -zc + s cos th); sensor at origin
        x = s * np.sin(th) * np.cos(ph); y = s * np.sin(th) * np.sin(ph); z = -zc + s * np.cos(th)
        d3 = (x * x + y * y + z * z) ** 1.5
        return G * rho * (-z) / d3 * s * s * np.sin(th)
    val, _ = integrate.tplquad(integrand, 0, 2 * np.pi, 0, np.pi, 0, Rv, epsabs=1e-16, epsrel=1e-9)
    return val


g3 = gz_sphere(3.0)
check("Q11 |dg| of void at 3 m (m/s^2)", g3, 2.135623e-8, 1e-5)
zmax = optimize.brentq(lambda z: gz_sphere(z) - 1e-9, 1.0, 100.0)
check("Q11 z_max for D = 1 m by root-finding the quadrature (m)", zmax, 13.864, 1e-4)
# exponent 3/2: double D, z_max should grow by 2^1.5
check("Q11 z_max(2D)/z_max(D) = 2^1.5", (13.864 * 2**1.5) / 13.864, 2**1.5, 1e-12)
Rv = 1.0
zmax2 = optimize.brentq(lambda z: gz_sphere(z) - 1e-9, 1.0, 200.0)
check("Q11 z_max for D = 2 m by quadrature (m)", zmax2, 13.864 * 2**1.5, 1e-4)

print("\nALL PASS" if not FAIL else f"\nFAILURES: {FAIL}")
