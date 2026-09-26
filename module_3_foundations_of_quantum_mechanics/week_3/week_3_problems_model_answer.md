# Week 3 Task problems – model answers

All sections

---

### Problem 1
Prove that the vector $|\psi_1\rangle = \frac{1}{\sqrt{2}}|u\rangle + \frac{1}{\sqrt{2}}|d\rangle$ is orthogonal to vector $|\psi_2\rangle = \frac{1}{\sqrt{2}}|u\rangle - \frac{1}{\sqrt{2}}|d\rangle$.

#### Problem 1 model answer
Two vectors are orthogonal if their inner product is 0. Here we have two vectors, $|\psi_1\rangle$ and $|\psi_2\rangle$ which are linear combinations of other two vectors, known as spin-up ($|u\rangle$) and spin-down ($|d\rangle$). Writing those vectors explicitly, we have

$$|\psi_1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad |\psi_2\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

We calculate the inner product 

$$\langle \psi_1 | \psi_2 \rangle = \left(\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \end{pmatrix}\right) \left(\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}\right) = \frac{1}{2} (1\cdot 1 + 1\cdot(-1)) = 0$$

Remember that the kets such as $|\psi\rangle$ are represented by column vectors, while their corresponding bras are represented by row vectors

$$\langle \psi_1 | = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \end{pmatrix}$$

As the inner product of $|\psi_1\rangle$ and $|\psi_2\rangle$ is zero, that means that they are orthogonal.

---

### Problem 2
Assume spin operator

$$\sigma_n = \begin{pmatrix} \cos(\theta) & \sin(\theta) \\ \sin(\theta) & -\cos(\theta) \end{pmatrix}$$

Calculate the eigenvectors and eigenvalues of $\sigma_n$. Assume the eigenvector $|\lambda\rangle$ has the form $\begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix}$ where $\alpha$ is an unknown parameter. Plug this vector into the eigenvalue equation and solve for $\alpha$ in terms of $\theta$. Why did we use a single parameter $\alpha$? Notice that our suggested column vector must have unit length.

#### Problem 2 model answer
The length of a vector $|\lambda\rangle$ is

$$\sqrt{\cos^2(\alpha) + \sin^2(\alpha)} = 1$$

which indeed has unit length. To find the eigenvectors and eigenvalues of the operator $\sigma_n$, we need to solve the eigenvalue equation

$$\sigma_n |\lambda\rangle = \lambda |\lambda\rangle$$

where $|\lambda\rangle$ denotes the eigenvectors and $\lambda$ are the corresponding eigenvalues.

To solve this eigenvalue equation, we can write the expression above as a system of two equations

$$\cos(\theta)\cos(\alpha) + \sin(\theta)\sin(\alpha) = \lambda \cos(\alpha)$$
$$\sin(\theta)\cos(\alpha) - \cos(\theta)\sin(\alpha) = \lambda \sin(\alpha)$$

Using the known trigonometric identities

$$\cos(A - B) = \cos A \cos B + \sin A \sin B$$
$$\sin(A - B) = \sin A \cos B - \cos A \sin B$$

we can simplify the system of equations and write

$$\cos(\theta - \alpha) = \lambda \cos(\alpha)$$
$$\sin(\theta - \alpha) = \lambda \sin(\alpha)$$

Isolating $\lambda$ we get

$$\lambda = \frac{\cos(\theta - \alpha)}{\cos(\alpha)} = \frac{\sin(\theta - \alpha)}{\sin(\alpha)} \quad (1)$$

As both lines are equal to $\lambda$ we can write

$$\cos(\theta - \alpha)\sin(\alpha) = \sin(\theta - \alpha)\cos(\alpha) \implies \sin(\theta - \alpha)\cos(\alpha) - \cos(\theta - \alpha)\sin(\alpha) = 0$$

The last expression can be simplified again using the same trigonometric identity as before, of the type $\sin(A - B)$:

$$\sin(\theta - 2\alpha) = 0$$

The function $\sin$ is equal to zero when its argument is equal to $0$ or $\pi$. Thus we can write

$$\theta - 2\alpha = 0 \implies \alpha_1 = \frac{\theta}{2}$$
$$\theta - 2\alpha = -\pi \implies \alpha_2 = \frac{\theta + \pi}{2}$$

We can substitute the two values $\alpha_1$ and $\alpha_2$ into either of Equations (1) to obtain the expressions for eigenvalues $\lambda_1$ and $\lambda_2$. Using, say, the top equation, we have

$$\lambda_1 = \frac{\cos(\theta/2)}{\cos(\theta/2)} = 1$$
$$\lambda_2 = \frac{\cos(\theta - \theta/2 - \pi/2)}{\cos(\theta/2 + \pi/2)} = \frac{\cos(\theta/2 - \pi/2)}{-\sin(\theta/2)} = \frac{\sin(\theta/2)}{-\sin(\theta/2)} = -1$$

The corresponding eigenvectors $|\lambda_1\rangle$ and $|\lambda_2\rangle$ are

$$|\lambda_1\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}, \quad |\lambda_2\rangle = \begin{pmatrix} \cos(\theta/2 + \pi/2) \\ \sin(\theta/2 + \pi/2) \end{pmatrix} = \begin{pmatrix} -\sin(\theta/2) \\ \cos(\theta/2) \end{pmatrix}$$

Why did we use a single parameter $\alpha$? Notice that our suggested column vector must have unit length. Working with polar coordinates in a plane we need two parameters to determine a vector. One parameter is the length that is fixed to one, so we need only one other parameter. As second parameter we used the angle $\alpha$.

---

### Problem 3
Which of the following functions could represent physically acceptable wave functions for a particle moving in one dimension? Assume that the particle can move over the whole real line, $-\infty < x < \infty$. Explain your reasoning. 

$$f(x) = 3\sin(\pi x)$$
$$g(x) = 4 - |x|$$
$$h^2(x) = 5x$$
$$e(x) = x^2$$

#### Problem 3 model answer
*(Plots of the four functions are shown at the bottom.)*

For a wave function to describe a physical state, it must be single-valued and normalisable. In particular, its squared magnitude must have a finite integral: 

$$\int_{-\infty}^{\infty} |\psi(x)|^2 dx < \infty$$

The wave function itself may be positive, negative or complex. A change of sign therefore does not make a wave function unacceptable. Similarly, a discontinuity in its first derivative does not automatically make it unacceptable.

Consider $f(x) = 3\sin(\pi x)$. This function is continuous, finite and single-valued. Its squared magnitude is $|f(x)|^2 = 9\sin^2(\pi x)$. However, the function continues to oscillate with the same amplitude as $x \to \pm\infty$. It does not decay at large $|x|$. Therefore, 

$$\int_{-\infty}^{\infty} |f(x)|^2 dx = 9 \int_{-\infty}^{\infty} \sin^2(\pi x) dx = \infty$$

Hence, $f(x) = 3\sin(\pi x)$ is not normalisable on $(-\infty, \infty)$. There is, however, nothing inherently wrong with a sinusoidal wave function. The problem here is that the sine function extends over the whole real line with constant amplitude.

If the particle were instead confined to a finite interval, for example $-10 \le x \le 10$, then the normalisation integral would be finite: 

$$\int_{-10}^{10} |3\sin(\pi x)|^2 dx = 9 \int_{-10}^{10} \sin^2(\pi x) dx = 90$$

A normalised wave function with the same sinusoidal shape would then be 

$$\psi(x) = \begin{cases} \frac{1}{\sqrt{10}}\sin(\pi x), & -10 \le x \le 10, \\ 0, & \text{otherwise}. \end{cases}$$

In this example, $\sin(\pi x)$ also vanishes at $x = -10$ and $x = 10$, so the wave function joins continuously to zero at the boundaries. Thus, whether a particular functional form is normalisable depends not only on the function itself, but also on the domain over which it describes the particle.

Consider $g(x) = 4 - |x|$. This function is continuous and single-valued. It becomes negative for $|x| > 4$, but this is not a problem: a wave function is allowed to take negative values.

Its squared magnitude is $|g(x)|^2 = (4 - |x|)^2$. At large $|x|$, the magnitude of the function increases rather than decreases. In fact, $|g(x)|^2 \sim x^2$ as $|x| \to \infty$. For example, considering only the region $x > 4$,

$$\int_{4}^{\infty} |g(x)|^2 dx = \int_{4}^{\infty} (4 - x)^2 dx = \int_{4}^{\infty} (x - 4)^2 dx = \infty$$

Therefore, $g(x) = 4 - |x|$ is not normalisable. Notice that $g(x)$ has a cusp at $x = 0$, so its first derivative changes abruptly there. This does not by itself make the function unacceptable. The decisive problem here is that the function grows in magnitude as $|x| \to \infty$, and therefore cannot be normalised.

We are given $h^2(x) = 5x$. Formally, this means that $h(x)$ is a square root of $5x$. As written, the equation does not uniquely specify which square-root branch should be chosen. However, irrespective of the choice of branch, $|h(x)|^2 = |h^2(x)| = |5x| = 5|x|$. The normalisation integral would therefore contain $\int_{-\infty}^{\infty} 5|x| dx$, which diverges. For example, $\int_{0}^{\infty} 5x dx = \infty$. Hence, $h^2(x) = 5x$ does not give a normalisable wave function. The essential problem is again the behaviour at large $|x|$: the magnitude of the corresponding wave function increases instead of decreasing, so the total probability cannot be finite.

Finally, consider $e(x) = x^2$. This function is continuous, finite at every finite value of $x$, and single-valued. However, $|e(x)|^2 = x^4$. The normalisation integral is therefore $\int_{-\infty}^{\infty} |e(x)|^2 dx = \int_{-\infty}^{\infty} x^4 dx$, which diverges. Thus, $e(x) = x^2$ is not normalisable. This illustrates that being smooth, continuous and finite at every finite position is not sufficient. For a particle moving over the whole real line, the wave function must also decrease sufficiently rapidly as $|x| \to \infty$.

#### Summary

| Function | Acceptable on $(-\infty, \infty)$? | Main reason |
| :--- | :--- | :--- |
| $3\sin(\pi x)$ | No | Does not decay at infinity |
| $4 - \vert x\vert$ | No | Grows in magnitude at infinity |
| $h^2(x) = 5x$ | No | Not normalisable |
| $x^2$ | No | Grows at infinity |

The important point is that negative values of a wave function are perfectly acceptable. In all four examples, the decisive issue is normalisability over the specified domain.