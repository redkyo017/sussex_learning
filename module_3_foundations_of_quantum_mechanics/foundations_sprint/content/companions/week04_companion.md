# Week 4 Companion — The Schrödinger Equation

Built on [Day 3](../day03.md) (operators, adjoints, eigenproblems) and [Day 5](../day05.md) (measurement, the Schrödinger equation, the box). Read [STRATEGY](../../STRATEGY.md) for the five-pass protocol; this companion is the Pass 1 and Pass 2 aid for `week_4/week_4_lecture.md`.

**Conventions.** Notation follows the Week 4 lecture: wave function $\Psi(x,t)$, spatial part $\psi(x)$, angular frequencies $\omega_n=E_n/\hbar$, coefficients $\alpha_n$ (Eqs. 4.4–4.6). Where the lecture writes a state as a wave function I sometimes write the same state as a ket; the ket form $|\varphi_n\rangle$ for energy eigenstates and $\hat H|\varphi_n\rangle=E_n|\varphi_n\rangle$ is the same eigenvalue equation as Eq. 4.3. The definition of the adjoint is from the Week 2 lecture (Eqs. 2.14–2.15), which the Week 4 lecture itself does not restate; I say so where I lean on it.

## What this week is really saying

Weeks 2 and 3 told you how to describe a state at one instant and what a measurement does to it. Week 4 adds the last rule: **how a state changes when nobody is looking.** That rule is the Schrödinger equation,
$$i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi,\qquad \hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\quad(\text{Eq. 4.1}).$$
Say it aloud: "the rate of change of the state, times $i\hbar$, equals the energy operator acting on the state."

The whole week is one idea, seen three times:

1. **Energy eigenstates are the special states that only pick up a phase.** If $\hat H\psi=E\psi$, then $\Psi=e^{-iEt/\hbar}\psi$ solves the equation. Nothing about its probabilities moves. These are the *stationary states*.
2. **Everything else is a superposition of them.** Expand the starting state in energy eigenstates, give each term its own phase, add. Because different energies rotate at different speeds, the *relative* phases change, and that is the only source of motion.
3. **Measuring energy is Week 3 again.** The coefficients $|\alpha_n|^2$ are the probabilities of the energies $E_n$; the eigenvalue $E_n$ is the value. Time evolution never changes $|\alpha_n|^2$.

Picture: each energy component is a clock hand of fixed length $|\alpha_n|$ spinning at its own rate $\omega_n$. The lengths never change; the *angles between the hands* do. A single hand (a stationary state) looks frozen when you only look at its length. Two or more hands with different speeds make the combined pattern in $x$ slosh back and forth.

The two examples of the week are the two ends of the same story. The **free particle** ($V=0$) has energy eigenfunctions $e^{ikx}$ that are not normalisable, so real free particles are wave packets (integrals over $k$ instead of sums over $n$). The **infinite well** has boundary conditions that force $k$ to be $n\pi/L$, so energies are discrete and the sum is genuinely a sum.

## Notation decoder

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\hat H$ | "H hat", the Hamiltonian | The energy operator: kinetic plus potential. Its eigenvalues are the possible energies. | $-\frac{\hbar^2}{2m}\partial_x^2+V(x)$ |
| $i\hbar\,\partial/\partial t$ | "i h-bar partial t" | "Rate of change in time", scaled so that it has units of energy. | On $e^{-i\omega t}$ it returns $\hbar\omega\,e^{-i\omega t}$ |
| $\Psi(x,t)$ | "capital psi of x and t" | The full, time-dependent wave function. | $e^{-i\omega t}\psi(x)$ |
| $\psi(x)$ | "small psi of x" | The spatial part only; the solution of $\hat H\psi=E\psi$. | $\sqrt{2/L}\sin(n\pi x/L)$ |
| $\partial^2/\partial x^2$ | "second partial x" | Differentiate twice in $x$, holding $t$ fixed. Measures curvature. | On $e^{ikx}$ gives $-k^2e^{ikx}$ |
| $E_n$ | "E sub n" | The $n$th allowed energy (an eigenvalue of $\hat H$). The list $\{E_n\}$ is the spectrum. | $E_n=n^2\pi^2\hbar^2/(2mL^2)$ in the well |
| $\omega_n$ | "omega n" | Angular frequency tied to the energy: $\omega_n=E_n/\hbar$. | $E=\hbar\omega$ is Eq. 4.3's definition of $E$ |
| $\lvert\varphi_n\rangle$ | "ket phi n" | The $n$th energy eigenstate as a ket, $\hat H\lvert\varphi_n\rangle=E_n\lvert\varphi_n\rangle$. | Orthonormal: $\langle\varphi_m\lvert\varphi_n\rangle=\delta_{mn}$ |
| $\alpha_n$ | "alpha n" | Amplitude of the $n$th stationary state in the expansion (Eq. 4.4). $\alpha_n=\langle\varphi_n\lvert\psi\rangle$ in ket language. | $\lvert\alpha_n\rvert^2$ is the probability of $E_n$ |
| $e^{-iE_nt/\hbar}$ | "e to the minus i E t over h-bar" | A pure phase: modulus 1, rotates at rate $\omega_n$. The time factor in a stationary state. | $\lvert e^{-i\theta}\rvert=1$ ([Move 1.3](../day01.md)) |
| $\hat A^\dagger$ | "A dagger" | The adjoint: defined by $\langle\psi\lvert\hat A\phi\rangle=\langle\hat A^\dagger\psi\lvert\phi\rangle$. For matrices, conjugate transpose. | $A=A^\dagger$ means Hermitian |
| $\langle\hat H\rangle$ | "expectation of H" | Average energy over many identical preparations: $\sum_n\lvert\alpha_n\rvert^2E_n$. | Need not be an eigenvalue |
| $e^{ikx}$ | "plane wave, wave number k" | Free-particle energy eigenfunction with momentum $p=\hbar k$ (Eq. 4.12). Not normalisable. | $E=\hbar^2k^2/2m$ |
| $\phi(k)$ | "phi of k" | Amplitude of the plane wave $e^{ikx}$ in a wave packet (Eq. 4.17); Fourier transform of $\Psi(x,0)$. | Plays the role of $\alpha_n$ for a continuous index |
| $L$ | "L" | Width of the infinite well: walls at $x=0$ and $x=L$. | $V=0$ inside, $\infty$ outside |
| $\lambda_{\mathrm{dB}}$ | "de Broglie wavelength" | $2\pi/\lvert k\rvert$; wavelength attached to momentum $p$ by $\lvert p\rvert=2\pi\hbar/\lambda_{\mathrm{dB}}$. | Larger $p$, shorter wavelength |
| $\Delta x\,\Delta p\ge\hbar/2$ | "delta x delta p at least h-bar over two" | Spreads in position and momentum cannot both be small. | Sharp $p$ means $\Delta x\to\infty$ |

## Skipped steps, expanded

### A. Separation of variables (lecture Eqs. 4.2–4.3)

The lecture *guesses* a product form and shows it works. Every step, slowly.

**Why a guess is allowed.** The Schrödinger equation is linear, so if you find some solutions, sums of them are solutions too. Products of a function of $x$ and a function of $t$ are the easiest solutions to find. The lecture then promises (and Eq. 4.4–4.5 deliver) that sums of these products are enough to match any starting state. So the guess loses nothing.

**Assumption you should notice.** $V$ depends on $x$ only. If $V$ also depended on $t$, the cancellation below would fail.

**The derivation.** Put $\Psi(x,t)=e^{-i\omega t}\psi(x)$ into $i\hbar\,\partial_t\Psi=-\frac{\hbar^2}{2m}\partial_x^2\Psi+V\Psi$.

1. Left side. $\partial_t$ only sees the factor with $t$. $\partial_t e^{-i\omega t}=-i\omega\,e^{-i\omega t}$. So the left side is $i\hbar(-i\omega)\,e^{-i\omega t}\psi=\hbar\omega\,e^{-i\omega t}\psi$, because $i\cdot(-i)=-i^2=1$.
2. Right side, first term. $\partial_x$ only sees $\psi(x)$; $e^{-i\omega t}$ is a constant for it and just comes out: $-\frac{\hbar^2}{2m}e^{-i\omega t}\psi''$.
3. Right side, second term. $V(x)e^{-i\omega t}\psi$; the exponential is already a common factor.
4. Every term now carries the same factor $e^{-i\omega t}$, which is never zero, so divide it out. Time has vanished:
$$\hbar\omega\,\psi=-\frac{\hbar^2}{2m}\psi''+V\psi=\hat H\psi.$$
5. Rename $E=\hbar\omega$: $\hat H\psi=E\psi$ (Eq. 4.3). This is an eigenvalue equation ([Move 3.2](../day03.md)). Acceptable solutions exist only for special $E_n$: those are the energies.

**Why "all solutions are sums of stationary states" is safe.** For each allowed $E_n$ you get $\psi_n$ and its own $\omega_n=E_n/\hbar$. The general time-dependent solution attaches each phase to its own term (Eq. 4.5): $\Psi=\sum\alpha_n\psi_ne^{-i\omega_nt}$. At $t=0$ every phase is 1 and you recover Eq. 4.4, so $\alpha_n$ are fixed by the starting state. The equation is first order in time, so the starting state determines everything after.

### B. Why a stationary state has constant $|\Psi|^2$

$\Psi_n=\psi_n(x)e^{-i\omega_nt}$. The conjugate is $\Psi_n^*=\psi_n^*(x)e^{+i\omega_nt}$ (conjugating $e^{-i\theta}$ flips the sign of the exponent). So
$$|\Psi_n|^2=\Psi_n^*\Psi_n=\psi_n^*\psi_n\;e^{i\omega_nt}e^{-i\omega_nt}=|\psi_n|^2\cdot e^{0}=|\psi_n|^2 .$$
The two exponentials cancel exactly because $|e^{-i\theta}|=1$ ([Move 1.3](../day01.md): a phase is a point on the unit circle). Same for any expectation value $\int\Psi^*\hat A\Psi\,\mathrm{d}x$ when $\hat A$ does not involve time: the phase from the bra and the phase from the ket cancel.

**Now two different energies.** With $\Psi=\Psi_1+\Psi_2$ the cross terms carry $e^{i\omega_1t}e^{-i\omega_2t}=e^{-i(\omega_2-\omega_1)t}$ and its conjugate. They do *not* cancel; together they give $2\cos[(\omega_2-\omega_1)t]$ (Euler, [Move 1.3](../day01.md)). That is the whole lecture line "the probability density oscillates at angular frequency $\omega_2-\omega_1$". If $\omega_1=\omega_2$ the difference is zero and nothing moves: motion needs *different* energies.

**Do not conflate two probabilities.** The probability that an energy measurement gives $E_n$ is $|\alpha_n|^2$: constant. The probability *density in position* $|\Psi(x,t)|^2$ can move. Both statements are true at once, because the second depends on relative phases and the first does not.

### C. The infinite well, with every algebra step (lecture 4.3)

1. Outside the well $V=\infty$; finite energy forces $\psi=0$ there. Inside, $\psi''=-k^2\psi$ with $k^2=2mE/\hbar^2$. Continuity of $\psi$ then demands $\psi(0)=\psi(L)=0$.
2. General solution $\alpha_+e^{ikx}+\alpha_-e^{-ikx}$. At $x=0$: $\alpha_++\alpha_-=0$, so $\alpha_-=-\alpha_+$.
3. Then $\psi=\alpha_+(e^{ikx}-e^{-ikx})=2i\alpha_+\sin kx$, since $e^{i\theta}-e^{-i\theta}=2i\sin\theta$. The factor $2i\alpha_+$ is just an overall constant, to be fixed by normalisation.
4. At $x=L$: $\sin kL=0$, so $kL=n\pi$; $n=1,2,3,\dots$ ($n=0$ is $\psi\equiv0$; negative $n$ repeats a positive one up to sign).
5. Normalise: $\int_0^LC^2\sin^2(n\pi x/L)\,\mathrm{d}x=C^2L/2$ (half-angle identity, [Move 1.4](../day01.md): the cosine part integrates to zero over whole half-waves). So $C=\sqrt{2/L}$.
6. Energies: $E_n=\hbar^2k^2/2m=n^2\pi^2\hbar^2/(2mL^2)$ (Eq. 4.20). The boundary conditions, not the differential equation, cause the quantisation.

### D. Free-particle numbers (lecture 4.2)

- Plug $e^{ikx}$ into Eq. 4.9: $\psi''=-k^2\psi$, so $-\frac{\hbar^2}{2m}(-k^2)\psi=\frac{\hbar^2k^2}{2m}\psi$: $E=\hbar^2k^2/2m$.
- Wave speed: $\omega/k=E/(\hbar k)=\hbar k/2m$. Particle speed $p/m=\hbar k/m$. Ratio 2 to 1: the single plane wave is not the particle. A packet's group speed equals $p/m$, which is why packets are the physical objects.
- Not normalisable: $|e^{ikx}|^2=1$, and $\int_{-\infty}^{\infty}1\,\mathrm{d}x$ diverges. Sharp momentum means completely unknown position (Eq. 4.15 with $\Delta p=0$).

### E. The adjoint rules, and why the order reverses

**Convention I rely on.** The Week 4 lecture does not define the adjoint. I use the Week 2 definition (Eq. 2.14, in integral form Eq. 2.15, here in one dimension):
$$\int\psi^*\,(\hat A\phi)\,\mathrm{d}x=\int(\hat A^\dagger\psi)^*\,\phi\,\mathrm{d}x .$$
To find $\hat A^\dagger$, move every derivative off $\phi$ onto $\psi^*$ by integration by parts ([Move 4.3](../day04.md)), then read off what acts on $\psi$. I assume the wave functions are normalisable, so they vanish at $\pm\infty$ and the boundary terms are zero.

**Why $(AB)^\dagger=B^\dagger A^\dagger$: the intuition.** The adjoint undoes each factor from the outside in, so the order reverses. Everyday version: socks then shoes, undone as shoes then socks. The reason is the definition (2.14) applied twice; writing that argument out is your job in the Week 4 adjoint task, so I do not do it for you. The Pauli check below shows the rule at work.

**Three or more factors.** Treat $ABC$ as $(AB)C$: $((AB)C)^\dagger=C^\dagger(AB)^\dagger=C^\dagger B^\dagger A^\dagger$. Every factor is adjointed and the whole order reverses. Consistency check with the Pauli matrices (Day 3), which are Hermitian: $\sigma_x\sigma_y\sigma_z=(i\sigma_z)\sigma_z=i\,\mathbb 1$, so $(\sigma_x\sigma_y\sigma_z)^\dagger=-i\,\mathbb 1$. The rule gives $\sigma_z\sigma_y\sigma_x=\sigma_z(-i\sigma_z)=-i\,\mathbb 1$. Same answer. Had you forgotten to reverse, $\sigma_x\sigma_y\sigma_z=+i\,\mathbb 1$ would have been wrong by a sign.

## Moves used this week

- [Move 1.3](../day01.md), Euler and global phase: [Day 1](../day01.md). Every $|e^{-i\theta}|=1$ step.
- [Move 1.4](../day01.md), half-angle identity: [Day 1](../day01.md). Normalising $\sin^2$ in the well.
- [Move 2.4](../day02.md), expansion in an orthonormal basis: [Day 2](../day02.md).
- [Move 3.2](../day03.md), eigenvalue equation: [Day 3](../day03.md). $\hat H\psi=E\psi$ is one.
- [Move 3.3](../day03.md), adjoint, Hermitian, $(AB)^\dagger=B^\dagger A^\dagger$: [Day 3](../day03.md).
- [Move 3.5](../day03.md), commutator (do two observables share eigenvectors?): [Day 3](../day03.md).
- [Move 4.3](../day04.md), integration by parts with vanishing boundary terms: [Day 4](../day04.md).
- [Move 4.5](../day04.md), normalisation and [Move 4.8](../day04.md), $e^{ikx}$ as a momentum eigenfunction: [Day 4](../day04.md).
- Moves 5.1 to 5.5, expansion probabilities, expectation, collapse, Schrödinger equation and stationary states, the box: [Day 5](../day05.md).

## Worked clones

Same *type* as the Week 4 task and portfolio problems, on different objects. Attempt each yourself first, ten minutes, then compare.

### Clone 1 — Expansion, energy probabilities, and a two-observable measurement chain

**Problem.** A system is in the state
$$|\psi_0\rangle=\frac{1}{\sqrt6}\Big[|\varphi_1\rangle+i\sqrt2\,|\varphi_2\rangle+\sqrt3\,|\varphi_3\rangle\Big],$$
where $|\varphi_n\rangle$ ($n=1,2,3$) are orthonormal energy eigenstates, $\hat H|\varphi_n\rangle=n^2E_0|\varphi_n\rangle$ (so $E_0,4E_0,9E_0$). An observable $\hat B$ has the same eigenstates with $\hat B|\varphi_1\rangle=2b_0|\varphi_1\rangle$, $\hat B|\varphi_2\rangle=-5b_0|\varphi_2\rangle$, $\hat B|\varphi_3\rangle=7b_0|\varphi_3\rangle$, where $b_0$ is a unit.

(a) What energies can be found, with what probabilities, and what is $\langle\hat H\rangle$?
(b) What values of $B$ can be found, with what probabilities, and what is $\langle\hat B\rangle$?
(c) An energy measurement gives $4E_0$. A $B$ measurement follows immediately. What do you get?
(d) Starting again from $|\psi_0\rangle$, a $B$ measurement gives $7b_0$; then $E$ is measured. What do you get? What is the probability of the whole chain "$E=4E_0$ first, then $B=-5b_0$"?

**Six steps.**

1. *Restate.* Find outcome sets and probabilities for $H$ and $B$ in $|\psi_0\rangle$; then follow collapse through two successive measurements. Givens: the state, the eigenvalue tables.
2. *Write the state.* Coefficient vector in the basis $(\varphi_1,\varphi_2,\varphi_3)$: $c=\frac{1}{\sqrt6}(1,\ i\sqrt2,\ \sqrt3)$. Check first that it is normalised.
3. *Name the moves.* Expansion and Born rule (5.1), expectation (5.2), collapse (5.3).
4. *Algebra.*
 - Normalisation: $|c_1|^2+|c_2|^2+|c_3|^2=\frac{1+2+3}{6}=1$. Note $|i\sqrt2|^2=2$: the $i$ drops out of the modulus.
 - (a) $P(E_0)=\frac16$, $P(4E_0)=\frac26=\frac13$, $P(9E_0)=\frac36=\frac12$. $\langle\hat H\rangle=\frac16E_0+\frac13(4E_0)+\frac12(9E_0)=\frac{1+8+27}{6}E_0=6E_0$.
 - (b) The *same* eigenstates, so the *same* probabilities, with the *new* eigenvalues attached: $P(2b_0)=\frac16$, $P(-5b_0)=\frac13$, $P(7b_0)=\frac12$. $\langle\hat B\rangle=\frac{2}{6}b_0-\frac{5}{3}b_0+\frac72b_0=\frac{2-10+21}{6}b_0=\frac{13}{6}b_0$.
 - (c) Outcome $4E_0$ collapses the state to $|\varphi_2\rangle$ (the factor $i\sqrt2/\sqrt6$ is thrown away on renormalising). $|\varphi_2\rangle$ is a $\hat B$ eigenvector, so $B=-5b_0$ with probability 1.
 - (d) $B=7b_0$ collapses to $|\varphi_3\rangle$, which is an energy eigenstate with $9E_0$: the energy is $9E_0$ with certainty. Chain probability: $P(E=4E_0)\times P(B=-5b_0\mid\text{collapsed})=\frac13\times1=\frac13$.
5. *Check.* Probabilities lie in $[0,1]$ and sum to 1 in both (a) and (b). $\langle\hat H\rangle=6E_0$ lies between $E_0$ and $9E_0$; $\langle\hat B\rangle=\frac{13}{6}b_0\approx2.17b_0$ lies between $-5b_0$ and $7b_0$. Neither average is an eigenvalue, which is fine.
6. *Answer.* Energies $E_0,4E_0,9E_0$ with probabilities $\frac16,\frac13,\frac12$ and $\langle\hat H\rangle=6E_0$; $B$ values $2b_0,-5b_0,7b_0$ with the same probabilities and $\langle\hat B\rangle=\frac{13}{6}b_0$; after $E=4E_0$ the value of $B$ is $-5b_0$ for certain.

**Traps the clone is built to show.**
- The eigenvalues of $\hat B$ are *not* a tidy pattern in $n$ (not equally spaced, not even monotonic), so you must attach each value to its own state. Never extrapolate a formula.
- Probabilities come from coefficients; values come from eigenvalues (Day 5 slogan).
- The chain works so neatly in (c) and (d) *only because $\hat H$ and $\hat B$ share eigenvectors* ($[\hat H,\hat B]|\varphi_n\rangle=(E_nb_n-b_nE_n)|\varphi_n\rangle=0$). If $\hat B$ had different eigenvectors, the collapsed state $|\varphi_2\rangle$ would have to be re-expanded in the $\hat B$ eigenbasis (a fresh [Move 5.1](../day05.md) problem), and the result would be a spread of values, not one.

### Clone 2 — Adjoints of operators, on new objects

**Problem.** Find the adjoint of each: (i) multiplication by $f(x)=(2+i)\,x^2$; (ii) $\hat D=x\,\dfrac{\mathrm d}{\mathrm dx}$; (iii) $\dfrac{\mathrm d^3}{\mathrm dx^3}$; and use the product rule to find $(\sigma_y\sigma_z\sigma_x)^\dagger$.

**Method (all three operator cases).** Write $\int\psi^*(\hat A\phi)\,\mathrm dx$, integrate by parts until no derivative touches $\phi$, drop boundary terms, and match the form $\int(\hat A^\dagger\psi)^*\phi\,\mathrm dx$. I use the Week 2 definition (Eq. 2.15); wave functions vanish at $\pm\infty$.

**(i) Multiplication by $f$.**
$\int\psi^*f\phi\,\mathrm dx=\int(f^*\psi)^*\phi\,\mathrm dx$, because $(f^*\psi)^*=f\psi^*$. So the adjoint multiplies by $f^*$. Here $f^*=(2-i)\,x^2$.
Check: it is Hermitian exactly when $f$ is real; this $f$ has an imaginary part $x^2$, so it is not.

**(ii) $\hat D=x\,\mathrm d/\mathrm dx$.**
$\int\psi^*x\phi'\,\mathrm dx=\big[\psi^*x\phi\big]_{-\infty}^{\infty}-\int(x\psi^*)'\phi\,\mathrm dx$. The boundary term vanishes. Product rule: $(x\psi^*)'=\psi^*+x\psi^{*\prime}$. So the integral is $\int\big[-(\psi+x\psi')\big]^*\phi\,\mathrm dx$ (all coefficients real, so conjugating the bracket changes nothing but the $\psi$'s). Reading off:
$$\hat D^\dagger\psi=-\psi-x\psi'\quad\Longrightarrow\quad\hat D^\dagger=-1-x\frac{\mathrm d}{\mathrm dx}=-\frac{\mathrm d}{\mathrm dx}\circ x .$$
Check: the derivative hitting $x$ produces the extra $-1$; that is the source of the constant that a careless guess ("just flip the sign") would miss. Bonus consistency check: $\hat D+\tfrac12$ then satisfies $(\hat D+\tfrac12)^\dagger=-1-x\partial_x+\tfrac12=-(\hat D+\tfrac12)$.

**(iii) $\mathrm d^3/\mathrm dx^3$.**
Three integrations by parts, each dropping a boundary term and each producing a minus sign:
$$\int\psi^*\phi'''=-\int\psi^{*\prime}\phi''=+\int\psi^{*\prime\prime}\phi'=-\int\psi^{*\prime\prime\prime}\phi=\int\big(-\psi'''\big)^*\phi .$$
So $(\mathrm d^3/\mathrm dx^3)^\dagger=-\,\mathrm d^3/\mathrm dx^3$.

**(iv) $(\sigma_y\sigma_z\sigma_x)^\dagger$ by the product rule.** $(\sigma_y\sigma_z\sigma_x)^\dagger=\sigma_x^\dagger\sigma_z^\dagger\sigma_y^\dagger=\sigma_x\sigma_z\sigma_y$ (Hermitian, order reversed). Direct check: $\sigma_y\sigma_z=i\sigma_x$, so $\sigma_y\sigma_z\sigma_x=i\sigma_x^2=i\,\mathbb 1$, adjoint $-i\,\mathbb 1$. Reversed product: $\sigma_z\sigma_y=-i\sigma_x$, so $\sigma_x\sigma_z\sigma_y=\sigma_x(-i\sigma_x)=-i\,\mathbb 1$. They agree.

**Six-steps summary.** (1) restate the operator and the definition used, (2) write $\int\psi^*\hat A\phi$, (3) name the move (integration by parts, [Move 4.3](../day04.md)), (4) algebra with each boundary term explicitly dropped and *why* (normalisable means zero at infinity), (5) check by an independent route (a sign count, a special case, the matrix version), (6) state $\hat A^\dagger$ in a sentence.

### Clone 3 — Time evolution of a two-state superposition

**Problem.** A system starts in $|\Psi(0)\rangle=\frac{1}{13}\big(5|\varphi_1\rangle-12i\,|\varphi_2\rangle\big)$, where $\hat H|\varphi_n\rangle=E_n|\varphi_n\rangle$ with $E_1=\hbar\Omega$ and $E_2=4\hbar\Omega$. (a) Write $|\Psi(t)\rangle$. (b) Show the probability of each energy is constant. (c) Find $\langle\hat H\rangle$. (d) For $|\chi\rangle=\frac{1}{\sqrt2}(|\varphi_1\rangle+|\varphi_2\rangle)$, which is *not* an energy eigenstate, show that $P_\chi(t)=|\langle\chi|\Psi(t)\rangle|^2$ does depend on time.

**Six steps.**

1. *Restate.* Attach time dependence to a known expansion; show which probabilities move and which do not.
2. *Write the state.* Coefficients $\alpha_1=5/13$, $\alpha_2=-12i/13$. Check: $|\alpha_1|^2+|\alpha_2|^2=\frac{25+144}{169}=1$.
3. *Name the moves.* Stationary-state phases (5.4), Born rule (5.1), Euler for the cross term (1.3).
4. *Algebra.*
 - (a) $\omega_1=\Omega$, $\omega_2=4\Omega$ (from $\omega_n=E_n/\hbar$). Each term gets its own phase (Eq. 4.5):
 $$|\Psi(t)\rangle=\tfrac{5}{13}e^{-i\Omega t}|\varphi_1\rangle-\tfrac{12i}{13}e^{-4i\Omega t}|\varphi_2\rangle .$$
 - (b) Moduli of the amplitudes: $\big|\tfrac{5}{13}e^{-i\Omega t}\big|^2=\tfrac{25}{169}$ and $\big|\tfrac{12i}{13}e^{-4i\Omega t}\big|^2=\tfrac{144}{169}$, for every $t$, since $|e^{-i\theta}|=1$ and $|i|=1$.
 - (c) $\langle\hat H\rangle=\frac{25}{169}\hbar\Omega+\frac{144}{169}(4\hbar\Omega)=\frac{601}{169}\hbar\Omega\approx3.56\,\hbar\Omega$, constant.
 - (d) $\langle\chi|\Psi(t)\rangle=\frac{1}{\sqrt2}(a+b)$ with $a=\frac5{13}e^{-i\Omega t}$, $b=-\frac{12i}{13}e^{-4i\Omega t}$. Then $|a+b|^2=|a|^2+|b|^2+2\,\mathrm{Re}(a^*b)$, and $a^*b=-\frac{60i}{169}e^{-3i\Omega t}$. Since $i\,e^{-3i\theta}=i\cos3\theta+\sin3\theta$, its real part is $\sin3\theta$, so $2\,\mathrm{Re}(a^*b)=-\frac{120}{169}\sin3\Omega t$. Hence
 $$P_\chi(t)=\tfrac12\Big[1-\tfrac{120}{169}\sin(3\Omega t)\Big].$$
5. *Check.* At $t=0$: $P_\chi=\tfrac12$, and directly $\langle\chi|\Psi(0)\rangle=\frac{5-12i}{13\sqrt2}$ has modulus squared $\frac{169}{169\cdot2}=\tfrac12$. The oscillation angular frequency is $3\Omega=(E_2-E_1)/\hbar$, as the lecture says. $P_\chi$ stays between $\frac12(1\pm\frac{120}{169})$, inside $[0,1]$.
6. *Answer.* The energy probabilities stay $\frac{25}{169}$ and $\frac{144}{169}$ forever; $\langle\hat H\rangle=\frac{601}{169}\hbar\Omega$; but the probability of finding the system in $|\chi\rangle$ oscillates at angular frequency $3\Omega$. Energy probabilities are frozen; anything sensitive to *relative* phase is not.

## Retrieval questions

Closed book, one attempt each, on paper. Each item names the misconception it traps.

1. A system is in a single energy eigenstate, $\Psi=\psi_n(x)e^{-iE_nt/\hbar}$. Does the wave function change in time? Does $|\Psi|^2$? Does any measurable probability? *(Trap: "stationary" means nothing at all happens.)* — **Hint:** compare $\Psi$ with $\Psi^*\Psi$; recall $|e^{-i\theta}|=1$. — **Solution sketch:** $\Psi$ itself changes: it is multiplied by a rotating phase. But $|\Psi|^2=|\psi_n|^2$ and every probability and expectation value is time-independent, because the phases from the bra and the ket cancel. Stationary refers to observable quantities, not to the raw function.
2. $\Psi(x,0)=\frac{1}{\sqrt2}\big(\psi_1(x)+i\psi_2(x)\big)$ with orthonormal energy eigenfunctions, $E_1\ne E_2$. What is the probability of measuring $E_2$ at time $t=100$ in any units? *(Trap: the phase $e^{-iE_2t/\hbar}$ must change the probability; or the factor $i$ changes it.)* — **Hint:** the amplitude of $\psi_2$ at time $t$ is $\alpha_2e^{-iE_2t/\hbar}$; take its modulus squared. — **Solution sketch:** $\alpha_2=i/\sqrt2$, and $|\alpha_2e^{-iE_2t/\hbar}|^2=|\alpha_2|^2=\frac12$ at every $t$, including $t=100$. Phases (including the $i$) never change a probability; only relative phases between components change *interference* patterns.
3. In an infinite well, $\Psi(x,0)=\frac{1}{\sqrt5}\big(\psi_1(x)+2\psi_3(x)\big)$ with normalised $\psi_n$. Give the possible energies in units of $E_1$ (with $E_n=n^2E_1$), their probabilities, and $\langle E\rangle$. Can a single measurement return $\langle E\rangle$? *(Trap: probabilities equal the coefficients unsquared; energies proportional to $n$ instead of $n^2$; average must be an outcome.)* — **Hint:** $|\alpha_1|^2=\frac15$, $|\alpha_3|^2=\frac45$; energies are $E_1$ and $9E_1$. — **Solution sketch:** $E_1$ with $\frac15$, $9E_1$ with $\frac45$ (sum 1). $\langle E\rangle=\frac15E_1+\frac45\cdot9E_1=\frac{37}{5}E_1=7.4E_1$. No single measurement returns $7.4E_1$; it is an average over many identical preparations.
4. Matrix $M=\begin{pmatrix}1&i\\2&3i\end{pmatrix}$. Find $M^\dagger$ and say whether $M$ is Hermitian. *(Trap: transposing without conjugating.)* — **Hint:** swap rows and columns, then conjugate every entry. Hermitian means $M^\dagger=M$; check the diagonal is real first. — **Solution sketch:** $M^\dagger=\begin{pmatrix}1&2\\-i&-3i\end{pmatrix}$. Not Hermitian: the entry $3i$ on the diagonal is not real, and $\overline{M_{12}}=-i\neq M_{21}=2$.
5. Compute $(\sigma_x\sigma_z\sigma_y)^\dagger$ using the product rule, then check by multiplying out. (Use $\sigma_x\sigma_z=-i\sigma_y$ and $\sigma_y^2=\mathbb 1$.) *(Trap: forgetting to reverse the order, or forgetting that the factors are Hermitian so the daggers vanish.)* — **Hint:** $(ABC)^\dagger=C^\dagger B^\dagger A^\dagger$; then reverse-order product $\sigma_y\sigma_z\sigma_x$, using $\sigma_y\sigma_z=i\sigma_x$. — **Solution sketch:** By the rule, $(\sigma_x\sigma_z\sigma_y)^\dagger=\sigma_y\sigma_z\sigma_x=(i\sigma_x)\sigma_x=i\,\mathbb 1$. Direct: $\sigma_x\sigma_z\sigma_y=(-i\sigma_y)\sigma_y=-i\,\mathbb 1$, whose conjugate transpose is $+i\,\mathbb 1$. They agree.
6. A free particle has $\psi(x)=e^{3ix/a}$. Find its momentum, its energy, and say whether it is an acceptable physical state. *(Trap: a plane wave is a real, single particle; forgetting to square $k$.)* — **Hint:** read off $k=3/a$; use $p=\hbar k$ and $E=\hbar^2k^2/2m$; test $\int|\psi|^2\mathrm dx$. — **Solution sketch:** $p=3\hbar/a$, $E=\frac{\hbar^2}{2m}\cdot\frac{9}{a^2}=\frac{9\hbar^2}{2ma^2}$. Not physical: $|\psi|^2=1$ everywhere, so the integral over the line diverges. Real free particles are wave packets, integrals of plane waves over $k$ (Eq. 4.17).
7. For a plane wave with wave number $k$, by what factor does the wave speed differ from the classical speed of a particle with momentum $\hbar k$? *(Trap: assuming the phase speed of a plane wave is the particle's speed.)* — **Hint:** wave speed is $\omega/k$ with $\omega=E/\hbar$; classical speed is $p/m$. — **Solution sketch:** $\omega/k=\hbar k/2m$ and $p/m=\hbar k/m$, so the wave moves at half the classical speed. The resolution is that a wave packet moves at the group speed $p/m$, not at the speed of its individual plane waves.
8. In the separation of variables step you divide both sides by $e^{-i\omega t}$. Why is that allowed, and does it mean the state has no time dependence? *(Trap: the time-independent equation describes a static state, or dividing by something that might vanish.)* — **Hint:** what is $|e^{-i\omega t}|$? And what does the time-independent equation actually describe? — **Solution sketch:** $|e^{-i\omega t}|=1$, so it is never zero and division is safe. The equation $\hat H\psi=E\psi$ only fixes the *spatial* factor and $E$; the full $\Psi=e^{-iEt/\hbar}\psi$ does still evolve, but only by a phase that no probability can see.

## Task 2 (discussion board): misconceptions

The task asks you to identify common misconceptions and discuss why they occur. Below is a *framework*, not a post. The board is peer discussion, so write your own in your own words, from your own understanding, with your own examples. Do not paste this table.

**How to structure a good post.** Choose two or three misconceptions. For each: (1) state it as the wrong claim a beginner would make; (2) explain *why it arises* (which classical habit or which piece of language misleads); (3) state the correct picture in one or two sentences using the module's terms; (4) give a *test* that separates the two pictures. Then reply to peers by testing their example the same way.

| Misconception to consider | Question to ask yourself |
|---|---|
| $\Psi$ is a physical wave in space | What kind of values does $\Psi$ take? |
| A stationary state means the particle is at rest | What does "stationary" refer to: the state, or a measurable quantity? |
| Superposition means "in one state, we just do not know which" | Could ignorance produce interference? |
| Collapse is caused by a conscious observer | What does the postulate itself say, and what does it leave out? |
| The uncertainty principle says measurement disturbs the system | Does the inequality refer to the state or to a measuring process? |
| Everything in quantum mechanics is quantised | Which systems have discrete energies, and what makes them so? |
| Energy quantisation is put in by hand | Where do the allowed values come from in the well? |
| The Schrödinger equation is a classical wave equation | How does its form differ from a classical wave equation? |
| Interference means the electron split into pieces | What is actually detected, and where does the pattern live? |

**Before posting, ask yourself for each item:** Can I say it in two sentences without notation? Can I name the equation that contradicts the wrong version? Would a sceptical peer accept my test? Cite anything you took from outside the module.

## Assessment 1 tips (method only)

These are about how to present *any* problem set of this kind. They contain no course solutions; the model answers are the university's.

1. **Read the command word.** "Find", "verify", "show that" and "what values and with what probabilities" each demand something different. "Show that" means a chain of justified steps to a stated target; the target is not part of your proof.
2. **Six-steps every problem**, even short ones (STRATEGY stand-in). Marks follow method, so write step 3 (which principle, in words) even when it feels obvious.
3. **State the definition you are using**, with its source (for example "adjoint defined by lecture Eq. 2.14"). Then use it, do not just quote the result.
4. **Probability problems.** Always (a) check normalisation of the state before anything else; (b) list *values* and *probabilities* separately, and never mix them; (c) confirm the probabilities sum to 1; (d) for any second measurement, say what the state is *after* the first, and in which basis the second measurement is expanded.
5. **Different observables.** Before chaining two measurements, ask whether they share eigenvectors. If yes, the collapsed state is already an eigenstate of the second. If not, expand again.
6. **Show every integration by parts.** Say that the boundary term vanishes and why. A missing justification is the classic lost mark.
7. **Signs and conjugates.** In every inner product conjugate the bra side. Write the conjugate explicitly on the line where you take it.
8. **Check step, always.** Units, normalisation, a limit, a sign. If the answer contains a probability outside $[0,1]$, you have found the error before the marker did.
9. **Answer in a sentence** that restates the question in your own words.
10. **Presentation.** Legible working in order, one problem per page, and check the submission requirements on the assessment page. Do not leave the file to the last hour.
11. **Independence.** Use the discussion board for method, not for handing over answers, and write up the final solutions yourself.

## Six-steps write-up template

Applied to this week's three problem types. Copy, then fill in.

**Type A: expansion and measurement.**
1. Restate: state, eigenvalue table, what is asked (values? probabilities? expectation? a chain?).
2. Write the state as a coefficient list in the eigenbasis; check $\sum|c_n|^2=1$.
3. Move: Born rule (5.1), expectation (5.2), collapse (5.3).
4. Algebra: $|c_n|^2$ line by line; attach eigenvalues; for chains, write the post-measurement state explicitly.
5. Check: sum to 1; $\langle A\rangle$ within the range of eigenvalues; repeat measurement certain.
6. Answer in a sentence.

**Type B: adjoints.**
1. Restate the operator and quote the definition (Eq. 2.14/2.15).
2. Write $\int\psi^*\,\hat A\phi\,\mathrm dx$.
3. Move: integration by parts (4.3), drop boundary terms (normalisable), product rule (3.3).
4. Algebra with every boundary term shown and dropped.
5. Check by an independent route: sign count, matrix version, special case.
6. State $\hat A^\dagger$; say whether $\hat A$ is Hermitian.

**Type C: time evolution.**
1. Restate the initial state and the spectrum.
2. Expansion coefficients $\alpha_n$; check normalisation.
3. Move: attach $e^{-iE_nt/\hbar}$ (5.4); Born rule (5.1).
4. Algebra: $\Psi(t)$; then $|\alpha_ne^{-iE_nt/\hbar}|^2$; then any interference term via Euler.
5. Check: $t=0$ recovers the initial state; frequencies equal $(E_m-E_n)/\hbar$.
6. Answer: say which probabilities are constant and which move.
