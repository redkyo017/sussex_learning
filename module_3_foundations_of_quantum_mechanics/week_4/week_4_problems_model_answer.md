# Discussion Topic: Week 4 Task problems – model answers

## Problems

### Problem 1
A system is initially in the state $|\psi_0\rangle = \frac{1}{7} [2|\phi_1\rangle + 3|\phi_2\rangle + |\phi_3\rangle + |\phi_4\rangle]$, where $|\phi_n\rangle$ are eigenstates of the system's Hamiltonian such that $\hat{H}|\phi_n\rangle = n^2\epsilon_0|\phi_n\rangle$.

1. If energy is measured, what values will be obtained and with what probabilities?
2. Consider an operator $\hat{A}$ whose action on $\phi_n$ is defined by $\hat{A}\phi_n = (n + 1)a_0\phi_n$. If $A$ is measured, what values will be obtained and with what probabilities?
3. Suppose that a measurement of the energy yields $4\epsilon_0$. If we measure $A$ immediately afterwards, what value will be obtained?

### Problem 1 Model Answer

1. 
Following the measurement of the energy, the system will collapse into one of its eigenstates $\phi_n$ with $n \in \{1, 2, 3, 4\}$. We need to find what is the energy eigenvalue $E_n$ associated with each of these eigenstates $\phi_n$. A measurement of the energy yields
$$E_n = \langle\phi_n|\hat{H}|\phi_n\rangle = \langle\phi_n|n^2\epsilon_0|\phi_n\rangle = n^2\epsilon_0\langle\phi_n|\phi_n\rangle = n^2\epsilon_0.$$

That leads to the following energies:
* $E_1 = \epsilon_0$
* $E_2 = 4\epsilon_0$
* $E_3 = 9\epsilon_0$
* $E_4 = 16\epsilon_0$

The probability of various measurement outcomes is given by the expression
$$P(E_n) = \frac{|\langle\phi_n|\psi_0\rangle|^2}{\langle\psi_0|\psi_0\rangle} = |\langle\phi_n|\psi_0\rangle|^2,$$
where we used the fact that $\psi_0$ is normalised,

$⟨\psi_{0}|\psi_{0}⟩=\frac{1}{\sqrt{7}}(\begin{matrix}\sqrt{2} & \sqrt{3} & 1 & 1\end{matrix})\frac{1}{\sqrt{7}}(\begin{matrix}\sqrt{2} \\ \sqrt{3} \\ 1 \\ 1\end{matrix})=\frac{2+3+1+1}{7}=1,$ 

Since the eigenstates $|\phi_n\rangle$ are orthonormal, i.e., $\langle\phi_n|\phi_m\rangle = \delta_{nm}$, we have:
* $P(E_1) = |\langle\phi_1|\psi_0\rangle|^2 = \left|\langle\phi_1|\left(\frac{1}{\sqrt{7}}[\sqrt{2}|\phi_1\rangle + \sqrt{3}|\phi_2\rangle + |\phi_3\rangle + |\phi_4\rangle]\right)\right|^2 = \left|\frac{\sqrt{2}}{\sqrt{7}}\underbrace{\langle\phi_1|\phi_1\rangle}_{= 1} + \frac{\sqrt{3}}{\sqrt{7}}\underbrace{\langle\phi_1|\phi_2\rangle}_{= 0} + \frac{1}{\sqrt{7}}\underbrace{\langle\phi_1|\phi_3\rangle}_{= 0} + \frac{1}{\sqrt{7}}\underbrace{\langle\phi_1|\phi_4\rangle}_{= 0}\right|^2 = \left|\frac{\sqrt{2}}{\sqrt{7}}\langle\phi_1|\phi_1\rangle\right|^2 = \left|\frac{\sqrt{2}}{\sqrt{7}}\right|^2 = \frac{2}{7}$ [Note: The source text shows $\frac{2}{7}$ squared computation context].
* $P(E_2) = \left|\frac{\sqrt{3}}{\sqrt{7}}\langle\phi_2|\phi_2\rangle\right|^2 = \left|\frac{\sqrt{3}}{\sqrt{7}}\right|^2 = \frac{3}{7}$
* $P(E_3) = \left|\frac{1}{\sqrt{7}}\langle\phi_3|\phi_3\rangle\right|^2 = \left|\frac{1}{\sqrt{7}}\right|^2 = \frac{1}{7}$
* $P(E_4) = \left|\frac{1}{\sqrt{7}}\langle\phi_4|\phi_4\rangle\right|^2 = \left|\frac{1}{\sqrt{7}}\right|^2 = \frac{1}{7}$

We notice that the sum of probabilities of all outcomes adds to 1.

2. 
Similarly, a measurement of the observable $\hat{A}$ yields
$$a_n = \langle\phi_n|\hat{A}|\phi_n\rangle,$$
leading to the following eigenvalues:
* $a_1 = 2a_0$
* $a_2 = 3a_0$
* $a_3 = 4a_0$
* $a_4 = 5a_0$

Again, using the Eq. (2), we can calculate the probabilities corresponding to the eigenvalues $a_n$:
$$
\begin{aligned}
    P(a_1) &= \left|\left\langle \phi_1|\psi_0 \right\rangle\right|^2\\
    &= \left|
    \left\langle \phi_1 \right|
    \left(
    \frac{1}{\sqrt{7}}
    \left[
    \sqrt{2}\left|\phi_1\right\rangle
    + \sqrt{3}\left|\phi_2\right\rangle
    + \left|\phi_3\right\rangle
    + \left|\phi_4\right\rangle
    \right]
    \right)
    \right|^2\\
    &= \left|
    \frac{\sqrt{2}}{\sqrt{7}}\underbrace{\left\langle \phi_1|\phi_1 \right\rangle}_{=1}
    + \frac{\sqrt{3}}{\sqrt{7}}\underbrace{\left\langle \phi_1|\phi_2 \right\rangle}_{=0}
    + \frac{1}{\sqrt{7}}\underbrace{\left\langle \phi_1|\phi_3 \right\rangle}_{=0}
    + \frac{1}{\sqrt{7}}\underbrace{\left\langle \phi_1|\phi_4 \right\rangle}_{=0}
    \right|^2\\
    &= \left|\frac{\sqrt{2}}{\sqrt{7}}\left\langle \phi_1|\phi_1 \right\rangle\right|^2
    = \left|\frac{\sqrt{2}}{\sqrt{7}}\right|^2
    = \frac{2}{7}\\
    P(a_2) &= \left|\frac{\sqrt{3}}{\sqrt{7}}\left\langle \phi_2|\phi_2 \right\rangle\right|^2
    = \left|\frac{\sqrt{3}}{\sqrt{7}}\right|^2
    = \frac{3}{7}\\
    P(a_3) &= \left|\frac{1}{\sqrt{7}}\left\langle \phi_3|\phi_3 \right\rangle\right|^2
    = \left|\frac{1}{\sqrt{7}}\right|^2
    = \frac{1}{7}\\
    P(a_4) &= \left|\frac{1}{\sqrt{7}}\left\langle \phi_4|\phi_4 \right\rangle\right|^2
    = \left|\frac{1}{\sqrt{7}}\right|^2
    = \frac{1}{7}.
\end{aligned}
$$

And again, the sum of probabilities of all outcomes adds to 1.

3. 
An energy measurement that yields $4\epsilon_0$ implies that the system is left in the state $\phi_2$. A measurement of the observable $A$ immediately afterwards leads to
$$\langle\phi_2|\hat{A}|\phi_2\rangle = 3a_0\underbrace{\langle\phi_2|\phi_2\rangle}_{= 1} = 3a_0.$$

---

### Problem 2
1. Find the hermitian conjugates of $x$, $i$, and $d/dx$.
2. Show that $(\hat{Q}\hat{R})^\dagger = \hat{R}^\dagger\hat{Q}^\dagger$ (note the reversed order), $(\hat{Q} + \hat{R})^\dagger = \hat{Q}^\dagger + \hat{R}^\dagger$, and $(c\hat{Q})^\dagger = c^\star\hat{Q}^\dagger$.

### Problem 2 Model Answer

1. 
The hermitian conjugate of an operator $\hat{Q}$ is the operator $\hat{Q}^\dagger$ such that
$$\langle f|\hat{Q}g\rangle = \langle\hat{Q}^\dagger f|g\rangle$$
for all $f(x)$ and $g(x)$.
(Notice that $\langle f|\hat{Q}g\rangle$ and $\langle f|\hat{Q}|g\rangle$ are just two different notations for the same braket. In both cases the operator $\hat{Q}$ acts on the function $g$.)

* **To find the hermitian conjugate of $x$**, we express the inner product under its integral form:
  $$\langle f|xg\rangle = \int_{-\infty}^{\infty} f^\star(x)[xg(x)]dx = \int_{-\infty}^{\infty} [xf^\star(x)]g(x)dx$$
  As $x$ is a pure real number, we have $x^\star = x$:
  $$\int_{-\infty}^{\infty} [x^\star f^\star(x)]g(x)dx = \int_{-\infty}^{\infty} [xf(x)]^\star g(x)dx = \langle xf|g\rangle$$
  Comparing $\langle f|xg\rangle = \langle xf|g\rangle$ with the definition of the hermitian conjugate, we see that $x^\dagger = x$, that is, $x$ is its own hermitian conjugate.

* **To find the hermitian conjugate of $i$**:
  $$\langle f|ig\rangle = \int_{-\infty}^{\infty} f^\star(x)[ig(x)]dx = \int_{-\infty}^{+\infty} [if^\star(x)]g(x)dx$$
  As $i$ is a pure imaginary number, we have $i^\star = -i$, which can be written as $(-i)^\star$:
  $$\int_{-\infty}^{+\infty} [(-i)^\star f^\star(x)]g(x)dx = \int_{-\infty}^{+\infty} [-if(x)]^\star g(x)dx = \langle -if|g\rangle$$
  Comparing $\langle f|ig\rangle = \langle -if|g\rangle$ with the definition, we see that $i^\dagger = -i$.

* **To find the hermitian conjugate of $d/dx$**, it will require us to evaluate the integral using integration by parts. Recall, the integration by parts formula is $\int_{a}^{b} u dv = uv\big|_a^b - \int_{a}^{b} v du$. Also, while $f(x)$ and $g(x)$ are arbitrary complex-valued functions, they still need to be normalisable so that their modulus squares can be interpreted as probabilities. For that to be the case, the limits of functions $f(x)$ and $g(x)$ when $x \longrightarrow \pm\infty$ must be zero, i.e.,
  $$\lim_{x\to\pm\infty} |f(x)| = 0$$
  $$\lim_{x\to\pm\infty} |g(x)| = 0$$
  Finally, as $f(x)$ and $g(x)$ are complex-valued functions, we can decompose them into their real and imaginary parts, writing, for example, $f(x) = u(x) + iv(x)$, where $u(x)$ and $v(x)$ are both real-valued functions.
  Armed with those facts, we can now use the same method:
  $$\left\langle f\middle|\frac{d}{dx}g\right\rangle = \int_{-\infty}^{+\infty} f^\star(x)\left[\frac{d}{dx}g(x)\right]dx$$
  Using integration by parts with $u = f^\star(x)$ and $dv = \frac{d}{dx}g(x)dx$:
$$\begin{aligned}
    {\left\langle f \middle| \frac{d}{d x}g \right\rangle} &= \int_{-\infty}^{+\infty} f^{\star}(x) \left[\frac{d}{d x} g(x)\right] d x\\
    &\text{using integration by part with $u = f^{\star}(x)$ and $d v = \frac{d}{d x} g(x)$}\\
    &= \underbrace{f^{\star}(x)g(x)\Big|_{-\infty}^{+\infty}}_{=0} - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}f^{\star}(x)\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}f^{\star}(x)\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}\left(u(x) + iv(x)\right)^{\star}\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}\left(u(x) - iv(x)\right)\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\left(\frac{d u(x)}{d x} - i\frac{d v(x)}{d x}\right)\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\left(\frac{d u(x)}{d x} + i\frac{d v(x)}{d x}\right)^{\star}\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}\left( u(x) + iv(x)\right)^{\star}\right] g(x) d x\\
    &= - \int_{-\infty}^{+\infty} \left[\frac{d}{d x}f^{\star}(x)\right] g(x) d x\\
    &= \int_{-\infty}^{+\infty} \left[-\frac{d}{d x}f^{\star}(x)\right] g(x) d x\\
    &= {\left\langle -\frac{d}{d x}f \middle| g \right\rangle}.
\end{aligned}$$

  Thus, $\left(\frac{d}{dx}\right)^\dagger = -\frac{d}{dx}$.


* **Finding the hermitian conjugate of the product of two operators, $\hat{Q}\hat{R}$**, we'll use the same method with integrals.:
$$\begin{aligned}
    {\langle f|\hat{Q}\hat{R}g \rangle} &= {\langle f|\hat{Q}\hat{R}|g \rangle} \\
    &= \int_{-\infty}^{+\infty} f^{\star}(x) \hat{Q}\hat{R} g(x) d x\\
    &= \int_{-\infty}^{+\infty} f^{\star}(x) \left\{\hat{Q}\left[\hat{R} g(x)\right]\right\} d x\\
    &= \int_{-\infty}^{+\infty}\left[\hat{Q}^{\dagger} f(x)\right]^{\star} \left[\hat{R} g(x)\right] d x\\
    &=\int_{-\infty}^{+\infty}\left\{\hat{R}^{\dagger}\left[\hat{Q}^{\dagger} f(x)\right]\right\}^{\star} g(x) d x\\
    &=\int_{-\infty}^{+\infty}\left[\hat{R}^{\dagger}\hat{Q}^{\dagger} f(x)\right]^{\star} g(x) d x\\
    &= {\langle \hat{R}^{\dagger}\hat{Q}^{\dagger}f|g \rangle}.
\end{aligned}$$

  Therefore, $(\hat{Q}\hat{R})^\dagger = \hat{R}^\dagger\hat{Q}^\dagger$.

* **Finding the hermitian conjugate of the sum of two operators, $\hat{Q} + \hat{R}$**:
$$\begin{aligned}
    {\langle f|(\hat{Q} + \hat{R})g \rangle} &= \int_{-\infty}^{+\infty} f^{\star}(x)\left(\hat{Q} + \hat{R}\right) g(x) d x\\
    &= \int_{-\infty}^{+\infty} f^{\star}(x)\left[\hat{Q}g(x) + \hat{R}g(x)\right] d x\\
    &= \int_{-\infty}^{+\infty} \left[f^{\star}(x)\hat{Q}g(x) + f^{\star}(x)\hat{R}g(x)\right] d x\\
    &= \int_{-\infty}^{+\infty} f^{\star}(x) \hat{Q}g(x) d x + \int_{-\infty}^{+\infty} f^{\star}(x) \hat{R}g(x) d x\\
    &= \int_{-\infty}^{+\infty} \hat{Q}^{\dagger}f^{\star}(x) g(x) d x + \int_{-\infty}^{+\infty} \hat{R}^{\dagger} f^{\star}(x) g(x) d x\\
    &= \int_{-\infty}^{+\infty} \left[\hat{Q}^{\dagger}f(x)\right]^{\star} g(x) d x + \int_{-\infty}^{+\infty} \left[\hat{R}^{\dagger} f(x)\right]^{\star} g(x) d x\\
    &= \int_{-\infty}^{+\infty} \left[\hat{Q}^{\dagger}f(x) + \hat{R}^{\dagger} f(x)\right]^{\star} g(x) d x \\
    &= \int_{-\infty}^{+\infty} \left[\left(\hat{Q}^{\dagger} + \hat{R}^{\dagger}\right) f(x)\right]^{\star} g(x) d x \\
    &= {\langle (\hat{Q}^{\dagger} + \hat{R}^{\dagger})f|g \rangle}.
\end{aligned}$$


* **Finding the hermitian conjugate of $c\hat{Q}$**, where $c$ is a complex constant:
$$\begin{aligned}
    {\langle f|c\hat{Q}g \rangle} &= \int_{-\infty}^{+\infty} f^{\star}(x) c\hat{Q}g(x) d x\\
    &= c \int_{-\infty}^{+\infty} f^{\star}(x) \hat{Q}g(x) d x\\
    &= c \int_{-\infty}^{+\infty} \left[\hat{Q}^{\dagger}f(x)\right]^{\star}g(x) d x\\
    &= \int_{-\infty}^{+\infty} \left(c^{\star}\right)^{\star}\left[\hat{Q}^{\dagger}f(x)\right]^{\star}g(x) d x\\
    &= \int_{-\infty}^{+\infty}\left[c^{\star}\hat{Q}^{\dagger}f(x)\right]^{\star}g(x) d x\\
    &= {\langle c^{\star}\hat{Q}^{\dagger}f|g \rangle}.
\end{aligned}$$
  Therefore, $(c\hat{Q})^\dagger = c^\star\hat{Q}^\dagger$.