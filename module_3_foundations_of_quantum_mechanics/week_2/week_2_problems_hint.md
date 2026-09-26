# Week 2 Task Problems – Hints

## Problem 1
Using the axioms for inner products:
- Linearity: $\langle C | (|A\rangle + |B\rangle) = \langle C | A \rangle + \langle C | B \rangle$
- Interchanging bras and kets corresponds to complex conjugation: $\langle B | A \rangle = \langle A | B \rangle^*$

Prove $(\langle A | + \langle B |)|C\rangle = \langle A | C \rangle + \langle B | C \rangle$;  
Prove that $\langle A | A \rangle$ is a real number.

### Problem 1 Hints
These hints are intended to help you get started. They do not contain the complete solution.

The linearity axiom is written with the sum appearing in the ket. In this part of the problem, however, the sum appears in the bra. Try first using the complex-conjugation property to reverse the order of the bra and ket:

$$\langle X | Y \rangle = \langle Y | X \rangle^*$$

Once the sum has been moved to the ket side, you can use the linearity axiom. Finally, take the complex conjugate again to return to the original ordering. You may also find the following property useful:

$$(z_1 + z_2)^* = z_1^* + z_2^*$$

Apply the complex-conjugation axiom to the special case in which the two states are the same. In other words, ask what the relation $\langle B | A \rangle = \langle A | B \rangle^*$ becomes when $B = A$. Then recall a simple property of complex numbers: if a complex number is equal to its own complex conjugate, what can you say about its imaginary part?

---

## Problem 2
Suppose that $f(x)$ and $g(x)$ are two eigenfunctions of an operator $\hat{Q}$ with the same eigenvalue $q$. Show that any linear combination of $f$ and $g$ is itself an eigenfunction of $\hat{Q}$ with eigenvalue $q$.

Check that $f(x) = \exp(x)$ and $g(x) = \exp(-x)$ are eigenfunctions of the operator $\frac{d^2}{dx^2}$, with the same eigenvalue. Construct two linear combinations of $f$ and $g$ that are orthogonal eigenfunctions on the interval $(-1, 1)$.

### Problem 2 Hints
These hints are intended to help you get started. They do not contain the complete solution.

Start by writing down what it means for $f(x)$ and $g(x)$ to be eigenfunctions with the same eigenvalue:

$$\hat{Q}f = qf, \quad \hat{Q}g = qg$$

Now define a general linear combination $h(x) = af(x) + bg(x)$, where $a$ and $b$ are constants, and apply $\hat{Q}$ to $h(x)$. Remember that a quantum-mechanical operator is linear:

$$\hat{Q}(af + bg) = a\hat{Q}f + b\hat{Q}g$$

After substituting the eigenvalue equations for $f$ and $g$, see whether you can factor out something common.

First apply the operator $d^2/dx^2$ separately to $e^x$ and $e^{-x}$. Compare the result with the original function in each case.

For the second part, notice that the interval $(-1, 1)$ is symmetric about $x = 0$. This suggests looking for one linear combination that is even and another that is odd. Try the combinations:

$$f(x) + g(x) \quad \text{and} \quad f(x) - g(x)$$

To check orthogonality, consider the inner product:

$$\int_{-1}^{1} h_1^*(x) h_2(x) \, dx$$

What happens when the integrand is an odd function and the integration limits are symmetric about zero?

---

## Problem 3
Which of the following functions make good wave functions for describing a particle moving in one dimension? Sketch the probability density for each of them and check whether it is normalisable. Determine the normalisation constant $C_n$ for those that are normalisable. The parameters $\lambda_n$ are all real and positive.

$$\psi_1(x) = \begin{cases} 0, & x < 0 \\ C_1 \sin(\lambda_1 x), & 0 \le x \le 2\pi/\lambda_1 \\ 0, & x > 2\pi/\lambda_1 \end{cases}$$

$$\psi_2(x) = \frac{C_2}{x + \lambda_2} \quad \text{for all } x$$

$$\psi_3(x) = C_3 \exp(\lambda_3 x^2) \quad \text{for all } x$$

$$\psi_4(x) = C_4 \exp(-\lambda_4 |x|) \quad \text{for all } x$$

### Problem 3 Hints
These hints are intended to help you get started. They do not contain the complete solution.

The first thing to consider for each candidate is its probability density, $|\psi(x)|^2$. A normalisable wave function must satisfy:

$$\int_{-\infty}^{\infty} |\psi(x)|^2 \, dx < \infty$$

If this integral is finite, the constant $C_n$ can then be chosen so that the integral equals $1$.

Notice that $\psi_1(x)$ is non-zero only over a finite interval. Therefore you only need to integrate between $0$ and $2\pi/\lambda_1$. After squaring the wave function, you will encounter:

$$\int_{0}^{2\pi/\lambda_1} \sin^2(\lambda_1 x) \, dx$$

The identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$ should make this integral straightforward. Once you have evaluated it, impose the normalisation condition to determine $C_1$. For the sketch, remember that the probability density is proportional to $\sin^2(\lambda_1 x)$, not $\sin(\lambda_1 x)$.

Before attempting the full integral for $\psi_2(x)$, inspect the denominator: $x + \lambda_2$. Is there a value of $x$ at which it becomes zero? Examine what happens to:

$$|\psi_2(x)|^2 = \frac{|C_2|^2}{(x + \lambda_2)^2}$$

near that point. A useful substitution is $u = x + \lambda_2$. You then need to decide whether an integral behaving like $\int \frac{du}{u^2}$ remains finite when the integration interval includes $u = 0$.

Squaring the magnitude for $\psi_3(x)$ gives:

$$|\psi_3(x)|^2 = |C_3|^2 \exp(2\lambda_3 x^2)$$

Pay particular attention to the fact that $\lambda_3 > 0$. Ask what happens to the exponential as $x \to \pm\infty$. Compare its behaviour with the more familiar Gaussian $\exp(-\lambda x^2)$. You may be able to decide whether the function is normalisable without explicitly evaluating the integral.

The absolute value makes $\psi_4(x)$ symmetric about $x = 0$. Therefore:

$$|\psi_4(-x)|^2 = |\psi_4(x)|^2$$

This allows you to simplify the normalisation integral using:

$$\int_{-\infty}^{\infty} |\psi_4(x)|^2 \, dx = 2 \int_{0}^{\infty} |\psi_4(x)|^2 \, dx$$

For $x \ge 0$, the absolute value is simply $|x| = x$, leaving an ordinary decaying exponential integral. Evaluate that integral and then impose the condition that the total probability equals 1.