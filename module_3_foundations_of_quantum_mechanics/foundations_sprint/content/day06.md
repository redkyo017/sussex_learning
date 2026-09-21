# Day 6 — The oscillator toolkit

> **Physics pair for today:** [P4 — Magnetism and Spin](physics/P4.md) (~1 h 40).

**Time box (~3.5 h):** 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Why this matters

Week 5 studies the quantum harmonic oscillator: a particle in the bowl-shaped potential $V(x)=\tfrac12 m\omega^2x^2$. The lecture solves it with **ladder operators** (Eqs. 5.6–5.16), and the Week 5 task then asks you to work with Gaussian wave functions and to compute spreads and an uncertainty product. Both halves are just tools you already own (Gaussian integrals, derivatives, commutators) plus one new trick: **rescale $x$ so that all the constants disappear**.

Today you learn five moves (6.1 to 6.5). You will practise them on *other* functions and *other* states than the ones in the Week 5 task, so that when you meet the task you are doing a technique you know, not copying an answer. The task itself is the university's to mark: attempt it cold after today, in the six-steps format.

## Warm-up (retrieval, 5 questions from Day 5, closed book, 20 min)

Answers are folded at the bottom of the file. Write yours down first.

1. A state is $|\psi\rangle=\tfrac{1}{\sqrt3}|1\rangle+\sqrt{\tfrac23}\,|2\rangle$, where $|1\rangle,|2\rangle$ are orthonormal eigenstates of an observable $\hat A$ with eigenvalues $4$ and $9$. What are the probabilities of measuring $4$ and $9$, and what is $\langle\hat A\rangle$?
2. You measure $\hat A$ and get $9$. What is the state immediately afterwards, and what is the probability that an immediate second measurement gives $9$ again?
3. Write the time-dependent Schrödinger equation. If $\Psi(x,t)=\varphi(x)\,e^{-iEt/\hbar}$, does $|\Psi|^2$ depend on $t$? Why?
4. Solve $\psi''=-k^2\psi$ on $0\le x\le L$ with $\psi(0)=\psi(L)=0$. What values may $k$ take?
5. In the box of Question 4, write the energy $E_n$ in terms of $k_n$, $\hbar$ and $m$, then in terms of $L$.

## Moves

### Move 6.1 — Substitution $\xi = x\sqrt{m\omega/\hbar}$: rewrite integrals and $\hat H$ in $\xi$ (15 min)

**The point.** The oscillator has three constants: $\hbar$, $m$, $\omega$. Every formula drags them around, and algebra with many symbols is where mistakes breed. The fix is to measure position in a natural ruler, so that all three constants fold into one number and then vanish.

**The substitution.** Define the **dimensionless variable**

$$\xi = x\sqrt{\frac{m\omega}{\hbar}}\qquad\Longleftrightarrow\qquad x=\sqrt{\frac{\hbar}{m\omega}}\,\xi .$$

Say it as "xi equals x times root of m omega over h-bar". The number $\sqrt{\hbar/m\omega}$ is a length, the oscillator's natural length scale, so $\xi$ is "how many natural lengths from the centre".

Three rewriting rules follow:

- **Powers of $x$:** $x^2=\dfrac{\hbar}{m\omega}\,\xi^2$.
- **The Jacobian:** $\mathrm{d}x=\sqrt{\dfrac{\hbar}{m\omega}}\,\mathrm{d}\xi$. Never forget it. The limits do not change, because the scale factor is positive and $\pm\infty$ stay $\pm\infty$.
- **Derivatives:** $\dfrac{\mathrm{d}}{\mathrm{d}x}=\sqrt{\dfrac{m\omega}{\hbar}}\,\dfrac{\mathrm{d}}{\mathrm{d}\xi}$, so $\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}=\dfrac{m\omega}{\hbar}\dfrac{\mathrm{d}^2}{\mathrm{d}\xi^2}$.

**The Hamiltonian in $\xi$.** Start from Eq. (5.4), $\hat H=\dfrac{\hat p^2}{2m}+\tfrac12 m\omega^2\hat x^2$ with $\hat p=-i\hbar\,\mathrm{d}/\mathrm{d}x$.

- Kinetic term: $-\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}=-\dfrac{\hbar^2}{2m}\cdot\dfrac{m\omega}{\hbar}\dfrac{\mathrm{d}^2}{\mathrm{d}\xi^2}=-\dfrac{\hbar\omega}{2}\dfrac{\mathrm{d}^2}{\mathrm{d}\xi^2}$.
- Potential term: $\tfrac12 m\omega^2\cdot\dfrac{\hbar}{m\omega}\xi^2=\dfrac{\hbar\omega}{2}\xi^2$.

So

$$\hat H=\frac{\hbar\omega}{2}\left(-\frac{\mathrm{d}^2}{\mathrm{d}\xi^2}+\xi^2\right).$$

Only one overall constant, $\hbar\omega/2$, survives, and it is the unit of energy. Inside the bracket there is no $\hbar$, no $m$, no $\omega$.

**Worked example (a different integral).** Evaluate $I=\displaystyle\int_{-\infty}^{\infty}x^2\,e^{-2m\omega x^2/\hbar}\,\mathrm{d}x$.

1. Exponent: $\dfrac{2m\omega}{\hbar}x^2=2\xi^2$. Also $x^2=\dfrac{\hbar}{m\omega}\xi^2$ and $\mathrm{d}x=\sqrt{\dfrac{\hbar}{m\omega}}\mathrm{d}\xi$.
2. So $I=\left(\dfrac{\hbar}{m\omega}\right)^{3/2}\displaystyle\int_{-\infty}^{\infty}\xi^2e^{-2\xi^2}\,\mathrm{d}\xi$. The power $3/2$ is $1$ from $x^2$ plus $\tfrac12$ from the Jacobian.
3. Gaussian moment (Move 4.4) with $a=2$: $\displaystyle\int\xi^2e^{-a\xi^2}\mathrm{d}\xi=\frac{\sqrt\pi}{2a^{3/2}}=\frac{\sqrt\pi}{4\sqrt2}$.
4. $I=\left(\dfrac{\hbar}{m\omega}\right)^{3/2}\dfrac{\sqrt\pi}{4\sqrt2}$.

Check the units: $x^2\,\mathrm{d}x$ is length cubed, and $(\hbar/m\omega)^{3/2}$ is length cubed. Always run this check.

### Move 6.2 — Differentiate a Gaussian twice; check $\hat H\psi=E\psi$ by matching terms (15 min)

**Two derivative facts.** For $f=e^{-\xi^2/2}$ the chain rule gives $f'=-\xi f$. For a product, use the product rule: $(\xi f)'=f+\xi f'$. Keep the exponential as a common factor and only track the polynomial in front.

**The matching-terms method.** To test whether $\psi$ is an eigenfunction of $\hat H$:

1. Compute $\psi''$ (twice, carefully).
2. Build $\hat H\psi=\dfrac{\hbar\omega}{2}\left(-\psi''+\xi^2\psi\right)$.
3. Factor out the common exponential.
4. The result is an eigenvalue equation only if what is left is a **constant times the original polynomial**. Match power by power: the $\xi^2$ terms must cancel, and what remains must be a constant multiple of $\psi$. That constant is $E$.

**Worked example (a wrong-width Gaussian, so it fails).** Let $f=e^{-\xi^2}$.

- $f'=-2\xi f$, and $f''=-2f-2\xi f'=(4\xi^2-2)f$.
- $\hat Hf=\dfrac{\hbar\omega}{2}\left(-(4\xi^2-2)+\xi^2\right)f=\dfrac{\hbar\omega}{2}(2-3\xi^2)f$.
- The bracket $(2-3\xi^2)$ is not a constant, so $f$ is **not** an eigenfunction of $\hat H$. The $\xi^2$ terms ($-4\xi^2$ from the kinetic term against $+\xi^2$ from the potential) fail to cancel. The width of the Gaussian is fixed by this cancellation.

### Move 6.3 — Gaussian moments: $\langle\xi^2\rangle$, $\sigma_x$, $\sigma_p$, uncertainty product (15 min)

**Recipe (Moves 4.4 to 4.6, now in $\xi$).**

1. Normalise in $\xi$: find the constant so that $\int|\psi|^2\mathrm{d}\xi=1$. (Work in $\xi$ throughout, and convert back at the end.)
2. $\langle\xi\rangle=\int\psi^*\,\xi\,\psi\,\mathrm{d}\xi$. If $|\psi|^2$ is even, the integrand is odd, so $\langle\xi\rangle=0$.
3. $\langle\xi^2\rangle=\int\psi^*\xi^2\psi\,\mathrm{d}\xi$.
4. **Standard deviation** (the "spread"): $\sigma_\xi=\sqrt{\langle\xi^2\rangle-\langle\xi\rangle^2}$. Convert: $\sigma_x=\sqrt{\hbar/m\omega}\;\sigma_\xi$.
5. **Momentum in $\xi$ units.** Since $\hat p=-i\hbar\sqrt{m\omega/\hbar}\;\mathrm{d}/\mathrm{d}\xi=\sqrt{m\hbar\omega}\,\hat\pi$ with $\hat\pi=-i\,\mathrm{d}/\mathrm{d}\xi$, we get $\sigma_p=\sqrt{m\hbar\omega}\;\sigma_\pi$. Here $\langle\pi^2\rangle=\int\psi^*\left(-\psi''\right)\mathrm{d}\xi$ (second derivative with respect to $\xi$).
6. **Uncertainty product:** $\sigma_x\sigma_p=\sqrt{\dfrac{\hbar}{m\omega}}\sqrt{m\hbar\omega}\;\sigma_\xi\sigma_\pi=\hbar\,\sigma_\xi\sigma_\pi$. Compare with the **uncertainty relation** $\sigma_x\sigma_p\ge\hbar/2$, that is, $\sigma_\xi\sigma_\pi\ge\tfrac12$.

**Worked example (a deliberately different Gaussian).** Take $\psi=C\,e^{-\xi^2/4}$ (not an oscillator eigenstate; it is only a practice function).

1. $|\psi|^2=C^2e^{-\xi^2/2}$, and $\int e^{-\xi^2/2}\mathrm{d}\xi=\sqrt{2\pi}$ (the formula with $a=\tfrac12$), so $C^2=1/\sqrt{2\pi}$.
2. $\langle\xi\rangle=0$ (odd integrand). $\langle\xi^2\rangle=C^2\dfrac{\sqrt\pi}{2(1/2)^{3/2}}=C^2\sqrt{2\pi}=1$. So $\sigma_\xi=1$.
3. $\psi'=-\tfrac{\xi}{2}\psi$ and $\psi''=\left(\tfrac{\xi^2}{4}-\tfrac12\right)\psi$. So $\langle\pi^2\rangle=\int\psi^*(-\psi'')\mathrm{d}\xi=\tfrac12-\tfrac14\langle\xi^2\rangle=\tfrac14$. Also $\langle\pi\rangle=-i\int\psi\,\psi'\,\mathrm{d}\xi=0$ (odd integrand). So $\sigma_\pi=\tfrac12$.
4. Form $\sigma_\xi\sigma_\pi$ from steps 2 and 3, and remember $\sigma_x\sigma_p=\hbar\,\sigma_\xi\sigma_\pi$. Compare $\sigma_\xi\sigma_\pi$ with $\tfrac12$ yourself.

### Move 6.4 — Ladder operators, number operator, $\hat H=\hbar\omega(\hat N+\tfrac12)$ (Week 5 Eqs. 5.6 to 5.16) (10 min)

Use the lecture's convention exactly. Lowering (annihilation) operator, Eq. (5.6):

$$\hat a=\frac1{\sqrt2}\left(\sqrt{\frac{m\omega}{\hbar}}\,\hat x+i\,\frac{1}{\sqrt{m\hbar\omega}}\,\hat p\right).$$

Raising (creation) operator, its **adjoint**, Eq. (5.7):

$$\hat a^\dagger=\frac1{\sqrt2}\left(\sqrt{\frac{m\omega}{\hbar}}\,\hat x-i\,\frac{1}{\sqrt{m\hbar\omega}}\,\hat p\right).$$

The two are each other's adjoint but not equal, so **neither is Hermitian** and neither is an observable. Inverting (Eqs. 5.8, 5.9):

$$\hat x=\sqrt{\frac{\hbar}{2m\omega}}\left(\hat a^\dagger+\hat a\right),\qquad \hat p=i\sqrt{\frac{m\hbar\omega}{2}}\left(\hat a^\dagger-\hat a\right).$$

Here $\hat x$ and $\hat p$ *are* Hermitian: the sum $\hat a^\dagger+\hat a$ is its own adjoint.

**Key results** (each proved in the lecture; know how):

- $[\hat a,\hat a^\dagger]=1$ (Eq. 5.10), using only $[\hat x,\hat p]=i\hbar$.
- **Number operator** $\hat N=\hat a^\dagger\hat a$ (Eq. 5.11). It is Hermitian: $\hat N^\dagger=\hat a^\dagger(\hat a^\dagger)^\dagger=\hat N$.
- $[\hat N,\hat a]=-\hat a$ and $[\hat N,\hat a^\dagger]=\hat a^\dagger$ (Eqs. 5.12, 5.13).
- $\hat H=\hbar\omega\left(\hat N+\tfrac12\right)=\hbar\omega\left(\hat a^\dagger\hat a+\tfrac12\right)$ (Eq. 5.16).
- On number eigenstates, written $|n\rangle$ for the lecture's $|\psi_n\rangle$ with $\hat N|n\rangle=n|n\rangle$: $\hat a|n\rangle=\sqrt n\,|n-1\rangle$ and $\hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle$ (Eqs. 5.14, 5.15).
- Energies: $E_n=\hbar\omega\left(n+\tfrac12\right)$ with $n=0,1,2,\dots$ The lowest is $E_0=\tfrac12\hbar\omega$, the **zero-point energy**: the particle can never be fully at rest.
- Ground state: $\hat a|0\rangle=0$, and $|n\rangle=\dfrac{1}{\sqrt{n!}}(\hat a^\dagger)^n|0\rangle$ (Eq. 5.24).

**Worked example (a different task from the Week 5 problems).** Compute $\hat p|4\rangle$ and $\langle5|\hat p|4\rangle$.

1. $\hat p|4\rangle=i\sqrt{\dfrac{m\hbar\omega}{2}}\left(\hat a^\dagger|4\rangle-\hat a|4\rangle\right)=i\sqrt{\dfrac{m\hbar\omega}{2}}\left(\sqrt5\,|5\rangle-2\,|3\rangle\right)$.
2. Take the inner product with $\langle5|$: orthonormality gives $\langle5|5\rangle=1$ and $\langle5|3\rangle=0$, so $\langle5|\hat p|4\rangle=i\sqrt5\sqrt{\dfrac{m\hbar\omega}{2}}=i\sqrt{\dfrac{5m\hbar\omega}{2}}$. The same step with $\langle4|$ gives $\langle4|\hat p|4\rangle=0$.

Notice what happened: an operator built from $\hat a,\hat a^\dagger$ only moves you between neighbouring rungs, and the inner product picks out the rung you asked for.

### Move 6.5 — Commutator algebra (10 min)

**Derive $[\hat x,\hat p]=i\hbar$.** A commutator is an operator, so to see what it *is*, let it act on an arbitrary **test function** $f(x)$. With $\hat p=\dfrac\hbar i\dfrac{\mathrm{d}}{\mathrm{d}x}$:

- $\hat x\hat p f=x\cdot\dfrac\hbar i f'$.
- $\hat p\hat x f=\dfrac\hbar i\dfrac{\mathrm{d}}{\mathrm{d}x}(xf)=\dfrac\hbar i\left(f+xf'\right)$ (product rule).
- Subtract: $[\hat x,\hat p]f=\dfrac\hbar i\,x f'-\dfrac\hbar i\,f-\dfrac\hbar i\,xf'=-\dfrac\hbar i\,f=i\hbar\,f$, since $-1/i=i$.

The $xf'$ terms cancel and one term survives. Since $f$ was arbitrary, $[\hat x,\hat p]=i\hbar$ as an operator identity.

**Product rules for commutators.** For any operators $A,B,C$:

$$[A,BC]=[A,B]\,C+B\,[A,C],\qquad [AB,C]=A\,[B,C]+[A,C]\,B .$$

Proof of the first: expand the right side: $ABC-BAC+BAC-BCA=ABC-BCA=[A,BC]$. The middle terms cancel. (The second is the identity the lecture uses for Eq. 5.12.)

**Worked example.** $[\hat x,\hat p^2]=[\hat x,\hat p]\hat p+\hat p[\hat x,\hat p]=i\hbar\hat p+i\hbar\hat p=2i\hbar\,\hat p$. The rule is "the commutator with a square is twice the single one, times the leftover operator", like differentiating $p^2$.

**Also useful:** $[A,A]=0$, $[A,B]=-[B,A]$, and $[A,B+C]=[A,B]+[A,C]$.

## Core concepts

- **Harmonic oscillator:** any system whose potential is quadratic in position, $V=\tfrac12 m\omega^2x^2$ (Week 5, §5.1). It matters because near the bottom of almost any potential well the curve looks like a parabola.
- **Dimensionless variable $\xi$:** position measured in units of the natural length $\sqrt{\hbar/m\omega}$, so constants disappear from the algebra.
- **Ladder operators $\hat a,\hat a^\dagger$:** built from $\hat x,\hat p$; they climb up and down the energy ladder. $\hat a^\dagger$ is the **raising operator** (adds one quantum $\hbar\omega$), $\hat a$ is the **lowering operator** (removes one).
- **Number operator $\hat N=\hat a^\dagger\hat a$:** counts the quanta. It is Hermitian, so it is measurable.
- **Zero-point energy $\tfrac12\hbar\omega$:** the ground state still carries energy, the oscillator can never be fully at rest.
- **Commutator relation $[\hat x,\hat p]=i\hbar$:** position and momentum do not commute; this non-commutativity is the source of the **uncertainty relation** $\sigma_x\sigma_p\ge\hbar/2$.
- **Standard deviation $\sigma_x$:** the spread of a measured quantity, $\sqrt{\langle x^2\rangle-\langle x\rangle^2}$.

Notation decoded: $\sigma_x$ is said "sigma-x"; $\hat a^\dagger$ is "a-dagger"; $[\hat a,\hat a^\dagger]$ is "commutator of a and a-dagger".

## Exercises

Attempt each one cold for 5 to 10 minutes before opening the hint. Read the solution sketch only after a real attempt.

1. Evaluate $\displaystyle\int_{-\infty}^{\infty}x^2\,e^{-m\omega x^2/(2\hbar)}\,\mathrm{d}x$ by substituting $\xi=x\sqrt{m\omega/\hbar}$, and check the units of your answer. — **Hint:** the exponent becomes $\xi^2/2$, so use the moment formula with $a=\tfrac12$; do not forget $\mathrm{d}x=\sqrt{\hbar/m\omega}\,\mathrm{d}\xi$. — **Solution sketch:** $x^2\,\mathrm{d}x=(\hbar/m\omega)^{3/2}\xi^2\,\mathrm{d}\xi$; $\int\xi^2e^{-\xi^2/2}\mathrm{d}\xi=\dfrac{\sqrt\pi}{2(1/2)^{3/2}}=\sqrt{2\pi}$; result $\sqrt{2\pi}\,(\hbar/m\omega)^{3/2}$, which has units of length cubed.
2. Differentiate $f(\xi)=e^{-\xi^2}$ and $g(\xi)=\xi\,e^{-\xi^2/2}$ twice each with respect to $\xi$. Write each answer as a polynomial times the original exponential ($e^{-\xi^2}$ for $f$, $h=e^{-\xi^2/2}$ for $g$). — **Hint:** use $f'=-2\xi f$; for $g$ use $h'=-\xi h$ and the product rule, $g'=h+\xi h'$, then differentiate again and collect. — **Solution sketch:** $f'=-2\xi f$, $f''=-2f-2\xi f'=(4\xi^2-2)f$. $g'=(1-\xi^2)h$, $g''=(-2\xi-\xi(1-\xi^2))h=(\xi^3-3\xi)h$.
3. Verify that $\psi_1(\xi)\propto\xi\,e^{-\xi^2/2}$ satisfies $\hat H\psi_1=E\psi_1$ with $\hat H=\dfrac{\hbar\omega}2\left(-\dfrac{\mathrm{d}^2}{\mathrm{d}\xi^2}+\xi^2\right)$, and find $E$. (This is the first excited state, not the ground state.) — **Hint:** use $g''$ from Exercise 2, compute $-g''+\xi^2g$, and check that all the $\xi^3$ terms cancel. — **Solution sketch:** $-g''+\xi^2g=(3\xi-\xi^3+\xi^3)h=3\xi h=3g$. So $\hat Hg=\dfrac{\hbar\omega}{2}\cdot3\,g=\dfrac{3\hbar\omega}{2}g$, and $E=\tfrac32\hbar\omega$, matching $E_1=\hbar\omega(1+\tfrac12)$.
4. Normalise $\psi_1=C\,\xi\,e^{-\xi^2/2}$ in the variable $\xi$ (that is, $\int|\psi_1|^2\mathrm{d}\xi=1$) and then compute $\langle\xi^2\rangle$, and hence $\langle x^2\rangle$, for this state. — **Hint:** $|\psi_1|^2=C^2\xi^2e^{-\xi^2}$, so you need $\int\xi^2e^{-\xi^2}$ and $\int\xi^4e^{-\xi^2}$. The second is not on the list: get it by differentiating $\int\xi^2e^{-a\xi^2}\mathrm{d}\xi=\tfrac{\sqrt\pi}{2}a^{-3/2}$ with respect to $a$ (this brings down $-\xi^2$), then set $a=1$. — **Solution sketch:** $\int\xi^2e^{-\xi^2}=\sqrt\pi/2$, so $C^2=2/\sqrt\pi$. $\int\xi^4e^{-a\xi^2}=\tfrac{3\sqrt\pi}{4}a^{-5/2}$, giving $3\sqrt\pi/4$ at $a=1$. Then $\langle\xi^2\rangle=\dfrac{2}{\sqrt\pi}\cdot\dfrac{3\sqrt\pi}{4}=\dfrac32$, and $\langle x^2\rangle=\dfrac{\hbar}{m\omega}\cdot\dfrac32$.
5. Using only $[\hat x,\hat x]=[\hat p,\hat p]=0$ and $[\hat x,\hat p]=i\hbar$ (so $[\hat p,\hat x]=-i\hbar$), show $[\hat a,\hat a^\dagger]=1$ from Eqs. (5.6), (5.7). Write $\alpha=\sqrt{m\omega/\hbar}$ and $\beta=1/\sqrt{m\hbar\omega}$ to shorten the algebra. — **Hint:** expand $\tfrac12[\alpha\hat x+i\beta\hat p,\;\alpha\hat x-i\beta\hat p]$ bilinearly; two terms vanish immediately, and note $\alpha\beta=1/\hbar$. — **Solution sketch:** $\tfrac12\left(-i\alpha\beta[\hat x,\hat p]+i\beta\alpha[\hat p,\hat x]\right)=\tfrac12\alpha\beta\left(-i\cdot i\hbar+i\cdot(-i\hbar)\right)=\tfrac12\cdot\tfrac1\hbar(\hbar+\hbar)=1$.
6. Go the other way: from $\hat x=\sqrt{\hbar/2m\omega}\,(\hat a^\dagger+\hat a)$, $\hat p=i\sqrt{m\hbar\omega/2}\,(\hat a^\dagger-\hat a)$ and $[\hat a,\hat a^\dagger]=1$, recover $[\hat x,\hat p]=i\hbar$. — **Hint:** the prefactors multiply to $i\hbar/2$; expand $[\hat a^\dagger+\hat a,\hat a^\dagger-\hat a]$ and use $[\hat a^\dagger,\hat a]=-1$. — **Solution sketch:** prefactor $=\sqrt{\tfrac{\hbar}{2m\omega}}\cdot i\sqrt{\tfrac{m\hbar\omega}{2}}=\tfrac{i\hbar}{2}$. $[\hat a^\dagger+\hat a,\hat a^\dagger-\hat a]=-[\hat a^\dagger,\hat a]+[\hat a,\hat a^\dagger]=1+1=2$ (the $[\hat a^\dagger,\hat a^\dagger]$ and $[\hat a,\hat a]$ terms are zero). So $[\hat x,\hat p]=\tfrac{i\hbar}{2}\cdot2=i\hbar$.
7. Compute $[\hat N,\hat a^\dagger]$ and $[\hat N,\hat a]$ from $\hat N=\hat a^\dagger\hat a$ and $[\hat a,\hat a^\dagger]=1$. — **Hint:** use $[AB,C]=A[B,C]+[A,C]B$ with $A=\hat a^\dagger$, $B=\hat a$; you need $[\hat a,\hat a]=0$, $[\hat a^\dagger,\hat a]=-1$ and $[\hat a,\hat a^\dagger]=1$, $[\hat a^\dagger,\hat a^\dagger]=0$. — **Solution sketch:** $[\hat N,\hat a^\dagger]=\hat a^\dagger[\hat a,\hat a^\dagger]+[\hat a^\dagger,\hat a^\dagger]\hat a=\hat a^\dagger$. $[\hat N,\hat a]=\hat a^\dagger[\hat a,\hat a]+[\hat a^\dagger,\hat a]\hat a=-\hat a$.
8. Given $\hat N|n\rangle=n|n\rangle$ and $[\hat N,\hat a^\dagger]=\hat a^\dagger$, show that $\hat a^\dagger|n\rangle$ is an eigenstate of $\hat H=\hbar\omega(\hat N+\tfrac12)$ with energy exactly $\hbar\omega$ higher than $E_n$. — **Hint:** rewrite $\hat N\hat a^\dagger=\hat a^\dagger\hat N+\hat a^\dagger$, then act on $|n\rangle$. — **Solution sketch:** $\hat N\hat a^\dagger|n\rangle=\hat a^\dagger\hat N|n\rangle+\hat a^\dagger|n\rangle=(n+1)\hat a^\dagger|n\rangle$. Then $\hat H\hat a^\dagger|n\rangle=\hbar\omega(n+1+\tfrac12)\hat a^\dagger|n\rangle=(E_n+\hbar\omega)\hat a^\dagger|n\rangle$.
9. Compute the commutator $[\hat x^2,\hat p]$. — **Hint:** use $[AB,C]=A[B,C]+[A,C]B$ with $A=B=\hat x$, and $[\hat x,\hat p]=i\hbar$. — **Solution sketch:** $[\hat x\hat x,\hat p]=\hat x[\hat x,\hat p]+[\hat x,\hat p]\hat x=i\hbar\hat x+i\hbar\hat x=2i\hbar\,\hat x$.
10. Using Eq. (5.8) and the ladder actions $\hat a|n\rangle=\sqrt n|n-1\rangle$, $\hat a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$, evaluate the matrix element $\langle2|\hat x|3\rangle$. Then explain in one sentence why $\langle n|\hat x|n\rangle=0$ for every $n$. — **Hint:** act with $(\hat a^\dagger+\hat a)$ on $|3\rangle$ first, then take the inner product with $\langle2|$ using orthonormality. — **Solution sketch:** $(\hat a^\dagger+\hat a)|3\rangle=\sqrt4\,|4\rangle+\sqrt3\,|2\rangle=2|4\rangle+\sqrt3\,|2\rangle$, so $\langle2|\hat x|3\rangle=\sqrt{\hbar/2m\omega}\cdot\sqrt3=\sqrt{3\hbar/2m\omega}$. For $\langle n|\hat x|n\rangle$, $\hat x|n\rangle$ only contains $|n\pm1\rangle$, which are orthogonal to $\langle n|$, so it is zero.

## Apply to the lecture (40 min)

Read Week 5 (`week_5/week_5_lecture.md`) in this order, with your Move 6.4 summary open beside it:

1. **§5.2** (Eqs. 5.3 to 5.5): find where $\hat H$ comes from. Start translating from Eq. (5.4) into $\xi$ using Move 6.1 (Eq. (5.5) lost its $m$'s in the export, so do not copy it) to see why the lecture calls the direct approach "no easy job".
2. **§5.3** (Eqs. 5.6 to 5.16): the whole derivation is Moves 6.4 and 6.5. Cover each line and try to produce it before reading it. Check that the Hermiticity argument for $\hat N$ uses $(AB)^\dagger=B^\dagger A^\dagger$ from Day 3.
3. **§5.4:** the three-step argument that $n$ is real, non-negative and an integer. Note where $\|\hat a|\psi_n\rangle\|^2\ge0$ is used.
4. **§5.5:** the ground state from $\hat a|0\rangle=0$ and the first excited state $\psi_1$ (compare with Exercises 2 to 4, where you handled the same shape $\xi e^{-\xi^2/2}$).

Then open the Week 5 companion, `companions/week05_companion.md`, and read its **Notation decoder** (for $\hat a$, $\hat a^\dagger$, $\hat N$, $\xi$, $\sigma$), **Skipped steps, expanded** (the derivations of Eqs. 5.10 to 5.16 with every line justified) and **Worked clones** (worked examples on functions different from the task's).

Finally, read the Week 5 task in `week_5/week_5_content.md`, section `## Apply`. Do not look for a shortcut. Attempt it cold, in the six-steps format, using Moves 6.1 to 6.3 as your toolbox; the model answers are the university's to provide.

## Anti-patterns / Common mistakes

- **Mixing $x$ and $\xi$.** Half the expression in dimensionful $x$ and half in dimensionless $\xi$ gives nonsense. Convert everything, work in one variable, and convert back only at the end.
- **Forgetting the Jacobian** $\mathrm{d}x=\sqrt{\hbar/m\omega}\,\mathrm{d}\xi$. It changes the power of $\hbar/m\omega$ in every integral. A units check (length cubed for $\int x^2\mathrm{d}x$) catches it.
- **Assuming $\hat a$ is Hermitian.** It is not: $\hat a^\dagger\ne\hat a$. Only $\hat N=\hat a^\dagger\hat a$, $\hat x$ and $\hat p$ are Hermitian. Do not write $\langle\hat a\rangle$ as if it were a measurement outcome.
- **Sign slips in commutators.** $[\hat p,\hat x]=-i\hbar$, and $[\hat a^\dagger,\hat a]=-1$. Write the sign down before you substitute.

## Confusion log

| Symbol | Step | Concept |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Tomorrow (Day 7): tensor products of qubits, the product-state test, and partial measurement, followed by a mixed problem set.

## Warm-up answers (fold below, check after writing yours)

<details>
<summary>Answers</summary>

1. $P(4)=|c_1|^2=\tfrac13$ and $P(9)=|c_2|^2=\tfrac23$ (they sum to 1). $\langle\hat A\rangle=4\cdot\tfrac13+9\cdot\tfrac23=\tfrac{22}{3}$.
2. The state collapses to $|2\rangle$; a repeat measurement gives $9$ with probability $1$.
3. $i\hbar\,\partial\Psi/\partial t=\hat H\Psi$. No: $|\Psi|^2=|\varphi|^2\,|e^{-iEt/\hbar}|^2=|\varphi|^2$, because a pure phase has modulus 1 (Move 1.3). That is why these are called stationary states.
4. $\psi=B\sin(kx)$ (the $\cos$ part is killed by $\psi(0)=0$), and $\psi(L)=0$ forces $\sin kL=0$, so $k_n=n\pi/L$ with $n=1,2,3,\dots$
5. $E_n=\hbar^2k_n^2/2m=n^2\pi^2\hbar^2/(2mL^2)$.

</details>
