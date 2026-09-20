# Week 2: The wave functions, operators and observables: Study

## 2. The wave functions, operators and observables

### Introduction
This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

In quantum mechanics the wave function is a mathematical description of a quantum particle's behaviour. It is a complex function that provides information about the particle's position, momentum and other properties. However, the wave function alone is not enough to make predictions about the behaviour of the particle. To extract useful information from the wave function, we need to use operators and observables.

Operators are mathematical objects that act on the wave function to produce a new wave function. They represent physical quantities such as position, momentum, energy and angular momentum. Operators are essential in quantum mechanics as they allow us to calculate the behaviour of quantum particles.

Observables are physical quantities that can be measured in experiments. They are represented by operators in quantum mechanics, and their eigenvalues correspond to the possible outcomes of measurements. Observables can include position, momentum, energy, angular momentum and many others.

In this section, we will explore the concept of the wave function, operators and observables in detail. We will discuss the mathematical representation of these concepts, and how they are used to make predictions about the behaviour of quantum particles.

In this Study you will cover the following topics:
- 2.1 Postulate 1: The state of a system
- 2.2 Postulate 2: Operators and observables

---

## 2.1 Postulate 1: The state of a system

The state of a quantum mechanical system is completely specified by the function $\psi(\mathbf{r}, t)$ that depends on the coordinates of the particle $\mathbf{r} = x\hat{\mathbf{e}}_x + y\hat{\mathbf{e}}_y + z\hat{\mathbf{e}}_z$ and the time $t$. This function is called the wave function or state function and has the property that the probability density $|\psi(\mathbf{r}, t)|^2 \mathrm{d}^3\mathbf{r} = \psi^*(\mathbf{r}, t)\psi(\mathbf{r}, t)\mathrm{d}^3\mathbf{r}$ is the probability that the particle lies in the volume element $\mathrm{d}^3\mathbf{r}$ located at position $\mathbf{r}$ and time $t$. This is the probabilistic interpretation of the wave function. As a result, the wave function must satisfy the condition that the probability of finding the particle somewhere in space is 1 and this gives us the normalisation condition,

$$\int_{-\infty}^{+\infty} \psi^*(\mathbf{r}, t)\psi(\mathbf{r}, t) \mathrm{d}^3\mathbf{r} = 1. \tag{2.1}$$

In order to represent a physical system, a wave function must satisfy specific mathematical requirements: wave functions $\psi(\mathbf{r}, t)$ that are physically acceptable must, along with their first derivatives $\frac{\mathrm{d}\psi(\mathbf{r}, t)}{\mathrm{d}\mathbf{r}}$, be *finite*, *continuous* and *single-valued* everywhere.

### Superposition
The state of a system does not have to be represented by a single wave function; it can be represented by a superposition of two or more wave functions. If $\psi_1(\mathbf{r}, t)$ and $\psi_2(\mathbf{r}, t)$ are both viable states of a system, then so too is any linear combination

$$\psi(\mathbf{r}, t) = \alpha_1 \psi_1(\mathbf{r}, t) + \alpha_2 \psi_2(\mathbf{r}, t), \tag{2.2}$$

where $\alpha_1$ and $\alpha_2$ are complex numbers. Mathematically, this is the statement that the states form a vector space over the complex numbers. An example from classical physics is a vibrating string; its state can be represented by a single wave or by the superposition (linear combination) of many waves. So, in general, according to the superposition principle, the linear superposition of many wave functions (which describe the various permissible physical states of a system) gives a new wave function that represents another possible physical state of the system. Using Dirac notation, we can write that statement as:

$$|\psi\rangle = \sum_i \alpha_i |\psi_i\rangle, \tag{2.3}$$

where the $\alpha_i$ are complex numbers. If we want to calculate the probability for this specific superposition, we use the Born rule and express the modulus square of the wave function $\psi$:

$$P = \left| \sum_i \alpha_i |\psi_i\rangle \right|^2. \tag{2.4}$$

### The inner product
An important mathematical structure present on Hilbert space is an inner product. It takes two vectors and returns a number. We will use it all the time when manipulating kets.

Given two vectors $\mathbf{u}$ and $\mathbf{v}$, the inner product is simply $\mathbf{u} \cdot \mathbf{v}$. Using Dirac notation, we write the inner product as

$$\langle u | v \rangle = \mathbf{u} \cdot \mathbf{v}. \tag{2.5}$$

A slight amendment to the inner product is needed if we're dealing with a complex vector space like we do in quantum mechanics. In this case, the inner product is

$$\langle u | v \rangle = \mathbf{u}^* \cdot \mathbf{v}, \tag{2.6}$$

where we take the complex conjugation of the first vector before we take the dot product. This has the advantage that the inner product of any vector with itself is necessarily non-negative

$$\langle u | u \rangle = \mathbf{u}^* \cdot \mathbf{u} \ge 0. \tag{2.7}$$

As we have seen previously, in quantum mechanics we often use an infinite-dimensional vector space of functions. The inner product between two complex functions $\psi(\mathbf{r})$ and $\phi(\mathbf{r})$ is defined by

$$\langle \psi | \phi \rangle = \int_{-\infty}^{+\infty} \psi^*(\mathbf{r}) \phi(\mathbf{r}) \mathrm{d}^3\mathbf{r}. \tag{2.8}$$

From the definition, we see that the inner product is linear in the second argument

$$\langle \psi | \alpha_1 \phi_1 + \alpha_2 \phi_2 \rangle = \alpha_1 \langle \psi | \phi_1 \rangle + \alpha_2 \langle \psi | \phi_2 \rangle, \tag{2.9}$$

for any complex numbers $\alpha_1$ and $\alpha_2$. However, the inner product is anti-linear in the first argument, which simply means that the complex conjugation on $\psi$ gives us

$$\langle \alpha_1 \psi_1 + \alpha_2 \psi_2 | \phi \rangle = \alpha_1^* \langle \psi_1 | \phi \rangle + \alpha_2^* \langle \psi_2 | \phi \rangle. \tag{2.10}$$

From the anti-linear statement, it follows that complex conjugation exchanges the two entries in the inner product

$$\langle \psi | \phi \rangle^* = \langle \phi | \psi \rangle. \tag{2.11}$$

To finish this section, let's introduce a bit of mathematical language. In mathematics, a vector space, whether finite or infinite-dimensional, with inner product defined as above, is called a Hilbert space $\mathcal{H}$. Hilbert space is the stage for quantum mechanics. The first thing you should do when describing any quantum system is specify its Hilbert space. If a particle is moving on some Hilbert space $S$, then the relevant Hilbert space is called $\mathcal{H} = L^2(S)$. The '$L^2$' tells us that $\mathcal{H}$ is the space of square-normalisable functions on $S$. Here the word 'square' and the superscript 2 both reflect the fact that you should integrate $|\psi|^2$ to determine whether it's normalisable. Again, in order to satisfy probabilistic interpretation of quantum mechanics, the probability density when summed over all space must add to 1. Stating that quantum mechanics is staged in Hilbert space $\mathcal{H} = L^2(S)$ is just a fancy way of saying the same thing in the language of mathematics.

---

## 2.2 Postulate 2: Operators and observables

In physics, an *observable* is a physical quantity that can be measured. For example, position, momentum and energy are all observables. According to the second postulate of quantum mechanics, to every observable in classical mechanics there corresponds a linear, *Hermitian operator* in quantum mechanics.

To understand what that means, it is helpful to remind ourselves of what we have seen in Week 1 about classical physics. In the classical world, the state of a physical system is described by its position $\mathbf{r}$ and velocity $\mathbf{v}$ (or, equivalently, momentum $\mathbf{p} = m\mathbf{v}$). All possible functions made of $\mathbf{r}$ and $\mathbf{p}$ will be observables. Indeed, the position and momentum are observables themselves, but we can also use the information of the state to calculate other observables, such as angular momentum

$$\mathbf{L} = \mathbf{r} \times \mathbf{p},$$

or energy

$$E = \frac{\mathbf{p}^2}{2m} + V(\mathbf{r}).$$

In general, any function $f(\mathbf{r}, \mathbf{p})$ can be considered a classical observable.

In the quantum world, the difference is that the state is now given by wave function $\psi(\mathbf{r})$. The question is then to know what the quantum observables look like. The second postulate of quantum mechanics states that all observables are represented by linear operators on the Hilbert space, which we can denote $\hat{A}$. Such an operator $\hat{A}$ acts on the wave function $\psi(\mathbf{r})$ and gives back a new wave function. The linearity of operators, similarly to wave functions, means that operators obey

$$\hat{A}[\alpha_1 \psi_1(\mathbf{r}) + \alpha_2 \psi_2(\mathbf{r})] = \alpha_1 \hat{A}[\psi_1(\mathbf{r})] + \alpha_2 \hat{A}[\psi_2(\mathbf{r})], \tag{2.12}$$

for any complex numbers $\alpha_1$ and $\alpha_2$.

So, what do those operators look like? The answer depends on the dimensionality of the vector space. If the state is described by a vector of finite dimension, say dimension $N$, then the corresponding linear operators are just $N \times N$ matrices. However, if the state is described by infinite-dimensional vector spaces (wave functions), then the operators take a form of differential operators. To make those notions less abstract, let's give a few examples of operators acting in infinite-dimensional Hilbert spaces.

- For a particle moving in three dimensions there are three position operators, one for each direction. These operators act on a wave function by multiplication:

$$\hat{x}\psi(\mathbf{r}) = x\psi(\mathbf{r})$$
$$\hat{y}\psi(\mathbf{r}) = y\psi(\mathbf{r})$$
$$\hat{z}\psi(\mathbf{r}) = z\psi(\mathbf{r})$$

If we know the state of a system, say a particle described by wave function $\psi(\mathbf{r})$, then applying the operator position $\hat{x}$ to $\psi(\mathbf{r})$ will return the position $x$ (no hat!).

- The momentum operator for a particle moving in three dimensions is

$$\hat{\mathbf{p}} = -i\hbar\boldsymbol{\nabla},$$

or, written out longhand,

$$\hat{p}_x = -i\hbar \frac{\partial}{\partial x}$$
$$\hat{p}_y = -i\hbar \frac{\partial}{\partial y}$$
$$\hat{p}_z = -i\hbar \frac{\partial}{\partial z}$$

Again, these should be thought of in terms of their action on the wave functions, for example,

$$\hat{p}_x \psi(\mathbf{r}) = -i\hbar \frac{\partial \psi(\mathbf{r})}{\partial x}.$$

- Once we know the operators for position and momentum, we can build the other operators. For example, the angular momentum operator is built from position and momentum operators in a way that is reminiscent of its classical form ($\mathbf{L} = \mathbf{r} \times \mathbf{p}$):

$$\hat{\mathbf{L}} = -i\hbar \hat{\mathbf{r}} \times \boldsymbol{\nabla}.$$

Similarly, the energy operator is

$$\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\hat{\mathbf{r}}),$$

where we define potential energy operator as $\hat{V}(\mathbf{r})\psi(\mathbf{r}) = V(\mathbf{r})\psi(\mathbf{r})$. Due to the special role the energy operator plays in quantum mechanics, it has its own name, with $\hat{H}$ standing for Hamiltonian (rather than $\hat{E}$ for energy).

### Eigenfunctions and eigenvalues
Given an $N \times N$ matrix $A$, its *eigenvalues* are a collection of up to $N$ numbers $\lambda$ that solve the equation

$$A\mathbf{u} = \lambda\mathbf{u}.$$

The corresponding vector $\mathbf{u}$ is then called the eigenvector. As operators in finite-dimensional vector space are represented by matrices, it is interesting to solve a similar eigenvalue equation

$$\hat{A}\psi(\mathbf{r}) = \lambda\psi(\mathbf{r}),$$

where $\lambda$ are its eigenvalues, and the corresponding functions $\psi(\mathbf{r})$ are its eigenfunctions. The collection of all eigenvalues is called the spectrum of the operator $\hat{A}$.

This has an important interpretation in quantum mechanics. If you measure the value of a physical observable associated to the operator $\hat{A}$, then the answer that you get will be one of the eigenvalues of $\hat{A}$. This is the key idea that relates operators to observables: the outcome of any measurement of $\hat{A}$ lies in the spectrum of $\hat{A}$.

We have seen that the time-independent Schrödinger equation is simply the eigenvalue equation for the Hamiltonian

$$\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r}).$$

All physical observables have an associated eigenvalue equation. For the momentum operator this is

$$\hat{\mathbf{p}}\psi(\mathbf{r}) = \mathbf{p}\psi(\mathbf{r}) \implies -i\hbar\boldsymbol{\nabla}\psi(\mathbf{r}) = \mathbf{p}\psi(\mathbf{r}).$$

The momentum eigenvalue equation can be solved. The momentum eigenstates are

$$\psi(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}}$$
$$\hat{\mathbf{p}}\psi(\mathbf{r}) = \hbar\mathbf{k}\psi(\mathbf{r}).$$

These eigenfunctions $\psi(\mathbf{r})$ are called *plane wave states* and their associated momentum eigenvalue is $\mathbf{p} = \hbar\mathbf{k}$, which is nothing other than the de Broglie matter wave relationship between momentum and wavelength.

### Hermitian operators
Not any linear operator qualifies as a physical observable in quantum mechanics. We should restrict attention to those operators that are *Hermitian*. Remember from Week 1 that an operator is said to be Hermitian if

$$\hat{A} = \hat{A}^\dagger, \tag{2.13}$$

where $\hat{A}^\dagger$ is the adjoint of $\hat{A}$. Given the operator $\hat{A}$, its adjoint $\hat{A}^\dagger$ is defined by the requirement that the following inner product relation holds:

$$\langle \psi | \hat{A}\phi \rangle = \langle \hat{A}^\dagger \psi | \phi \rangle, \tag{2.14}$$

for all states $\psi$ and $\phi$. For the sake of completeness, we can write this condition in terms of integrals of wave functions:

$$\int \psi^* \hat{A} \phi \mathrm{d}^3\mathbf{r} = \int (\hat{A}^\dagger \psi)^* \phi \mathrm{d}^3\mathbf{r}. \tag{2.15}$$

You'll notice the advantage of the Dirac notation as its compactness enhances the readability of expressions.

All physical observables correspond to Hermitian operators. As an exercise, let's check that this is the case for the position operator. For $\hat{\mathbf{r}}$ to be Hermitian, we must show that:

$$\langle \phi | \hat{\mathbf{r}}\psi \rangle = \langle \psi | \hat{\mathbf{r}}\phi \rangle^*.$$

On the left-hand side, we have:

$$\langle \phi | \hat{\mathbf{r}}\psi \rangle = \int \phi^* (\mathbf{r}\psi) \mathrm{d}^3\mathbf{r}.$$

The right-hand side gives:

$$\langle \psi | \hat{\mathbf{r}}\phi \rangle^* = \left( \int \psi^* (\mathbf{r}\phi) \mathrm{d}^3\mathbf{r} \right)^*.$$

Eigenvalues of $\hat{\mathbf{r}}$ are real, $\mathbf{r} = \mathbf{r}^*$, thus:

$$\langle \psi | \hat{\mathbf{r}}\phi \rangle^* = \int \psi (\mathbf{r}\phi^*) \mathrm{d}^3\mathbf{r} = \int \phi^* (\mathbf{r}\psi) \mathrm{d}^3\mathbf{r}$$
$$\therefore \langle \phi | \hat{\mathbf{r}}\psi \rangle = \langle \psi | \hat{\mathbf{r}}\phi \rangle^*$$

### Properties of Hermitian operators
The eigenvalue equation for a Hermitian operator is

$$\hat{A}|\psi_n\rangle = \lambda_n |\psi_n\rangle,$$

where $\lambda_n$ are the eigenvalues and $\psi_n$ the eigenfunctions. The label runs over $n = 1, \dots, \infty$, reflecting the fact that we have an infinite-dimensional Hilbert space. For Hermitian operator $\hat{A}$, the eigenvalues and eigenfunctions have the following two properties:
- The eigenvalues $\lambda_n$ are real.
- If two eigenvalues are distinct, $\lambda_n \neq \lambda_m$, then their corresponding eigenfunctions are orthogonal: $\langle \psi_n | \psi_m \rangle = 0$.

Recall our important statement from earlier: the outcome of any measurement of $\hat{A}$ is given by one of the eigenvalues of $\hat{A}$. The first of the properties above ensures that the result of any measurement is guaranteed to be a real number. Indeed, all measurements in the labs always give real numbers, never complex, so it is a good thing that quantum mechanics agrees with the reality.

To prove the first property above, start by writing that operator $\hat{A}$ is Hermitian. For any $\psi_n$ and $\psi_m$ we have:

$$\langle \psi_n | \hat{A}^\dagger \psi_m \rangle = \langle \psi_n | \hat{A} \psi_m \rangle.$$

Then, using the eigenvalue equations, rewrite the expressions above using eigenvalues:

$$\langle \psi_n | \hat{A}^\dagger \psi_m \rangle = \lambda_n^* \langle \psi_n | \psi_m \rangle$$
$$\langle \psi_n | \hat{A} \psi_m \rangle = \lambda_m \langle \psi_n | \psi_m \rangle$$
$$\implies (\lambda_n^* - \lambda_m)\langle \psi_n | \psi_m \rangle = 0$$

If we set $n = m$, for the last expression to be true for any $\psi_n$ and $\psi_m$, it follows that

$$\lambda_n^* = \lambda_n, \tag{2.16}$$

meaning that the eigenvalue $\lambda_n$ is real. That proves the first property. If we set $n \neq m$, that is, $\lambda_n \neq \lambda_m$, for the same expression to be true for any $\psi_n$ and $\psi_m$, it follows that

$$\langle \psi_n | \psi_m \rangle = \int \psi_n^* \psi_m \mathrm{d}\mathbf{r} = 0, \tag{2.17}$$

meaning that the two eigenfunctions $\psi_n$ and $\psi_m$ must be orthogonal, which proves the second property.

An operator with distinct eigenvalues is said to have a non-degenerate spectrum. If, on the other hand, two or more eigenvalues coincide, then we say it has a degenerate spectrum. In this case, it's still possible to pick orthogonal eigenfunctions, but we won't prove this. However, it means that in all cases, if we normalise the eigenstates then we can always take them to obey

$$\langle \psi_n | \psi_m \rangle = \int \psi_n^* \psi_m \mathrm{d}\mathbf{r} = \delta_{nm}, \tag{2.18}$$

where $\delta_{nm}$ is the Kronecker delta symbol defined as

$$\delta_{nm} = \begin{cases} 0 & \text{if } n \neq m \\ 1 & \text{if } n = m \end{cases}. \tag{2.19}$$

Eigenfunctions that obey Eq. (2.18) are said to be orthonormal. The eigenfunctions of any Hermitian operator are complete. This means that we can expand any wave function $\psi(\mathbf{r})$ in terms of eigenstates of a given operator $\hat{A}$

$$\psi(\mathbf{r}) = \sum_{n=1}^{\infty} a_n \psi_n(\mathbf{r}), \tag{2.20}$$

for some complex coefficients $a_n$. If you know both the wave function $\psi$ and the normalised eigenfunctions $\psi_n$, then it's simple to get an expression for these coefficients: we use the orthonormality relation from Eq. (2.18), together with linearity of the inner product from Eq. (2.12), to get

$$\langle \psi_n | \psi \rangle = \sum_m a_m \langle \psi_n | \psi_m \rangle = \sum_m a_m \delta_{nm} = a_n, \tag{2.21}$$

or, in terms of integrals,

$$a_n = \int \psi_n^*(\mathbf{r}) \psi(\mathbf{r}) \mathrm{d}^3\mathbf{r}. \tag{2.22}$$

Finally, the norm of a wave function $\psi(\mathbf{r})$ is

$$\|\psi(\mathbf{r})\|^2 = \int |\psi(\mathbf{r})|^2 \mathrm{d}^3\mathbf{r} = \sum_m \sum_n \int a_n^* \psi_n^* a_m \psi_m \mathrm{d}^3\mathbf{r} = \sum_n |a_n|^2, \tag{2.23}$$

where we have again used the orthonormality condition from Eq. (2.18). We see that a wave function is normalised only if

$$\sum_n |a_n|^2 = 1. \tag{2.24}$$

---

## Summary

Well done! You have now reached the end of this week’s Study – Week 2: The wave functions, operators and observables.

In this section, we explored the concept of the wave function, operators and observables. We also discussed the mathematical representation of these concepts, and how they are used to make predictions about the behaviour of quantum particles.

---

## References

There are no references for this week.