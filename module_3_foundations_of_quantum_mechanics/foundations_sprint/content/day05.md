# Day 5 — Measurement, the Schrödinger equation and stationary states

**Time box (~3.5 h):** 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Why this matters

Week 4 is where the whole sprint pays off. Every Week 4 lecture step is one of three things: (1) turn a state into probabilities (expand, square the coefficients), (2) split the Schrödinger equation into a time part and a space part, or (3) solve a one-line differential equation with boundary conditions in a box. Assessment 1 (due Thursday of Week 4, 17:00 UK) leans hard on the first, and on Days 1–5 overall. Today gives you the technique for each of the three, on states and operators that are deliberately *not* the course's own. The course problems are yours to solve.

Moves used today from earlier days: 2.4 (expansion in an orthonormal basis), 3.2 (eigenvalue equation), 3.3 (Hermitian, real eigenvalues, orthogonal eigenvectors), 4.5 (normalisation), 4.8 (derivative operator, $e^{ikx}$).

## Warm-up (retrieval, 5 questions from Day 4, closed book, 20 min)

Write each answer on paper before opening the folded answers at the bottom of this file.

1. Find $C>0$ so that $\psi(x)=C\,e^{-2x}$ for $x\ge0$, and $\psi(x)=0$ for $x<0$, is normalised. (Move 4.5, 4.2)
2. State $\int_{-\infty}^{\infty}e^{-ax^2}\,\mathrm{d}x$ for $a>0$, and say in one sentence why $\int_{-\infty}^{\infty}x\,e^{-x^2}\,\mathrm{d}x=0$. (Move 4.4)
3. What is $\hat p\,e^{ikx}$, where $\hat p=\frac{\hbar}{i}\frac{\mathrm{d}}{\mathrm{d}x}$? Say which number is the eigenvalue. (Move 4.8)
4. Is $\psi(x)=e^{x}$ on the whole real line an acceptable wave function? Which item of the checklist fails? (Move 4.7)
5. A particle has $\psi(x)=C\,e^{-x}$ for $x\ge 0$ and $\psi=0$ for $x<0$. Find $C>0$ and then $\langle x\rangle$. (Moves 4.5, 4.6, 4.3)

## Moves

### Move 5.1 — State expansion in an eigenbasis; probabilities $|c_n|^2$

*Plain English first.* An observable (energy, say) is an operator. Its eigenvectors form an orthonormal basis (Move 3.3). Any state can be written as a weighted sum of those eigenvectors. The weights are the amplitudes. The chance of each outcome is the **squared size** of its amplitude.

*Notation.* Let $\hat A|a_n\rangle=a_n|a_n\rangle$ with $\langle a_m|a_n\rangle=\delta_{mn}$. Then

$$|\psi\rangle=\sum_n c_n|a_n\rangle,\qquad c_n=\langle a_n|\psi\rangle,\qquad P(a_n)=|c_n|^2,\qquad \sum_n|c_n|^2=1 .$$

Say it aloud: "the amplitude $c_n$ is the inner product of the $n$th eigenvector with the state; the probability is its modulus squared."

*Why it works.* Normalisation $\langle\psi|\psi\rangle=1$ expands (using orthonormality) to $\sum|c_n|^2=1$. That is exactly the statement that the probabilities of a complete set of outcomes add to 1.

*Worked example (new state).* On a two-level system take $\hat A|a_1\rangle=-3u\,|a_1\rangle$, $\hat A|a_2\rangle=+4u\,|a_2\rangle$ (with $u$ some unit) and
$$|\psi\rangle=\frac{1}{\sqrt{34}}\big(5|a_1\rangle-3i|a_2\rangle\big).$$
Check normalisation: $\frac{1}{34}(|5|^2+|-3i|^2)=\frac{25+9}{34}=1$. Then $P(-3u)=25/34$ and $P(4u)=9/34$. The phase $-i$ on the second amplitude changes nothing here, because $|-3i|^2=9$.

### Move 5.2 — Expectation value (discrete): $\langle A\rangle=\sum_n|c_n|^2a_n$

*Plain English.* The average of many repeated measurements on identically prepared systems. Each possible eigenvalue is weighted by its probability.

$$\langle A\rangle=\langle\psi|\hat A|\psi\rangle=\sum_n|c_n|^2\,a_n .$$

*Worked example.* Same state as above: $\langle A\rangle=\frac{25}{34}(-3u)+\frac{9}{34}(4u)=\frac{-75+36}{34}u=-\frac{39}{34}u\approx-1.15u$. Note that $-1.15u$ is *not* an eigenvalue; an average need not be a possible outcome. Sanity check: it lies between $-3u$ and $4u$, as an average must.

### Move 5.3 — Collapse and repeat measurement

The **measurement postulate** in three lines. Read them as a recipe:

1. **Expand** the state in the eigenbasis of the observable you measure.
2. **Square** the coefficients: $P(a_n)=|c_n|^2$. The values you can get are the eigenvalues $a_n$, and nothing else.
3. **Collapse**: if you got $a_n$, the state is now $|a_n\rangle$ (renormalised). Measure the same observable again immediately and you get $a_n$ with probability 1.

The slogan to keep: **probabilities come from the coefficients; values come from the eigenvalues.** They live in different places and must never be swapped.

*Worked example.* In the two-level system above, suppose the measurement returned $4u$. The state is now $|a_2\rangle$ (the factor $-3i/\sqrt{34}$ is just a phase and a size, thrown away when we renormalise). A second measurement of $\hat A$ returns $4u$ with certainty. A measurement of some *other* observable $\hat B$ is a fresh Move 5.1 problem, now starting from $|a_2\rangle$.

*Two observables.* If $\hat A$ and $\hat B$ commute (Move 3.5), they can be given a common set of eigenvectors; when they share eigenvectors, after $\hat A$ has given $a_n$ the state $|a_n\rangle$ is already a $\hat B$ eigenvector, so $\hat B$ is certain. If they do not share eigenvectors, then the collapse onto an $\hat A$ eigenstate leaves $\hat B$ uncertain, and measuring $\hat B$ collapses the state *away* from $\hat A$'s eigenstate: a later $\hat A$ measurement is no longer certain.

*Degenerate outcomes (one extra rule).* If several eigenvectors share the same eigenvalue, the state after that outcome is the **projection** of $|\psi\rangle$ onto their span, then renormalised. Keep only the matching terms, then divide by the square root of the sum of their $|c|^2$.

### Move 5.4 — Time-dependent vs time-independent Schrödinger equation; separation of variables; stationary states

*Plain English.* The full equation says how the wave function changes in time. Because $V$ does not depend on $t$, we can guess a solution where the time part and the space part are multiplied together. The time part is always a pure phase.

The **Schrödinger equation** in one dimension (lecture Eq. 4.1):
$$i\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}+V(x)\Psi=\hat H\Psi .$$
Here the **Hamiltonian** $\hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)$ is the energy operator: kinetic plus potential.

*Separation of variables (lecture Eq. 4.2).* Try $\Psi(x,t)=e^{-i\omega t}\psi(x)$. Left side: $i\hbar\,\partial_t\Psi=i\hbar(-i\omega)e^{-i\omega t}\psi=\hbar\omega\,e^{-i\omega t}\psi$. Right side: $e^{-i\omega t}$ is a constant as far as $\partial_x$ is concerned, so it comes out. Cancel $e^{-i\omega t}$ from both sides and write $E=\hbar\omega$:
$$\hat H\psi(x)=E\,\psi(x).$$
This is the **time-independent Schrödinger equation**, and it is an eigenvalue equation (Move 3.2) for $\hat H$. Only special values $E_n$ (the **energy levels**) allow acceptable solutions $\psi_n$.

*Stationary states.* $\Psi_n(x,t)=\psi_n(x)\,e^{-iE_nt/\hbar}$. Because $|e^{-iE_nt/\hbar}|=1$ (Move 1.3), $|\Psi_n|^2=|\psi_n|^2$: every probability and expectation value is frozen in time.

*Time evolution of a general state.* Expand the starting state in energy eigenstates, $\Psi(x,0)=\sum_n\alpha_n\psi_n(x)$ (lecture Eq. 4.4), then attach each term's own phase (Eq. 4.5):
$$\Psi(x,t)=\sum_n\alpha_n\,\psi_n(x)\,e^{-iE_nt/\hbar}.$$
Different terms carry *different* phases, so in $|\Psi|^2$ the cross terms do not cancel. For two real terms (Eq. 4.8 and the line after):
$$|\Psi|^2=\alpha_1^2\psi_1^2+\alpha_2^2\psi_2^2+2\alpha_1\alpha_2\psi_1\psi_2\cos\!\big[(E_2-E_1)t/\hbar\big].$$
So motion needs a superposition of *different* energies. And the energy probabilities are still $|\alpha_n|^2$, with $\langle\hat H\rangle=\sum_n|\alpha_n|^2E_n$: that is Moves 5.1 and 5.2 applied to $\hat H$.

### Move 5.5 — Particle in a box: solve $\psi''=-k^2\psi$ with boundary conditions

*The set-up.* Potential well: $V=0$ for $0\le x\le L$ and $V=\infty$ outside. A finite-energy state must have $\psi=0$ where $V=\infty$. Inside, the equation is free:
$$-\frac{\hbar^2}{2m}\psi''=E\psi\iff\psi''=-k^2\psi,\qquad k^2=\frac{2mE}{\hbar^2}.$$

*Full derivation, no skipped steps.*

1. **General solution.** The lecture uses $\psi=\alpha_+e^{ikx}+\alpha_-e^{-ikx}$. Check: differentiating twice gives $(ik)^2\psi=-k^2\psi$. (Equivalent: $A\cos kx+B\sin kx$.)
2. **Boundary condition at $x=0$.** The wave function must be continuous, and it is $0$ outside, so $\psi(0)=0$. That gives $\alpha_++\alpha_-=0$, so $\alpha_-=-\alpha_+$ and
$$\psi=\alpha_+(e^{ikx}-e^{-ikx})=2i\alpha_+\sin kx .$$
Rename the constant: $\psi=C\sin kx$.
3. **Boundary condition at $x=L$.** $\psi(L)=0$ needs $\sin kL=0$, so $kL=n\pi$:
$$k_n=\frac{n\pi}{L},\qquad n=1,2,3,\dots$$
$n=0$ gives $\psi\equiv0$ (no particle). Negative $n$ gives the same function up to a sign, so nothing new.
4. **Normalise (Move 4.5).** $\int_0^L C^2\sin^2\!\frac{n\pi x}{L}\,\mathrm{d}x$. Use $\sin^2\theta=\tfrac12(1-\cos2\theta)$ (Move 1.4): the cosine part integrates to zero over whole half-waves, leaving $C^2L/2=1$, so
$$\psi_n(x)=\sqrt{\frac{2}{L}}\sin\!\Big(\frac{n\pi x}{L}\Big).$$
5. **Energies.** $E_n=\dfrac{\hbar^2k_n^2}{2m}=\dfrac{n^2\pi^2\hbar^2}{2mL^2}$ (lecture Eq. 4.20). The energy is **quantised** because the boundary conditions only allow certain $k$.

*Things to notice.* (a) $\psi$ is continuous at the walls but its slope jumps there: allowed, because $V$ is infinite (the "continuous derivative" item of Move 4.7 needs a *finite* potential). (b) The lowest level is $E_1>0$: the zero-point energy. Squeezing the particle into width $L$ forces a momentum spread of order $\hbar/L$, hence kinetic energy of order $\hbar^2/(2mL^2)$. (c) $E_n\propto n^2$ and $E_1\propto 1/L^2$: shrink the box and every level shoots up. (d) $\psi_n$ is a standing wave: a superposition of $+\hbar k$ and $-\hbar k$ momenta, so it has no definite momentum.

## Core concepts

- **Measurement postulate:** measuring $\hat A$ returns one eigenvalue $a_n$ with probability $|c_n|^2$, where $c_n$ is the amplitude of $|a_n\rangle$ in the state. Say it as "the Born rule in the eigenbasis".
- **Collapse:** after the result $a_n$, the state is the matching eigenvector, renormalised. Immediate repeat gives the same answer.
- **Expectation value (discrete):** $\langle A\rangle=\sum|c_n|^2a_n$. An average over many identical preparations, not a value you will see on one shot.
- **Hamiltonian $\hat H$:** the energy operator; its eigenvalues are the possible energies.
- **Schrödinger equation:** the law for how $\Psi$ changes with time; the time-independent form is $\hat H\psi=E\psi$.
- **Time evolution:** $\Psi(x,t)=\sum\alpha_n\psi_n e^{-iE_nt/\hbar}$. Each energy component just rotates its phase; the moduli $|\alpha_n|$ never change. (Compact form: $|\Psi(t)\rangle=e^{-i\hat Ht/\hbar}|\Psi(0)\rangle$; this is the "time-evolution operator" that the Week 4 quiz asks about.)
- **Separation of variables:** guess a product $e^{-i\omega t}\psi(x)$ so the PDE splits into an ordinary differential equation in $x$.
- **Stationary state:** a solution of the form $\psi_n(x)e^{-iE_nt/\hbar}$; all probabilities are time-independent.
- **Boundary condition:** a requirement on $\psi$ at the edge of the region (here $\psi(0)=\psi(L)=0$). Boundary conditions, not the equation, select the allowed $k$ and hence the **energy levels**.
- **Potential well:** a region where $V$ is low, trapping the particle; the infinite square well is the simplest.
- **Time is not an observable:** in $\Psi(x,t)$, $t$ is a parameter, a label for "when". There is no Hermitian operator whose eigenvalues are times.

## Exercises

All exercises use new states and operators. Cold attempt first (10 min per exercise, at most), then the hint, then the sketch. Use $\varepsilon$ for an energy unit and $\hbar$, $m$, $L$ as usual.

1. A three-level system has energy eigenstates $|\varphi_1\rangle,|\varphi_2\rangle,|\varphi_3\rangle$ with $E_n=n^2\varepsilon$ (energies $\varepsilon,4\varepsilon,9\varepsilon$). It is prepared in $|\psi\rangle=\frac{1}{7}\big(2|\varphi_1\rangle+3i|\varphi_2\rangle-6|\varphi_3\rangle\big)$. Check normalisation, then give every possible energy with its probability, and compute $\langle E\rangle$. — **Hint:** square the modulus of each coefficient, prefactor included (so $|3i/7|^2=9/49$, and the sign of $-6$ is irrelevant); the three probabilities must add to 1; then weight the energies by these probabilities. — **Solution sketch:** $|c|^2$ sum: $(4+9+36)/49=49/49=1$. $P(\varepsilon)=4/49\approx0.082$, $P(4\varepsilon)=9/49\approx0.184$, $P(9\varepsilon)=36/49\approx0.735$. $\langle E\rangle=(4\cdot1+9\cdot4+36\cdot9)\varepsilon/49=364\varepsilon/49=52\varepsilon/7\approx7.43\,\varepsilon$, which lies between $\varepsilon$ and $9\varepsilon$.

2. Same system and state as Exercise 1. An operator $\hat A$ has $\hat A|\varphi_n\rangle=(5-2n)\,a\,|\varphi_n\rangle$ (so $3a,\,a,\,-a$). (a) What values can a measurement of $A$ give, with what probabilities, and what is $\langle A\rangle$? (b) An energy measurement gives $4\varepsilon$. A measurement of $A$ follows. What do you get? Explain why. — **Hint:** the eigenvectors are the same states $|\varphi_n\rangle$, so the probabilities are the same $|c_n|^2$ as in Exercise 1, only the values attached change. For (b), collapse first, then ask what $\hat A$ does to the collapsed state. — **Solution sketch:** (a) $3a$ with $4/49$, $a$ with $9/49$, $-a$ with $36/49$; $\langle A\rangle=(4\cdot3+9\cdot1-36)a/49=-15a/49\approx-0.31\,a$ (between $-a$ and $3a$, as it must be). (b) After the outcome $4\varepsilon$ the state is $|\varphi_2\rangle$ (up to a phase), which is an $\hat A$ eigenvector with eigenvalue $a$, so $A=a$ with probability 1. $\hat A$ and $\hat H$ share eigenvectors, so they can be sharp together.

3. A qubit is in $|\psi\rangle=\frac15(3|0\rangle+4|1\rangle)$ with $\sigma_z|0\rangle=|0\rangle$, $\sigma_z|1\rangle=-|1\rangle$, and $\sigma_x$ eigenvectors $|\pm\rangle=\frac{1}{\sqrt2}(|0\rangle\pm|1\rangle)$ with eigenvalues $\pm1$. (a) If $\sigma_x$ is measured directly on $|\psi\rangle$, what is $P(+1)$? (b) Now measure $\sigma_z$ first and get $+1$. Then measure $\sigma_x$. What can you get, and with what probabilities? (c) If you then measure $\sigma_z$ again, is the answer certain? Say why, in terms of $[\sigma_z,\sigma_x]$. — **Hint:** for (a), $c_+=\langle+|\psi\rangle=\frac{1}{\sqrt2}\cdot\frac{3+4}{5}$. For (b), collapse to $|0\rangle$ and expand $|0\rangle$ in the $|\pm\rangle$ basis. For (c), after the $\sigma_x$ result the state is $|+\rangle$ or $|-\rangle$; expand that in $|0\rangle,|1\rangle$. — **Solution sketch:** (a) $P(+1)=|c_+|^2=49/50=0.98$. (b) After $\sigma_z=+1$ the state is $|0\rangle=\frac{1}{\sqrt2}(|+\rangle+|-\rangle)$, so $\sigma_x=\pm1$ each with probability $1/2$. (c) No: $|\pm\rangle$ each give $\sigma_z=\pm1$ with probability $1/2$. The operators do not commute ($[\sigma_z,\sigma_x]=2i\sigma_y\neq0$), so they have no common eigenbasis and measuring $\sigma_x$ destroys the earlier $\sigma_z$ information.

4. Take the system and state of Exercise 1. An operator $\hat C$ has $\hat C|\varphi_1\rangle=c|\varphi_1\rangle$, $\hat C|\varphi_2\rangle=c|\varphi_2\rangle$ and $\hat C|\varphi_3\rangle=-c|\varphi_3\rangle$ ($c$ is a constant with units). (a) A measurement of $C$ gives $+c$. Write the state immediately after, properly normalised. (b) An energy measurement follows. What are the probabilities of $\varepsilon$, $4\varepsilon$, $9\varepsilon$, and what is $\langle E\rangle$? (c) Repeat $\hat C$ immediately: what do you get? — **Hint:** the eigenvalue $+c$ is shared by $|\varphi_1\rangle$ and $|\varphi_2\rangle$, so keep only those two terms of the state, then rescale so that the squared coefficients add to 1. Renormalising means dividing by the square root of the sum of the kept $|c|^2$. — **Solution sketch:** (a) Keep $2|\varphi_1\rangle+3i|\varphi_2\rangle$ (times $1/7$); the kept weight is $(4+9)/49=13/49$, so divide by its root: new state $\frac{1}{\sqrt{13}}(2|\varphi_1\rangle+3i|\varphi_2\rangle)$. (Probability of this outcome was $13/49$.) (b) $P(\varepsilon)=4/13$, $P(4\varepsilon)=9/13$, $P(9\varepsilon)=0$, so $\langle E\rangle=(4\varepsilon+36\varepsilon)/13=40\varepsilon/13\approx3.08\,\varepsilon$. Forgetting to renormalise would give probabilities summing to $13/49$: a red flag. (c) $+c$ with probability 1.

5. A system in the same energy eigenbasis ($E_n=n^2\varepsilon$) is prepared in the un-normalised state $|\chi\rangle=3|\varphi_1\rangle+4|\varphi_2\rangle+12i|\varphi_3\rangle$. (a) Normalise it. (b) Find the energy probabilities and $\langle E\rangle$. (c) If the preparation is repeated $1690$ times and $E$ is measured each time, about how many outcomes of each energy do you expect? — **Hint:** the norm-squared is $9+16+144$; check it is a perfect square. Multiply each probability by $1690$ for (c). — **Solution sketch:** (a) $9+16+144=169=13^2$, so $|\psi\rangle=\frac{1}{13}(\dots)$. (b) $P=9/169,\,16/169,\,144/169$; $\langle E\rangle=(9+64+1296)\varepsilon/169=1369\varepsilon/169\approx8.10\,\varepsilon$. (c) $1690\times$ those: $90$, $160$, $1440$ (they sum to $1690$).

6. A particle in the infinite well has (real, orthonormal) energy eigenfunctions $\psi_n(x)$ and energies $E_n$. (a) Show that $|\Psi(x,t)|^2$ is independent of time if $\Psi(x,0)=\psi_2(x)$. (b) For $\Psi(x,0)=\frac35\psi_1(x)+\frac45\psi_3(x)$, find $\Psi(x,t)$ and $|\Psi(x,t)|^2$, and show it depends on time. Give its angular frequency in terms of $E_1$, using $E_n=n^2E_1$. — **Hint:** attach $e^{-iE_nt/\hbar}$ to each term. In (a) you multiply $\psi_2$ by its conjugate phase, giving $1$. In (b) multiply out $\Psi^*\Psi$; the cross terms combine into a cosine (use $e^{i\theta}+e^{-i\theta}=2\cos\theta$, Move 1.3). — **Solution sketch:** (a) $\Psi=\psi_2e^{-iE_2t/\hbar}$ so $|\Psi|^2=\psi_2^2\,|e^{-iE_2t/\hbar}|^2=\psi_2^2$. (b) $\Psi=\frac35\psi_1e^{-iE_1t/\hbar}+\frac45\psi_3e^{-iE_3t/\hbar}$, and $|\Psi|^2=\frac{9}{25}\psi_1^2+\frac{16}{25}\psi_3^2+\frac{24}{25}\psi_1\psi_3\cos\!\big[(E_3-E_1)t/\hbar\big]$. The cosine makes it time-dependent; the angular frequency is $(E_3-E_1)/\hbar=8E_1/\hbar$, and the period is $2\pi\hbar/(8E_1)$.

7. For the state of Exercise 6(b), (a) show that the probability of measuring energy $E_1$ (and $E_3$) does not change with time even though $|\Psi|^2$ does, and (b) compute $\langle E\rangle$ in units of $E_1$. — **Hint:** the amplitude of $\psi_n$ at time $t$ is $\alpha_ne^{-iE_nt/\hbar}$; take its modulus squared. — **Solution sketch:** (a) $|\alpha_ne^{-iE_nt/\hbar}|^2=|\alpha_n|^2$: $P(E_1)=9/25$, $P(E_3)=16/25$ for all $t$. Phases rotate the amplitudes, not their sizes. The *position* pattern moves because it depends on the *relative* phase. (b) $\langle E\rangle=\frac{9}{25}E_1+\frac{16}{25}\cdot9E_1=\frac{153}{25}E_1=6.12\,E_1$, constant in time.

8. Solve the infinite well again, but with the walls at $x=-L/2$ and $x=+L/2$. Use $\psi=A\cos kx+B\sin kx$ and the boundary conditions $\psi(\pm L/2)=0$. Find the allowed $k$, the normalised functions, and the energies; compare with the well on $[0,L]$. — **Hint:** write the two boundary conditions, then add them and subtract them. One combination kills $B$, the other kills $A$. — **Solution sketch:** Adding: $2A\cos(kL/2)=0$. Subtracting: $2B\sin(kL/2)=0$. Either $B=0$ and $\cos(kL/2)=0$ (so $k=n\pi/L$ with $n$ odd), or $A=0$ and $\sin(kL/2)=0$ (so $k=n\pi/L$ with $n$ even, $n\ge2$). So $\psi_n=\sqrt{2/L}\cos(n\pi x/L)$ for odd $n$, $\sqrt{2/L}\sin(n\pi x/L)$ for even $n$, and $E_n=n^2\pi^2\hbar^2/(2mL^2)$: the same energies, the same width $L$, only the origin has moved.

9. Ground state of the well on $[0,L]$: (a) starting from $\psi=C\sin(\pi x/L)$, find $C$. (b) Find the probability of finding the particle in the left third, $0\le x\le L/3$. (c) Compare with the value for a uniform density and comment. — **Hint:** use $\sin^2\theta=\frac12(1-\cos2\theta)$ and the substitution $\theta=\pi x/L$ (or integrate in $x$ directly); for (b) the antiderivative of $\frac1L(1-\cos\frac{2\pi x}{L})$ is $\frac xL-\frac{1}{2\pi}\sin\frac{2\pi x}{L}$. — **Solution sketch:** (a) $C^2L/2=1$, so $C=\sqrt{2/L}$. (b) $P=\big[\frac xL-\frac{1}{2\pi}\sin\frac{2\pi x}{L}\big]_0^{L/3}=\frac13-\frac{\sin(2\pi/3)}{2\pi}=\frac13-\frac{\sqrt3}{4\pi}\approx0.196$. (c) A uniform density would give $1/3\approx0.333$. The ground state is piled up in the middle, so the outer thirds get less. The middle third then holds about $1-2(0.196)=0.61$.

10. Ground-state energy scaling. (a) By what factor does $E_1$ change if $L$ is halved? If $L$ is tripled? (b) For an electron ($m=9.11\times10^{-31}$ kg, $\hbar=1.055\times10^{-34}$ J s) in a well of width $L=1.0$ nm, compute $E_1$ in joules and in eV ($1\text{ eV}=1.602\times10^{-19}$ J). (c) Give $E_2-E_1$ for that well, and the ground energy if the width is $0.5$ nm. — **Hint:** $E_1\propto L^{-2}$, so ratios need no constants. For (b) compute $\pi^2\hbar^2$ first, then divide by $2mL^2$; check that the units are joules. — **Solution sketch:** (a) $L\to L/2$: $E_1\times4$. $L\to3L$: $E_1/9$. (b) $E_1=\pi^2\hbar^2/(2mL^2)\approx6.0\times10^{-20}$ J $\approx0.38$ eV. (c) $E_2-E_1=3E_1\approx1.1$ eV. At $0.5$ nm, $E_1=4\times0.376\approx1.5$ eV. Each reading agrees with "confine harder, energy goes up": the zero-point energy.

11. Show that $\psi_1$ and $\psi_2$ for the well on $[0,L]$ are orthogonal, $\int_0^L\psi_1\psi_2\,\mathrm{d}x=0$. Why does this matter for the probabilities in Move 5.1? — **Hint:** substitute $u=\pi x/L$, use $\sin2u=2\sin u\cos u$, and then a substitution $w=\sin u$ (or recognise $\sin^2u\cos u$ as a derivative). — **Solution sketch:** $\int_0^L\frac2L\sin\frac{\pi x}{L}\sin\frac{2\pi x}{L}\mathrm{d}x=\frac2\pi\int_0^\pi\sin u\sin2u\,\mathrm{d}u=\frac4\pi\int_0^\pi\sin^2u\cos u\,\mathrm{d}u=\frac4\pi\Big[\frac{\sin^3u}{3}\Big]_0^\pi=0$. They are eigenvectors of the Hermitian $\hat H$ with different eigenvalues (Move 3.3), so orthogonality is guaranteed. Orthonormality is what makes $c_n=\langle\psi_n|\Psi\rangle$ and $\sum|c_n|^2=1$ work.

## Assessment 1 readiness checklist

Skills only. Tick an item only when you can do it on a blank page, without notes, in under a few minutes. Anything unticked is tomorrow morning's warm-up.

**Day 1 — algebra and complex numbers**
- [ ] I can rearrange, use exponent rules and simplify square roots and fractions without losing signs.
- [ ] I can write the conjugate $z^*$ and modulus $|z|$ of a complex number, and use $|z|^2=z^*z$.
- [ ] I can use $e^{i\theta}=\cos\theta+i\sin\theta$, know $|e^{i\theta}|=1$, and explain why a global phase does not change a probability.
- [ ] I can use $\sin^2+\cos^2=1$ and the double-angle identities.

**Day 2 — kets, bras, inner products**
- [ ] I can write the bra of a ket (conjugate transpose) and compute $\langle\phi|\psi\rangle$ for column vectors.
- [ ] I can state the inner-product axioms (linear in the ket, conjugate symmetry, $\langle A|A\rangle\ge0$) and use them to prove a small identity line by line.
- [ ] I can expand a state in an orthonormal basis, find $c_n=\langle n|\psi\rangle$ and check normalisation.
- [ ] I can multiply a $2\times2$ matrix by a vector and by another matrix.

**Day 3 — operators**
- [ ] I can find eigenvalues and eigenvectors of a $2\times2$ matrix and normalise the eigenvectors.
- [ ] I can find the adjoint of a matrix and state the Hermitian condition, and know that Hermitian operators have real eigenvalues and orthogonal eigenvectors.
- [ ] I can prove $(AB)^\dagger=B^\dagger A^\dagger$ with the order reversed, and the sum and scalar rules.
- [ ] I can write the Pauli matrices, their eigenvectors, and a commutator $[A,B]=AB-BA$.

**Day 4 — functions and integrals**
- [ ] I can treat $\int\varphi^*\psi\,\mathrm{d}x$ as an inner product and normalise a wave function.
- [ ] I can do exponential, sine and half-line integrals, and integrate by parts with vanishing boundary terms.
- [ ] I can judge acceptability of a wave function against the five-item checklist.
- [ ] I can find the momentum operator's action on $e^{ikx}$ and find the adjoint of a simple operator by integrating by parts.

**Day 5 — measurement and dynamics**
- [ ] I can turn a state expansion into probabilities and an expectation value, and keep probabilities and eigenvalues separate.
- [ ] I can apply collapse (including renormalising) and say when a second measurement is certain.
- [ ] I can derive the time-independent Schrödinger equation by separating variables.
- [ ] I can solve the box problem from $\psi''=-k^2\psi$ with boundary conditions, including the normalisation constant and energies.

## Apply to the lecture (40 min)

Open `week_4/week_4_lecture.md` next to the Week 4 companion (`companions/week04_companion.md`). Read the companion sections in this order: **What this week is really saying**, **Notation decoder**, **Skipped steps, expanded**, then **Retrieval questions**.

Pair each lecture section with today's moves:

| Lecture section | Move today | What to check |
|---|---|---|
| 4.1 Time independent Schrödinger equation (Eqs. 4.1–4.8) | 5.4, 5.1, 5.2 | Can you redo the separation of variables from Eq. 4.2 and reproduce the cosine term in $|\Psi|^2$ without looking? |
| 4.1, closing list (probabilities $|\alpha_n|^2$, $\sum|\alpha_n|^2=1$, $\langle\hat H\rangle$) | 5.1, 5.2 | This is Move 5.1 and 5.2 with $\hat H$ as the observable. |
| 4.2 The free particle (Eqs. 4.9–4.18) | 5.4, 4.8 | $e^{ikx}$ is an eigenfunction (Move 4.8); why is it not normalisable (Move 4.5)? Note $\hbar^2k^2/2m$. |
| 4.3 The infinite potential well (Eqs. 4.19–4.20, Figs. 4.1–4.2) | 5.5 | Redo the derivation without the lecture: step 2 gives the sine, step 3 quantises $k$. |

Use the six quiz themes as a self-test before you look at the questions: (1) what the Hamiltonian is, (2) what the time-evolution operator does to a state, (3) why time is not an observable, (4) why normalisation matters, (5) why energy in a well is quantised, (6) the shape of the ground-state density and why it is not constant. Each of these is a paragraph you can already write from today's notes.

Then, and only then, open the Week 4 Task and Portfolio problems and attempt them cold. Today's exercises are practice for the technique; the course problems themselves are for you to solve and write up in the six-steps format.

## Anti-patterns / Common mistakes

- **Mixing up coefficients and probabilities.** The coefficient $c_n$ is an amplitude (a complex number); the probability is $|c_n|^2$. When the prefactor (such as $1/\sqrt{34}$) is part of the coefficient, square the whole coefficient, prefactor included; do not square the bracket entry alone. Also never attach the eigenvalue to the probability slot: a table of "value, probability" has the *eigenvalue* in the first column and $|c_n|^2$ in the second.
- **Forgetting to renormalise after a collapse.** After any measurement whose outcome covers several basis states (or after you drop terms), divide by the square root of the remaining weight. Quick check: the new $|c|^2$ must sum to 1.
- **Treating time as an observable.** $t$ is a parameter that labels when, not an eigenvalue of an operator. Stationary states have a time-dependent phase but a time-independent density; a superposition of different energies has a time-dependent density but time-independent energy probabilities. Also: the energy "uncertainty" relation $\Delta E\,\Delta t$ is not a Hermitian-operator statement.
- **Taking $n=0$ in the box, or dropping the boundary conditions.** $n=0$ is the empty box; the quantisation comes from the conditions at the walls, not from the differential equation.

## Confusion log

| Symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |

## Warm-up answers (fold: cover until you have tried)

<details>
<summary>Answers to the five Day-4 warm-up questions</summary>

1. $\int|\psi|^2=C^2\int_0^\infty e^{-4x}\,\mathrm{d}x=\frac{C^2}{4}$. Set to 1: $C=2$.
2. $\int_{-\infty}^{\infty}e^{-ax^2}\,\mathrm{d}x=\sqrt{\pi/a}$. The integrand $xe^{-x^2}$ is odd, so the left half cancels the right half.
3. $\hat p\,e^{ikx}=\frac\hbar i\cdot ik\,e^{ikx}=\hbar k\,e^{ikx}$. The eigenvalue is $\hbar k$.
4. No: it is unbounded and not normalisable on all of $\mathbb R$ ($|\psi|^2=e^{2x}$ grows without bound as $x\to+\infty$, so $\int|\psi|^2\mathrm dx$ diverges). The other checklist items (continuous, single-valued, smooth) pass.
5. $\int_0^\infty C^2e^{-2x}\,\mathrm{d}x=C^2/2=1$, so $C=\sqrt2$. $\langle x\rangle=2\int_0^\infty x\,e^{-2x}\,\mathrm{d}x=2\cdot\frac14=\frac12$ (by parts, or $\int_0^\infty xe^{-ax}\mathrm{d}x=1/a^2$).

</details>
