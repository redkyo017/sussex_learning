"""Generate the probability-density sketch for Assessment 1, Question 2.

rho(x) = |psi(x)|^2 with psi(x) = B exp(beta x)   for x < 0
                              = B exp(-2 beta x) for x >= 0
and B^2 = 4 beta / 3 (Question 3).

Everything is plotted in dimensionless units: the horizontal axis is
beta*x and the vertical axis is rho/beta, so the figure is valid for any
positive beta.  Marked: the mean <x> = -1/(4 beta) (Question 4) and the
most likely position x = 0 (Question 5).
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

B2 = 4.0 / 3.0          # B^2 in units of beta
MEAN = -0.25            # <x> in units of 1/beta
PEAK = B2               # rho(0) in units of beta

u_left = np.linspace(-3.0, 0.0, 600)    # u = beta * x
u_right = np.linspace(0.0, 1.5, 600)

rho_left = B2 * np.exp(2.0 * u_left)
rho_right = B2 * np.exp(-4.0 * u_right)

fig, ax = plt.subplots(figsize=(7.2, 4.4))

ax.plot(u_left, rho_left, color="#1f4e79", lw=2.2,
        label=r"$|\psi|^2=B^2e^{2\beta x}$   $(x<0)$")
ax.plot(u_right, rho_right, color="#a4260a", lw=2.2,
        label=r"$|\psi|^2=B^2e^{-4\beta x}$   $(x\geq 0)$")

# most likely position: the cusp at x = 0
ax.plot([0.0], [PEAK], marker="o", ms=8, color="black", zorder=5)
ax.annotate(r"most likely position $x=0$" "\n" r"$|\psi(0)|^2=B^2=\dfrac{4\beta}{3}$",
            xy=(0.0, PEAK), xytext=(0.42, 1.18),
            fontsize=9.5,
            arrowprops=dict(arrowstyle="->", lw=1.1, color="black"))

# mean position: horizontal leader, kept above the curve so it crosses nothing
ax.axvline(MEAN, color="#2e7d32", ls="--", lw=1.6)
ax.annotate(r"$\langle x\rangle=-\dfrac{1}{4\beta}$",
            xy=(MEAN, 1.02), xytext=(-2.55, 0.98),
            fontsize=10.5, color="#2e7d32", va="center",
            arrowprops=dict(arrowstyle="->", lw=1.2, color="#2e7d32"))

# decay lengths, to make the asymmetry explicit
ax.annotate("", xy=(-0.5, 0.49), xytext=(0.0, 0.49),
            arrowprops=dict(arrowstyle="<->", lw=1.0, color="#1f4e79"))
ax.text(-0.25, 0.60, r"$\dfrac{1}{2\beta}$", fontsize=9.5, color="#1f4e79",
        ha="center")
ax.annotate("", xy=(0.0, 0.49), xytext=(0.25, 0.49),
            arrowprops=dict(arrowstyle="<->", lw=1.0, color="#a4260a"))
ax.text(0.125, 0.60, r"$\dfrac{1}{4\beta}$", fontsize=9.5, color="#a4260a",
        ha="center")
ax.text(0.36, 0.455, r"(widths at $B^2/e$)", fontsize=8.5, color="#555555")

ax.set_xlabel(r"position  $\beta x$", fontsize=11)
ax.set_ylabel(r"probability density  $|\psi(x)|^2/\beta$", fontsize=11)
ax.set_xlim(-3.0, 1.5)
ax.set_ylim(0.0, 1.60)
ax.axhline(0.0, color="black", lw=0.8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(loc="upper left", fontsize=9.5, frameon=False)
ax.grid(alpha=0.18)
fig.tight_layout()

out = "figures/psi_probability_density.png"
fig.savefig(out, dpi=220)
print("wrote", out)
