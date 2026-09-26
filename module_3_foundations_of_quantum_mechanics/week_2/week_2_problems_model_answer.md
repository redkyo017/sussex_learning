# Week 2 Task Problems – Model Answers

## Problem 1
Using the axioms for inner products:
- Linearity: $\langle C | (|A\rangle + |B\rangle) = \langle C | A \rangle + \langle C | B \rangle$
- Interchanging bras and kets corresponds to complex conjugation: $\langle B | A \rangle = \langle A | B \rangle^*$

1. Prove $(\langle A | + \langle B |)|C\rangle = \langle A | C \rangle + \langle B | C \rangle$
2. Prove that $\langle A | A \rangle$ is a real number.

### Problem 1 Model Answer

#### Part 1
We want to evaluate $(\langle A | + \langle B |)|C\rangle$. First, use the complex conjugation axiom to swap the bra and ket sides:

$$(\langle A | + \langle B |)|C\rangle = \Big(\langle C | (|A\rangle + |B\rangle)\Big)^*$$

Next, apply the linearity axiom on the ket side inside the complex conjugate:

$$\langle C | (|A\rangle + |B\rangle) = \langle C | A \rangle + \langle C | B \rangle$$

Substituting this back in gives:

$$(\langle A | + \langle B |)|C\rangle = (\langle C | A \rangle + \langle C | B \rangle)^*$$

Using the property of complex conjugation $(z_1 + z_2)^* = z_1^* + z_2^*$:

$$(\langle A | + \langle B |)|C\rangle = \langle C | A \rangle^* + \langle C | B \rangle^*$$

Finally, applying the complex conjugation axiom again to each term ($\langle C | A \rangle^* = \langle A | C \rangle$ and $\langle C | B \rangle^* = \langle B | C \rangle$):

$$(\langle A | + \langle B |)|C\rangle = \langle A | C \rangle + \langle B | C \rangle$$

#### Part 2
To prove that $\langle A | A \rangle$ is real, set $B = A$ in the complex conjugation axiom $\langle B | A \rangle = \langle A | B \rangle^*$:

$$\langle A | A \rangle = \langle A | A \rangle^*$$

A complex number $z = x + iy$ satisfies $z = z^*$ if and only if its imaginary part is zero ($y = 0$). Therefore, $\langle A | A \rangle$ must be a purely real number.

---

## Problem 2
Suppose that $f(x)$ and $g(x)$ are two eigenfunctions of an operator $\hat{Q}$ with the same eigenvalue $q$. Show that any linear combination of $f$ and $g$ is itself an eigenfunction of $\hat{Q}$ with eigenvalue $q$.

Check that $f(x) = \exp(x)$ and $g(x) = \exp(-x)$ are eigenfunctions of the operator $\frac{d^2}{dx^2}$, with the same eigenvalue. Construct two linear combinations of $f$ and $g$ that are orthogonal eigenfunctions on the interval $(-1, 1)$.

### Problem 2 Model Answer

#### Part 1: Linear Combination Proof
Since $f(x)$ and $g(x)$ are eigenfunctions of $\hat{Q}$ with eigenvalue $q$, we have:

$$\hat{Q}f(x) = qf(x) \quad \text{and} \quad \hat{Q}g(x) = qg(x)$$

Consider a general linear combination $h(x) = a f(x) + b g(x)$, where $a, b \in \mathbb{C}$. Applying the linear operator $\hat{Q}$ to $h(x)$:

$$\hat{Q}h(x) = \hat{Q}\Big(a f(x) + b g(x)\Big) = a \hat{Q}f(x) + b \hat{Q}g(x)$$

Substituting the eigenvalue equations for $f$ and $g$:

$$\hat{Q}h(x) = a (q f(x)) + b (q g(x)) = q \Big(a f(x) + b g(x)\Big) = q h(x)$$

Thus, $h(x)$ is an eigenfunction of $\hat{Q}$ with the same eigenvalue $q$.

#### Part 2: Derivatives of Exponential Functions
Applying $\frac{d^2}{dx^2}$ to $f(x) = e^x$:

$$\frac{d^2}{dx^2} e^x = \frac{d}{dx} e^x = 1 \cdot e^x$$

Applying $\frac{d^2}{dx^2}$ to $g(x) = e^{-x}$:

$$\frac{d^2}{dx^2} e^{-x} = \frac{d}{dx} (-e^{-x}) = 1 \cdot e^{-x}$$

Both $f(x)$ and $g(x)$ are eigenfunctions of $\frac{d^2}{dx^2}$ with eigenvalue $q = 1$.

#### Part 3: Constructing Orthogonal Combinations
We construct symmetric (even) and antisymmetric (odd) linear combinations:

$$\psi_1(x) = \frac{f(x) + g(x)}{2} = \frac{e^x + e^{-x}}{2} = \cosh(x)$$

$$\psi_2(x) = \frac{f(x) - g(x)}{2} = \frac{e^x - e^{-x}}{2} = \sinh(x)$$

To check orthogonality on the symmetric interval $(-1, 1)$, we evaluate their inner product:

$$\langle \psi_1 | \psi_2 \rangle = \int_{-1}^{1} \psi_1^*(x) \psi_2(x) \, dx = \int_{-1}^{1} \cosh(x) \sinh(x) \, dx$$

Since $\cosh(x)$ is an even function and $\sinh(x)$ is an odd function, their product $\cosh(x)\sinh(x)$ is an odd function. The integral of an odd function over a symmetric interval $[-a, a]$ is identically zero:

$$\int_{-1}^{1} \cosh(x) \sinh(x) \, dx = \left[ \frac{1}{2} \sinh^2(x) \right]_{-1}^{1} = \frac{1}{2}\sinh^2(1) - \frac{1}{2}\sinh^2(-1) = 0$$

Thus, $\psi_1(x) = \cosh(x)$ and $\psi_2(x) = \sinh(x)$ are orthogonal eigenfunctions on $(-1, 1)$.

---

## Problem 3
Which of the following functions make good wave functions for describing a particle moving in one dimension? Sketch the probability density for each of them and check whether it is normalisable. Determine the normalisation constant $C_n$ for those that are normalisable. The parameters $\lambda_n$ are all real and positive.

$$\psi_1(x) = \begin{cases} 0, & x < 0 \\ C_1 \sin(\lambda_1 x), & 0 \le x \le 2\pi/\lambda_1 \\ 0, & x > 2\pi/\lambda_1 \end{cases}$$

$$\psi_2(x) = \frac{C_2}{x + \lambda_2} \quad \text{for all } x$$

$$\psi_3(x) = C_3 \exp(\lambda_3 x^2) \quad \text{for all } x$$

$$\psi_4(x) = C_4 \exp(-\lambda_4 |x|) \quad \text{for all } x$$

### Problem 3 Model Answer

#### Analysis of $\psi_1(x)$
The probability density is non-zero only on $[0, 2\pi/\lambda_1]$:

$$|\psi_1(x)|^2 = |C_1|^2 \sin^2(\lambda_1 x)$$

We check normalisation by integrating over all space:

$$\int_{-\infty}^{\infty} |\psi_1(x)|^2 \, dx = |C_1|^2 \int_{0}^{2\pi/\lambda_1} \sin^2(\lambda_1 x) \, dx$$

Using the trigonometric identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:

$$\int_{0}^{2\pi/\lambda_1} \sin^2(\lambda_1 x) \, dx = \int_{0}^{2\pi/\lambda_1} \frac{1 - \cos(2\lambda_1 x)}{2} \, dx = \left[ \frac{x}{2} - \frac{\sin(2\lambda_1 x)}{4\lambda_1} \right]_{0}^{2\pi/\lambda_1} = \frac{\pi}{\lambda_1}$$

Setting the total probability to 1:

$$|C_1|^2 \frac{\pi}{\lambda_1} = 1 \implies C_1 = \sqrt{\frac{\lambda_1}{\pi}}$$

$\psi_1(x)$ is **normalisable** and represents a physically acceptable wave function.

#### Analysis of $\psi_2(x)$
The function is given by $\psi_2(x) = \frac{C_2}{x + \lambda_2}$. Since $\lambda_2 > 0$ is real, the denominator vanishes at $x = -\lambda_2$.

At $x = -\lambda_2$, the function has a singularity where $|\psi_2(x)| \to \infty$. Furthermore, evaluating the integral around the singularity $u = x + \lambda_2$:

$$\int_{-\epsilon}^{\epsilon} \frac{du}{u^2} = \left[ -\frac{1}{u} \right]_{-\epsilon}^{\epsilon} = -\frac{1}{\epsilon} - \left(-\frac{1}{-\epsilon}\right) \to \infty$$

Because the function diverges at $x = -\lambda_2$ and the normalisation integral diverges, $\psi_2(x)$ is **not normalisable** and is **not physically acceptable**.

#### Analysis of $\psi_3(x)$
The probability density is given by:

$$|\psi_3(x)|^2 = |C_3|^2 \exp(2\lambda_3 x^2)$$

Since $\lambda_3 > 0$, as $x \to \pm\infty$, $2\lambda_3 x^2 \to +\infty$, causing $\exp(2\lambda_3 x^2) \to \infty$. The normalisation integral diverges:

$$\int_{-\infty}^{\infty} |\psi_3(x)|^2 \, dx = \infty$$

Thus, $\psi_3(x)$ is **not normalisable** and **not physically acceptable**.

#### Analysis of $\psi_4(x)$
The probability density is:

$$|\psi_4(x)|^2 = |C_4|^2 \exp(-2\lambda_4 |x|)$$

Since the integrand is symmetric about $x = 0$:

$$\int_{-\infty}^{\infty} |\psi_4(x)|^2 \, dx = 2|C_4|^2 \int_{0}^{\infty} \exp(-2\lambda_4 x) \, dx$$

Evaluating the integral:

$$\int_{0}^{\infty} \exp(-2\lambda_4 x) \, dx = \left[ -\frac{1}{2\lambda_4} \exp(-2\lambda_4 x) \right]_{0}^{\infty} = 0 - \left( -\frac{1}{2\lambda_4} \right) = \frac{1}{2\lambda_4}$$

Substituting this back into the normalisation condition:

$$2|C_4|^2 \left( \frac{1}{2\lambda_4} \right) = 1 \implies \frac{|C_4|^2}{\lambda_4} = 1 \implies C_4 = \sqrt{\lambda_4}$$

$\psi_4(x)$ is **normalisable** and represents a physically acceptable wave function.

---

## Summary Table

| Function | Normalisable? | Normalisation Constant $C_n$ | Main Reason |
| :--- | :--- | :--- | :--- |
| $\psi_1(x)$ | **Yes** | $C_1 = \sqrt{\lambda_1/\pi}$ | Finite domain, well-behaved |
| $\psi_2(x)$ | **No** | None | Diverges at $x = -\lambda_2$ |
| $\psi_3(x)$ | **No** | None | Diverges exponential growth at $\pm\infty$ |
| $\psi_4(x)$ | **Yes** | $C_4 = \sqrt{\lambda_4}$ | Decays exponentially at $\pm\infty$ |