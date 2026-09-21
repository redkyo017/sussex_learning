# Day 2 — Vectors, Bra-Ket Notation and Inner Products

> **Physics pair for today:** [P2 — Waves, Light and the Birth of Quantum Mechanics](physics/P2.md) (~1 h 45).

**Time box (about 3.5 h):** 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Why this matters

Most Module 3 problems are linear algebra wearing a quantum costume. The week 2 lecture (§2.1, Eqs. 2.5–2.11) introduces the inner product in one page, and every later week uses it without comment: proving bra-ket identities, checking that two states are orthogonal, reading off measurement probabilities from a state expansion. Today you learn to write kets and bras as columns and rows, compute inner products by hand, and prove small identities from two axioms. The spin basis $|u\rangle, |d\rangle$ is our running example, the same one the Week 3 Task uses (the Week 3 lecture itself does not use these names; the Week 6 lecture writes the same states as $|\psi_z^\pm\rangle$ and $|\psi_x^\pm\rangle$ in Eqs. 6.1 and 6.2, and Day 3 gives the mapping).

## Warm-up (retrieval, closed book, 20 min)

Answer from memory, then check the folded answers at the bottom of the file. These come from Day 1.

1. Write the complex conjugate of $z = 2 - 3i$.
2. What is $|3 - 4i|$?
3. What is $e^{i\pi}$, and why?
4. Write $\cos 2\theta$ in terms of $\sin\theta$ alone, and write $\sin 2\theta$ in terms of $\sin\theta$ and $\cos\theta$.
5. Show that $z^* z$ is a real number for $z = a + ib$ ($a, b$ real).

## Moves

### Move 2.1 — Column vectors, dot product, length

**Say it aloud.** A *vector* is a list of numbers that we can add together and scale. A **column vector** is that list written vertically. In two dimensions:

$$\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}.$$

Adding vectors adds components. Scaling by a number $\alpha$ multiplies every component by $\alpha$.

**Dot product (real vectors).** Multiply matching components and add:

$$\mathbf{u}\cdot\mathbf{v} = u_1 v_1 + u_2 v_2.$$

**Length.** $|\mathbf{v}| = \sqrt{\mathbf{v}\cdot\mathbf{v}} = \sqrt{v_1^2 + v_2^2}$. A vector of length 1 is called *normalised*.

**Worked example.** Take $\mathbf{u} = (3, 1)^{\mathsf T}$ and $\mathbf{v} = (2, -4)^{\mathsf T}$. Then $\mathbf{u}\cdot\mathbf{v} = 6 - 4 = 2$, and $|\mathbf{u}| = \sqrt{9+1} = \sqrt{10}$.

**Why it works.** The dot product measures how much two arrows point the same way. It is zero when they are at right angles. Keep that picture: "inner product zero" will mean "perpendicular", also for complex vectors and for functions.

**Running example.** The spin basis as columns:

$$|u\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |d\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

Any two-component column is $c_u|u\rangle + c_d|d\rangle = (c_u, c_d)^{\mathsf T}$.

### Move 2.2 — Ket, bra (conjugate transpose), inner product

**Say it aloud.** A **ket**, written $|\psi\rangle$ and said "ket psi", is a column vector. A **bra**, written $\langle\psi|$ and said "bra psi", is the row vector you get from the ket by two operations together: turn the column into a row (transpose) and conjugate every entry. This is the *conjugate transpose*, also written $\dagger$:

$$|\psi\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} \quad\Longrightarrow\quad \langle\psi| = \begin{pmatrix} \psi_1^* & \psi_2^* \end{pmatrix}.$$

An **inner product** takes a bra and a ket and returns one number. Written $\langle\varphi|\psi\rangle$ and said "bra phi, ket psi", it is the row times the column:

$$\langle\varphi|\psi\rangle = \begin{pmatrix} \varphi_1^* & \varphi_2^* \end{pmatrix}\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = \varphi_1^*\psi_1 + \varphi_2^*\psi_2.$$

This matches the lecture's Eq. 2.6, $\langle u|v\rangle = \mathbf{u}^*\cdot\mathbf{v}$: conjugate the first vector, then take the dot product.

**Worked example.** Let $|a\rangle = (i, 2)^{\mathsf T}$ and $|b\rangle = (3, 1+i)^{\mathsf T}$. Then $\langle a| = (-i,\ 2)$, since $i^* = -i$ and $2^* = 2$. So

$$\langle a|b\rangle = (-i)(3) + (2)(1+i) = -3i + 2 + 2i = 2 - i.$$

Swap the roles: $\langle b| = (3,\ 1-i)$, so $\langle b|a\rangle = 3i + 2(1-i) = 2 + i$. Notice $\langle b|a\rangle = \langle a|b\rangle^*$. That is not luck; see Move 2.3.

**Why conjugate the first slot?** Try the dot product with no conjugation on the complex vector $(1, i)^{\mathsf T}$ with itself: $1\cdot 1 + i\cdot i = 1 - 1 = 0$. A non-zero vector would have "length squared" zero, which is nonsense, and complex "lengths squared" would not even be real in general. With the conjugate, we get $1^*\cdot 1 + i^*\cdot i = 1 + (-i)(i) = 1 + 1 = 2$. In general $\langle\psi|\psi\rangle = |\psi_1|^2 + |\psi_2|^2 \ge 0$, a real, non-negative number that vanishes only for the zero vector. The lecture states this in Eq. 2.7. Because probabilities in quantum mechanics are of the form $|\text{something}|^2$, we need an inner product that produces exactly such sums.

### Move 2.3 — Inner-product axioms

The course rules for inner products, in the words the course uses, are:

1. **Linearity (in the ket).** $\langle C|\{|A\rangle + |B\rangle\} = \langle C|A\rangle + \langle C|B\rangle$. The lecture (Eq. 2.9) also includes constants: $\langle\psi|\alpha_1\phi_1 + \alpha_2\phi_2\rangle = \alpha_1\langle\psi|\phi_1\rangle + \alpha_2\langle\psi|\phi_2\rangle$. Constants come straight out of the ket slot.
2. **Interchanging bras and kets corresponds to complex conjugation.** $\langle B|A\rangle = \langle A|B\rangle^*$ (lecture Eq. 2.11).
3. **Positivity.** $\langle A|A\rangle \ge 0$ (lecture Eq. 2.7).

**Consequences to remember.**

- From axioms 1 and 2 together, the bra slot is not linear but *anti-linear*: constants come out conjugated, $\langle\alpha A|B\rangle = \alpha^*\langle A|B\rangle$ (lecture Eq. 2.10). Exercise 5 asks you to prove it.
- Order matters: $\langle A|B\rangle$ and $\langle B|A\rangle$ are usually different complex numbers, but always complex conjugates of each other.

**Strategy for proofs.** Almost every bra-ket proof in the course is a two-line game: move the object you want into the slot where an axiom applies (by swapping with axiom 2), apply linearity, and swap back. Write each line with the axiom you used beside it. This is exactly the habit the six-steps write-up format rewards (see `STRATEGY.md`).

### Move 2.4 — Orthonormal basis, expansion, normalisation

**Say it aloud.** Two vectors are **orthogonal** if their inner product is zero: $\langle A|B\rangle = 0$. A vector is *normalised* if $\langle A|A\rangle = 1$. A set of vectors that are all normalised and mutually orthogonal is **orthonormal**. For $|u\rangle, |d\rangle$:

$$\langle u|u\rangle = 1,\quad \langle d|d\rangle = 1,\quad \langle u|d\rangle = 0 = \langle d|u\rangle.$$

A **basis** is a set of vectors such that every vector can be written as a combination of them. In two dimensions, an orthonormal pair is a basis.

**Expansion.** Any state can be written

$$|\psi\rangle = c_u|u\rangle + c_d|d\rangle = \sum_n c_n |n\rangle.$$

The numbers $c_n$ are the **expansion coefficients**.

**Reading off a coefficient.** Take the inner product of $|\psi\rangle$ with a basis bra and use linearity and orthonormality:

$$\langle u|\psi\rangle = c_u\langle u|u\rangle + c_d\langle u|d\rangle = c_u.$$

So $c_n = \langle n|\psi\rangle$. In column language: the coefficient is just the matching component.

**Normalisation.** The **normalisation** condition $\langle\psi|\psi\rangle = 1$ becomes, in the basis,

$$|c_u|^2 + |c_d|^2 = 1.$$

If a state is not normalised, divide by its length: $|\psi\rangle \to |\psi\rangle/\sqrt{\langle\psi|\psi\rangle}$. Later, $|c_n|^2$ will be the probability of outcome $n$, which is why this sum must be 1.

**Worked example.** The unnormalised ket $(3, 4i)^{\mathsf T}$ has $\langle\psi|\psi\rangle = 9 + 16 = 25$, so the normalised ket is $\tfrac15(3, 4i)^{\mathsf T}$, with $c_u = 3/5$ and $c_d = 4i/5$. A global phase such as $e^{i\gamma}$ multiplying the whole ket would not change any $|c_n|^2$ (Move 1.3).

### Move 2.5 — Matrix times vector, matrix multiplication (2 by 2)

A **matrix** is a rectangular grid of numbers. A $2\times 2$ matrix acts on a column by rows-times-column: each output entry is the row of the matrix dotted (no conjugation here) with the column. This is the **matrix–vector product**:

$$\begin{pmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} m_{11}v_1 + m_{12}v_2 \\ m_{21}v_1 + m_{22}v_2 \end{pmatrix}.$$

**Worked example.** With $M = \begin{pmatrix} 2 & 0 \\ 1 & -1 \end{pmatrix}$ and $\mathbf{v} = (1, 3)^{\mathsf T}$: $M\mathbf{v} = (2\cdot 1 + 0\cdot 3,\ 1\cdot 1 + (-1)\cdot 3)^{\mathsf T} = (2, -2)^{\mathsf T}$.

**Matrix times matrix.** Do the matrix–vector product once for each column of the right-hand matrix, and place the results side by side. Entry $(i,j)$ of $MN$ is (row $i$ of $M$) times (column $j$ of $N$). Order matters: in general $MN \ne NM$.

**Worked example.** $M = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $N = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Then $MN = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}$, but $NM = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}$.

## Core concepts

- **Ket** $|\psi\rangle$: a state, as a column. **Bra** $\langle\psi|$: its conjugate transpose, a row.
- **Inner product** $\langle\varphi|\psi\rangle$: bra times ket, a single complex number. Read it "the overlap of $\varphi$ with $\psi$".
- **Orthogonal / orthonormal / basis:** perpendicular; perpendicular and unit length; a set you can build everything from.
- **Expansion coefficient** $c_n = \langle n|\psi\rangle$; **normalisation** $\sum_n|c_n|^2 = 1$.
- **Matrix** and **matrix–vector product**: the machinery that lets an operator act on a ket (Day 3).
- **Notation decoded.** The angle brackets are just bookkeeping: $|\ \rangle$ says "column", $\langle\ |$ says "conjugated row". Sticking a bra next to a ket, $\langle\varphi|\psi\rangle$, is the "bracket", which is where the name comes from.
- **Function version (preview, Day 4).** For wave functions the sum becomes an integral, $\langle\psi|\phi\rangle = \int\psi^*\phi\,\mathrm{d}x$ (lecture Eq. 2.8). The same axioms hold, so everything you prove today carries over.

## Exercises

Attempt each one cold on paper for at least five minutes before opening the hint. Use the spin basis columns from Move 2.1 where relevant.

1. Let $|\varphi\rangle = (1+2i,\ 3)^{\mathsf T}$ and $|\psi\rangle = (2,\ 1-i)^{\mathsf T}$. Compute $\langle\varphi|\psi\rangle$ and $\langle\psi|\varphi\rangle$, and confirm they are complex conjugates. — **Hint:** write the bra first, conjugating every entry of $|\varphi\rangle$, then multiply entry by entry and add. — **Solution sketch:** $\langle\varphi| = (1-2i,\ 3)$, so $\langle\varphi|\psi\rangle = 2(1-2i) + 3(1-i) = 5 - 7i$. Likewise $\langle\psi| = (2,\ 1+i)$ gives $\langle\psi|\varphi\rangle = 2(1+2i) + 3(1+i) = 5 + 7i = (5-7i)^*$.

2. Find the normalisation constant $N$ (take it real and positive) such that $|\psi\rangle = N\,(1+i,\ 2-i)^{\mathsf T}$ is normalised. — **Hint:** you need $\langle\psi|\psi\rangle = N^2(|1+i|^2 + |2-i|^2) = 1$; use $|a+ib|^2 = a^2 + b^2$. — **Solution sketch:** $|1+i|^2 = 2$ and $|2-i|^2 = 5$, so $7N^2 = 1$ and $N = 1/\sqrt{7}$.

3. Show that $|\alpha\rangle = \tfrac15(3|u\rangle + 4|d\rangle)$ and $|\beta\rangle = \tfrac15(4|u\rangle - 3|d\rangle)$ form an orthonormal pair. — **Hint:** write them as columns, and check three things: $\langle\alpha|\alpha\rangle$, $\langle\beta|\beta\rangle$ and $\langle\alpha|\beta\rangle$. All entries are real, so the conjugation changes nothing here. — **Solution sketch:** $\langle\alpha|\alpha\rangle = (9+16)/25 = 1$, $\langle\beta|\beta\rangle = (16+9)/25 = 1$, $\langle\alpha|\beta\rangle = (12 - 12)/25 = 0$. So they are normalised and orthogonal.

4. Expand $|\chi\rangle = \tfrac{1}{\sqrt6}\,(1-i,\ 2)^{\mathsf T}$ in the basis $|u\rangle, |d\rangle$, and obtain the coefficients $c_u$ and $c_d$ using $c_n = \langle n|\psi\rangle$ (with $\chi$ in place of $\psi$). — **Hint:** $\langle u| = (1, 0)$ and $\langle d| = (0, 1)$; the row picks out a component. — **Solution sketch:** $c_u = \langle u|\chi\rangle = (1-i)/\sqrt6$ and $c_d = \langle d|\chi\rangle = 2/\sqrt6$, so $|\chi\rangle = \tfrac{1-i}{\sqrt6}|u\rangle + \tfrac{2}{\sqrt6}|d\rangle$. Check: $|c_u|^2 + |c_d|^2 = 2/6 + 4/6 = 1$.

5. From the two axioms (linearity in the ket; $\langle B|A\rangle = \langle A|B\rangle^*$), prove that the bra slot is anti-linear: $\langle\alpha A|B\rangle = \alpha^*\langle A|B\rangle$ for a complex number $\alpha$. — **Hint:** the axiom is about the ket slot, so use the swap axiom to move $\alpha A$ into the ket slot first. Also use $(zw)^* = z^*w^*$. — **Solution sketch:** $\langle\alpha A|B\rangle = \langle B|\alpha A\rangle^*$ (swap) $= (\alpha\langle B|A\rangle)^*$ (linearity, constants out of the ket slot) $= \alpha^*\langle B|A\rangle^*$ (conjugate a product) $= \alpha^*\langle A|B\rangle$ (swap back).

6. Show that $\langle A|B\rangle + \langle B|A\rangle$ is a real number for any two kets, and verify with the vectors of Exercise 1. — **Hint:** call $z = \langle A|B\rangle$ and ask what the second term is in terms of $z$; then recall what $z + z^*$ is. — **Solution sketch:** by the swap axiom $\langle B|A\rangle = z^*$, so the sum is $z + z^* = 2\,\mathrm{Re}\,z$, real. With Exercise 1: $(5-7i) + (5+7i) = 10$.

7. Compute $M|v\rangle$ for $M = \begin{pmatrix} 1 & i \\ -i & 2 \end{pmatrix}$ and $|v\rangle = (1+i,\ 2)^{\mathsf T}$. Then compute $MN$ and $NM$ for $N = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and state whether they are equal. — **Hint:** row times column for each output entry; recall $i^2 = -1$ and $(-i)(1+i) = -i - i^2$. — **Solution sketch:** $M|v\rangle = (1\cdot(1+i) + i\cdot 2,\ (-i)(1+i) + 2\cdot 2)^{\mathsf T} = (1+3i,\ 5-i)^{\mathsf T}$. Also $MN = \begin{pmatrix} i & 1 \\ 2 & -i \end{pmatrix}$ and $NM = \begin{pmatrix} -i & 2 \\ 1 & i \end{pmatrix}$, which are not equal.

8. For the normalised state $|\psi\rangle = \tfrac{1}{\sqrt7}\big((1+i)|u\rangle + (2-i)|d\rangle\big)$ from Exercise 2, compute $|\langle u|\psi\rangle|^2$ and $|\langle d|\psi\rangle|^2$, and check that they add to 1. — **Hint:** $\langle u|\psi\rangle$ is the $u$-component; then take the modulus squared with $|a+ib|^2 = a^2+b^2$. — **Solution sketch:** $|\langle u|\psi\rangle|^2 = |1+i|^2/7 = 2/7$ and $|\langle d|\psi\rangle|^2 = |2-i|^2/7 = 5/7$. Sum: $7/7 = 1$.

9. Let $|\varphi\rangle = a_u|u\rangle + a_d|d\rangle$ and $|\psi\rangle = c_u|u\rangle + c_d|d\rangle$. Using only the axioms and orthonormality of the basis, show that $\langle\varphi|\psi\rangle = a_u^*c_u + a_d^*c_d$. Then check it with the two vectors of Exercise 1. — **Hint:** pull the sums out with linearity in the ket slot, then anti-linearity in the bra slot (Exercise 5), and kill the cross terms with $\langle u|d\rangle = 0$. — **Solution sketch:** $\langle\varphi|\psi\rangle = c_u\langle\varphi|u\rangle + c_d\langle\varphi|d\rangle$, and $\langle\varphi|u\rangle = a_u^*\langle u|u\rangle + a_d^*\langle d|u\rangle = a_u^*$, $\langle\varphi|d\rangle = a_d^*$. So the result is $a_u^*c_u + a_d^*c_d$, which is the row-times-column formula. Check: $a = (1+2i, 3)$, $c = (2, 1-i)$ gives $5 - 7i$, matching Exercise 1.

10. A student computes $\langle\psi|\psi\rangle$ for $|\psi\rangle = (1, i)^{\mathsf T}$ by multiplying the row $(1, i)$ (no conjugation) with the column and gets $0$. Find the mistake, give the correct answer, and say why the wrong answer should have been a warning sign. — **Hint:** what must $\langle\psi|\psi\rangle$ be for a non-zero vector? Compare with the "why conjugate" discussion in Move 2.2. — **Solution sketch:** the bra of $(1, i)^{\mathsf T}$ is $(1, -i)$, not $(1, i)$. Then $\langle\psi|\psi\rangle = 1\cdot 1 + (-i)(i) = 2$. A non-zero vector cannot have zero squared length, since $\langle\psi|\psi\rangle = \sum|\psi_n|^2$ is strictly positive there.

## Apply to the lecture

Read `week_2/week_2_lecture.md` §2.1 with today's moves open beside it.

- **Postulate 1 and superposition (Eqs. 2.2–2.4).** The lecture says states form a vector space over the complex numbers. That is Move 2.1 with complex scalars $\alpha_i$. Eq. 2.3, $|\psi\rangle = \sum_i\alpha_i|\psi_i\rangle$, is the expansion of Move 2.4 written in general notation. When the $|\psi_i\rangle$ are orthonormal, $\alpha_i = \langle\psi_i|\psi\rangle$, and $|\alpha_i|^2$ is the weight of $|\psi_i\rangle$ in the state. Eq. 2.4 is written loosely in the lecture; the companion unpacks how to read it as probabilities of individual outcomes.
- **Interpretation of $c_n$.** Look for the sentence about the Born rule and the normalisation Eq. 2.1. Your check $|c_u|^2 + |c_d|^2 = 1$ is the finite-dimensional version of Eq. 2.1.
- **The inner product section (Eqs. 2.5–2.11).** Map each equation to today's moves: Eq. 2.6 is Move 2.2, Eqs. 2.9–2.11 are Move 2.3, Eq. 2.7 is the positivity axiom. Notice the lecture calls the space with an inner product a Hilbert space.
- **Next.** Read the Week 2 companion (`content/companions/week02_companion.md`), section on Postulate 1, then continue to the Week 4 companion (`content/companions/week04_companion.md`) when you get to state expansions. Day 3 turns matrices into operators.

## Anti-patterns / Common mistakes

- **Forgetting the conjugate on the bra.** Turning a ket into a bra always means conjugating each entry as well as making the column a row.
- **Assuming $\langle A|B\rangle = \langle B|A\rangle$.** They are complex conjugates, equal only when the number is real.
- **Using the row vector without conjugating.** Writing $(\psi_1, \psi_2)$ as the bra gives wrong answers for complex components, including "zero length" for a non-zero vector.
- **Pulling a constant out of the bra slot unconjugated.** Constants come out of the ket slot as they are, and out of the bra slot as their conjugate.

## Confusion log

Spend the last 10 minutes here. Note anything you could not do without looking, then write tomorrow's first question.

| Symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |

## Warm-up answers (fold: try first)

<details>
<summary>Show answers</summary>

1. $z^* = 2 + 3i$ (flip the sign of the imaginary part).
2. $|3-4i| = \sqrt{9+16} = 5$.
3. $e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0 = -1$ (Euler's formula).
4. $\cos 2\theta = 1 - 2\sin^2\theta$ (also $2\cos^2\theta - 1$); $\sin 2\theta = 2\sin\theta\cos\theta$.
5. $z^*z = (a - ib)(a + ib) = a^2 + b^2$, real and non-negative; the cross terms $iab - iab$ cancel.

</details>
