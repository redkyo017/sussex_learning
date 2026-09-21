# Week 3 Companion — Probabilistic Nature of Measurement

Built on [Day 2](../day02.md) (kets, bras, inner products, expansion), [Day 3](../day03.md) (eigenproblems, Hermitian, Pauli) and [Day 4](../day04.md) (integrals, acceptable wave functions). Reading protocol: [STRATEGY](../../STRATEGY.md). Lecture equation numbers below refer to `week_3_lecture.md`.

## What this week is really saying

Five plain-English claims carry the whole week.

1. **Every measurable quantity is a Hermitian operator $\hat{A}$, and the only numbers a measurement can ever return are its eigenvalues $\lambda_n$** (Postulate 3, Eq. 3.1). The operator is the menu of possible answers. It does not care what state you are in.
2. **The state decides the odds, not the answer.** Write the state in the eigenbasis of $\hat{A}$, $|\psi\rangle=\sum_n\alpha_n|\phi_n\rangle$. Then $P(\lambda_n)=|\alpha_n|^2=|\langle\phi_n|\psi\rangle|^2$ (Postulate 4, the Born rule, Eqs. 3.2 to 3.4). Identically prepared systems give different outcomes. Only the frequencies are predictable.
3. **After you get $\lambda_n$, the state is $|\phi_n\rangle$** (Postulate 5, collapse, Eq. 3.5). Measure again straight away and you get $\lambda_n$ with certainty. A system has a definite value of an observable only when it sits in an eigenstate of that observable.
4. **The expectation value $\langle\hat{A}\rangle_\psi$ is the average over many identical runs**, $\sum_n\lambda_n|\alpha_n|^2=\langle\psi|\hat{A}|\psi\rangle$ (Eqs. 3.9 and 3.10). It is generally not itself a possible outcome.
5. **The wave function is not "where the particle actually is".** It is an amplitude. For position, $|\psi(x)|^2$ is a probability *density*, so the probability of finding the particle in a tiny stretch $\mathrm{d}x$ is $|\psi|^2\,\mathrm{d}x$. Section 3.4 is the argument about what, if anything, is true *before* the measurement (realist, orthodox, agnostic). Those three positions are opinion and history. The postulates are the mathematics you must be able to use.

**Picture.** A die that is loaded differently for each state you prepare. The faces are the eigenvalues (fixed by $\hat{A}$). The loading is $|\alpha_n|^2$ (fixed by $|\psi\rangle$). Rolling the die is the measurement, and afterwards the die is glued onto the face it showed (collapse).

## Notation decoder

Convention notes. (i) The lecture uses $\lambda_n$, $|\phi_n\rangle$, $\alpha_n$; I keep them. (ii) The lecture text of Week 3 does not define $|u\rangle,|d\rangle$ or $\sigma_n$; they come from the Week 3 task and Day 3 (spin-up and spin-down as $\begin{pmatrix}1\\0\end{pmatrix}$, $\begin{pmatrix}0\\1\end{pmatrix}$). (iii) I use the dimensionless Pauli matrices with eigenvalues $\pm1$. The physical spin component is $\tfrac{\hbar}{2}$ times that. The lecture does not state this, so it is my convention. (iv) $\Delta A$ is not defined in Week 3 (uncertainty relations come later); I define it below because it clarifies "average" versus "spread".

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\hat{A}$ | "A hat" | Operator for observable $A$; a matrix in a finite basis. Hermitian (Postulate 2). | $\hat{A}=\begin{pmatrix}2&0\\0&5\end{pmatrix}$ |
| $\lambda_n$ | "lambda n" | The $n$th eigenvalue of $\hat{A}$: a possible measurement outcome | Above: $\lambda_1=2$, $\lambda_2=5$ |
| $\lvert\phi_n\rangle$ | "ket phi n" | Eigenstate (eigenvector) belonging to $\lambda_n$: $\hat{A}\lvert\phi_n\rangle=\lambda_n\lvert\phi_n\rangle$ (Eq. 3.1) | Above: $\lvert\phi_1\rangle=\begin{pmatrix}1\\0\end{pmatrix}$ |
| $\alpha_n$ | "alpha n" | Expansion coefficient of $\lvert\psi\rangle$ along $\lvert\phi_n\rangle$; $\alpha_n=\langle\phi_n\lvert\psi\rangle$ | $\lvert\psi\rangle=\tfrac{3}{5}\lvert\phi_1\rangle+\tfrac{4}{5}\lvert\phi_2\rangle$ gives $\alpha_1=\tfrac35$ |
| $\langle\phi_n\lvert\psi\rangle$ | "bra phi n, ket psi" | Overlap (inner product); conjugate the left object first | Complex in general |
| $P(\lambda_n)$ | "probability of lambda n" | Chance of getting outcome $\lambda_n$: $\lvert\alpha_n\rvert^2$ (Eq. 3.4) | $\tfrac{9}{25}$ in the example above |
| $\delta_{ni}$ | "Kronecker delta" | 1 if $n=i$, else 0; encodes orthonormality $\langle\phi_n\lvert\phi_i\rangle=\delta_{ni}$ | $\delta_{23}=0$, $\delta_{22}=1$ |
| $\sum_n$ | "sum over n" | Add up the term for every eigenstate | $\sum_n\lvert\alpha_n\rvert^2=1$ |
| $\langle\hat{A}\rangle_\psi$ | "expectation of A in state psi" | Average outcome over many identical runs. The subscript says it depends on the state. | Mean of many dice rolls |
| $\langle\psi\lvert\hat{A}\lvert\psi\rangle$ | "psi, A, psi" | Same thing as one inner product (Eq. 3.10). Divide by $\langle\psi\lvert\psi\rangle$ if not normalised (Eq. 3.11). | See worked clones |
| $\Delta A$ | "delta A", spread | $\sqrt{\langle\hat{A}^2\rangle-\langle\hat{A}\rangle^2}$: typical scatter of outcomes. Zero exactly in an eigenstate. | Eigenstate: every run gives $\lambda_n$, so $\Delta A=0$ |
| Hermitian | "Hermitian" | $\hat{A}^\dagger=\hat{A}$; guarantees real eigenvalues and orthogonal eigenstates | $\begin{pmatrix}1&i\\-i&1\end{pmatrix}$ |
| $\lvert u\rangle,\lvert d\rangle$ | "up, down" | Spin-up and spin-down basis kets, the eigenstates of $\sigma_z$ | $\lvert u\rangle=\begin{pmatrix}1\\0\end{pmatrix}$ |
| $\sigma_n$ | "sigma n" | A spin operator for the direction labelled $n$; a 2×2 Hermitian matrix with eigenvalues $\pm1$ in my convention | $\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ |
| $\hat{x}$ | "x hat" | Position operator: multiply the wave function by $x$ | $\hat{x}\psi=x\psi(x)$ |
| $\hat{p}$ | "p hat" | Momentum operator $\tfrac{\hbar}{i}\tfrac{\partial}{\partial x}$ | $\hat{p}\,e^{ikx}=\hbar k\,e^{ikx}$ |
| $\hbar$ | "h-bar" | Reduced Planck constant; sets the scale of momentum, spin and energy | Spin component $\pm\hbar/2$ |
| $\psi^*$ | "psi star" | Complex conjugate of the wave function | $(3+i)^*=3-i$ |
| $\mathrm{d}^3\mathbf{r}$ | "d-three-r" | Volume element: integrate over all of 3D space | Region of volume $\Delta V$: $\int\approx(\cdot)\Delta V$ |
| $\lvert\psi\rangle\to\lvert\phi_n\rangle$ | "collapses to" | State just after outcome $\lambda_n$ (Eq. 3.5) | Get $-1$: state is $\lvert d\rangle$ |

## Skipped steps, expanded

### A. Why $P(\lambda_n)=|\alpha_n|^2$ (Eqs. 3.2 to 3.4)

Eq. 3.4 compresses the chain from $|\langle\phi_n|\psi\rangle|^2$ through $\left|\sum_i\alpha_i\langle\phi_n|\phi_i\rangle\right|^2$ to $|\alpha_n|^2$ into a single displayed line, with the middle step unexplained. Here it is slowly.

1. Expand: $|\psi\rangle=\sum_i\alpha_i|\phi_i\rangle$ ([Move 2.4](../day02.md)). Dummy index $i$, so it does not clash with the fixed $n$.
2. Take the inner product with $|\phi_n\rangle$. The inner product is linear in the ket ([Move 2.3](../day02.md)), so the sum comes out: $\langle\phi_n|\psi\rangle=\sum_i\alpha_i\langle\phi_n|\phi_i\rangle$.
3. Orthonormality: $\langle\phi_n|\phi_i\rangle=\delta_{ni}$. Every term is zero except $i=n$, so $\langle\phi_n|\psi\rangle=\alpha_n$. This is also the recipe for finding any coefficient: $\alpha_n=\langle\phi_n|\psi\rangle$.
4. Square the modulus: $P(\lambda_n)=|\alpha_n|^2$.
5. Why the probabilities add to 1: $1=\langle\psi|\psi\rangle=\sum_n\sum_i\alpha_n^*\alpha_i\delta_{ni}=\sum_n|\alpha_n|^2$. Normalisation of the state is exactly "the probabilities sum to 1". If your state is not normalised, divide by $\langle\psi|\psi\rangle$ first.

The lecture says "assuming the spectrum is non-degenerate". With a repeated eigenvalue you add $|\alpha|^2$ over every eigenstate that shares it.

### B. Why $\langle\hat{A}\rangle=\sum_n\lambda_n|\alpha_n|^2=\langle\psi|\hat{A}|\psi\rangle$ (Eqs. 3.9 and 3.10)

*First equality (the average).* This is the ordinary definition of an average: each value times its probability, $\sum_n\lambda_nP(\lambda_n)$, with $P(\lambda_n)=|\alpha_n|^2$ from part A.

*Second equality (the inner-product form).* The lecture's block of integrals with $\mathrm{d}^3\mathbf{r}$ does the same job as this shorter bra-ket calculation:

1. Bra of the sum: $\langle\psi|=\sum_n\alpha_n^*\langle\phi_n|$. The coefficients get conjugated (bra rule, [Move 2.2](../day02.md)), which is why the lecture writes $\left(\sum_n\alpha_n^*\phi_n^*\right)$.
2. Operator on the ket: $\hat{A}|\psi\rangle=\sum_m\alpha_m\hat{A}|\phi_m\rangle=\sum_m\alpha_m\lambda_m|\phi_m\rangle$. The first step uses that $\hat{A}$ is linear; the second uses the eigenvalue equation. This is the underbrace $\hat{A}\phi_m=\lambda_m\phi_m$ in the lecture.
3. Combine: $\langle\psi|\hat{A}|\psi\rangle=\sum_n\sum_m\alpha_n^*\alpha_m\lambda_m\langle\phi_n|\phi_m\rangle$. The numbers $\alpha^*_n,\alpha_m,\lambda_m$ are constants and slide out of the integral. What is left is the orthonormality integral $\int\phi_n^*\phi_m\,\mathrm{d}^3\mathbf{r}=\delta_{nm}$ (the last underbrace).
4. The delta kills every term except $m=n$: $\sum_n|\alpha_n|^2\lambda_n$. Done.

*Eq. 3.11 (un-normalised state).* Replace $\psi$ by $c\psi$ with $c$ any complex constant. The numerator $\langle\psi|\hat{A}|\psi\rangle$ gets multiplied by $|c|^2$, and so does the denominator $\langle\psi|\psi\rangle$. The $|c|^2$ cancels, so dividing by $\langle\psi|\psi\rangle$ always gives the right average whatever the scale.

*Spread.* $\Delta A$ measures how far outcomes scatter around the average. In an eigenstate $\langle\hat{A}^2\rangle=\lambda_n^2=\langle\hat{A}\rangle^2$, so $\Delta A=0$. That is the mathematical content of "a definite value only in an eigenstate" (Section 3.3).

### C. Why Hermitian implies real eigenvalues and orthogonal eigenstates

The lecture uses this silently: Postulate 2 says observables are Hermitian, and Postulate 4 needs real outcomes and *orthonormal* eigenstates. The proof is four lines. Use the adjoint rule $\langle\hat{A}\chi|\phi\rangle=\langle\chi|\hat{A}^\dagger\phi\rangle$ and $\hat{A}^\dagger=\hat{A}$.

*Real eigenvalues.* Let $\hat{A}|\phi\rangle=\lambda|\phi\rangle$ with $|\phi\rangle\ne0$.

1. $\langle\phi|\hat{A}\phi\rangle=\lambda\langle\phi|\phi\rangle$ (constant leaves the ket unchanged).
2. Hermitian: $\langle\phi|\hat{A}\phi\rangle=\langle\hat{A}\phi|\phi\rangle=\langle\lambda\phi|\phi\rangle=\lambda^*\langle\phi|\phi\rangle$. A constant leaving the *bra* side comes out conjugated.
3. Subtract: $(\lambda-\lambda^*)\langle\phi|\phi\rangle=0$. Since $\langle\phi|\phi\rangle>0$, $\lambda=\lambda^*$, so $\lambda$ is real.

*Orthogonal eigenstates.* Let $\hat{A}|\phi\rangle=\lambda|\phi\rangle$ and $\hat{A}|\chi\rangle=\mu|\chi\rangle$ with $\lambda\ne\mu$. Then $\langle\chi|\hat{A}\phi\rangle=\lambda\langle\chi|\phi\rangle$, and also $=\langle\hat{A}\chi|\phi\rangle=\mu^*\langle\chi|\phi\rangle=\mu\langle\chi|\phi\rangle$ (since $\mu$ is real). So $(\lambda-\mu)\langle\chi|\phi\rangle=0$ and the overlap is zero.

### D. The measure-A, measure-M, measure-A-again story (Section 3.3)

The lecture calls the steps $\beta_m$ and $\gamma_n$. Read it as three re-expansions, each with the same recipe from part A:

1. Measure $\hat{A}$, get $\lambda_6$. State is $|\phi_6\rangle$.
2. Re-expand $|\phi_6\rangle$ in the eigenbasis of $\hat{M}$: $\beta_m=\langle\chi_m|\phi_6\rangle$, $P(\mu_m)=|\beta_m|^2$.
3. Measure $\hat{M}$, get $\mu_{17}$. State is $|\chi_{17}\rangle$.
4. Re-expand in the $\hat{A}$ eigenbasis: $\gamma_n=\langle\phi_n|\chi_{17}\rangle$. Chance of $\lambda_6$ again is $|\gamma_6|^2$, usually below 1.

*Tiny numeric version.* Spin along $z$: measure $\sigma_z$ and get $+1$, so the state is $|u\rangle=\begin{pmatrix}1\\0\end{pmatrix}$. Now measure $\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$. Its $+1$ eigenvector is $\tfrac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$ (check: $\sigma_y\begin{pmatrix}1\\i\end{pmatrix}=\begin{pmatrix}-i\cdot i\\ i\cdot1\end{pmatrix}=\begin{pmatrix}1\\i\end{pmatrix}$). Overlap with $|u\rangle$: $\tfrac{1}{\sqrt2}(1\cdot1+(-i)\cdot0)=\tfrac{1}{\sqrt2}$, so $P(+1)=\tfrac12$; the other outcome also has $\tfrac12$. After the $\sigma_y$ result, a fresh $\sigma_z$ measurement gives $\pm1$ with 50% each. The earlier "definite $+1$" was destroyed. That is Section 3.3's "measurement is never innocent".

## Moves used this week

| Move | What for | Where taught |
|---|---|---|
| 2.2 Ket, bra, inner product | $\langle\phi_n\lvert\psi\rangle$, conjugate the left side | [Day 2](../day02.md) |
| 2.3 Inner-product axioms | Linearity in the ket pulls $\alpha_i$ out (part A) | [Day 2](../day02.md) |
| 2.4 Orthonormal basis and expansion | $\alpha_n=\langle\phi_n\lvert\psi\rangle$; $\sum\lvert\alpha_n\rvert^2=1$ | [Day 2](../day02.md) |
| 2.5 Matrix times vector | Acting with $\hat{A}$ on a ket | [Day 2](../day02.md) |
| 3.1 Operators as matrices | Read off what $\hat{A}$ does | [Day 3](../day03.md) |
| 3.2 Eigenvalue equation, 2×2 recipe | List of outcomes and eigenstates | [Day 3](../day03.md) |
| 3.3 Adjoint, Hermitian, real eigenvalues | Part C; Hermiticity proofs | [Day 3](../day03.md) |
| 3.4 Pauli matrices | Spin measurement examples | [Day 3](../day03.md) |
| 4.1 Functions as vectors | $\langle\phi\lvert\psi\rangle=\int\phi^*\psi\,\mathrm{d}x$ | [Day 4](../day04.md) |
| 4.2 Integrals | Normalisation and interval probabilities | [Day 4](../day04.md) |
| 4.3 Integration by parts | Hermiticity of derivative operators | [Day 4](../day04.md) |
| 4.4 Gaussians | Normalisability checks | [Day 4](../day04.md) |
| 4.5 Normalisation | Prerequisite for reading $\lvert\alpha_n\rvert^2$ as probability | [Day 4](../day04.md) |
| 4.6 Expectation, probability in an interval | Eqs. 3.9 to 3.11 | [Day 4](../day04.md) |
| 4.7 Acceptable wave function checklist | Which functions can be states | [Day 4](../day04.md) |

Collapse and repeated measurement are taught as a full move on Day 5 ([Move 5.3](../day05.md)); this week needs only the idea.

## Worked clones

The four clones below have the same *type* as the Week 3 task and portfolio problems but use different objects. They are not the course's problems. Use them to learn the method, then attempt the course problems yourself on a blank page in the six-steps format.

### Clone 1 — Are two kets orthogonal? (type: proof by inner product)

**Problem.** Show that $|\psi_1\rangle=\tfrac{1}{\sqrt2}\big(|u\rangle+i|d\rangle\big)$ and $|\psi_2\rangle=\tfrac{1}{\sqrt2}\big(|u\rangle-i|d\rangle\big)$ are orthogonal, and that each is normalised.

**Method.** Orthogonal means $\langle\psi_1|\psi_2\rangle=0$. Build the bra from the *left* ket by conjugating its coefficients, then use $\langle u|u\rangle=\langle d|d\rangle=1$, $\langle u|d\rangle=\langle d|u\rangle=0$.

1. Bra: $\langle\psi_1|=\tfrac{1}{\sqrt2}\big(\langle u|-i\langle d|\big)$, because $i^*=-i$.
2. Expand the product:
$$\langle\psi_1|\psi_2\rangle=\tfrac12\Big(\langle u|u\rangle+(-i)\langle u|d\rangle+(-i)\langle d|u\rangle+(-i)(-i)\langle d|d\rangle\Big)$$
where the two cross terms vanish and $(-i)(-i)=i^2=-1$. So $\langle\psi_1|\psi_2\rangle=\tfrac12(1-1)=0$.
3. Normalisation: $\langle\psi_1|\psi_1\rangle=\tfrac12\big(1+(-i)(i)\big)=\tfrac12(1+1)=1$. Similarly $\langle\psi_2|\psi_2\rangle=\tfrac12\big(1+(i)(-i)\big)=1$.
4. Column-vector cross-check: $\psi_1=\tfrac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$, so $\langle\psi_1|=\tfrac{1}{\sqrt2}(1,\,-i)$ and $\langle\psi_1|\psi_2\rangle=\tfrac12\big(1\cdot1+(-i)(-i)\big)=0$.

**Trap.** Forget to conjugate and you get $\tfrac12(1+i\cdot(-i))=\tfrac12(1+1)=1$: "not orthogonal", a wrong verdict caused by a missing star. (Those two kets are the $\pm1$ eigenstates of $\sigma_y$, which is why orthogonality had to come out; Section C says Hermitian matrices always give this.)

### Clone 2 — Eigenproblem with a parameter (type: 2×2 eigenvalues and eigenvectors, one unknown angle)

**Problem.** For real $\varphi$, take $\hat{B}=\begin{pmatrix}1&e^{-i\varphi}\\ e^{i\varphi}&1\end{pmatrix}$. Find eigenvalues and normalised eigenvectors, then the measurement statistics in the state $|u\rangle$.

**Step 0, is it a legal observable?** Diagonal entries real. Below-diagonal entry $e^{i\varphi}$ is the conjugate of the above-diagonal entry $e^{-i\varphi}$. So $\hat{B}^\dagger=\hat{B}$, Hermitian.

**Eigenvalues ([Move 3.2](../day03.md)).** $\det(\hat{B}-\lambda I)=(1-\lambda)^2-e^{-i\varphi}e^{i\varphi}=(1-\lambda)^2-1=0$, so $\lambda(\lambda-2)=0$ and $\lambda_1=2,\ \lambda_2=0$. Check: trace $=2=2+0$; $\det\hat{B}=1-1=0=2\cdot0$.

**Eigenvector for $\lambda_1=2$.** $\begin{pmatrix}-1&e^{-i\varphi}\\ e^{i\varphi}&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=0$. Row 1: $x=e^{-i\varphi}y$. Take $y=1$: $\begin{pmatrix}e^{-i\varphi}\\1\end{pmatrix}$; row 2 check: $e^{i\varphi}e^{-i\varphi}-1=0$. Length$^2=|e^{-i\varphi}|^2+1=2$. So $|\phi_1\rangle=\tfrac{1}{\sqrt2}\begin{pmatrix}e^{-i\varphi}\\1\end{pmatrix}$.

**Eigenvector for $\lambda_2=0$.** Row 1 of $\hat{B}$ itself: $x+e^{-i\varphi}y=0$, so $x=-e^{-i\varphi}y$. Then $|\phi_2\rangle=\tfrac{1}{\sqrt2}\begin{pmatrix}-e^{-i\varphi}\\1\end{pmatrix}$. Check row 2: $e^{i\varphi}(-e^{-i\varphi})+1=0$.

**Orthogonality check.** $\langle\phi_1|=\tfrac{1}{\sqrt2}(e^{i\varphi},\,1)$, so $\langle\phi_1|\phi_2\rangle=\tfrac12\big(e^{i\varphi}(-e^{-i\varphi})+1\big)=0$.

**A different route, mirroring "guess a unit-length form".** Because only the *relative phase* of the two entries matters, write a trial eigenvector as $\tfrac{1}{\sqrt2}\begin{pmatrix}1\\e^{i\chi}\end{pmatrix}$ with one unknown $\chi$. Row 1 of $\hat{B}v=\lambda v$: $1+e^{-i\varphi}e^{i\chi}=\lambda$. The eigenvalue must be real, so $e^{i(\chi-\varphi)}$ must be real: $\chi=\varphi$ (giving $\lambda=2$) or $\chi=\varphi+\pi$ (giving $\lambda=0$). Row 2 then holds automatically ($e^{i\varphi}+e^{i\chi}=\lambda e^{i\chi}$ is $2e^{i\varphi}=2e^{i\varphi}$ for $\chi=\varphi$). This reproduces the vectors above up to an overall phase $e^{-i\varphi}$, which is physically irrelevant (global phase, [Move 1.3](../day01.md)).

**Statistics in $|u\rangle=\begin{pmatrix}1\\0\end{pmatrix}$ (Postulate 4).** $\langle\phi_1|u\rangle=\tfrac{e^{i\varphi}}{\sqrt2}$, so $P(2)=\tfrac12$. $\langle\phi_2|u\rangle=\tfrac{-e^{i\varphi}}{\sqrt2}$, so $P(0)=\tfrac12$. Sum is 1. Expectation two ways: $\sum\lambda_nP(\lambda_n)=2\cdot\tfrac12+0\cdot\tfrac12=1$; and $\langle u|\hat{B}|u\rangle=B_{11}=1$. They agree, as Eq. 3.9 and Eq. 3.10 promise. The value $1$ is never an outcome; only $2$ or $0$ occur.

### Clone 3 — Acceptable wave function? (type: apply the checklist, justify each verdict)

**Checklist ([Move 4.7](../day04.md)), for $x$ over the whole real line:** finite everywhere; continuous; single-valued; continuous derivative when the potential is finite; normalisable ($\int|\psi|^2\mathrm{d}x$ finite and non-zero).

| Function | Finite | Continuous | Derivative continuous | Normalisable | Verdict |
|---|---|---|---|---|---|
| $\dfrac{1}{1+x^2}$ | yes, at most 1 | yes | yes | $\int\dfrac{\mathrm{d}x}{(1+x^2)^2}=\dfrac{\pi}{2}$ | **Acceptable** |
| $\dfrac{\sin x}{x}$ | yes; at $x=0$ take the limit 1 | yes | yes | tail $\le 1/x^2$ integrable; $\int\dfrac{\sin^2x}{x^2}\mathrm{d}x=\pi$ | **Acceptable** |
| $\tan x$ | **no**: blows up at $x=\pm\pi/2$ | no | no | no | **Not acceptable** |
| $\lvert x\rvert e^{-x^2}$ | yes | yes | **kink at 0**: slope $+1$ from the right, $-1$ from the left | $\int x^2e^{-2x^2}\mathrm{d}x=\dfrac{\sqrt\pi}{4\sqrt2}$ | Normalisable and continuous, but fails the strict derivative test |

Working for the two non-trivial cells:

- $\int_{-\infty}^{\infty}\dfrac{\mathrm{d}x}{(1+x^2)^2}=\Big[\dfrac{x}{2(1+x^2)}+\dfrac12\arctan x\Big]_{-\infty}^{\infty}=\dfrac12\Big(\dfrac\pi2-\Big(-\dfrac\pi2\Big)\Big)=\dfrac\pi2$.
- For $x>0$, $f=xe^{-x^2}$ and $f'=(1-2x^2)e^{-x^2}\to1$ as $x\to0^+$. For $x<0$, $f=-xe^{-x^2}$ and $f'\to-1$ as $x\to0^-$. [Move 4.4](../day04.md) with $a=2$: $\int_{-\infty}^{\infty}x^2e^{-2x^2}\mathrm{d}x=\dfrac{\sqrt\pi}{2\cdot2^{3/2}}=\dfrac{\sqrt\pi}{4\sqrt2}$.

**How to write the verdict.** State your criteria first. For the kinked function say: "continuous and normalisable; the derivative jumps at $x=0$, so it is acceptable only if the potential is allowed to be infinite (or a delta spike) there." Marks go to naming *which* condition fails and why, not to the bare word yes or no.

### Clone 4 — Hermiticity technique, and "relative probability in a tiny region"

**Part (a). Method: integration by parts and conjugation, shown on $\hat{D}^4=\dfrac{\mathrm{d}^4}{\mathrm{d}x^4}$.**

Claim: $\langle\phi|\hat{D}^4\psi\rangle=\langle\hat{D}^4\phi|\psi\rangle$ for normalisable $\phi,\psi$ that, together with their derivatives, die away at $\pm\infty$ (so every boundary term below vanishes).

1. Definition ([Move 4.1](../day04.md)): $\langle\phi|\hat{D}^4\psi\rangle=\int_{-\infty}^{\infty}\phi^*\,\psi^{(4)}\,\mathrm{d}x$.
2. Integrate by parts ([Move 4.3](../day04.md)), moving one derivative from the ket to the bra: $\int\phi^*\psi^{(4)}\mathrm{d}x=\big[\phi^*\psi'''\big]_{-\infty}^{\infty}-\int(\phi^*)'\,\psi'''\,\mathrm{d}x$. The boundary term is zero.
3. Repeat. Each pass moves one more derivative and produces one factor of $-1$ and one boundary term, which is zero. After the second pass: $+\int(\phi^*)''\psi''\,\mathrm{d}x$; after the third: $-\int(\phi^*)'''\psi'\,\mathrm{d}x$; after the fourth: $+\int(\phi^*)^{(4)}\psi\,\mathrm{d}x$. Four integrations by parts, so $(-1)^4=+1$.
4. Conjugation: $(\phi^*)^{(4)}=(\phi^{(4)})^*=(\hat{D}^4\phi)^*$. So the result is $\int(\hat{D}^4\phi)^*\psi\,\mathrm{d}x=\langle\hat{D}^4\phi|\psi\rangle$. $\square$

Lesson to carry away: *move every derivative off the ket and onto the bra by integrating by parts, throw away the boundary terms, and count the minus signs.* Each integration by parts contributes one minus sign, and the number of derivatives decides the overall sign.

**Part (b). Method: relative probability in a tiny region.**

*Problem.* A particle in 3D has $\psi\propto e^{-r^2/b^2}$, where $b$ is a constant length and $r$ the distance from the origin. Region A, of volume $\Delta V_A$, sits at $r=0$. Region B, of volume $\Delta V_B=2\Delta V_A$, sits at $r=b/2$. Find $P_A/P_B$. Ignore the variation of $\psi$ inside each region.

1. Principle (from Eq. 3.10: the integrand $\psi^*\psi$ is the density): probability in a tiny region $\approx|\psi|^2\,\Delta V$.
2. The unknown constant of proportionality in $\psi$ cancels in a ratio, so you never normalise.
3. $|\psi(0)|^2\propto e^{0}=1$. $|\psi(b/2)|^2\propto e^{-2(b/2)^2/b^2}=e^{-1/2}\approx0.6065$.
4. $\dfrac{P_A}{P_B}=\dfrac{1\cdot\Delta V_A}{e^{-1/2}\cdot2\Delta V_A}=\dfrac{e^{1/2}}{2}\approx0.824$.
5. Check: it is a ratio, so it has no units. If the volumes were equal it would be $e^{1/2}\approx1.65>1$: greater than 1 makes sense, because $|\psi|^2$ is largest at the origin. The extra factor 2 in region B's volume pulls it below 1, consistent with 0.824.

The general recipe: **square the modulus, multiply by the volume, divide.** Do not forget the square, and do not forget that the exponent is squared too (the exponent doubles).

## Retrieval questions

Closed book first, then hint, then sketch. Each item names the misconception it traps.

1. State $|\psi\rangle=\tfrac15\big(3|u\rangle+4i|d\rangle\big)$ with $\sigma_z|u\rangle=+|u\rangle$, $\sigma_z|d\rangle=-|d\rangle$. What are the probabilities of $+1$ and $-1$, and what is $\langle\sigma_z\rangle$? *(Traps: using amplitudes instead of squared moduli, and mishandling the $i$.)* — **Hint:** the coefficients are already the $\alpha_n$; square the modulus of each, then use $\sum\lambda_nP_n$. — **Solution sketch:** $P(+1)=|3/5|^2=9/25$, $P(-1)=|4i/5|^2=16/25$; sum $=1$. $\langle\sigma_z\rangle=\tfrac{9}{25}-\tfrac{16}{25}=-\tfrac{7}{25}$. Check by $\langle\psi|\sigma_z|\psi\rangle$: $\sigma_z|\psi\rangle=\tfrac15(3,\,-4i)^T$, bra $=\tfrac15(3,\,-4i)$, product $=\tfrac{1}{25}\big(9+(-4i)(-4i)\big)=\tfrac{1}{25}(9-16)=-\tfrac7{25}$.
2. In question 1 you measure $\sigma_z$ and get $-1$; you immediately measure $\sigma_z$ again. What is $P(-1)$ the second time? *(Traps: thinking the original $16/25$ still applies.)* — **Hint:** what is the state right after the first outcome (Postulate 5)? — **Solution sketch:** The state is $|d\rangle$, so the second measurement gives $-1$ with probability 1 ($|\langle d|d\rangle|^2=1$). The $16/25$ described the *first* measurement on the *original* state only.
3. Un-normalised $|\psi\rangle=|u\rangle+2i|d\rangle$. Find $P(+1)$ for $\sigma_z$ and $\langle\sigma_z\rangle$. *(Traps: forgetting to normalise; Eq. 3.11.)* — **Hint:** compute $\langle\psi|\psi\rangle$ first. — **Solution sketch:** $\langle\psi|\psi\rangle=1+|2i|^2=5$. $P(+1)=1/5$, $P(-1)=4/5$. $\langle\psi|\sigma_z|\psi\rangle=1+(-2i)(-2i)=1-4=-3$. So $\langle\sigma_z\rangle=-3/5$. Cross-check: $\tfrac15-\tfrac45=-\tfrac35$.
4. For $|\psi\rangle=\tfrac{1}{\sqrt2}\big(|u\rangle+i|d\rangle\big)$, show $\langle\sigma_z\rangle=0$. Can a single $\sigma_z$ measurement return $0$? *(Traps: the expectation value is an outcome.)* — **Hint:** what are the only possible outcomes, by Postulate 3? — **Solution sketch:** $P(\pm1)=\tfrac12$ each, so $\langle\sigma_z\rangle=\tfrac12-\tfrac12=0$. But $0$ is not an eigenvalue, so no single measurement returns it; the *average* over many runs tends to $0$. Here $\Delta\sigma_z=\sqrt{1-0}=1$ (because $\sigma_z^2=I$, so $\langle\sigma_z^2\rangle=1$).
5. True or false: "$|\psi(x_0)|^2$ is the probability that the particle is at $x_0$." *(Traps: quiz Q2's option that the wave function gives actual position; density versus probability.)* — **Hint:** what does a probability of finding it at one exact point equal for a continuous variable? — **Solution sketch:** False. $|\psi(x_0)|^2$ is a probability *density* (units 1/length in 1D). The probability of finding the particle in $[x_0,x_0+\mathrm{d}x]$ is $|\psi(x_0)|^2\mathrm{d}x$. The wave function is an amplitude, not the actual position.
6. $\hat{C}=\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}$. Check it is Hermitian, find eigenvalues and eigenvectors, then the outcome probabilities and $\langle\hat{C}\rangle$ in state $|u\rangle$. *(Traps: dropping a conjugate in the off-diagonal entry; unnormalised eigenvectors.)* — **Hint:** characteristic polynomial $\lambda^2-(\text{trace})\lambda+\det=0$, with $(1-i)(1+i)=2$. — **Solution sketch:** Diagonal real; $1+i=(1-i)^*$, so Hermitian. Trace 5, $\det=6-2=4$, so $\lambda^2-5\lambda+4=0$, $\lambda=1,4$. For $\lambda=4$: row 1 of $\hat{C}-4I$ gives $-2x+(1-i)y=0$; $y=2$ gives $(1-i,\,2)$, length$^2$ $=2+4=6$. For $\lambda=1$: $x+(1-i)y=0$; $y=1$ gives $(-1+i,\,1)$, length$^2$ $=2+1=3$. Orthogonal: $\big(\overline{-1+i}\big)(1-i)+1\cdot2=(-1-i)(1-i)+2=-2+2=0$. In $|u\rangle$: $P(4)=|\overline{(1-i)}|^2/6=2/6=1/3$; $P(1)=|\overline{(-1+i)}|^2/3=2/3$. $\langle\hat{C}\rangle=4\cdot\tfrac13+1\cdot\tfrac23=2=C_{11}$, as $\langle u|\hat{C}|u\rangle$ demands.
7. Which of $\operatorname{sech}x$, $\dfrac1x$, $\cos x$ (all on the whole line) are acceptable wave functions? *(Traps: "bounded" is not enough; "normalisable" is separate from "finite".)* — **Hint:** run the checklist and evaluate $\int|\psi|^2$ for each; $\int\operatorname{sech}^2x\,\mathrm{d}x=[\tanh x]$. — **Solution sketch:** $\operatorname{sech}x$: finite, smooth, $\int\operatorname{sech}^2x\,\mathrm{d}x=\tanh(\infty)-\tanh(-\infty)=2$, acceptable. $1/x$: infinite at $x=0$, no. $\cos x$: finite and smooth but $\int\cos^2x\,\mathrm{d}x$ grows without bound (average of $\cos^2$ is $\tfrac12$ on every stretch), not normalisable, no.
8. Reproduce the proof that a Hermitian operator has real eigenvalues, from memory, in three lines. *(Traps: forgetting that a constant on the bra side is conjugated.)* — **Hint:** compute $\langle\phi|\hat{A}\phi\rangle$ two ways: act on the ket, or move $\hat{A}$ onto the bra. — **Solution sketch:** $\langle\phi|\hat{A}\phi\rangle=\lambda\langle\phi|\phi\rangle$. By Hermiticity it equals $\langle\hat{A}\phi|\phi\rangle=\lambda^*\langle\phi|\phi\rangle$. Subtract: $(\lambda-\lambda^*)\langle\phi|\phi\rangle=0$, and $\langle\phi|\phi\rangle>0$, so $\lambda=\lambda^*$.

## Six-steps write-up template

This is the stand-in structure from [STRATEGY](../../STRATEGY.md) (not the university's own text). Below it is applied to each of this week's four problem types. Use the prompts as the skeleton of your own solution; the content is yours to fill.

**The six steps.** 1. Restate and list givens. 2. Write the state or operator in notation. 3. Name the principle or move. 4. Do the algebra, every line. 5. Check. 6. State the answer in a sentence.

| Step | Orthogonality / inner-product proof | 2×2 eigenproblem | Acceptable wave function | Hermiticity or relative probability |
|---|---|---|---|---|
| 1. Restate | "Show $\langle\psi_1\lvert\psi_2\rangle=0$"; list both kets | "Find $\lambda$ and $\lvert\phi\rangle$ of $\hat{A}$"; note any parameter | "Which of these can be a wave function?" | "Show $\langle\phi\lvert\hat{O}\psi\rangle=\langle\hat{O}\phi\lvert\psi\rangle$" or "find $P_A/P_B$" |
| 2. Write | Column vectors and bras (conjugate the left ket) | Matrix, identity, unknown $(x,y)^T$ | Each function, its domain, a quick sketch | The integral form ([Move 4.1](../day04.md)), or $\psi\propto\ldots$ and the two regions |
| 3. Name | [Move 2.2](../day02.md), 2.3: inner product, orthonormal basis | [Move 3.2](../day03.md) recipe, Hermitian check (3.3) | Checklist, [Move 4.7](../day04.md) | [Move 4.3](../day04.md) (by parts), conjugation; or density $\times$ volume |
| 4. Algebra | Expand, kill cross terms, simplify complex numbers | Determinant, roots, one row for the ratio, normalise | One row per function, one condition per column | Two integrations by parts with boundary terms named; or square, multiply, divide |
| 5. Check | Also compute $\langle\psi_j\lvert\psi_j\rangle=1$; try the column form | Trace $=\sum\lambda$, $\det=\prod\lambda$, plug the vector back; eigenvectors orthogonal | Integral really finite; a spot-check point | Units, ratio limits, probabilities in $[0,1]$ |
| 6. Answer | "Hence the states are orthogonal (and normalised)" | List eigenpairs; for a statistics question, add $P(\lambda_n)$ and $\langle\hat{A}\rangle$ | One sentence per function, stating which condition decides | "Hence $\hat{O}$ is Hermitian on normalisable functions" or "the ratio is …" |

**Common-slip checklist before you hand anything in.**
- Did I conjugate the left-hand object in every inner product?
- Do my probabilities sum to 1, and is each in $[0,1]$?
- Is every quoted outcome an eigenvalue, not an average?
- Did I name what happens to boundary terms, and why they vanish?
