"""Independent numerical check of an assignment's results.

The rule this encodes: a check that re-runs the same algebra is not a check.
Every function below arrives at the answer by a DIFFERENT mechanism than the
written derivation - quadrature instead of an antiderivative, finite
differences instead of the product rule, an eigensolver instead of a
characteristic polynomial.

Copy this next to the solutions, delete what does not apply, and keep it so
the numbers can be re-checked after any edit.

Needs numpy (absent from system Python on this machine):
    python3 -m venv .venv && ./.venv/bin/pip install numpy matplotlib
    ./.venv/bin/python verify_template.py
"""

import numpy as np

FAILURES = []


def check(name, got, expected, tol=1e-6):
    """Compare and record. Prints PASS/FAIL so the whole run is auditable."""
    got, expected = float(got), float(expected)
    ok = abs(got - expected) < tol
    if not ok:
        FAILURES.append(name)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: got {got:.10g}, expected {expected:.10g}")


# ---------------------------------------------------------------------
# 1. Integrals -> numerical quadrature
#    Derivation used an antiderivative; this uses a fine grid instead.
# ---------------------------------------------------------------------
def check_integrals():
    print("== normalisation and expectation values ==")
    lam = 1.9                                  # arbitrary test value
    A2 = lam                                   # claim: A = sqrt(lambda)
    x = np.linspace(-120 / lam, 120 / lam, 4_000_001)   # wide tails, fine grid
    with np.errstate(over="ignore"):           # np.where evaluates both branches
        rho = A2 * np.exp(-2 * lam * np.abs(x))

    check("normalisation = 1", np.trapezoid(rho, x), 1.0, 1e-5)
    check("<x> = 0 by symmetry", np.trapezoid(x * rho, x), 0.0, 1e-5)
    check("<x^2> = 1/(2 lambda^2)",
          np.trapezoid(x**2 * rho, x), 1 / (2 * lam**2), 1e-5)


# ---------------------------------------------------------------------
# 2. Operator identities -> finite differences
#    Derivation used the product rule; this never differentiates by hand.
#    Test with a wave function UNRELATED to the one in the question, so a
#    result that only holds for the special case cannot pass.
# ---------------------------------------------------------------------
def check_commutator():
    print("\n== operator identities ==")
    hbar, h = 1.0, 1e-6
    x0 = np.array([0.37, -1.2, 2.5])
    psi = lambda x: np.exp(-0.8 * x**2) * (1 + 0.5 * x**3) + 0.3 * np.cos(1.7 * x)
    d = lambda f, x: (f(x + h) - f(x - h)) / (2 * h)

    xp = x0 * (hbar / 1j) * d(psi, x0)                 # x p psi
    px = (hbar / 1j) * d(lambda x: x * psi(x), x0)     # p x psi
    check("[x,p] psi = i hbar psi",
          np.max(np.abs((xp - px) - 1j * hbar * psi(x0))), 0.0)


# ---------------------------------------------------------------------
# 3. Matrices -> numpy.linalg, not a characteristic polynomial
# ---------------------------------------------------------------------
def check_matrix():
    print("\n== matrix properties ==")
    A = np.array([[-3, 2j], [-2j, -3]])
    print(f"  {'PASS' if np.allclose(A.conj().T, A) else 'FAIL'}  A is Hermitian")
    ev, evec = np.linalg.eig(A)
    ev = np.sort(ev.real)
    check("lower eigenvalue", ev[0], -5.0, 1e-9)
    check("upper eigenvalue", ev[1], -1.0, 1e-9)
    check("eigenvectors orthogonal",
          abs(np.vdot(evec[:, 0], evec[:, 1])), 0.0, 1e-9)


# ---------------------------------------------------------------------
# 4. Probabilities -> must be in [0,1] and sum to 1.
#    This catches a skipped normalisation step, which is the single most
#    common error in measurement questions.
# ---------------------------------------------------------------------
def check_probabilities():
    print("\n== probability set ==")
    coeffs = np.array([1 / np.sqrt(2), 0.5, 0.5j])     # expansion coefficients
    norm = np.vdot(coeffs, coeffs).real
    P = np.abs(coeffs) ** 2 / norm                     # divide by norm ALWAYS
    check("state norm", norm, 1.0)
    check("probabilities sum to 1", P.sum(), 1.0)
    for i, p in enumerate(P, 1):
        assert 0.0 <= p <= 1.0, f"P{i} outside [0,1]"
    check("P(b2)", P[1], 0.25)


if __name__ == "__main__":
    check_integrals()
    check_commutator()
    check_matrix()
    check_probabilities()
    print("\n" + ("ALL CHECKS PASSED" if not FAILURES
                  else f"FAILURES: {', '.join(FAILURES)}"))
