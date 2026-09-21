# Day 3 — Operators, Eigenproblems, Hermitian Matrices and the Pauli Matrices

**Time box (~3.5 h):** 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Why this matters

Week 3 says the only numbers a measurement can ever return are the *eigenvalues* of an operator (postulate 3, Eq. 3.1 in the lecture). Week 4 makes you work with adjoints and Hermitian operators, and Week 6 writes spin measurements as 2×2 matrices. All of that is one skill: take a small matrix, find its special numbers and special vectors, and know what "Hermitian" promises about them.

Today you learn five moves (3.1 to 3.5). By tonight you can find the eigenpairs of any 2×2 matrix on a blank page, and you can say why measured values are real numbers.

## Warm-up (20 min, closed book, retrieval from Day 2)

Answers are at the bottom of the file. Write your answer first, then check.

1. (Move 2.1) For $\mathbf{u} = (1, 2)^{\mathsf T}$ and $\mathbf{v} = (3, -1)^{\mathsf T}$, compute $\mathbf{u}\cdot\mathbf{v}$ and $|\mathbf{u}|$.
2. (Move 2.2) Let $|\psi\rangle = \begin{pmatrix}1+i\\ 2\end{pmatrix}$. Write the bra $\langle\psi|$ and compute $\langle\psi|\psi\rangle$.
3. (Moves 2.2, 2.3) With $|\varphi\rangle = \begin{pmatrix}1\\ i\end{pmatrix}$ and $|\chi\rangle = \begin{pmatrix}2\\ 1\end{pmatrix}$, compute $\langle\varphi|\chi\rangle$ and $\langle\chi|\varphi\rangle$. How are the two answers related?
4. (Move 2.4) Show that $|e_1\rangle = \frac15\begin{pmatrix}3\\ 4\end{pmatrix}$ and $|e_2\rangle = \frac15\begin{pmatrix}4\\ -3\end{pmatrix}$ are orthonormal, then write $\begin{pmatrix}1\\ 0\end{pmatrix} = c_1|e_1\rangle + c_2|e_2\rangle$ and check $c_1^2 + c_2^2 = 1$.
5. (Move 2.5) Multiply $\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}$. Then swap the order and multiply again. Are the results equal?

## Moves

### Move 3.1 — Operators as matrices; how an operator acts on a ket (10 min)

**Plain English.** An *operator* is a machine that eats a ket (a state) and returns another ket. In this module, for a two-level system, the machine is a 2×2 matrix and "eating" is matrix times column vector (Move 2.5).

**Notation, said aloud.** $\hat{A}$ is "A hat", the operator. $\hat{A}|\psi\rangle$ is "A hat acting on ket psi". In a basis, $\hat{A}$ is a table of numbers $A_{jk}$ and $|\psi\rangle$ is a column of numbers, so

$$\hat{A}|\psi\rangle = \begin{pmatrix} a & b\\ c & d\end{pmatrix}\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix} = \begin{pmatrix} a\psi_1 + b\psi_2\\ c\psi_1 + d\psi_2\end{pmatrix}.$$

The two basis kets for a spin-½ particle are written $|u\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ ("spin-up") and $|d\rangle = \begin{pmatrix}0\\1\end{pmatrix}$ ("spin-down"), as in the Week 3 Task (the Week 3 lecture itself does not use these names; the Week 6 lecture, Eqs. 6.1 and 6.2, writes the same states differently). Bridging line: the Week 6 lecture calls the state with $S_z = +$ (respectively $S_z = -$) $|\psi_z^+\rangle$ (respectively $|\psi_z^-\rangle$) and the states with $S_x = \pm$ $|\psi_x^\pm\rangle$, so I read $|u\rangle \leftrightarrow |\psi_z^+\rangle$, $|d\rangle \leftrightarrow |\psi_z^-\rangle$, $|+x\rangle \leftrightarrow |\psi_x^+\rangle$, $|-x\rangle \leftrightarrow |\psi_x^-\rangle$. The lecture gives no column vectors for these, only the overlaps in Eqs. 6.1 and 6.2, so the column forms used here are the standard convention and not something the lecture states. A matrix's first column is what it does to $|u\rangle$; its second column is what it does to $|d\rangle$.

**Worked example.** Let $\hat{M} = \begin{pmatrix}0&2\\ 3&1\end{pmatrix}$ and $|\psi\rangle = \begin{pmatrix}1\\ -1\end{pmatrix}$. Then $\hat{M}|\psi\rangle = \begin{pmatrix}0\cdot 1 + 2\cdot(-1)\\ 3\cdot 1 + 1\cdot(-1)\end{pmatrix} = \begin{pmatrix}-2\\ 2\end{pmatrix}$. The output is a different vector, not just a rescaled one. That is the normal case. The next move is about the special vectors where the output *is* a rescaled copy.

### Move 3.2 — Eigenvalue equation; 2×2 characteristic polynomial; eigenvector solve; normalise (20 min)

**Plain English.** Most vectors get turned to point somewhere new by $\hat{A}$. A few special vectors only get stretched (or flipped). They keep their direction. The stretch factor is the *eigenvalue* $\lambda$ and the special vector is the *eigenvector*. In physics the eigenvector is called an *eigenstate*. This is the eigenvalue equation from the lecture (Eq. 3.1):

$$\hat{A}|\phi\rangle = \lambda|\phi\rangle.$$

Say it as "A hat on phi equals lambda times phi". Measurement can only return one of these $\lambda$ values, and after the measurement the system sits in the matching eigenstate.

**Why the recipe works.** Move everything to one side: $(\hat{A} - \lambda I)|\phi\rangle = 0$. We want a nonzero $|\phi\rangle$ that this matrix sends to zero. That is only possible when the matrix $A - \lambda I$ squashes the plane flat, which happens exactly when its determinant is zero. For a 2×2 matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ the determinant is $ad - bc$. The condition $\det(A - \lambda I) = 0$ is a quadratic in $\lambda$, called the *characteristic polynomial*. A quadratic has two roots, so a 2×2 matrix has two eigenvalues (counted with repetition).

> **THE FIVE-LINE ALGORITHM (2×2 eigenpairs)**
>
> 1. **Determinant:** write $\det(A - \lambda I) = 0$, that is $(a-\lambda)(d-\lambda) - bc = 0$.
> 2. **Solve for $\lambda$:** expand to $\lambda^2 - (a+d)\lambda + (ad - bc) = 0$ and solve. Two roots: $\lambda_1, \lambda_2$.
> 3. **Plug back:** for one root at a time, write the system $(A - \lambda I)\begin{pmatrix}x\\y\end{pmatrix} = 0$.
> 4. **Solve one row for the ratio:** the two rows say the same thing, so use just one to get $y/x$. Set whichever component makes the equation easiest (for example $x = 1$) and read off the other; if a component must be 0, use the other one. When you divide by $i$ remember $1/i = -i$ (because $i\cdot(-i) = -i^2 = 1$), and so $1/(-i) = i$.
> 5. **Normalise:** divide the vector by its length so that $\langle\phi|\phi\rangle = 1$. Use the bra, with conjugates: length$^2 = |x|^2 + |y|^2$.
>
> **Checks (always):** trace $a + d = \lambda_1 + \lambda_2$ and $\det A = \lambda_1\lambda_2$. Then verify $A|\phi\rangle = \lambda|\phi\rangle$ by direct multiplication.

**Worked example.** $A = \begin{pmatrix}5&2\\2&2\end{pmatrix}$.

1. $\det(A - \lambda I) = (5-\lambda)(2-\lambda) - 4 = 0$.
2. Expand: $\lambda^2 - 7\lambda + 6 = 0$, so $(\lambda - 1)(\lambda - 6) = 0$ and $\lambda = 1$ or $6$. Check: trace $= 7 = 1 + 6$, det $= 6 = 1\cdot 6$.
3. For $\lambda = 6$: $\begin{pmatrix}-1&2\\2&-4\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix} = 0$.
4. Row 1: $-x + 2y = 0$, so $x = 2y$. Take $y = 1$: vector $\begin{pmatrix}2\\1\end{pmatrix}$. (Row 2 gives $2x = 4y$, the same statement.)
5. Length$^2 = 4 + 1 = 5$, so $|\phi_6\rangle = \frac{1}{\sqrt5}\begin{pmatrix}2\\1\end{pmatrix}$.

Repeat for $\lambda = 1$: $\begin{pmatrix}4&2\\2&1\end{pmatrix}$, row 1 gives $4x + 2y = 0$, $y = -2x$, vector $\begin{pmatrix}1\\-2\end{pmatrix}$, normalised $|\phi_1\rangle = \frac{1}{\sqrt5}\begin{pmatrix}1\\-2\end{pmatrix}$.

Check by multiplying: $A\begin{pmatrix}2\\1\end{pmatrix} = \begin{pmatrix}12\\6\end{pmatrix} = 6\begin{pmatrix}2\\1\end{pmatrix}$. Good.

**Two facts about the answer.**
- An eigenvector is only defined up to a constant. $\begin{pmatrix}2\\1\end{pmatrix}$, $\begin{pmatrix}-2\\-1\end{pmatrix}$ and $i\begin{pmatrix}2\\1\end{pmatrix}$ all describe the same physical state. After normalising, the leftover freedom is a global phase $e^{i\theta}$ (Move 1.3), which changes nothing measurable.
- If both eigenvalues are equal, the eigenvalue is called *degenerate*. Then there may be a whole plane of eigenvectors (for example, the identity matrix) or only one direction (see Exercise 10). Step 4 tells you which: if the rows give no constraint, everything is an eigenvector.

### Move 3.3 — Adjoint, Hermitian, $(AB)^\dagger = B^\dagger A^\dagger$, real eigenvalues, orthogonal eigenvectors (10 min)

**Adjoint for matrices.** The *adjoint* $A^\dagger$ ("A dagger") is the conjugate transpose: swap rows and columns, then conjugate every entry. It is the matrix version of the lecture's definition (Eq. 2.14), $\langle\psi|\hat{A}\phi\rangle = \langle\hat{A}^\dagger\psi|\phi\rangle$. Example:

$$A = \begin{pmatrix}1 & 2i\\ 3 & 4\end{pmatrix}\ \Rightarrow\ A^\dagger = \begin{pmatrix}1 & 3\\ -2i & 4\end{pmatrix}.$$

Kets and bras are the special case: the bra is the adjoint of the ket.

**Hermitian.** $A$ is *Hermitian* if $A^\dagger = A$ (lecture Eq. 2.13). Concretely: the diagonal entries are real, and the entry below the diagonal is the conjugate of the entry above it. A real symmetric matrix is Hermitian. A *complex* symmetric matrix generally is not.

**Product rule.** $(AB)^\dagger = B^\dagger A^\dagger$. The order reverses, exactly like taking off socks and shoes. Also $(A+B)^\dagger = A^\dagger + B^\dagger$ and $(cA)^\dagger = c^*A^\dagger$: the scalar gets conjugated.

**Why a Hermitian matrix has real eigenvalues (in words).** Take an eigenvector $|\phi\rangle$ with $A|\phi\rangle = \lambda|\phi\rangle$. Compute the number $\langle\phi|A\phi\rangle$ in two ways.

- Directly: $\langle\phi|A\phi\rangle = \lambda\langle\phi|\phi\rangle$, because $\lambda$ just comes out of the ket.
- Using Hermiticity, move $A$ across to the bra: $\langle\phi|A\phi\rangle = \langle A\phi|\phi\rangle$. Now the bra of $\lambda|\phi\rangle$ carries a conjugate, so this equals $\lambda^*\langle\phi|\phi\rangle$.

Both are the same number, so $(\lambda - \lambda^*)\langle\phi|\phi\rangle = 0$. Since $\langle\phi|\phi\rangle > 0$ for a non-zero vector (Move 2.3), $\lambda = \lambda^*$, so $\lambda$ is real. This matches the proof in the Week 2 lecture around Eq. 2.16.

**Why eigenvectors for different eigenvalues are orthogonal (in words).** Take $A|\phi_n\rangle = \lambda_n|\phi_n\rangle$ and $A|\phi_m\rangle = \lambda_m|\phi_m\rangle$ with $\lambda_n \ne \lambda_m$. Compute $\langle\phi_n|A\phi_m\rangle$ two ways again: it equals $\lambda_m\langle\phi_n|\phi_m\rangle$, and, moving $A$ to the left, $\lambda_n^*\langle\phi_n|\phi_m\rangle$. The eigenvalues are real, so $\lambda_n^* = \lambda_n$, and $(\lambda_n - \lambda_m)\langle\phi_n|\phi_m\rangle = 0$. The first factor is not zero, so the inner product is zero: the eigenvectors are orthogonal.

**One example.** In Move 3.2 the matrix $\begin{pmatrix}5&2\\2&2\end{pmatrix}$ is real symmetric, hence Hermitian. Its eigenvalues $1, 6$ are real, and $\begin{pmatrix}2\\1\end{pmatrix}$ and $\begin{pmatrix}1\\-2\end{pmatrix}$ have dot product $2 - 2 = 0$. The eigenvectors of a Hermitian matrix form an orthonormal basis, which is exactly what the lecture needs in order to write $|\psi\rangle = \sum_n\alpha_n|\phi_n\rangle$ (Eq. 3.8).

### Move 3.4 — Pauli matrices: eigenvectors, spin-up/down, $\pm x$, $\pm y$ states (15 min)

The three *Pauli matrices* are

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_y = \begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Say them as "sigma x", "sigma y", "sigma z". Each is Hermitian (check: the diagonals are real and the off-diagonals are conjugates of each other), each squares to the identity, and each has eigenvalues $+1$ and $-1$ (trace 0, determinant $-1$, so $\lambda^2 = 1$). For a spin-½ particle the spin component is $\hat{S}_j = \frac{\hbar}{2}\sigma_j$, so the measured values are $\pm\hbar/2$. This factor $\hbar/2$ is the standard convention and is not spelled out in the Week 6 lecture; the lecture's own Stern-Gerlach statement is that a measurement gives one of two outcomes, $S = +$ or $S = -$.

**$\sigma_z$ is already diagonal.** Its eigenvectors are the basis kets: $\sigma_z|u\rangle = +1\,|u\rangle$ and $\sigma_z|d\rangle = -1\,|d\rangle$. So "spin-up" and "spin-down" along $z$ are the eigenstates with eigenvalues $+1$ and $-1$.

**Reference card of eigenstates** (you derive these with the five-line algorithm in the exercises):

| Operator | Eigenvalue $+1$ | Eigenvalue $-1$ |
|---|---|---|
| $\sigma_z$ | $\lvert u\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ | $\lvert d\rangle = \begin{pmatrix}0\\1\end{pmatrix}$ |
| $\sigma_x$ | $\lvert +x\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$ | $\lvert -x\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$ |
| $\sigma_y$ | $\lvert +y\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix}$ | $\lvert -y\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\ -i\end{pmatrix}$ |

Notice the pattern. An eigenstate of one Pauli matrix, seen in the eigenbasis of another, is an equal mix: each outcome has probability $\tfrac12$. This is the algebra behind the Stern-Gerlach result in Week 6, where a particle prepared with definite $S_z$ gives a 50/50 outcome for $S_x$.

**Only one place to be careful.** The eigenvector of $\sigma_y$ contains $i$. Its bra has $-i$. Forgetting that conjugate is the most common slip in this move.

### Move 3.5 — Commutator $[A,B] = AB - BA$ (5 min)

The *commutator* of two matrices is $[A,B] = AB - BA$. Say it as "commutator of A and B". It is zero when the order of multiplication does not matter, and non-zero when it does. Matrix multiplication usually depends on order (you saw this in warm-up question 5).

**Worked example.** $A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $B = \begin{pmatrix}0&3\\1&0\end{pmatrix}$. Then $AB = \begin{pmatrix}0&3\\-1&0\end{pmatrix}$ and $BA = \begin{pmatrix}0&-3\\1&0\end{pmatrix}$, so $[A,B] = \begin{pmatrix}0&6\\-2&0\end{pmatrix}$.

Why physicists care (preview of Week 6): two operators that do not commute have no common eigenbasis (they cannot be simultaneously diagonalised), so in general a state cannot have definite values of both. They can still share an individual eigenvector in special cases. The Week 3 lecture says the physical point in words when it discusses measuring $A$ then a different observable $M$ with different eigenstates.

## Core concepts

- **Operator** = a matrix that transforms states. **Observable** = a Hermitian operator. Its eigenvalues are the possible measurement results.
- **Eigenvalue / eigenvector / eigenstate.** The number and the direction that survive the operator. Every measurement question begins by finding them.
- **Hermitian** is the guarantee that (a) results are real and (b) eigenstates for different results are orthogonal, so probabilities $|\langle\phi_n|\psi\rangle|^2$ make sense.
- **Adjoint** is the conjugate transpose. On a scalar it means conjugate. On a product it reverses the order.
- **Degenerate** means two eigenvectors share one eigenvalue. The recipe still works but you must handle a plane of eigenvectors.
- **Notation decoded.** $\hat{A}$ operator; $A^\dagger$ adjoint; $|\phi\rangle$ ket; $\langle\phi|$ bra (conjugate transpose of the ket); $\langle\phi|A\psi\rangle$ inner product of $\phi$ with $A\psi$; $[A,B]$ commutator.

## Exercises (90 min, cold attempt first: 5 minutes with no hint before you open the hint)

1. Find the eigenvalues and normalised eigenvectors of $\begin{pmatrix}4&2\\2&1\end{pmatrix}$. — **Hint:** Use the five-line algorithm. Expand $(4-\lambda)(1-\lambda) - 4 = 0$; the constant term cancels, so the quadratic factorises at once. Check trace and determinant against your roots. — **Solution sketch:** $\lambda^2 - 5\lambda = 0$, so $\lambda = 0$ or $5$. For $\lambda = 5$: $-x + 2y = 0$, so $x = 2y$ and the normalised vector is $\frac{1}{\sqrt5}\begin{pmatrix}2\\1\end{pmatrix}$. For $\lambda = 0$: $4x + 2y = 0$, so $y = -2x$, giving $\frac{1}{\sqrt5}\begin{pmatrix}1\\-2\end{pmatrix}$. Trace $5 = 0+5$, det $4 - 4 = 0 = 0\cdot 5$. Direct check: $\begin{pmatrix}4&2\\2&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix} = \begin{pmatrix}10\\5\end{pmatrix} = 5\begin{pmatrix}2\\1\end{pmatrix}$. The two vectors have dot product $2 - 2 = 0$.

2. Find the eigenvalues and normalised eigenvectors of $\sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$. — **Hint:** The determinant is $(0-\lambda)(0-\lambda) - (-i)(i)$. Remember $(-i)(i) = -i^2 = 1$, and $1/i = -i$. In step 4, row 1 reads $-\lambda x - iy = 0$. — **Solution sketch:** $\lambda^2 - 1 = 0$, so $\lambda = \pm1$. For $\lambda = +1$: $-x - iy = 0$, so $x = -iy$. Take $x = 1$, then $y = 1/(-i) = i$, using $1/i = -i$ and hence $1/(-i) = i$ (check row 2: $ix - y = i - i = 0$). Normalise: length$^2 = |1|^2 + |i|^2 = 2$, giving $\frac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$. For $\lambda = -1$: $x - iy = 0$, so $x = 1$ gives $y = -i$, i.e. $\frac{1}{\sqrt2}\begin{pmatrix}1\\-i\end{pmatrix}$. Verify one by multiplying: $\sigma_y\begin{pmatrix}1\\i\end{pmatrix} = \begin{pmatrix}-i\cdot i\\ i\end{pmatrix} = \begin{pmatrix}1\\ i\end{pmatrix}$.

3. Find the eigenvalues and normalised eigenvectors of $\begin{pmatrix}1&i\\-i&1\end{pmatrix}$. — **Hint:** The product of the off-diagonal entries is $i\cdot(-i) = 1$. Expand the determinant, then handle each $\lambda$ separately. Compare this matrix with $I - \sigma_y$ afterwards to see why the answers look familiar. — **Solution sketch:** $(1-\lambda)^2 - 1 = 0$, so $\lambda = 0$ or $2$. For $\lambda = 2$: row 1 is $-x + iy = 0$, so $x = iy$. Choose $x = 1$, then $y = -i$ (from $iy = 1$, $y = 1/i = -i$). Normalised: $\frac{1}{\sqrt2}\begin{pmatrix}1\\-i\end{pmatrix}$. For $\lambda = 0$: row 1 is $x + iy = 0$; $x = 1$ gives $y = i$. Normalised: $\frac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$. The matrix equals $I - \sigma_y$, which is why the eigenvectors are those of $\sigma_y$ with eigenvalues $1 \mp 1$.

4. For each matrix decide whether it is Hermitian, and say why. $M_1 = \begin{pmatrix}2 & 1-i\\ 1+i & 3\end{pmatrix}$, $M_2 = \begin{pmatrix}1 & i\\ i & 1\end{pmatrix}$, $M_3 = \begin{pmatrix}0 & 2i\\ -2i & 5\end{pmatrix}$. — **Hint:** Write $M^\dagger$ by swapping rows and columns first and only then conjugating every entry. Compare with $M$ entry by entry. — **Solution sketch:** $M_1$: transpose has $(1+i)$ on the top right, conjugate gives $(1-i)$, and the bottom left becomes $(1-i)^* = 1+i$. So $M_1^\dagger = M_1$, Hermitian. $M_2$: transposing changes nothing (it is symmetric), but conjugating turns $i$ into $-i$, so $M_2^\dagger = \begin{pmatrix}1&-i\\-i&1\end{pmatrix} \ne M_2$. Not Hermitian: symmetric is not enough for complex entries. $M_3$: diagonal entries real, and $(2i)^* = -2i$ sits in the mirror position. Hermitian.

5. Let $A = \begin{pmatrix}1 & i\\ 0 & 2\end{pmatrix}$ and $B = \begin{pmatrix}1 & 0\\ i & 1\end{pmatrix}$. Compute $(AB)^\dagger$ and $B^\dagger A^\dagger$ and compare. Also compute $A^\dagger B^\dagger$. — **Hint:** Compute $AB$ first (row times column), then take its dagger. Separately compute $A^\dagger$ and $B^\dagger$ and multiply in the order $B^\dagger$ first. — **Solution sketch:** $AB = \begin{pmatrix}1\cdot1 + i\cdot i & i\\ 2i & 2\end{pmatrix} = \begin{pmatrix}0 & i\\ 2i & 2\end{pmatrix}$, so $(AB)^\dagger = \begin{pmatrix}0 & -2i\\ -i & 2\end{pmatrix}$. Also $A^\dagger = \begin{pmatrix}1&0\\-i&2\end{pmatrix}$, $B^\dagger = \begin{pmatrix}1&-i\\0&1\end{pmatrix}$, and $B^\dagger A^\dagger = \begin{pmatrix}1 + (-i)(-i) & -2i\\ -i & 2\end{pmatrix} = \begin{pmatrix}0&-2i\\-i&2\end{pmatrix}$, matching $(AB)^\dagger$. The wrong order gives $A^\dagger B^\dagger = \begin{pmatrix}1&-i\\-i&1\end{pmatrix}$, which differs.

6. Show that $\sigma_x\sigma_y = i\sigma_z$, and hence that $[\sigma_x,\sigma_y] = 2i\sigma_z$. — **Hint:** Compute $\sigma_x\sigma_y$ and $\sigma_y\sigma_x$ separately, entry by entry. The two products are related by a sign. — **Solution sketch:** $\sigma_x\sigma_y = \begin{pmatrix}0\cdot0 + 1\cdot i & 0\\ 0 & 1\cdot(-i)\end{pmatrix} = \begin{pmatrix}i&0\\0&-i\end{pmatrix} = i\sigma_z$. Likewise $\sigma_y\sigma_x = \begin{pmatrix}-i&0\\0&i\end{pmatrix} = -i\sigma_z$. Then $[\sigma_x,\sigma_y] = i\sigma_z - (-i\sigma_z) = 2i\sigma_z$.

7. Using $|+y\rangle$ and $|-y\rangle$ from Exercise 2, check that they are orthonormal, and compute $|\langle u|+y\rangle|^2$ and $|\langle d|+y\rangle|^2$. — **Hint:** Write the bra of $|+y\rangle$ with the $i$ conjugated. Inner products use $\langle\cdot|\cdot\rangle$ with conjugated bra entries. $|u\rangle = (1,0)^T$, $|d\rangle = (0,1)^T$. — **Solution sketch:** $\langle+y|+y\rangle = \frac12(1\cdot1 + (-i)(i)) = \frac12(1+1) = 1$; same for $-y$. Overlap: $\langle+y|-y\rangle = \frac12(1\cdot1 + (-i)(-i)) = \frac12(1 - 1) = 0$. Orthonormal. Then $\langle u|+y\rangle = \frac{1}{\sqrt2}$, so probability $\frac12$; $\langle d|+y\rangle = \frac{i}{\sqrt2}$, and $|i/\sqrt2|^2 = \frac12$. The two probabilities add to 1 as required.

8. Find the eigenstates of $\sigma_x$ using the five-line algorithm and verify that $|\langle u|+x\rangle|^2 = \tfrac12$. — **Hint:** The characteristic equation is $\lambda^2 - 1 = 0$. For $\lambda = 1$, row 1 reads $-x + y = 0$. The bra $\langle u|$ picks out the first component of $|+x\rangle$. — **Solution sketch:** $\lambda = \pm1$. For $+1$: $y = x$, so $|+x\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$. For $-1$: $y = -x$, so $|-x\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$. Then $\langle u|+x\rangle = \frac{1}{\sqrt2}$ and its square is $\frac12$. (Orthogonality of these two states is left for the course's own Week 3 task; do not use this exercise as a substitute for attempting that problem yourself.)

9. Explain why every eigenvalue of a Hermitian matrix must be real. — **Hint:** Go back to Move 2.3. Two facts do the work: $\langle\psi|\phi\rangle^* = \langle\phi|\psi\rangle$ (conjugate symmetry) and $\langle\phi|\phi\rangle > 0$ for $|\phi\rangle \ne 0$. Compute $\langle\phi|A\phi\rangle$ two ways, once as $\lambda\langle\phi|\phi\rangle$ and once with $A$ moved across the bra. — **Solution sketch:** Let $A|\phi\rangle = \lambda|\phi\rangle$ with $|\phi\rangle \ne 0$. Then $\langle\phi|A\phi\rangle = \lambda\langle\phi|\phi\rangle$. Since $A = A^\dagger$, also $\langle\phi|A\phi\rangle = \langle A\phi|\phi\rangle = \lambda^*\langle\phi|\phi\rangle$ (a scalar in the ket comes out conjugated from the bra). Subtract: $(\lambda - \lambda^*)\langle\phi|\phi\rangle = 0$. The norm is positive, so $\lambda = \lambda^*$, meaning $\lambda$ is real.

10. Find the eigenvalues of $P = \begin{pmatrix}3&0\\0&3\end{pmatrix}$ and $Q = \begin{pmatrix}3&1\\0&3\end{pmatrix}$. In each case describe the eigenvectors. Which matrix is Hermitian? — **Hint:** Both have the repeated root $\lambda = 3$. Plug it back in (step 3) and ask what the rows of $A - 3I$ say about $x$ and $y$. — **Solution sketch:** Both have $(3-\lambda)^2 = 0$, so $\lambda = 3$ (degenerate). For $P$: $A - 3I$ is the zero matrix, so every vector is an eigenvector: a whole plane. For $Q$: $A - 3I = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ gives $y = 0$, so only multiples of $\begin{pmatrix}1\\0\end{pmatrix}$. $P$ is Hermitian (real diagonal). $Q$ is not ($Q^\dagger$ has the 1 in the lower left), which shows a non-Hermitian matrix can fail to have a full set of eigenvectors.

11. Compute $[\sigma_z,\sigma_x]$ and $\sigma_y^2$. — **Hint:** For the commutator, multiply in both orders. Use $\sigma_y\sigma_y$ with $(-i)(i) = 1$. — **Solution sketch:** $\sigma_z\sigma_x = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and $\sigma_x\sigma_z = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$, so $[\sigma_z,\sigma_x] = \begin{pmatrix}0&2\\-2&0\end{pmatrix} = 2i\sigma_y$ (since $i\sigma_y = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$). And $\sigma_y^2 = \begin{pmatrix}(-i)(i) & 0\\0&(i)(-i)\end{pmatrix} = I$. The pattern $[\sigma_x,\sigma_y] = 2i\sigma_z$, $[\sigma_z,\sigma_x] = 2i\sigma_y$ cycles through $x \to y \to z$.

## Apply to the lecture (40 min)

Do this after the exercises, with the lecture files open.

- **Week 3 (measurement and eigenvalues).** Read `week_3/week_3_lecture.md` section 3.1 (Postulate 3, Eq. 3.1) and the start of section 3.2, and the companion `companions/week03_companion.md` sections on the eigenvalue table and on collapse. Look for: the table with a row of $\lambda_n$, a row of $|\phi_n\rangle$ and a row of probabilities. Say aloud which of your five algorithm steps produced each row. Also read section 3.3 (Eq. 3.5) and the "measure a different observable" passage; connect it with Move 3.5.
- **Week 2 lecture, Hermitian operators section.** Read the proof of real eigenvalues around Eq. 2.16 and compare it with your Exercise 9: same argument, different notation.
- **Week 6 (spin-½ matrices).** Read `week_6/week_6_lecture.md` on the Stern-Gerlach experiment, the passage where a measurement of $S_z$ collapses to $|\psi_z^+\rangle$ or $|\psi_z^-\rangle$, and Eqs. 6.1 and 6.2, then `companions/week06_companion.md`. Note that Eq. 6.1 is a table of overlaps between eigenstates; it is not a Pauli matrix with $\pm1$ on the diagonal. Eq. 6.2 holds the $1/\sqrt2$ overlaps. Look for where the successive $\hat{S}_z$, $\hat{S}_x$, $\hat{S}_z$ measurements use the fact that $|\langle u|+x\rangle|^2 = \frac12$.
- **Week 4 Apply, Problem 2.** Do not do it today. But read its wording and notice that it asks for adjoints of operators (not of matrices). Move 3.3's rule for products is the matrix version of what you will need. Attempt that problem yourself, without help from this file.

## Anti-patterns / Common mistakes

- **Forgetting to normalise.** An eigenvector is not finished until $\langle\phi|\phi\rangle = 1$. Otherwise probabilities like $|\langle\phi|\psi\rangle|^2$ come out wrong.
- **Treating the matrix's entries as its eigenvalues.** The diagonal of $\begin{pmatrix}5&2\\2&2\end{pmatrix}$ is $5, 2$, but the eigenvalues are $1$ and $6$. Only for a diagonal matrix do the two coincide. Use trace and determinant to catch this.
- **Dropping the conjugate when taking $\dagger$.** Transpose alone is not enough. $\begin{pmatrix}1&i\\i&1\end{pmatrix}$ is symmetric but not Hermitian. Conjugate, then transpose (or the reverse; the order of those two does not matter, but omitting either does).

## Confusion log (10 min)

| Symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |

Tomorrow (Day 4): functions as vectors, and integrals. Skim your Day 2 notes on $\langle\varphi|\psi\rangle$ once before bed, because Day 4 replaces the sum with an integral.

## Warm-up answers (fold this section until you have attempted all five)

1. $\mathbf{u}\cdot\mathbf{v} = 3 - 2 = 1$; $|\mathbf{u}| = \sqrt{1+4} = \sqrt5$.
2. $\langle\psi| = (1-i,\ 2)$ (row, conjugated); $\langle\psi|\psi\rangle = |1+i|^2 + 4 = 2 + 4 = 6$.
3. $\langle\varphi|\chi\rangle = 1\cdot2 + (-i)(1) = 2 - i$; $\langle\chi|\varphi\rangle = 2\cdot1 + 1\cdot i = 2 + i$. The two are complex conjugates of each other (conjugate symmetry).
4. $\langle e_1|e_2\rangle = \frac{1}{25}(12 - 12) = 0$; $\langle e_1|e_1\rangle = \frac{9+16}{25} = 1$; $\langle e_2|e_2\rangle = \frac{16+9}{25} = 1$. Orthonormal. Coefficients: $c_1 = \langle e_1|(1,0)^{\mathsf T}\rangle = \frac35$, $c_2 = \frac45$, and $c_1^2 + c_2^2 = \frac{9+16}{25} = 1$.
5. $\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix} = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, but $\begin{pmatrix}1&0\\1&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}1&1\\1&2\end{pmatrix}$. Not equal: order matters.
