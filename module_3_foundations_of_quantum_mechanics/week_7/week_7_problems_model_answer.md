# Topic: Week 7 Task problems – model answers

### Problems

#### Problem 1

1.  Show that the state $|{\psi}\rangle = \frac{1}{\sqrt{2}}\left(|{\uparrow \downarrow}\rangle - |{\downarrow \uparrow}\rangle\right)$ cannot be written as a product state.

Problem 1 model answer

We start by decomposing the state |ψ⟩ on the full basis subtended by the states $|{\uparrow}\rangle$ and $|{\downarrow}\rangle$

$$\begin{align*}
    |{\psi}\rangle &= \frac{1}{\sqrt{2}}\left(|{\uparrow \downarrow}\rangle - |{\downarrow \uparrow}\rangle\right)\\
    &= 0|{\uparrow \uparrow}\rangle + \frac{1}{\sqrt{2}} |{\uparrow \downarrow}\rangle - \frac{1}{\sqrt{2}} |{\downarrow \uparrow}\rangle + 0 |{\downarrow \downarrow}\rangle.
\end{align*}$$
If $|{\psi}\rangle$ were a product of the two independent states we could write

$$\begin{align*}
		|{\psi}\rangle &= \left(a_1 |{\uparrow}\rangle + b_1 |{\downarrow}\rangle\right)\otimes \left(a_2 |{\uparrow}\rangle + b_2 |{\downarrow}\rangle\right)\\
		&= a_1 a_2 |{\uparrow \uparrow}\rangle + a_1 b_2 |{\uparrow \downarrow}\rangle + b_2 a_1 |{\downarrow \uparrow}\rangle + b_1 b_2 |{\downarrow \downarrow}\rangle.
\end{align*}$$
By equating coefficients in front of the basis vectors in both expressions, we obtain the following system of equations

$$\begin{align*}
    \begin{cases}
        a_1 a_2 &= 0\\
        a_1 b_2 &= \frac{1}{\sqrt{2}}\\
        b_1 a_2 &= -\frac{1}{\sqrt{2}}\\
        b_1 b_2 &= 0
    \end{cases}
\end{align*}$$
This system doesn't allow a solution. You can convince yourself by inspecting the two first lines: $a_1 a_2 = 0$ means that either $a_1 = 0$ or $a_2 = 0$ (or both). In the second line we have $a_1 b_2 = 1/\sqrt{2}$, meaning that $a_1$ cannot be zero, thus $a_2 = 0$. However, if $a_2 = 0$, then the product $b_1 a_2$ should be equal to zero, but we have $b_1 a_2 = -1/\sqrt{2}$, which contradicts what we have just established for $a_2$. Thus, the system doesn't allow for a solution, and we cannot write the state |$|{\psi}\rangle$ as a product state, meaning it is an entangled state.

#### Problem 2

In the following question we will be working with the state |$|{\psi}\rangle$ that is made of two entangled particles. The measurement on each particle can give two possible values that we will denote 0 and 1 (we could note those two outcomes $\uparrow$ and $\downarrow$, or $+$ and $−$, or 'Head' and 'Tail'; the notation doesn't matter). The entangled state $|{\psi}\rangle$ is defined as  
$$\begin{equation*}
    |{\psi}\rangle = A\left(\frac{1}{\sqrt{2}}|{00}\rangle + \frac{1}{2}|{01}\rangle + \frac{1}{2}|{11}\rangle\right),
\end{equation*}$$
where A is a normalisation constant.

1.  a) Find the value of A such that $|{\psi}\rangle$ is normalised.  
    b) You measure the state of the first particle and obtain a measurement of $|{0}\rangle$.  
    What is the state after this measurement?  
    c) If you now measure the second qubit, what are the possible results and  
    probabilities of those results?
2.  Suppose instead you measure the first particle and obtain a measurement of $|{1}\rangle$.  
    a) What is the state after this measurement?  
    b) If you now measure the second particle, what are the possible results and probabilities of those results?
3.  Is $|{\psi}\rangle$ an entangled state? Justify your answer.

Problem 2 model answer

1.  1.  We are looking for A such that $|\psi|^2 = \langle{\psi|\psi}\rangle = 1$. Here, we have  
        $$\begin{align*}
          \langle{\psi|\psi}\rangle &= A\left(\frac{1}{\sqrt{2}}\langle{00}| + \frac{1}{2}\langle{01}| + \frac{1}{2}\langle{11}|\right)\cdot A\left(\frac{1}{\sqrt{2}}|{00}\rangle + \frac{1}{2}|{01}\rangle + \frac{1}{2}|{11}\rangle\right)\\
          &= A^2\left(\frac{1}{\sqrt{2}}\frac{1}{\sqrt{2}}\langle{00|00}\rangle + \frac{1}{2}\frac{1}{2}\langle{01|01}\rangle + \frac{1}{2}\frac{1}{2}\langle{11|11}\rangle\right)\\
          &= A^2\left(\frac{1}{2} + \frac{1}{4} + \frac{1}{4}\right)\\
          &= A^2\equiv 1\\
        &\Rightarrow \boxed{A = 1}
        \end{align*}$$
    2.  If a measurement on particle 1 yields the outcome $|{0}\rangle$, the state after the measurement is the projection of $|{\psi}\rangle$ onto the subspace where particle 1 is measured as $|{0}\rangle$. That means that the new state contains only outcomes where particle 1 gave outcome $|{0}\rangle$, i.e., the state $|{11}\rangle$ drops off and the new wave function is
        
        $$\begin{align*}
              |{\psi'}\rangle = B\left(\frac{1}{\sqrt{2}}|{00}\rangle + \frac{1}{2}|{01}\rangle\right),
          \end{align*}$$
        
        where B is a new constant of normalisation such that $|\psi'|^2 = \langle{\psi'|\psi'}\rangle = 1$. Using the same method as in i) a), we find that $B=2/\sqrt{3}$, giving for a new wave function the expression
        
        $$\begin{align*}
          |{\psi'}\rangle = \frac{\sqrt{2}}{\sqrt{3}}|{00}\rangle + \frac{1}{\sqrt{3}}|{01}\rangle.
        \end{align*}$$
        
        Notice that the new wave function must be normalised, meaning that any subsequent measurement on $|{\psi'}\rangle$ will yield outcomes whose probabilities add to 1. This is an example of how a measurement on a quantum system can fundamentally modify it.
        
    3.  The probabilities of obtaining $|{00}\rangle$ and $|{01}\rangle$ are
        
        $$\begin{align*}
          P(|{00}\rangle) &= \left|\langle{00|\psi'}\rangle\right|^2 = \frac{2}{3}\\
          P(|{01}\rangle) &= \left|\langle{01|\psi'}\rangle\right|^2 = \frac{1}{3}.
        \end{align*}$$
        
        Notice that the probabilities add to 1, as expected.
        
2.  1.  If a measurement on particle 1 yields the outcome $|{1}\rangle$, the state after the measurement is the projection of $|{\psi}\rangle$ onto the subspace where particle 1 is measured as $|{1}\rangle$.
        
        $$\begin{equation*}
            |{\psi''}\rangle = |{11}\rangle.
        \end{equation*}$$
        
        Given that we have only one surviving state, the normalisation constant is trivially equal to 1.
        
    2.  The result of the measurement of the second particle on the state $|{\psi''}\rangle = |{11}\rangle$ is 1, with the probability of 1.
        
    3.  The state $|{\psi}\rangle$ is an entangled state. One way to see this is that in the two different outcomes to measuring the state of the first particle, we get differing probabilities for the outcome of the second particle. Hence the states of the two particles are not independent of each other.
        
            Another way to see this is to solve the system of equations that would give rise to the $|{\psi}\rangle$ as a result of the product of the two single-particle wave functions (one for each particle)
        
        $$\begin{align*}
            |{\psi}\rangle &= \left(\frac{1}{\sqrt{2}}|{00}\rangle + \frac{1}{2}|{01}\rangle + \frac{1}{2}|{11}\rangle\right) \equiv \underbrace{\left(a_1|{0}\rangle + b_1 |{1}\rangle\right)}_{\text{Particle 1}}\otimes \underbrace{\left(a_2|{0}\rangle + b_2 |{1}\rangle\right)}_{\text{Particle 2}}\\
            \Rightarrow & \begin{cases}
                \frac{1}{\sqrt{2}} &= a_1 a_2\\
                \frac{1}{2} &= a_1 b_2\\
                0 &= b_1 a_2\\
                \frac{1}{2} &= b_1 b_2\\
            \end{cases}  
        \end{align*}$$
        
        You can verify that the system cannot be solved. We cannot write $|{\psi}\rangle$ as a product of two single-particle states, hence it is an entangled state.
        

Problem 3

Consider the three composite spin operators $\sigma_x\otimes 1$, $\sigma_y\otimes 1$, and $\sigma_z\otimes 1$, acting on a general product state

$$|\psi\rangle = \left(a_1|\uparrow\rangle+b_1|\downarrow\rangle\right) \otimes \left(a_2|\uparrow\rangle+b_2|\downarrow\rangle\right)$$

Using the expressions for the kets and operators listed below, prove that when any of these three composite spin operators acts on a product state, the result is still a product state.

$$\begin{aligned} |\uparrow\rangle &= \begin{pmatrix} 1\\ 0 \end{pmatrix}, &\qquad |\downarrow\rangle &= \begin{pmatrix} 0\\ 1 \end{pmatrix}, \\[1em] 1 &= \begin{pmatrix} 1 & 0\\ 0 & 1 \end{pmatrix}, &\qquad \sigma_x &= \begin{pmatrix} 0 & 1\\ 1 & 0 \end{pmatrix}, \\[1em] \sigma_y &= \begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix}, &\qquad \sigma_z &= \begin{pmatrix} 1 & 0\\ 0 & -1 \end{pmatrix}. \end{aligned}$$

Problem 3 model answer

It is useful first to write the state of each spin separately:

$$|\phi_1\rangle = a_1|\uparrow\rangle+b_1|\downarrow\rangle, \qquad |\phi_2\rangle = a_2|\uparrow\rangle+b_2|\downarrow\rangle.$$

The complete two-spin state is therefore $\mid\psi\rangle = |\phi{_1}\rangle\otimes|\phi{_2}\rangle.$.

We will use the general property of tensor products $(A\otimes B) \left( |u\rangle\otimes|v\rangle \right) = \left(A|u\rangle\right) \otimes \left(B|v\rangle\right)$.

Since the second operator is the identity, $1\mid\phi{_2}\rangle=\mid\phi{_2}\rangle$.

Therefore,

$(\sigma_i\otimes 1)\mid\psi\rangle = \left(\sigma{_i}\mid\phi{_1}\rangle\right) \otimes\mid\phi{_2}\rangle, \qquad i=x,y,z.$

We can now verify this explicitly for each of the three Pauli matrices.

1.  **Action of σx⊗1**

From

$$\sigma{_x}= \begin{pmatrix} 0 & 1\\ 1 & 0 \end{pmatrix},$$

we obtain

$$\begin{aligned} \sigma{_x}|\uparrow\rangle &= \begin{pmatrix} 0 & 1\\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1\\ 0 \end{pmatrix} = \begin{pmatrix} 0\\ 1 \end{pmatrix} = |\downarrow\rangle, \\[1em] \sigma{_x}|\downarrow\rangle &= \begin{pmatrix} 0 & 1\\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0\\ 1 \end{pmatrix} = \begin{pmatrix} 1\\ 0 \end{pmatrix} = |\uparrow\rangle. \end{aligned}$$

Thus,

$$\begin{aligned} \sigma{_x}|\phi{_1}\rangle &= \sigma{_x} \left( a{_1}|\uparrow\rangle+b{_1}|\downarrow\rangle \right) \\ &= a{_1}|\downarrow\rangle+b{_1}|\uparrow\rangle \\ &= b_1|\uparrow\rangle+a_1|\downarrow\rangle. \end{aligned}$$

Hence,

$$\boxed{ (\sigma{_x}\otimes 1)|\psi\rangle = \left( b_1|\uparrow\rangle+a_1|\downarrow\rangle \right) \otimes \left( a_2|\uparrow\rangle+b_2|\downarrow\rangle \right) }.$$

The result can still be written as a tensor product of a state of the first spin and a state of the second spin. It is therefore still a product state. The operator σx exchanges the spin-up and spin-down amplitudes of the first spin, while the second spin is unchanged.

2.  **Action of $\boldsymbol{\sigma_y\otimes 1}$**

From

$$\sigma_y= \begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix},$$

we find

$$\begin{aligned} \sigma_y|\uparrow\rangle &= \begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix} \begin{pmatrix} 1\\ 0 \end{pmatrix} = \begin{pmatrix} 0\\ i \end{pmatrix} = i|\downarrow\rangle, \\[1em] \sigma_y|\downarrow\rangle &= \begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix} \begin{pmatrix} 0\\ 1 \end{pmatrix} = \begin{pmatrix} -i\\ 0 \end{pmatrix} = -i|\uparrow\rangle. \end{aligned}$$

Therefore,

$$\begin{aligned} \sigma{_y}|\phi_1\rangle &= \sigma_y \left( a_1|\uparrow\rangle+b_1|\downarrow\rangle \right) \\ &= ia_1|\downarrow\rangle -ib_1|\uparrow\rangle \\ &= -ib_1|\uparrow\rangle +ia_1|\downarrow\rangle. \end{aligned}$$

Hence,

$$\boxed{ (\sigma_y\otimes 1)|\psi\rangle = \left( -ib_1|\uparrow\rangle +ia_1|\downarrow\rangle \right) \otimes \left( a_2|\uparrow\rangle+b_2|\downarrow\rangle \right) }.$$

Again, the final state is explicitly a product state. The operator $\sigma_y$ exchanges the spin-up and spin-down components of the first spin and introduces phase factors $i$ and $−i$. The second spin remains unchanged.

3.  **Action of $\boldsymbol{\sigma_z\otimes 1}$**

From

$$\sigma_z= \begin{pmatrix} 1 & 0\\ 0 & -1 \end{pmatrix},$$

we have

$$\begin{aligned} \sigma_z|\uparrow\rangle &= \begin{pmatrix} 1 & 0\\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1\\ 0 \end{pmatrix} = \begin{pmatrix} 1\\ 0 \end{pmatrix} = |\uparrow\rangle, \\[1em] \sigma_z|\downarrow\rangle &= \begin{pmatrix} 1 & 0\\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0\\ 1 \end{pmatrix} = \begin{pmatrix} 0\\ -1 \end{pmatrix} = -|\downarrow\rangle. \end{aligned}$$

Thus,

$$\begin{aligned} \sigma_z|\phi_1\rangle &= \sigma_z \left( a_1|\uparrow\rangle+b_1|\downarrow\rangle \right) \\ &= a_1|\uparrow\rangle-b_1|\downarrow\rangle. \end{aligned}$$

Hence,

$$\boxed{ (\sigma_z\otimes 1)|\psi\rangle = \left( a_1|\uparrow\rangle-b_1|\downarrow\rangle \right) \otimes \left( a_2|\uparrow\rangle+b_2|\downarrow\rangle \right) }.$$

This is again a product state. The operator $\sigma_z$ leaves the spin-up component of the first spin unchanged and changes the sign of its spin-down component. The second spin is unaffected.

**Conclusion**

For all three operators,

$$\boxed{ (\sigma_i\otimes 1) \left( |\phi_1\rangle\otimes|\phi_2\rangle \right) = \left( \sigma_i|\phi_1\rangle \right) \otimes|\phi_2\rangle, \qquad i=x,y,z. }$$

In each case, the operator changes only the state of the first spin and leaves the second spin unchanged. The resulting state can still be written as a tensor product of two single-spin states, so it remains a product state.

**Physical insight:** The operators $\sigma_x\otimes 1$, $\sigma_y\otimes 1$, and $\sigma_z\otimes 1$ are local operations: they act only on the first subsystem. Such an operation cannot create entanglement from an initially separable state.

More generally, any product operator $A\otimes B$ acting on a product state preserves the product form:

$$(A\otimes B) \left( |\phi_1\rangle\otimes|\phi_2\rangle \right) = \left(A|\phi_1\rangle\right) \otimes \left(B|\phi_2\rangle\right).$$

An operator involving both subsystems is therefore not automatically entangling. For example, $\sigma_z\otimes\sigma_z$ is itself a product operator and still maps a product state onto another product state. To create entanglement from an initially separable state, an operation that genuinely couples the two subsystems is required, such as a CNOT operation for a suitable input state.

This topic is closed for comments.