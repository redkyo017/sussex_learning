# Week 5 Companion — The quantum harmonic oscillator

**Built on:** [Day 4](../day04.md) (Gaussian integrals, expectation values) and [Day 6](../day06.md) (the oscillator toolkit). Reading order and the five-pass protocol are in [STRATEGY](../../STRATEGY.md).

**How to use it.** Read the "really saying" section first (pass 1). Keep the notation decoder open next to the lecture (pass 2). Use "Skipped steps" when a line of §5.3 to §5.5 does not follow. Then attempt the Week 5 task cold, in the six-steps format, *before* you read the worked clones. The clones use different states from the task on purpose: you are meant to learn the technique and then carry it over yourself.

## What this week is really saying

Picture a marble in a smooth bowl, or a mass on a spring. The potential energy is a parabola, $V(x)=\tfrac12 m\omega^2x^2$. Classically the marble can have any energy at all, including zero (sitting still at the bottom).

Quantum mechanically three things change:

1. **Energy comes in equal steps.** The allowed energies are $E_n=\hbar\omega\left(n+\tfrac12\right)$ with $n=0,1,2,\dots$ Each rung of the ladder is exactly $\hbar\omega$ above the one below. That is a "quantum" of oscillator energy.
2. **There is a ladder, and two operators to walk on it.** The raising operator $\hat a^\dagger$ climbs one rung (adds one quantum). The lowering operator $\hat a$ descends one rung (removes one quantum). The number operator $\hat N=\hat a^\dagger\hat a$ simply reads off which rung you are on.
3. **The ladder has a bottom, and the bottom is not zero.** Lowering the ground state gives nothing at all: $\hat a|0\rangle=0$. So the ground state is where the ladder stops. It still has energy $\tfrac12\hbar\omega$ (the zero-point energy) because position and momentum cannot both be sharp, so the particle can never be perfectly at rest at the bottom.

The lecture's trick is worth naming. Solving the Schrödinger equation for this potential directly is "no easy job". Instead the lecture works entirely with **commutators**: from $[\hat x,\hat p]=i\hbar$ it derives $[\hat a,\hat a^\dagger]=1$, and everything else (equal steps, the bottom of the ladder, the $\sqrt n$ factors) drops out of that one line of algebra. This is the "linear algebra in Dirac notation" pattern again: operators acting on kets.

The second half of the story is the wave functions: each $\psi_n(x)$ is a **polynomial of degree $n$ times a Gaussian** (Eq. 5.31). The Gaussian tail makes the state normalisable; the polynomial creates the $n$ nodes.

## Notation decoder

The lecture writes the states as $|\psi_n\rangle$. Below I shorten that to $|n\rangle$ when only the label matters. Equation numbers are the lecture's.

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\omega$ | "omega" | angular frequency of the classical motion, $\omega=\sqrt{k/m}$ (Eq. 5.2) | a stiffer spring has larger $\omega$, so the rungs are further apart |
| $\hbar\omega$ | "h-bar omega" | the size of one energy quantum; the gap between neighbouring rungs | $E_2-E_1=\hbar\omega$ |
| $\hat H$ | "H-hat" | the energy operator (Eq. 5.4): $\hat p^2/2m+\tfrac12m\omega^2\hat x^2$ | $\hat H\vert n\rangle=E_n\vert n\rangle$ |
| $\hat a$ | "a-hat" or "the lowering operator" | $\hat a=\dfrac1{\sqrt2}\left(\sqrt{\dfrac{m\omega}{\hbar}}\,\hat x+i\dfrac1{\sqrt{m\hbar\omega}}\,\hat p\right)$ (Eq. 5.6) | $\hat a\vert 3\rangle=\sqrt3\,\vert 2\rangle$ |
| $\hat a^\dagger$ | "a-dagger" or "the raising operator" | $\hat a^\dagger=\dfrac1{\sqrt2}\left(\sqrt{\dfrac{m\omega}{\hbar}}\,\hat x-i\dfrac1{\sqrt{m\hbar\omega}}\,\hat p\right)$ (Eq. 5.7); the adjoint of $\hat a$ | $\hat a^\dagger\vert 3\rangle=2\,\vert 4\rangle$ |
| $\dagger$ | "dagger" | conjugate transpose ([Move 3.3](../day03.md)); reverses the order of a product | $(\hat a^\dagger\hat a)^\dagger=\hat a^\dagger\hat a$ |
| $\hat N$ | "N-hat" or "the number operator" | $\hat N=\hat a^\dagger\hat a$ (Eq. 5.11); counts quanta; Hermitian | $\hat N\vert 5\rangle=5\vert 5\rangle$ |
| $\lvert n\rangle$ (lecture: $\lvert\psi_n\rangle$) | "ket n" or "the state with n quanta" | the common eigenstate of $\hat N$ and $\hat H$, orthonormal | $\langle 2\vert 3\rangle=0$, $\langle 3\vert 3\rangle=1$ |
| $n$ | "n" | the eigenvalue of $\hat N$: a non-negative integer $0,1,2,\dots$ | $n=0$ is the ground state |
| $E_n=\hbar\omega\left(n+\tfrac12\right)$ | "E-n equals h-bar omega times n plus a half" | the allowed energies (Eq. 5.20) | $E_0=\tfrac12\hbar\omega$, $E_1=\tfrac32\hbar\omega$ |
| $\hat H=\hbar\omega\left(\hat N+\tfrac12\right)$ | "H equals h-bar omega times N plus a half" | the Hamiltonian rewritten with the number operator (Eq. 5.16) | acting on $\vert n\rangle$ it just multiplies by $E_n$ |
| $[\hat A,\hat B]$ | "commutator of A and B" | $\hat A\hat B-\hat B\hat A$ ([Move 3.5](../day03.md)); zero means order does not matter | $[\hat x,\hat p]=i\hbar$ |
| $[\hat a,\hat a^\dagger]=1$ | "a, a-dagger commutator equals one" | the key identity (Eq. 5.10); equivalently $\hat a\hat a^\dagger=\hat a^\dagger\hat a+1=\hat N+1$ | see "Skipped steps" |
| $\hat x$ in ladder form | "x-hat in terms of a" | $\hat x=\sqrt{\dfrac{\hbar}{2m\omega}}\left(\hat a^\dagger+\hat a\right)$ (Eq. 5.8) | used for $\langle x\rangle$ and $\langle x^2\rangle$ without integrals |
| $\hat p$ in ladder form | "p-hat in terms of a" | $\hat p=i\sqrt{\dfrac{m\hbar\omega}{2}}\left(\hat a^\dagger-\hat a\right)$ (Eq. 5.9) | note the **minus**, and the $i$ in front |
| $\xi$ | "xi" (ksee) | the dimensionless position $\xi=x\sqrt{m\omega/\hbar}$ ([Move 6.1](../day06.md)) | $\hat a=\dfrac1{\sqrt2}\left(\xi+\dfrac{\mathrm d}{\mathrm d\xi}\right)$ |
| $\sigma_x$, $\Delta x$ | "sigma x", "delta x" | the spread (standard deviation) $\sqrt{\langle x^2\rangle-\langle x\rangle^2}$ | large $\sigma_x$ means a wide packet |
| $\lVert\hat a\vert n\rangle\rVert^2$ | "norm squared of a on n" | the bra-ket $\langle n\vert \hat a^\dagger\hat a\vert n\rangle$; always $\ge0$ | equals $n$, so $n\ge 0$ |
| $\hat a\vert 0\rangle=0$ | "a on the ground state is zero" | the zero vector (not a state); marks the bottom of the ladder | it is not $\vert {-1}\rangle$, no such state exists |
| $H_n(z)$ | "Hermite polynomial of order n" | the polynomial factor of $\psi_n$ (Eq. 5.31) | $H_1(z)\propto z$ |
| $n!$ | "n factorial" | $n(n-1)\cdots 2\cdot1$ | $3!=6$ |

**Three slips in the lecture worth pencilling in (the third is in S1 below).**

- **Eq. (5.5)** prints $-\frac{\hbar^2}{2}\frac{\partial^2\psi}{\partial x^2}+\frac12\omega^2x^2\psi$, which has dropped the mass. The correct position-space form (from Eq. 5.4 with $\hat p=-i\hbar\,\mathrm d/\mathrm dx$) is
$$\hat H\psi=-\frac{\hbar^2}{2m}\frac{\mathrm d^2\psi}{\mathrm dx^2}+\frac12m\omega^2x^2\psi .$$
- **Eq. (5.26)** prints $\left(\sqrt{m\omega/\hbar}\,x+\mathrm d/\mathrm dx\right)\psi_0=0$. Look at the previous line: the coefficient of $\hat p$ is $\dfrac{i}{\sqrt{m\hbar\omega}}\cdot(-i\hbar)=\sqrt{\hbar/m\omega}$, and multiplying through by $\sqrt{m\omega/\hbar}$ turns the first term into $\dfrac{m\omega}{\hbar}x$. So the equation that leads to Eq. (5.27) is $\left(\dfrac{m\omega}{\hbar}x+\dfrac{\mathrm d}{\mathrm dx}\right)\psi_0=0$. Only this version integrates to an exponent $-m\omega x^2/2\hbar$.

## Skipped steps, expanded

### S1. The commutator $[\hat a,\hat a^\dagger]=1$ (lecture Eq. 5.10), line by line

Shorthand, only to keep lines short: $\alpha=\sqrt{m\omega/\hbar}$ and $\beta=1/\sqrt{m\hbar\omega}$. Then
$$\hat a=\tfrac1{\sqrt2}\left(\alpha\hat x+i\beta\hat p\right),\qquad \hat a^\dagger=\tfrac1{\sqrt2}\left(\alpha\hat x-i\beta\hat p\right),\qquad \alpha\beta=\sqrt{\frac{m\omega}{\hbar}}\cdot\frac{1}{\sqrt{m\hbar\omega}}=\frac1{\hbar}.$$
The last fact, $\alpha\beta=1/\hbar$, is the one the lecture uses silently.

1. The two factors of $\tfrac1{\sqrt2}$ multiply to $\tfrac12$:
$$[\hat a,\hat a^\dagger]=\tfrac12\left[\alpha\hat x+i\beta\hat p,\ \alpha\hat x-i\beta\hat p\right].$$
2. The commutator is linear in each slot (it is built from products and differences), so expand into four commutators:
$$=\tfrac12\Big(\alpha^2[\hat x,\hat x]-i\alpha\beta[\hat x,\hat p]+i\beta\alpha[\hat p,\hat x]+\beta^2[\hat p,\hat p]\Big).$$
Signs: $\alpha\hat x$ against $-i\beta\hat p$ gives $-i\alpha\beta[\hat x,\hat p]$; $i\beta\hat p$ against $\alpha\hat x$ gives $+i\alpha\beta[\hat p,\hat x]$; $i\beta\hat p$ against $-i\beta\hat p$ gives $\beta^2[\hat p,\hat p]$ because $i\cdot(-i)=1$.
3. Any operator commutes with itself: $[\hat x,\hat x]=[\hat p,\hat p]=0$. Also $[\hat p,\hat x]=-[\hat x,\hat p]=-i\hbar$.
4. Substitute $[\hat x,\hat p]=i\hbar$ and $\alpha\beta=1/\hbar$:
$$=\tfrac12\left(-i\cdot\tfrac1\hbar\cdot i\hbar+i\cdot\tfrac1\hbar\cdot(-i\hbar)\right)=\tfrac12\left(-i^2+(-i^2)\right)=\tfrac12(1+1)=1 .$$

The lecture's displayed middle line writes the cross terms as $-i[\hat x,\hat p]$ and $+i[\hat p,\hat x]$ without the factor $\alpha\beta=1/\hbar$ in front. If you plug in $i\hbar$ with no $1/\hbar$ you get $\hbar$, not $1$. The middle line simply omits the factor $\alpha\beta=1/\hbar$; the final value $1$ is correct once it is restored. This is the classic "skipped constant" trap.

**Consequences used repeatedly.** $[\hat a^\dagger,\hat a]=-1$, and $\hat a\hat a^\dagger=\hat a^\dagger\hat a+1=\hat N+1$.

### S2. Why $\hat H=\hbar\omega\left(\hat N+\tfrac12\right)$ (Eqs. 5.11 and 5.16)

1. Multiply out $\hat N=\hat a^\dagger\hat a$, keeping the order of $\hat x$ and $\hat p$:
$$\hat N=\tfrac12\left(\alpha\hat x-i\beta\hat p\right)\left(\alpha\hat x+i\beta\hat p\right)=\tfrac12\left(\alpha^2\hat x^2+i\alpha\beta\,\hat x\hat p-i\alpha\beta\,\hat p\hat x+\beta^2\hat p^2\right).$$
2. Group the middle two terms as a commutator: $i\alpha\beta(\hat x\hat p-\hat p\hat x)=\dfrac i\hbar[\hat x,\hat p]=\dfrac i\hbar\cdot i\hbar=-1$.
3. So $\hat N=\tfrac12\left(\alpha^2\hat x^2+\beta^2\hat p^2-1\right)$, i.e. $\hat N+\tfrac12=\tfrac12\left(\alpha^2\hat x^2+\beta^2\hat p^2\right)$.
4. Multiply by $\hbar\omega$ and use $\hbar\omega\alpha^2=m\omega^2$ and $\hbar\omega\beta^2=1/m$:
$$\hbar\omega\left(\hat N+\tfrac12\right)=\tfrac12m\omega^2\hat x^2+\frac{\hat p^2}{2m}=\hat H .$$
The "$+\tfrac12$" is the leftover from the non-commuting $\hat x\hat p$ against $\hat p\hat x$. If $\hat x$ and $\hat p$ commuted there would be no zero-point energy.

### S3. Two more commutators, and why $\hat a$ lowers and $\hat a^\dagger$ raises (Eqs. 5.12 and 5.13 onward)

**Identity used:** $[\hat A\hat B,\hat C]=\hat A[\hat B,\hat C]+[\hat A,\hat C]\hat B$. (Check by expanding both sides; [Move 6.5](../day06.md).)

1. $[\hat N,\hat a]=[\hat a^\dagger\hat a,\hat a]=\hat a^\dagger[\hat a,\hat a]+[\hat a^\dagger,\hat a]\hat a=0+(-1)\hat a=-\hat a$.
2. $[\hat N,\hat a^\dagger]=\hat a^\dagger[\hat a,\hat a^\dagger]+[\hat a^\dagger,\hat a^\dagger]\hat a=\hat a^\dagger\cdot1+0=+\hat a^\dagger$.
3. Suppose $\hat N|n\rangle=n|n\rangle$. Rearrange step 1 as $\hat N\hat a=\hat a\hat N-\hat a$ and apply to $|n\rangle$:
$$\hat N\left(\hat a|n\rangle\right)=\hat a\hat N|n\rangle-\hat a|n\rangle=n\,\hat a|n\rangle-\hat a|n\rangle=(n-1)\,\hat a|n\rangle .$$
So $\hat a|n\rangle$ is again an eigenvector of $\hat N$, with eigenvalue lowered by one.
4. Rearrange step 2 as $\hat N\hat a^\dagger=\hat a^\dagger\hat N+\hat a^\dagger$, and the same argument gives $\hat N\left(\hat a^\dagger|n\rangle\right)=(n+1)\,\hat a^\dagger|n\rangle$. Raised by one.

### S4. The factors $\sqrt n$ and $\sqrt{n+1}$ (Eqs. 5.14 and 5.15)

Steps 3 and 4 only say that $\hat a|n\rangle$ is *proportional* to $|n-1\rangle$. The lecture writes $\hat a|n\rangle=\alpha_-|n-1\rangle$ and fixes $\alpha_-$ by demanding that the norms match.

- **Lowering.** Use $\lVert\hat A|\psi\rangle\rVert^2=\langle\psi|\hat A^\dagger\hat A|\psi\rangle$. Then $\lVert\hat a|n\rangle\rVert^2=\langle n|\hat a^\dagger\hat a|n\rangle=\langle n|\hat N|n\rangle=n\langle n|n\rangle=n$. The right-hand side has norm squared $|\alpha_-|^2\langle n-1|n-1\rangle=|\alpha_-|^2$. Hence $|\alpha_-|^2=n$; take the phase to be $+1$ by convention: $\hat a|n\rangle=\sqrt n\,|n-1\rangle$.
- **Raising.** Now the operator combination is $\hat a\hat a^\dagger$, not $\hat N$: $\lVert\hat a^\dagger|n\rangle\rVert^2=\langle n|\hat a\hat a^\dagger|n\rangle$. Use $\hat a\hat a^\dagger=\hat N+1$ from S1:
$$\langle n|(\hat N+1)|n\rangle=n+1 ,\qquad\text{so}\qquad \hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle .$$

**Sanity check that $[\hat a,\hat a^\dagger]=1$ is respected.** On $|n\rangle$: $\hat a\hat a^\dagger|n\rangle=\sqrt{n+1}\,\hat a|n+1\rangle=\sqrt{n+1}\sqrt{n+1}|n\rangle=(n+1)|n\rangle$, and $\hat a^\dagger\hat a|n\rangle=\sqrt n\,\hat a^\dagger|n-1\rangle=\sqrt n\sqrt n|n\rangle=n|n\rangle$. The difference is $|n\rangle$, i.e. $[\hat a,\hat a^\dagger]=1$. 

### S5. Why $n=0,1,2,\dots$ and nothing else (§5.4)

1. **$n$ is real:** $\hat N$ is Hermitian, so its eigenvalues are real. (Hermitian check: $\hat N^\dagger=(\hat a^\dagger\hat a)^\dagger=\hat a^\dagger(\hat a^\dagger)^\dagger=\hat a^\dagger\hat a$, using $(AB)^\dagger=B^\dagger A^\dagger$, [Move 3.3](../day03.md).)
2. **$n\ge0$:** Eq. (5.22) shows $n=\langle n|\hat N|n\rangle=\lVert\hat a|n\rangle\rVert^2$, and a squared length cannot be negative.
3. **$n$ is an integer:** Lowering repeatedly gives eigenvalues $n,n-1,n-2,\dots$, and each lowering is allowed to continue only while the state is not the zero vector. Suppose $n$ were, say, $2.4$. Then the sequence goes $2.4,\,1.4,\,0.4,\,-0.6,\dots$ and the last value is negative, contradicting step 2. The only way to stop the sequence before it goes negative is to reach a state with $\hat a|\nu\rangle=0$, and $\lVert\hat a|\nu\rangle\rVert^2=\nu$ so this needs $\nu=0$ exactly. The ladder can only end at $0$, so starting values are non-negative integers.
4. **The energies:** from $\hat H|n\rangle=\hbar\omega\left(\hat N+\tfrac12\right)|n\rangle=\hbar\omega\left(n+\tfrac12\right)|n\rangle$ (Eq. 5.20), $E_n=\hbar\omega\left(n+\tfrac12\right)$, and $E_0=\tfrac12\hbar\omega$.

### S6. Building states: $|1\rangle$ from $|0\rangle$, then $|n\rangle$ (Eqs. 5.24 to 5.30)

**Abstract version.** Set $n=0$ in $\hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle$: $\hat a^\dagger|0\rangle=\sqrt1\,|1\rangle=|1\rangle$. Then $\hat a^\dagger|1\rangle=\sqrt2\,|2\rangle$, so $|2\rangle=\dfrac1{\sqrt2}\hat a^\dagger|1\rangle=\dfrac1{\sqrt2}(\hat a^\dagger)^2|0\rangle$. Next, $|3\rangle=\dfrac1{\sqrt3}\hat a^\dagger|2\rangle=\dfrac1{\sqrt{3\cdot2}}(\hat a^\dagger)^3|0\rangle$. Each step divides by one more square root; the product of the roots is $\sqrt{n!}$:
$$|n\rangle=\frac1{\sqrt{n!}}\left(\hat a^\dagger\right)^n|0\rangle .$$

**Wave-function version.** In the variable $\xi=x\sqrt{m\omega/\hbar}$ ([Move 6.1](../day06.md)), $\dfrac{\mathrm d}{\mathrm dx}=\sqrt{\dfrac{m\omega}{\hbar}}\dfrac{\mathrm d}{\mathrm d\xi}$, and the ladder operators become
$$\hat a=\frac1{\sqrt2}\left(\xi+\frac{\mathrm d}{\mathrm d\xi}\right),\qquad \hat a^\dagger=\frac1{\sqrt2}\left(\xi-\frac{\mathrm d}{\mathrm d\xi}\right).$$
(Check the first: $\alpha\hat x=\xi$, and $i\beta\hat p=i\beta(-i\hbar)\,\mathrm d/\mathrm dx=\beta\hbar\,\mathrm d/\mathrm dx=\dfrac1\alpha\cdot\alpha\,\dfrac{\mathrm d}{\mathrm d\xi}=\dfrac{\mathrm d}{\mathrm d\xi}$, since $\beta\hbar=1/\alpha$.)

- The ground state satisfies $\hat a\psi_0=0$, i.e. $\left(\xi+\dfrac{\mathrm d}{\mathrm d\xi}\right)\psi_0=0$, whose solution is a Gaussian of the form $e^{-\xi^2/2}$. This is the lecture's Eq. (5.27) derivation, and it also shows the correct form of Eq. (5.26).
- Raise it. With $f=e^{-\xi^2/2}$ we have $f'=-\xi f$, so
$$\hat a^\dagger f=\frac1{\sqrt2}\left(\xi f+\xi f\right)=\sqrt2\,\xi\,f .$$
This is the lecture's "two equal terms add" step in Eq. (5.30). The polynomial part of $\psi_1$ is therefore $\xi$.
- Raise again, on $g=\xi f$ (whose derivative is $g'=(1-\xi^2)f$):
$$\hat a^\dagger g=\frac1{\sqrt2}\left(\xi\cdot\xi f-(1-\xi^2)f\right)=\frac1{\sqrt2}\,(2\xi^2-1)\,f .$$
So $\psi_2\propto(2\xi^2-1)e^{-\xi^2/2}$: polynomial of degree 2 times the same Gaussian. Each raising raises the degree by one, which is why the lecture says "a polynomial of order $n$ times a Gaussian".

## Moves used this week

- **[Move 3.3](../day03.md)** Adjoint, Hermitian, $(AB)^\dagger=B^\dagger A^\dagger$: used to show $\hat N$ is Hermitian and $\hat a^\dagger=(\hat a)^\dagger$ (see Day 3).
- **[Move 3.5](../day03.md)** Commutator $[A,B]=AB-BA$ (Day 3).
- **[Move 4.4](../day04.md)** Gaussian integrals $\int e^{-ax^2}=\sqrt{\pi/a}$, $\int x^2e^{-ax^2}=\sqrt\pi/(2a^{3/2})$, odd integrands vanish ([Day 4](../day04.md)).
- **[Move 4.5](../day04.md)** Normalisation: find $C$ so that $\int|\psi|^2\,\mathrm dx=1$ (Day 4).
- **[Move 4.6](../day04.md)** Expectation value, variance, standard deviation (Day 4).
- **[Move 6.1](../day06.md)** Substitution $\xi=x\sqrt{m\omega/\hbar}$: rewrite integrals and $\hat H$ in $\xi$ ([Day 6](../day06.md)).
- **[Move 6.2](../day06.md)** Differentiate a Gaussian twice; check $\hat H\psi=E\psi$ by matching terms (Day 6).
- **[Move 6.3](../day06.md)** Gaussian moments $\langle\xi^2\rangle$, $\sigma_x$, $\sigma_p$ and the uncertainty product (Day 6).
- **[Move 6.4](../day06.md)** Ladder operators $\hat a,\hat a^\dagger,\hat N$ (Eqs. 5.6 to 5.11), $[\hat a,\hat a^\dagger]=1$, $\hat H=\hbar\omega(\hat N+\tfrac12)$ (Day 6).
- **[Move 6.5](../day06.md)** Commutator algebra: $[\hat x,\hat p]=i\hbar$ and $[A,BC]=[A,B]C+B[A,C]$ (Day 6).

## Worked clones

These solve problems of the **same type** as the Week 5 task and portfolio, but on **different states**. The task's own state, its normalisation constant, its spreads and its uncertainty product are deliberately left for you. When you have done the clones, do the task on the ground state, cold, in the six-steps format. Use the moves, not the numbers.

### Clone 1. "Show that $\psi$ satisfies $\hat H\psi=E\psi$" (the type of Task Problem 1)

**Problem.** Show that $\psi_1(x)=x\,e^{-m\omega x^2/(2\hbar)}$ (first excited state, unnormalised) satisfies $\hat H\psi_1=E\psi_1$ with $\hat H=-\dfrac{\hbar^2}{2m}\dfrac{\mathrm d^2}{\mathrm dx^2}+\tfrac12m\omega^2x^2$, and find $E$.

**Technique in general (any Gaussian-type trial function $\psi=P(x)\,e^{-bx^2/2}$ with $P$ a polynomial).**

1. Write $\hat H$ in the position representation: second derivative plus $x^2$ term. The operator $\hat H$ contains no time derivative, so work with the spatial function only.
2. Differentiate **twice**. Keep the exponential as a common factor and track only the polynomial in front. Use $\dfrac{\mathrm d}{\mathrm dx}e^{-bx^2/2}=-bx\,e^{-bx^2/2}$.
3. Assemble $-\dfrac{\hbar^2}{2m}\psi''+\tfrac12m\omega^2x^2\psi$ and pull out the exponential.
4. Collect by power of $x$. The highest power (the kinetic term's leading $x^{k+2}$ against the potential's) must cancel. Whatever survives must be a **constant times $P$**. That constant is $E$. If it is not, $\psi$ is not an eigenfunction.

**Solution.** Write $b=m\omega/\hbar$ so the exponent is $-bx^2/2$, and let $f=e^{-bx^2/2}$, with $f'=-bx\,f$.

1. $\psi_1=x f$. First derivative (product rule): $\psi_1'=f+x(-bx f)=(1-bx^2)f$.
2. Second derivative: $\psi_1''=(-2bx)f+(1-bx^2)(-bx f)=(-2bx-bx+b^2x^3)f=(b^2x^3-3bx)f$.
3. Kinetic term: $-\dfrac{\hbar^2}{2m}\psi_1''=-\dfrac{\hbar^2b^2}{2m}x^3f+\dfrac{3\hbar^2b}{2m}x\,f$. Now $\dfrac{\hbar^2b^2}{2m}=\dfrac{\hbar^2}{2m}\dfrac{m^2\omega^2}{\hbar^2}=\dfrac{m\omega^2}2$, and $\dfrac{\hbar^2b}{2m}=\dfrac{\hbar^2}{2m}\dfrac{m\omega}\hbar=\dfrac{\hbar\omega}{2}$. So the kinetic term is $\left(-\dfrac{m\omega^2}{2}x^3+\dfrac{3\hbar\omega}{2}x\right)f$.
4. Potential term: $\tfrac12m\omega^2x^2\cdot xf=\tfrac12m\omega^2x^3f$.
5. Add: the $x^3$ terms cancel exactly ($-\tfrac12m\omega^2+\tfrac12m\omega^2=0$), leaving
$$\hat H\psi_1=\frac{3\hbar\omega}{2}\,x\,f=\frac{3\hbar\omega}{2}\,\psi_1 .$$

**Check.** $E=\tfrac32\hbar\omega=\hbar\omega\left(1+\tfrac12\right)=E_1$, which matches Eq. (5.20) with $n=1$. Units: $\hbar\omega$ is energy. The cancellation of the $x^3$ terms is the hidden condition that fixes the Gaussian's width: with any other $b$ they would not cancel.

### Clone 2. "Expectation values, spreads and the uncertainty product" (the type of Task Problem 2)

Two states, so that you see one Gaussian-type state and one that is not a Gaussian at all.

**Clone 2a. The first excited state $\psi_1$.**

Work in $\xi$ ([Move 6.1](../day06.md)). In $\xi$ the state is $\psi_1=C\,\xi\,e^{-\xi^2/2}$, and momentum is $\hat p=\sqrt{m\hbar\omega}\,\hat\pi$ with $\hat\pi=-i\,\mathrm d/\mathrm d\xi$. Day 6 Exercise 4 found the normalisation and $\langle\xi^2\rangle$ for this state; here it is redone in one place and extended to momentum.

1. **Normalise.** $\int|\psi_1|^2\mathrm d\xi=C^2\int\xi^2e^{-\xi^2}\mathrm d\xi=C^2\dfrac{\sqrt\pi}{2}=1$ (moment formula, $a=1$), so $C^2=\dfrac2{\sqrt\pi}$.
2. **Means vanish.** $|\psi_1|^2$ is even, so $\langle\xi\rangle=\int\psi_1\,\xi\,\psi_1\,\mathrm d\xi$ has an odd integrand: $\langle\xi\rangle=0$. For $\langle\pi\rangle=-i\int\psi_1\psi_1'\,\mathrm d\xi$: $\psi_1\psi_1'$ is (odd)(even)=odd, so $\langle\pi\rangle=0$.
3. **$\langle\xi^2\rangle$.** $C^2\int\xi^4e^{-\xi^2}\mathrm d\xi$. Fourth moment: $\int\xi^4e^{-a\xi^2}\mathrm d\xi=\dfrac{3\sqrt\pi}{4}a^{-5/2}$, which is $\dfrac{3\sqrt\pi}4$ at $a=1$. So $\langle\xi^2\rangle=\dfrac2{\sqrt\pi}\cdot\dfrac{3\sqrt\pi}4=\dfrac32$.
4. **$\langle\pi^2\rangle$.** With $g=\xi e^{-\xi^2/2}$ we have $g''=(\xi^3-3\xi)e^{-\xi^2/2}$ (Day 6 Exercise 2, or Clone 1 with $b=1$). Then
$$\langle\pi^2\rangle=-\int\psi_1\psi_1''\,\mathrm d\xi=-C^2\int\xi(\xi^3-3\xi)e^{-\xi^2}\mathrm d\xi=-C^2\left(\frac{3\sqrt\pi}{4}-3\cdot\frac{\sqrt\pi}{2}\right)=-\frac2{\sqrt\pi}\left(-\frac{3\sqrt\pi}{4}\right)=\frac32 .$$
5. **Spreads.** $\sigma_\xi=\sqrt{3/2}$ and $\sigma_\pi=\sqrt{3/2}$, so $\sigma_x=\sqrt{\dfrac{3\hbar}{2m\omega}}$ and $\sigma_p=\sqrt{\dfrac{3m\hbar\omega}{2}}$.
6. **Product.** $\sigma_x\sigma_p=\hbar\,\sigma_\xi\sigma_\pi=\dfrac{3\hbar}{2}$. It exceeds $\hbar/2$ by a factor of $3$.

**Check.** The uncertainty relation $\sigma_x\sigma_p\ge\hbar/2$ holds. Also the energy: $\langle\hat H\rangle=\dfrac{\hbar\omega}{2}\left(\langle\pi^2\rangle+\langle\xi^2\rangle\right)=\dfrac{\hbar\omega}{2}\cdot3=\tfrac32\hbar\omega=E_1$, as it must, since $\psi_1$ is an eigenstate of $\hat H$ with that eigenvalue. This check is valuable: it ties the two integrals together, so an error in either would show up.

**Clone 2b. A box ground state, for contrast.**

A particle in an infinite well $0\le x\le L$ in its lowest state: $\psi(x)=\sqrt{\dfrac2L}\sin\dfrac{\pi x}{L}$ (already normalised, Day 5). Find $\sigma_x\sigma_p$.

1. **$\langle x\rangle$.** $|\psi|^2$ is symmetric about $x=L/2$, so $\langle x\rangle=L/2$ (this is a probability-weighted average of a distribution symmetric about the middle).
2. **$\langle x^2\rangle$.** Use $\sin^2\theta=\tfrac12(1-\cos2\theta)$ ([Move 1.4](../day01.md)):
$$\langle x^2\rangle=\frac2L\int_0^Lx^2\sin^2\frac{\pi x}L\,\mathrm dx=\frac1L\left[\frac{L^3}3-\int_0^Lx^2\cos\frac{2\pi x}L\,\mathrm dx\right].$$
Integrate by parts twice ([Move 4.3](../day04.md)), writing $k=2\pi/L$. First $\int_0^Lx^2\cos kx\,\mathrm dx=\left[\dfrac{x^2\sin kx}k\right]_0^L-\dfrac2k\int_0^Lx\sin kx\,\mathrm dx$. The bracket is $0$ since $\sin kL=\sin2\pi=0$. Next $\int_0^Lx\sin kx\,\mathrm dx=\left[-\dfrac{x\cos kx}k\right]_0^L+\dfrac1k\int_0^L\cos kx\,\mathrm dx=-\dfrac Lk+0$, since $\cos kL=1$ and $\int_0^L\cos kx\,\mathrm dx=0$. So $\int_0^Lx^2\cos kx\,\mathrm dx=-\dfrac2k\left(-\dfrac Lk\right)=\dfrac{2L}{k^2}=\dfrac{2L\cdot L^2}{4\pi^2}=\dfrac{L^3}{2\pi^2}$. Then
$$\langle x^2\rangle=L^2\left(\frac13-\frac1{2\pi^2}\right).$$
3. **Variance.** $\sigma_x^2=\langle x^2\rangle-\langle x\rangle^2=L^2\left(\dfrac13-\dfrac1{2\pi^2}-\dfrac14\right)=L^2\left(\dfrac1{12}-\dfrac1{2\pi^2}\right)$, so $\sigma_x\approx0.181\,L$.
4. **Momentum.** $\hat p^2=-\hbar^2\,\mathrm d^2/\mathrm dx^2$ and $\psi''=-(\pi/L)^2\psi$, so $\langle p^2\rangle=\dfrac{\hbar^2\pi^2}{L^2}$. Also $\langle p\rangle=-i\hbar\dfrac2L\dfrac\pi L\int_0^L\sin\dfrac{\pi x}{L}\cos\dfrac{\pi x}{L}\,\mathrm dx=0$ (the integral is $\dfrac{L}{2\pi}\left[\sin^2\right]_0^L=0$). So $\sigma_p=\dfrac{\pi\hbar}L$.
5. **Product.** $\sigma_x\sigma_p=\pi\hbar\sqrt{\dfrac1{12}-\dfrac1{2\pi^2}}=\hbar\sqrt{\dfrac{\pi^2}{12}-\dfrac12}\approx0.568\,\hbar$.

**Check and contrast.** $0.568\hbar>0.5\hbar$, consistent with the bound. Look at the moral: how close a state comes to $\sigma_x\sigma_p=\hbar/2$ depends on the *form* of $\psi$, and you can test any candidate state this way. When you work a state of your own, compare its product with $\hbar/2$ yourself.

### Clone 3. Ladder-operator manipulation without integrals (the type of the Portfolio Problems)

**Problem.** Compute $\langle 2|\hat x^2|2\rangle$ and $\langle 2|\hat p^2|2\rangle$, and the product $\sigma_x\sigma_p$ for $|2\rangle$, using only $\hat a$, $\hat a^\dagger$ and Eqs. (5.14) and (5.15).

**Technique.**

1. Replace $\hat x$ by Eq. (5.8): $\hat x=\sqrt{\dfrac{\hbar}{2m\omega}}\left(\hat a^\dagger+\hat a\right)$.
2. **Square it, keeping the order of every factor:**
$$\hat x^2=\frac\hbar{2m\omega}\left(\hat a^\dagger\hat a^\dagger+\hat a^\dagger\hat a+\hat a\hat a^\dagger+\hat a\hat a\right).$$
3. Sandwich between $\langle 2|$ and $|2\rangle$ and apply the **selection rule**: $\hat a^\dagger$ or $\hat a$ moves you one rung, so a term survives only if the net number of rungs moved is zero (otherwise you get $\langle 2|4\rangle=0$ or $\langle 2|0\rangle=0$). So $\hat a^\dagger\hat a^\dagger$ and $\hat a\hat a$ contribute nothing.
4. Evaluate the survivors with Eqs. (5.14) and (5.15): $\hat a^\dagger\hat a|2\rangle=\hat a^\dagger\sqrt2|1\rangle=\sqrt2\sqrt2|2\rangle=2|2\rangle$, and $\hat a\hat a^\dagger|2\rangle=\hat a\sqrt3|3\rangle=\sqrt3\sqrt3|2\rangle=3|2\rangle$.

**Solution.**
$$\langle 2|\hat x^2|2\rangle=\frac{\hbar}{2m\omega}\left(0+2+3+0\right)=\frac{5\hbar}{2m\omega}.$$
For momentum, Eq. (5.9): $\hat p=i\sqrt{\dfrac{m\hbar\omega}2}\left(\hat a^\dagger-\hat a\right)$, so $\hat p^2=-\dfrac{m\hbar\omega}2\left(\hat a^\dagger\hat a^\dagger-\hat a^\dagger\hat a-\hat a\hat a^\dagger+\hat a\hat a\right)$. The prefactor $i^2=-1$ is the source of the extra sign; the cross terms carry a minus each. The diagonal element is
$$\langle 2|\hat p^2|2\rangle=-\frac{m\hbar\omega}2\left(0-2-3+0\right)=\frac{5m\hbar\omega}{2}.$$
Both means vanish: $\hat x$ and $\hat p$ turn $|2\rangle$ into $|1\rangle$ or $|3\rangle$, orthogonal to $\langle2|$. So $\sigma_x^2=\langle x^2\rangle$, $\sigma_p^2=\langle p^2\rangle$, and
$$\sigma_x\sigma_p=\sqrt{\frac{5\hbar}{2m\omega}\cdot\frac{5m\hbar\omega}{2}}=\frac{5}{2}\hbar .$$

**Checks.** (i) Energy: $\langle\hat H\rangle=\dfrac{\langle p^2\rangle}{2m}+\tfrac12m\omega^2\langle x^2\rangle=\dfrac{5\hbar\omega}4+\dfrac{5\hbar\omega}4=\tfrac52\hbar\omega=E_2$. (ii) Equal share: half the energy is kinetic, half potential, the classical virial result. (iii) The uncertainty relation: $\tfrac52\hbar\ge\tfrac12\hbar$, consistent with the bound and well above it, as you expect for an excited rung. Try the same technique on a different rung and see what pattern the numbers follow; Practice Exercise 4 does that.

### Practice exercises (attempt cold, hint second, sketch last)

1. Verify that $\psi=(2\xi^2-1)\,e^{-\xi^2/2}$ satisfies $\hat H\psi=E\psi$ with $\hat H=\dfrac{\hbar\omega}2\left(-\dfrac{\mathrm d^2}{\mathrm d\xi^2}+\xi^2\right)$ and find $E$. — **Hint:** with $f=e^{-\xi^2/2}$ use $f'=-\xi f$; differentiate the product twice, collect powers of $\xi$, and check that the $\xi^4$ terms cancel. — **Solution sketch:** $\psi'=(4\xi-\xi(2\xi^2-1))f=(5\xi-2\xi^3)f$; $\psi''=\left((5-6\xi^2)-\xi(5\xi-2\xi^3)\right)f=(2\xi^4-11\xi^2+5)f$. Then $-\psi''+\xi^2\psi=(-2\xi^4+11\xi^2-5+2\xi^4-\xi^2)f=(10\xi^2-5)f=5\psi$. So $\hat H\psi=\tfrac52\hbar\omega\,\psi$, i.e. $E=\tfrac52\hbar\omega=E_2$.
2. Show that $\psi=\xi\,e^{-\xi^2}$ is **not** an eigenfunction of $\hat H$ in Exercise 1. — **Hint:** the exponent is $-\xi^2$, not $-\xi^2/2$; with $h=e^{-\xi^2}$ we have $h'=-2\xi h$. — **Solution sketch:** $\psi'=(1-2\xi^2)h$, $\psi''=(-4\xi-2\xi(1-2\xi^2))h=(4\xi^3-6\xi)h$. So $-\psi''+\xi^2\psi=(6\xi-4\xi^3+\xi^3)h=(6\xi-3\xi^3)h$. The bracket is not a constant times $\xi$, so it is not an eigenfunction: the width is wrong.
3. For the box ground state of Clone 2b, redo the calculation for the **first excited** box state $\psi=\sqrt{2/L}\,\sin(2\pi x/L)$ and state the uncertainty product. — **Hint:** the same steps, but now $k=4\pi/L$ in the $\cos$ integral and $\psi''=-(2\pi/L)^2\psi$; the boundary terms still vanish because $\sin kL=0$ and $\cos kL=1$. — **Solution sketch:** $\langle x\rangle=L/2$ by symmetry. $\int_0^Lx^2\cos kx\,\mathrm dx=2L/k^2=L^3/(8\pi^2)$, so $\langle x^2\rangle=L^2\left(\tfrac13-\tfrac1{8\pi^2}\right)$ and $\sigma_x^2=L^2\left(\tfrac1{12}-\tfrac1{8\pi^2}\right)$. Also $\langle p\rangle=0$ and $\langle p^2\rangle=4\pi^2\hbar^2/L^2$, so $\sigma_p=2\pi\hbar/L$. Product: $\hbar\sqrt{\pi^2/3-\tfrac12}\approx1.67\,\hbar$.
4. Using the ladder method, compute $\langle 3|\hat x^2|3\rangle$ and $\langle 3|\hat p^2|3\rangle$, then $\sigma_x\sigma_p$ for $|3\rangle$. — **Hint:** first show $\langle3|\hat x|3\rangle=\langle3|\hat p|3\rangle=0$ using orthogonality of $|n\rangle$ states; then follow Clone 3 with $|3\rangle$ in place of $|2\rangle$, so the surviving terms are $\hat a^\dagger\hat a|3\rangle$ and $\hat a\hat a^\dagger|3\rangle$. — **Solution sketch:** $\hat x$ and $\hat p$ each turn $|3\rangle$ into $|2\rangle$ or $|4\rangle$, orthogonal to $\langle3|$, so both means are $0$. Then $\hat a^\dagger\hat a|3\rangle=3|3\rangle$ and $\hat a\hat a^\dagger|3\rangle=4|3\rangle$, so $\langle x^2\rangle=\dfrac{\hbar}{2m\omega}(3+4)=\dfrac{7\hbar}{2m\omega}$ and $\langle p^2\rangle=\dfrac{m\hbar\omega}2(3+4)=\dfrac{7m\hbar\omega}2$. Then $\sigma_x\sigma_p=\sqrt{\tfrac{7}{2}\cdot\tfrac72}\,\hbar=\tfrac72\hbar$. Energy check: $\tfrac{7\hbar\omega}4+\tfrac{7\hbar\omega}4=\tfrac72\hbar\omega=E_3$.
5. A state is $|\psi\rangle=\dfrac1{\sqrt2}\left(|2\rangle+|3\rangle\right)$. Find $\langle\psi|\hat x|\psi\rangle$ using Eq. (5.8). — **Hint:** expand into four bra-kets; $\langle m|\hat a|n\rangle=\sqrt n\,\delta_{m,n-1}$ and $\langle m|\hat a^\dagger|n\rangle=\sqrt{n+1}\,\delta_{m,n+1}$, so only the two "cross" terms survive. — **Solution sketch:** $\langle\hat x\rangle=\dfrac12\sqrt{\dfrac\hbar{2m\omega}}\left[\langle2|\hat a|3\rangle+\langle3|\hat a^\dagger|2\rangle\right]=\dfrac12\sqrt{\dfrac\hbar{2m\omega}}\left(\sqrt3+\sqrt3\right)=\sqrt{\dfrac{3\hbar}{2m\omega}}$. The diagonal terms $\langle2|\hat x|2\rangle$ and $\langle3|\hat x|3\rangle$ are zero.
6. Compute $\hat a^\dagger\hat a^\dagger|1\rangle$, then apply $\hat N$ to it, and give the energy of the resulting state. — **Hint:** apply Eq. (5.15) twice, carrying the square-root factors along. — **Solution sketch:** $\hat a^\dagger|1\rangle=\sqrt2|2\rangle$; $\hat a^\dagger\sqrt2|2\rangle=\sqrt2\sqrt3|3\rangle=\sqrt6\,|3\rangle$. $\hat N$ gives $3\sqrt6|3\rangle$, so the eigenvalue is $3$, and the energy is $E_3=\tfrac72\hbar\omega$. Two quanta were added to $E_1=\tfrac32\hbar\omega$: $\tfrac32+2=\tfrac72$.

## Retrieval questions

Quiz-style, closed book. Each states the misconception it is built to catch.

1. Is $\hat a$ a Hermitian operator? What is its adjoint, and can you measure "$\hat a$" in the lab? — **Hint:** compare Eqs. (5.6) and (5.7) and recall what Hermitian means. — **Solution sketch:** No. $\hat a^\dagger$ is its adjoint and $\hat a\ne\hat a^\dagger$, so $\hat a$ is not Hermitian and is not an observable. It is a tool for moving between states. *Trap:* believing every named operator is a measurable quantity.
2. What is $\hat a|0\rangle$? — **Hint:** put $n=0$ into $\hat a|n\rangle=\sqrt n\,|n-1\rangle$. — **Solution sketch:** It is the zero vector, $0$. There is no state "$|{-1}\rangle$". *Trap:* writing $\hat a|0\rangle=|{-1}\rangle$ or $|0\rangle$, or thinking the result is a normalised state with zero energy.
3. Why can the oscillator not have energy $0$? — **Hint:** use $E_n=\hbar\omega\left(n+\tfrac12\right)$ and the smallest allowed $n$. — **Solution sketch:** The smallest $n$ is $0$, giving $E_0=\tfrac12\hbar\omega>0$. The "$+\tfrac12$" came from $[\hat x,\hat p]=i\hbar$ (S2): position and momentum cannot both be sharp, so the particle is never at rest. *Trap:* carrying over the classical picture where "at rest at the bottom" has zero energy.
4. Is $\hat a\hat a^\dagger=\hat a^\dagger\hat a$? What is $\hat a\hat a^\dagger$ in terms of $\hat N$? — **Hint:** use $[\hat a,\hat a^\dagger]=1$. — **Solution sketch:** No. $\hat a\hat a^\dagger=\hat a^\dagger\hat a+1=\hat N+1$. On $|n\rangle$ it gives $n+1$, whereas $\hat a^\dagger\hat a$ gives $n$. *Trap:* treating operators like numbers and dropping the order.
5. You apply $\hat a^\dagger$ to $|3\rangle$ and then measure the energy. What do you get and with what probability? — **Hint:** use Eq. (5.15) to write the new state, and note its normalisation. — **Solution sketch:** $\hat a^\dagger|3\rangle=2|4\rangle$, an eigenstate of $\hat H$ with $E_4=\tfrac92\hbar\omega$, so the measured energy is $\tfrac92\hbar\omega$ with probability $1$ (after normalising, the state is $|4\rangle$). *Trap:* thinking the factor $2$ changes the probability or that $\hat a^\dagger$ itself is a measurement.
6. In $\hat a|n\rangle=\sqrt n\,|n-1\rangle$, why is there a $\sqrt n$? — **Hint:** ask what condition makes $|n-1\rangle$ a unit-length state and compute the length of $\hat a|n\rangle$. — **Solution sketch:** $\hat a|n\rangle$ has length-squared $\langle n|\hat a^\dagger\hat a|n\rangle=n$, so a state of length $\sqrt n$ pointing along $|n-1\rangle$ must be $\sqrt n\,|n-1\rangle$. *Trap:* thinking the $\sqrt n$ is arbitrary or that $\hat a$ preserves normalisation.
7. In $\hat p=i\sqrt{m\hbar\omega/2}\left(\hat a^\dagger-\hat a\right)$, why is the relative sign a minus, and what would go wrong with a plus? — **Hint:** solve Eqs. (5.6) and (5.7) for $\hat p$ by subtracting them. — **Solution sketch:** $\hat a^\dagger-\hat a=\dfrac{1}{\sqrt2}\left(-2i\beta\hat p\right)$, so $\hat p\propto\hat a^\dagger-\hat a$, with an $i$ in front. A plus would give $\hat x$, not $\hat p$. Also, $\hat p$ must be Hermitian, and $i(\hat a^\dagger-\hat a)$ is Hermitian while $\hat a^\dagger+\hat a$ times $i$ would not be. *Trap:* copying $\hat p$ with a plus sign, or dropping the $i$.
8. Energy steps: the lecture says the oscillator's energy "changes in steps of $\hbar\omega$". Is the energy $E_n=n\hbar\omega$? — **Hint:** compare $E_1-E_0$ with $E_0$. — **Solution sketch:** No. $E_n=\hbar\omega\left(n+\tfrac12\right)$. The step is $\hbar\omega$, but the whole ladder is offset by the zero-point $\tfrac12\hbar\omega$. *Trap:* writing $E_n=n\hbar\omega$ and forgetting the half.

## Six-steps write-up template

The university's own six-steps page is not in the local exports; this uses the stand-in in [STRATEGY](../../STRATEGY.md) applied to this week's problem types. Fill each line in your own words. Braces `{...}` stand for what you supply.

**Type A: "show that $\psi$ satisfies $\hat H\psi=E\psi$"**

1. **Restate.** Show that $\psi={\text{the given function}}$ solves $\hat H\psi=E\psi$ with $\hat H={\text{the given operator}}$. Givens: $m$, $\omega$, and the stated $E$ if there is one.
2. **Write the state.** $\psi$ as a polynomial times a Gaussian; note whether the function depends on $t$, and say which parts you are treating.
3. **Name the move.** [Move 6.2](../day06.md): differentiate twice, substitute, match terms. Optionally [Move 6.1](../day06.md) to simplify constants.
4. **Algebra.** $\psi'$, then $\psi''$, then $-\frac{\hbar^2}{2m}\psi''+\frac12m\omega^2x^2\psi$; factor out the Gaussian; show the highest powers cancel; identify the constant multiplying $\psi$.
5. **Check.** Units of $E$; agreement with $E_n=\hbar\omega(n+\tfrac12)$ for the right $n$; the leading terms cancelled (not just "assumed").
6. **Answer.** One sentence: "$\psi$ is an eigenfunction of $\hat H$ with eigenvalue $E=\dots$".

**Type B: "normalise, then find $\langle x^2\rangle$, $\sigma_x$, $\sigma_p$ and compare with $\hbar/2$"**

1. **Restate.** Find the constant, the two spreads and the product; compare with $\sigma_x\sigma_p\ge\hbar/2$.
2. **Write the state.** $|\psi|^2$ and whether it is even (so $\langle x\rangle=0$) or not.
3. **Name the moves.** 6.1 (substitute $\xi$), 4.4 (Gaussian integrals), 4.5 (normalise), 4.6 (expectation and variance), 6.3 (momentum in $\xi$ units).
4. **Algebra.** In order: normalisation; $\langle x\rangle$; $\langle x^2\rangle$; $\sigma_x$; $\langle p\rangle$; $\langle p^2\rangle$; $\sigma_p$; product. Keep the Jacobian $\mathrm dx=\sqrt{\hbar/m\omega}\,\mathrm d\xi$ in every integral and convert back at the end.
5. **Check.** Units of $\sigma_x$ (length), $\sigma_p$ (momentum), product (action, like $\hbar$); a state's energy from $\langle p^2\rangle/2m+\tfrac12m\omega^2\langle x^2\rangle$ if it is an eigenstate; the product respects the bound.
6. **Answer.** State each value with units, and say in words whether the bound is met, exceeded or saturated.

**Type C: "use $\hat a$ and $\hat a^\dagger$ to find an expectation value"**

1. **Restate.** Find $\langle\psi|\hat O|\psi\rangle$ for a stated state $|\psi\rangle$ (a single $|n\rangle$ or a superposition).
2. **Write the state.** Expand as $\sum c_n|n\rangle$ and write $\hat O$ using Eq. (5.8) or (5.9).
3. **Name the move.** [Move 6.4](../day06.md) and the selection rule: $\hat a^\dagger$ or $\hat a$ moves one rung, so only matching rungs survive.
4. **Algebra.** Expand into bra-kets $\langle m|\hat a|n\rangle=\sqrt n\,\delta_{m,n-1}$ and $\langle m|\hat a^\dagger|n\rangle=\sqrt{n+1}\,\delta_{m,n+1}$; keep the $c_n^*c_m$ coefficients and the operator prefactor.
5. **Check.** Prefactor units; for a real superposition of neighbouring rungs, whether the sign of the answer makes sense; a limit such as a single $|n\rangle$ giving zero for $\hat x$ and $\hat p$.
6. **Answer.** A full sentence with the value and its units.

## Confusion log

| Where (lecture § / eq.) | Symbol or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
