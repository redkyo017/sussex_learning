"""Independent numerical check of every result in the Assessment 2 portfolio.

Nothing here reuses the algebra from the write-up: integrals are done by
quadrature, operator identities by finite differences or random matrices, the
oscillator by truncated ladder matrices evolved with scipy's expm and, separately,
by Hermite functions in position space, and the spins by numpy Kronecker products.

    python verify.py        (needs numpy, scipy)

Every line should report PASS.
"""

import math

import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import eval_hermite

FAILS = []


def ok(name, got, expected, tol=1e-6):
    good = abs(got - expected) < tol
    if not good:
        FAILS.append(name)
    print(f"  {'PASS' if good else 'FAIL'}  {name}: got {complex(got).real:.10g}"
          + (f"{complex(got).imag:+.3g}i" if abs(complex(got).imag) > 1e-12 else "")
          + f", expected {complex(expected).real:.10g}")


def check(name, cond):
    if not cond:
        FAILS.append(name)
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


rng = np.random.default_rng(672128)

# ----------------------------------------------------------------------------
print("== Week 2, Problem 1: triangular wave function (quadrature) ==")
for a, b in [(1.0, 3.0), (0.7, 1.9), (2.0, 4.0)]:
    A = math.sqrt(3 / b)
    psi = lambda x: A * x / a if 0 <= x <= a else (A * (b - x) / (b - a) if a <= x <= b else 0.0)
    norm = quad(lambda x: psi(x) ** 2, 0, a)[0] + quad(lambda x: psi(x) ** 2, a, b)[0]
    left = quad(lambda x: psi(x) ** 2, 0, a)[0]
    mean = quad(lambda x: x * psi(x) ** 2, 0, a)[0] + quad(lambda x: x * psi(x) ** 2, a, b)[0]
    xs = np.linspace(0, b, 200_001)
    mode = xs[np.argmax([psi(x) ** 2 for x in xs])]
    tag = f"(a={a}, b={b})"
    ok(f"(a) A = sqrt(3/b) normalises {tag}", norm, 1.0, 1e-9)
    ok(f"(c) most probable x = a {tag}", mode, a, 1e-4)
    ok(f"(d) P(x<a) = a/b {tag}", left, a / b, 1e-9)
    ok(f"(e) <x> = (2a+b)/4 {tag}", mean, (2 * a + b) / 4, 1e-9)

# limiting cases, approached numerically from the general integral
a = 1.0
for b, expect_P, expect_x in [(2.0, 0.5, 1.0), (1.0 + 1e-6, 1.0, 0.75)]:
    A = math.sqrt(3 / b)
    left = quad(lambda x: (A * x / a) ** 2, 0, a)[0]
    right = quad(lambda x: (A * (b - x) / (b - a)) ** 2, a, b)[0]
    mean = (quad(lambda x: x * (A * x / a) ** 2, 0, a)[0]
            + quad(lambda x: x * (A * (b - x) / (b - a)) ** 2, a, b)[0])
    ok(f"(d) limit b -> {b:.6g}a: P(x<a)", left / (left + right), expect_P, 1e-5)
    ok(f"(e) limit b -> {b:.6g}a: <x>/a", mean, expect_x, 1e-5)

# ----------------------------------------------------------------------------
print("\n== Week 2, Problem 2: inner-product axioms on random complex vectors ==")
ip = lambda B, A: sum(np.conj(B[i]) * A[i] for i in range(3))   # the given definition
cvec = lambda: rng.normal(size=3) + 1j * rng.normal(size=3)
worst_sym = worst_lin = 0.0
min_pos = np.inf
for _ in range(1000):
    A, B, C = cvec(), cvec(), cvec()
    c1, c2 = complex(*rng.normal(size=2)), complex(*rng.normal(size=2))
    worst_sym = max(worst_sym, abs(ip(B, A) - np.conj(ip(A, B))))
    worst_lin = max(worst_lin, abs(ip(C, c1 * A + c2 * B) - (c1 * ip(C, A) + c2 * ip(C, B))))
    val = ip(A, A)
    min_pos = min(min_pos, val.real)
    check_imag = abs(val.imag) < 1e-12
    if not check_imag:
        FAILS.append("<A|A> real")
ok("conjugate symmetry, worst |<B|A> - <A|B>*|", worst_sym, 0.0, 1e-12)
ok("linearity in 2nd argument, worst residual", worst_lin, 0.0, 1e-12)
check(f"<A|A> real and > 0 for 1000 random A (min {min_pos:.3g})", min_pos > 0)
ok("<0|0> = 0", ip(np.zeros(3), np.zeros(3)), 0.0, 1e-15)

# ----------------------------------------------------------------------------
print("\n== Week 3, Problem 1: x and p Hermitian (grid quadrature, finite differences) ==")
hbar = 1.0
x = np.linspace(-30, 30, 600_001)
dx = x[1] - x[0]
phi = (1 + 0.4j * x) * np.exp(-0.3 * x ** 2 + 1.1j * x)
psi = (0.5 - x + 0.2j * x ** 2) * np.exp(-0.5 * (x - 1) ** 2 - 0.7j * x)
inner = lambda f, g: np.trapezoid(np.conj(f) * g, x)
p_op = lambda f: (hbar / 1j) * np.gradient(f, dx)
ok("<phi|x psi> = <x phi|psi>", abs(inner(phi, x * psi) - inner(x * phi, psi)), 0.0, 1e-9)
ok("<phi|p psi> = <p phi|psi>", abs(inner(phi, p_op(psi)) - inner(p_op(phi), psi)), 0.0, 1e-6)
D = lambda f: np.gradient(f, dx)
ok("d/dx alone is anti-Hermitian: <phi|D psi> + <D phi|psi>",
   abs(inner(phi, D(psi)) + inner(D(phi), psi)), 0.0, 1e-6)

# ----------------------------------------------------------------------------
print("\n== Week 3, Problem 2: hydrogen 1s, relative probabilities ==")
a0 = 52.9177210544          # pm (CODATA 2022 Bohr radius)
N2 = 1 / (math.pi * a0 ** 3)
radial = quad(lambda r: 4 * math.pi * r ** 2 * N2 * math.exp(-2 * r / a0), 0, 50 * a0)[0]
ok("1s density 1/(pi a0^3) e^{-2r/a0} is normalised (radial quadrature)", radial, 1.0, 1e-9)
P0, Pa = N2 * 1.0, N2 * math.exp(-2) * 1.0
ok("P(nucleus, 1 pm^3) = 2.15e-6", P0 / 1e-6, 2.15, 0.006)
ok("P(r=a0, 1 pm^3) = 2.91e-7", Pa / 1e-7, 2.91, 0.006)
ok("ratio = e^2 = 7.389", P0 / Pa, 7.389, 0.001)
# small-but-finite cube: averaging |psi|^2 over a 1 pm cube barely changes the ratio
s = 1.0
pts = (np.arange(20) + 0.5) / 20 * s - s / 2
X, Y, Z = np.meshgrid(pts, pts, pts, indexing="ij")
dens = lambda cx: np.mean(N2 * np.exp(-2 * np.sqrt((X + cx) ** 2 + Y ** 2 + Z ** 2) / a0))
ratio_cube = dens(0.0) / dens(a0)
# the 1s cusp at r=0 makes the point-value approximation ~2% generous at the nucleus
check(f"finite-cube ratio {ratio_cube:.4f} within 2% of e^2 (approximation error "
      f"{100 * (1 - ratio_cube / math.e ** 2):.1f}%)", abs(ratio_cube / math.e ** 2 - 1) < 0.02)

# ----------------------------------------------------------------------------
print("\n== Week 4, Problem 1: three-state probabilities ==")
c = np.array([math.sqrt(3) / 3, 2 / 3, math.sqrt(2) / 3])
ok("norm = 1", np.vdot(c, c).real, 1.0, 1e-12)
for i, (p, n) in enumerate(zip([1 / 3, 4 / 9, 2 / 9], [270, 360, 180]), 1):
    ok(f"P(phi_{i})", abs(c[i - 1]) ** 2, p, 1e-12)
    ok(f"N(phi_{i}) of 810", 810 * abs(c[i - 1]) ** 2, n, 1e-9)
# Monte Carlo: 810 systems repeatedly; average counts approach the expectation
runs = rng.multinomial(810, np.abs(c) ** 2, size=20_000)
counts, spread = runs.mean(axis=0), runs.std(axis=0)
check(f"Monte Carlo mean counts {np.round(counts, 1)} ~ (270, 360, 180)",
      np.allclose(counts, [270, 360, 180], atol=1.0))
sd = np.sqrt(810 * np.abs(c) ** 2 * (1 - np.abs(c) ** 2))
check(f"binomial spreads {np.round(sd, 2)} = (13.42, 14.14, 11.83), i.e. 12-14",
      np.allclose(sd, [13.42, 14.14, 11.83], atol=0.01))
check(f"Monte Carlo spreads {np.round(spread, 2)} match binomial within 2%",
      np.allclose(spread, sd, rtol=0.02))

# ----------------------------------------------------------------------------
print("\n== Week 4, Problem 2: Hermitian algebra on random matrices ==")
herm = lambda n: (lambda M: (M + M.conj().T) / 2)(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
isherm = lambda M: np.allclose(M, M.conj().T)
Q, R = herm(4), herm(4)
check("(a) Q + R Hermitian", isherm(Q + R))
check("(b) 2.7 Q Hermitian (alpha real)", isherm(2.7 * Q))
check("(b) (2.7 + 0.5i) Q NOT Hermitian", not isherm((2.7 + 0.5j) * Q))
check("(b) i Q is anti-Hermitian", np.allclose((1j * Q).conj().T, -1j * Q))
check("(c) QR NOT Hermitian for generic non-commuting Q, R", not isherm(Q @ R))
check("(c) (QR)^dagger = RQ", np.allclose((Q @ R).conj().T, R @ Q))
U = np.linalg.qr(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))[0]
Qc = U @ np.diag(rng.normal(size=4)) @ U.conj().T
Rc = U @ np.diag(rng.normal(size=4)) @ U.conj().T          # shares eigenvectors -> commutes
check("(c) QR Hermitian when [Q,R] = 0", isherm(Qc @ Rc) and np.allclose(Qc @ Rc, Rc @ Qc))
# (d) H on a grid: <f|Hg> vs <Hf|g> with second derivative by finite differences
m, V = 1.0, lambda xx: 0.5 * xx ** 2 + 0.1 * xx ** 4
H = lambda f: -(hbar ** 2) / (2 * m) * np.gradient(np.gradient(f, dx), dx) + V(x) * f
ok("(d) <phi|H psi> = <H phi|psi>", abs(inner(phi, H(psi)) - inner(H(phi), psi)), 0.0, 1e-5)
Vc = lambda xx: 0.5 * xx ** 2 + 0.3j
Hc = lambda f: -(hbar ** 2) / (2 * m) * np.gradient(np.gradient(f, dx), dx) + Vc(x) * f
check("(d) complex V breaks Hermiticity (control)",
      abs(inner(phi, Hc(psi)) - inner(Hc(phi), psi)) > 1e-2)

# ----------------------------------------------------------------------------
print("\n== Week 5: oscillator via truncated ladder matrices and expm (hbar=m=omega=1) ==")
Nmax = 40
a_m = np.diag(np.sqrt(np.arange(1, Nmax)), 1)
X = (a_m + a_m.T) / math.sqrt(2)
P = 1j * (a_m.T - a_m) / math.sqrt(2)
Hm = P @ P / 2 + X @ X / 2           # built from x and p, not from n + 1/2
psi0 = np.zeros(Nmax, complex)
psi0[:3] = np.array([5, 4, 3]) / math.sqrt(50)
ok("P1 norm", np.vdot(psi0, psi0).real, 1.0, 1e-12)
ok("P1(a) <E> = 59/50 hbar omega", np.vdot(psi0, Hm @ psi0).real, 59 / 50, 1e-9)
for t in [0.0, 0.4, 1.3, 2.9]:
    pt = expm(-1j * Hm * t) @ psi0
    ok(f"P1(b) <E>(t={t}) unchanged", np.vdot(pt, Hm @ pt).real, 59 / 50, 1e-9)
    ok(f"P1(c) <x>(t={t}) = (20+12sqrt2)/25 sqrt(1/2) cos t",
       np.vdot(pt, X @ pt).real, (20 + 12 * math.sqrt(2)) / 25 / math.sqrt(2) * math.cos(t), 1e-9)

psi2 = np.zeros(Nmax, complex)
psi2[1], psi2[2] = 1 / math.sqrt(2), -1j / math.sqrt(2)
ok("P2 <p>(0) = -sqrt(m hbar omega)", np.vdot(psi2, P @ psi2), -1.0, 1e-9)
for t in [0.5, 2.0]:
    pt = expm(-1j * Hm * t) @ psi2
    ok(f"P2 <p>(t={t}) = -cos t", np.vdot(pt, P @ pt), -math.cos(t), 1e-9)
    ok(f"P2 <x>(t={t}) = -sin t", np.vdot(pt, X @ pt), -math.sin(t), 1e-9)
for coef, want, label in [(+1j, +1.0, "+i flips the sign"), (1.0, 0.0, "real coefficient gives 0")]:
    v = np.zeros(Nmax, complex)
    v[1], v[2] = 1 / math.sqrt(2), coef / math.sqrt(2)
    ok(f"P2 variant: {label}", np.vdot(v, P @ v), want, 1e-9)
alt = np.zeros(Nmax, complex)
alt[0], alt[1] = 1 / math.sqrt(2), -1j / math.sqrt(2)
ok("P2 alternative reading (n=0,1): <p> = -sqrt(m hbar omega/2)", np.vdot(alt, P @ alt), -1 / math.sqrt(2), 1e-9)

print("\n== Week 5, Problem 2 again: Hermite functions in position space ==")
xg = np.linspace(-15, 15, 300_001)
dxg = xg[1] - xg[0]
phin = lambda n: (np.pi ** -0.25 / math.sqrt(2 ** n * math.factorial(n))
                  * eval_hermite(n, xg) * np.exp(-xg ** 2 / 2))
wave = (phin(1) - 1j * phin(2)) / math.sqrt(2)
ok("position-space norm", np.trapezoid(abs(wave) ** 2, xg), 1.0, 1e-9)
ok("<p> = int psi* (-i d/dx) psi dx", np.trapezoid(np.conj(wave) * (-1j) * np.gradient(wave, dxg), xg), -1.0, 1e-6)
wave5 = (5 * phin(0) + 4 * phin(1) + 3 * phin(2)) / math.sqrt(50)
ok("W5 P1(c) at t=0: <x> = int x |psi|^2", np.trapezoid(xg * abs(wave5) ** 2, xg),
   (20 + 12 * math.sqrt(2)) / 25 / math.sqrt(2), 1e-9)

# ----------------------------------------------------------------------------
print("\n== Week 7: singlet with Kronecker products ==")
I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0, -1.0]).astype(complex)
up, dn = np.array([1, 0], complex), np.array([0, 1], complex)
S = (np.kron(up, dn) - np.kron(dn, up)) / math.sqrt(2)
SxA, TyB = np.kron(sx, I2), np.kron(I2, sy)
ev = lambda O: np.vdot(S, O @ S)
ok("(a) <sigma_x tau_y>", ev(SxA @ TyB), 0.0, 1e-12)
ok("(b) <tau_y>", ev(TyB), 0.0, 1e-12)
ok("(b) <sigma_x>", ev(SxA), 0.0, 1e-12)
ok("(c) correlation", ev(SxA @ TyB) - ev(SxA) * ev(TyB), 0.0, 1e-12)
check("[sigma_x x 1, 1 x tau_y] = 0, so order of measurement is irrelevant",
      np.allclose(SxA @ TyB, TyB @ SxA))
T0 = (np.kron(up, dn) + np.kron(dn, up)) / math.sqrt(2)
check("sigma_x tau_y |S> = -i |T0> (orthogonal to |S>)", np.allclose(SxA @ TyB @ S, -1j * T0))
# full correlation matrix: <sigma_i tau_j> = -delta_ij, the known singlet result
paulis = [sx, sy, sz]
M = np.array([[ev(np.kron(p, I2) @ np.kron(I2, q)).real for q in paulis] for p in paulis])
check("singlet correlation matrix = -identity", np.allclose(M, -np.eye(3)))
# sequential-measurement simulation: Bob measures tau_y, state collapses, Alice measures sigma_x
proj = lambda O, s: (np.eye(4) + s * O) / 2
joint = sum(sa * sb * np.vdot(S, proj(SxA, sa) @ proj(TyB, sb) @ S).real
            for sa in (1, -1) for sb in (1, -1))
ok("sum over outcomes of s_A s_B P(s_A, s_B)", joint, 0.0, 1e-12)
for sb in (1, -1):
    pb = np.vdot(S, proj(TyB, sb) @ S).real
    post = proj(TyB, sb) @ S / math.sqrt(pb)
    ok(f"P(Bob tau_y = {sb:+d})", pb, 0.5, 1e-12)
    ok(f"Alice <sigma_x> after Bob gets {sb:+d}", np.vdot(post, SxA @ post), 0.0, 1e-12)
    ok(f"Alice <sigma_y> after Bob gets {sb:+d} (perfect anticorrelation, control)",
       np.vdot(post, np.kron(sy, I2) @ post), -sb, 1e-12)

print(f"\n{'ALL PASS' if not FAILS else 'FAILURES: ' + ', '.join(FAILS)}")
