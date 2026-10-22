# Discussion Topic: Week 7 Task problems – hints

## Problems

### Problem 1
Show that the state $|\psi\rangle = \frac{1}{\sqrt{2}}
\left(
|\uparrow\downarrow\rangle -
|\downarrow\uparrow\rangle
\right)$ cannot be written as a product state.

#### Problem 1 hints
These hints are intended to help you get started. They do not contain the complete solution.

* A general product state of two spin $-\frac{1}{2}$ particles can be written as
  $$\mid\psi_{\text{prod}}\rangle= (a_{1}\mid~\uparrow\rangle+b_{1}\mid~\downarrow\rangle)\otimes(a_{2}\mid~\uparrow\rangle +b_{2}\mid~\downarrow\rangle).$$
* Expand this tensor product. You should obtain four terms involving the basis states:
  $$\vert\;\uparrow\uparrow\;\rangle\;,\;\vert\;\uparrow\downarrow\;\rangle\;,\;\vert\;\downarrow\uparrow\;\rangle\;,\;\vert\;\downarrow\downarrow\;\rangle\;.$$
* Next write the state given in the question in the same four-state basis, including zero coefficients where necessary.
  $$\vert\;\mathrm\psi\;\rangle\;=\;0\;\vert\;\uparrow\uparrow\;\rangle\;+\;1\;2\;\vert\;\uparrow\downarrow\;\rangle\;-\;1\;2\;\vert\;\downarrow\uparrow\;\rangle\;+\;0\;\vert\;\downarrow\downarrow\;\rangle\;.$$
* If the given state really were a product state, the coefficients of corresponding basis states in the two expressions would have to be equal.
* This gives four simultaneous conditions involving $a_0, a_1, b_0, b_1$. Look particularly at the conditions arising from $|\uparrow\uparrow\rangle$ and $|\uparrow\downarrow\rangle$.
* If a product of two numbers is zero, at least one of them must be zero. But if another product containing one of those same numbers is non-zero, what does that tell you?
* Try following this logic through the four equations. If the equations contradict one another, then no choices of $a_0, a_1, b_0, b_1$ can reproduce the given state.
* A two-particle pure state that cannot be expressed as a product of two single-particle states is an *entangled state*.

---

### Problem 2
In the following question we will work with a state $|\psi\rangle$ made of two particles. A measurement on each particle can give two possible values, which we denote by $0$ and $1$.

The state is
$$\mid\psi\rangle=A\left(\frac{1}{\sqrt{2}}\mid00\rangle+\frac{1}{2}\mid01\rangle+\frac{1}{2}\mid11\right),$$
where $A$ is a normalisation constant.

a. Find the value of $A$ such that $|\psi\rangle$ is normalised.

b. You measure the state of the first particle and obtain $|0\rangle$. What is the state after this measurement?

c. If you now measure the second particle, what are the possible results and probabilities of those results?

ii. Suppose instead that you measure the first particle and obtain $|1\rangle$.
   1. What is the state after this measurement?
   2. If you now measure the second particle, what are the possible results and probabilities of those results?

iii. Is $|\psi\rangle$ an entangled state? Justify your answer.

#### Problem 2 hints
These hints are intended to help you get started. They do not contain the complete solution.

##### 1. Normalisation
* Start from $\langle\psi|\psi\rangle=1$.
* The states 

  $|00\rangle,\qquad |01\rangle,\qquad |10\rangle,\qquad |11\rangle$ 

form an orthonormal basis. This means, for example, 

$\langle00|00\rangle=1, \qquad \langle00|01\rangle=0.$

* Therefore, when calculating the norm, the cross terms between different basis states disappear.
* Square the magnitudes of the three coefficients inside the brackets, add them together, and then determine what $A$ must be so that the total probability is $1$.

##### 2. First particle measured to be $0$
* Each two-particle ket contains two labels: 

  $|\text{first particle},\text{ second particle}\rangle$.

* If the first particle has been measured and the result is $0$, keep only those terms in the original state whose *first digit is $0$*.
* Which of $|00\rangle, |01\rangle, |11\rangle$ survive this measurement?
* The surviving part of the original state is not necessarily normalised. Introduce a new normalisation constant $A'$ and impose $\langle \psi' | \psi' \rangle = 1$.
* This renormalisation is important because all subsequent measurement probabilities must again add to $1$.

##### 3. Now measuring the second particle
* Use the *new, normalised state after the first measurement*, not the original state.
* Look at the second digit of each surviving basis state. The probability of each outcome is the squared magnitude of its coefficient.
* As a check, $P(0) + P(1) = 1$.

##### 4a. First particle measured to be $1$
* Apply exactly the same projection idea as before, but this time keep only terms whose *first digit is $1$*.
* Inspect the original state:
  $$|\psi\rangle = A\left( \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{2}|01\rangle + \frac{1}{2}|11\rangle \right)$$
* How many terms survive this measurement?
* If only one basis state survives, the state after the measurement is particularly simple.

##### 4b. Measurement of the second particle
* Once the first measurement has left the system in a definite two-particle basis state, inspect the second digit.
* Is the second particle still in a superposition, or is its value now completely determined?

##### 4c. Is the original state entangled?
There are at least two useful ways to investigate this.
* **Method 1: use the measurement results.** Compare what can happen to the second particle depending on whether the first particle is found in state $0$ or state $1$. If the state were a simple product $|\phi_1\rangle\otimes|\phi_2\rangle$, measuring the first particle would not change the state $|\phi_2\rangle$ of the second particle. Is that what happens here?
* **Method 2: try to factorise the state.** Write a general product state as 
  $\left(a_1|0\rangle+b_1|1\rangle\right) \otimes \left(a_2|0\rangle+b_2|1\rangle\right)$.

Expand it: 
  $a{_1}a{_2}|00\rangle + a{_1}b{_2}|01\rangle + b{_1}a{_2}|10\rangle + b{_1}b{_2}|11\rangle$. 

Compare these four coefficients with those of the state in the question. In particular, the coefficient of $|10\rangle$ is zero, while several of the other coefficients are non-zero. 
Ask whether there is any choice of $a{_1},b{_1},a{_2},b{_2}$ coefficients that can satisfy all four conditions simultaneously.

---

### Problem 3
Consider the three composite spin operators $\sigma{_x}\otimes 1, \sigma{_y}\otimes 1,$, and $\sigma{_z}\otimes 1$, acting on a general product state. 
  
  $|\psi\rangle = \left(a_1|\uparrow\rangle+b_1|\downarrow\rangle\right) \otimes \left(a_2|\uparrow\rangle+b_2|\downarrow\rangle\right)$

Using the expressions for the kets and operators listed below, prove that when any of these three composite spin operators acts on a product state, the result is still a product state.
  $$\begin{aligned} |\uparrow\rangle = \begin{pmatrix} 1\\ 0 \end{pmatrix}, \qquad |\downarrow\rangle = \begin{pmatrix} 0\\ 1 \end{pmatrix}, \\[1em]
  1 = \begin{pmatrix} 1\; 0\\ 0 \; 1 \end{pmatrix}, \qquad \sigma{_x} = \begin{pmatrix} 0 \; 1\\ 1 \; 0 \end{pmatrix}, \\[1em] \sigma{_y} = \begin{pmatrix} 0 \; -i\\ i \; 0 \end{pmatrix}, \qquad \sigma{_z} = \begin{pmatrix} 1 \; 0\\ 0 \; -1 \end{pmatrix}. \end{aligned}$$

#### Problem 3 hints
These hints are intended to help you get started. They do not contain the complete solution.

* It may help to write the two single-spin states separately: 

$|\phi{_1}\rangle = a{_1}|\uparrow\rangle+b{_1}|\downarrow\rangle,\\ |\phi{_2}\rangle = a{_2}|\uparrow\rangle+b{_2}|\downarrow\rangle$. 

The original state can then be written simply as 

  $|\psi\rangle = |\phi{_1}\rangle\otimes|\phi{_2}\rangle$.

A key property of tensor products is 

  $(A\otimes B) \,\left( |u\rangle\otimes|v\rangle \right) = \left(A|u\rangle\right) \otimes \left(B|v\rangle\right)$.

Use this with $B=1$ (the identity operator). What does the identity operator do to 

$|\psi_2\rangle$?

You can then study each Pauli matrix by finding its action on the two basis states 

$|\uparrow\rangle$ and $|\downarrow\rangle$.

##### For $\boldsymbol{\sigma_x}$:
Multiply
  $$\begin{pmatrix} 0 & 1\\ 1 & 0 \end{pmatrix}$$
first by 
    $$\begin{pmatrix} 1\\ 0 \end{pmatrix}$$ 
and then by 
    $$\begin{pmatrix} 0\\ 1 \end{pmatrix}$$
What happens to $|\uparrow\rangle$ and $|\downarrow\rangle$? Use this to determine 
    $$\sigma{_x} \left( a{_1}|\uparrow\rangle+b{_1}|\downarrow\rangle \right).$$

##### For $\boldsymbol{\sigma{_y}}$:
Repeat the same procedure with 
    $$\sigma{_y} = \begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix}.$$
Be careful with factors of $i$. Work out separately $\sigma{_y}|\uparrow\rangle \;\text{and}\; \sigma{_y}|\downarrow\rangle.$ and $\sigma{_y}|\uparrow\rangle \;\text{and}\; \sigma{_y}|\downarrow\rangle.$, then use linearity to find the action on the general first-spin state.

##### For $\boldsymbol{\sigma{_z}}$:
Work out $\sigma{_z}|\uparrow\rangle \;\text{and}\; \sigma{_z}|\downarrow\rangle.$ and $\sigma{_z}|\uparrow\rangle \;\text{and}\; \sigma{_z}|\downarrow\rangle.$ One component is unchanged while the other acquires a minus sign.

##### Final step:
After applying each composite operator, do not immediately expand the complete two-particle state. Instead, ask whether your result can still be written in the form 

$|\text{new state of particle 1}\rangle \otimes |\text{state of particle 2}\rangle.$. 

If it can, then it is still a product state.

The broader idea is that $\sigma{_x}\otimes1$, $\sigma{_y}\otimes1$, and $\sigma{_z}\otimes1$ act only on the first subsystem. Think about whether an operation that acts on one subsystem alone can create correlations between two initially independent systems.