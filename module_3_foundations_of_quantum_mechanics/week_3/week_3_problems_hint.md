# Week 3 Task Problems – Hints

## Problem 1
Prove that the vector $|\psi_1\rangle = \frac{1}{\sqrt{2}}|u\rangle + \frac{1}{\sqrt{2}}|d\rangle$ is orthogonal to the vector $|\psi_2\rangle = \frac{1}{\sqrt{2}}|u\rangle - \frac{1}{\sqrt{2}}|d\rangle$.

### Problem 1 Hints
These hints are intended to help you get started. They do not contain the complete solution.

Two states are orthogonal if their inner product is zero. Therefore, the quantity you need to calculate is $\langle \psi_1 | \psi_2 \rangle$. You can approach this in two equivalent ways.

#### Approach 1: Use the basis states directly
Substitute the expressions for $|\psi_1\rangle$ and $|\psi_2\rangle$ into the inner product and expand it. You will then encounter inner products such as $\langle u | u \rangle$, $\langle u | d \rangle$, $\langle d | u \rangle$, and $\langle d | d \rangle$. Recall that $|u\rangle$ and $|d\rangle$ form an orthonormal basis. What are the values of these four inner products?

#### Approach 2: Write the states as column vectors
Use state representation:

$$|u\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |d\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

First construct the column vectors corresponding to $|\psi_1\rangle$ and $|\psi_2\rangle$. Remember that a bra is obtained from a ket by taking the Hermitian conjugate: transpose the column vector and complex conjugate its entries.

Finally, multiply the row vector $\langle \psi_1 |$ by the column vector $|\psi_2\rangle$. What result would demonstrate orthogonality?

---

## Problem 2
Assume the spin operator

$$\sigma_n = \begin{pmatrix} \cos(\theta) & \sin(\theta) \\ \sin(\theta) & -\cos(\theta) \end{pmatrix}$$

Calculate the eigenvectors and eigenvalues of $\sigma_n$. Assume that an eigenvector has the form

$$|\lambda\rangle = \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix}$$

where $\alpha$ is an unknown parameter. Plug this vector into the eigenvalue equation and solve for $\alpha$ in terms of $\theta$.

Why did we use a single parameter $\alpha$? Notice that our suggested column vector must have unit length.

### Problem 2 Hints
These hints are intended to help you get started. They do not contain the complete solution.

Begin with the eigenvalue equation:

$$\sigma_n |\lambda\rangle = \lambda |\lambda\rangle$$

Substitute the matrix and the suggested eigenvector:

$$\begin{pmatrix} \cos(\theta) & \sin(\theta) \\ \sin(\theta) & -\cos(\theta) \end{pmatrix} \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix} = \lambda \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix}$$

Perform the matrix multiplication. This gives two simultaneous equations, one from each component of the vector.

The following trigonometric identities are particularly useful:

$$\cos(A - B) = \cos A \cos B + \sin A \sin B$$

$$\sin(A - B) = \sin A \cos B - \cos A \sin B$$

After using these identities, you should be able to express $\lambda$ in two different ways. Since both expressions represent the same eigenvalue, set them equal to one another.

You should eventually obtain a trigonometric condition involving $2\alpha - \theta$. Remember that $\sin\beta = 0$ for values of $\beta$ separated by $\pi$. There should be two independent eigenvectors.

Once you have found the two possible values of $\alpha$, substitute each one back into either of your equations for $\lambda$ to obtain the corresponding eigenvalue.

#### Why is only one parameter needed?
A general real two-component vector has two components, but the eigenvectors here are required to have unit length:

$$\cos^2(\alpha) + \sin^2(\alpha) = 1$$

Geometrically, a unit vector in a two-dimensional real plane lies on the unit circle. Once its length is fixed, only one parameter, its angle, is required to specify its direction.

---

## Problem 3
Which of the following functions could represent physically acceptable wave functions for a particle moving in one dimension? Assume that the particle can move over the whole real line, $-\infty < x < \infty$. Explain your reasoning.

1. $f(x) = 3 \sin(\pi x)$
2. $g(x) = 4 - |x|$
3. $h^2(x) = 5x$
4. $e(x) = x^2$

### Problem 3 Hints
These hints are intended to help you get started. They do not contain the complete solution.

Start by recalling the basic requirements for a physically acceptable wave function. In particular, it must be possible to normalise it, so you should ask whether:

$$\int_{-\infty}^{\infty} |\psi(x)|^2 \, dx < \infty$$

is finite.

Also remember that the wave function itself is allowed to be positive, negative or complex. A negative value of $\psi(x)$ is therefore not by itself a reason for rejecting a function.

#### Analysis of $f(x) = 3 \sin(\pi x)$
Sketch $3 \sin(\pi x)$ over an increasingly large range of $x$. Does its amplitude decrease as $|x| \to \infty$?

The relevant quantity for normalisation is $|f(x)|^2 = 9 \sin^2(\pi x)$. Think about what happens when a positive periodic function is integrated over an interval whose length becomes arbitrarily large.

Would your conclusion be different if the particle were confined to a finite interval rather than the whole real line?

#### Analysis of $g(x) = 4 - |x|$
Sketch $g(x) = 4 - |x|$. Do not reject it simply because it becomes negative: wave functions may have either sign.

Instead, calculate $|g(x)|^2 = (4 - |x|)^2$ and inspect its behaviour as $|x| \to \infty$. Does it decrease sufficiently rapidly as $x$ becomes large?

#### Analysis of $h^2(x) = 5x$
For $h^2(x) = 5x$, note that $|h(x)|^2 = |5x| = 5|x|$. Look at the integral:

$$\int_{-\infty}^{\infty} 5|x| \, dx$$

Does it converge or diverge?

#### Analysis of $e(x) = x^2$
For $e(x) = x^2$, the function is smooth, continuous and single-valued. However, these conditions alone are not enough. Calculate:

$$|e(x)|^2 = x^4$$

and inspect its behaviour as $|x| \to \infty$. Would its integral over the whole real line be finite?

---

## General Strategy
A useful general strategy for all four cases is:

$$\text{function} \longrightarrow |\psi(x)|^2 \longrightarrow \text{behaviour as } |x| \to \infty \longrightarrow \text{normalisable or not?}$$