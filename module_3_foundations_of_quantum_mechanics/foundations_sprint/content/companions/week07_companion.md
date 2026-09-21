# Week 7 Companion — Composite Systems and Entanglement

Built on [Day 2](../day02.md) (bras, kets, orthonormal bases), [Day 3](../day03.md) (operators, Pauli matrices) and [Day 7](../day07.md) (Moves 7.1 to 7.5). Reading method: [STRATEGY](../../STRATEGY.md), five passes. Use this page beside `week_7/week_7_lecture.md`.

## What this week is really saying

**One sentence:** if you want to describe two particles, you need *one* state for the pair, and some pair-states cannot be cut into "a state for A" times "a state for B".

Three ideas, in plain English.

1. **Two particles, one state.** A single spin has two basis states, up and down. Two spins do not have "two plus two" states; they have four, because you must say what *both* are doing: up-up, up-down, down-up, down-down. The state of the pair is a list of four amplitudes. (The lecture's coin and die: 2 times 6 = 12 amplitudes.) The tensor product $\otimes$ is the rule for building this bigger space.
2. **Some pair-states factorise, some do not.** If Alice and Bob prepare their spins independently, the pair-state is a *product state*: (Alice's state) $\otimes$ (Bob's state). Then each side behaves as if the other did not exist. But the four amplitudes of a general pair-state are free (only their squared moduli must sum to 1), so most pair-states are *not* products. These are *entangled*. The lecture's summary: you can know everything about the pair and nothing about the parts.
3. **Correlation without a message.** In certain entangled states, when both spins are measured in matching bases, the two results agree (or disagree) perfectly when compared, yet each result alone is a fair coin flip. Measuring Alice's spin changes what you should *predict* for Bob's, but Bob, on his own, sees no change at all in his statistics. Nothing is sent. The link only appears when they compare notes by an ordinary channel; that is exactly how the key distribution of Section 7.4 works.

**Physical picture.** Two Stern-Gerlach boxes, Alice's and Bob's, fed by one source. Each box is a qubit reader. The source can send two independent spins (product state) or a pair that was prepared *together* (entangled). Independent spins give uncorrelated readings. A pair prepared together can give readings that always match, even though each box alone looks random.

## Notation decoder

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\otimes$ | "tensor" | glue a state of A to a state of B to make a state of the pair | $\lvert 1\rangle\otimes\lvert 0\rangle = \lvert 10\rangle$ |
| $S_{\rm AB} = S_{\rm A}\otimes S_{\rm B}$ | "S-A-B is S-A tensor S-B" | the composite system; dimensions multiply | 3-level system with 4-level system: $3\times4 = 12$ basis kets |
| $\lvert\uparrow\downarrow\rangle$ | "up-down" | one single basis ket of the pair: Alice up, Bob down. First label is Alice's | $\lvert\uparrow\downarrow\rangle\ne\lvert\downarrow\uparrow\rangle$ |
| $\lvert 00\rangle$ | "ket zero-zero" | same thing with qubit labels, $\uparrow\to0$, $\downarrow\to1$ | $\lvert 01\rangle$ is Alice 0, Bob 1 |
| $\lvert\psi_{\rm AB}\rangle$, $\sum_{a,b}\alpha(a,b)\lvert ab\rangle$ | "psi-A-B", "sum over a and b of alpha of a-b" | general pair-state: one amplitude per pair of labels | four amplitudes for two qubits |
| $\langle ab\vert a'b'\rangle=\delta_{a,a'}\delta_{b,b'}$ | "delta a a-prime times delta b b-prime" | inner product is 1 only if both labels match, else 0 | $\langle 01\vert 01\rangle=1$, $\langle 01\vert 11\rangle=0$ |
| $\phi_{\uparrow\downarrow}$ | "phi up-down" | the amplitude of $\lvert\uparrow\downarrow\rangle$ in Eq. (7.4) | probability of that outcome is $\lvert\phi_{\uparrow\downarrow}\rvert^2$ |
| $\sigma_x,\sigma_y,\sigma_z$ and $\tau_x,\tau_y,\tau_z$ | "sigma", "tau" | Pauli matrices; $\sigma$ is Alice's set, $\tau$ is Bob's | $\sigma_x\lvert\uparrow\rangle=\lvert\downarrow\rangle$ |
| $\sigma\otimes\mathbb 1$ | "sigma tensor identity" | Alice's operator: acts on Alice's slot, leaves Bob's alone. The lecture then writes just $\sigma$ | $(\sigma_x\otimes\mathbb1)\lvert01\rangle=\lvert11\rangle$ |
| $\mathbb 1\otimes\tau$ | "identity tensor tau" | Bob's operator; written just $\tau$ | $(\mathbb1\otimes\tau_x)\lvert01\rangle=\lvert00\rangle$ |
| $\tau_z\sigma_z$ | "tau-z sigma-z" | composite observable: product of Alice's and Bob's operators; eigenvalue tells whether the two $z$-results agree ($+1$) or disagree ($-1$) | acts on $\lvert 01\rangle$ as $(+1)(-1)$, so $-\lvert01\rangle$ |
| product state (separable) | "product state" | can be written as (state of A) $\otimes$ (state of B). Test: $ad=bc$ | $\lvert0\rangle\otimes\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$ |
| entangled state | "entangled" | not a product state: $ad\ne bc$ | four amplitudes $0,\,1,\,1,\,0$ over $\sqrt2$ |
| Bell states $\Phi^\pm,\Psi^\pm$ | "Bell states" | the four orthonormal maximally entangled two-qubit states | see [Day 7, Move 7.5](../day07.md) |
| singlet $\psi_{\rm S}$, triplet $\psi_{{\rm T}1,2,3}$ | "singlet", "triplet" | the lecture's names (Eq. 7.6) for the Bell states; the singlet is the one with the minus sign between the two opposite-spin kets | same four states as the Bell states, different labels |
| $\langle\sigma_z\rangle$ | "expectation of sigma-z" | average of many $\pm1$ results; $0$ means $+1$ and $-1$ equally likely, not "no result" | fair coin: $\tfrac12(+1)+\tfrac12(-1)=0$ |

Careful with **spin labels**: the lecture says the labels ($\uparrow\downarrow$, $0/1$, $\pm1$, Head/Tail) do not matter. Only the structure does.

## Skipped steps, expanded

### 1. Why the Kronecker product is the right rule (Eqs. 7.1 to 7.3)

The lecture goes from $[\alpha_\uparrow\lvert\uparrow\rangle+\alpha_\downarrow\lvert\downarrow\rangle]\otimes[\beta_\uparrow\lvert\uparrow\rangle+\beta_\downarrow\lvert\downarrow\rangle]$ straight to four terms (Eq. 7.3). The missing step is a single rule: **$\otimes$ is linear in each slot** ([Move 2.3](../day02.md) style linearity, once for each slot).

- Expand the first bracket: $\alpha_\uparrow\lvert\uparrow\rangle\otimes[\ldots]+\alpha_\downarrow\lvert\downarrow\rangle\otimes[\ldots]$. Numbers can be pulled out of a slot.
- Expand each remaining bracket the same way. Four terms result, each of the form (number) $\lvert{\rm a}\rangle\otimes\lvert{\rm b}\rangle=$ (number) $\lvert{\rm ab}\rangle$.

Now the *column-vector* form. Order the basis as $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$ (first label changes slowest). For $(a,b)^{\mathsf T}\otimes(c,d)^{\mathsf T}$ the four amplitudes are $ac,\,ad,\,bc,\,bd$, so the column is $(ac,ad,bc,bd)^{\mathsf T}$. That is "each entry of the first vector times the whole second vector". Nothing else is being assumed; the Kronecker recipe is just the expansion above written in a column.

**Operators, same logic.** $(A\otimes B)\lvert j\,k\rangle=(A\lvert j\rangle)\otimes(B\lvert k\rangle)$. The matrix entry in row $(i,l)$, column $(j,k)$ is $A_{ij}B_{lk}$. Row label $(i,l)$ sits at position $2i+l$ (counting from 0), so all rows with the same $i$ form a block, and block $(i,j)$ is $A_{ij}\,B$. That is the "replace each entry of $A$ by that entry times $B$" recipe. It is a consequence, not a separate rule.

### 2. The product-state test $ad=bc$ (Eq. 7.4 onwards)

The lecture *says* the singlet and triplets cannot be factorised ("it is impossible to find the values") and leaves the checking to you. The quick tool is [Move 7.3](../day07.md), and here is a picture for it.

Write the four amplitudes as a $2\times2$ table (rows: Alice's label, columns: Bob's label):

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}.$$

A product state has amplitudes $\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta$, so the table is (column of $\alpha,\beta$) times (row of $\gamma,\delta$). Its two rows are copies of the same row, scaled: row 1 is $\alpha(\gamma,\delta)$, row 2 is $\beta(\gamma,\delta)$. Two rows are proportional exactly when the $2\times2$ determinant vanishes, and that determinant is $ad-bc$. That is why the test is $ad=bc$ (you met the $2\times2$ determinant on [Day 3](../day03.md)).

Physical reading: rows proportional means "whatever Alice gets, Bob's leftover state is the same". Product means no dependence. Entangled means Bob's state depends on Alice's result. The next section shows this directly.

### 3. Projection and renormalisation in a partial measurement

The lecture's postulate ([Move 5.3](../day05.md), collapse) is stated for a full state. For a pair you measure only one slot. Write the general state $\lvert\psi\rangle=a\lvert00\rangle+b\lvert01\rangle+c\lvert10\rangle+d\lvert11\rangle$ and measure Alice's qubit.

1. **Outcome 0 means the state must now be built from kets whose first label is 0.** The projector is $P_0=\lvert0\rangle\langle0\rvert\otimes\mathbb1$. Acting on $\lvert\psi\rangle$ it keeps $a\lvert00\rangle+b\lvert01\rangle$ and deletes the rest.
2. **Probability of outcome 0** is the length-squared of what survives: $\langle\psi\rvert P_0\lvert\psi\rangle=\lvert a\rvert^2+\lvert b\rvert^2$ ([Move 5.1](../day05.md): probabilities are $\lvert\text{amplitude}\rvert^2$, and you add the ones that lead to the same outcome).
3. **Renormalise.** What survives has length-squared $\lvert a\rvert^2+\lvert b\rvert^2<1$, but a state must have total probability 1 ([Move 2.4](../day02.md)), so divide by $\sqrt{\lvert a\rvert^2+\lvert b\rvert^2}$. The new state is $\lvert0\rangle\otimes\dfrac{a\lvert0\rangle+b\lvert1\rangle}{\sqrt{\lvert a\rvert^2+\lvert b\rvert^2}}$.
4. **Read off Bob's statistics:** $P(\text{Bob}=0)=\lvert a\rvert^2/(\lvert a\rvert^2+\lvert b\rvert^2)$ and $P(\text{Bob}=1)=\lvert b\rvert^2/(\lvert a\rvert^2+\lvert b\rvert^2)$. These are *conditional* probabilities, so they sum to 1 (that is the sanity check).
5. **Link to Section 2 above.** After outcome 1, Bob's leftover is $(c,d)$. So Bob's leftover is the same for both outcomes exactly when $(a,b)\propto(c,d)$, i.e. $ad=bc$. Product state: measuring Alice tells you nothing new about Bob.

The joint probability of "Alice 0 and Bob 0" is $\lvert a\rvert^2$ whichever route you take (measure Alice first, or Bob first). Use this as your consistency check.

**How the lecture's expectation-value calculation works (Section 7.2), on a fresh state.** The lecture computes $\langle\sigma_z\rangle=\langle\psi\lvert\sigma_z\rvert\psi\rangle$ in nine lines with the singlet. The recipe, which you can apply to *any* state and which I show here on $\lvert\chi\rangle=\tfrac13(\lvert01\rangle+2\lvert10\rangle+2\lvert11\rangle)$ (norm: $1+4+4=9$, so $\tfrac13$ is right):

- (i) Pull the numerical factor outside: $\tfrac19$ from $(\tfrac13)^2$ (the lecture's $\tfrac12$).
- (ii) Let the operator act on the ket first: $(\sigma_z\otimes\mathbb1)\lvert\chi\rangle=\tfrac13(\lvert01\rangle-2\lvert10\rangle-2\lvert11\rangle)$, because $\sigma_z$ gives $+$ on Alice's 0 and $-$ on Alice's 1.
- (iii) Take the inner product with the bra of the *original* state and use $\langle ab\vert a'b'\rangle=\delta\delta$: cross terms vanish, matching terms give amplitude products: $\tfrac19(1\cdot1+2\cdot(-2)+2\cdot(-2))=\tfrac19(1-4-4)=-\tfrac79$.
- (iv) Check by probabilities: $P(\text{Alice}=0)=\tfrac19$ (from $\lvert01\rangle$), $P(\text{Alice}=1)=\tfrac89$, so $\langle\sigma_z\rangle=\tfrac19(+1)+\tfrac89(-1)=-\tfrac79$. Same.

**Composite observable line (Section 7.3).** "Apply $\sigma_z$ first, then $\tau_z$": the order is irrelevant because they act on different slots ([Move 7.2](../day07.md)), and each operator only multiplies a basis ket by $\pm1$ according to its own label. So $\tau_z\sigma_z\lvert ab\rangle=(\pm1)_a(\pm1)_b\lvert ab\rangle$: $+1$ if the labels *agree*, $-1$ if they differ. An eigenvector of $\tau_z\sigma_z$ is a state built only from kets with the same product sign.

**Section 7.4 (key distribution), one link only.** When Eve measures one photon, that is a collapse ([Move 5.3](../day05.md)). The pair is left in a state with definite polarisations, which is a product state: her measurement destroys the entanglement, and the tests Alice and Bob run on the compared data reveal that. The lecture's no-cloning claim is quoted from outside sources, so treat it as a stated result here, not something this companion proves.

**Not covered.** The lecture cites Susskind (2014, Section 6.6) for the parameter count (4 real parameters for a product, 6 for a general pair). The file `susskind.pdf` is in the resources folder (`exteral_resources`) but I have not read it, so this companion does not summarise it. The parameter count itself is stated in the lecture (Section 7.2) and is in [Move 7.3](../day07.md) of Day 7.

## Moves used this week

| Move | Where it is used | Taught on |
|---|---|---|
| 2.4 Orthonormal basis, expansion, normalisation | the four-ket basis, $\langle ab\vert a'b'\rangle=\delta\delta$, normalising a pair-state | [Day 2](../day02.md) |
| 3.1 Operators as matrices; how an operator acts on a ket | $\sigma_{x,y,z}$ on single spins (the lecture's table before Eq. 7.7) | [Day 3](../day03.md) |
| 3.4 Pauli matrices | $\sigma$ and $\tau$ operators and eigenvalues $\pm1$ | [Day 3](../day03.md) |
| 5.3 Collapse | partial measurement; Eve's measurement in Section 7.4 | Day 5 |
| 7.1 Two-qubit basis and tensor product of kets | Section 7.1, Eqs. 7.1 to 7.3 | [Day 7](../day07.md) |
| 7.2 Tensor product of operators | $\sigma\otimes\mathbb1$, $\mathbb1\otimes\tau$, Eq. 7.7 | [Day 7](../day07.md) |
| 7.3 Product-state test $ad=bc$ | product versus entangled, Eqs. 7.4 and 7.6 | [Day 7](../day07.md) |
| 7.4 Partial measurement | conditional states and probabilities | [Day 7](../day07.md) |
| 7.5 Bell states, correlations | Section 7.3 composite observables; Section 7.4 | [Day 7](../day07.md) |

## Worked clones

Each clone has the **same type** as a Week 7 task problem but uses different states and operators. I do not solve the task problems themselves.

### Clone 1 — Is it a product state? (type of Task Problem 1)

*Type:* given a two-qubit state, decide whether it can be written as $\lvert{\rm A}\rangle\otimes\lvert{\rm B}\rangle$, and if so give the factors; if not, say why no factors exist.

**State (a):** $\tfrac12(\lvert00\rangle+i\lvert01\rangle+\lvert10\rangle+i\lvert11\rangle)$.

1. Restate: product or entangled? Given: $a=1,\ b=i,\ c=1,\ d=i$ (all over 2).
2. [Move 7.3](../day07.md): compare $ad$ and $bc$ (normalisation does not matter).
3. $ad=1\cdot i=i$; $bc=i\cdot1=i$. Equal, so **product**.
4. Find factors: rows are $(1,i)$ and $(1,i)$, identical, so Alice's amplitudes are equal and Bob's is $(1,i)$. Try $\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\otimes\tfrac{1}{\sqrt2}(\lvert0\rangle+i\lvert1\rangle)$. Expanding: $\tfrac12(\lvert00\rangle+i\lvert01\rangle+\lvert10\rangle+i\lvert11\rangle)$. It matches.
5. Check: norm of the original is $\tfrac14(1+1+1+1)=1$ (each $\lvert i\rvert=1$). Each factor has norm $\tfrac12(1+1)=1$. Good.

**State (b):** $\tfrac{1}{\sqrt7}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+2\lvert11\rangle)$.

- $a=1,b=1,c=1,d=2$: $ad=2$, $bc=1$. Not equal, so **entangled**. Norm check: $1+1+1+4=7$. Good.
- *Why no factorisation exists* (the type of argument the task asks for): a product would need $\alpha\gamma=1$, $\alpha\delta=1$, $\beta\gamma=1$ so $\gamma=\delta$ and $\alpha=\beta$, and then $\beta\delta=\alpha\gamma=1\ne2$. Contradiction.

**State (c):** $\tfrac{1}{\sqrt{26}}(3\lvert00\rangle-3\lvert01\rangle+2\lvert10\rangle-2\lvert11\rangle)$.

- $ad=3\cdot(-2)=-6$, $bc=(-3)\cdot2=-6$. Equal: **product**. Rows $(3,-3)$ and $(2,-2)$ are proportional. Factors: $(3\lvert0\rangle+2\lvert1\rangle)\otimes(\lvert0\rangle-\lvert1\rangle)/\sqrt{26}$, since $\sqrt{(9+4)(1+1)}=\sqrt{26}$. Expanding gives $3\lvert00\rangle-3\lvert01\rangle+2\lvert10\rangle-2\lvert11\rangle$. Good.

### Clone 2 — Partial measurement (type of Task Problem 2)

*Type:* normalise a three-term pair-state, measure one qubit, give the post-measurement state, then the possible results and probabilities for the other qubit, and say whether it is entangled.

**State:** $\lvert\psi\rangle=B\,(\lvert01\rangle+2\lvert10\rangle+2\lvert11\rangle)$, $B$ real and positive.

1. **Normalise ([Move 2.4](../day02.md)).** $B^2(1+4+4)=1$, so $B=\tfrac13$.
2. **Measure the first qubit and get 0 ([Move 7.4](../day07.md)).** Terms with first label 0: only $\tfrac13\lvert01\rangle$. Probability $=\tfrac19$. After renormalising, the state is $\lvert01\rangle$. Measuring the second qubit now gives 1 with probability 1.
3. **Measure the first qubit and get 1.** Terms with first label 1: $\tfrac13(2\lvert10\rangle+2\lvert11\rangle)$. Probability $=\tfrac{4+4}{9}=\tfrac89$. Renormalise (divide by $\sqrt{8/9}$, i.e. by $\tfrac{2\sqrt2}{3}$): state $=\dfrac{2\lvert10\rangle+2\lvert11\rangle}{2\sqrt2}=\lvert1\rangle\otimes\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$. Second qubit: $0$ or $1$, each with probability $\tfrac12$.
4. **Check:** $\tfrac19+\tfrac89=1$. Joint probability "first 1, second 0" is $\tfrac89\cdot\tfrac12=\tfrac49=\left\lvert\tfrac23\right\rvert^2$, the squared amplitude of $\lvert10\rangle$. Good.
5. **Entangled?** $a=0,b=\tfrac13,c=\tfrac23,d=\tfrac23$: $ad=0$, $bc=\tfrac29$. Not equal: **entangled**. Confirmed by the conditional states: Bob's state is $\lvert1\rangle$ after Alice gets 0 but $\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$ after Alice gets 1. They differ.
6. **Bonus cross-check by measuring the second qubit first.** Outcome 0: only $\tfrac23\lvert10\rangle$, probability $\tfrac49$, state $\lvert10\rangle$. Outcome 1: $\tfrac13\lvert01\rangle+\tfrac23\lvert11\rangle$, probability $\tfrac{1+4}{9}=\tfrac59$, state $\tfrac{1}{\sqrt5}(\lvert0\rangle+2\lvert1\rangle)\otimes\lvert1\rangle$. Sum: $\tfrac49+\tfrac59=1$. Joint "second 1, first 1": $\tfrac59\cdot\tfrac45=\tfrac49$, the same as before.

### Clone 3 — A composite operator acting on a product state (type of Task Problem 3)

*Type:* apply a tensor-product operator to a product state and decide whether the result is still a product state.

**Operator and state.** $\sigma_z\otimes\sigma_x$ on $\lvert\Pi\rangle=\tfrac15(3\lvert0\rangle+4i\lvert1\rangle)\otimes\tfrac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$.

**By the ket rule ([Move 7.2](../day07.md)).** $(\sigma_z\otimes\sigma_x)(\lvert u\rangle\otimes\lvert v\rangle)=(\sigma_z\lvert u\rangle)\otimes(\sigma_x\lvert v\rangle)$.

- $\sigma_z(3\lvert0\rangle+4i\lvert1\rangle)=3\lvert0\rangle-4i\lvert1\rangle$.
- $\sigma_x(\lvert0\rangle-\lvert1\rangle)=\lvert1\rangle-\lvert0\rangle=-(\lvert0\rangle-\lvert1\rangle)$.
- Result: $-\tfrac{1}{5\sqrt2}(3\lvert0\rangle-4i\lvert1\rangle)\otimes(\lvert0\rangle-\lvert1\rangle)$. It is still a product state (its two factors are visible).

**By the $4\times4$ matrix ([Move 7.2](../day07.md), Kronecker).** $\sigma_z\otimes\sigma_x=\begin{pmatrix}\sigma_x&0\\0&-\sigma_x\end{pmatrix}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}$. The product state as a column: $\tfrac{1}{5\sqrt2}(3,\,-3,\,4i,\,-4i)^{\mathsf T}$. Multiplying: row 1 gives entry 2, row 2 gives entry 1, row 3 gives minus entry 4, row 4 gives minus entry 3:

$$\tfrac{1}{5\sqrt2}(-3,\ 3,\ 4i,\ -4i)^{\mathsf T}.$$

This agrees with the ket-rule result (expand $-(3\lvert0\rangle-4i\lvert1\rangle)\otimes(\lvert0\rangle-\lvert1\rangle)$ to get $-3,\,3,\,4i,\,-4i$).

**Checks.** (1) Norm: $\tfrac{1}{50}(9+9+16+16)=1$. (2) Product test on the result: $a=-3,b=3,c=4i,d=-4i$ gives $ad=12i$ and $bc=12i$. Equal. Product.

**Why it must work.** The rule $(A\otimes B)(\lvert u\rangle\otimes\lvert v\rangle)=(A\lvert u\rangle)\otimes(B\lvert v\rangle)$ hands back a ket that is already written as a product. So *any* single tensor-product operator $A\otimes B$ maps product states to product states.

**When a state does become entangled.** The guarantee is only for operators of the form $A\otimes B$. An operator that is a *sum* of such terms can entangle. Example: the controlled-NOT, $\lvert0\rangle\langle0\rvert\otimes\mathbb1+\lvert1\rangle\langle1\rvert\otimes\sigma_x$, on $\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\otimes\lvert0\rangle$ gives $\tfrac{1}{\sqrt2}(\lvert0\rangle\otimes\lvert0\rangle+\lvert1\rangle\otimes\sigma_x\lvert0\rangle)=\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$, with $ad=\tfrac12\ne0=bc$.

## Retrieval questions

Closed book first. Each item names the misconception it traps.

1. Compute $(1,2)^{\mathsf T}\otimes(3,-1)^{\mathsf T}$ as a four-entry column, then state the dimension of the composite of a 3-level system with a 4-level one. *(Traps: adding dimensions instead of multiplying; mis-ordering the Kronecker entries.)* — **Hint:** first vector's entry times the whole second vector; dimension is a product. — **Solution sketch:** $(1\cdot3,\ 1\cdot(-1),\ 2\cdot3,\ 2\cdot(-1))^{\mathsf T}=(3,-1,6,-2)^{\mathsf T}$. Dimension $3\times4=12$, not 7.

2. Is $\tfrac{1}{\sqrt5}(2\lvert10\rangle+\lvert11\rangle)$ entangled? *(Traps: "a superposition of two kets must be entangled".)* — **Hint:** compute $ad$ and $bc$; here $a=b=0$. — **Solution sketch:** $ad=0=bc$, so it is a product: $\lvert1\rangle\otimes\tfrac{1}{\sqrt5}(2\lvert0\rangle+\lvert1\rangle)$. Norm $4+1=5$. A superposition inside one slot is not entanglement between slots.

3. Compute $(\sigma_x\otimes\mathbb1)\lvert01\rangle$ and $(\mathbb1\otimes\sigma_x)\lvert01\rangle$. *(Traps: mixing up which slot an operator acts on.)* — **Hint:** first label is Alice's; $\sigma_x$ flips $0\leftrightarrow1$ in *its own* slot only. — **Solution sketch:** $(\sigma_x\otimes\mathbb1)\lvert01\rangle=\lvert11\rangle$ (Alice's 0 flips); $(\mathbb1\otimes\sigma_x)\lvert01\rangle=\lvert00\rangle$ (Bob's 1 flips). Different results, so the operators differ.

4. Alice and Bob share $\tfrac{1}{\sqrt5}(2\lvert00\rangle+\lvert11\rangle)$. What is the probability Bob reads 0 if Alice does nothing? What if Alice measures (Bob is not told her result) and Bob then measures? *(Traps: "measuring Alice's qubit sends a signal that changes Bob's statistics".)* — **Hint:** case 1: use the amplitude of the only ket with Bob's label 0; case 2: average Bob's conditional probability over Alice's outcomes, weighted by their probabilities. — **Solution sketch:** case 1: $\lvert2/\sqrt5\rvert^2=\tfrac45$. Case 2: Alice gets 0 with probability $\tfrac45$ (state $\lvert00\rangle$, Bob reads 0 for sure) and 1 with probability $\tfrac15$ (state $\lvert11\rangle$, Bob reads 0 never): $\tfrac45\cdot1+\tfrac15\cdot0=\tfrac45$. Same either way, so Alice cannot signal Bob. Her choice only matters once they compare records.

5. Section 7.4 says the key bits "do not exist yet" between the source and the polarisers. Why is this different from Alice and Bob simply having agreed a list of answers in advance? *(Traps: "hidden information" carried by each particle.)* — **Hint:** what does the lecture (Section 7.2) say about the completeness of the state vector? What does the state predict for one side taken alone? — **Solution sketch:** for the entangled pair, the lecture says the state vector is as complete a description as possible and, taken alone, each side's outcome is equally likely $+1$ or $-1$ (all single-spin expectation values are 0). So there is nothing more to "read off" than the ket; the bit is only fixed at measurement. Whether a pre-agreed list can imitate the correlations (Bell-type tests) is beyond this week's text; I have not read the external resources, so I do not claim more here.

6. Take $\tfrac12(\lvert00\rangle-\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$. Compute $\langle\sigma_z\otimes\sigma_z\rangle$, $\langle\sigma_z\otimes\mathbb1\rangle$, $\langle\mathbb1\otimes\sigma_z\rangle$ and the correlation $\langle AB\rangle-\langle A\rangle\langle B\rangle$. Is the state a product state? *(Traps: "entangled = correlated", or "zero correlation proves product".)* — **Hint:** each ket has weight $\tfrac14$; $\sigma_z\otimes\sigma_z$ gives $+1$ when the labels agree and $-1$ when they differ; then apply $ad=bc$. — **Solution sketch:** $\langle\sigma_z\otimes\sigma_z\rangle=\tfrac14(+1-1-1+1)=0$; $\langle\sigma_z\otimes\mathbb1\rangle=\tfrac14(+1+1-1-1)=0$; $\langle\mathbb1\otimes\sigma_z\rangle=\tfrac14(+1-1+1-1)=0$; correlation $0-0\cdot0=0$. But $ad=1\cdot1=1$, $bc=(-1)(1)=-1$, so it **is entangled**. So the $z$-$z$ correlation being 0 does not show a product state; the test is $ad=bc$. (The other direction does hold: a product state has zero correlation.)

7. State $\tfrac{1}{\sqrt{11}}(\lvert00\rangle+3\lvert01\rangle+\lvert11\rangle)$. Measure the second qubit and get 1. Give the probability, the post-measurement state, and the distribution for the first qubit; then say what goes wrong if you divide by $\sqrt{11}$ instead of the correct number. *(Traps: forgetting to renormalise after collapse.)* — **Hint:** keep the terms with second label 1; the correct divisor is the square root of *their* total probability. — **Solution sketch:** kept: $\tfrac{1}{\sqrt{11}}(3\lvert01\rangle+\lvert11\rangle)$, probability $\tfrac{9+1}{11}=\tfrac{10}{11}$. Divide by $\sqrt{10/11}$: state $\tfrac{1}{\sqrt{10}}(3\lvert0\rangle+\lvert1\rangle)\otimes\lvert1\rangle$; first qubit $P(0)=\tfrac9{10}$, $P(1)=\tfrac1{10}$. Dividing by $\sqrt{11}$ only would give $\tfrac9{11},\tfrac1{11}$, which sum to $\tfrac{10}{11}$, not 1. Check: outcome 0 has probability $\tfrac1{11}$, and $\tfrac{10}{11}+\tfrac1{11}=1$.

8. For $\lvert\Phi^-\rangle=\tfrac{1}{\sqrt2}(\lvert00\rangle-\lvert11\rangle)$, compute $\langle\sigma_z\otimes\mathbb1\rangle$ and the eigenvalue of $\sigma_z\otimes\sigma_z$. Does "expectation 0" mean Alice's result is 0? *(Traps: reading an expectation value as an outcome.)* — **Hint:** the outcomes of $\sigma_z$ are $\pm1$; weight them by probabilities. For $\sigma_z\otimes\sigma_z$, apply it to each ket. — **Solution sketch:** $P(+1)=P(-1)=\tfrac12$ so the expectation is 0, but no single result is 0: each run gives $+1$ or $-1$. $\sigma_z\otimes\sigma_z$: $\lvert00\rangle\to(+1)(+1)$, $\lvert11\rangle\to(-1)(-1)=+1$, so $\sigma_z\otimes\sigma_z\lvert\Phi^-\rangle=+\lvert\Phi^-\rangle$: eigenvalue $+1$, results always agree.

9. Give a one-line reason why a single tensor-product operator such as $A\otimes B$ can never turn a product state into an entangled one, and name one operator that can. *(Traps: "any two-qubit operator preserves product states".)* — **Hint:** write out $(A\otimes B)(\lvert u\rangle\otimes\lvert v\rangle)$. — **Solution sketch:** the ket rule gives $(A\lvert u\rangle)\otimes(B\lvert v\rangle)$; look at what form that has. The controlled-NOT (a sum of two tensor-product terms) turns $\lvert+\rangle\otimes\lvert0\rangle$ into $\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$.

## Six-steps write-up template

Uses the stand-in six steps from [STRATEGY](../../STRATEGY.md) (the university page is not in the local exports).

**Product or entangled**
1. Restate the state; list $a,b,c,d$.
2. Write the $2\times2$ table of amplitudes.
3. Name [Move 7.3](../day07.md): product iff $ad=bc$.
4. Compute $ad$ and $bc$; if equal, factor by matching rows; if not equal, show the factorisation cannot exist.
5. Check: normalisation, and that any factors multiply back to the original.
6. Answer in a sentence: "The state is a product/entangled because ...".

**Partial measurement**
1. Restate which qubit is measured and which result is observed.
2. Write the state with a normalisation constant $A$ (or $B$) if unknown.
3. Name Moves 2.4, 7.4 and 5.3.
4. (i) Find the constant from $\sum\lvert\text{amp}\rvert^2=1$. (ii) Keep the terms matching the outcome; probability is their $\lvert\text{amp}\rvert^2$ sum. (iii) Divide by its square root. (iv) Read off the other qubit's probabilities.
5. Check: conditional probabilities sum to 1; joint probabilities match squared amplitudes; compare the conditional states for each outcome and link to $ad=bc$.
6. Answer with the state, probability and results, and a stated verdict on entanglement.

**Composite operator**
1. Restate the operator and the state.
2. Write kets in slot order (Alice, Bob).
3. Name [Move 7.2](../day07.md): $(A\otimes B)(\lvert u\rangle\otimes\lvert v\rangle)=(A\lvert u\rangle)\otimes(B\lvert v\rangle)$.
4. Apply each factor to its own ket; simplify each; optionally verify with the $4\times4$ Kronecker matrix.
5. Check: norm unchanged for unitary operators such as Paulis; $ad=bc$ on the result.
6. Answer: "The result is $\ldots$, still a product state, because each operator acted on its own slot."

## Portfolio method note

Week 7's Consolidate task involves expectation values and a correlation in a two-spin state. This note is **method only**; it contains no answers and no calculation on the state or operators the portfolio uses.

- **Expectation value:** $\langle O\rangle=\langle\psi\rvert O\lvert\psi\rangle$. Apply the operator to the ket first (use the single-spin rules and the lecture's Eq. 7.7 pattern, one slot at a time), then take the inner product with the bra of the original state. Cross terms die by orthonormality, matching terms give products of amplitudes (Skipped step 3 above shows the four sub-steps).
- **Watch the order and which slot:** for a composite operator the two factors act on different slots, so their order does not matter, but you must not lose the phase factors that $\sigma_y$ produces. A conjugated amplitude appears when you form the bra.
- **Correlation:** $\langle AB\rangle-\langle A\rangle\langle B\rangle$ needs three numbers: the joint expectation, and each side's expectation on its own. Compute all three by the same recipe; do not assume any of them.
- **Demo of the *shape* of the calculation on an unrelated state:** for $\tfrac{1}{\sqrt5}(\lvert00\rangle+2\lvert11\rangle)$ and the operators $\sigma_z\otimes\mathbb1$, $\mathbb1\otimes\sigma_z$ you would get $\langle A\rangle=\tfrac15-\tfrac45=-\tfrac35$, $\langle B\rangle=-\tfrac35$, $\langle AB\rangle=1$, correlation $1-\tfrac9{25}=\tfrac{16}{25}$. A product state would give 0.
- **Sanity checks to write down:** (1) each single-spin expectation lies in $[-1,1]$; (2) the correlation of a product state is 0; (3) a state you claim is an eigenvector of $A\otimes B$ gives $\langle AB\rangle$ equal to its eigenvalue.
- **Write-up:** use the six steps; say the move names in step 3; show the sub-steps of the inner product rather than only the final number.
