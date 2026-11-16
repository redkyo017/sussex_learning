"""Primary computations for Module 4 Assessment 1 (PRB), candidate 672128.

Every number quoted in QT_PRB_solutions.tex comes from here. The closed-form
algebra of the written solutions is reproduced; verify.py then re-derives each
result by a different mechanism.

    ./.venv/bin/python compute.py      # prints results, writes figures/*.pdf
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- constants (CODATA 2018 exact/recommended) -------------------------------
h = 6.62607015e-34
hbar = h / (2 * np.pi)
kB = 1.380649e-23
u = 1.66053906660e-27
mu0 = 1.25663706212e-6
G = 6.67430e-11
m_Rb = 86.909180527 * u
R_E = 6.371e6

# =============================================================================
# Q1  OPM SNR
# =============================================================================
S1, BW1, Bsig1 = 50e-15, 1e3, 2e-12
noise1 = S1 * np.sqrt(BW1)
SNR1 = Bsig1 / noise1
Q1 = dict(noise=noise1, SNR=SNR1, SNR_dB=20 * np.log10(SNR1), SNR_power=SNR1**2,
          alt_SNR_1Hz=Bsig1 / S1)

# =============================================================================
# Q2-Q5  loop-current source
# =============================================================================
R = 1e-3
z0 = 2e-2
BW4 = 100.0
SENSORS = {  # name: (standoff from scalp [m], sensitivity [T/sqrt(Hz)])
    "NV": (0.0, 1e-9),
    "OPM": (1e-2, 10e-15),
    "SQUID": (6e-2, 3e-15),
}


def B_loop(z, I, R=R):
    return mu0 / 2 * R**2 * I / (z**2 + R**2) ** 1.5


def I_min(z, Bmin, R=R):
    """Current giving B = Bmin on axis at distance z (exact on-axis formula)."""
    return 2 * Bmin * (z**2 + R**2) ** 1.5 / (mu0 * R**2)


Q2 = dict(rel_err_at_2cm=1 - (1 + R**2 / z0**2) ** -1.5)

Q3 = {}
for name, (d, S) in SENSORS.items():
    z = z0 + d
    Q3[name] = dict(z=z, figure_of_merit=1 / (S * (z**2 + R**2) ** 1.5),
                    dipole_fom=1 / (S * z**3))
best = max(Q3, key=lambda k: Q3[k]["figure_of_merit"])
Q3["ratio_OPM_SQUID"] = Q3["OPM"]["figure_of_merit"] / Q3["SQUID"]["figure_of_merit"]
Q3["ratio_OPM_NV"] = Q3["OPM"]["figure_of_merit"] / Q3["NV"]["figure_of_merit"]
Q3["best"] = best

Q4 = {}
for name, (d, S) in SENSORS.items():
    z = z0 + d
    Bmin = S * np.sqrt(BW4)
    Q4[name] = dict(Bmin=Bmin, I=I_min(z, Bmin), I_dipole=2 * Bmin * z**3 / (mu0 * R**2),
                    I_alt_1Hz=I_min(z, S))

# Q5 limits and crossovers
Q5 = {}
for name, (d, S) in SENSORS.items():
    Bmin = S * np.sqrt(BW4)
    Q5[name] = dict(I_at_0=I_min(d, Bmin), I_at_10cm=I_min(0.10 + d, Bmin))
# deep limit (dipole, z0 >> standoffs): I ratio -> S ratio
Q5["deep_ratio_SQUID_OPM"] = 3e-15 / 10e-15
# closed-form crossover in the dipole approximation: S_O (z0+dO)^3 = S_S (z0+dS)^3
k = (10 / 3) ** (1 / 3)
Q5["cross_OPM_SQUID_dipole"] = (6e-2 - k * 1e-2) / (k - 1)
# NV vs OPM: S_NV z0^3 = S_OPM (z0+1cm)^3 -> z0 = 1cm / ((1e5)^(1/3) - 1)
kk = (1e-9 / 10e-15) ** (1 / 3)
Q5["cross_NV_OPM_dipole"] = 1e-2 / (kk - 1)


def make_q5_figure(path="figures/q5_Imin_vs_depth.pdf"):
    zz = np.linspace(0, 0.15, 3001)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    styles = {"NV": ("#d62728", "-"), "OPM": ("#1f77b4", "--"), "SQUID": ("#2ca02c", "-.")}
    for name, (d, S) in SENSORS.items():
        c, ls = styles[name]
        ax.semilogy(zz * 100, I_min(zz + d, S * np.sqrt(BW4)), color=c, ls=ls, lw=2,
                    label=f"{name}: standoff {d*100:.0f} cm, {S*1e15:g} fT/$\\sqrt{{\\mathrm{{Hz}}}}$"
                    if name != "NV" else f"NV: on scalp, 1 nT/$\\sqrt{{\\mathrm{{Hz}}}}$")
    x = Q5_cross_exact["OPM_SQUID"]
    ax.axvline(x * 100, color="grey", lw=0.8, ls=":")
    ax.annotate(f"OPM = SQUID\n$z_0\\approx{x*100:.1f}$ cm", xy=(x * 100, I_min(x + 0.01, 1e-13)),
                xytext=(x * 100 + 0.6, 1.5e-6), fontsize=9,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.axvline(2, color="black", lw=0.6, alpha=0.4)
    ax.text(2.15, 2e-2, "$z_0=2$ cm\n(Q4)", fontsize=8)
    ax.set_xlabel("Source depth below scalp $z_0$ (cm)")
    ax.set_ylabel("Minimum detectable loop current $I_{\\min}$ (A)")
    ax.set_xlim(0, 15)
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.6))
    ax.set_title("$R=1$ mm, SNR = 1 in a 100 Hz bandwidth", fontsize=10)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


from scipy.optimize import brentq
Q5_cross_exact = {
    "OPM_SQUID": brentq(lambda x: I_min(x + 0.01, 1e-13) - I_min(x + 0.06, 3e-14), 0.01, 0.2),
}
# NV vs OPM: no crossing for z0 >= 0 -- record the ratio at the surface instead
Q5_cross_exact["NV_over_OPM_at_0"] = I_min(0.0, 1e-8) / I_min(0.01, 1e-13)


# =============================================================================
# Q6-Q8  atom interferometer
# =============================================================================
T_at, lam, tau, d_sep, g0, dg = 1e-6, 780e-9, 0.1, 10e-3, 9.8, 1e-9
lam_dB_thermal = h / np.sqrt(2 * np.pi * m_Rb * kB * T_at)
v_rms = np.sqrt(3 * kB * T_at / m_Rb)
Q6 = dict(m=m_Rb, lam_thermal=lam_dB_thermal, v_rms=v_rms, lam_rms=h / (m_Rb * v_rms),
          v_mean=np.sqrt(8 * kB * T_at / (np.pi * m_Rb)),
          lam_mean=h / (m_Rb * np.sqrt(8 * kB * T_at / (np.pi * m_Rb))))

k_eff = 4 * np.pi / lam
Q7 = dict(k=2 * np.pi / lam, k_eff=k_eff, dphi=k_eff * dg * tau**2,
          phi_total=k_eff * g0 * tau**2,
          alt_single_k=2 * np.pi / lam * dg * tau**2,
          alt_d_formula=m_Rb * dg * d_sep * tau / hbar,
          d_selfconsistent=hbar * k_eff * tau / m_Rb,
          v_recoil=hbar * k_eff / m_Rb)
Q8 = dict(S=k_eff * tau**2, phase_per_uGal=k_eff * tau**2 * 1e-8)

# =============================================================================
# Q9-Q11  gravitational perturbations
# =============================================================================
M_moon, r_moon = 7.3e22, 3.85e8
Q9 = dict(direct=G * M_moon / r_moon**2, tidal=2 * G * M_moon * R_E / r_moon**3,
          tidal_horizon=G * M_moon * R_E / r_moon**3)
Q9["tidal_over_min"] = Q9["tidal"] / dg

m_p = 70.0
Q10 = dict(dg_1m=G * m_p / 1.0**2,
           r_match_tidal=np.sqrt(G * m_p / Q9["tidal"]),
           r_match_direct=np.sqrt(G * m_p / Q9["direct"]),
           r_detect=np.sqrt(G * m_p / dg))

rho = 5500.0
D, r_v = 1.0, 3.0
dm = rho * np.pi / 6 * D**3
Q11 = dict(dm=dm, dg=G * dm / r_v**2, dg_edge=G * dm / (r_v + D / 2) ** 2,
           coef=np.sqrt(G * rho * np.pi / (6 * dg)))
Q11["rmax_1m"] = Q11["coef"] * 1.0**1.5


def make_q11_figure(path="figures/q11_rmax_vs_diameter.pdf"):
    DD = np.logspace(-1, 1, 400)
    rmax = Q11["coef"] * DD**1.5
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.loglog(DD, rmax, lw=2, color="#1f77b4",
              label="$z_{\\max}=\\sqrt{\\pi G\\rho D^3/(6\\,\\Delta g_{\\min})}\\approx 13.9\\,D^{3/2}$")
    ax.fill_between(DD, rmax, 1e3, color="#d62728", alpha=0.08)
    ax.fill_between(DD, DD / 2, rmax, color="#2ca02c", alpha=0.10)
    ax.loglog(DD, DD / 2, color="grey", lw=0.8, ls=":")
    ax.text(0.13, 35, "not detectable\n($|\\Delta g| < 10^{-9}$ m/s$^2$)", fontsize=8, color="#a01010")
    ax.text(0.28, 0.32, "detectable", fontsize=8, color="#1a6e1a")
    ax.text(3.0, 0.9, "$z=D/2$: void reaches sensor", fontsize=7, color="grey")
    ax.plot([1], [Q11["rmax_1m"]], "o", color="black", ms=5)
    ax.annotate(f"$D=1$ m: $z_{{\\max}}\\approx{Q11['rmax_1m']:.1f}$ m", xy=(1, Q11["rmax_1m"]),
                xytext=(2.0, 6.0), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.plot([1], [3], "s", color="#ff7f0e", ms=5)
    ax.annotate("Q11 example ($D=1$ m, 3 m)", xy=(1, 3), xytext=(1.5, 0.35), fontsize=8,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.set_xlim(0.1, 10)
    ax.set_ylim(0.05, 600)
    ax.set_xlabel("Void diameter $D$ (m)")
    ax.set_ylabel("Maximum detectable depth of void centre $z_{\\max}$ (m)")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_title("$\\rho=5.5$ g/cm$^3$, $\\Delta g_{\\min}=1.0\\times10^{-9}$ m/s$^2$", fontsize=10)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


if __name__ == "__main__":
    def show(title, d):
        print(f"== {title} ==")
        for k_, v in d.items():
            print(f"   {k_}: {v}")
    for t, dct in [("Q1", Q1), ("Q2", Q2), ("Q3", Q3), ("Q4", Q4), ("Q5", Q5),
                   ("Q5 exact crossovers", Q5_cross_exact), ("Q6", Q6), ("Q7", Q7),
                   ("Q8", Q8), ("Q9", Q9), ("Q10", Q10), ("Q11", Q11)]:
        show(t, dct)
    make_q5_figure()
    make_q11_figure()
    print("figures written")
