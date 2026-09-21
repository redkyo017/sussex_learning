# Day 4 — Calculus as the Module Uses It

> **Physics pair for today:** [P3 — Springs, Standing Waves and Confinement](physics/P3.md) (~1 h 35).

**Time box (~3.5 h):** warm-up 20 min · moves 60 min · exercises 90 min · apply 40 min · confusion log 10 min.

## Why this matters

Every wave-function problem in Weeks 2, 3 and 5 is the same three-step routine: square the function, integrate it, read off a number. You need normalisation (find $C$), probabilities in an interval, expectation values, and a quick check that a function is a legal wave function. The calculus involved is small: exponentials, $\sin^2$, one integration by parts and one Gaussian formula. Today teaches exactly that and no more. It unlocks the Week 2 wave-function task (Postulates 1 and 2), the Week 3 acceptability question, and the Gaussian integrals in the Week 5 oscillator problems.

The one idea to hold on to: **functions are just infinite-length vectors.** A vector has components $v_1, v_2, v_3, \dots$; a function has a component $\psi(x)$ at every point $x$. The dot product sums products of components; the function version *integrates* them. Nothing new is happening.

## Warm-up (retrieval, five Day 3 questions, closed book)

Answers are at the bottom of the file. Attempt all five before looking.

1. Find the eigenvalues of $\begin{pmatrix}4&2\\2&1\end{pmatrix}$ and one normalised eigenvector for each.
2. State the rule for $(AB)^\dagger$, and say what "Hermitian" means for a matrix.
3. Write down $\sigma_z$, and give its two eigenvalues with their eigenvectors.
4. Compute the commutator $[\sigma_x,\sigma_z]$ as a matrix.
5. Is $\begin{pmatrix}1&i\\-i&1\end{pmatrix}$ Hermitian? What must be true of its eigenvalues, and why?

## Moves

### Move 4.1 — Functions as vectors: $\langle\phi|\psi\rangle=\int\phi^*\psi\,\mathrm{d}x$

Say it as: "bra phi, ket psi equals the integral of phi-star times psi, dx".

For column vectors (Move 2.2), $\langle\phi|\psi\rangle=\sum_n \phi_n^*\psi_n$: conjugate the bra's components, multiply component by component, add. For functions the "components" are the values $\phi(x)$ and $\psi(x)$, and "add over all components" becomes "integrate over all $x$":

$$\langle\phi|\psi\rangle=\int_{-\infty}^{\infty}\phi^*(x)\,\psi(x)\,\mathrm{d}x .$$

Everything from Day 2 carries over: linearity in the ket, $\langle\psi|\phi\rangle=\langle\phi|\psi\rangle^*$, and $\langle\psi|\psi\rangle\ge 0$. The special case $\langle\psi|\psi\rangle=\int\psi^*\psi\,\mathrm{d}x=\int|\psi|^2\mathrm{d}x$ is the "length squared" of the function, and "normalised" means length 1. Two functions are orthogonal when $\langle\phi|\psi\rangle=0$. The lecture defines a Hilbert space as the space of allowed states; for functions this amounts to requiring that the length squared is finite.

*Worked example (not a course problem).* On $[0,1]$ take $\phi(x)=1$ and $\psi(x)=x^2$. Then $\langle\phi|\psi\rangle=\int_0^1 x^2\,\mathrm{d}x=\tfrac13$ and $\langle\psi|\psi\rangle=\int_0^1 x^4\,\mathrm{d}x=\tfrac15$. So $x^2$ has length $1/\sqrt5$ and is not orthogonal to the constant function.

### Move 4.2 — Integral cheat sheet, part 1: exponentials, $\sin^2$, half-lines, sketching $|\psi|^2$

Each line ends with *when the module needs it*.

- **Exponential:** $\displaystyle\int e^{ax}\,\mathrm{d}x=\frac{e^{ax}}{a}$ for $a\neq0$. Hence $\displaystyle\int_0^\infty e^{-ax}\mathrm{d}x=\frac1a$ for $a>0$. *Needed when* a decaying exponential (like a bound-state tail) must be normalised.
- **Absolute value:** split at the kink. $\displaystyle\int_{-\infty}^{\infty}e^{-a|x|}\mathrm{d}x=\int_{-\infty}^{0}e^{ax}\mathrm{d}x+\int_0^\infty e^{-ax}\mathrm{d}x=\frac2a$. *Needed when* $|x|$ appears in a wave function; you cannot integrate $|x|$ in one piece.
- **Sine squared:** $\sin^2\theta=\tfrac12(1-\cos2\theta)$ (Move 1.4), so $\displaystyle\int_0^{b}\sin^2(kx)\,\mathrm{d}x=\frac b2-\frac{\sin(2kb)}{4k}$. Over a whole number of half-periods the second term is 0. *Needed when* a sine-shaped wave function sits in a finite region (box states).
- **Half-lines and pieces:** $\int_{-\infty}^\infty=\int_{-\infty}^{a}+\int_a^{b}+\int_b^\infty$. A function that is 0 on a stretch contributes 0 there, so only integrate where $\psi\neq0$. *Needed when* a wave function is defined piecewise.
- **Sketching $|\psi|^2$:** square the height at every point (negative parts become positive, complex parts use $|z|^2=z^*z$), then note where it is zero, where it peaks, and where it decays. *Needed when* a problem says "sketch the probability density".

### Move 4.3 — Integration by parts, and when boundary terms vanish

The rule: $\displaystyle\int_a^b u\,v'\,\mathrm{d}x=\big[u\,v\big]_a^b-\int_a^b u'\,v\,\mathrm{d}x$. It moves a derivative from one factor onto the other, at the price of a minus sign and a **boundary term** $[uv]$.

For wave functions the boundary term is at $\pm\infty$ (or at the edges of a region where $\psi$ is 0). The rule to remember: the boundary term vanishes for normalisable functions that die away at infinity (fast enough that $\int|\psi|^2\mathrm{d}x$ converges). Exercise 7 does one concrete case. *Needed when* you compare two integrals that differ only in which factor carries the derivative, or evaluate $\int x\,e^{-ax}\,\mathrm{d}x$.

*Worked example.* $\displaystyle\int_0^\infty x\,e^{-2x}\mathrm{d}x$: take $u=x$, $v'=e^{-2x}$, so $v=-\tfrac12e^{-2x}$. Then $=\big[-\tfrac x2e^{-2x}\big]_0^\infty+\tfrac12\int_0^\infty e^{-2x}\mathrm{d}x=0+\tfrac12\cdot\tfrac12=\tfrac14$.

### Move 4.4 — Integral cheat sheet, part 2: Gaussians and odd integrands

A **Gaussian** is a function of the form $e^{-ax^2}$: a bell curve. For $a>0$ the module supplies (Week 5 hints):

$$\int_{-\infty}^{\infty}e^{-ax^2}\mathrm{d}x=\sqrt{\frac{\pi}{a}},\qquad \int_{-\infty}^{\infty}x^2e^{-ax^2}\mathrm{d}x=\frac{\sqrt\pi}{2a^{3/2}} .$$

*Needed when* normalising a Gaussian wave function and computing $\langle x^2\rangle$. Memorise both; deriving them is not required.

**Odd and even.** A function is *even* if $f(-x)=f(x)$ (e.g. $x^2$, $e^{-x^2}$, $\cos x$) and *odd* if $f(-x)=-f(x)$ (e.g. $x$, $x\,e^{-x^2}$, $\sin x$). Over a symmetric interval:

$$\int_{-u}^{u}f_{\text{odd}}\,\mathrm{d}x=0,\qquad \int_{-u}^{u}f_{\text{even}}\,\mathrm{d}x=2\int_0^u f_{\text{even}}\,\mathrm{d}x .$$

Parity rules: even $\times$ even = even, odd $\times$ odd = even, even $\times$ odd = odd. *Needed when* an integral looks hard but is odd (so it is 0), for example $\langle x\rangle$ for a symmetric $|\psi|^2$.

**Matching the formula.** Write the exponent as $-a x^2$ and read off $a$. For $|\psi|^2=C^2e^{-x^2}$, $a=1$. For $|\psi|^2=C^2e^{-4x^2}$, $a=4$. Squaring $\psi$ doubles the exponent: this is the most common slip.

### Move 4.5 — Normalisation: find $C$ so that $\int|\psi|^2\mathrm{d}x=1$

Postulate 1 says the particle is somewhere, so total probability is 1. The recipe:

1. Form $|\psi|^2=\psi^*\psi$ (real functions: just square; complex: multiply by the conjugate).
2. Integrate over all space, or over the region where $\psi\neq0$. The answer contains $C^2$.
3. Set it equal to 1 and solve $C^2=\dots$, then take the positive root (any global phase, Move 1.3, is a free choice).
4. If the integral is infinite, no $C$ works: $\psi$ is **not normalisable**, and it is not a legal wave function.

The number $C$ is the **normalisation constant**.

*Worked example.* $\psi=Ce^{-x}$ for $x\ge0$, 0 otherwise. $\int|\psi|^2=C^2\int_0^\infty e^{-2x}\mathrm{d}x=C^2/2=1$, so $C=\sqrt2$.

### Move 4.6 — Expectation value, probability in an interval, variance

Say it as: "the average of $x$, weighted by the probability density".

- **Probability in an interval:** $P(a\le x\le b)=\displaystyle\int_a^b|\psi|^2\mathrm{d}x$. The **probability density** $|\psi|^2$ is probability per unit length; you must integrate it to get a probability.
- **Expectation value:** $\langle x\rangle=\langle\psi|\hat x\psi\rangle=\displaystyle\int\psi^*\,x\,\psi\,\mathrm{d}x=\int x\,|\psi|^2\mathrm{d}x$. The x sits *between* $\psi^*$ and $\psi$; for $x$ the order does not matter, but it will for $\hat p$. Similarly $\langle x^2\rangle=\int x^2|\psi|^2\mathrm{d}x$. This is the Day 5 recipe $\sum|c_n|^2a_n$ with the sum turned into an integral.
- **Variance:** $\sigma_x^2=\langle x^2\rangle-\langle x\rangle^2$; the **standard deviation** is $\sigma_x=\sqrt{\sigma_x^2}$, the typical spread around the average. (The lecture's Week 5 uses $\Delta x\equiv\sigma_x$.)

These formulas assume $\psi$ is already normalised. If not, normalise first.

### Move 4.7 — Acceptable wave function checklist

From the Week 2 lecture (Postulate 1): a physically acceptable $\psi$ must, along with its first derivative, be *finite*, *continuous* and *single-valued* everywhere. Add normalisability. Run these tests in order:

1. **Finite:** no point where $\psi\to\pm\infty$ (e.g. $1/x$ at 0).
2. **Single-valued:** one value of $\psi$ at each $x$ (a function, not a curve that doubles back).
3. **Continuous:** no jumps. A step function fails.
4. **Continuous derivative:** no kinks (sharp corners), with the usual caveat that this requirement is tied to finite potentials. Follow the lecture's statement when a problem asks about acceptability.
5. **Normalisable:** $\int|\psi|^2\mathrm{d}x$ is finite. Anything that does not decay at infinity (plain $e^{x}$, $\sin x$ on all of $\mathbb R$) fails here.

Justify a "no" by naming the first test it fails and the reason in one line.

### Move 4.8 — Derivative operator, $\hat p=\frac\hbar i\frac{\mathrm d}{\mathrm dx}$, and $e^{ikx}$ as a momentum eigenfunction

An **operator** acts on a function and returns a function. The **momentum operator** in one dimension is

$$\hat p\,\psi(x)=\frac{\hbar}{i}\frac{\mathrm d\psi}{\mathrm dx}=-i\hbar\frac{\mathrm d\psi}{\mathrm dx}$$

(the lecture writes $\hat p_x=-i\hbar\,\partial/\partial x$; the two forms are equal because $1/i=-i$). Read it as "differentiate, then multiply by $-i\hbar$".

An **eigenfunction** of $\hat p$ satisfies $\hat p\psi=p\,\psi$: differentiating gives back the *same* function times a constant. Apply it to $e^{ikx}$:

$$\hat p\,e^{ikx}=-i\hbar\,(ik)\,e^{ikx}=\hbar k\,e^{ikx},$$

so $e^{ikx}$ is an eigenfunction with eigenvalue $\hbar k$. This is the **plane wave** of the lecture, and $p=\hbar k$ is the de Broglie relation. The function $\sin kx$ is not an eigenfunction: differentiating turns it into $\cos kx$, which is not a multiple of $\sin kx$.

## Core concepts

- **Wave function $\psi(x)$:** the function that specifies the state (Postulate 1). Say "psi of x". It can be complex.
- **$|\psi|^2=\psi^*\psi$:** always real and $\ge0$; it is the probability density. Forgetting the star is the classic slip.
- **Normalised vs normalisable:** *normalisable* means the total is finite (some $C$ works); *normalised* means it is already 1.
- **Position operator:** $\hat x$ just multiplies by $x$. **Momentum operator:** differentiates. Operators do not commute, which Day 6 exploits.
- **The bridge:** matrix language (Day 2) and calculus language (today) are one theory. Sum over $n$ becomes integral over $x$; a column vector becomes a function; a matrix becomes a differential operator.

## Exercises

Cold attempt first, for at least 10 minutes each; open the hint only after a real try; check against the solution sketch last.

1. Normalise $\psi(x)=C\,x\,e^{-x^2}$ on the whole line (find $C>0$). — **Hint:** $|\psi|^2=C^2x^2e^{-2x^2}$: squaring doubles the exponent, so $a=2$ in the formula for $\int x^2e^{-ax^2}\mathrm dx$ (Move 4.4). — **Solution sketch:** $\int|\psi|^2\mathrm dx=C^2\int x^2e^{-2x^2}\mathrm dx=C^2\cdot\dfrac{\sqrt\pi}{2\cdot2^{3/2}}=C^2\dfrac{\sqrt\pi}{4\sqrt2}$. Set to 1: $C^2=\dfrac{4\sqrt2}{\sqrt\pi}$, so $C=\big(4\sqrt2/\sqrt\pi\big)^{1/2}\approx1.79$ (check: $4\sqrt2/\sqrt\pi\approx3.19$).
2. Normalise $\psi(x)=C\,e^{-x^2}$ on $(-\infty,\infty)$. — **Hint:** square first: the exponent becomes $-2x^2$, so $a=2$ in $\sqrt{\pi/a}$. — **Solution sketch:** $C^2\int e^{-2x^2}\mathrm dx=C^2\sqrt{\pi/2}=1$, so $C^2=\sqrt{2/\pi}$ and $C=(2/\pi)^{1/4}$.
3. For each function decide whether it is an acceptable wave function on the whole real line, and name the first checklist test it fails: (a) $x\,e^{-x^2}$; (b) $1/x$; (c) $e^{x}$; (d) $\psi=1$ for $|x|<1$ and $0$ otherwise; (e) $\sin x$. — **Hint:** run Move 4.7 in order: finite, continuous, then normalisable. For (a) check what happens as $|x|\to\infty$ and integrate $x^2e^{-2x^2}$ with the Gaussian formula. — **Solution sketch:** (a) acceptable: finite, smooth, decays fast, $\int x^2e^{-2x^2}\mathrm dx=\sqrt\pi/(2\cdot2^{3/2})$ is finite. (b) fails "finite" at $x=0$ (and $\int1/x^2$ diverges). (c) finite and smooth but fails normalisable ($|\psi|^2=e^{2x}$ blows up as $x\to\infty$). (d) fails "continuous" (jumps at $x=\pm1$). (e) fails normalisable ($\sin^2x$ does not decay, so the integral is infinite).
4. A particle has $\psi(x)=C\,x^2$ for $0\le x\le L$ and $0$ elsewhere. Find $C$, then $\langle x\rangle$, $\langle x^2\rangle$ and $\sigma_x$. — **Hint:** $\int_0^Lx^4\mathrm dx=L^5/5$; then $\langle x\rangle=C^2\int_0^Lx^5\mathrm dx$ and $\langle x^2\rangle=C^2\int_0^Lx^6\mathrm dx$. — **Solution sketch:** $C^2L^5/5=1$, so $C^2=5/L^5$, $C=\sqrt5/L^{5/2}$. $\langle x\rangle=\tfrac{5}{L^5}\cdot\tfrac{L^6}{6}=\tfrac{5L}{6}$; $\langle x^2\rangle=\tfrac5{L^5}\cdot\tfrac{L^7}{7}=\tfrac{5L^2}{7}$; $\sigma_x^2=\tfrac{5L^2}7-\tfrac{25L^2}{36}=\tfrac{180-175}{252}L^2=\tfrac{5L^2}{252}$, so $\sigma_x=L\sqrt{5/252}\approx0.14\,L$.
5. A particle in a box of width $L$ has $\psi(x)=\sqrt{2/L}\,\sin(\pi x/L)$ for $0\le x\le L$. What is the probability of finding it in $0\le x\le L/4$? — **Hint:** integrate $|\psi|^2=(2/L)\sin^2(\pi x/L)$ using $\sin^2\theta=\tfrac12(1-\cos2\theta)$ (Moves 1.4 and 4.2). — **Solution sketch:** $P=\tfrac2L\big[\tfrac x2-\tfrac{L}{4\pi}\sin\tfrac{2\pi x}{L}\big]_0^{L/4}=\tfrac2L\big(\tfrac L8-\tfrac L{4\pi}\big)=\tfrac14-\tfrac1{2\pi}\approx0.091$. Sanity check: less than the uniform-density value $1/4$, because the density is small near the wall.
6. Apply $\hat p=\frac\hbar i\frac{\mathrm d}{\mathrm dx}$ to (a) $e^{ikx}$ and (b) $\sin(kx)$ (with $k$ real). Which is an eigenfunction, and with what eigenvalue? — **Hint:** differentiate, multiply by $\hbar/i=-i\hbar$, then ask whether the result is a constant times the original function. — **Solution sketch:** (a) $\hat pe^{ikx}=\hbar k\,e^{ikx}$: eigenfunction, eigenvalue $\hbar k$. (b) $\hat p\sin kx=-i\hbar k\cos kx$, not a multiple of $\sin kx$: not an eigenfunction. (Writing $\sin kx=(e^{ikx}-e^{-ikx})/2i$ shows it is a mix of eigenvalues $+\hbar k$ and $-\hbar k$.)
7. Let $\phi(x)=e^{-x^2}$ and $\psi(x)=x\,e^{-x^2}$ (both real). Use integration by parts to show that $\displaystyle\int_{-\infty}^{\infty}\phi\,\frac{\mathrm d\psi}{\mathrm dx}\,\mathrm dx=-\int_{-\infty}^{\infty}\frac{\mathrm d\phi}{\mathrm dx}\,\psi\,\mathrm dx$, evaluate both sides, and say why the boundary term is zero. — **Hint:** take $u=\phi$ and $v'=\psi'$ (Move 4.3); the boundary term is $[\phi\psi]_{-\infty}^{\infty}$. To evaluate, use $\psi'=(1-2x^2)e^{-x^2}$, $\phi'=-2x\,e^{-x^2}$ and the Gaussian formulas of Move 4.4 with $a=2$. — **Solution sketch:** boundary term: $[x\,e^{-2x^2}]_{-\infty}^{\infty}=0$, because the function dies away at both ends. Left side: $\int(1-2x^2)e^{-2x^2}\mathrm dx=\sqrt{\pi/2}-2\cdot\tfrac{\sqrt\pi}{4\sqrt2}=\tfrac{\sqrt\pi}{\sqrt2}-\tfrac{\sqrt\pi}{2\sqrt2}=\tfrac{\sqrt\pi}{2\sqrt2}\approx0.63$. Right side: $-\int(-2x\,e^{-x^2})(x\,e^{-x^2})\mathrm dx=2\int x^2e^{-2x^2}\mathrm dx=2\cdot\tfrac{\sqrt\pi}{4\sqrt2}=\tfrac{\sqrt\pi}{2\sqrt2}$. The two sides agree. General rule (all you need): the boundary term vanishes for normalisable functions that die away at infinity.
8. Let $\psi(x)=C$ for $0<x<1$, $\psi(x)=2C$ for $1<x<2$, and $\psi=0$ elsewhere. Find $C$, sketch $|\psi|^2$, and find the probability of finding the particle in $1<x<2$. — **Hint:** the density is two flat plateaus; each integral is height times width. Label the plateau heights on the sketch. — **Solution sketch:** $|\psi|^2=C^2$ on $(0,1)$ and $4C^2$ on $(1,2)$. Total $=C^2+4C^2=5C^2=1$, so $C=1/\sqrt5$. Densities $1/5$ and $4/5$. $P(1<x<2)=4/5$. (This $\psi$ is not continuous, so it is a density-sketching exercise only.)
9. Show without integrating that $\int_{-\infty}^{\infty}x\,e^{-x^2}\mathrm dx=0$, and explain why $\langle x\rangle=0$ for any $\psi$ with $|\psi|^2$ even. — **Hint:** decide whether the integrand is odd or even (Move 4.4), then use the symmetric-interval rule. — **Solution sketch:** $f(x)=x\,e^{-x^2}$ has $f(-x)=-x\,e^{-x^2}=-f(x)$: odd, so the integral over $(-\infty,\infty)$ is 0. For $\langle x\rangle=\int x|\psi|^2\mathrm dx$ with $|\psi|^2$ even, the integrand is odd$\times$even = odd, so $\langle x\rangle=0$.
10. For $\psi(x)=C\,e^{-2x^2}$ on the whole line, find $C$, $\langle x\rangle$, $\langle x^2\rangle$ and $\sigma_x$. — **Hint:** $|\psi|^2=C^2e^{-4x^2}$, so $a=4$. Use both Gaussian formulas from Move 4.4; $\langle x\rangle$ is zero by parity. — **Solution sketch:** $C^2\sqrt{\pi/4}=1\Rightarrow C^2=2/\sqrt\pi$. $\langle x\rangle=0$. $\langle x^2\rangle=C^2\frac{\sqrt\pi}{2\cdot4^{3/2}}=\frac2{\sqrt\pi}\cdot\frac{\sqrt\pi}{16}=\frac18$. $\sigma_x=\sqrt{1/8}=1/(2\sqrt2)\approx0.35$.
11. Normalise the complex function $\psi(x)=C\,e^{ikx}$ on $0\le x\le L$ ($k$ real) and explain what goes wrong if you integrate $\psi$ instead of $|\psi|^2$. — **Hint:** $|\psi|^2=\psi^*\psi=C^2e^{-ikx}e^{ikx}$; use $|e^{i\theta}|=1$ (Move 1.3). — **Solution sketch:** $|\psi|^2=C^2$, so $C^2L=1$ and $C=1/\sqrt L$. Integrating $\psi$ itself gives $C(e^{ikL}-1)/(ik)$, a complex number, which cannot be a probability. Probability always comes from $\psi^*\psi$.
12. On $[-1,1]$ let $\phi(x)=x$ and $\psi(x)=x^3$. Compute $\langle\phi|\psi\rangle$, $\langle\psi|\phi\rangle$ and $\langle\phi|\phi\rangle$; then repeat $\langle\phi|\psi\rangle$ on $[0,1]$ and say whether the functions are orthogonal on each interval. — **Hint:** the functions are real, so the conjugation does nothing; the integrand is $x\cdot x^3=x^4$. Ask whether it is odd or even. — **Solution sketch:** on $[-1,1]$: $\langle\phi|\psi\rangle=\int x^4\mathrm dx=2/5=\langle\psi|\phi\rangle$ (real, so equal to its conjugate), and $\langle\phi|\phi\rangle=\int x^2\mathrm dx=2/3$. On $[0,1]$: $\int_0^1x^4\mathrm dx=1/5$. Neither is zero, so the functions are not orthogonal on either interval. Orthogonality depends on the interval, exactly as it depends on the basis in Day 2.

## Apply to the lecture

- **Week 2 companion, section on Postulate 2 (and the Postulate 1 acceptability list):** read it now with Moves 4.5 to 4.8 open. Look for where the lecture writes $\int\psi^*\psi\,\mathrm{d}^3\mathbf r=1$ and check that you can replace $\mathrm{d}^3\mathbf r$ with $\mathrm dx$ for one dimension. Find where the lecture says "finite, continuous and single-valued" and match each word to a test in Move 4.7.
- **Week 2 lecture, Postulate 2:** find $\hat p_x=-i\hbar\,\partial/\partial x$ and the plane-wave states with eigenvalue $\hbar\mathbf k$, and check they match Move 4.8.
- **Week 3 companion:** look for the probability-density language ("the probability that the result lies in a region") and match it to Move 4.6. Note where the lecture uses $|\langle\phi_n|\psi\rangle|^2$ for discrete outcomes, which is the discrete cousin of $\int|\psi|^2\mathrm dx$.
- **Week 5 (preview):** the oscillator ground state is a Gaussian, and its hint list contains exactly the two Gaussian integrals and the odd-function rule from Move 4.4. You have them today; Day 6 adds the substitution that makes them easy.
- **What to look for:** every time a lecture writes an integral over $\psi^*\dots\psi$, ask "what is the operator in the middle?" (identity for normalisation, $\hat x$ for $\langle x\rangle$, $\hat p$ for $\langle p\rangle$).

## Anti-patterns / Common mistakes

- **Integrating $\psi$ instead of $|\psi|^2=\psi^*\psi$.** The normalisation condition uses the density. Symptom: complex or negative "probabilities".
- **Dropping limits or the piece structure.** Integrate from $-\infty$ to $\infty$ or only where $\psi\ne0$, and write the limits down every time. A piecewise $\psi$ needs a piecewise integral.
- **Forgetting the factor of 2** for an even integrand over $(-\infty,\infty)$: $\int_{-\infty}^\infty e^{-a|x|}\mathrm dx=2/a$, not $1/a$.
- **Reading $a$ off $\psi$ instead of $|\psi|^2$** in a Gaussian formula. Squaring doubles the exponent.
- **Skipping a sanity check.** Probabilities lie in $[0,1]$; $\sigma_x^2\ge0$; a normalisation constant should have the right units (here, inverse square root of length).

## Confusion log

| Symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |

Tomorrow (Day 5): measurement and the Schrödinger equation. Before sleeping, re-do exercise 4 or 10 from a blank page.

## Warm-up answers

1. Characteristic polynomial $(4-\lambda)(1-\lambda)-4=\lambda^2-5\lambda=0$, so $\lambda=0$ or $5$. For $\lambda=5$: $(2,1)^T/\sqrt5$. For $\lambda=0$: $(1,-2)^T/\sqrt5$.
2. $(AB)^\dagger=B^\dagger A^\dagger$ (order reverses, conjugate transpose each). Hermitian means $A^\dagger=A$: the conjugate transpose equals the matrix itself.
3. $\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$; eigenvalue $+1$ with $(1,0)^T$ (spin up), eigenvalue $-1$ with $(0,1)^T$ (spin down).
4. $\sigma_x\sigma_z=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\sigma_z\sigma_x=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, so $[\sigma_x,\sigma_z]=\begin{pmatrix}0&-2\\2&0\end{pmatrix}$ ($=-2i\sigma_y$).
5. Its conjugate transpose is the same matrix, so yes it is Hermitian. Hermitian matrices have real eigenvalues (here $0$ and $2$), because $\langle\psi|A\psi\rangle$ equals its own conjugate.
