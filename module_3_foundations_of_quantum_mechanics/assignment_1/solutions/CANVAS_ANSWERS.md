# Assessment 1 (PRB) — Canvas submission helper

Two sections:

- **Part A — pointer lines.** Use these if you submit the PDF (recommended). Paste one line into each Canvas question box so no marker meets an empty box.
- **Part B — full answers per Canvas question.** Use these only if you decide to answer inside Canvas instead of uploading the PDF, or if Overleaf fails on the day.

## How the two numbering schemes line up

Canvas asks 13 separate questions; your professor's LaTeX template groups the same 13 into 5. The mark totals agree (8 + 37 + 22 + 8 + 25 = 100).

| Canvas question | Marks | PDF template | Topic |
| :--- | :--- | :--- | :--- |
| Q1 | 8 | Question 1 | Hermitian matrix |
| Q2 | 7 | Question 2 (a) | Probability density + sketch |
| Q3 | 10 | Question 2 (b) | Normalisation constant |
| Q4 | 15 | Question 2 (c) | Average position |
| Q5 | 5 | Question 2 (d) | Most likely position |
| Q6 | 2 | Question 3 (a) | $\hat{x}\hat{p}\varphi$ |
| Q7 | 5 | Question 3 (b) | $\hat{p}\hat{x}\varphi$ |
| Q8 | 5 | Question 3 (c) | Difference, for $\varphi$ |
| Q9 | 10 | Question 3 (d) | Difference, general $\psi$ |
| Q10 | 8 | Question 4 | Born rule, un-normalised state |
| Q11 | 10 | Question 5 (a) | Energy measurement |
| Q12 | 10 | Question 5 (b) | Measuring $A$ |
| Q13 | 5 | Question 5 (c) | Collapse, then $A$ |
| Q14 | 0 | — | PDF upload slot |

---

# Part A — pointer lines for the PDF route

The PDF carries this mapping itself: a Canvas range in every section heading (e.g. "Question 2 (Canvas questions 2–5)") and a `(Canvas Qn)` tag on every sub-part heading. A marker landing on any Canvas question can therefore find the matching workings without doing the arithmetic themselves.

Fill in the page numbers after you compile, or delete the page reference and keep the section reference only. Type these in one sitting, in a single browser tab, then upload the PDF at Q14 and press **Submit**.

- **Q1:** Full solution and workings are in the uploaded PDF (Question 14), section "Question 1", p. \_\_.
- **Q2:** See uploaded PDF (Question 14), section "Question 2", part (a), p. \_\_. The sketch is Figure 1.
- **Q3:** See uploaded PDF (Question 14), section "Question 2", part (b), p. \_\_.
- **Q4:** See uploaded PDF (Question 14), section "Question 2", part (c), p. \_\_. The average position is marked on Figure 1.
- **Q5:** See uploaded PDF (Question 14), section "Question 2", part (d), p. \_\_. The most likely position is marked on Figure 1.
- **Q6:** See uploaded PDF (Question 14), section "Question 3", part (a), p. \_\_.
- **Q7:** See uploaded PDF (Question 14), section "Question 3", part (b), p. \_\_.
- **Q8:** See uploaded PDF (Question 14), section "Question 3", part (c), p. \_\_.
- **Q9:** See uploaded PDF (Question 14), section "Question 3", part (d), p. \_\_.
- **Q10:** See uploaded PDF (Question 14), section "Question 4", p. \_\_.
- **Q11:** See uploaded PDF (Question 14), section "Question 5", part (a), p. \_\_.
- **Q12:** See uploaded PDF (Question 14), section "Question 5", part (b), p. \_\_.
- **Q13:** See uploaded PDF (Question 14), section "Question 5", part (c), p. \_\_.
- **Q14:** Upload `QT01_PRB_solutions.pdf` here.

If you prefer, you can also paste the short **Answer** line from Part B into each box alongside the pointer, so the marker sees the result immediately. The workings still live in the PDF.

---

# Part B — full answers, per Canvas question

Each block is self-contained. In the Canvas rich content editor, type the prose directly and insert each displayed formula with the equation editor (the LaTeX between the `$$` delimiters goes into the editor's LaTeX box).

---

## Q1 (8 marks) — Prove $\hat{A}$ is Hermitian

An operator is Hermitian when it equals its own adjoint, $\hat{A} = \hat{A}^{\dagger}$; this is the condition for an operator to represent an observable. For a matrix, the adjoint is the transpose with every entry complex conjugated, $\hat{A}^{\dagger} = (\hat{A}^{\mathsf{T}})^{*}$.

**Step 1 — transpose** (reflect the entries about the leading diagonal):

$$\hat{A}^{\mathsf{T}} = \begin{pmatrix} -3 & 2i \\ -2i & -3 \end{pmatrix}^{\mathsf{T}} = \begin{pmatrix} -3 & -2i \\ 2i & -3 \end{pmatrix}$$

**Step 2 — complex conjugate** (replace $i$ by $-i$ everywhere):

$$\hat{A}^{\dagger} = \begin{pmatrix} -3 & -2i \\ 2i & -3 \end{pmatrix}^{*} = \begin{pmatrix} -3 & 2i \\ -2i & -3 \end{pmatrix}$$

**Step 3 — compare.** This is entry-by-entry identical to $\hat{A}$, so $\hat{A}^{\dagger} = \hat{A}$ and the operator is Hermitian.

Equivalently, in components the condition $A_{ij} = A_{ji}^{*}$ holds: both diagonal entries are real ($-3 = -3^{*}$), and the off-diagonal entries are conjugate partners, since $A_{12} = 2i$ and $A_{21}^{*} = (-2i)^{*} = 2i$.

**Check — the eigenvalues must be real.** The characteristic equation is

$$\det(\hat{A} - \lambda I) = (-3-\lambda)^{2} - (2i)(-2i) = (\lambda+3)^{2} - 4 = 0$$

using $(2i)(-2i) = -4i^{2} = 4$. Hence $\lambda + 3 = \pm 2$, giving $\lambda_{1} = -1$ and $\lambda_{2} = -5$. Both are real, as Hermiticity requires. The corresponding eigenvectors are

$$|\lambda_{1}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} i \\ 1 \end{pmatrix}, \qquad |\lambda_{2}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} -i \\ 1 \end{pmatrix}$$

and they are orthogonal, since $\langle \lambda_{1} | \lambda_{2}\rangle = \tfrac{1}{2}[(-i)(-i) + 1] = \tfrac{1}{2}(i^{2}+1) = 0$, which is the second property guaranteed for a Hermitian operator.

**Answer.** $\hat{A}^{\dagger} = \hat{A}$, so $\hat{A}$ is Hermitian; its eigenvalues $-1$ and $-5$ are real and its eigenvectors are orthogonal.

---

## Q2 (7 marks) — Probability density and sketch

The measurable quantity is the probability density, the modulus square of the wave function, so that $\rho(x)\,dx$ is the probability of finding the particle between $x$ and $x + dx$:

$$\rho(x) = |\psi(x)|^{2} = \psi^{*}(x)\psi(x)$$

The exponentials are real, so squaring affects only the constant $B$, and each exponent doubles:

$$|\psi(x)|^{2} = \begin{cases} |B|^{2}\exp(2\beta x) & x < 0 \\ |B|^{2}\exp(-4\beta x) & x \ge 0 \end{cases}$$

The sketch must show three features:

1. **It is continuous at the origin and peaks there.** $\rho(0^{-}) = \rho(0^{+}) = |B|^{2}$, so the branches join. Since $\beta > 0$, the left branch rises towards $x=0$ and the right branch falls away from it.
2. **It decays to zero both ways**, since $e^{2\beta x} \to 0$ as $x \to -\infty$ and $e^{-4\beta x} \to 0$ as $x \to +\infty$. This is what makes it normalisable.
3. **It is asymmetric.** The density falls by a factor $e$ over a distance $1/(2\beta)$ on the left but only $1/(4\beta)$ on the right, so it is spread twice as far to the left.

A fourth point matters later: the slopes at the origin are $2\beta|B|^{2}$ from the left and $-4\beta|B|^{2}$ from the right. They differ, so the peak is a sharp cusp, not a smooth turning point.

**Answer.** $|\psi(x)|^{2} = |B|^{2}e^{2\beta x}$ for $x<0$ and $|B|^{2}e^{-4\beta x}$ for $x \ge 0$: an asymmetric, cusped peak at the origin decaying to zero in both directions, twice as extended to the left as to the right.

> **Sketch:** upload `figures/psi_probability_density.png` into this answer box using the image button in the Canvas editor.

---

## Q3 (10 marks) — Normalisation constant $B$

The particle must be somewhere, so the total probability is one:

$$\int_{-\infty}^{\infty} |\psi(x)|^{2}\,dx = 1$$

The wave function is defined piecewise, so the integral splits at $x = 0$:

$$|B|^{2}\int_{-\infty}^{0} e^{2\beta x}\,dx + |B|^{2}\int_{0}^{\infty} e^{-4\beta x}\,dx = 1$$

Both integrals are elementary, each exponential vanishing at the infinite limit because $\beta > 0$:

$$\int_{-\infty}^{0} e^{2\beta x}\,dx = \left[\frac{e^{2\beta x}}{2\beta}\right]_{-\infty}^{0} = \frac{1}{2\beta}, \qquad \int_{0}^{\infty} e^{-4\beta x}\,dx = \left[-\frac{e^{-4\beta x}}{4\beta}\right]_{0}^{\infty} = \frac{1}{4\beta}$$

Adding them:

$$|B|^{2}\left(\frac{1}{2\beta} + \frac{1}{4\beta}\right) = \frac{3|B|^{2}}{4\beta} = 1 \quad \Longrightarrow \quad |B|^{2} = \frac{4\beta}{3}$$

Only the modulus is fixed, since multiplying $\psi$ by a phase $e^{i\theta}$ leaves $|\psi|^{2}$ and every prediction unchanged. Taking that free phase to be zero:

$$B = \sqrt{\frac{4\beta}{3}} = 2\sqrt{\frac{\beta}{3}}$$

**Check — dimensions.** $\beta x$ must be dimensionless, so $\beta \sim (\text{length})^{-1}$ and $B \sim (\text{length})^{-1/2}$, which is correct for a 1D wave function because $|\psi|^{2}dx$ must be a pure number.

**Answer.** $|B|^{2} = 4\beta/3$, so $B = 2\sqrt{\beta/3}$ taking the phase to be zero. The peak density is $|\psi(0)|^{2} = 4\beta/3$.

---

## Q4 (15 marks) — Average position

The expectation value of position in a normalised state, with $\hat{x}$ acting by multiplication, is

$$\langle \hat{x}\rangle = \int_{-\infty}^{\infty} \psi^{*}(x)\,\hat{x}\,\psi(x)\,dx = \int_{-\infty}^{\infty} x\,|\psi(x)|^{2}\,dx$$

This is the ordinary mean of a distribution with $|\psi|^{2}$ as the density. It is valid without dividing by $\langle\psi|\psi\rangle$ because $B$ was chosen in Q3 to normalise the state. Splitting at the origin:

$$\langle \hat{x}\rangle = |B|^{2}\underbrace{\int_{-\infty}^{0} x\,e^{2\beta x}\,dx}_{I_{-}} + |B|^{2}\underbrace{\int_{0}^{\infty} x\,e^{-4\beta x}\,dx}_{I_{+}}$$

**Using the hint.** A factor of $x$ is generated by differentiating with respect to the exponent, since $\partial e^{\gamma x}/\partial\gamma = x e^{\gamma x}$.

For the left integral, with $\gamma > 0$ for convergence:

$$F(\gamma) = \int_{-\infty}^{0} e^{\gamma x}\,dx = \frac{1}{\gamma} \quad \Longrightarrow \quad \int_{-\infty}^{0} x\,e^{\gamma x}\,dx = \frac{\partial}{\partial\gamma}\frac{1}{\gamma} = -\frac{1}{\gamma^{2}}$$

Setting $\gamma = 2\beta$ gives $I_{-} = -1/(4\beta^{2})$.

For the right integral, with $\gamma < 0$ for convergence:

$$G(\gamma) = \int_{0}^{\infty} e^{\gamma x}\,dx = -\frac{1}{\gamma} \quad \Longrightarrow \quad \int_{0}^{\infty} x\,e^{\gamma x}\,dx = \frac{\partial}{\partial\gamma}\left(-\frac{1}{\gamma}\right) = \frac{1}{\gamma^{2}}$$

Setting $\gamma = -4\beta$ gives $I_{+} = 1/(16\beta^{2})$.

**Combining**, the two contributions have opposite signs and do not cancel:

$$I_{-} + I_{+} = -\frac{1}{4\beta^{2}} + \frac{1}{16\beta^{2}} = \frac{-4+1}{16\beta^{2}} = -\frac{3}{16\beta^{2}}$$

$$\langle \hat{x}\rangle = \frac{4\beta}{3}\times\left(-\frac{3}{16\beta^{2}}\right) = -\frac{1}{4\beta}$$

**Check 1 — by parts.** $I_{+} = \left[-\frac{xe^{-4\beta x}}{4\beta}\right]_{0}^{\infty} + \frac{1}{4\beta}\int_{0}^{\infty}e^{-4\beta x}dx = 0 + \frac{1}{16\beta^{2}}$, the boundary term vanishing because the exponential beats the linear growth. Substituting $x = -u$ in $I_{-}$ gives $-\int_{0}^{\infty}ue^{-2\beta u}du = -1/(4\beta^{2})$. Both agree.

**Check 2 — sign and size.** The result is negative, as the sketch demands: the density extends twice as far to the left, so the mean is pulled left of the peak. Its magnitude $1/(4\beta)$ is smaller than the left decay length $1/(2\beta)$, as it must be. And $1/\beta$ has dimensions of length.

**Answer.** $\langle x \rangle = -\dfrac{1}{4\beta}$, marked on the sketch by a vertical line at $\beta x = -0.25$, to the left of the peak.

---

## Q5 (5 marks) — Most likely position

The most likely position is where the probability density is largest, i.e. the mode of $\rho(x) = |\psi(x)|^{2}$.

Setting $d\rho/dx = 0$ does **not** work here, and it is worth saying why:

$$\frac{d\rho}{dx} = \begin{cases} 2\beta|B|^{2}e^{2\beta x} > 0 & x < 0 \\ -4\beta|B|^{2}e^{-4\beta x} < 0 & x > 0 \end{cases}$$

Neither expression ever vanishes, because an exponential is never zero at finite argument and $\beta > 0$. There is no stationary point anywhere.

The maximum is found instead by monotonicity: $\rho$ increases strictly throughout $x < 0$ and decreases strictly throughout $x > 0$, so its greatest value is at the join,

$$x_{\text{max}} = 0, \qquad \rho(0) = |B|^{2} = \frac{4\beta}{3}$$

Since the one-sided slopes differ ($2\beta|B|^{2}$ against $-4\beta|B|^{2}$), the curve turns over in a sharp cusp rather than a smooth arch.

**Answer.** The most likely position is $x = 0$, where $|\psi(0)|^{2} = 4\beta/3$ is greatest; it is a cusp, marked on the sketch at the apex. Note it differs from the average position $-1/(4\beta)$, because the distribution is asymmetric.

---

## Q6 (2 marks) — $\left[x\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)\right]\phi(x)$

Here the derivative acts on $\phi$ first, and the result is then multiplied by $x$. Using $1/i = -i$, this operator is $\hat{x}\hat{p}$. Differentiating,

$$\frac{\partial \phi}{\partial x} = \frac{\partial}{\partial x}\big(N\sin(kx)\big) = Nk\cos(kx)$$

so

$$\left[x\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)\right]\phi(x) = x \cdot \frac{\hbar}{i} Nk\cos(kx) = -i\hbar Nkx\cos(kx)$$

**Answer.** $-i\hbar N k x\cos(kx)$.

---

## Q7 (5 marks) — $\left[\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)x\right]\phi(x)$

Now the multiplication by $x$ happens first, so the derivative acts on the product $x\phi(x)$ and the product rule is needed:

$$\frac{\partial}{\partial x}\big(x\,\phi(x)\big) = \phi(x) + x\frac{\partial \phi}{\partial x} = N\sin(kx) + Nkx\cos(kx)$$

Multiplying by the prefactor $\hbar/i = -i\hbar$:

$$\left[\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)x\right]\phi(x) = -i\hbar N\sin(kx) - i\hbar Nkx\cos(kx)$$

The second term reproduces Q6; the first is new, and is precisely the term generated by the product rule.

**Answer.** $-i\hbar N\sin(kx) - i\hbar N k x\cos(kx)$.

---

## Q8 (5 marks) — The difference, for $\phi(x)$

Subtracting the Q7 result from the Q6 result, the $x\cos(kx)$ terms are identical and cancel:

$$\begin{aligned} \text{(Q6)} - \text{(Q7)} &= -i\hbar Nkx\cos(kx) - \big(-i\hbar N\sin(kx) - i\hbar Nkx\cos(kx)\big) \\ &= -i\hbar Nkx\cos(kx) + i\hbar N\sin(kx) + i\hbar Nkx\cos(kx) \\ &= i\hbar N\sin(kx) \end{aligned}$$

Since $\phi(x) = N\sin(kx)$, the difference is the original wave function multiplied by a constant:

$$\text{(Q6)} - \text{(Q7)} = i\hbar\,\phi(x)$$

Note that the answer depends on neither $k$ nor $N$.

**Answer.** $i\hbar N\sin(kx) = i\hbar\,\phi(x)$.

---

## Q9 (10 marks) — The difference, for a general $\psi(x)$

Q8 used one particular wave function. If the same result holds for any $\psi$, it is a statement about the operators themselves rather than about the state, which is a much stronger conclusion. Let $\psi(x)$ be any differentiable wave function.

First term — derivative, then multiply by $x$:

$$\left[x\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)\right]\psi(x) = \frac{\hbar}{i}\,x\frac{\partial \psi}{\partial x}$$

Second term — multiply by $x$, then differentiate, which needs the product rule:

$$\left[\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)x\right]\psi(x) = \frac{\hbar}{i}\frac{\partial}{\partial x}\big(x\psi(x)\big) = \frac{\hbar}{i}\left(\psi(x) + x\frac{\partial \psi}{\partial x}\right)$$

Subtracting, the terms in $x\,\partial\psi/\partial x$ cancel:

$$\frac{\hbar}{i}\left(x\frac{\partial \psi}{\partial x} - \psi(x) - x\frac{\partial \psi}{\partial x}\right) = -\frac{\hbar}{i}\psi(x) = i\hbar\,\psi(x)$$

using $-1/i = i$. Because $\psi$ was arbitrary, this is an identity between operators:

$$[\hat{x},\hat{p}]\,\psi(x) = (\hat{x}\hat{p} - \hat{p}\hat{x})\,\psi(x) = i\hbar\,\psi(x) \quad \Longrightarrow \quad [\hat{x},\hat{p}] = i\hbar$$

This is the canonical commutation relation between position and momentum.

**Checks.** Putting $\psi = \phi = N\sin(kx)$ recovers the Q8 answer $i\hbar\phi(x)$, so the general and special cases agree. Dimensionally, the commutator of a position with a momentum is an action, and $\hbar$ is an action.

**Answer.** $i\hbar\,\psi(x)$ for any $\psi$, i.e. the operator identity $[\hat{x},\hat{p}] = i\hbar$. Position and momentum do not commute, so they share no eigenstates and cannot both be sharp; this is the origin of $\Delta x\,\Delta p \ge \hbar/2$.

---

## Q10 (8 marks) — Probability of measuring $a_{3}$

For a **normalised** state expanded in orthonormal eigenstates of the observable, $|\psi\rangle = \sum_{n}\alpha_{n}|\phi_{n}\rangle$, the Born rule gives $P(a_{n}) = |\langle \phi_{n}|\psi\rangle|^{2} = |\alpha_{n}|^{2}$. The normalisation requirement is essential, so check it first.

**Step 1 — is the state normalised?** Using orthonormality $\langle\phi_{m}|\phi_{n}\rangle = \delta_{mn}$, all cross terms vanish and

$$\langle \psi | \psi \rangle = \left|\frac{1}{\sqrt{3}}\right|^{2} + \left|-\frac{\sqrt{2}}{\sqrt{3}}\right|^{2} + \left|\frac{i}{\sqrt{3}}\right|^{2} = \frac{1}{3} + \frac{2}{3} + \frac{1}{3} = \frac{4}{3} \neq 1$$

The modulus square removes both the minus sign and the factor $i$, since $|-z|^{2} = |z|^{2}$ and $|i|^{2} = 1$. The state is **not** normalised, so the Born rule cannot be applied as it stands.

**Step 2 — account for it.** For an un-normalised state,

$$P(a_{3}) = \frac{|\langle \phi_{3}|\psi\rangle|^{2}}{\langle \psi|\psi\rangle}$$

Orthonormality leaves only the third term in the overlap, $\langle\phi_{3}|\psi\rangle = i/\sqrt{3}$, so $|\langle\phi_{3}|\psi\rangle|^{2} = 1/3$ and

$$P(a_{3}) = \frac{1/3}{4/3} = \frac{1}{4}$$

Equivalently, normalise first: dividing by $\sqrt{4/3} = 2/\sqrt{3}$ gives $|\psi_{\text{norm}}\rangle = \tfrac{1}{2}|\phi_{1}\rangle - \tfrac{\sqrt{2}}{2}|\phi_{2}\rangle + \tfrac{i}{2}|\phi_{3}\rangle$, whose coefficients square to $\tfrac14 + \tfrac12 + \tfrac14 = 1$, and then $P(a_{3}) = |i/2|^{2} = 1/4$.

**Check.** $P(a_{1}) = 1/4$, $P(a_{2}) = 1/2$, $P(a_{3}) = 1/4$, summing to $1$ as exclusive probabilities must. Skipping the normalisation step would have given a total of $4/3$, which is impossible.

**Answer.** $P(a_{3}) = \dfrac{1}{4}$, i.e. 25%.

---

## Q11 (10 marks) — Measuring the energy

**First, check normalisation**, since the Born rule requires it. Using orthonormality,

$$\langle \psi_{0}|\psi_{0}\rangle = \frac{2}{7} + \frac{3}{7} + \frac{1}{7} + \frac{1}{7} = 1$$

The state is already normalised, so no rescaling is needed.

**Possible outcomes.** A measurement can only return an eigenvalue of the corresponding operator. Given $\hat{H}|\phi_{n}\rangle = n^{2}E_{0}|\phi_{n}\rangle$, the energies are $E_{n} = n^{2}E_{0}$, and only $n = 1,2,3,4$ appear in $|\psi_{0}\rangle$ (all other coefficients are zero):

$$E_{1} = E_{0}, \qquad E_{2} = 4E_{0}, \qquad E_{3} = 9E_{0}, \qquad E_{4} = 16E_{0}$$

**Probabilities.** By the Born rule, $P(E_{n}) = |\alpha_{n}|^{2}$:

| Energy | $E_{0}$ | $4E_{0}$ | $9E_{0}$ | $16E_{0}$ |
| :--- | :--- | :--- | :--- | :--- |
| Probability | $2/7$ | $3/7$ | $1/7$ | $1/7$ |

**Check.** They sum to $7/7 = 1$, and each lies in $[0,1]$. Also $\langle \hat{H}\rangle = \frac{2(1)+3(4)+1(9)+1(16)}{7}E_{0} = \frac{39}{7}E_{0} \approx 5.6E_{0}$, which lies between the smallest and largest possible outcomes, as an average must.

**Answer.** $E_{0}$, $4E_{0}$, $9E_{0}$, $16E_{0}$ with probabilities $2/7$, $3/7$, $1/7$, $1/7$ respectively.

---

## Q12 (10 marks) — Measuring $A$

**The key observation.** $\hat{A}|\phi_{n}\rangle = (n+1)a_{0}|\phi_{n}\rangle$ says the $|\phi_{n}\rangle$ are eigenstates of $\hat{A}$ as well as of $\hat{H}$. The state is therefore *already* expanded in the eigenbasis of $\hat{A}$: no change of basis is needed, the expansion coefficients are unchanged, and only the list of eigenvalues differs.

**Possible outcomes.** For $n = 1,2,3,4$:

$$a_{1} = 2a_{0}, \qquad a_{2} = 3a_{0}, \qquad a_{3} = 4a_{0}, \qquad a_{4} = 5a_{0}$$

**Probabilities.** The outcome $(n+1)a_{0}$ occurs exactly when the system is found in $|\phi_{n}\rangle$, so each probability is again $|\alpha_{n}|^{2}$:

| Value of $A$ | $2a_{0}$ | $3a_{0}$ | $4a_{0}$ | $5a_{0}$ |
| :--- | :--- | :--- | :--- | :--- |
| Probability | $2/7$ | $3/7$ | $1/7$ | $1/7$ |

**Check.** They sum to 1, and $\langle \hat{A}\rangle = \frac{2(2)+3(3)+1(4)+1(5)}{7}a_{0} = \frac{22}{7}a_{0} \approx 3.1a_{0}$, lying between $2a_{0}$ and $5a_{0}$ as required.

**Answer.** $2a_{0}$, $3a_{0}$, $4a_{0}$, $5a_{0}$ with probabilities $2/7$, $3/7$, $1/7$, $1/7$ — the same probabilities as the energy measurement, because $\hat{H}$ and $\hat{A}$ share eigenstates.

---

## Q13 (5 marks) — Measuring $A$ immediately after obtaining $4E_{0}$

**Step 1 — identify the state.** The measured energy must be an eigenvalue, so

$$n^{2}E_{0} = 4E_{0} \quad \Longrightarrow \quad n^{2} = 4 \quad \Longrightarrow \quad n = 2$$

rejecting the negative root because the states are labelled $n = 1,2,3,\dots$. No other $n$ gives this energy, so the outcome identifies the eigenstate uniquely — the spectrum is non-degenerate here.

**Step 2 — collapse.** Immediately after a measurement yielding a given eigenvalue, the system is left in the corresponding normalised eigenstate. The superposition is destroyed:

$$|\psi_{0}\rangle \; \longrightarrow \; |\phi_{2}\rangle$$

**Step 3 — measure $A$.** Acting on the collapsed state,

$$\hat{A}|\phi_{2}\rangle = (2+1)a_{0}|\phi_{2}\rangle = 3a_{0}|\phi_{2}\rangle$$

so $|\phi_{2}\rangle$ is an eigenstate of $\hat{A}$ with eigenvalue $3a_{0}$. The expansion now has the single term $|\phi_{2}\rangle$ with coefficient 1, so $P(3a_{0}) = 1$ and every other outcome has probability zero.

**Check.** This is consistent with Q12: $3a_{0}$ was the value associated with $|\phi_{2}\rangle$ there. What has changed is not the list of possible values but their probabilities, which have gone from $(2/7, 3/7, 1/7, 1/7)$ to $(0,1,0,0)$.

**Answer.** $A = 3a_{0}$, with certainty. The energy measurement did not merely reveal a value, it prepared the system in $|\phi_{2}\rangle$; because $\hat{H}$ and $\hat{A}$ commute and share that eigenstate, the subsequent measurement of $A$ is fully determined.

---

## Q14 (0 marks)

Upload `QT01_PRB_solutions.pdf`.
