# Week 1: Language and tools of quantum mechanics: Study

## 1: Language and tools of quantum mechanics

### Introduction
This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

This week we will cover the basics of linear algebra, which is the branch of mathematics dealing with vectors and matrices. Indeed, the bulk of quantum mechanics can be described using vectors and matrices; thus linear algebra is the natural language of quantum mechanics.

You will also cover some fundamental concepts of quantum mechanics, such as wave functions, operators and Dirac notation. The aim is to give you a brief overview and intuitive understanding of concepts that we will cover in more detail in the following weeks.

In this Study you will cover the following topics:
- 1.1 Wave function – a quantum description of a particle
- 1.2 Linear algebra and Dirac notation (bra-ket)
- 1.3 Operators and observables
- 1.4 Eigenfunctions and eigenvalues

---

## 1.1 Wave function – a quantum description of a particle

In *classical mechanics*, knowing *the state of a system* means that we know everything that is necessary to predict the future of that system. We talk about the *determinism* of classical physics – the understanding that the knowledge of the present determines the entire future of the system.

For example, let's consider a simple particle of mass $m$, constrained to move in one dimension ($x$-axis) and subjected to the force $F(x, t)$ that derives from a potential $V$. In this example, the state of a system is described by position $x$. Indeed, if we know $x(t)$, we can calculate the particle's velocity ($v = \frac{\mathrm{d}x}{\mathrm{d}t}$), momentum ($p = mv$) or any other variable of interest at any future time $t$. In classical mechanics, we can find the position $x(t)$ of a particle by applying Newton's second law:

$$F = ma \tag{1.1}$$

where $a = \frac{\mathrm{d}^2 x}{\mathrm{d}t^2}$ is the acceleration of the particle and

$$F = -\frac{\partial V}{\partial x}. \tag{1.2}$$

Combining Eq. (1.1) and Eq. (1.2) leads us to the second order differential equation,

$$-\frac{\partial V}{\partial x} = m \frac{\mathrm{d}^2 x}{\mathrm{d}t^2}. \tag{1.3}$$

The knowledge of the initial conditions in position $x(0)$ and velocity $v(0) = \frac{\mathrm{d}x(0)}{\mathrm{d}t}$ is sufficient to solve Eq. (1.3) for a *unique* $x(t)$. That means that the knowledge of the state of the particle in the present tells us exactly what will happen to it at any future time $t$.

*Quantum mechanics* approaches the same problem quite differently. The state of a system is described by the particle's *wave function* $\psi(x, t)$. To find it, we need to solve the Schrödinger equation

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V\psi, \tag{1.4}$$

where $i = \sqrt{-1}$, and $\hbar = \frac{h}{2\pi} = 1.055 \times 10^{-34}\text{ J}\cdot\text{s}$, is the reduced Planck's constant.

One can notice the similarities between classical and quantum mechanics. Given initial conditions at time $t = 0$ [quantum: $\psi(x, 0)$; classical: $x(0)$], both the Schrödinger equation and Newton's second law give the state of the particle for all future times $t > 0$. In that, they are both deterministic theories. However, the fundamental difference between quantum and classical mechanics stems from the very nature of the wave function $\psi(x, t)$. In 1926, German physicist Max Born stated that the probability density of finding a system in a given state (say at position $x$ at time $t$), when measured, is proportional to the square of the amplitude of the system's wave function, $|\psi(x, t)|^2$, at that state. This key postulate of quantum mechanics is known as the *Born rule*. Using probability density, we can calculate the probability of finding the particle at the point between $x$ and $x + \mathrm{d}x$, at time $t$:

$$P(x, x + \mathrm{d}x; t) = |\psi(x, t)|^2 \mathrm{d}x = \psi^*(x, t)\psi(x, t)\mathrm{d}x. \tag{1.5}$$

From Eq. (1.5) you can notice that to calculate the probability of finding the particle between two positions $a$ and $b$, it is sufficient to integrate $|\psi(x, t)|^2$ over that range:

$$P(a, b; t) = \int_{a}^{b} |\psi(x, t)|^2 \mathrm{d}x = \text{\{probability of finding the particle between } a \text{ and } b\text{, at time } t\text{\}}. \tag{1.6}$$

**Figure 1.1:** Plot of a typical probability density $|\psi(x, t)|^2$ as a function of position $x$. The maximum value of the function $|\psi|^2$, located at $x=c$, corresponds to the most likely position of the particle. The integral of the probability density function $|\psi|^2$ between positions $a$ and $b$ is represented by the shaded area underneath the curve and represents the probability of finding the particle between positions $a$ and $b$.

As in any probability distribution, the sum over all possibilities must be equal to 1. This leads us to the normalisation condition for quantum states:

$$\int_{-\infty}^{+\infty} |\psi(x, t)|^2 \mathrm{d}x = 1, \tag{1.7}$$

in other words, if you measure the particle you will certainly find it somewhere.

You will often find in the literature that wave functions borrow the language from the theory of probabilities, namely:
- $|\psi(x, t)| \rightarrow$ probability amplitude
- $|\psi(x, t)|^2 \rightarrow$ probability density

The wave functions we have encountered so far were only functions of position and time – quantities with intuitive meaning. However, quantum systems can have additional quantities that define them. For example, to describe an electron inside the atom in a quantum mechanical way, we need to include other quantities in its wave function, such as spin, orbital angular momentum, energy, and so on. The complexity of wave functions often leads to complicated mathematical calculations. In the next topic, you will see how the formalism of *linear algebra* and *Dirac notation* can lead to a simpler description of quantum systems.

---

## 1.2 Linear algebra and Dirac notation (bra-ket)

The wave functions that describe the state of a physical system in quantum mechanics can be mathematically represented by vectors. On the other hand, the operations on quantum states, such as rotations, translations, measurements, and so on, are represented by matrices. We can use the mathematical formalism operating on vectors and matrices, known as *linear algebra*, to describe and manipulate quantum states.

The vector spaces we use to define quantum mechanical states are called *Hilbert spaces*: a complex vector space with an inner product. When you come across the term Hilbert space in quantum mechanics, it refers to the space of states. A Hilbert space may have either a finite or an infinite number of dimensions. For example, a two-dimensional complex Hilbert space is used for describing the spin of an electron, which can take two values: spin-up and spin-down. On the other hand, for quantities such as position and momentum, there are infinite possibilities. Therefore, they are represented by a state vector in an infinite-dimensional Hilbert space.

In the next paragraph we will list the properties that the mathematicians have wisely chosen as requisite for a vector space. As you read them, compare them with the world of familiar three-dimensional vectors ('arrows' in 3D space). A vector space is the collection of all the complex vectors of a given dimension with vector addition and scalar multiplication. In practice, let $\mathbf{v}$, $\mathbf{w}$ and $\mathbf{u}$ be vectors, and $c$ and $d$ be scalars. Then vector addition and scalar multiplication have the following properties:

- $\mathbf{v} + \mathbf{w} = \mathbf{w} + \mathbf{v}$ (commutativity)
- $\mathbf{v} + (\mathbf{w} + \mathbf{u}) = (\mathbf{v} + \mathbf{w}) + \mathbf{u}$ (associativity)
- $c(\mathbf{v} + \mathbf{w}) = c\mathbf{v} + c\mathbf{w}$ (distributivity of scalar multiplication)
- $(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$ (distributivity of scalar addition)
- $\mathbf{v} + \mathbf{0} = \mathbf{v}$ (existence of a unique additive zero)
- $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ (existence of additive inverse $-\mathbf{v}$)

These are similar properties to real and complex numbers. (Numbers are actually vectors of dimension 1.) The last two properties might seem obvious. We added them because they are needed to define the notion of vector space, which doesn't only apply to vectors, but potentially any other kind of mathematical objects such as functions.

Handling large arrays of states isn't easy using vector notation, so instead of explicitly writing out the whole vector each time, quantum physics usually uses the notation developed by physicist Paul Dirac – the *Dirac notation* (also called *bra-ket notation*). In Dirac notation, the vectors in the space are denoted by $|v\rangle$, called a *ket*, where $v$ is some symbol that identifies the vector. One could equally well use something like $\vec{v}$ or $\mathbf{v}$. Just as we can express any three-dimensional vector in terms of the basis vectors, $\mathbf{r} = x\hat{\mathbf{e}}_1 + y\hat{\mathbf{e}}_2 + z\hat{\mathbf{e}}_3$, so we can expand any wave function as a superposition of basis state vectors,

$$|v\rangle = \lambda_1 |v_1\rangle + \lambda_2 |v_2\rangle + \dots. \tag{1.8}$$

Each ket has its corresponding *bra*, which is its Hermitian conjugate. Remember, the Hermitian conjugate is obtained by taking a transpose and changing the sign of any imaginary values, and thus

$$|v\rangle = \langle v|^\dagger, \tag{1.9}$$

where symbol $\dagger$ (pronounced dagger) denotes Hermitian conjugate. You can think of kets as column vectors, and bras as row vectors. As in quantum mechanics (and generally in matrix algebra), the order of vectors in operation and their nature (row versus column) matter; bra-ket notation is, fundamentally, nothing more than a reminder for ‘that's a row vector' versus ‘that's a column vector'.

A multiple of a vector by a complex number $c$ is written as $c|v\rangle$ – think of it as analogous to $c\vec{v}$ or $c\mathbf{v}$. In Dirac notation, the *inner product* of the vectors $|v\rangle$ with $|w\rangle$ is written $\langle v|w\rangle$. This resembles the ordinary dot product $\vec{v} \cdot \vec{w}$ except that one takes a complex conjugate of the vector on the left; thus think of it as $\vec{v}^* \cdot \vec{w}$. When you multiply a bra $\langle v|$ by a ket $|w\rangle$, with the bra on the left as in $\langle v|w\rangle$, you're computing an inner product. You're asking for a single number that describes how much $v$ and $w$ align with each other. If $v$ is perpendicular to $w$, then $\langle v|w\rangle$ is zero. If $v$ is parallel to $w$, and both are unit vectors, then the magnitude of $\langle v|w\rangle$ is one. For the in-between cases, you get something in between.

When you flip the order and multiply a ket $|v\rangle$ by a bra $\langle w|$, with the ket on the left as in $|v\rangle\langle w|$, you're computing an *outer product*. $|v\rangle\langle w|$ isn't a single number, it's a whole matrix! A matrix that converts between $v$ and $w$, to be specific. If you left-multiply $|v\rangle\langle w|$ by $\langle v|$, you end up with $\langle w|$. If you right-multiply $|v\rangle\langle w|$ by $|w\rangle$, you end up with $|v\rangle$. Why? Because of associativity:

$$\langle v| \cdot (|v\rangle\langle w|) = \langle v|v\rangle \cdot \langle w| = 1 \cdot \langle w| = \langle w|$$

$$(|v\rangle\langle w|) \cdot |w\rangle = |v\rangle \cdot \langle w|w\rangle = |v\rangle \cdot 1 = |v\rangle$$

Note that we assumed $v$ and $w$ to be unit vectors, and thus we have $\langle v|v\rangle = \langle w|w\rangle = 1$.

Imagine if each of the vectors $v$ and $w$ had 100 components. The matrix that transforms $v$ into $w$ would have $100 \times 100 = 10,000$ elements. However, using Dirac notation we were able to perform calculations without writing matrix elements explicitly. It will often be the case that Dirac notation will facilitate calculations by working in abstract terms, which will lead to simpler expressions.

To summarise, think of bra-ket notation as being made up of four key concepts from linear algebra:
- The ket $|v\rangle$ is a column vector, $|v\rangle = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$.
- The bra $\langle v|$ is a row vector, $\langle v| = \begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix}$.
- The bra-ket $\langle v|w\rangle$ is an inner product (scalar).
- The ket-bra $|v\rangle\langle w|$ is an outer product (matrix).

We have seen that you can do a lot of maths on kets and bras that would be unwieldy if you had to spell out all the elements of a state vector every time. Operators can assist you. The next topic takes a closer look at how you can use operators to make your calculations.

---

## 1.3 Operators and observables

In physics, an *observable* is a physical quantity that can be measured. We have seen that kets and bras describe the state of a system. But what if you want to measure some quantity – an observable – of the system (such as its momentum) or change the system (such as by raising a hydrogen atom to an excited state)? That’s where operators come in. You apply an operator to a bra or ket to extract a value and/or change the bra or ket to a different state. In general, an operator gives you a new bra or ket when you use that operator:

$$\hat{A}|\psi\rangle = |\psi'\rangle. \tag{1.10}$$

In a similar way to the way we describe wave functions by vectors, the operators are described mathematically by matrices. There are many operators in quantum physics. Some of the most important ones are:

### Hamiltonian operator
$\hat{H}$: When applied to a bra or ket, it gives you the energy of the state that the bra or ket represents:

$$\hat{H}|\psi\rangle = E|\psi\rangle, \tag{1.11}$$

where $E$ is the energy of the system represented by the ket $|\psi\rangle$.

### Identity operator
$\hat{I}$: This operator leaves the state unchanged:

$$\hat{I}|\psi\rangle = |\psi\rangle. \tag{1.12}$$

### Gradient operator
$\boldsymbol{\nabla}$: This operator takes a spatial derivative. For example, in three dimensions it can be written as:

$$\boldsymbol{\nabla}|\psi\rangle = \frac{\partial}{\partial x}|\psi\rangle \hat{\mathbf{e}}_x + \frac{\partial}{\partial y}|\psi\rangle \hat{\mathbf{e}}_y + \frac{\partial}{\partial z}|\psi\rangle \hat{\mathbf{e}}_z = \left( \frac{\partial}{\partial x}\hat{\mathbf{e}}_x + \frac{\partial}{\partial y}\hat{\mathbf{e}}_y + \frac{\partial}{\partial z}\hat{\mathbf{e}}_z \right)|\psi\rangle. \tag{1.13}$$

### Linear momentum operator
$\hat{P}$: This operator finds the momentum of a state. It looks like this:

$$\hat{P}|\psi\rangle = -i\hbar\boldsymbol{\nabla}|\psi\rangle. \tag{1.14}$$

### Time-evolution operator
$\hat{U}$: This operator allows us to evolve a wave function forward in time. For a Hamiltonian $\hat{H}$ that is time-independent, we have $|\psi(t)\rangle = \hat{U}|\psi(0)\rangle$, where

$$\hat{U} = e^{-i\hat{H}t/\hbar} \tag{1.15}$$

denotes the time-evolution operator.

In the last example, you notice that an operator can be a function of another operator.

There are some classes of operators that have particular importance in quantum physics: *Hermitian* operators and *unitary* operators. An operator $\hat{A}$ is Hermitian if it is equal to its Hermitian adjoint $\hat{A}^\dagger$:

$$\hat{A}^\dagger = \hat{A}. \tag{1.16}$$

To find the Hermitian adjoint of an operator $\hat{A}$ (remember, we are manipulating matrices here):
1. find the transpose $\hat{A}^T$ by interchanging the rows and columns
2. take the complex conjugate

$$\hat{A}^{T*} = \hat{A}^\dagger. \tag{1.17}$$

In linear algebra, finding the inverse of the matrix is often useful because applying the inverse of an operator undoes the work the operator did: $\hat{A}^{-1}\hat{A} = \hat{A}\hat{A}^{-1} = \hat{I}$. But finding the inverse of a large matrix usually isn't easy, so quantum physics calculations are sometimes limited to working with *unitary operators*, $\hat{U}$, where the operator's inverse is equal to its Hermitian adjoint:

$$\hat{U}^{-1} = \hat{U}^\dagger. \tag{1.18}$$

Eq. (1.18) leads to the following property:

$$\hat{U}^\dagger \hat{U} = \hat{I}. \tag{1.19}$$

The *expectation value* of an operator is the mean or average value of that operator with respect to a given quantum state. In other words, we are asking the following question: if a quantum state $|\psi\rangle$ is prepared many times and we measure a quantity associated with the operator $\hat{A}$ each time, what is the average of the measurement results? This is the expectation value and we write this as

$$\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle. \tag{1.20}$$

Now, the outcome of a measurement has got to be a real number, and so, a fortiori, is the average of many measurements $\langle A \rangle = \langle A \rangle^*$. This condition is equivalent to saying that $\hat{A}$ is a Hermitian operator. In Week 2, we will learn about the operators in more detail, but it is sufficient for now to notice that Hermitian operators naturally arise in quantum mechanics because their expectation values are real.

---

## 1.4 Eigenfunctions and eigenvalues

When you apply an operator to a ket, you generally get a new ket. For instance, $\hat{A}|\psi\rangle = |\psi'\rangle$. However, sometimes you can make matters a little simpler by casting your problem in terms of *eigenfunctions* and *eigenvalues*. Instead of giving you an entirely new ket, applying an operator to its eigenfunction (a ket) merely gives you the same eigenfunction back again, multiplied by its eigenvalue (a constant). In other words, $|\psi\rangle$ is an eigenfunction of the operator $\hat{A}$ if the number $\lambda$ is a complex constant and obeys the equation

$$\hat{A}|\psi\rangle = \lambda|\psi\rangle. \tag{1.21}$$

Notice that an eigenvalue can be complex, but if the operators are Hermitian, the values of $\lambda$ are real and their eigenfunctions are orthogonal. The collection of all the eigenvalues of an operator is called its *spectrum*. Sometimes two (or more) linearly independent eigenfunctions share the same eigenvalue; in that case, the spectrum is said to be *degenerate*.

This has an important interpretation in physics. If you measure the value of a physical observable $\hat{A}$, then the answer that you get will be one of the eigenvalues of $\hat{A}$. This is the key idea in quantum mechanics that relates operators to observables.

We've already met this idea in the previous section. The time-independent Schrödinger equation is simply the eigenvalue equation for the Hamiltonian. Indeed, using separable solutions of the form

$$\psi(x, t) = e^{-i\omega t}\psi(x), \tag{1.22}$$

we can rewrite Eq. (1.4) (we drop briefly Dirac notation to work in the same form as Eq. (1.4)):

$$\left( -\frac{\hbar^2}{2m} \frac{\partial^2 \psi(x, t)}{\partial x^2} + V\psi(x, t) \right) = i\hbar \frac{\partial \psi(x, t)}{\partial t}$$

$$\left( -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V \right)\psi(x) = i\hbar (-i\omega) \psi(x)$$

$$\hat{H}\psi(x) = \hbar\omega\psi(x)$$

$$\hat{H}\psi(x) = E\psi(x),$$

with eigenvalue $E = \hbar\omega$, eigenfunction $\psi(x)$ and Hamiltonian operator $\hat{H} = \left(-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V\right)$. All physical observables have an associated eigenvalue equation. For the momentum operator this is

$$\hat{P}|\psi\rangle = \mathbf{p}|\psi\rangle \implies -i\hbar\boldsymbol{\nabla}|\psi\rangle = \mathbf{p}|\psi\rangle. \tag{1.23}$$

(Notice, the bold $\mathbf{p}$ represents the momentum, which is a vectorial quantity.)

---

## Summary

Well done! You have now reached the end of this week’s Study – Week 1: Language and tools of quantum mechanics.

In this section we explored the basics of linear algebra, which is the branch of mathematics dealing with vectors and matrices. We also covered some fundamental concepts of quantum mechanics, such as wave functions, operators and Dirac notation to give you a brief overview and intuitive understanding of concepts that we will cover in more detail in the following weeks.