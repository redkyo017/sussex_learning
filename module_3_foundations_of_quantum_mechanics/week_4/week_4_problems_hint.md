# Discussion Topic: Week 4 Task problems – hints

## Problems

### Problem 1
A system is initially in the state
$$\vert{}\psi_0\rangle = \frac{1}{\sqrt{7}} \left[ \sqrt{2}\vert{}\phi_1\rangle + \sqrt{3}\vert{}\phi_2\rangle + \vert{}\phi_3\rangle + \vert{}\phi_4\rangle \right],$$
where $\vert{}\phi_n\rangle$ are eigenstates of the system's Hamiltonian such that
$$\hat{H}\vert{}\phi_n\rangle = n^2 \epsilon_0 \vert{}\phi_n\rangle.$$

1. If energy is measured, what values will be obtained and with what probabilities?
2. Consider an operator $\hat{A}$ whose action on $\vert{}\phi_n\rangle$ is defined by $\hat{A}\vert{}\phi_n\rangle = (n+1)a_0\vert{}\phi_n\rangle$. If $A$ is measured, what values will be obtained and with what probabilities?
3. Suppose that a measurement of the energy yields $4\epsilon_0$. If we measure $A$ immediately afterwards, what value will be obtained?

#### Problem 1 hints
*These hints are intended to help you get started. They do not contain the complete solution.*

1. The state is already written as a superposition of energy eigenstates $\vert{}\phi_n\rangle$, so first identify the energy associated with each one from
   $$\hat{H}\vert{}\phi_n\rangle = n^2 \epsilon_0 \vert{}\phi_n\rangle.$$
   Remember that if a normalised state is written as
   $$\vert{}\psi\rangle = \sum_n c_n \vert{}\phi_n\rangle,$$
   then the probability of obtaining the result associated with $\vert{}\phi_n\rangle$ is
   $$P_n = \vert{}c_n\vert{}^2.$$
   Identify the four coefficients $c_n$ in the given state and square their magnitudes.
   As a useful check, your four probabilities should add up to one.

2. Compare the action of $\hat{A}$,
   $$\hat{A}\vert{}\phi_n\rangle = (n+1)a_0\vert{}\phi_n\rangle,$$
   with the general eigenvalue equation
   $$\hat{A}\vert{}\phi_n\rangle = a_n \vert{}\phi_n\rangle.$$
   This immediately tells you the possible outcomes of a measurement of $A$.
   Notice also something important: the eigenstates of $\hat{A}$ appearing here are the same states $\vert{}\phi_n\rangle$ that appear in the expansion of $\vert{}\psi_0\rangle$.
   Therefore, what determines the probability of each outcome? Do you need to calculate a new set of expansion coefficients, or can you use the coefficients already present in $\vert{}\psi_0\rangle$?

3. First identify which value of $n$ corresponds to the measured energy
   $$E_n = n^2 \epsilon_0 = 4\epsilon_0.$$
   After an ideal measurement of the energy, the state collapses onto the energy eigenstate associated with the measured result.
   Once you know which $\vert{}\phi_n\rangle$ the system is in, use
   $$\hat{A}\vert{}\phi_n\rangle = (n+1)a_0\vert{}\phi_n\rangle$$
   to determine what an immediate measurement of $A$ will give. Ask whether there is any remaining uncertainty once the system is in this eigenstate.

---

### Problem 2
1. Find the Hermitian conjugates of $x$, $i$, $\frac{d}{dx}$.
2. Show that 
   $$(\hat{Q}\hat{R})^\dagger = \hat{R}^\dagger \hat{Q}^\dagger \quad \text{(note the reversed order)}$$
   $$(\hat{Q} + \hat{R})^\dagger = \hat{Q}^\dagger + \hat{R}^\dagger$$
   and
   $$(c\hat{Q})^\dagger = c^\star \hat{Q}^\dagger,$$
   where $c$ is a complex constant.

#### Problem 2 hints
*These hints are intended to help you get started. They do not contain the complete solution.*

The key definition throughout this problem is the definition of the Hermitian conjugate:
$$\langle f \vert{} \hat{Q} g \rangle = \langle \hat{Q}^\dagger f \vert{} g \rangle.$$
A useful strategy is therefore to start with the left-hand side and manipulate it until the operator acting on $f$ can be identified.

1. **For $x$:**
   Write the inner product explicitly:
   $$\langle f \vert{} x g \rangle = \int_{-\infty}^{\infty} f^\star(x) x g(x) dx.$$
   Remember that the position variable $x$ is real, so
   $$x^\star = x.$$
   Try rearranging the integrand into the form
   $$[\text{something acting on } f(x)]^\star g(x).$$
   You can then compare the result directly with the definition of the Hermitian conjugate.

   **For $i$:**
   Proceed in the same way, but remember that complex conjugation changes the sign of $i$:
   $$i^\star = -i.$$
   Ask what factor must act on $f$ so that its complex conjugate produces the factor $i$ appearing in the original integral.

   **For $\frac{d}{dx}$:**
   Start from
   $$\langle f \vert{} \frac{d}{dx} g \rangle = \int_{-\infty}^{\infty} f^\star(x) \frac{dg(x)}{dx} dx.$$
   Here the important mathematical tool is *integration by parts*:
   $$\int u \, dv = uv - \int v \, du.$$
   Choose
   $$u = f^\star(x), \quad dv = \frac{dg}{dx} dx.$$
   This transfers the derivative from $g$ onto $f^\star$. Pay careful attention to the minus sign introduced by integration by parts.
   For functions in the appropriate domain, the boundary term
   $$\left. f^\star(x) g(x) \right\vert{}_{-\infty}^{+\infty}$$
   vanishes. Once this term has gone, compare the remaining expression with
   $$\langle \hat{Q}^\dagger f \vert{} g \rangle.$$
   The sign in front of the derivative is the crucial point.

2. **Product of two operators**
   Start with
   $$\langle f \vert{} \hat{Q}\hat{R} g \rangle.$$
   Remember that the rightmost operator acts first:
   $$\hat{Q}\hat{R} g = \hat{Q}(\hat{R} g).$$
   First use the definition of the Hermitian conjugate to move $\hat{Q}$ from the ket side to the bra side. Then repeat the same process for $\hat{R}$.
   Watch carefully what happens to the order of the two operators. Which operator is moved first, and which operator ends up acting first on $f$?

   **Sum of two operators**
   Start with
   $$\langle f \vert{} (\hat{Q} + \hat{R}) g \rangle.$$
   Use linearity to separate this into two inner products:
   $$\langle f \vert{} \hat{Q} g \rangle + \langle f \vert{} \hat{R} g \rangle.$$
   Apply the definition of the Hermitian conjugate separately to each term, and then combine the result again.
   Multiplication by a complex constant
   Start with
   $$\langle f|c\hat{Q}g\rangle.$$

   The constant c can be taken outside the inner product on the ket side. However, when you rewrite the result as something acting on the bra-side function , remember that complex conjugation is involved. The useful identity is
   $$(c^\star)^\star=c.$$
   This should indicate why the complex conjugate of , rather than itself, appears in the Hermitian conjugate.
