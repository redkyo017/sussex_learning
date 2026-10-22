# Topic: Week 5 Task problems – model answers

## Problems

### Problem 1

The ground state of quantum harmonic oscillator of mass $m$ and angular frequency $\omega$ is
$$\psi_0(x,t) = A \exp\left(-\frac{m\omega}{2\hbar}x^2 - i\omega t\right),$$
where $A$ is a constant. Show that $\psi_0(x,t)$ is a solution of the Schrödinger equation
$$\hat{H}|\psi_0(x,t)\rangle = E|\psi_0(x,t)\rangle \tag{1}$$
where the Hamiltonian $\hat{H}$ is that of quantum harmonic oscillator, i.e.,
$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2,$$
and the energy of the ground state is $E = \hbar\omega/2$.

*Hint: Write $\hat{H}$ in the position representation and substitute $\psi_0(x,t)$ into the Eq. (1).*

### Problem 1 model answer

We start by expressing relevant operators and the Hamiltonian in position representation.
$$\hat{p} \longrightarrow -i\hbar \frac{\partial}{\partial x}$$
$$\hat{p}^2 \longrightarrow (-i\hbar)^2 \frac{\partial^2}{\partial x^2} = -\hbar^2 \frac{\partial^2}{\partial x^2}$$
$$\hat{x} \longrightarrow x$$
$$\hat{x}^2 \longrightarrow x^2$$

The energy of the excited state $n$ of the quantum harmonic oscillator is $E_n = \hbar\omega\left(n + \frac{1}{2}\right)$, so for the ground state $n = 0$ we obtain
$$E_0 = \frac{\hbar \omega}{2}.$$

Thus, the Schrödinger equation can be written as
$$-\frac{\hbar^2}{2m}\frac{\partial^2 \psi_0(x,t)}{\partial x^2}+\frac{1}{2}m\omega^2 x^2 \psi_0(x,t) = \frac{\hbar \omega}{2}\psi_0(x,t).$$

Substituting the ground state of the quantum harmonic oscillator wave function into the equation above, we obtain
$$\begin{align*}
	\begin{split}
	-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\left[A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right)\right]+\frac{1}{2}m\omega^2 x^2 A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \\
	\quad= \frac{\hbar \omega}{2}A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right).
	\end{split}
\end{align*}$$

Dividing by $A $:
$$\begin{align*}
	-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2}\left[\exp\left(-\frac{m\omega}{2\hbar}x^2\right)\right]+\frac{1}{2}m\omega^2 x^2 \exp\left(-\frac{m\omega}{2\hbar}x^2\right) &= \frac{\hbar \omega}{2}\exp\left(-\frac{m\omega}{2\hbar}x^2\right).
\end{align*}$$

Differentiating the first time:
$$\begin{align*}
    -\frac{\hbar^2}{2m}\frac{\partial }{\partial x}\left[-2x\frac{m\omega}{2\hbar}\exp\left(-\frac{m\omega}{2\hbar}x^2\right)\right]+\frac{1}{2}m\omega^2 x^2 \exp\left(-\frac{m\omega}{2\hbar}x^2\right) &= \frac{\hbar \omega}{2}\exp\left(-\frac{m\omega}{2\hbar}x^2\right).
\end{align*}$$

Differentiating the second time and taking care of the derivative of the product of two functions of $x$ in the first term above ($\exp\left(-\frac{m\omega}{2\hbar}x^2\right)$), we obtain
$$\begin{align*}
	\begin{split}
		-\frac{\hbar^2}{2m} 	\left[-\frac{m\omega}{\hbar}\exp\left(-\frac{m\omega}{2\hbar}x^2\right) + x\frac{m\omega}{\hbar}2x\frac{m\omega}{2\hbar}\exp\left(-\frac{m\omega}{2\hbar}x^2\right) \right]+\frac{1}{2}m\omega^2 x^2 \exp\left(-\frac{m\omega}{2\hbar}x^2\right)\\
		= \frac{\hbar \omega}{2}\exp\left(-\frac{m\omega}{2\hbar}x^2\right).
	\end{split}
\end{align*}$$

Dividing by $\exp\left(-\frac{m\omega}{2\hbar}x^2\right)$:
$$\begin{align*}
		-\frac{\hbar^2}{2m} \left[-\frac{m\omega}{\hbar} + x\frac{m\omega}{\hbar}2x\frac{m\omega}{2\hbar} \right]+\frac{1}{2}m\omega^2 x^2 &= \frac{\hbar \omega}{2}.
\end{align*}$$

Simplifying the expression:
$$\begin{align*}
	\frac{\hbar^2 m \omega}{2 m \hbar} - \frac{\hbar^2 m^2 \omega^2 x^2}{2 m \hbar^2} + \frac{1}{2}m\omega^2 x^2 &= \frac{\hbar \omega}{2}\\
	\frac{\hbar\omega}{2} - \frac{1}{2}m\omega^2 x^2 + \frac{1}{2}m\omega^2 x^2 &= \frac{\hbar \omega}{2}\\
	\frac{\hbar \omega}{2} &= \frac{\hbar \omega}{2}.\\
	\mathrm{Q.E.D.}\quad \square
\end{align*}$$

---

### Problem 2

The famous Heisenberg uncertainty for position and momentum is given by
$$\Delta x \Delta p \ge \frac{\hbar}{2} \tag{2}$$

In this problem, we will calculate explicitly the uncertainty $\Delta x \Delta p$ of the quantum harmonic oscillator ground state $\psi_0(x,t) =  A\exp\left(-\frac{m\omega}{2\hbar}x^2 - i\omega t\right)$ (the same wave function from the previous question).

1. Find the normalisation constant $A$.
2. The uncertainty of an observable is its standard deviation given by the following expression $\Delta x \equiv \sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2},$ where $\langle x^2 \rangle$ is the expectation value of $x$-squared, and $\langle x \rangle^2$ is the expectation value squared of x. Calculate $\langle x \rangle$ and $\langle x^2 \rangle$, and find the uncertainty $\Delta x$.
3. Using the similar strategy as in (b), find the uncertainty in momentum $\Delta p$.
4. Compare the product $\Delta x \Delta p$ to the Heisenberg's uncertainty relation (Eq. (2)). What can you tell about the uncertainty of the harmonic oscillator ground state?

*Hints:*
- You will greatly simplify the calculations if you perform the following change of variables:
  $$\begin{align*}
        x &= \sqrt{\frac{\hbar}{m\omega}} \xi\\
        \text d x &= \sqrt{\frac{\hbar}{m\omega}} \text d \xi\\ 
    \end{align*}$$
- Integrals:
  $$\begin{aligned}
        \int_{-\infty}^{+\infty} e^{-ax^2}\text d x &= \sqrt{\frac{\pi}{a}}\\
        \int_{-\infty}^{+\infty} x^2 e^{-ax^2}\text d x &= \frac{\sqrt{\pi}}{2 a^{3/2}}.
    \end{aligned}$$

For an odd function, the integral over a symmetric interval equals zero, i.e.,
$$\int_{-u}^{+u} f_{\mathrm{odd}}(x) \text d x = 0.$$

---

### Problem 2 model answer

*Red text indicates when hints provided have been used in the model answer.*

1. We write the normalisation condition for $\psi_0(x,t)$:
   $$\begin{align*}
    \int_{-\infty}^{+\infty} \psi_0^{\star}(x,t)\psi_0(x,t) \text d x &= 1\\
    \Rightarrow \int_{-\infty}^{+\infty} A\exp\left(-\frac{m\omega}{2\hbar}x^2 + \cancel{i\omega t}\right) A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \text d x &= 1\\
    \Rightarrow A^2\int_{-\infty}^{+\infty} \exp\left(-\frac{m\omega}{\hbar}x^2 \right) \text d x &= 1\\\end{align*}$$

   Using one of the integrals given in the hint, we obtain
   $$\begin{align*}
	  A^2 \sqrt{\frac{\pi}{\frac{m\omega}{\hbar}}} &=1\\
    \Rightarrow A^2 &= \sqrt{\frac{m\omega}{\pi \hbar}} \\
    \Rightarrow \boxed{A = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}}\end{align*}
    $$

2. 
   *Calculating $\langle x \rangle$:*
   The definition of the expectation value of $x$ is:
   $$\begin{align*}\langle{x}\rangle = \langle{\psi_0|\hat{x}|\psi_0}\rangle\end{align*}$$
   Writing it in functional form, we have
   $$\begin{align*}
    \langle{x}\rangle &= \int_{-\infty}^{+\infty} \psi_0^{\star}(x,t) \hat{x} \psi_0(x,t) \text d x\\
    & =\int_{-\infty}^{+\infty}  A\exp\left(-\frac{m\omega}{2\hbar}x^2 + i\cancel{\omega t}\right) x  A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \text d x\\
    & =A^2\int_{-\infty}^{+\infty}  \exp\left(-\frac{m\omega}{2\hbar}x^2\right) x  \exp\left(-\frac{m\omega}{2\hbar}x^2 \right) \text d x\\\end{align*}
  $$
   Using the change of variables suggested in hints, we obtain
   $$\begin{align*}
      \langle{x}\rangle & =\left(\frac{m\omega}{\pi \hbar}\right)^{1/2} \int_{-\infty}^{+\infty} \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{black} \right) \cdot \color{red}\sqrt{\frac{\hbar}{m\omega}}\xi\color{black} \cdot \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{black}\right) \color{red}\sqrt{\frac{\hbar}{m\omega}} \text d\xi\\
      &= \left(\frac{m\omega}{\pi \hbar}\right)^{1/2} \left(\frac{\hbar}{m\omega}\right) \underbrace{\int_{-\infty}^{+\infty} \xi \exp\left(-\xi^2 \right)\text d \xi}_{\equiv 0} \\
      &= 0.
    \end{align*}
    $$
   We remark that $\xi \exp\left(-\xi^2 \right)$ is an odd function of $\xi$ ($\xi$: odd parity; $\exp\left(-\xi^2 \right)$: even parity; thus, $\xi \exp\left(-\xi^2 \right)$ is an odd function), and is integrated over a symmetric interval (from $-\infty$ to $+\infty$), thus, as recalled in hints, the integral is zero.
   Thus,
   $$\boxed{\langle{x}\rangle = 0}$$

   *Calculating $\langle x^2 \rangle$:*
   We are calculating the expectation value of $x^2$, that is:
   $$\begin{align*}
      \langle{x^2}\rangle = \langle{\psi_0|\hat{x}^2|\psi_0}\rangle.
    \end{align*}$$
    $$
      \begin{align*}
      \langle{x^2}\rangle &= \int_{-\infty}^{+\infty} \psi_0^{\star}(x,t) \hat{x}^2 \psi_0(x,t) \text d x\\
      & =\int_{-\infty}^{+\infty}  A\exp\left(-\frac{m\omega}{2\hbar}x^2 + \cancel{i\omega t}\right) x^2  A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \text d x\\
      & =A^2\int_{-\infty}^{+\infty}  \exp\left(-\frac{m\omega}{2\hbar}x^2\right) x^2  \exp\left(-\frac{m\omega}{2\hbar}x^2 \right) \text d x\\
      & =A^2\int_{-\infty}^{+\infty}  \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{black}\right) \cdot \color{red}\frac{\hbar}{m\omega}\xi^2\color{black} \cdot \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{black}\right)\color{red}\sqrt{\frac{\hbar}{m\omega}} \text d\xi\color{black} \\
      & =A^2 \left(\frac{\hbar}{m\omega}\right)^{3/2} \int_{-\infty}^{+\infty} \xi^2 \exp\left(-\xi^2\right) \text d \xi.
    \end{align*}
    $$
   Using the integral result given in the hint we have
   $$\begin{align*}
      \int_{-\infty}^{+\infty} x^2 \exp\left(-a x^2\right) \text d x = \frac{\sqrt{\pi}}{2 a^{3/2}}.
    \end{align*}$$
    In our case $x = \xi$ and $a = 1$, giving
    $$\int_{-\infty}^{+\infty} \xi^2 \exp\left(\xi^2\right) \text d \xi = \frac{\sqrt{\pi}}{2}.$$
   Substituting this result leads to:
   $$\begin{align*}
    \langle{x^2}\rangle &= A^2 \left(\frac{\hbar}{m\omega}\right)^{3/2} \frac{\sqrt{\pi}}{2}\\
    &= \left(\frac{m\omega}{\pi \hbar}\right)^{1/2} \left(\frac{\hbar}{m\omega}\right)^{3/2} \frac{\sqrt{\pi}}{2}\\
    &= \frac{\hbar}{2m\omega}.
    \end{align*}$$
   Thus, we have:
    $$\begin{aligned}
    \boxed{\langle{x^2}\rangle = \frac{\hbar}{2m\omega}}
    \end{aligned}$$
    Calculation of $\Delta x$\
    With the knowledge of $\langle{x}\rangle$ and $\langle{x^2}\rangle$ we can express the uncertainty $\Delta x$
    $$\begin{align*}
      \Delta x &= \sqrt{\langle{x^2}\rangle- \langle{x}^2}\rangle\\
      &= \sqrt{\frac{\hbar}{2m\omega} - 0}\\
      &=  \sqrt{\frac{\hbar}{2m\omega}}.
    \end{align*}$$
    $$\begin{align*}
        \boxed{\Delta x  = \sqrt{\frac{\hbar}{2m\omega}}}
    \end{align*}$$


3. 
   *Calculation of $\langle p \rangle$:*
   We will use the suggested change of variables
   $$\begin{align*}
      x &= \sqrt{\frac{\hbar}{m\omega}} \xi\\
      \text d x &= \sqrt{\frac{\hbar}{m\omega}} \text d \xi\\
      \frac{\partial}{\partial x} &= \sqrt{\frac{m\omega}{\hbar}} \frac{\partial}{\partial \xi}\\
    \end{align*}$$

   $$\begin{align*}
      \langle{p}\rangle &= \langle{\psi_0|\hat{p}|\psi_0}\rangle = \int_{-\infty}^{+\infty} \psi_0^{\star}(x,t) \hat{p} \psi_0(x,t) \text d x\\
      & =\int_{-\infty}^{+\infty}  A\exp\left(-\frac{m\omega}{2\hbar} x^2 + \cancel{i\omega t}\right) \left(-i\hbar \frac{\partial}{\partial x}\right)  A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \text d x\\
      &= A^2 \int_{-\infty}^{+\infty} \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{blue}\right) \left(-i\hbar \color{red}\sqrt{\frac{m\omega}{\hbar}} \frac{\partial}{\partial \xi}\color{blue}\right) \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{blue}\right) \color{red}\sqrt{\frac{\hbar}{m\omega}} \text d \xi\color{blue} \\
      & = -i\hbar \left(\frac{m\omega}{\pi \hbar}\right)^{1/2} \cancel{\sqrt{\frac{\hbar}{m\omega}}}  \cancel{\sqrt{\frac{m\omega}{\hbar}}} \int_{-\infty}^{+\infty} \exp\left(-\frac{\xi^2}{2}\right)\frac{\partial}{\partial \xi} \exp\left(-\frac{\xi^2}{2}\right) \text d \xi\\
      &= i \left(\frac{\hbar m\omega}{\pi}\right)^{1/2} \underbrace{\int_{-\infty}^{+\infty} \xi \exp\left(-\xi^2\right) \text d \xi}_{\equiv 0}\\
      &= 0.
    \end{align*}$$

    We remark that $\xi \exp\left(-\xi^2 \right)$ is an odd function of $\xi$ ($\xi$ : odd parity; $\exp\left(-\xi^2 \right):$ even parity; thus, $\xi \exp\left(-\xi^2 \right)$ is an odd function), and is integrated over a symmetric interval (from $-\infty$ to $+\infty$), thus, as recalled in hints, the integral is zero. Thus,

   *Calculation of $\langle p^2 \rangle$:*
   $$\begin{align*}
      \langle{p^2}\rangle &= \langle{\psi_0|\hat{p}^2|\psi_0}\rangle = \int_{-\infty}^{+\infty} \psi_0^{\star}(x,t) \hat{p}^2 \psi_0(x,t) \text d x\\
      &= \int_{-\infty}^{+\infty}  A\exp\left(-\frac{m\omega}{2\hbar} x^2 + \cancel{i\omega t}\right) \left(-i\hbar \frac{\partial}{\partial x}\right)^2  A\exp\left(-\frac{m\omega}{2\hbar}x^2 - \cancel{i\omega t}\right) \text d x\\
      &= A^2 \int_{-\infty}^{+\infty}  \exp\left(-\frac{m\omega}{2\hbar} x^2\right) \left(-\hbar^2 \frac{\partial^2}{\partial x^2}\right) \exp\left(-\frac{m\omega}{2\hbar}x^2 \right) \text d x\\
      &= A^2 \int_{-\infty}^{+\infty} \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{blue}\right) \left(\hbar^2 \color{red}\frac{m\omega}{\hbar} \frac{\partial^2}{\partial \xi^2}\color{blue}\right) \exp\left(-\frac{m\omega}{2\hbar}\color{red}\frac{\hbar}{m\omega}\xi^2\color{blue}\right) \color{red}\sqrt{\frac{\hbar}{m\omega}} \text d \xi\color{blue} \\
      &= -\left(\frac{m\omega}{\pi \hbar}\right)^{1/2} \sqrt{\frac{\hbar}{m\omega}}\hbar^2 \frac{m\omega}{\hbar} \int_{-\infty}^{+\infty} \exp\left(-\frac{\xi^2}{2} \right) \frac{\partial^2}{\partial \xi^2} \exp\left(-\frac{\xi^2}{2} \right) \text d \xi\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left(-\frac{\xi^2}{2} \right)\frac{\partial}{\partial \xi}\left[ -\xi \exp\left(-\frac{\xi^2}{2} \right)\right] \text d \xi\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left(-\frac{\xi^2}{2} \right)\left[ -\exp\left(-\frac{\xi^2}{2} \right) + (-\xi)(-\xi)\exp\left(-\frac{\xi^2}{2} \right) \right] \text d \xi\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left(-\frac{\xi^2}{2} \right)\left[ -\exp\left(-\frac{\xi^2}{2} \right) + \xi^2\exp\left(-\frac{\xi^2}{2} \right) \right] \text d \xi\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \left[\xi^2\exp\left(-\xi^2 \right) -\exp\left(-\xi^2 \right) \right] \text d \xi\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}}\left[ \underbrace{\int_{-\infty}^{+\infty} \xi^2\exp\left(-\xi^2 \right)\text d \xi}_{\sqrt{\pi}/2} - \underbrace{\int_{-\infty}^{+\infty}\exp\left(-\xi^2 \right)  \text d \xi}_{\sqrt{\pi}} \right]\\
      &= -\frac{m\omega \hbar}{\sqrt{\pi}}\left[\frac{\sqrt{\pi}}{2}-\sqrt{\pi}\right]\\
      &= \frac{m\omega \hbar}{\sqrt{\pi}}\frac{\sqrt{\pi}}{2}\\
      &= \frac{m\omega\hbar}{2}.
    \end{align*}$$

   Thus, 
      $\boxed{\langle{p^2}\rangle = \frac{m\omega\hbar}{2}}$ 
   
   *Calculation of $\Delta p$:*
   With the knowledge of $\langle p \rangle$ and $\langle p^2 \rangle$ we can express the uncertainty $\Delta p$:
   $$\begin{align*}
      \Delta p &= \sqrt{\langle{p^2}\rangle- \langle{p\rangle}^2}\\
      &= \sqrt{\frac{m\omega\hbar}{2} - 0}\\
      &=  \sqrt{\frac{m\omega\hbar}{2}}.
    \end{align*}$$

4. The product $\Delta x \Delta p$ corresponds to the uncertainty in the position and momentum of the harmonic oscillator ground state:
   $$\begin{align*}
      \Delta x \Delta p = \sqrt{\frac{\hbar}{2m\omega}} \sqrt{\frac{m\omega\hbar}{2}}= \frac{\hbar}{2}.
    \end{align*}$$
   On the other hand, we have a famous Heisenberg uncertainty given by:
   $$\Delta x \Delta p \ge \frac{\hbar}{2}$$
   One can see that the uncertainty in the position and momentum of the harmonic oscillator ground state is a special case, in the sense that it is the smallest possible uncertainty (notice $=$ sign instead of $\ge$) allowed by general Heisenberg uncertainty principle. We say that the harmonic oscillator ground state is a *minimum uncertainty wave packet*, or an *optimum state for position and momentum*.