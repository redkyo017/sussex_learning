# Discussion Topic: Week 5 Task problems – hints

## Problems

### Problem 1
The ground state of a quantum harmonic oscillator of mass $m$ and angular frequency $\omega$ is
$$\psi_0(x,t) = A\exp\left( -\frac{m\omega}{2\hbar}x^2-i\omega t \right),$$
where $A$ is a constant. Show that $\psi_0(x,t)$ is a solution of the Schrödinger equation
$$\hat{H}|\psi{_0}(x,t)\rangle = E\mid\psi_0(x,t)\rangle,$$
where the Hamiltonian is that of the quantum harmonic oscillator,
$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2,$$
and the energy of the ground state is
$$E=\frac{\hbar\omega}{2}.$$

*Hint: Write $\hat{H}$ in the position representation and substitute $\psi_0(x,t)$ into the Schrödinger equation.*

#### Problem 1 hints
These hints are intended to help you get started. They do not contain the complete solution.

* Start by writing the position and momentum operators in the position representation:
  $$\hat{x}\rightarrow x, \qquad \hat{p}\rightarrow -i\hbar\frac{\partial}{\partial x}.$$
* What does this imply for $\hat{p}^2$? Once you have worked this out, substitute these expressions into $\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2$.
* You should obtain a differential operator involving a second derivative with respect to $x$.
* Next apply this Hamiltonian to 

   $\psi{_0}(x,t) = A\exp\left( -\frac{m\omega}{2\hbar}x^2-i\omega t \right)$.
* Since the Hamiltonian contains derivatives with respect to $x$, the factor involving t behaves simply as a constant during these derivatives. It may therefore be useful to focus first on the spatial part
  $$\exp\left(-\frac{m\omega}{2\hbar}x^2\right).$$
* To keep the differentiation tidy, you could temporarily define $\alpha = \frac{m\omega}{2\hbar}$ so that the spatial part becomes $e^{-\alpha x^2}$.
* Calculate its first derivative and then its second derivative. Be particularly careful with the second derivative: after the first differentiation you have a product of $x$ and an exponential, so the *product rule* is required.
* You should find that the second derivative contains two types of terms: one proportional to the original Gaussian and another proportional to $x^2$ times the Gaussian.
* Finally substitute this second derivative into the Hamiltonian. Look at what happens to the terms proportional to $m\omega^2x^2\psi{_0}$.
* If the proposed wave function is an energy eigenstate, all remaining terms should be expressible in the form $\text{constant}\times\psi{_0}(x,t)$.
* Compare that constant with the stated ground-state energy $E=\hbar\omega/2$.

---

### Problem 2
The Heisenberg uncertainty relation for position and momentum is
$$\Delta x \Delta p \ge \frac{\hbar}{2}$$
In this problem, we will calculate explicitly the uncertainty $\Delta x\,\Delta p$ of the quantum harmonic oscillator ground state $\psi{_0}(x,t) = A\exp\left( -\frac{m\omega}{2\hbar}x^2-i\omega t \right).$.

1. Find the normalisation constant $A$.
2. The uncertainty $\Delta x$ is the standard deviation
   $$\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$$
   Calculate $\langle x \rangle$ and $\langle x^2 \rangle$, and hence find $\Delta x$.
3. Using a similar strategy to part (b), find the uncertainty in momentum $\Delta p$.
4. Compare the product $\Delta x \Delta p$ with the Heisenberg uncertainty relation. What can you say about the harmonic oscillator ground state?

*Useful information:*
The following change of variables can simplify the calculations:
$$x = \sqrt{\frac{\hbar}{m\omega}}\,\xi, \qquad dx = \sqrt{\frac{\hbar}{m\omega}}\,d\xi.$$

You may also use Gaussian integrals:
$$\int_{-\infty}^{+\infty} e^{-ax^2}\,dx = \sqrt{\frac{\pi}{a}}, \\ \int_{-\infty}^{+\infty} x^2e^{-ax^2}\,dx = \frac{\sqrt{\pi}}{2a^{3/2}}.$$

Remember also that the integral of an odd function over a symmetric interval is zero:
$$\int_{-u}^{+u}f_{\mathrm{odd}}(x)\,dx=0.$$

#### Problem 2 hints
These hints are intended to help you get started. They do not contain the complete solution.

1. **Normalisation**
   * Start from the normalisation condition $\int_{-\infty}^{+\infty} |\psi_0(x,t)|^2 dx = 1$.
   * First calculate the complex conjugate $\psi_0^*(x,t)$. What happens to the time-dependent phase when $\psi_0^* \psi_0$ is formed?
   * After multiplying the two exponentials, your integral should have the form of a standard Gaussian:
     $$|A|^2 \int_{-\infty}^{+\infty} e^{-a x^2}\,dx = 1.$$
   * Identify $a$ by comparing the exponent with the Gaussian integral supplied in the question, then solve for $A$.

2. **Position uncertainty**
   * You need two quantities:
     $$\langle x\rangle, \qquad \langle x^2\rangle.$$
   * Start with 

      $\langle x\rangle = \int_{-\infty}^{+\infty} \psi{_0}^\star(x,t)\, x\, \psi{_0}(x,t)\,dx$.
   
   Before doing any integration, inspect the parity of the integrand. The probability density $|\psi_0(x,t)|^2$ is an even function of $x$, while $x$ is odd. What does that tell you about the integral over $(-\infty, +\infty)$?
   * For $\langle x^2 \rangle$, write
     $$\langle x^2\rangle = \int_{-\infty}^{+\infty} \psi{_0}^\star(x,t)\, x^2\, \psi{_0}(x,t)\,dx.$$
     This time the integrand is even and does not vanish. You can either use the supplied Gaussian integral directly or make the substitution $x = \sqrt{\frac{\hbar}{m\omega}} \xi$.
   * If you make this substitution, remember to replace *all three* of $x$, $x^2$, $dx$.
   * Once $\langle x \rangle$ and $\langle x^2 \rangle$ are known, substitute them into $\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$.

3. **Momentum uncertainty**
   * Follow exactly the same overall strategy, but now use the momentum operator in the position representation:
     $$\hat{p} = -i\hbar\frac{\partial}{\partial x}.$$
   * You need $\langle p \rangle = \langle \psi_0 | \hat{p} | \psi_0 \rangle$ and $\langle p^2 \rangle = \langle \psi_0 | \hat{p}^2 | \psi_0 \rangle$.
   * In position representation, $\hat{p}^2 = -\hbar^2 \frac{\partial^2}{\partial x^2}$.
   * For $\langle p \rangle$, first differentiate the Gaussian once. Inspect the parity of the resulting integrand before attempting to evaluate the integral.
   * For $\langle p^2 \rangle$, you need the second derivative of the Gaussian. The differentiation performed in Problem 1 can therefore be reused here.
   * After taking the second derivative, you should obtain terms involving both $e^{-m\omega x^2/\hbar}$ and $x^2e^{-m\omega x^2/\hbar}$.
   * Both integrals are given in the useful information above.
   * Finally use $\Delta p = \sqrt{\langle p^2 \rangle - \langle p \rangle^2}$.

4. **Comparing with the uncertainty principle**
   * Once you have obtained $\Delta x$ and $\Delta p$, multiply them together and simplify:
     $$\Delta x \Delta p $$
   * In particular, look for factors of m and \omega that cancel.
   * Then compare your result with the lower bound $\Delta x\,\Delta p \geq \frac{\hbar}{2}$.
   * Does the ground state give a product larger than the lower bound, or does it reach the limiting value exactly? What would the latter tell you about the ground state?