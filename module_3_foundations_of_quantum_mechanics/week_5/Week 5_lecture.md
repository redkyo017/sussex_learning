# Week 5: Quantum harmonic oscillator: Study

## Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

This week, we will study the important topic of the quantum harmonic oscillator. The harmonic oscillator is a key system both in classical and quantum mechanics. Its importance stems from the fact that many systems can be represented using the formalism of the harmonic oscillator. It is also one of the few quantum-mechanical systems for which an exact, analytical solution is known.

In this Study you will cover the following topics:

- 5.1 Introduction to the harmonic oscillator
- 5.2 The quantum harmonic oscillator
- 5.3 Ladder and number operators
- 5.4 Energy eigenvalues
- 5.5 Energy eigenstates

## 5.1 Introduction to the harmonic oscillator

The defining feature of the harmonic oscillator is that it is a system with a potential energy that depends, in the one-dimensional case, quadratically on the position $x$

$$V(x) = \frac{1}{2} k x^2 \tag{5.1}$$

where $k$ is a positive proportionality constant. Such a potential is shown in Figure 5.1. We know that the motion of a particle of mass $m$ in such a potential is harmonic motion of frequency $\omega = \sqrt{k/m}$. It is common to rewrite Eq. (5.1) using $\omega$, as frequency of motion presents a more intuitive picture than that carried by the coefficient $k$:

$$V(x) = \frac{1}{2} m \omega^2 x^2 \tag{5.2}$$

> **Figure 5.1:** The harmonic potential. The figure shows the harmonic potential as a function of the position $x$. The harmonic potential has the shape of a parabola and is proportional to $x^2$. 
> *Long description:* A diagram showing an x-axis and a y-axis that starts halfway along the x-axis, which bisects an inverted parabolic curve labelled $V(x) = \frac{1}{2} k x^2 = \frac{1}{2} m \omega^2 x^2$.

Now that we have defined a harmonic oscillator, there are two questions we might ask about it:

- How does the wave function $\psi(x, t)$ of a particle in harmonic potential change as a function of time? To answer this question, we need to know the Hamiltonian.
- What are the oscillator's possible energies? These are also determined by the Hamiltonian.

To answer those questions in the context of quantum physics, we will now consider the quantum version of the harmonic oscillator.

## 5.2 The quantum harmonic oscillator

Classical physics tells us that the Hamiltonian of the harmonic oscillator is simply the sum of the kinetic and potential energies of the system

$$H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2 \tag{5.3}$$

We can now turn it into a quantum mechanical equation by reinterpreting $x$ and $p$ as operators, defined by their action on $\psi(x)$. We'll use the 'hat' symbol to distinguish our quantum operators $\hat{x}$ and $\hat{p}$ from their classical counterparts. From previous weeks, we know that we can replace classical quantities $x$ and $p$ with their corresponding quantum operators:

$$\hat{x} |\psi\rangle \to x \psi(x)$$

$$\hat{p} |\psi\rangle \to -i\hbar \frac{\partial}{\partial x} \psi(x)$$

Replacing $x$ and $p$ in Eq. (5.3) by the operators $\hat{x}$ and $\hat{p}$, we obtain the quantum version of the harmonic oscillator Hamiltonian

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 \tag{5.4}$$

and can express explicitly its action on the wave function $\psi$

$$\hat{H} |\psi\rangle \to -\frac{\hbar^2}{2} \frac{\partial^2 \psi(x)}{\partial x^2} + \frac{1}{2}\omega^2 x^2 \psi(x) \tag{5.5}$$

It's difficult to overstate the importance of the harmonic oscillator in quantum mechanics. It is, by some margin, the single most important example that we will study. To paraphrase Prof. David Tong (2017), the reasons for this are twofold [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-5-quantum-harmonic-oscillator-study#sect6). The first is Taylor's theorem: if you take any potential $V(x)$ and expand close to a minimum then, at leading order, you will most likely find the harmonic oscillator. This means that small perturbations of more or less any system in Nature are described by the Hamiltonian in Eq. (5.4).

The second reason for the utility of the harmonic oscillator is more practical. Human beings are not particularly good at solving equations. At some point, the only system that we can actually solve is the harmonic oscillator. Or, more precisely, things that can be made to look like the harmonic oscillator. The art of physics is then to make everything look like a harmonic oscillator. Take whatever you think is the coolest result in physics – maybe the Higgs boson, or some new material like topological insulators, or maybe gravitational waves or Hawking radiation. For all of them, the underlying theory is primarily to do with harmonic oscillators.

The problem is how to find the energy eigenvalues and eigenstates of this Hamiltonian. This problem can be studied by means of two separate methods. The first method, called the analytic method, consists of solving the time-independent Schrödinger equation for the Hamiltonian in Eq. (5.4). The second method, called the ladder or algebraic method, does not deal with solving the Schrödinger equation, but deals instead with operator algebra involving operators known as the *creation* and *annihilation* or ladder operators; this method is in essence a matrix formulation, because it expresses the various quantities in terms of matrices. We are going to adopt the second method, for it is more straightforward, more elegant and much simpler than solving the Schrödinger equation. Unlike the examples seen in the last week, solving the Schrödinger equation for the potential $V(x) = \frac{1}{2}m\omega^2 x^2$ is no easy job.

## 5.3 Ladder and number operators

Let us now show how to solve the harmonic oscillator eigenvalue problem using the algebraic method. Although the two observables that feature in this Hamiltonian are position $\hat{x}$ and momentum $\hat{p}$, it turns out that to develop the theory of the quantum harmonic oscillator there are two linear combinations of these operators that are extremely useful. One linear combination will lead to the *lowering* (or *annihilation*) operator, the second to the *raising* (or *creation*) operator, and collectively we will refer to those as *ladder operators*. For now, these are just names, but as we go along we'll see that the names were well chosen.

Lowering (annihilation) operator:

$$\hat{a} = \frac{1}{\sqrt{2}} \left( \sqrt{\frac{m\omega}{\hbar}} \hat{x} + i \frac{1}{\sqrt{m\hbar\omega}} \hat{p} \right) \tag{5.6}$$

Raising (creation) operator:

$$\hat{a}^\dagger = \frac{1}{\sqrt{2}} \left( \sqrt{\frac{m\omega}{\hbar}} \hat{x} - i \frac{1}{\sqrt{m\hbar\omega}} \hat{p} \right) \tag{5.7}$$

Notice that those two operators are each other's adjoint, but they are not equal, $\hat{a} \neq \hat{a}^\dagger$. Therefore, they are not Hermitian operators. This means that, unlike position and momentum operators, the ladder operators don't represent physical observables. Remember, the peculiarity of Hermitian operators is that they correspond to measurable quantities. We apply a Hermitian operator to a quantum system, or rather, to the wave function $\psi$ and, as a result, we obtain one of the possible values in the spectrum of eigenvalues of that operator. While ladder operators are not used for measurement, they are extremely handy to manipulate and describe our system. We can reverse the Eqs. (5.6) and (5.7) and express the position and momentum operators as functions of ladder operators:

Position operator:

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}} (\hat{a}^\dagger + \hat{a}) \tag{5.8}$$

Momentum operator:

$$\hat{p} = i \sqrt{\frac{m\hbar\omega}{2}} (\hat{a}^\dagger - \hat{a}) \tag{5.9}$$

### Commutators

Using operators in the study of the harmonic oscillator reduces the entire study of wave functions and wave equations to a very small number of algebraic tricks, which almost always involve the commutation relations. If you are used to ordinary algebra, the order of multiplication doesn't matter: $A \cdot B = B \cdot A$. But linear operators are not ordinary numbers: when they are multiplied (or applied sequentially), the order counts. In general, when $\hat{A}$ acts on $\hat{B} |\psi\rangle$, the result is not the same as when $\hat{B}$ acts on $\hat{A} |\psi\rangle$. In other words, except for special cases, $\hat{A}\hat{B} \neq \hat{B}\hat{A}$. Given two operators or matrices, the combination $\hat{A}\hat{B} - \hat{B}\hat{A}$ is called the commutator of $\hat{A}$ with $\hat{B}$ and it is denoted by a special symbol:

$$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$$

For example, the commutators between operators $\hat{x}$ and $\hat{p}$ are:

$$[\hat{x}, \hat{p}] = \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar$$
$$[\hat{x}, \hat{x}] = \hat{x}\hat{x} - \hat{x}\hat{x} = 0$$
$$[\hat{p}, \hat{p}] = \hat{p}\hat{p} - \hat{p}\hat{p} = 0$$

When the commutator between two operators is different from zero, it indicates that the order of application of the two operators is important. To observe, or measure, simultaneously two different quantities, the commutator of their observables (operators) must be zero. The fact that position and momentum operators don't commute is at the heart of Heisenberg's uncertainty principle [2]: we cannot measure at the same time with arbitrary accuracy the position and the momentum of a particle. Conversely, the pairs of physical observables whose commutator is zero have no uncertainty principle and we can know both of them at the same time. So, you can see why physicists like to calculate commutation relations between various operators, and that's what we will be doing next for our ladder operators.

$$
\begin{aligned}
[\hat{a}, \hat{a}^\dagger] &= \left[ \frac{1}{\sqrt{2}}\left(\sqrt{\frac{m\omega}{\hbar}}\hat{x} + i\frac{1}{\sqrt{m\hbar\omega}}\hat{p}\right), \frac{1}{\sqrt{2}}\left(\sqrt{\frac{m\omega}{\hbar}}\hat{x} - i\frac{1}{\sqrt{m\hbar\omega}}\hat{p}\right) \right] \\
&= \frac{1}{2} \left( \frac{m\omega}{\hbar} \underbrace{[\hat{x}, \hat{x}]}_{0} + \frac{1}{m\hbar\omega}\underbrace{[\hat{p}, \hat{p}]}_{0} - i\underbrace{[\hat{x}, \hat{p}]}_{i\hbar} + i\underbrace{[\hat{p}, \hat{x}]}_{-i\hbar} \right) \\
&= \frac{1}{2} \left( -i(i\hbar) + i(-i\hbar) \right) \\
\implies [\hat{a}, \hat{a}^\dagger] &= 1 \tag{5.10}
\end{aligned}
$$

Armed with the knowledge of ladder operators, we are ready to introduce another operator that plays an important role in the quantum harmonic oscillator, the *number operator* $\hat{N}$, defined simply as:

$$\hat{N} = \hat{a}^\dagger \hat{a} \tag{5.11}$$

Notice that the number operator, unlike dagger operators, is a Hermitian operator. As usual, to show that the operator is Hermitian, we can show that $\hat{N}^\dagger = \hat{N}$:

$$\hat{N}^\dagger = (\hat{a}^\dagger \hat{a})^\dagger = \hat{a}^\dagger (\hat{a}^\dagger)^\dagger = \hat{a}^\dagger \hat{a} = \hat{N}$$

where we used the results from linear algebra, $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger \hat{A}^\dagger$ and $(\hat{A}^\dagger)^\dagger = \hat{A}$. Let's evaluate the commutator between the number operator and lowering operator:

$$[\hat{N}, \hat{a}] = [\hat{a}^\dagger \hat{a}, \hat{a}] = \hat{a}^\dagger \underbrace{[\hat{a}, \hat{a}]}_{0} + \underbrace{[\hat{a}^\dagger, \hat{a}]}_{-1} \hat{a} = -\hat{a} \tag{5.12}$$

where we used the commutator identity $[\hat{A}\hat{B}, \hat{C}] = \hat{A}[\hat{B}, \hat{C}] + [\hat{A}, \hat{C}]\hat{B}$. Similarly, we can show that:

$$[\hat{N}, \hat{a}^\dagger] = \hat{a}^\dagger \tag{5.13}$$

Let's consider now the eigenvalue equation of the number operator:

$$\hat{N} |\psi_n\rangle = n |\psi_n\rangle$$

where we label the eigenstate $|\psi_n\rangle$ with index $n$ to stress that its corresponding eigenvalue is $n$. We know that operators can act and change quantum states. If we start with some quantum state $|\psi_n\rangle$ and apply lowering operator $\hat{a}$ on it, we will obtain a different state $\hat{a} |\psi_n\rangle$. In our specific example, an interesting property emerges: if $|\psi_n\rangle$ is an eigenstate of $\hat{N}$, then $\hat{a} |\psi_n\rangle$ is also an eigenstate of $\hat{N}$. Let's apply $\hat{N}$ to the state $\hat{a} |\psi_n\rangle$ and see what happens:

$$\hat{N} (\hat{a} |\psi_n\rangle) \equiv \hat{N}\hat{a} |\psi_n\rangle$$

Using the commutation relation from Eq. (5.12) we can write:

$$\hat{N}\hat{a} - \hat{a}\hat{N} = -\hat{a} \implies \hat{N}\hat{a} = \hat{a}\hat{N} - \hat{a}$$

so that:

$$
\begin{aligned}
\hat{N} (\hat{a} |\psi_n\rangle) &= \hat{a}\hat{N} |\psi_n\rangle - \hat{a} |\psi_n\rangle \\
&= \hat{a} \underbrace{(\hat{N} |\psi_n\rangle)}_{n |\psi_n\rangle} - \hat{a} |\psi_n\rangle \\
&= n \hat{a} |\psi_n\rangle - \hat{a} |\psi_n\rangle \\
\implies \hat{N} (\hat{a} |\psi_n\rangle) &= (n - 1) (\hat{a} |\psi_n\rangle)
\end{aligned}
$$

which means that $\hat{a} |\psi_n\rangle$ is an eigenstate of $\hat{N}$ with eigenvalue $(n - 1)$. We can label our new state $\alpha_- |\psi_{n-1}\rangle = \hat{a} |\psi_n\rangle$ to stress that its eigenvalue is $(n - 1)$, with $\alpha_-$ being a constant that allows for an appropriate normalisation of the state.

Similarly, we can do the same exercise with the raising operator $\hat{a}^\dagger$ and find that a new state $\alpha_+ |\psi_{n+1}\rangle = \hat{a}^\dagger |\psi_n\rangle$ is also an eigenstate of operator $\hat{N}$, but with the eigenvalue $(n + 1)$. Combining the two results for clarity, we have:

$$\hat{a} |\psi_n\rangle = \alpha_- |\psi_{n-1}\rangle$$
$$\hat{a}^\dagger |\psi_n\rangle = \alpha_+ |\psi_{n+1}\rangle$$

where $|\psi_n\rangle$, $|\psi_{n-1}\rangle$ and $|\psi_{n+1}\rangle$ are the eigenstates of the operator $\hat{N}$ with the corresponding eigenvalues, respectively, $n$, $n-1$ and $n+1$:

$$\hat{N} |\psi_n\rangle = n |\psi_n\rangle$$
$$\hat{N} |\psi_{n-1}\rangle = (n - 1) |\psi_{n-1}\rangle$$
$$\hat{N} |\psi_{n+1}\rangle = (n + 1) |\psi_{n+1}\rangle$$

So when $\hat{a}$ acts on an eigenstate $|\psi_n\rangle$ of $\hat{N}$ it simply gives us another eigenstate of $\hat{N}$, $|\psi_{n-1}\rangle$, but with the eigenvalue that has decreased by one. This is the reason why we call an operator $\hat{a}$ the *lowering operator*. Similarly, because $\hat{a}^\dagger$ produces a new eigenstate with the eigenvalue that has increased by one, we call an operator $\hat{a}^\dagger$ the *rising operator*. To complete the picture, let's calculate the normalisation constants $\alpha_-$ and $\alpha_+$. Recall that the norm squared is defined as the inner product of the bra with the ket:

$$\|\hat{A} |\psi\rangle\|^2 = \langle \psi | \underbrace{\hat{A}^\dagger}_{\text{bra}} \underbrace{\hat{A} |\psi\rangle}_{\text{ket}} \rangle$$

Starting from:

$$\hat{a} |\psi_n\rangle = \alpha_- |\psi_{n-1}\rangle$$

we will calculate the norm of the left-hand and the right-hand side of the equation and state that it is equal. For the left-hand side, we have:

$$
\begin{aligned}
\|\hat{a} |\psi_n\rangle\|^2 &= \langle \psi_n | \underbrace{\hat{a}^\dagger \hat{a}}_{\hat{N}} | \psi_n \rangle \\
&= \langle \psi_n | \underbrace{\hat{N} | \psi_n \rangle}_{n | \psi_n \rangle} \\
&= n \underbrace{\langle \psi_n | \psi_n \rangle}_{1} \\
\implies \|\hat{a} |\psi_n\rangle\|^2 &= n
\end{aligned}
$$

The norm of the right-hand side of the equation is:

$$\|\alpha_- |\psi_{n-1}\rangle\|^2 = |\alpha_-|^2 \underbrace{\langle \psi_{n-1} | \psi_{n-1} \rangle}_{1} = |\alpha_-|^2$$

Thus we have:

$$|\alpha_-|^2 = n \implies \alpha_- = \sqrt{n}$$

We can do the same calculation for the raising operator, and we would find:

$$|\alpha_+|^2 = n + 1 \implies \alpha_+ = \sqrt{n + 1}$$

Finally, with everything we have seen so far, we can summarise the action of ladder operators on the eigenstates of the number operator $\hat{N}$:

$$\hat{a} |\psi_n\rangle = \sqrt{n} |\psi_{n-1}\rangle \tag{5.14}$$
$$\hat{a}^\dagger |\psi_n\rangle = \sqrt{n + 1} |\psi_{n+1}\rangle \tag{5.15}$$

Let's take a step back. What we have done so far is to construct two ladder operators and study some of their properties, mainly their action on the eigenstates of the number operator $\hat{N}$. You may rightly ask, what was the point of this exercise, and what is the connection between ladder operators, the number operator and the quantum harmonic oscillator? To answer that question, let's do one last calculation by evaluating the quantity $\hbar\omega (\hat{N} + \frac{1}{2})$. We'll start by evaluating the number operator $\hat{N}$ in terms of the two ladder operators:

$$
\begin{aligned}
\hat{N} &= \hat{a}^\dagger \hat{a} \\
&= \left( \frac{1}{\sqrt{2}} \left( \sqrt{\frac{m\omega}{\hbar}} \hat{x} - i \frac{1}{\sqrt{m\hbar\omega}} \hat{p} \right) \right) \left( \frac{1}{\sqrt{2}} \left( \sqrt{\frac{m\omega}{\hbar}} \hat{x} + i \frac{1}{\sqrt{m\hbar\omega}} \hat{p} \right) \right) \\
&= \frac{1}{2} \left( \frac{m\omega}{\hbar} \hat{x}^2 + \frac{1}{m\hbar\omega} \hat{p}^2 + i\frac{1}{\hbar}\hat{x}\hat{p} - i\frac{1}{\hbar}\hat{p}\hat{x} \right) \\
&= \frac{1}{2} \left( \frac{m\omega}{\hbar} \hat{x}^2 + \frac{1}{m\hbar\omega} \hat{p}^2 + \frac{i}{\hbar}\underbrace{[\hat{x}, \hat{p}]}_{i\hbar} \right) \\
&= \frac{1}{2} \left( \frac{m\omega}{\hbar} \hat{x}^2 + \frac{1}{m\hbar\omega} \hat{p}^2 - 1 \right)
\end{aligned}
$$

Now, let's plug this result into:

$$
\begin{aligned}
\hbar\omega \left( \hat{N} + \frac{1}{2} \right) &= \hbar\omega \left( \frac{m\omega}{2\hbar} \hat{x}^2 + \frac{1}{2m\hbar\omega} \hat{p}^2 - \frac{1}{2} + \frac{1}{2} \right) \\
&= \frac{1}{2}m\omega^2 \hat{x}^2 + \frac{1}{2m}\hat{p}^2 \equiv \hat{H}
\end{aligned}
$$

As you can see, the last line is the Hamiltonian of the quantum harmonic oscillator. We can write it in terms of the number operator $\hat{N}$ or in terms of the ladder operators. In both cases, it takes a particularly simple form:

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 = \hbar\omega \left( \hat{N} + \frac{1}{2} \right) = \hbar\omega \left( \hat{a}^\dagger \hat{a} + \frac{1}{2} \right) \tag{5.16}$$

We can interpret the last result as follows. The energy of the quantum harmonic oscillator is quantised. That means that energy can only change in discrete steps called *quanta*, with each step having a magnitude of $\hbar\omega$. In this context, we will see that this operator $\hat{N}$ counts how many energy quanta there are in the system, hence the name number operator. Similarly, the raising and lowering operators allow us to raise or lower the number of energy quanta from the system, hence their name.

For completeness, let's add that the formalism of ladder and number operators extends into many other fields of physics. When dealing with many-particle systems, for example, the number operator measures the number of particles in the system, while the ladder operators allow us to add and remove particles from the system. In that context, the lowering operator is called the *annihilation operator*, $\hat{a}$, and it lowers the number of particles in a given state by one. Conversely, the raising operator is called the *creation operator*, $\hat{a}^\dagger$, and it increases the number of particles in a given state by one.

## 5.4 Energy eigenvalues

Now that we have introduced the tools that allow us to study the quantum harmonic oscillator, we will examine its Hamiltonian. We will see that the energies are quantised, meaning that only discrete energy values are possible. To find those values, we need to determine its spectrum of energy eigenvalues. We will use a method proposed by Paul Dirac (2010), which makes use of ladder and number operators [[3]](https://canvas.sussex.ac.uk/courses/41954/pages/week-5-quantum-harmonic-oscillator-study#sect7).

Let's recall the three expressions that the Hamiltonian operator of the quantum harmonic oscillator can take

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 \tag{5.17}$$

$$= \hbar\omega \left( \hat{a}^\dagger \hat{a} + \frac{1}{2} \right) \tag{5.18}$$

$$= \hbar\omega \left( \hat{N} + \frac{1}{2} \right) \tag{5.19}$$

What we need to do, is to solve the eigenvalue problem of this Hamiltonian

$$\hat{H} |\psi_n\rangle = E_n |\psi_n\rangle$$

where $|\psi_n\rangle$ is an eigenstate that corresponds to the eigenvalue $E_n$. We can write explicitly the Hamiltonian, and then rearrange it to obtain a convenient expression

$$
\begin{aligned}
\hat{H} |\psi_n\rangle &= E_n |\psi_n\rangle \\
\implies \hbar\omega \left( \hat{N} + \frac{1}{2} \right) |\psi_n\rangle &= E_n |\psi_n\rangle \\
\implies \left( \hat{N} + \frac{1}{2} \right) |\psi_n\rangle &= \frac{E_n}{\hbar\omega} |\psi_n\rangle \\
\implies \hat{N} |\psi_n\rangle &= \left( \frac{E_n}{\hbar\omega} - \frac{1}{2} \right) |\psi_n\rangle = n |\psi_n\rangle
\end{aligned}
$$

where $n$ is the eigenvalue of the number operator. It has a simple relationship with the eigenvalue of the Hamiltonian operator $E_n$:

$$n = \frac{E_n}{\hbar\omega} - \frac{1}{2} \implies E_n = \hbar\omega \left( n + \frac{1}{2} \right) \tag{5.20}$$

If we can figure out the eigenvalues of the number operator $n$, then we can use this relationship to immediately build the eigenvalues of the Hamiltonian $E_n$. This is precisely the strategy that we will follow in the following sections.

What do we know about the eigenvalues $n$? We will show in the following sections that $n$ must be an integer larger than or equal to zero. For that we will constrain the possible value of $n$, showing that:

- $n$ is real ($n \in \mathbb{R}$)
- $n$ is larger than or equal to zero ($n \ge 0$)
- finally, $n$ is an integer ($n \in \mathbb{N}$).

- **$n \in \mathbb{R}$:** As the number operator $\hat{N}$ is Hermitian, we know for sure that $n \in \mathbb{R}$.
- **$n \ge 0$:** To show that $n \ge 0$, we write the expectation value of the number operator:

$$\langle \psi_n | \hat{N} | \psi_n \rangle = n \langle \psi_n | \psi_n \rangle = n \tag{5.21}$$

We can write the same expectation value using the ladder operators $\hat{N} = \hat{a}^\dagger \hat{a}$:

$$\langle \psi_n | \hat{N} | \psi_n \rangle = \langle \psi_n | \hat{a}^\dagger \hat{a} | \psi_n \rangle = \|\hat{a} | \psi_n \rangle\|^2 \ge 0 \tag{5.22}$$

where we recall that the norm squared is just bra times ket, and that the norm must always be larger than or equal to zero. Combining the equations Eq. (5.21) and Eq. (5.22), we find that $n \ge 0$.

- **$n \in \mathbb{N}$:** To show that $n$ is an integer, let's consider the action of the lowering operator $\hat{a}$ on the eigenstate $|\psi_n\rangle$:

$$\hat{a} |\psi_n\rangle = \sqrt{n} |\psi_{n-1}\rangle \tag{5.23}$$

The action of $\hat{a}$ on the number operator eigenstate is that it generates another number operator eigenstate with an eigenvalue decreased by 1. We have seen this general result of the lowering operator previously. A particular case of this result is that the action of $\hat{a}$ on $|\psi_n\rangle$ can be equal to zero, meaning that the state $|\psi_n\rangle$ is destroyed:

$$\hat{a} |\psi_n\rangle = 0 \quad \text{if} \quad n = 0$$

Such destruction of the state $|\psi_n\rangle$ occurs if $n = 0$ because the prefactor $\sqrt{n}$ in Eq. (5.23) vanishes. Using these results we're now going to prove that the eigenvalues $n$ can only take integer values.

Eq. (5.23) shows that repeated applications of the operator $\hat{a}$ on $|\psi_n\rangle$ generate a sequence of eigenvectors $n-1, n-2, n-3, \dots$. Since $n \ge 0$ and since $\hat{a} |\psi_0\rangle = 0$, this sequence has to terminate at $n = 0$; this is true if we start with an integer value of $n$. But if we start with a non-integer $n$, the sequence will not lead to the $n = 0$ and will not terminate; hence it leads to eigenvectors with negative values of $n$. But, as shown above, since $n$ cannot be negative, we conclude that $n$ has to be an integer larger than or equal to zero. To recapitulate, the eigenvalues $n$ of the number operator $\hat{N}$ are quantised, as they can only be non-negative integers, $n = 0, 1, 2, 3, \dots$. Using Eq. (5.20), it is straightforward to establish the eigenvalues of the quantum harmonic oscillator Hamiltonian, that is, the allowed quantised energies $E_n$:

$$E_n = \hbar\omega \left( n + \frac{1}{2} \right) \quad \text{with} \quad n = 0, 1, 2, 3, \dots$$

It is common to represent the quantum harmonic oscillator and its energies on a plot like that in Figure 5.2. Notice that the lowest energy eigenvalue corresponds to $n = 0$ and is simply $E_0 = \frac{1}{2}\hbar\omega$. From there, each possible energy eigenvalue is separated by a quantum of energy $\hbar\omega$ – the minimum energy we can add to or remove from the system. If we were to measure the energy of a classical harmonic oscillator, any positive value would be possible, from zero to, in principle, infinity. We see that the quantum harmonic oscillator is very different: if we measure its energy, we can only obtain one of the discrete values $E_n$. In addition, the lowest energy we can get is not zero but $\frac{1}{2}\hbar\omega$. Classically, zero energy means that the particle in the harmonic potential isn't moving at all. For a quantum harmonic oscillator, the fact that the lowest possible energy is not zero means that we can never have a quantum particle fully at rest. This lowest possible energy is usually called the zero point energy and is one of the foundational features of quantum mechanics. Referring to Figure 5.2 again, we can see that the lowering operator $\hat{a}$ allows us to go from eigenstate $n$ to eigenstate $n-1$, where we have removed one quantum of energy $-\hbar\omega$. Similarly, the raising operator $\hat{a}^\dagger$ allows us to go from eigenstate $n$ to eigenstate $n+1$, where we have added one quantum of energy $+\hbar\omega$.

> **Figure 5.2:** Energy levels in the quantum harmonic oscillator. The plot shows the harmonic potential as a function of the position $x$. The various quantum energy levels are separated by the energy $\hbar\omega$. Application of the raising operator increases energy by one quantum $\hbar\omega$. Application of the lowering operator decreases energy by one quantum $\hbar\omega$.
> *Long description:* A diagram showing an x-axis pointing to the right. An inverted parabolic curve on the line is divided into six sections by six horizontal lines representing the energies of the harmonic oscillator. Starting at the bottom, the first line is labelled $E_0 = \frac{1}{2}\hbar\omega$; the second line is labelled $E_1 = \frac{3}{2}\hbar\omega$; the third line is labelled $E_2 = \frac{5}{2}\hbar\omega$; the fourth line is labelled $E_{n-1} = \hbar\omega[(n-1) + \frac{1}{2}]$; the fifth line is labelled $E_n = \hbar\omega[n + \frac{1}{2}]$; the sixth line is labelled $E_{n+1} = \hbar\omega[(n+1) + \frac{1}{2}]$. Arrows labelled '$\hbar\omega$' represent the energy splitting between the two energy states and are plotted between the first and second, second and third, fourth and fifth, and fifth and sixth horizontal lines. An arrow pointing from the fifth to the fourth horizontal line is labelled $\hat{a}$ with the $|\psi_{n-1}\rangle$. An arrow pointing from the fifth to the sixth horizontal line is labelled $\hat{a}^\dagger$ with the $|\psi_n\rangle$. Above the sixth line is labelled $|\psi_{n+1}\rangle$.

Even though ladder operators $\hat{a}$ and $\hat{a}^\dagger$ are non-Hermitian, and thus cannot be used to measure physical quantities, they are extremely useful because they allow us to manipulate the quantum harmonic oscillator by lowering and raising its energy. On the other hand, the number operator $\hat{N}$ is Hermitian, allowing us to measure the number of energy quanta present in the system.

## 5.5 Energy eigenstates

After we have calculated the energy of a quantum particle in a harmonic oscillator, we will build the corresponding eigenstates. We will do it in two different ways: first, using the creation operator and then, in a more concrete way, using wave functions.

We have seen that the state $|\psi\rangle_{n+1}$ can be built from the state $|\psi\rangle_n$ by adding a quantum of energy $+\hbar\omega$ with raising operator $\hat{a}^\dagger$. Similarly, we can build the state $|\psi\rangle_n$ from the state $|\psi\rangle_{n-1}$ and so on. We can write

$$\hat{a}^\dagger |\psi_{n-1}\rangle = \sqrt{n} |\psi_n\rangle \implies |\psi_n\rangle = \frac{1}{\sqrt{n}} \hat{a}^\dagger |\psi_{n-1}\rangle$$
$$|\psi_{n-1}\rangle = \frac{1}{\sqrt{n-1}} \hat{a}^\dagger |\psi_{n-2}\rangle$$

Substituting $|\psi_{n-1}\rangle$ in the top line by its value in the second line gives

$$|\psi_n\rangle = \frac{1}{\sqrt{n(n-1)}} (\hat{a}^\dagger)^2 |\psi_{n-2}\rangle$$

We can substitute the state $|\psi_{n-2}\rangle$ in terms of the state $|\psi_{n-3}\rangle$, and continue until we reach the ground state $|\psi_0\rangle$

$$|\psi_n\rangle = \frac{1}{\sqrt{n \cdot (n-1) \cdot (n-2) \dots 2 \cdot 1}} (\hat{a}^\dagger)^n |\psi_0\rangle$$

We can simplify the last expression using the factorial $n! = n \cdot (n-1) \cdot (n-2) \dots 2 \cdot 1$

$$|\psi_n\rangle = \frac{1}{\sqrt{n!}} (\hat{a}^\dagger)^n |\psi_0\rangle \tag{5.24}$$

What the last expression is saying is that to generate the eigenstate $|\psi_n\rangle$, which is the eigenstate with $n$ energy quanta above the ground state, we simply need to apply the raising operator $\hat{a}^\dagger$ $n$ times on the ground state. Indeed, every time we apply the raising operator to the eigenstate, we add one energy quantum to our system; applying it $n$ times will add $n$ quanta. If we start from the normalised ground state $|\psi_0\rangle$, the pre-factor $1/\sqrt{n!}$ ensures that the final state $|\psi_n\rangle$ is also normalised.

Now that we have the eigenstate in a somewhat abstract form, using the ground state and raising operator, we will work out its expression in terms of the wave functions. To establish the expression for the ground state, remember that when we act with the lowering operator on the ground state of the system, we get zero, meaning we destroy the state. Using the definition of the lowering operator from Eq. (5.6), we can write this as

$$\hat{a} |\psi_0\rangle = 0 \implies \left( \sqrt{\frac{m\omega}{\hbar}} \hat{x} + \frac{i}{\sqrt{m\hbar\omega}} \hat{p} \right) |\psi_0\rangle = 0 \tag{5.25}$$

where we removed the factor $1/2$ by multiplying both sides of the bottom equation by $2$. The next step is to calculate the action of the operators $\hat{x}$ and $\hat{p}$ on the ground state $|\psi_0\rangle$. Looking at the Eq. (5.25), we obtain

$$\left[ \sqrt{\frac{m\omega}{\hbar}} x + \frac{i}{\sqrt{m\hbar\omega}} \left( -i\hbar \frac{\mathrm{d}}{\mathrm{d}x} \right) \right] \psi_0(x) = 0$$

$$\left( \sqrt{\frac{m\omega}{\hbar}} x + \frac{\mathrm{d}}{\mathrm{d}x} \right) \psi_0(x) = 0 \tag{5.26}$$

where, to obtain a simple expression Eq. (5.26) for the first order differential equation, we multiplied the first line by $\sqrt{m\omega/\hbar}$. To solve Eq. (5.26) we can first rearrange the equation to separate the derivative and $x$, divide both sides by $\psi_0(x)$ and integrate

$$\sqrt{\frac{m\omega}{\hbar}} x \cdot \psi_0(x) + \frac{\mathrm{d}\psi_0(x)}{\mathrm{d}x} = 0$$

$$\frac{1}{\psi_0(x)} \frac{\mathrm{d}\psi_0(x)}{\mathrm{d}x} = -\sqrt{\frac{m\omega}{\hbar}} x$$

$$\int \frac{1}{\psi_0(x)} \frac{\mathrm{d}\psi_0(x)}{\mathrm{d}x} \mathrm{d}x = -\int \sqrt{\frac{m\omega}{\hbar}} x \, \mathrm{d}x$$

$$\ln[\psi_0(x)] = -\frac{m\omega}{2\hbar} x^2 + C$$

where $C$ is an integration constant. Exponentiating the last line, we obtain the expression for the ground state wave function of the quantum harmonic oscillator

$$\psi_0(x) = A e^{-\frac{m\omega x^2}{2\hbar}} \tag{5.27}$$

where $A$ is simply $A = e^C$. The ground state wave function of the quantum harmonic oscillator is thus a Gaussian. To determine the normalisation constant $A$, we write that the probability of finding the particle in the whole space is equal to 1

$$\int_{-\infty}^{+\infty} |\psi_0(x)|^2 \mathrm{d}x = 1$$

$$|A|^2 \int_{-\infty}^{+\infty} e^{-\frac{m\omega x^2}{\hbar}} \mathrm{d}x = 1$$

Using the well-known integral of a Gaussian function

$$\int_{-\infty}^{+\infty} e^{-a x^2} \mathrm{d}x = \sqrt{\frac{\pi}{a}}$$

and realising that, in our case, $a = m\omega/\hbar$, we can write

$$|A|^2 \sqrt{\frac{\pi\hbar}{m\omega}} = 1$$

$$|A|^2 = \sqrt{\frac{m\omega}{\pi\hbar}}$$

$$A = \left( \frac{m\omega}{\pi\hbar} \right)^{1/4}$$

Finally, we can write the full expression for the wave function of the ground state of the quantum harmonic oscillator

$$\psi_0(x) = \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} e^{-\frac{m\omega x^2}{2\hbar}} \tag{5.28}$$

Calculating the wave functions of the higher energy levels is conceptually straightforward. We start by writing the result that we derived earlier, relating the eigenstate $|\psi_n\rangle$ to the ground state $|\psi_0\rangle$ via the raising operator $\hat{a}^\dagger$ and follow the same technique that we carried out earlier for the lowering operator

$$|\psi_n\rangle = \frac{1}{\sqrt{n!}} (\hat{a}^\dagger)^n |\psi_0\rangle$$

$$\implies |\psi_n\rangle = \frac{1}{\sqrt{n!}} \left( \sqrt{\frac{m\omega}{2\hbar}} \hat{x} - \frac{i}{\sqrt{2m\hbar\omega}} \hat{p} \right)^n |\psi_0\rangle$$

$$\implies \psi_n(x) = \frac{1}{\sqrt{n!}} \left[ \sqrt{\frac{m\omega}{2\hbar}} x - \frac{i}{\sqrt{2m\hbar\omega}} \left( -i\hbar \frac{\mathrm{d}}{\mathrm{d}x} \right) \right]^n \psi_0(x)$$

$$\implies \psi_n(x) = \frac{1}{\sqrt{n!}} \left[ \sqrt{\frac{m\omega}{2\hbar}} x - \sqrt{\frac{\hbar}{2m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} \right]^n \psi_0(x)$$

$$\implies \psi_n(x) = \frac{1}{\sqrt{n!}} \left[ \sqrt{\frac{m\omega}{2\hbar}} x - \sqrt{\frac{\hbar}{2m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} \right]^n \left[ \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} e^{-\frac{m\omega x^2}{2\hbar}} \right]$$

Finally, we get the general expression that allows us to calculate any eigenfunction $\psi_n(x)$ that we're interested in for an arbitrary $n$

$$\implies \psi_n(x) = \frac{1}{\sqrt{2^n n!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x - \sqrt{\frac{\hbar}{m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} \right]^n e^{-\frac{m\omega x^2}{2\hbar}} \tag{5.29}$$

As an example, let's consider the first excited state for which $n = 1$

$$\psi_1(x) = \frac{1}{\sqrt{2^1 1!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x - \sqrt{\frac{\hbar}{m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} \right]^1 e^{-\frac{m\omega x^2}{2\hbar}}$$

$$= \frac{1}{\sqrt{2}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x - \sqrt{\frac{\hbar}{m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} \right] e^{-\frac{m\omega x^2}{2\hbar}}$$

$$= \frac{1}{\sqrt{2}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x e^{-\frac{m\omega x^2}{2\hbar}} - \sqrt{\frac{\hbar}{m\omega}} \frac{\mathrm{d}}{\mathrm{d}x} e^{-\frac{m\omega x^2}{2\hbar}} \right]$$

$$= \frac{1}{\sqrt{2}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x e^{-\frac{m\omega x^2}{2\hbar}} - \sqrt{\frac{\hbar}{m\omega}} \left( -\frac{m\omega x}{\hbar} \right) e^{-\frac{m\omega x^2}{2\hbar}} \right]$$

$$= \frac{1}{\sqrt{2}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ \sqrt{\frac{m\omega}{\hbar}} x e^{-\frac{m\omega x^2}{2\hbar}} + \sqrt{\frac{m\omega}{\hbar}} x e^{-\frac{m\omega x^2}{2\hbar}} \right]$$

$$= \frac{1}{\sqrt{2}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \left[ 2 \sqrt{\frac{m\omega}{\hbar}} x e^{-\frac{m\omega x^2}{2\hbar}} \right]$$

Rearranging the expression above, we obtain the result for the first excited state energy eigenfunction

$$\psi_1(x) = \sqrt{\frac{2m\omega}{\hbar}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} x \, e^{-\frac{m\omega x^2}{2\hbar}} \tag{5.30}$$

We can, of course, repeat this exercise to get any excited state $\psi_n(x)$, but, as you can probably imagine, the maths becomes a little tedious. However, what we would have found is that each excited state $\psi_n(x)$ has the general form made of three terms:
- a pre-factor
- a polynomial of order $n$
- a Gaussian

$$\psi_1(x) = \underbrace{\sqrt{\frac{2m\omega}{\hbar}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4}}_{A} \underbrace{x}_{B} \underbrace{e^{-\frac{m\omega x^2}{2\hbar}}}_{C}$$

To avoid diving into tedious mathematics, we'll just give the general result for any excited state $\psi_n(x)$

$$\psi_n(x) = \underbrace{\frac{1}{\sqrt{2^n n!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4}}_{A} \underbrace{H_n \left( \sqrt{\frac{m\omega}{\hbar}} x \right)}_{B} \underbrace{e^{-\frac{m\omega x^2}{2\hbar}}}_{C} \tag{5.31}$$

where $H_n(z)$ is a special kind of polynomial, called a **Hermite polynomial**. The amplitudes of $\psi_n(x)$ and probabilities $|\psi_n(x)|^2$ of the first six eigenstates are plotted in Figure 5.3.

> **Figure 5.3:** Amplitudes (red) and probabilities of finding a particle at position $x$ in a quantum mechanical oscillator (blue) of the first six eigenstates.
> *Long description:* Figure 5.3: Twelve diagrams arranged in a three by four grid:
> - **Row one** shows the first three amplitudes, all in a two-by-two grid: ground wave function, $\psi_0(x)$, starts at the left on the x-axis, going to the top of the y-axis and ending at the right-hand edge of the x-axis; first excited wave function, $\psi_1(x)$, starts at the left on the x-axis, going down to two-thirds of the way along the outside edge of the bottom left hand quadrant, then to one-third of the way along the top right-hand quadrant and ending at the right-hand edge of the central horizontal line; second excited wave function, $\psi_2(x)$, starts at the left on the x-axis, going up to two-thirds of the way along the outside edge of the top left hand quadrant, then down to the bottom of the y-axis, then up to one-third of the way along the top right-hand quadrant and ending at the right-hand edge of the x-axis.
> - **Row two** shows the first three probabilities, all in a rectangle divided into two: Probability density function $|\psi_0(x)|^2$ starts in the bottom left corner, going along two-thirds of the bottom edge before rising to the top of the y-axis, then dropping to the bottom of the right-hand side one-third of the way along the right-hand side and ending in the bottom right-hand corner; Probability density function $|\psi_1(x)|^2$ starts in the bottom left corner, going along two-thirds of the bottom edge before rising almost to the top, to the left of the y-axis, going down to the bottom of the y-axis, returning up to close to the top to the right of the y-axis dropping to the bottom one-third of the way along the right-hand side and ending in the bottom right-hand corner; Probability density function $|\psi_2(x)|^2$ starts in the bottom left corner, going along half of the bottom edge before rising almost to the top, three-quarters of the way across the first half, going down to the bottom close to the y-axis, then rising up to two-thirds of the way up the y-axis before dropping to the bottom of the right-hand side close to the y-axis, rising to close to the top and then dropping to the bottom half way along the right-hand side and ending in the bottom right-hand corner.
> - **Row three** shows the second three amplitudes, all in a two by two grid: $\psi_3(x)$ a wave starts at the left on the central horizontal line, going to the bottom of the left-hand bottom quadrant half way along, then rises to close to the top of the top left-hand quadrant three-quarters of the way along, then drops to a quarter of the way along the bottom right-hand quadrant close to the edge then rises to half way along the top edge of the top right-hand quadrant before ending at the right-hand edge of the central horizontal line; $\psi_4(x)$ a wave starts at the left on the central horizontal line, going to the bottom of the left hand bottom quadrant half way along, then rises to close to the top of the top left-hand quadrant three-quarters of the way along, then drops to close to the vertical central line, to the left and close to the bottom, then rises to a quarter of the way along the bottom right-hand quadrant close to the edge, then rises to close to the vertical central line, to the right and close to the top, then drops to close to the bottom, a quarter of the way along the bottom right-hand quadrant, then rises to the top edge of the top right-hand quadrant before ending at the right-hand edge of the central horizontal line; $\psi_5(x)$ a wave starts at the left on the central horizontal line, going to the top of the left hand top quadrant a third of the way along, then drops to close to the bottom of the bottom left-hand quadrant two thirds of the way along, then rises to close to the central line close to the top, then drops to the central line close to the bottom, then rises close to the central line in the top right-hand quadrant, drops down to close to the bottom edge of the bottom right-hand quadrant, rises up the top edge of the top right-hand quadrant two-thirds of the way along before ending at the right-hand edge of the central horizontal line.
> - **Row four** shows the second three probabilities, all in a rectangle divided into two: $|\psi_3(x)|^2$ a wave starts in the bottom left corner, going along a third of the bottom edge before rising to three quarters of the way up in the left-hand half, half-way along, then drops to two-thirds of the way along the bottom edge, then half-way up, then down to close to the central vertical line, then rises up to half-way up the central vertical line, then down to close to the central line to the bottom edge in the right-hand half, up again to close to the previous peak, then down to the bottom edge, then up to halfway along the top edge, three-quarters of the way up then down to two-thirds of the way along the bottom edge, ending in the bottom right-hand corner; $|\psi_4(x)|^2$ a wave starts in the bottom left corner, going along a third of the bottom edge before rising to close to the top half way along the top edge in the left-hand half, then drops to two-thirds of the way along the bottom edge, then half-way up, then down to the bottom edge, then halfway up close to the central vertical line, then down to the bottom of the central vertical line, then half-way up close to the central vertical line, then down close to the central line to the bottom edge in the right-hand half, up again to close to the previous peak, then down to the bottom edge, then up to halfway along the top edge then down to two-thirds of the way along the bottom edge, ending in the bottom right-hand corner; $|\psi_5(x)|^2$ a wave starts in the bottom left corner, going along one-third of the bottom edge before rising to close to the top edge a third of the way along in the left-hand half, then drops to half of the way along the bottom edge, then two-thirds of the way up, then down to the bottom edge, then two-thirds of the way up, then down to the bottom edge close to the central vertical line, then up to two-thirds of the way up the central vertical line, then down to the bottom edge close to the vertical line, then up two-thirds of the way, then down, then up just over two-thirds of the way then down, then up to the top edge two-thirds of the way along then down close to the bottom right-hand corner, ending in the bottom right-hand corner.

You can notice that the probability density approaches a limit in which the particle is most likely to be found at the extremes of the harmonic potential, that is, closer to its sides. Similarly, it becomes least likely to be found at the centre of the potential. This result is consistent with the classical limit in the sense that the extrema of the potential are the turning points of a classical particle undergoing harmonic motion where it is momentarily at rest so it spends a large fraction of its time there. By contrast, the centre of the potential is where the classical particle is moving the fastest, so it spends a small fraction of its time there.

## Summary

Well done! You have now reached the end of this week's Study – Week 5: Quantum harmonic oscillator.

This week, we studied the important topic of the quantum harmonic oscillator. The harmonic oscillator is a key system both in classical and quantum mechanics. Its importance stems from the fact that many systems can be represented using the formalism of harmonic oscillator. It is also one of the few quantum-mechanical systems for which an exact, analytical solution is known.