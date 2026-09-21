# Day 7 — Tensor Products, Entanglement and a Mock Problem Set

> **Physics pair for today:** [P5 — Measurement, Interpretations and Quantum Technology](physics/P5.md) (~1 h 35).

## Why this matters

Week 7 is about two quantum systems living together as one. The lecture builds a two-spin space from a *tensor product* (Section 7.1), separates *product states* from *entangled states* (7.2), lets Alice's and Bob's operators act on the composite space (7.2–7.3), and ends with quantum key distribution (7.4). Every Week 7 problem is a small calculation on four-component vectors and 4×4 matrices: test whether a state factorises, measure one half and see what is left of the other, or push a Pauli operator through a composite ket.

Today you learn those moves (Moves 7.1 to 7.5). Then you take a **Mock Problem Set** that sweeps Days 1 to 7, so you find out which earlier move is still leaky before Assessment 2 asks you to use all of them together.

Time box (about 3.5 h): warm-up 20 min, moves 60 min, exercises plus mock set 90 min (about 40 min on the exercises, then 50 min timed on the mock set), apply 40 min, confusion log 10 min.

Notation note. The lecture writes a spin as $|\uparrow\rangle, |\downarrow\rangle$ and a composite ket as $|\uparrow\downarrow\rangle$. Today we mostly write the same thing as a **qubit** (a two-level system) with basis $|0\rangle, |1\rangle$. The dictionary is $|\uparrow\rangle = |0\rangle = (1,0)^{\mathsf T}$ and $|\downarrow\rangle = |1\rangle = (0,1)^{\mathsf T}$. The lecture itself says the labels ($\uparrow\downarrow$, $0/1$, $\pm 1$, Head/Tail) do not matter; only the structure does.

## Warm-up (retrieval, 5 questions from Day 6, closed book)

Write each answer before you look at the answers at the bottom of the file.

1. Using $[\hat a, \hat a^\dagger] = 1$ and $\hat N = \hat a^\dagger \hat a$, compute $[\hat a, \hat N]$. (Move 6.4, 6.5)
2. With $\xi = x\sqrt{m\omega/\hbar}$, write $\mathrm{d}x$ in terms of $\mathrm{d}\xi$. (Move 6.1)
3. What is $\int_{-\infty}^{\infty} \xi^2 e^{-\xi^2}\,\mathrm{d}\xi$? (Move 4.4, 6.3)
4. Given $\hat H = \hbar\omega(\hat N + \tfrac12)$, what energy does the state with $\hat N = 3$ have? (Move 6.4)
5. Use $[A, BC] = [A,B]C + B[A,C]$ and $[\hat x, \hat p] = i\hbar$ to find $[\hat x, \hat p^{\,2}]$. (Move 6.5)

## Moves

### Move 7.1 — Two-qubit basis and the tensor product of kets

**Statement.** Two qubits A and B, each with basis $\{|0\rangle, |1\rangle\}$, make a composite system whose basis has $2 \times 2 = 4$ elements:

$$|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle .$$

Say it as: "ket zero-zero", and so on. The **first** label always belongs to A (Alice), the **second** to B (Bob). The lecture's Eq. (7.1) does exactly this with arrows. A ket like $|01\rangle$ is a *single* basis vector of the composite space, not two vectors.

**The tensor product** $\otimes$ (say "tensor") glues a state of A to a state of B:

$$|a\rangle \otimes |b\rangle = |ab\rangle .$$

**By hand on basis kets first.** Use the standard column vectors $|0\rangle = (1,0)^{\mathsf T}$, $|1\rangle = (0,1)^{\mathsf T}$.

$$|0\rangle \otimes |1\rangle = |01\rangle = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}.$$

The four basis kets of the composite space are the four standard unit vectors, in the order $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ (positions 1 to 4).

**The Kronecker product** is the rule that makes this work for any column vectors. For $(a, b)^{\mathsf T} \otimes (c, d)^{\mathsf T}$, multiply the whole second vector by each entry of the first, and stack:

$$\begin{pmatrix}a\\b\end{pmatrix}\otimes\begin{pmatrix}c\\d\end{pmatrix} = \begin{pmatrix}a\,c\\a\,d\\b\,c\\b\,d\end{pmatrix}.$$

**Worked example.** Take $|+\rangle \equiv \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle) = \tfrac{1}{\sqrt2}(1,1)^{\mathsf T}$ and combine it with $|0\rangle$:

$$|+\rangle \otimes |0\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1\cdot 1\\1\cdot 0\\1\cdot 1\\1\cdot 0\end{pmatrix} = \frac{1}{\sqrt2}\begin{pmatrix}1\\0\\1\\0\end{pmatrix} = \frac{1}{\sqrt2}(|00\rangle + |10\rangle).$$

Distributing $\otimes$ over the sum gives the same answer: $\tfrac{1}{\sqrt2}(|0\rangle\otimes|0\rangle + |1\rangle\otimes|0\rangle)$. Rule: $\otimes$ is linear in each slot.

**Order matters.** $|0\rangle \otimes |1\rangle = |01\rangle \ne |10\rangle = |1\rangle \otimes |0\rangle$. The first slot is Alice's, always.

**Orthonormality carries over** (lecture, just after Table 7.1):

$$\langle ab | a'b' \rangle = \delta_{a,a'}\,\delta_{b,b'} .$$

Say it as: the inner product is 1 only if *both* labels match, otherwise 0.

**Counting.** Dimensions multiply: quantum coin (2) times quantum die (6) gives 12; three qubits give $2^3 = 8$ basis kets.

### Move 7.2 — Tensor product of operators

**Statement.** To act on one qubit only, pad with the identity $\mathbb 1$ on the other. Alice's operator is $\sigma \otimes \mathbb 1$; Bob's is $\mathbb 1 \otimes \tau$ (the lecture, Section 7.2; it then drops the $\otimes\,\mathbb 1$ and writes just $\sigma$ or $\tau$). The rule for how they act:

$$(A \otimes B)\,(|a\rangle \otimes |b\rangle) = (A|a\rangle) \otimes (B|b\rangle) .$$

Say it as: each operator acts on its own qubit and leaves the other alone.

**By hand on kets (do this first).** With $\sigma_x|0\rangle = |1\rangle$ and $\sigma_z|1\rangle = -|1\rangle$:

$$(\sigma_z \otimes \sigma_x)(|1\rangle \otimes |0\rangle) = (\sigma_z|1\rangle) \otimes (\sigma_x|0\rangle) = -|1\rangle \otimes |1\rangle = -|11\rangle .$$

**The Kronecker product of matrices.** Replace every entry of $A$ by that entry times the whole matrix $B$:

$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B\\ a_{21}B & a_{22}B\end{pmatrix}.$$

For two $2\times2$ matrices this is $4 \times 4$.

**The 4×4 for $\sigma_x \otimes \mathbb 1$.** Here $A = \sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $B = \mathbb 1$, so the blocks are $0\cdot\mathbb 1$ and $1\cdot\mathbb 1$:

$$\sigma_x \otimes \mathbb 1 = \begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}.$$

Check on $|01\rangle = (0,1,0,0)^{\mathsf T}$: the matrix returns its second column, $(0,0,0,1)^{\mathsf T} = |11\rangle$. In words: $\sigma_x$ flips Alice's qubit, Bob's stays as it was. This matches the ket rule: $(\sigma_x|0\rangle)\otimes|1\rangle = |11\rangle$.

**The 4×4 for $\mathbb 1 \otimes \sigma_z$.** Now $A = \mathbb 1$ and $B = \sigma_z$, so each diagonal block is $\sigma_z$:

$$\mathbb 1 \otimes \sigma_z = \begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.$$

It leaves the first label alone and gives $+1$ if Bob's label is 0, $-1$ if it is 1.

**Why Alice's and Bob's operators commute.** They touch different slots, so the order does not matter: $(\sigma\otimes\mathbb 1)(\mathbb 1\otimes\tau) = \sigma \otimes \tau = (\mathbb 1\otimes\tau)(\sigma\otimes\mathbb 1)$. (The lecture uses this in Section 7.3 to say both can be measured simultaneously.)

### Move 7.3 — The product-state test: $ad = bc$

**Statement.** A general two-qubit state is

$$|\psi\rangle = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle .$$

It is a **product state** (factorises as $|\text{A}\rangle \otimes |\text{B}\rangle$) if and only if $ad = bc$. Otherwise it is **entangled**.

**Proof in five lines.**

1. Multiply out a product: $(\alpha|0\rangle + \beta|1\rangle)\otimes(\gamma|0\rangle + \delta|1\rangle) = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle$ (compare the lecture's Eq. 7.3).
2. So a product has $a = \alpha\gamma$, $b = \alpha\delta$, $c = \beta\gamma$, $d = \beta\delta$.
3. Then $ad = \alpha\gamma\beta\delta = (\alpha\delta)(\beta\gamma) = bc$. So *product implies* $ad = bc$.
4. Conversely, suppose $ad = bc$ and $a \neq 0$. Choose $\alpha = a,\ \beta = c,\ \gamma = 1,\ \delta = b/a$. Then $\alpha\gamma = a$, $\alpha\delta = b$, $\beta\gamma = c$, and $\beta\delta = bc/a = d$. So it factorises.
5. If $a = 0$, then $bc = 0$. If $b = 0$ the state is $|1\rangle\otimes(c|0\rangle + d|1\rangle)$; if $c = 0$ it is $(b|0\rangle + d|1\rangle)\otimes|1\rangle$. Both are products.

Normalisation does not matter for the test: multiplying all four amplitudes by the same constant multiplies both sides of $ad = bc$ by its square.

**Say it aloud.** "$ad$ is the product of the two diagonal amplitudes; $bc$ is the product of the two off-diagonal ones. A product state has them equal." Diagonal means $|00\rangle$ and $|11\rangle$; off-diagonal means $|01\rangle$ and $|10\rangle$.

**Three new states, tested.**

- $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$: $a = d = 1/\sqrt2$, $b = c = 0$. $ad = \tfrac12 \ne 0 = bc$. **Entangled.**
- $\tfrac12(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$: all amplitudes $\tfrac12$, so $ad = \tfrac14 = bc$. **Product.** Factorise: $\tfrac{1}{\sqrt2}(|0\rangle + |1\rangle) \otimes \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle) = |+\rangle \otimes |+\rangle$.
- $\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$: $a = d = 0$, $b = c = 1/\sqrt2$. $ad = 0 \ne \tfrac12 = bc$. **Entangled.**

**Two terms is not the same as entangled.** $\tfrac{1}{\sqrt2}(|00\rangle + |01\rangle)$ has two terms, yet $ad = 0 = bc$, and it equals $|0\rangle \otimes |+\rangle$. A product state can be a superposition; what it cannot do is have its two halves depend on each other.

**Parameter count (lecture, Section 7.2).** A product state needs 4 real parameters; the general two-qubit state needs 6. The two extra dimensions are where entanglement lives.

### Move 7.4 — Partial measurement: project, renormalise, read off the other qubit

**Statement.** You measure only *one* qubit in the $\{|0\rangle, |1\rangle\}$ basis. Then:

1. **Group** the terms of $|\psi\rangle$ by the outcome you got on the measured qubit.
2. **Probability** of that outcome is the sum of $|\text{amplitude}|^2$ over the terms in the group (this is Move 5.1 applied to a sub-sum).
3. **Collapse:** keep only that group. This is the projection $P|\psi\rangle$ (Move 5.3).
4. **Renormalise:** divide by the square root of the probability so the state has length 1.
5. **Read off** the other qubit from what is left, and take $|\text{amplitude}|^2$ for its distribution.

**Worked example (new state).** Let

$$|\psi\rangle = \frac{1}{\sqrt6}\big(|00\rangle + 2|10\rangle + |11\rangle\big).$$

Check: $1 + 4 + 1 = 6$, so it is normalised. Measure the **first** qubit.

*Outcome 1 on the first qubit.* The terms with first label 1 are $2|10\rangle + |11\rangle$. Probability $= \tfrac{4 + 1}{6} = \tfrac56$.
Projected, unnormalised: $\tfrac{1}{\sqrt6}(2|10\rangle + |11\rangle) = \tfrac{1}{\sqrt6}|1\rangle \otimes (2|0\rangle + |1\rangle)$.
Renormalise by dividing by $\sqrt{5/6}$: the new state is $|1\rangle \otimes \tfrac{1}{\sqrt5}(2|0\rangle + |1\rangle)$.
Now measure the second qubit: $P(0) = \tfrac45$, $P(1) = \tfrac15$.

*Outcome 0 on the first qubit.* Only $|00\rangle$ remains, probability $\tfrac16$. The new state is $|00\rangle$, so the second qubit is 0 with certainty.

Check: $\tfrac16 + \tfrac56 = 1$. The joint probability of "first = 1, second = 0" is $\tfrac56 \cdot \tfrac45 = \tfrac23 = \tfrac46$, matching the squared amplitude of $|10\rangle$, which is $\tfrac46$.

**Sanity check with Move 7.3.** $a = 1, b = 0, c = 2, d = 1$: $ad = 1 \ne 0 = bc$. Entangled, and consistent with what we saw: the second qubit's distribution *depends* on the first qubit's outcome ($(1,0)$ versus $(\tfrac45,\tfrac15)$). For a product state the conditional distribution would be the same whichever outcome you got.

**Forgetting to renormalise** is the standard error: after collapse you must divide by $\sqrt{P}$, otherwise the second distribution would come out as $\tfrac{4}{6},\tfrac{1}{6}$, which does not sum to 1.

### Move 7.5 — Bell states, correlations, and what entanglement does not imply

**The four Bell states** (an orthonormal basis of two qubits):

$$|\Phi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|00\rangle \pm |11\rangle\big), \qquad |\Psi^\pm\rangle = \tfrac{1}{\sqrt2}\big(|01\rangle \pm |10\rangle\big).$$

They are orthonormal. **Your turn:** for each of the four, read off $a, b, c, d$ (the amplitudes of $|00\rangle, |01\rangle, |10\rangle, |11\rangle$) and compare $ad$ with $bc$ (Move 7.3). Record your verdict yourself. The lecture's arrow-language names for these states are in Eq. (7.6): one of them is called the **singlet** $\tfrac{1}{\sqrt2}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ and three are the **triplet** states $\psi_{\mathrm T1}, \psi_{\mathrm T2}, \psi_{\mathrm T3}$; match them to the four kets above by writing $\uparrow=0$, $\downarrow=1$. Below we practise on $|\Phi^+\rangle$ and $|\Psi^+\rangle$.

**Composite observables** are products like $\sigma_z \otimes \sigma_z$ (the lecture's $\tau_z\sigma_z$). Its eigenvalue tells you whether the two results agree ($+1$) or disagree ($-1$).

*Worked example.* Apply $\sigma_z \otimes \sigma_z$ to $|\Phi^+\rangle$: $|00\rangle \to (+1)(+1)|00\rangle$ and $|11\rangle \to (-1)(-1)|11\rangle$. So $|\Phi^+\rangle$ is an eigenvector with eigenvalue $+1$: measured in the $z$ basis, Alice and Bob always **agree**. Applying it to $|\Psi^+\rangle$: $|01\rangle \to (+1)(-1)|01\rangle$ and $|10\rangle \to (-1)(+1)|10\rangle$, eigenvalue $-1$: they always **disagree**.

**Each side alone looks random.** In $|\Phi^+\rangle$, Alice's outcome is 0 or 1 with probability $\tfrac12$ each; so is Bob's. $\langle \sigma_z \otimes \mathbb 1\rangle = \tfrac12(+1) + \tfrac12(-1) = 0$, likewise for Bob, while $\langle \sigma_z\otimes\sigma_z\rangle = +1$.

**Correlation.** The lecture-style measure of how much two results move together is

$$\text{correlation} = \langle AB\rangle - \langle A\rangle\langle B\rangle .$$

For $|\Phi^+\rangle$ and $A = \sigma_z\otimes\mathbb1$, $B = \mathbb1\otimes\sigma_z$: $1 - 0\cdot 0 = 1$, the maximum. For a product state the correlation is always 0 (each side is independent).

**Correlated is not communicating.** The results are correlated, but Alice cannot use the correlation to send Bob a message. Bob's outcomes are 50/50 whatever Alice does (Exercise 9 proves it for $|\Phi^+\rangle$). The correlation only shows up when the two of them *compare notes* over an ordinary channel. That is exactly how quantum key distribution (lecture Section 7.4) works: each gets a random string, the strings match, and no message travelled between them through the entanglement. So entangled states do **not** allow faster-than-light signalling; what they defy is the classical idea that each particle carries its own pre-set answer. The lecture's phrase is that in an entangled state you can know everything about the whole and nothing about the parts.

## Core concepts

- **Composite system:** two systems treated as one; states live in the tensor product space, dimension = product of dimensions.
- **Tensor product / Kronecker product:** $\otimes$ is the abstract operation; the Kronecker product is how you compute it on column vectors and matrices.
- **Product state:** $|\psi_{\rm A}\rangle\otimes|\psi_{\rm B}\rangle$. Independent preparations; test: $ad = bc$.
- **Entangled state:** not a product state.
- **Bell states, singlet:** the four two-qubit states $|\Phi^\pm\rangle, |\Psi^\pm\rangle$ of Move 7.5 (test each with $ad = bc$); the lecture's singlet and triplet names label these four.
- **Partial measurement:** measure one qubit; project, renormalise, read off the other.
- **Correlation:** joint statistics not explained by the separate ones.
- **Qubit:** a two-level quantum system, the smallest building block; a spin-1/2 is one (Week 6 link).

## Exercises

1. Compute, as column vectors with four entries, (a) $|1\rangle\otimes|0\rangle$ and (b) $\tfrac{1}{\sqrt2}(|0\rangle - |1\rangle)\otimes|1\rangle$. — **Hint:** use $(a,b)^{\mathsf T}\otimes(c,d)^{\mathsf T} = (ac, ad, bc, bd)^{\mathsf T}$; or expand into basis kets and place a 1 at the right position. — **Solution sketch:** (a) $|10\rangle = (0,0,1,0)^{\mathsf T}$. (b) expanding gives $\tfrac{1}{\sqrt2}(|01\rangle - |11\rangle) = \tfrac{1}{\sqrt2}(0,1,0,-1)^{\mathsf T}$. Check length: $\tfrac12(1+1) = 1$.

2. Write $|+\rangle\otimes|0\rangle$ and $|0\rangle\otimes|+\rangle$ as four-component vectors, with $|+\rangle = \tfrac{1}{\sqrt2}(|0\rangle+|1\rangle)$. Are they equal? Then find the position (1 to 8) of $|101\rangle$ in a three-qubit vector. — **Hint:** the order of the tensor factors sets which slot changes fastest; for three qubits, read the label as a binary number and add 1. — **Solution sketch:** $|+\rangle\otimes|0\rangle = \tfrac{1}{\sqrt2}(1,0,1,0)^{\mathsf T}$; $|0\rangle\otimes|+\rangle = \tfrac{1}{\sqrt2}(1,1,0,0)^{\mathsf T}$. Not equal: order of factors matters. $|101\rangle$: binary 101 = 5, so position $5+1 = 6$.

3. Using the $4\times4$ matrix for $\sigma_x\otimes\mathbb 1$ from Move 7.2, compute its action on $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$. Name the result. — **Hint:** the vector is $\tfrac{1}{\sqrt2}(1,0,0,1)^{\mathsf T}$; multiply row by row. — **Solution sketch:** rows give $(v_3, v_4, v_1, v_2)$, so the result is $\tfrac{1}{\sqrt2}(0,1,1,0)^{\mathsf T} = \tfrac{1}{\sqrt2}(|01\rangle + |10\rangle) = |\Psi^+\rangle$. Alice's flip turned one Bell state into another. Ket check: $(\sigma_x\otimes\mathbb1)|00\rangle = |10\rangle$, $|11\rangle \to |01\rangle$.

4. Build the $4\times4$ matrix of $\mathbb 1\otimes\sigma_y$ (with $\sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$) and apply it to $|10\rangle$. Verify with the ket rule. — **Hint:** the matrix is block-diagonal with two copies of $\sigma_y$; $|10\rangle = (0,0,1,0)^{\mathsf T}$ picks the third column. — **Solution sketch:** $\mathbb1\otimes\sigma_y = \begin{pmatrix}\sigma_y&0\\0&\sigma_y\end{pmatrix}$, third column $(0,0,0,i)^{\mathsf T}$, so the result is $i|11\rangle$. Ket rule: $|1\rangle\otimes(\sigma_y|0\rangle) = |1\rangle\otimes i|1\rangle = i|11\rangle$. Same.

5. Decide product or entangled, and factorise if product: (a) $\tfrac{1}{\sqrt{50}}(|00\rangle + 2|01\rangle + 3|10\rangle + 6|11\rangle)$; (b) $\tfrac12(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$. — **Hint:** compute $ad$ and $bc$ from the four amplitudes; for (a) guess factors $(|0\rangle + x|1\rangle)\otimes(|0\rangle + y|1\rangle)$ and match. — **Solution sketch:** (a) $ad = 6$, $bc = 6$: product; $(|0\rangle + 3|1\rangle)\otimes(|0\rangle + 2|1\rangle)/\sqrt{50}$, normalisation $\sqrt{10}\cdot\sqrt5 = \sqrt{50}$. (b) $ad = -\tfrac14$, $bc = \tfrac14$: entangled.

6. Find the value of $\lambda$ that makes $\dfrac{1}{N}\big(|00\rangle + \lambda|01\rangle + |10\rangle + 2|11\rangle\big)$ a product state, then find $N$ so it is normalised. — **Hint:** impose $ad = bc$ on the unnormalised amplitudes $1, \lambda, 1, 2$. — **Solution sketch:** $1\cdot 2 = \lambda\cdot 1$, so $\lambda = 2$. Then $N^2 = 1 + 4 + 1 + 4 = 10$, $N = \sqrt{10}$. Factorised: $(|0\rangle + |1\rangle)\otimes(|0\rangle + 2|1\rangle)/\sqrt{10}$.

7. The state is $|\psi\rangle = \tfrac{1}{\sqrt{10}}\big(|00\rangle + |01\rangle + 2|10\rangle - 2|11\rangle\big)$. Measure the **second** qubit and get 1. Give the probability of that outcome, the state afterwards, and the distribution for the first qubit. Then repeat for outcome 0, and compare. — **Hint:** group terms by the second label: outcome 1 keeps $|01\rangle$ and $-2|11\rangle$; divide by the square root of the probability. — **Solution sketch:** outcome 1: probability $\tfrac{1+4}{10} = \tfrac12$; state $\tfrac{1}{\sqrt5}(|0\rangle - 2|1\rangle)\otimes|1\rangle$; first qubit $P(0) = \tfrac15$, $P(1) = \tfrac45$. Outcome 0: probability $\tfrac12$; state $\tfrac{1}{\sqrt5}(|0\rangle + 2|1\rangle)\otimes|0\rangle$; same $\tfrac15,\tfrac45$. The $z$-distributions agree but the states differ by a sign. Here $ad = -2 \ne 2 = bc$: entangled, even though $z$-statistics alone cannot show it.

8. Compute $(\sigma_x\otimes\sigma_x)|\Phi^+\rangle$ and $(\sigma_x\otimes\sigma_x)|\Phi^-\rangle$. What does each eigenvalue say about Alice's and Bob's $x$-results? — **Hint:** $\sigma_x$ swaps $0 \leftrightarrow 1$, so $\sigma_x\otimes\sigma_x$ swaps $|00\rangle \leftrightarrow |11\rangle$. — **Solution sketch:** $|\Phi^+\rangle \to \tfrac{1}{\sqrt2}(|11\rangle + |00\rangle) = +|\Phi^+\rangle$, eigenvalue $+1$: $x$-results always agree. $|\Phi^-\rangle \to \tfrac{1}{\sqrt2}(|11\rangle - |00\rangle) = -|\Phi^-\rangle$, eigenvalue $-1$: they always disagree.

9. Alice and Bob share $|\Phi^+\rangle$. Show that Bob's probability of reading 0 in the $z$ basis is $\tfrac12$ whether or not Alice measures first (and not knowing her result). What does this tell you about faster-than-light signalling? — **Hint:** case 1: read off the amplitude of the terms with Bob's label 0 directly. Case 2: Alice gets 0 or 1 with probability $\tfrac12$ each, collapsing to $|00\rangle$ or $|11\rangle$; average over her outcomes. — **Solution sketch:** case 1: only $|00\rangle$ has Bob = 0, so $P = |1/\sqrt2|^2 = \tfrac12$. Case 2: $P = \tfrac12\cdot 1 + \tfrac12\cdot 0 = \tfrac12$. Same either way, so Bob sees no change caused by Alice's action. The correlation only appears after they compare results by an ordinary channel: no signal.

## Mock Problem Set

Ten mixed problems covering Days 1 to 7. The objects are new (none repeats a day exercise), but the techniques are the ones you practised. Set a timer for **50 minutes**; aim for about 5 minutes per problem, and skip any problem that stalls you. Write each answer in the six-steps format from `STRATEGY.md` (stand-in version): Restate, Write the state, Name the move, Algebra, Check, Answer. Only then open the hint, and only then the solution sketch. Each problem is worth 4 marks (see the rubric below).

1. **[Day 1: Moves 1.2, 1.3, 1.4]** (a) Write $z = 1 - i$ in the form $r e^{i\theta}$ and compute $z^8$. (b) Use a double-angle identity to give $\cos^2(\pi/12)$ exactly. — **Hint:** (a) $r = |z| = \sqrt{z^* z}$ and $\theta$ from the point $(1,-1)$; raise to the 8th power using $e^{i\theta n}$. (b) $\cos^2\theta = \tfrac12(1 + \cos 2\theta)$ with $2\theta = \pi/6$. — **Solution sketch:** (a) $|z|^2 = (1+i)(1-i) = 2$, $z = \sqrt2\,e^{-i\pi/4}$, $z^8 = 16\,e^{-2\pi i} = 16$. (b) $\cos^2(\pi/12) = \tfrac12(1 + \cos\tfrac\pi6) = \tfrac12(1 + \tfrac{\sqrt3}{2}) = \tfrac{2+\sqrt3}{4}\approx0.933$.

2. **[Day 2: Moves 2.2, 2.3, 2.4]** In an orthonormal basis $\{|1\rangle, |2\rangle\}$ let $|\varphi\rangle = 2|1\rangle - i|2\rangle$ and $|\psi\rangle = |1\rangle + (1+i)|2\rangle$. Find $\langle\varphi|\psi\rangle$ and $\langle\psi|\varphi\rangle$, normalise $|\psi\rangle$, and give the probability of finding $|1\rangle$ in the normalised state. — **Hint:** the bra $\langle\varphi|$ has *conjugated* coefficients: $2\langle1| + i\langle2|$. Expect $\langle\psi|\varphi\rangle = \langle\varphi|\psi\rangle^*$. — **Solution sketch:** $\langle\varphi|\psi\rangle = 2\cdot1 + i(1+i) = 1 + i$; $\langle\psi|\varphi\rangle = 1 - i$, the conjugate. $\langle\psi|\psi\rangle = 1 + |1+i|^2 = 3$, so the normalised state is $\tfrac{1}{\sqrt3}\big(|1\rangle + (1+i)|2\rangle\big)$ and $P(1) = \tfrac13$.

3. **[Day 3: Move 3.2, 3.3]** For $M = \begin{pmatrix}1&2\\2&-2\end{pmatrix}$ find the eigenvalues and normalised eigenvectors, check that the eigenvectors are orthogonal, and say why that had to happen. — **Hint:** solve $\det(M - \lambda\mathbb1) = 0$; for each $\lambda$ solve one row of $(M-\lambda\mathbb1)v = 0$ and normalise. — **Solution sketch:** $\lambda^2 + \lambda - 6 = 0$, so $\lambda = 2, -3$. For $\lambda = 2$: $-x + 2y = 0$, $v = (2,1)^{\mathsf T}/\sqrt5$. For $\lambda = -3$: $4x + 2y = 0$, $v = (1,-2)^{\mathsf T}/\sqrt5$. Dot product $2 - 2 = 0$. $M$ is real symmetric, so Hermitian, so its eigenvalues are real and eigenvectors for different eigenvalues are orthogonal.

4. **[Day 3: Moves 3.4, 3.5, 3.3]** Compute $[\sigma_y, \sigma_z]$ using the Pauli matrices, express it in terms of a single Pauli matrix, and decide whether $i[\sigma_y,\sigma_z]$ is Hermitian. — **Hint:** multiply $\sigma_y\sigma_z$ and $\sigma_z\sigma_y$ separately, subtract; for the last part use $(cA)^\dagger = c^*A^\dagger$. — **Solution sketch:** $\sigma_y\sigma_z = \begin{pmatrix}0&i\\i&0\end{pmatrix}$, $\sigma_z\sigma_y = \begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, difference $\begin{pmatrix}0&2i\\2i&0\end{pmatrix} = 2i\,\sigma_x$. Then $i[\sigma_y,\sigma_z] = -2\sigma_x$, which is Hermitian ($\sigma_x^\dagger = \sigma_x$, and $-2$ is real).

5. **[Day 4: Moves 4.4, 4.5, 4.6, 4.7]** Let $\psi(x) = C\,x^2\,e^{-x^2}$ on the whole real line. Check it is an acceptable wave function, find $C$, and compute $\langle x\rangle$ and $\langle x^2\rangle$. — **Hint:** $|\psi|^2 = C^2x^4e^{-2x^2}$, so $a = 2$. Get $\int x^4e^{-ax^2}\,\mathrm{d}x$ by differentiating $\int x^2e^{-ax^2}\,\mathrm{d}x = \tfrac{\sqrt\pi}{2a^{3/2}}$ with respect to $a$ and changing sign; differentiate once more for $\int x^6e^{-ax^2}\,\mathrm{d}x$. For $\langle x\rangle$ look at the parity of the integrand. — **Solution sketch:** finite, smooth, single-valued, and $|\psi|^2$ dies away fast enough to be normalisable. $\int x^4e^{-ax^2}\,\mathrm{d}x = \tfrac{3\sqrt\pi}{4a^{5/2}}$, which at $a=2$ is $\tfrac{3\sqrt\pi}{16\sqrt2}$, so $C^2 = \tfrac{16\sqrt2}{3\sqrt\pi}\approx4.26$. $\langle x\rangle = C^2\int x^5e^{-2x^2}\,\mathrm{d}x = 0$ (odd integrand). $\int x^6e^{-ax^2}\,\mathrm{d}x = \tfrac{15\sqrt\pi}{8a^{7/2}}$, which at $a=2$ is $\tfrac{15\sqrt\pi}{64\sqrt2}$, so $\langle x^2\rangle = \tfrac{16\sqrt2}{3\sqrt\pi}\cdot\tfrac{15\sqrt\pi}{64\sqrt2} = \tfrac54$.

6. **[Day 4 and Day 6: Moves 4.4, 6.3]** For $\psi(x) = C\,x\,e^{-x^2/4}$ on the whole real line, find $C$, then $\langle x\rangle$, $\langle x^2\rangle$ and $\sigma_x$. — **Hint:** $|\psi|^2 = C^2x^2e^{-x^2/2}$, so $a = \tfrac12$; use $\int x^2e^{-ax^2}\,\mathrm{d}x = \tfrac{\sqrt\pi}{2a^{3/2}}$, and $\int x^4 e^{-ax^2}\,\mathrm{d}x = \tfrac{3\sqrt\pi}{4a^{5/2}}$ (differentiate the first with respect to $a$ and change sign); for $\langle x\rangle$ look at the parity of the integrand. — **Solution sketch:** at $a=\tfrac12$, $a^{3/2} = \tfrac{1}{2\sqrt2}$ so $\int x^2e^{-x^2/2}\,\mathrm{d}x = \sqrt{2\pi}$, giving $C^2 = \tfrac{1}{\sqrt{2\pi}}$. $\langle x\rangle$: integrand $x^3e^{-x^2/2}$ is odd, so 0. $a^{5/2} = \tfrac{1}{4\sqrt2}$ so $\int x^4e^{-x^2/2}\,\mathrm{d}x = 3\sqrt{2\pi}$, and $\langle x^2\rangle = \tfrac{3\sqrt{2\pi}}{\sqrt{2\pi}} = 3$. Hence $\sigma_x = \sqrt3$.

7. **[Day 5: Moves 5.1, 5.2, 5.3]** An observable $\hat A$ has normalised eigenstates $|a_1\rangle$ (eigenvalue 3) and $|a_2\rangle$ (eigenvalue $-1$). The state is $|\psi\rangle = \tfrac{1}{\sqrt5}\big(|a_1\rangle + 2i\,|a_2\rangle\big)$. Find the probabilities of each result, $\langle\hat A\rangle$, and the state and the outcome of an immediate second measurement if the first gave 3. — **Hint:** $|c_n|^2$ with $c_2 = 2i/\sqrt5$ means $|c_2|^2 = c_2^*c_2 = 4/5$; the average is $\sum |c_n|^2 a_n$. — **Solution sketch:** $P(3) = \tfrac15$, $P(-1) = \tfrac45$, sum 1. $\langle\hat A\rangle = \tfrac35 - \tfrac45 = -\tfrac15$. After the result 3 the state is $|a_1\rangle$, and a repeat measurement gives 3 with certainty.

8. **[Day 5: Moves 5.4, 5.5, 5.1]** A particle in a box of width $L$ (walls at $x = 0$ and $x = L$). Solve $\psi'' = -k^2\psi$ with $\psi(0) = \psi(L) = 0$ to find the allowed $k$, and $E$ from $E = \hbar^2k^2/2m$. Normalise the lowest state. Given the state $\Psi = \tfrac{1}{5}(3\psi_1 + 4\psi_2)$ with $\psi_n$ normalised energy eigenstates, what is the probability of measuring $E_2$? — **Hint:** general solution $A\sin kx + B\cos kx$; $\psi(0)=0$ removes $B$, then $\psi(L)=0$ forces $kL = n\pi$. For normalisation use $\int_0^L\sin^2(\pi x/L)\,\mathrm{d}x = L/2$. — **Solution sketch:** $k_n = n\pi/L$, $E_n = \tfrac{n^2\pi^2\hbar^2}{2mL^2}$, $\psi_1 = \sqrt{2/L}\sin(\pi x/L)$. $P(E_2) = |4/5|^2 = \tfrac{16}{25}$; also $P(E_1) = \tfrac{9}{25}$ and the sum is 1.

9. **[Day 6: Moves 6.4, 6.5]** With $[\hat a,\hat a^\dagger] = 1$, $\hat N = \hat a^\dagger\hat a$, $[\hat N,\hat a] = -\hat a$ and $\hat H = \hbar\omega(\hat N + \tfrac12)$, show $[\hat N, \hat a^2] = -2\hat a^2$. Suppose $\hat N|n\rangle = n|n\rangle$. Show that $\hat a^2|n\rangle$ is an eigenvector of $\hat N$ (or is zero) and give its energy. — **Hint:** write $\hat a^2 = \hat a\hat a$ and use $[A, BC] = [A,B]C + B[A,C]$; then rearrange the result as $\hat N\hat a^2 = \hat a^2\hat N - 2\hat a^2$ and apply both sides to $|n\rangle$. — **Solution sketch:** $[\hat N,\hat a\hat a] = [\hat N,\hat a]\hat a + \hat a[\hat N,\hat a] = -\hat a^2 - \hat a^2 = -2\hat a^2$. So $\hat N\hat a^2|n\rangle = (\hat a^2\hat N - 2\hat a^2)|n\rangle = (n-2)\hat a^2|n\rangle$: eigenvalue $n-2$ (two rungs down). Energy $\hbar\omega(n - 2 + \tfrac12) = \hbar\omega(n - \tfrac32)$.

10. **[Day 7: Moves 7.1 to 7.4]** $|\chi\rangle = \tfrac{1}{\sqrt{10}}\big(3|00\rangle + |11\rangle\big)$. (a) Is it a product state? (b) Measure the second qubit; if you get 1, what is the state of the first qubit? (c) Compute $\langle\sigma_z\otimes\mathbb1\rangle$. — **Hint:** (a) write the amplitudes as $c_{00} = 3/\sqrt{10}$, $c_{11} = 1/\sqrt{10}$, $c_{01} = c_{10} = 0$ and use the product-state test $c_{00}c_{11} = c_{01}c_{10}$ (the $ad = bc$ test of Move 7.3). (b) keep only the terms with second label 1 and renormalise. (c) $(\sigma_z\otimes\mathbb1)|jk\rangle = \pm|jk\rangle$ with $+$ if $j = 0$; use $\langle\chi|\ldots|\chi\rangle = \sum|{\rm amplitude}|^2\cdot(\pm1)$. — **Solution sketch:** (a) $c_{00}c_{11} = \tfrac{3}{10} \ne 0 = c_{01}c_{10}$: entangled. (b) Outcome 1 has probability $\tfrac{1}{10}$; the state collapses to $|11\rangle$, so the first qubit is $|1\rangle$ with certainty. (c) $\tfrac{9}{10}(+1) + \tfrac{1}{10}(-1) = \tfrac45$.

### Scoring rubric

Score each problem out of 4 marks:

| Mark | What earns it |
|---|---|
| Method (1) | Restated the problem, wrote the state, and named the right move before calculating. |
| Algebra (1) | Algebra shown and every step correct: signs, conjugates, factors, order of tensor factors. |
| Check (1) | Ran a check: normalisation sums to 1, orthogonality, limiting case, or $ad$ versus $bc$. |
| Answer (1) | Stated the answer in a full sentence, with correct labels or units. |

Total is out of 40. **34 to 40:** ready, move to Assessment work. **26 to 33:** redo the flagged moves in the table below, then re-attempt those problems fresh. **Below 26:** revisit the day file for each flagged move and re-do its exercises cold before trying the mock again.

### Which move do I retry?

| If you went wrong on... | Retry this move | Day |
|---|---|---|
| Problem 1: modulus, polar form, or a double-angle result | 1.2, 1.3, 1.4 | Day 1 |
| Problem 2: missing conjugates on a bra, wrong sign, or unnormalised state | 2.2, 2.3, 2.4 | Day 2 |
| Problem 3: eigenvalues or eigenvectors wrong, or no orthogonality check | 3.2, 3.3 | Day 3 |
| Problem 4: commutator arithmetic or Hermitian check | 3.4, 3.5, 3.3 | Day 3 |
| Problem 5: integral wrong, wrong $C$, or forgot acceptability checks | 4.4, 4.5, 4.6, 4.7 | Day 4 |
| Problem 6: Gaussian integral or odd-integrand shortcut | 4.4, 6.3 | Day 4 and Day 6 |
| Problem 7: probabilities not $|c_n|^2$, or no collapse | 5.1, 5.2, 5.3 | Day 5 |
| Problem 8: box boundary conditions or energy formula | 5.4, 5.5 | Day 5 |
| Problem 9: commutator algebra or ladder logic | 6.4, 6.5 | Day 6 |
| Problem 10(a): wrong $ad = bc$ verdict | 7.3 | Day 7 |
| Problem 10(b): forgot to renormalise, wrong conditional state | 7.4 | Day 7 |
| Problem 10(c) or any tensor-product operator action | 7.1, 7.2 | Day 7 |
| Any problem: right method, wrong final number | Redo with the **Check** habit from Move 5.1 (does it sum to 1?) | Day 5 |

## Apply to the lecture

You already have everything the Week 7 lecture uses. Read `week_7/week_7_lecture.md` now, with the Week 7 Companion (`content/companions/week07_companion.md`) open, in this order:

1. Section 7.1 (composite systems): find the coin-and-die table; it is Move 7.1 with 2 and 6 in place of 2 and 2. Find Eq. (7.3) and match it to step 1 of the Move 7.3 proof.
2. Section 7.2 (entangled states): find the singlet and triplet in Eq. (7.6), and match them to the Bell-state dictionary above. Follow the spin-operator table and Eq. (7.7): each line is Move 7.2 with the identity in the passive slot. Look for how the lecture computes expectation values in a composite state.
3. Section 7.3 (composite observables): find where $\tau_z\sigma_z$ is applied to a state and the eigenvalue $-1$ read off; that is the eigenvalue reading of Move 7.5.
4. Section 7.4 (QKD): read it as an application of "correlated but not communicating".

The link back to Week 6: a spin-1/2 in a Stern-Gerlach apparatus **is** the qubit. The Pauli matrices from Day 3 act on it, and today you learned to run two of them in parallel. Use the Week 6 Companion (`content/companions/week06_companion.md`) if you need the physical picture back.

Now open the Week 7 quiz and task problems, and, before you read any solutions, ask yourself for each one: which move is this (7.1 to 7.5), and can I write the setup?

## Anti-patterns / Common mistakes

- **Treating any two-term superposition as entangled.** The test is $ad = bc$, not "how many terms". $\tfrac{1}{\sqrt2}(|00\rangle + |01\rangle) = |0\rangle\otimes|+\rangle$ is a product state.
- **Forgetting to renormalise after a partial collapse.** After measuring one qubit, divide by $\sqrt{P}$. If the second distribution does not sum to 1, this is why.
- **Mixing up the ordering of tensor factors.** The first label is Alice's, the second is Bob's; $|01\rangle \neq |10\rangle$ and $\sigma_x\otimes\mathbb1 \neq \mathbb1\otimes\sigma_x$. Write the slot labels above your kets if you are prone to slips.
- **Saying "correlated" means "communicates".** No: each side alone is random.

## Confusion log

| Symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |

## Answers to the warm-up

1. $[\hat a, \hat N] = [\hat a, \hat a^\dagger\hat a] = [\hat a,\hat a^\dagger]\hat a + \hat a^\dagger[\hat a,\hat a] = \hat a$.
2. $x = \xi\sqrt{\hbar/(m\omega)}$, so $\mathrm{d}x = \sqrt{\hbar/(m\omega)}\,\mathrm{d}\xi$.
3. $\dfrac{\sqrt\pi}{2}$ (from $\int x^2e^{-ax^2}\,\mathrm{d}x = \sqrt\pi/(2a^{3/2})$ with $a=1$).
4. $\hbar\omega(3 + \tfrac12) = \tfrac72\hbar\omega$.
5. $[\hat x, \hat p^{\,2}] = [\hat x,\hat p]\hat p + \hat p[\hat x,\hat p] = 2i\hbar\hat p$.
