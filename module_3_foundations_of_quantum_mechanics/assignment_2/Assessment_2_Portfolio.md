# Assessment 2 [Portfolio (POF)]

## Portfolio problems

### Week 2:
#### Problem 1

At time $t = 0$ a particle is represented by the wave function

$$\begin{equation*}
	\psi(x,0) =
	\begin{cases}
		A\left(\dfrac{x}{a}\right) &0\le x\le a,\\
		A\dfrac{(b-x)}{(b-a)} &a\le x \le b,\\
		0, &\text{otherwise},
	\end{cases}
\end{equation*}$$

where $A$, $a$, and $b$ are positive real constants.

a. Normalise $\psi$ (that is, find $A$, in terms of $a$ and $b$).\
b. Sketch $\psi(x,0)$ as a function of $x$.\
c. Where is the particle most likely to be found, at $t = 0$?\
d. What is the probability of finding the particle to the left of $x = a$? Check your result in the limiting cases $b \to 2a$ and $b \to a$.\
e. What is the expectation value of $x$?

---

#### Problem 2

In the concrete representation of bras and kets by row and column vectors, the inner product is defined in terms of components:

$$\begin{align*}
	\langle{B|A}\rangle &= (\beta_1^{\star}\, \beta_2^{\star}\, \beta_3^{\star}) \begin{pmatrix}\alpha_1\\ \alpha_2\\ \alpha_3 \end{pmatrix}\\
	&= \beta_1^{\star}\alpha_1 + \beta_2^{\star}\alpha_2 + \beta_3^{\star}\alpha_3.
\end{align*}$$

The rule for inner products is essentially the same as for dot products: add the products of corresponding components of the vectors whose inner product is being calculated.

Show that the inner product $\langle{B|A}\rangle$, defined as above, satisfies all the axioms of inner products (conjugate symmetry, linearity in the second argument, and positive-definiteness).

### Week 3
#### Problem 1

Show that the position operator $\hat{x}=x$ and momentum operator $\hat{p} = \frac{\hbar}{i}\frac{\partial}{\partial x}$ are Hermitian, in other words, that $\langle{\phi|\hat{x}\psi}\rangle = \langle{\hat{x}\phi|\psi}\rangle$ and $\langle{\phi|\hat{p}\psi}\rangle = \langle{\hat{p}\phi|\psi}\rangle$

---

#### Problem 2

The wave function of an electron in the lowest energy state of a hydrogen atom is proportional to $e^{-r/a_0}$, with $a_0$ a constant and $r$ the distance from the nucleus. Calculate the relative probabilities of finding the electron inside a region of volume $1.0\text{ pm}^3$, located at

- the nucleus
- a distance $a_0$ from the nucleus.

As the region of interest is so small, even on the scale of the atom, we can ignore the variation of $\psi$ within it.

### Week 4
#### Problem 1

Consider a system whose state is given in terms of an orthonormal set of three vectors: $\lvert \phi_1 \rangle$, $\lvert \phi_2 \rangle$, $\lvert \phi_3 \rangle$ as

$$\lvert \psi \rangle= \frac{\sqrt{3}}{3}{\lvert\phi_1\rangle} + \frac{2}{3}{\lvert\phi_2\rangle} + \frac{\sqrt{2}}{3}{\lvert\phi_3\rangle}$$

a. Verify that $\lvert \psi\rangle$ is normalised. Then, calculate the probability of finding the system in any one of the states $\lvert \phi_1 \rangle$, $\lvert \phi_2 \rangle$ and $\lvert \phi_3 \rangle$. Verify that the total probability is equal to one.\
b. Consider now an ensemble of 810 identical systems, each one of them in the state $|\psi\rangle$. If measurements are done on all of them, how many systems will be found in each of the states $\lvert \phi_1 \rangle$, $\lvert \phi_2 \rangle$ and $\lvert \phi_3 \rangle$.

#### Problem 2

1. Show that the sum of two hermitian operators is hermitian.
2. Suppose $\hat{Q}$ is hermitian, and $\alpha$ is a complex number. Under what condition (on $\alpha$) is $\alpha \hat{Q}$ hermitian?
3. When is the product of two hermitian operators hermitian?
4. Show that the Hamiltonian operator $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{d x^2}+ V(x)$ is hermitian.

### Week 5
#### Problem 1

Consider a system whose wave function at time $t = 0$ is given by:

$$\begin{equation*}
\lvert \psi(x,0) \rangle = \frac{5}{\sqrt{50}}\lvert\phi_0(x)\rangle + \frac{4}{\sqrt{50}}\lvert\phi_1(x)\rangle + \frac{3}{\sqrt{50}}\lvert\phi_2(x)\rangle,
\end{equation*}$$

where $\lvert\phi_n(x)\rangle$ is the wave function of the $n^{\mathrm{th}}$ excited state for a harmonic oscillator of energy $E_n = \hbar \omega \left(n + \frac{1}{2}\right)$.

a. Find the average energy of this system.\
b. Find the state $\lvert\psi(x,t)\rangle$ at a later time $t$ and the average value of the energy; compare the result with the value obtained in (a). *Hint:* the eigenvalue equation for the time-evolution operator is $$\hat{U}|{\phi_n(x)}\rangle \equiv e^{-i\hat{H}t/\hbar}|{\phi_n(x)}\rangle =  e^{-iE_n t/\hbar}|{\phi_n(x)}\rangle.$$
\
c. Find the expectation value of the operator $\hat{x}$ with respect to the state $|\psi(x, t)\rangle$ (i.e., find $\langle{\psi(x,t)\rvert\hat{x}\lvert\psi(x,t)\rangle}$). *Hint:* Use $\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}^{\dagger} + \hat{a}\right)$.

---

#### Problem 2

Calculate the expectation value of the momentum for a harmonic oscillator prepared in a state which is a superposition of two number states:

$$\begin{equation*}
	\lvert{\psi}\rangle = \frac{1}{\sqrt{2}}\left(\lvert{\psi_1}\rangle - i\lvert{\psi_2\rangle}\right).
\end{equation*}$$

### Week 7
#### Problem 1

Consider a two-spin composite state $|{\psi}\rangle$ prepared such that we can write

$$\begin{align*}
    \lvert{\psi}\rangle = \frac{1}{\sqrt{2}}\left(\lvert{\uparrow_A \downarrow_B}\rangle - \lvert{\downarrow_A \uparrow_B}\rangle\right),
\end{align*}$$

where, for clarity, the subscripts $A$ and $B$ denote the subspace on which Alice and Bob will measure their spin components. First, Bob measures $y$-component of the spin with the operator $\tau_y$, then Alice measures $x$-component with the operator $\sigma_x$.

a. What is the expectation value of $\langle{\sigma_x \tau_y}\rangle = \langle{\psi\rvert\sigma_x \tau_y\lvert\psi}\rangle$? 
\
b. Calculate the expectation values of $\langle{\tau_y}\rangle = \langle{\psi\rvert\tau_y\lvert\psi}\rangle$ and $\langle{\sigma_x}\rangle = \langle{\psi\rvert\sigma_x\lvert\psi}\rangle$.
\
c. What is the correlation between the two measurements ($\langle{\sigma_x \tau_y}\rangle - \langle{\sigma_x}\rangle\langle{\tau_y}\rangle$)?