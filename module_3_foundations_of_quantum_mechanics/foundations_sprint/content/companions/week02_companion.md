# Week 2 Companion — Wave Functions, Operators and Observables

Use this beside `week_2/week_2_lecture.md` (Passes 1 and 2 of the reading protocol in [STRATEGY.md](../../STRATEGY.md)). Equation numbers below are the lecture's. Built on [Day 1](../day01.md), [Day 2](../day02.md) and [Day 4](../day04.md).

## What this week is really saying

Two postulates, and each is one sentence.

**Postulate 1 (the state).** Everything there is to know about a particle is stored in one complex-valued function $\psi(\mathbf{r},t)$. You never see $\psi$ directly. What you see is $|\psi|^2$, which is a **probability density**: the chance of finding the particle in a tiny box of volume $\mathrm{d}^3\mathbf{r}$ at position $\mathbf{r}$ is $|\psi|^2\,\mathrm{d}^3\mathbf{r}$. Since the particle must be *somewhere*, the total is 1 (Eq. 2.1).

**Postulate 2 (the observables).** Every measurable quantity (position, momentum, energy, ...) is an **operator**: a machine that takes a function in and gives a function out. When you measure that quantity, the number you read off is always one of the machine's **eigenvalues**, that is, a number $q$ for which the machine returns the same function scaled, $\hat Q\psi = q\psi$.

**A picture that carries both.**

- *Probability cloud.* Think of $|\psi(\mathbf{r})|^2$ as the density of a fog. Where the fog is thick, the particle is likely to be found. The fog holds one unit of "stuff" in total, which is normalisation.
- *A ket as an arrow.* Choose a set of perpendicular unit arrows $|1\rangle, |2\rangle, \dots$ (an orthonormal basis, [Move 2.4](../day02.md)). The state $|\psi\rangle$ is an arrow, and its **components** $a_n = \langle n|\psi\rangle$ are **amplitudes**. The squared lengths $|a_n|^2$ are probabilities, so the arrow has length 1 (Eq. 2.24). A wave function is the same idea with infinitely many perpendicular arrows, one per point in space, and the sum becomes an integral.
- *An operator as a machine.* It grabs the arrow and moves it. Most arrows come out pointing in a new direction. A few special arrows (eigenvectors) come out pointing the *same* way, only longer or shorter. Those special arrows and their stretch factors are what measurements return.

The lecture is hard because it says these things in one dense page each. The rest of this companion unpacks them.

## Notation decoder

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\psi(\mathbf{r},t)$ | "psi of r and t" | the wave function: a complex number for each position and time | $\psi(x)=Ce^{-|x|}$ |
| $\psi^*$ | "psi star" | complex conjugate: flip the sign of every $i$ ([Move 1.2](../day01.md)) | $(e^{ikx})^*=e^{-ikx}$ |
| $\lvert\psi\rvert^2=\psi^*\psi$ | "mod psi squared" | probability density: real and $\ge 0$ | $\lvert e^{ikx}\rvert^2=1$ |
| $\mathbf{r}=x\hat{\mathbf e}_x+y\hat{\mathbf e}_y+z\hat{\mathbf e}_z$ | "position vector r" | a point in space, written as steps along three axes | $\mathbf r=(1,0,2)$ means $x=1,y=0,z=2$ |
| $\hat{\mathbf e}_x$ | "e-x hat" | unit arrow (length 1) along the $x$ axis; the hat here means "unit vector", not "operator" | $\hat{\mathbf e}_x=(1,0,0)$ |
| $\mathrm{d}^3\mathbf r$ | "d-three-r" | a tiny volume element, $\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ | in 1D it is just $\mathrm{d}x$ |
| $\int\lvert\psi\rvert^2\mathrm d^3\mathbf r=1$ | "the integral of mod psi squared is one" | normalisation: total probability is 1 (Eq. 2.1) | $\psi=2\,e^{-2x}$ on $x\ge0$ |
| $\lvert\psi\rangle$ | "ket psi" | the state as a vector (column) | $\lvert u\rangle=(1,0)^{\mathsf T}$ |
| $\langle\varphi\rvert$ | "bra phi" | conjugate transpose of the ket $\lvert\varphi\rangle$ ([Move 2.2](../day02.md)) | $\lvert a\rangle=(i,2)^{\mathsf T}\Rightarrow\langle a\rvert=(-i,\ 2)$ |
| $\langle\varphi\lvert\psi\rangle=\int\varphi^*\psi\,\mathrm d^3\mathbf r$ | "bra phi ket psi" | inner product: one complex number, "overlap of $\varphi$ with $\psi$" (Eqs. 2.6, 2.8) | orthogonal means it is 0 |
| $\alpha_i$ | "alpha i" | complex weights in a superposition $\sum_i\alpha_i\lvert\psi_i\rangle$ (Eq. 2.3) | $\tfrac{1}{\sqrt2}(\psi_1+\psi_2)$ |
| $\hat A$ (also written $\hat O$, $\hat Q$) | "A hat" | an operator: a rule turning a function into a function | $\hat x\psi=x\psi$ |
| $\hat A\psi=\lambda\psi$ | "A hat psi equals lambda psi" | eigenvalue equation: $\psi$ is an eigenfunction, $\lambda$ its eigenvalue | $\hat p\,e^{ikx}=\hbar k\,e^{ikx}$ |
| $\hat p_x=-i\hbar\,\partial/\partial x$ | "p-x hat" | momentum operator: differentiate, multiply by $-i\hbar$ | on $e^{ikx}$ gives $\hbar k$ |
| $\hat A^\dagger$ | "A dagger" | adjoint: the operator with $\langle\psi\lvert\hat A\phi\rangle=\langle\hat A^\dagger\psi\lvert\phi\rangle$ (Eq. 2.14) | Hermitian means $\hat A^\dagger=\hat A$ |
| $\delta_{nm}$ | "kronecker delta n m" | 1 if $n=m$, else 0; packs "orthonormal" into one symbol (Eqs. 2.18, 2.19) | $\langle n\lvert m\rangle=\delta_{nm}$ |
| $\mathcal H=L^2(S)$ | "Hilbert space, L-two of S" | the space of functions on $S$ with $\int\lvert\psi\rvert^2<\infty$ | wave functions live here |
| $\hbar$ | "h-bar" | Planck's constant over $2\pi$; sets the scale of quantum effects | appears in $\hat p$ |

Two reading habits that remove most of the confusion:

1. A **hat means operator** (except $\hat{\mathbf e}_x$, which is a unit vector). An unhatted letter, like $x$ or $\lambda$, is just a number or a function value.
2. "Bra times ket" is always an integral $\int(\text{left})^*(\text{right})$. Conjugate the left object, multiply, integrate.

## Skipped steps, expanded

### 1. The normalisation argument (Eq. 2.1)

*What the lecture says:* $|\psi|^2\mathrm d^3\mathbf r$ is the probability of finding the particle in $\mathrm d^3\mathbf r$, so the integral over all space is 1.

*The steps:*

1. Cut space into many tiny boxes labelled $j$, with volumes $\Delta V_j$. Suppose the particle is in box $j$ with probability $P_j\approx|\psi(\mathbf r_j)|^2\Delta V_j$.
2. The particle is in exactly one box, and the boxes do not overlap, so probabilities add: $\sum_jP_j=1$.
3. Let the boxes shrink. The sum becomes the integral: $\int|\psi|^2\mathrm d^3\mathbf r=1$.
4. Why $|\psi|^2$ and not $\psi$? $\psi$ is complex, so it can be negative or complex, which no probability can be. The product $\psi^*\psi=(\mathrm{Re}\,\psi)^2+(\mathrm{Im}\,\psi)^2$ is real and $\ge0$ ([Move 1.2](../day01.md)).
5. **A given $\psi$ usually comes with the wrong total.** Suppose $\int|\psi|^2\mathrm d^3\mathbf r=N$, with $0<N<\infty$. Then $\psi/\sqrt N$ has total $\frac1N\cdot N=1$. Scaling the state by a constant does not change which physical situation it describes, only its size, so this is legal. That is normalising ([Move 4.5](../day04.md)).
6. **Why "normalisable" is a requirement.** If $N=\infty$ (for instance a plane wave, where $|\psi|^2$ is constant forever) no $1/\sqrt N$ exists, and $\psi$ is not a state. If $N=0$, then $\psi=0$ everywhere: no particle at all.
7. **Phase.** $e^{i\gamma}\psi$ has the same $|\psi|^2$ for real $\gamma$ ([Move 1.3](../day01.md)), so the constant $C$ can be chosen real and positive without loss.

The lecture's "finite, continuous, single-valued" list for $\psi$ and $\psi'$ is the checklist of [Move 4.7](../day04.md). *Finite* is needed so the integral can be finite. *Single-valued* is needed so $|\psi|^2$ has one value at each point.

### 2. Superposition (Eqs. 2.2 to 2.4)

*What the lecture says:* if $\psi_1,\psi_2$ are states then so is $\alpha_1\psi_1+\alpha_2\psi_2$.

*The steps:*

1. This is the vector-space property of [Day 2](../day02.md): you can add arrows and scale them by complex numbers, and you still have an arrow. Adding functions pointwise and scaling them by a constant is exactly that.
2. **Caution on Eq. 2.4.** It writes $P=\left|\sum_i\alpha_i|\psi_i\rangle\right|^2$. Read this as shorthand for "square the length of the combined arrow", i.e. $P=\langle\psi|\psi\rangle$ where $|\psi\rangle=\sum_i\alpha_i|\psi_i\rangle$. It is the *norm squared*, a single number. The pointwise density is $|\psi(\mathbf r)|^2$, a function.
3. Expand the norm for two terms. Anti-linearity in the bra (Eq. 2.10) and linearity in the ket (Eq. 2.9) give
$$\langle\psi|\psi\rangle=|\alpha_1|^2\langle\psi_1|\psi_1\rangle+|\alpha_2|^2\langle\psi_2|\psi_2\rangle+\alpha_1^*\alpha_2\langle\psi_1|\psi_2\rangle+\alpha_2^*\alpha_1\langle\psi_2|\psi_1\rangle.$$
4. The last two terms are conjugates of each other (Eq. 2.11), so together they equal $2\,\mathrm{Re}\left(\alpha_1^*\alpha_2\langle\psi_1|\psi_2\rangle\right)$. This is the **interference** term.
5. If $\psi_1,\psi_2$ are orthonormal (Eq. 2.18), the cross terms vanish and $\langle\psi|\psi\rangle=|\alpha_1|^2+|\alpha_2|^2$. Normalisation then reads $\sum_i|\alpha_i|^2=1$, which is Eq. 2.24 for two terms.

### 3. Eigenfunction and eigenvalue statements (Eqs. 2.12 to 2.17, 2.21)

*What the lecture says:* $\hat A\psi=\lambda\psi$; measured values are eigenvalues; for Hermitian $\hat A$, eigenvalues are real and eigenfunctions of different eigenvalues are orthogonal.

*The steps for "$e^{i\mathbf k\cdot\mathbf r}$ is a momentum eigenfunction", in one dimension:*

1. $\hat p\,e^{ikx}=-i\hbar\dfrac{\mathrm d}{\mathrm dx}e^{ikx}=-i\hbar\,(ik)\,e^{ikx}$ (chain rule: the derivative of $e^{ikx}$ is $ik\,e^{ikx}$).
2. $-i\cdot i=-i^2=1$, so this is $\hbar k\,e^{ikx}$. The eigenvalue is $\hbar k$ (the de Broglie relation, [Move 4.8](../day04.md)).

*The steps for "eigenvalues of a Hermitian operator are real". The lecture compresses these lines, so here they are in full.*

1. Let $\hat A\psi_n=\lambda_n\psi_n$ and $\hat A\psi_m=\lambda_m\psi_m$, and $\hat A=\hat A^\dagger$.
2. Ket side, linear (Eq. 2.9): $\langle\psi_n|\hat A\psi_m\rangle=\lambda_m\langle\psi_n|\psi_m\rangle$.
3. Bra side, anti-linear (Eq. 2.10), using the definition of the adjoint (Eq. 2.14) and $\hat A^\dagger=\hat A$: $\langle\psi_n|\hat A\psi_m\rangle=\langle\hat A\psi_n|\psi_m\rangle=\lambda_n^*\langle\psi_n|\psi_m\rangle$. (The lecture's middle line, $\langle\psi_n|\hat A^\dagger\psi_m\rangle=\lambda_n^*\ldots$, is correct but compressed; here it is expanded. The eigenvalue $\lambda_n$ is conjugated because it comes out of the bra.)
4. Subtract: $(\lambda_n^*-\lambda_m)\langle\psi_n|\psi_m\rangle=0$.
5. Take $n=m$. Then $\langle\psi_n|\psi_n\rangle>0$, so $\lambda_n^*=\lambda_n$: real.
6. Take $n\neq m$ with $\lambda_n\neq\lambda_m$. Since eigenvalues are real, $\lambda_n^*-\lambda_m=\lambda_n-\lambda_m\neq0$, so $\langle\psi_n|\psi_m\rangle=0$: orthogonal.

*The steps for reading off expansion coefficients (Eq. 2.21).* The lecture cites "linearity from Eq. (2.12)"; the property actually used is linearity of the inner product in the ket, Eq. 2.9.

1. Start from $\psi=\sum_ma_m\psi_m$.
2. Take the inner product with $\psi_n$: $\langle\psi_n|\psi\rangle=\sum_ma_m\langle\psi_n|\psi_m\rangle$ (linearity in the ket).
3. Orthonormality: $\langle\psi_n|\psi_m\rangle=\delta_{nm}$, so only the term $m=n$ survives: $\langle\psi_n|\psi\rangle=a_n$.

## Moves used this week

- **[Move 1.2](../day01.md)** complex numbers, conjugate, $|z|^2=z^*z$: for $|\psi|^2$, and every inner product.
- **[Move 1.3](../day01.md)** Euler, $|e^{i\theta}|=1$, global phase: for plane waves and for choosing $C$ real.
- **[Move 2.2](../day02.md)** ket, bra, inner product: Eqs. 2.5 to 2.11.
- **[Move 2.3](../day02.md)** inner-product axioms: the proofs in the worked clones below.
- **[Move 2.4](../day02.md)** orthonormal expansion and normalisation: Eqs. 2.18 to 2.24.
- **[Move 4.1](../day04.md)** functions as vectors, $\langle\varphi|\psi\rangle=\int\varphi^*\psi\,\mathrm dx$: Eq. 2.8.
- **[Move 4.2](../day04.md)** exponential and half-line integrals, sketching $|\psi|^2$.
- **[Move 4.3](../day04.md)** integration by parts.
- **[Move 4.4](../day04.md)** Gaussian integrals and odd integrands.
- **[Move 4.5](../day04.md)** normalisation: find $C$.
- **[Move 4.6](../day04.md)** probability in an interval and expectation values.
- **[Move 4.7](../day04.md)** acceptable-wave-function checklist.
- **[Move 4.8](../day04.md)** $\hat p=-i\hbar\,\mathrm d/\mathrm dx$ and plane waves.

## Worked clones

Each clone is the same *type* of problem as one of the week's task problems, on a **different object**. Write your own solution first, then compare. Each is in the [six-steps stand-in format](../../STRATEGY.md#six-steps-write-up-stand-in). Nothing here is a solution to a course problem instance.

### Clone 1 — proving a bra-ket identity from the axioms

**Axioms used** (the course's two, plus the scalar half of the first, which is lecture Eq. 2.9 with $\alpha_2=0$):

1. linearity in the ket: $\langle C|\{|A\rangle+|B\rangle\}=\langle C|A\rangle+\langle C|B\rangle$ and $\langle C|\alpha A\rangle=\alpha\langle C|A\rangle$;
2. conjugate symmetry: $\langle B|A\rangle=\langle A|B\rangle^*$.

**Problem.** For any kets $A,B$ and complex $\alpha$, prove (a) $\langle\alpha A|B\rangle=\alpha^*\langle A|B\rangle$; (b) $\langle A|B\rangle+\langle B|A\rangle$ is a real number.

1. **Restate.** Prove (a) and (b) using only the axioms above. Givens: $A,B$ are kets, $\alpha\in\mathbb C$.
2. **Write the state.** No particular functions are needed. Let $z=\langle A|B\rangle$, a single complex number. Concretely, to test the answer later, take $A=(1,i)^{\mathsf T}$, $B=(2,1)^{\mathsf T}$, for which $z=1\cdot2+(-i)(1)=2-i$.
3. **Name the move.** [Move 2.3](../day02.md): use axiom 2 to swap the two slots, use axiom 1 to pull the scalar out of the ket slot, then use axiom 2 again to swap back.
4. **Algebra.**
   (a) Axiom 2 with roles $\alpha A\to$ first slot, $B\to$ second: $\langle\alpha A|B\rangle=\langle B|\alpha A\rangle^*$. Axiom 1 (scalar): $\langle B|\alpha A\rangle=\alpha\langle B|A\rangle$. So $\langle\alpha A|B\rangle=\left(\alpha\langle B|A\rangle\right)^*=\alpha^*\langle B|A\rangle^*$, using $(uv)^*=u^*v^*$. Axiom 2 once more: $\langle B|A\rangle^*=\langle A|B\rangle$. Hence $\langle\alpha A|B\rangle=\alpha^*\langle A|B\rangle$.
   (b) By axiom 2, $\langle B|A\rangle=\langle A|B\rangle^*=z^*$. So the sum is $z+z^*=(x+iy)+(x-iy)=2x=2\,\mathrm{Re}\,z$, with $x=\mathrm{Re}\,z$ and $y=\mathrm{Im}\,z$ real. A real number.
5. **Check.** With $A=(1,i)^{\mathsf T}$, $B=(2,1)^{\mathsf T}$: $\langle B|A\rangle=2\cdot1+1\cdot i=2+i$, so the sum is $(2-i)+(2+i)=4=2\,\mathrm{Re}(2-i)$. For (a), take $\alpha=i$: $\alpha A=(i,-1)^{\mathsf T}$, bra $=(-i,-1)$, $\langle\alpha A|B\rangle=(-i)(2)+(-1)(1)=-1-2i$. And $\alpha^*z=(-i)(2-i)=-2i+i^2=-1-2i$. They match.
6. **Answer.** $\langle\alpha A|B\rangle=\alpha^*\langle A|B\rangle$ (scalars leave the bra conjugated), and $\langle A|B\rangle+\langle B|A\rangle=2\,\mathrm{Re}\langle A|B\rangle$ is real.

**Try it yourself.**

1. Prove that $\langle A|B\rangle-\langle B|A\rangle$ is purely imaginary (real part zero), and that $\langle\alpha A|\beta B\rangle=\alpha^*\beta\langle A|B\rangle$ for complex $\alpha,\beta$. Then check the second identity for $\alpha=1+i$, $\beta=2$, $A=(1,0)^{\mathsf T}$, $B=(1,1)^{\mathsf T}$. — **Hint:** first part: with $z=\langle A|B\rangle$, axiom 2 makes the difference $z-z^*$; for the second, pull $\beta$ out of the ket slot first, then use clone 1(a). — **Solution sketch:** $z-z^*=(x+iy)-(x-iy)=2iy$, purely imaginary. Next, $\langle\alpha A|\beta B\rangle=\beta\langle\alpha A|B\rangle=\beta\alpha^*\langle A|B\rangle$. Numbers: $\langle A|B\rangle=1\cdot1+0\cdot1=1$; the ket $\alpha A=(1+i,0)^{\mathsf T}$ has bra $(1-i,0)$; $\beta B=(2,2)^{\mathsf T}$; so $\langle\alpha A|\beta B\rangle=(1-i)(2)+0=2-2i$. The formula gives $\alpha^*\beta\langle A|B\rangle=(1-i)(2)(1)=2-2i$. They match.

### Clone 2 — a combination of eigenfunctions is an eigenfunction

**Setting.** Instead of the operator used in the course task, use $\hat Q=\dfrac{\mathrm d^4}{\mathrm dx^4}$ (differentiate four times), on the functions $f=\sin kx$ and $g=\cos kx$, with $k$ a positive real constant.

**Problem.** Show $f$ and $g$ are eigenfunctions of $\hat Q$ with the same eigenvalue, that every combination $af+bg$ is too, and find two combinations that are orthogonal on the interval $(0,\pi/k)$.

1. **Restate.** Find $q$ with $\hat Qf=qf$, $\hat Qg=qg$. Then test $h=af+bg$ ($a,b$ constants). Then find two combinations $h_1,h_2$ with $\langle h_1|h_2\rangle=\int_0^{\pi/k}h_1h_2\,\mathrm dx=0$ (real functions, so no conjugates are needed).
2. **Write the state.** Differentiate each function four times and list the results:

   | | $f=\sin kx$ | $g=\cos kx$ |
   |---|---|---|
   | first | $k\cos kx$ | $-k\sin kx$ |
   | second | $-k^2\sin kx$ | $-k^2\cos kx$ |
   | third | $-k^3\cos kx$ | $k^3\sin kx$ |
   | fourth | $k^4\sin kx$ | $k^4\cos kx$ |
3. **Name the move.** Eigenvalue equation ($\hat Q\psi=q\psi$) plus linearity of differentiation; for orthogonality, [Move 4.1](../day04.md) and the double-angle identity ([Move 1.4](../day01.md)).
4. **Algebra.** The fourth row gives $\hat Qf=k^4f$ and $\hat Qg=k^4g$: same eigenvalue $q=k^4$. For $h=af+bg$, linearity gives $\hat Qh=a\hat Qf+b\hat Qg=ak^4f+bk^4g=k^4h$. So $h$ is an eigenfunction with the same eigenvalue $k^4$ (unless $a=b=0$, the zero function).
   Orthogonality: try $h_1=f+g$ and $h_2=f-g$. Then $h_1h_2=f^2-g^2=\sin^2kx-\cos^2kx=-\cos2kx$. So
   $$\langle h_1|h_2\rangle=-\int_0^{\pi/k}\cos2kx\,\mathrm dx=-\left[\frac{\sin2kx}{2k}\right]_0^{\pi/k}=-\frac{\sin2\pi-\sin0}{2k}=0.$$
5. **Check.** Direct: $h_1''''=(\sin kx+\cos kx)''''=k^4(\sin kx+\cos kx)$, matches. Sanity: on $(0,\pi/k)$ the function $\sin^2kx-\cos^2kx$ is negative near the ends and positive in the middle, and the two lobes have equal area, so zero is plausible. (Also $f$ and $g$ themselves are orthogonal here: $\int_0^{\pi/k}\sin kx\cos kx\,\mathrm dx=\left[\tfrac{\sin^2kx}{2k}\right]_0^{\pi/k}=0$.)
6. **Answer.** $\hat Q$ has eigenvalue $k^4$ for both $\sin kx$ and $\cos kx$; every combination $a\sin kx+b\cos kx$ is an eigenfunction with the same eigenvalue; and $\sin kx\pm\cos kx$ are orthogonal on $(0,\pi/k)$.

**Try it yourself.**

2. Let $\hat p=-i\hbar\,\mathrm d/\mathrm dx$ and $f=e^{2ix}$, $g=e^{-2ix}$. Find the eigenvalue of $\hat p$ for each. Is $f+g$ an eigenfunction of $\hat p$? Which operator built from $\hat p$ gives $f$ and $g$ the *same* eigenvalue, and what is it? — **Hint:** apply $\hat p$ to each and to $f+g=2\cos2x$; for the second operator try applying $\hat p$ twice. — **Solution sketch:** $\hat pf=-i\hbar(2i)f=2\hbar f$ and $\hat pg=-i\hbar(-2i)g=-2\hbar g$, so the eigenvalues differ ($\pm2\hbar$). Then $\hat p(2\cos2x)=-i\hbar(-4\sin2x)=4i\hbar\sin2x$, which is not a multiple of $\cos2x$, so $f+g$ is *not* an eigenfunction: the "same eigenvalue" condition matters. But $\hat p^2f=2\hbar\cdot2\hbar f=4\hbar^2f$ and $\hat p^2g=(-2\hbar)^2g=4\hbar^2g$, so under $\hat p^2$ both have eigenvalue $4\hbar^2$, and then $\cos2x$ is an eigenfunction of $\hat p^2$ with $4\hbar^2$.

### Clone 3 — normalising, and checking acceptability

**Problem.** For each function, decide whether it can be a one-dimensional wave function and find $C$ where it can. (a) $\psi_a(x)=Cx\,e^{-x}$ for $x\ge0$, and $0$ for $x<0$. (b) $\psi_b(x)=C\,e^{ikx}$ for all real $x$, $k$ real. $C>0$ real is assumed for (a).

**(a) in the six-steps format.**

1. **Restate.** Test whether $\int|\psi_a|^2\mathrm dx$ is finite; if so find $C$ with $\int|\psi_a|^2\mathrm dx=1$; also check continuity of $\psi_a$ and $\psi_a'$.
2. **Write the state.** $|\psi_a|^2=C^2x^2e^{-2x}$ for $x\ge0$, else 0. Shape: zero at $x=0$, rises, peaks, decays. The derivative of $x^2e^{-2x}$ is $2x(1-x)e^{-2x}$, zero at $x=1$, so the peak is at $x=1$ and the density is thin far out.
3. **Name the move.** Normalisation ([Move 4.5](../day04.md)) with a half-line integral ([Move 4.2](../day04.md)) done by parts twice ([Move 4.3](../day04.md)); then the acceptability checklist ([Move 4.7](../day04.md)).
4. **Algebra.** $I=\int_0^\infty x^2e^{-2x}\mathrm dx$. Integration by parts with $u=x^2$, $\mathrm dv=e^{-2x}\mathrm dx$:
   $$I=\left[-\tfrac12x^2e^{-2x}\right]_0^\infty+\int_0^\infty xe^{-2x}\mathrm dx.$$
   The boundary term is 0 at both ends (at $\infty$ the exponential beats $x^2$). Again with $u=x$:
   $$\int_0^\infty xe^{-2x}\mathrm dx=\left[-\tfrac12xe^{-2x}\right]_0^\infty+\tfrac12\int_0^\infty e^{-2x}\mathrm dx=0+\tfrac12\cdot\tfrac12=\tfrac14.$$
   So $I=\tfrac14$ and $C^2I=1$ gives $C^2=4$, $C=2$.
   Acceptability: $\psi_a$ is finite everywhere, single-valued, and continuous (at $x=0$ both sides give 0). Its derivative is $0$ for $x<0$ but $\psi_a'(0^+)=C(1-0)e^0=C=2$ for $x>0$: a jump.
5. **Check.** Peak height: $|\psi_a(1)|^2=4e^{-2}\approx0.54$. A hump of height about 0.5 and width of order 2 has area of order 1, consistent. The integrand is positive, so $I>0$, as it must be. Units: $x$ is measured in units of the decay length (the exponent $x$ in $e^{-x}$ must be dimensionless), so $C=2$ is in units of length$^{-1/2}$ once that length is restored.
6. **Answer.** $\psi_a$ is normalisable, with $C=2$. But its first derivative jumps at $x=0$, so $\psi_a$ is normalisable and continuous, but $\psi_a'$ jumps at $x=0$ (0 on the left, $C$ on the right). It therefore fails the continuous-derivative test ([Day 4](../day04.md) [Move 4.7](../day04.md), test 4), so it is acceptable only if an infinite wall sits at $x=0$.

**(b).**

1. **Restate.** Can $\psi_b=Ce^{ikx}$ be normalised?
2. **Write the state.** $|\psi_b|^2=|C|^2|e^{ikx}|^2=|C|^2\cdot1$ ($|e^{i\theta}|=1$, [Move 1.3](../day01.md)): a flat line at height $|C|^2$ for all $x$.
3. **Name the move.** Normalisation: total area under a constant.
4. **Algebra.** $\int_{-L}^{L}|C|^2\mathrm dx=2L|C|^2$. As $L\to\infty$ this is infinite for any $C\ne0$, and it is 0 for $C=0$. Neither is 1.
5. **Check.** A flat density spread over all space has infinite area, so no scaling can fix it. This is the plane wave from Postulate 2, an eigenfunction of $\hat p$ with eigenvalue $\hbar k$.
6. **Answer.** $\psi_b$ cannot be normalised, so it is not a physical state by itself, even though it is a perfectly good eigenfunction. Real states are superpositions of several such plane waves (a "wave packet"), which are normalisable.

**Try it yourself.**

3. Normalise $\psi(x)=Cx\,e^{-x^2/2}$ for all real $x$ (take $C>0$), and state whether $\psi$ is acceptable. — **Hint:** $|\psi|^2=C^2x^2e^{-x^2}$, an even function, so use the Gaussian moment from [Move 4.4](../day04.md), $\int_{-\infty}^{\infty}x^2e^{-ax^2}\mathrm dx=\sqrt\pi/(2a^{3/2})$ with $a=1$; check $\psi$ and $\psi'$ for jumps. — **Solution sketch:** $\int_{-\infty}^\infty x^2e^{-x^2}\mathrm dx=\sqrt\pi/2$, so $C^2\sqrt\pi/2=1$, $C^2=2/\sqrt\pi$, $C=\sqrt2\,\pi^{-1/4}\approx1.06$. Acceptability: $\psi'=C(1-x^2)e^{-x^2/2}$, finite and continuous, and $\psi$ is finite, continuous and single-valued and decays at both ends, so yes. Check: $|\psi|^2$ vanishes at $x=0$ and has two symmetric humps at $x=\pm1$ (derivative of $x^2e^{-x^2}$ is $2x(1-x^2)e^{-x^2}$), each of height $C^2e^{-1}\approx0.42$; total area of order 1 is plausible.

## Retrieval questions

Closed book. Each names the misconception it traps. Attempt before opening the hint.

1. A function $\psi$ has $\int_{-\infty}^\infty|\psi|^2\mathrm dx=3$. Is it a valid state as it stands? What is the fix? *(Traps: "the norm has to be built into $\psi$ already", or "the total of $\psi$, not $|\psi|^2$, is 1".)* — **Hint:** the total probability must be 1; how do you rescale $\psi$ by a constant to change the integral by a factor of $\tfrac13$? — **Solution sketch:** As it stands the total probability is 3, not 1, so it is not normalised. Scaling $\psi\to\psi/\sqrt3$ multiplies $|\psi|^2$ by $\tfrac13$, giving total 1. The scaled function describes the same physical situation; only $|\psi|^2$'s size was wrong.

2. In one dimension, what are the units of $\psi$, and why is $\psi$ itself not a probability? *(Traps: "$\psi$ is the probability", "$|\psi|^2$ is a probability rather than a density".)* — **Hint:** $|\psi|^2\mathrm dx$ is a probability (dimensionless). What units does $\mathrm dx$ carry? — **Solution sketch:** $|\psi|^2\mathrm dx$ has no units, and $\mathrm dx$ has units of length, so $|\psi|^2$ has units 1/length and $\psi$ has units length$^{-1/2}$. $\psi$ is complex-valued and has the wrong units for a probability; $|\psi|^2$ is a probability per unit length, a density.

3. Write $\int\varphi^*\hat A\psi\,\mathrm dx$ in bra-ket notation. Is $\langle\hat A\varphi|\psi\rangle$ always the same thing? *(Traps: putting a star inside the bra symbol, moving the operator to the bra without checking that $\hat A$ is Hermitian.)* — **Hint:** the conjugation is built into the bra; the operator acts on whatever is to its right. For the second part, recall what Eq. 2.14 says about moving an operator across. — **Solution sketch:** It is $\langle\varphi|\hat A\psi\rangle$. By Eq. 2.14, moving $\hat A$ onto the bra gives $\langle\hat A^\dagger\varphi|\psi\rangle$, so $\langle\hat A\varphi|\psi\rangle$ equals it only when $\hat A^\dagger=\hat A$ (Hermitian). For general $\hat A$ the two differ.

4. Is $\cos kx$ a momentum eigenfunction? Is $e^{ikx}$? *(Trap: "any wave is a momentum eigenstate", "real functions can be eigenfunctions of $\hat p$".)* — **Hint:** apply $-i\hbar\,\mathrm d/\mathrm dx$ to each and ask whether the result is a constant times the original. — **Solution sketch:** $\hat p\cos kx=-i\hbar(-k\sin kx)=i\hbar k\sin kx$, which is not a multiple of $\cos kx$: not an eigenfunction. $\hat p\,e^{ikx}=\hbar k\,e^{ikx}$: yes, eigenvalue $\hbar k$. Since $\cos kx=\tfrac12(e^{ikx}+e^{-ikx})$, it is a superposition of momenta $+\hbar k$ and $-\hbar k$.

5. $\hat A$ is Hermitian with eigenvalues 2 and 5, with eigenfunctions $\psi_a$ and $\psi_b$. Show $\langle\psi_a|\psi_b\rangle=0$. Are $\psi_a,\psi_b$ automatically *orthonormal*? *(Trap: "orthogonal" and "orthonormal" mean the same.)* — **Hint:** evaluate $\langle\psi_a|\hat A\psi_b\rangle$ in two ways (act right, act left) and subtract. — **Solution sketch:** Acting right: $\langle\psi_a|\hat A\psi_b\rangle=5\langle\psi_a|\psi_b\rangle$. Acting left (Hermitian): $=\langle\hat A\psi_a|\psi_b\rangle=2^*\langle\psi_a|\psi_b\rangle=2\langle\psi_a|\psi_b\rangle$. So $3\langle\psi_a|\psi_b\rangle=0$: orthogonal. Not automatically orthonormal: $3\psi_a$ is still an eigenfunction with eigenvalue 2, so lengths are free and must be fixed by hand (normalise).

6. An operator has eigenvalue $q$ with only one independent eigenfunction. What is the eigenvalue called? Give an example of the opposite case from Clone 2. *(Trap: "degenerate" sounds like "broken" or "bad".)* — **Hint:** it is about counting independent eigenfunctions for one eigenvalue; recall the eigenvalue $k^4$ of $\mathrm d^4/\mathrm dx^4$. — **Solution sketch:** One eigenfunction: non-degenerate. Two or more independent eigenfunctions with the same eigenvalue: degenerate. Example: $\mathrm d^4/\mathrm dx^4$ has $\sin kx$ and $\cos kx$ (and $e^{\pm kx}$) all with eigenvalue $k^4$. Degeneracy is normal and harmless; orthogonal eigenfunctions can still be chosen within it (the lecture asserts this without proof).

7. For $\psi(x)=x$, compute $\hat x\hat p\psi$ and $\hat p\hat x\psi$. Do the operators commute? *(Trap: "operators built from multiplication and differentiation all commute", "operators can be reordered freely".)* — **Hint:** work from the right: apply the operator nearest $\psi$ first. — **Solution sketch:** $\hat p\psi=-i\hbar\cdot1$, so $\hat x\hat p\psi=x\cdot(-i\hbar)=-i\hbar x$. And $\hat x\psi=x^2$, so $\hat p\hat x\psi=-i\hbar\cdot2x=-2i\hbar x$. Not equal, so they do not commute; the difference $(\hat x\hat p-\hat p\hat x)\psi=i\hbar x=i\hbar\psi$. (Both operators are still linear and associative.)

8. $\psi_1,\psi_2$ are orthonormal states and $\psi=(\psi_1+\psi_2)/\sqrt2$. Is $\psi$ normalised? Is $|\psi(x)|^2=\tfrac12|\psi_1|^2+\tfrac12|\psi_2|^2$ at every point? *(Traps: "probabilities of a superposition just add", "superposition breaks normalisation".)* — **Hint:** expand $\langle\psi|\psi\rangle$ as in Skipped Step 2; then look at the pointwise product $\psi^*\psi$ and its cross terms. — **Solution sketch:** $\langle\psi|\psi\rangle=\tfrac12(1+1+2\,\mathrm{Re}\langle\psi_1|\psi_2\rangle)=\tfrac12(1+1+0)=1$: normalised. But pointwise $|\psi|^2=\tfrac12|\psi_1|^2+\tfrac12|\psi_2|^2+\mathrm{Re}(\psi_1^*\psi_2)$. The cross term is zero only *after integrating*, not at each point. Example: where $\psi_1=\psi_2=1$ (real), $|\psi|^2=\tfrac12\cdot4=2$, not $1$. That local excess is interference.

9. Why can a measured value never be complex? Prove it for an eigenfunction $\psi$ of a Hermitian $\hat A$ with eigenvalue $\lambda$, and say whether "every operator is an observable" is true. *(Traps: "any operator is measurable", "eigenvalues can be complex".)* — **Hint:** compute $\langle\psi|\hat A\psi\rangle$ once acting right and once acting left, using $\hat A=\hat A^\dagger$. — **Solution sketch:** Right: $\langle\psi|\hat A\psi\rangle=\lambda\langle\psi|\psi\rangle$. Left: $=\langle\hat A\psi|\psi\rangle=\lambda^*\langle\psi|\psi\rangle$. So $(\lambda-\lambda^*)\langle\psi|\psi\rangle=0$ and, since $\langle\psi|\psi\rangle>0$, $\lambda=\lambda^*$: real. Not every operator is an observable: observables must be Hermitian (Postulate 2), which is exactly what guarantees real measurement outcomes.

10. The state is $\psi=3\psi_1+4i\,\psi_2$ with $\psi_1,\psi_2$ orthonormal eigenfunctions. Find $a_1=\langle\psi_1|\psi\rangle$ and $a_2=\langle\psi_2|\psi\rangle$, then normalise $\psi$. *(Trap: squaring $a_n$ instead of $|a_n|^2$; forgetting the bra conjugates.)* — **Hint:** use $\langle\psi_n|\psi_m\rangle=\delta_{nm}$ and linearity in the ket; then the norm is $\sum|a_n|^2$. — **Solution sketch:** $a_1=3$, $a_2=4i$. Norm squared $=|3|^2+|4i|^2=9+16=25$ (with $a_n^2$ one would get $9-16=-7$, absurd). So the normalised state is $\tfrac15(3\psi_1+4i\psi_2)$, with $|a_1|^2=\tfrac9{25}$ and $|a_2|^2=\tfrac{16}{25}$ adding to 1.

## Six-steps write-up template

Use this for any "normalise", "is this an acceptable wave function?" or "find the constant" problem. It follows the stand-in in [STRATEGY.md](../../STRATEGY.md#six-steps-write-up-stand-in), not the university's own text.

1. **Restate.** Write "find $C$ such that $\int|\psi|^2\,\mathrm dx=1$" and "decide whether $\psi$ is acceptable". List the givens: the formula for $\psi$, where it is non-zero, and which constants are real and positive.
2. **Write the state.** Compute $|\psi|^2=\psi^*\psi$ explicitly. Sketch it: where it is zero, where it peaks, how it decays. If $\psi$ is piecewise, write each piece with its range.
3. **Name the move.** Say it in words: "Normalisation ([Move 4.5](../day04.md)); half-line or Gaussian integral ([Move 4.2](../day04.md) or 4.4); by parts if a polynomial multiplies an exponential ([Move 4.3](../day04.md)); acceptability checklist ([Move 4.7](../day04.md))".
4. **Algebra.** First test the integral: is it finite? If it diverges, stop: not normalisable. If finite, solve $C^2\cdot(\text{integral})=1$ for $C$. Show the limits, the piece-by-piece integration, and any boundary terms.
5. **Check.** Is $|\psi|^2\ge0$? Do the peak height and width give an area of order 1? Are $\psi$ and $\psi'$ finite and continuous at joins? Are units right ($\psi$ has units length$^{-1/2}$ in 1D)? A limiting case, if there is one.
6. **Answer.** One sentence: "$\psi$ is / is not normalisable; $C=\ldots$; it is / is not acceptable because ...".

Common slip to police at step 4: integrating $\psi$ instead of $|\psi|^2$, and forgetting the factor 2 for an even integrand on the whole line.
