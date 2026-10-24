"""Sketch of psi(x,0) for Week 2 Problem 1 (figures/psi_triangle.pdf)."""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

a, b = 1.0, 2.6
A = math.sqrt(3 / b)

fig, ax = plt.subplots(figsize=(5.6, 2.9))
ax.plot([-0.5, 0, a, b, b + 0.6], [0, 0, A, 0, 0], color="#1f4e9c", lw=2)
ax.fill_between([0, a, b], [0, A, 0], color="#1f4e9c", alpha=0.08)
ax.plot([a, a], [0, A], ls=":", color="0.4", lw=1)
ax.plot([-0.5, a], [A, A], ls=":", color="0.4", lw=1)
ax.annotate("peak: most probable position", xy=(a, A), xytext=(a + 0.35, A * 1.02),
            fontsize=9, arrowprops=dict(arrowstyle="->", color="0.3"))

ax.set_xticks([0, a, b], ["$0$", "$a$", "$b$"])
ax.set_yticks([0, A], ["$0$", r"$A=\sqrt{3/b}$"])
ax.set_xlabel("$x$")
ax.set_ylabel(r"$\psi(x,0)$")
ax.set_xlim(-0.5, b + 0.6)
ax.set_ylim(0, A * 1.25)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()

out = Path(__file__).with_name("figures")
out.mkdir(exist_ok=True)
fig.savefig(out / "psi_triangle.pdf")
print("wrote", out / "psi_triangle.pdf")
