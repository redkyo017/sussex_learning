# Day 1 — Complex numbers and trig triage

> **Physics pair for today:** [P1 — Energy and Classical State](physics/P1.md) (~1.5 h).

**Time box (~3.5 h):** 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Why this matters

Every quantum state in Module 3 is built from complex numbers. The lecture writes the probability of a superposition as a modulus squared (Week 2, Eq. 2.4) and says the inner product takes "the complex conjugation of the first vector" (Week 2, §2.1, "The inner product"). If $z^*$ and $|z|^2$ are not automatic for you, every later step reads as noise. Trig rides along: the two-component states you will meet in Week 3 are written with sines and cosines, and the double-angle identities turn awkward products into single terms.

Today teaches four moves: algebra triage (1.1), complex numbers (1.2), Euler's formula (1.3) and trig identities (1.4). Nothing here is quantum yet; it is the grammar the quantum sentences are written in.

## Warm-up (diagnostic, closed book, 20 min)

Day 1 has no earlier days to recall, so this is a diagnostic of five school-level questions. Answer them without a calculator, then open the fold at the bottom of the file. Whatever you miss tells you what to slow down on in Move 1.1.

1. Compute $\dfrac{1}{2} + \dfrac{1}{3}$ and $\dfrac{2}{3} \times \dfrac{9}{4}$.
2. Simplify $2^3 \cdot 2^{-5}$ and $(x^2)^3 / x^4$.
3. Solve $x^2 - 5x + 6 = 0$.
4. Write down $\sin$ and $\cos$ of $30^\circ$, $45^\circ$ and $60^\circ$.
5. Expand $(a+b)^2$.

## Moves

### Move 1.1 — Algebra triage: rearrange, exponent rules, square roots, fractions

**Statement.** Four habits cover almost all the algebra in Weeks 2–7.

- *Rearrange:* whatever you do to one side of an equation you do to the other. To isolate $x$ in $3x + 2 = 11$, subtract 2, then divide by 3.
- *Exponents:* $a^m a^n = a^{m+n}$, $\;(a^m)^n = a^{mn}$, $\;a^{-n} = 1/a^n$, $\;a^0 = 1$. Say it aloud: "multiplying same-base powers adds the exponents".
- *Square roots:* $\sqrt{ab} = \sqrt{a}\sqrt{b}$, and $\sqrt{a^2} = |a|$ (the positive root). Note $\sqrt{a+b} \neq \sqrt{a} + \sqrt{b}$.
- *Fractions:* add over a common denominator; divide by a fraction by multiplying by its flip. Also $(a+b)^2 = a^2 + 2ab + b^2$ (the cross term is the one people drop).

**Why it works.** These are just the definitions of multiplication and powers applied consistently. An exponent counts repeated multiplication, so adding exponents counts the combined repeats.

**Worked example.** Simplify $\dfrac{4x^3}{2x^{-1}} \cdot \dfrac{1}{\sqrt{x^2}}$ for $x > 0$. Numbers: $4/2 = 2$. Powers of $x$: $x^3 / x^{-1} = x^{3-(-1)} = x^4$. Root: $\sqrt{x^2} = x$, so dividing gives $x^{-1}$. Total: $2 x^{4-1} = 2x^3$.

### Move 1.2 — Complex numbers: $i$, $a+ib$, conjugate $z^*$, modulus, $|z|^2 = z^*z$

**Statement.** The imaginary unit $i$ is defined by $i^2 = -1$. A *complex number* is $z = a + ib$ with $a, b$ real. Say it as "a plus i b". The number $a$ is the *real part* and $b$ is the *imaginary part* (note: $b$ itself, without the $i$).

The *complex conjugate* $z^*$ (say "z star") flips the sign of $i$ everywhere: $z^* = a - ib$. The *modulus* $|z|$ (say "mod z") is the distance of $z$ from zero on the plane whose axes are the real and imaginary parts:

$$|z| = \sqrt{a^2 + b^2}, \qquad |z|^2 = z^* z = a^2 + b^2.$$

**Why it works.** Draw $z$ as the point $(a, b)$. Pythagoras gives the distance $\sqrt{a^2 + b^2}$. Multiplying out, $(a - ib)(a + ib) = a^2 + iab - iab - i^2 b^2 = a^2 + b^2$: the two middle terms cancel and $-i^2 = +1$. So $z^* z$ is always a real number that is at least zero. This is exactly why probabilities, built as $\psi^*\psi$, can be real and non-negative even though $\psi$ is complex.

**Worked example.** Let $z = 2 - 5i$. Real part 2, imaginary part $-5$. Conjugate $z^* = 2 + 5i$. Modulus squared: $z^* z = (2+5i)(2-5i) = 4 + 25 = 29$, so $|z| = \sqrt{29}$. Check with Pythagoras: $2^2 + (-5)^2 = 29$.

Two more rules you will use constantly: $(zw)^* = z^* w^*$ and $(z^*)^* = z$.

### Move 1.3 — Euler: $e^{i\theta} = \cos\theta + i\sin\theta$, $|e^{i\theta}| = 1$, global phase

**Statement.** *Euler's formula* says

$$e^{i\theta} = \cos\theta + i\sin\theta \qquad (\theta \text{ in radians}).$$

Say it as "e to the i theta equals cosine theta plus i sine theta". It is a point on the *unit circle* (the circle of radius 1 around zero in the complex plane), reached by turning through angle $\theta$ from the positive real axis. The angle $\theta$ is called the *phase*.

**Why it works (intuition).** The point $(\cos\theta, \sin\theta)$ lies on the unit circle by definition of sine and cosine. Euler's formula says the complex exponential is that same point, with the real part as the horizontal coordinate and the imaginary part as the vertical one. It also obeys the exponent rule, $e^{i\alpha}e^{i\beta} = e^{i(\alpha+\beta)}$: multiplying by $e^{i\beta}$ rotates by $\beta$.

**Modulus is 1.** $|e^{i\theta}|^2 = (e^{i\theta})^* e^{i\theta} = e^{-i\theta}e^{i\theta} = e^0 = 1$. The conjugate of $e^{i\theta}$ is $e^{-i\theta}$ because conjugating flips the sign of $i$.

**Global phase.** Multiplying a whole state by $e^{i\gamma}$ multiplies its probabilities by $|e^{i\gamma}|^2 = 1$, so nothing measurable changes. A common phase factor on the whole state is called a *global phase*. (A relative phase between two terms inside a superposition is different, and does matter.)

**Worked example.** Take $\theta = \pi/3$: $e^{i\pi/3} = \cos 60^\circ + i\sin 60^\circ = \tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}$. Modulus squared: $\tfrac14 + \tfrac34 = 1$. Now take the number $c = 0.6\,e^{i\pi/3}$: $|c|^2 = 0.36 \cdot 1 = 0.36$, the same as for $c = 0.6$, so the phase drops out of the probability.

### Move 1.4 — Trig identities: $\sin^2+\cos^2 = 1$, double-angle, half-angle

**Statement.** Keep four identities:

- $\sin^2\theta + \cos^2\theta = 1$
- $\sin 2\theta = 2\sin\theta\cos\theta$
- $\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$
- Half-angle forms (rearrange the last line): $\cos^2\theta = \dfrac{1+\cos 2\theta}{2}$, $\quad \sin^2\theta = \dfrac{1-\cos 2\theta}{2}$.

The three-line form of $\cos 2\theta$ is called the *double-angle identity*.

**Why it works.** The first is Pythagoras on the unit circle. The others come from taking $e^{i\cdot 2\theta} = (e^{i\theta})^2$ and expanding both sides: $\cos 2\theta + i\sin 2\theta = (\cos\theta + i\sin\theta)^2 = \cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta$. Match real parts and imaginary parts. Half-angle forms are the reason $\int \sin^2$ is easy later (Day 4).

**Worked example.** Rewrite $4\sin\theta\cos\theta\,\cos 2\theta$ as one term. Use $2\sin\theta\cos\theta = \sin 2\theta$, so the expression is $2\sin 2\theta\cos 2\theta = \sin 4\theta$ (apply the same identity again with $2\theta$ in place of $\theta$).

## Core concepts

- **Complex numbers as points.** $a + ib$ is a point $(a,b)$. Conjugating reflects it across the real axis. The modulus is its distance from the origin.
- **$z^*z$ is the "size squared".** It is the only complex-number combination Module 3 uses to make probabilities. It is never $z^2$.
- **Phase is an angle.** $e^{i\theta}$ carries no size, only direction. A state's size is fixed by its modulus.
- **Notation decoded.** $z^*$ or $\bar z$: "z star", flip $i$ to $-i$. $|z|$: "mod z", length. $\mathrm{Re}\,z$, $\mathrm{Im}\,z$: the real and imaginary parts, both real numbers. The Week 2 lecture writes $\psi^*$ for the conjugate of $\psi$.

## Exercises

Attempt each one cold for a fixed time before reading the hint. Only then open the solution sketch.

1. Let $z = 3 - 4i$. Write down $\mathrm{Re}\,z$, $\mathrm{Im}\,z$, $z^*$ and $|z|$. — **Hint:** flip the sign on the $i$ term for $z^*$; use $|z|^2 = a^2 + b^2$ for the modulus. — **Solution sketch:** $\mathrm{Re}\,z = 3$, $\mathrm{Im}\,z = -4$, $z^* = 3 + 4i$, $|z|^2 = 9 + 16 = 25$, so $|z| = 5$.
2. For a general $z = a + ib$ (with $a, b$ real), show that $|z|^2 = z^* z$ is real and never negative. — **Hint:** multiply out $(a - ib)(a + ib)$ and watch which terms cancel. — **Solution sketch:** $z^* z = a^2 + iab - iab - i^2 b^2 = a^2 + b^2$. Squares of real numbers are $\ge 0$, so the sum is real and $\ge 0$; it is zero only when $a = b = 0$.
3. Compute $(a + ib)(a - ib)$ and then evaluate it for $a = 2$, $b = 3$. — **Hint:** this is the difference-of-squares pattern with $i^2 = -1$. — **Solution sketch:** $(a+ib)(a-ib) = a^2 - i^2 b^2 = a^2 + b^2$. For $a = 2, b = 3$ it equals $4 + 9 = 13$.
4. Evaluate $e^{i\theta}$ at $\theta = 0$, $\pi/2$ and $\pi$, and plot each as a point on the complex plane. — **Hint:** use $e^{i\theta} = \cos\theta + i\sin\theta$ and the values of sine and cosine at those angles. — **Solution sketch:** $\theta = 0$: $1 + 0i = 1$. $\theta = \pi/2$: $0 + i = i$. $\theta = \pi$: $-1 + 0i = -1$. All three sit on the unit circle: right, top, left.
5. Show that $|e^{i\theta}| = 1$ for every real $\theta$. Then let $c$ be any complex number and show $|e^{i\gamma}c|^2 = |c|^2$. Say in one sentence why a global phase changes nothing measurable. — **Hint:** write $|w|^2 = w^* w$ and use $(e^{i\theta})^* = e^{-i\theta}$. — **Solution sketch:** $|e^{i\theta}|^2 = e^{-i\theta}e^{i\theta} = 1$. Then $|e^{i\gamma}c|^2 = e^{-i\gamma}c^* e^{i\gamma}c = |c|^2$. Probabilities are built from $|\cdot|^2$, and the phase factor multiplies each by 1.
6. Rewrite $6\sin x\cos x$ as a single sine, and rewrite $\sin\theta\cos\theta\cos 2\theta$ as $\tfrac14\sin 4\theta$. — **Hint:** $2\sin A\cos A = \sin 2A$; apply it once, then again. — **Solution sketch:** $6\sin x\cos x = 3\cdot 2\sin x\cos x = 3\sin 2x$. For the second: $\sin\theta\cos\theta = \tfrac12\sin 2\theta$, so the product is $\tfrac12\sin 2\theta\cos 2\theta = \tfrac14\cdot 2\sin 2\theta\cos 2\theta = \tfrac14\sin 4\theta$.
7. Simplify $\cos^2\theta - \sin^2\theta$. Then use it to evaluate $\cos^2(\pi/8) - \sin^2(\pi/8)$ exactly, and write $\cos^2(\pi/8)$ using the half-angle form. — **Hint:** the first expression is one of the forms of $\cos 2\theta$; for the last part use $\cos^2\theta = (1+\cos 2\theta)/2$ with $\theta = \pi/8$. — **Solution sketch:** $\cos^2\theta - \sin^2\theta = \cos 2\theta$. At $\theta = \pi/8$ this is $\cos(\pi/4) = 1/\sqrt{2}$. Half-angle: $\cos^2(\pi/8) = \tfrac12\bigl(1 + \tfrac{1}{\sqrt2}\bigr)$.
8. Find the modulus of $(1+i)/\sqrt{2}$. — **Hint:** the modulus of a quotient by a positive real number is the modulus of the top divided by that number; or compute $z^*z$ directly. — **Solution sketch:** $|1+i|^2 = 1 + 1 = 2$, so $|1+i| = \sqrt 2$, and $|(1+i)/\sqrt2| = \sqrt2/\sqrt2 = 1$. It is a point on the unit circle (it equals $e^{i\pi/4}$).
9. Write $-i$ in the form $e^{i\varphi}$ and give a valid $\varphi$. — **Hint:** locate $-i$ on the complex plane (straight down from the origin) and ask which angle from the positive real axis reaches it. — **Solution sketch:** $-i = \cos\varphi + i\sin\varphi$ needs $\cos\varphi = 0$, $\sin\varphi = -1$, so $\varphi = -\pi/2$ (equivalently $3\pi/2$, since adding $2\pi$ changes nothing).
10. (a) Check that the two-component list $(\cos\theta,\ \sin\theta)$ has unit length, i.e. $\cos^2\theta + \sin^2\theta = 1$. (b) Now compute $|c|^2$ for $c = i\sin\theta$ and compare it with $c^2$; then find $|\cos\theta|^2 + |i\sin\theta|^2$. — **Hint:** for (a) apply Move 1.4 directly; for (b) remember $|c|^2 = c^*c$, not $c^2$. — **Solution sketch:** (a) $\cos^2\theta + \sin^2\theta = 1$, so it has unit length: a point on the unit circle. (b) $c^* = -i\sin\theta$, so $|c|^2 = (-i\sin\theta)(i\sin\theta) = \sin^2\theta$, whereas $c^2 = i^2\sin^2\theta = -\sin^2\theta$. Hence $|\cos\theta|^2 + |i\sin\theta|^2 = \cos^2\theta + \sin^2\theta = 1$ too: a factor of $i$ does not change the size.

## Apply to the lecture

In Week 2, §2.1 ("Postulate 1: The state of a system"), read the paragraph after Eq. (2.3) and Eq. (2.4). The coefficients $\alpha_i$ are complex, and the probability is a modulus squared. Ask yourself: why must the probability be real? Because $|z|^2 = z^*z \ge 0$ (Exercise 2). Then read the inner-product paragraph in the same section: the lecture takes "the complex conjugation of the first vector", which is exactly Move 1.2 applied to each component, and that is why the inner product of a vector with itself is non-negative.

In Week 3, the probabilities of outcomes are the moduli squared $|\langle\phi_n|\psi\rangle|^2$ (Eqs. 3.2 and 3.4); a global phase on $|\psi\rangle$ cannot change them (Exercise 5). The eigenvectors you will compute in Week 3 involve trigonometric entries, which is where Move 1.4 helps. Read the Week 2 and Week 3 notation decoders in the companions after finishing today (do not open them before you have attempted the exercises).

## Anti-patterns / Common mistakes

- **Forgetting the conjugate flips the sign of $i$ everywhere.** $(2 + 5i)^* = 2 - 5i$, and $(e^{i\theta})^* = e^{-i\theta}$. Conjugate every $i$ in the expression, not just the first one you see.
- **Treating $|z|^2$ as $z^2$.** $z^2$ can be negative or complex; $|z|^2 = z^*z$ is real and non-negative (Exercise 10b).
- **Mixing degrees and radians.** Euler's formula needs radians. $e^{i\pi} = -1$, whereas $e^{i\,180}$ is not.
- **Dropping the cross term.** $(a+b)^2 \neq a^2 + b^2$; the missing piece is $2ab$.

## Confusion log

| Symbol | Step | Concept |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Tomorrow (Day 2): column vectors and the ket/bra notation. Bring today's Move 1.2, since the bra is "conjugate, then transpose".

<details>
<summary>Warm-up answers (open after attempting)</summary>

1. $\tfrac{1}{2}+\tfrac{1}{3} = \tfrac56$; $\tfrac23\times\tfrac94 = \tfrac{18}{12} = \tfrac32$.
2. $2^3\cdot 2^{-5} = 2^{-2} = \tfrac14$; $(x^2)^3/x^4 = x^6/x^4 = x^2$.
3. Factor: $(x-2)(x-3) = 0$, so $x = 2$ or $x = 3$.
4. $\sin 30^\circ = \tfrac12$, $\cos 30^\circ = \tfrac{\sqrt3}{2}$; $\sin 45^\circ = \cos 45^\circ = \tfrac{1}{\sqrt2}$; $\sin 60^\circ = \tfrac{\sqrt3}{2}$, $\cos 60^\circ = \tfrac12$.
5. $(a+b)^2 = a^2 + 2ab + b^2$.

</details>
