"""Independent numerical check of every result in the Assessment 1 solutions.

Nothing here reuses the algebra from the write-up: the integrals are done by
quadrature, the commutator by finite differences, and the matrix results by
numpy's eigensolver.  Run it with the same venv as make_figure.py:

    ./.venv/bin/python verify.py

All 28 checks should report PASS.
"""

import numpy as np


def ok(name, got, expected, tol=1e-6):
    print(f"  {'PASS' if abs(got - expected) < tol else 'FAIL'}  {name}: "
          f"got {got:.10g}, expected {expected:.10g}")


print("== Q2-Q5: the piecewise exponential state (quadrature, beta = 1.7) ==")
beta = 1.7
B2 = 4 * beta / 3
xs = np.linspace(-200 / beta, 200 / beta, 40_000_001)
with np.errstate(over="ignore"):        # np.where evaluates both branches
    rho = B2 * np.where(xs < 0, np.exp(2 * beta * xs), np.exp(-4 * beta * xs))

norm = np.trapezoid(rho, xs)
mean = np.trapezoid(xs * rho, xs)
sq = np.trapezoid(xs**2 * rho, xs)
ok("Q3  normalisation integral = 1", norm, 1.0, 1e-5)
ok("Q3  B = 2 sqrt(beta/3)", np.sqrt(B2), 2 * np.sqrt(beta / 3))
ok("Q4  <x> = -1/(4 beta)", mean, -1 / (4 * beta), 1e-5)
ok("Q4  <x^2> = 3/(8 beta^2)", sq, 3 / (8 * beta**2), 1e-5)
ok("Q4  Delta x = sqrt(5)/(4 beta)", np.sqrt(sq - mean**2),
   np.sqrt(5) / (4 * beta), 1e-5)
imax = int(np.argmax(rho))
ok("Q5  mode at x = 0", xs[imax], 0.0, 1e-4)
ok("Q5  peak height = 4 beta/3", rho[imax], 4 * beta / 3, 1e-4)

print("\n== Q1: Hermiticity and spectrum ==")
A = np.array([[-3, 2j], [-2j, -3]])
print("  PASS  A^dagger == A" if np.allclose(A.conj().T, A) else "  FAIL  A^dagger != A")
ev, evec = np.linalg.eig(A)
ev = np.sort(ev.real)
ok("Q1  lower eigenvalue", ev[0], -5.0, 1e-9)
ok("Q1  upper eigenvalue", ev[1], -1.0, 1e-9)
ok("Q1  eigenvectors orthogonal", abs(np.vdot(evec[:, 0], evec[:, 1])), 0.0, 1e-9)
sigma_y = np.array([[0, -1j], [1j, 0]])
print("  PASS  A == -3 I - 2 sigma_y"
      if np.allclose(A, -3 * np.eye(2) - 2 * sigma_y) else "  FAIL  sigma_y identity")

print("\n== Q6-Q9: the commutator, by finite differences ==")
hbar, N, k, h = 1.0, 1.3, 2.1, 1e-6
phi = lambda x: N * np.sin(k * x)
deriv = lambda f, x: (f(x + h) - f(x - h)) / (2 * h)
x0 = np.array([0.37, -1.2, 2.5])

a = x0 * (hbar / 1j) * deriv(phi, x0)                  # x p
b = (hbar / 1j) * deriv(lambda x: x * phi(x), x0)      # p x
ok("Q6  = -i hbar N k x cos(kx)",
   np.max(np.abs(a - (-1j * hbar * N * k * x0 * np.cos(k * x0)))), 0.0)
ok("Q7  = -i hbar N [sin(kx) + kx cos(kx)]",
   np.max(np.abs(b - (-1j * hbar * N * (np.sin(k * x0) + k * x0 * np.cos(k * x0))))), 0.0)
ok("Q8  (a) - (b) = i hbar phi", np.max(np.abs((a - b) - 1j * hbar * phi(x0))), 0.0)

# Q9: an unrelated general wave function, to show the result is state-independent
psi = lambda x: np.exp(-0.8 * x**2) * (1 + 0.5 * x**3) + 0.3 * np.cos(1.7 * x)
a2 = x0 * (hbar / 1j) * deriv(psi, x0)
b2 = (hbar / 1j) * deriv(lambda x: x * psi(x), x0)
ok("Q9  [x,p] psi = i hbar psi (general psi)",
   np.max(np.abs((a2 - b2) - 1j * hbar * psi(x0))), 0.0)

print("\n== Q10: Born rule on an un-normalised state ==")
c = np.array([1 / np.sqrt(3), -np.sqrt(2) / np.sqrt(3), 1j / np.sqrt(3)])   # template
ok("Q10 <psi|psi>", np.vdot(c, c).real, 4 / 3)
P = np.abs(c) ** 2 / np.vdot(c, c).real
ok("Q10 P(a3)", P[2], 0.25)
ok("Q10 probabilities sum to 1", P.sum(), 1.0)

# the two rival readings of the sqrt-stripped Canvas export (see NOTES.md)
cc = np.array([1 / 3, -2 / 3, 1j / 3])
ok("Q10 canvas-literal variant = 1/6",
   (np.abs(cc) ** 2 / np.vdot(cc, cc).real)[2], 1 / 6)
c3 = np.array([1 / 3, -np.sqrt(2) / 3, 1j / 3])
ok("Q10 other sqrt reading also = 1/4",
   (np.abs(c3) ** 2 / np.vdot(c3, c3).real)[2], 0.25)

print("\n== Q11-Q13: energy and A measurements ==")
alpha = np.array([np.sqrt(2), np.sqrt(3), 1, 1]) / np.sqrt(7)
ok("Q11 state normalised", np.vdot(alpha, alpha).real, 1.0)
P = np.abs(alpha) ** 2
n = np.arange(1, 5)
ok("Q11 P(E0) = 2/7", P[0], 2 / 7)
ok("Q11 P(4E0) = 3/7", P[1], 3 / 7)
ok("Q11 P(9E0) = 1/7", P[2], 1 / 7)
ok("Q11 P(16E0) = 1/7", P[3], 1 / 7)
ok("Q11 <H> = 39/7 E0", (P * n**2).sum(), 39 / 7)
ok("Q12 <A> = 22/7 a0", (P * (n + 1)).sum(), 22 / 7)
sel = np.where(n**2 == 4)[0]
ok("Q13 energy 4E0 selects a unique n", len(sel), 1)
ok("Q13 that n is 2", n[sel][0], 2)
ok("Q13 A after collapse = 3 a0", n[sel][0] + 1, 3)
