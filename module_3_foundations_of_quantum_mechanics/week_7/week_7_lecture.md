# Week 7: Quantum entanglement and composite systems: Study

## Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

This week, we will cover a captivating branch of quantum mechanics that focuses on composite systems and entangled states. These concepts lie at the heart of quantum physics, presenting us with intriguing phenomena and opening up new avenues for technological advancements.

Our journey begins with an exploration of composite systems, where we will study the behaviour of multiple quantum particles when they are combined. We will uncover how these systems can exhibit properties that are distinct from their individual constituents, giving rise to complex and interconnected behaviours. Understanding composite systems is crucial as it forms the basis for comprehending the intricate nature of entanglement.

We will also explore composite observables, which are measurements performed on composite systems. These observables provide valuable insights into the joint behaviour of entangled particles and allow us to extract meaningful information about their entangled states.

Finally, we will explore the practical applications of entanglement in the realm of quantum technologies. Specifically, we will investigate the concept of quantum key distribution (QKD), a revolutionary cryptographic protocol that harnesses the power of entanglement to ensure secure communication. QKD enables the exchange of encryption keys with unparalleled security, as any eavesdropping attempts disrupt the entangled state and can be readily detected.

In this Study you will cover the following topics:
- [7.1 Composite systems](#71-composite-systems)
- [7.2 Entangled states](#72-entangled-states)
- [7.3 Composite observables](#7.3-composite-observables)
- [7.4 Application of entanglement in quantum technologies: Quantum key distribution](#74-application-of-entanglement-in-quantum-technologies:-quantum-key-distribution)

---
## 7.1 Composite systems

In this section we will examine how multiple physical systems combine into one bigger, composite system. Mathematically, composite systems are represented with a *tensor product* whose symbol is $\otimes$. For example, we could combine two systems that we will call $S_\text{A}$ for 'quantum coin' and $S_\text{B}$ for 'quantum die'. Quantum coin has two basis states, heads $H$ and tails $T$. Of course, a classical coin must be in either one state or the other, but a quantum coin can exist in a superposition

$$|\psi_\text{A}\rangle = \alpha_H |H\rangle + \alpha_T |T\rangle .$$

Likewise, a quantum die can be in a state that is a superposition of its six basis states.

$$|\psi_\text{B}\rangle = \alpha_1 |1\rangle + \alpha_2 |2\rangle + \alpha_3 |3\rangle + \alpha_4 |4\rangle + \alpha_5 |5\rangle + \alpha_6 |6\rangle$$

Combining these two systems to form a composite system that we will call $S_\text{AB}$ is done by forming the tensor product of $S_\text{A}$ and $S_\text{B}$

$$S_\text{AB} = S_\text{A} \otimes S_\text{B} .$$

We can define the composite system $S_\text{AB}$ by specifying its basis vectors, as seen in Table 7.1.

**Vectors table**

| | $\vert1\rangle$ | $\vert2\rangle$ | $\vert3\rangle$ | $\vert4\rangle$ | $\vert5\rangle$ | $\vert6\rangle$ |
--- | --- | --- | --- | --- | --- | --- 
| $\vert H\rangle$ | $\vert H1\rangle$ | $\vert H2\rangle$ | $\vert H3\rangle$ | $\vert H4\rangle$ | $\vert H5\rangle$ | $\vert H6\rangle$ |
| $\vert T\rangle$ | $\vert T1\rangle$ | $\vert T2\rangle$ | $\vert T3\rangle$ | $\vert T4\rangle$ | $\vert T5\rangle$ | $\vert T6\rangle$ |

> **Table 7.1:** the basis states of the composite system $S_\text{AB}$. A composite system is made using a tensor product of the two subsystems. In this example, a two-dimensional 'quantum coin' and a six-dimensional 'quantum die' make a composite system of dimension 12 ($2 \times 6$). Each combined state-label shows the state of each of the two subsystems.

Notice that even though the state-labels of $S_\text{AB}$ are doubly indexed, ket-vectors like $|H4\rangle$ represent a single state of the combined system. The composite system $S_\text{AB}$, like any other quantum system, can be in a state that is a superposition of its basis states

$$|\psi_\text{AB}\rangle = \alpha_{H1} |H1\rangle + \dots + \alpha_{H6} |H6\rangle + \alpha_{T1} |T1\rangle + \dots + \alpha_{T6} |T6\rangle .$$

We can easily extend those rules to more complicated systems. For example, a composite system $S_\text{ABC}$ made of three systems of dimensions $N_\text{A}$, $N_\text{B}$ and $N_\text{C}$ would be $S_\text{ABC} = S_\text{A} \otimes S_\text{B} \otimes S_\text{C}$ and would have $N_\text{ABC} = N_\text{A} \times N_\text{B} \times N_\text{C}$ basis vectors.

To define more general notations than those of quantum coin and die, we can use an example of expansion of a state from each system into its basis vectors

$$|\psi_\text{A}\rangle = \sum_a \alpha(a) |a\rangle$$

$$|\psi_\text{B}\rangle = \sum_b \alpha(b) |b\rangle$$

$$|\psi_\text{AB}\rangle = \sum_{a,b} \alpha(a, b) |ab\rangle .$$

It is common to define orthonormal basis vectors:

$$\langle a | a' \rangle = \delta_{a,a'}$$

$$\langle b | b' \rangle = \delta_{b,b'}$$

$$\langle ab | a'b' \rangle = \delta_{a,a'} \delta_{b,b'} .$$

The last line deals with the basis vectors of the composite systems. The right side is zero unless $a = a'$ and $b = b'$. If the labels do match, the inner product is one.

Now that we eased our minds into composite systems using coins and dice, let's scrutinise how systems of spins behave when combined together into larger systems. Consider two quantum physicists, Alice and Bob, each having their own Stern-Gerlach apparatus, called $A$ and $B$ respectively, that they can use to prepare states and measure spin components. Each can be independently oriented along any axis. Let's define the names for those spins and call the full sets of components for Alice's and Bob's spins, respectively,

- Alice: $\sigma_x, \sigma_y, \sigma_z$
- Bob: $\tau_x, \tau_y, \tau_z$.

Following the precepts of building composite systems, the space of states for the two-spin system is a tensor product between Alice's and Bob's systems. We can choose any axis to specify the state of spins, but, to fix things, let's look at their $z$ components. Previously, we decided to label the spins with $+$ and $-$ symbols ($S_z = +$ and $S_z = -$); however, there are many other ways to indicate the two possible values of a spin. We could call it 'up' and 'down' or use the arrows $\uparrow$ and $\downarrow$. Using the latter, the four basis vectors of the composite state are

$$|\uparrow\uparrow\rangle, |\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle, |\downarrow\downarrow\rangle , \tag{7.1}$$

where the first part of each label represents the state of Alice's spin $\sigma$, and the second part represents Bob's spin $\tau$.

The simplest type of state for the composite system is called a *product state*. A product state is the result of completely independent preparations by Alice and Bob, in which each uses his or her own apparatus to prepare a spin. Using explicit notation, suppose Alice and Bob prepare their spin in states:

- Alice: $|\psi_\text{A}\rangle = \alpha_\uparrow |\uparrow\rangle + \alpha_\downarrow |\downarrow\rangle$
- Bob: $|\psi_\text{B}\rangle = \beta_\uparrow |\uparrow\rangle + \beta_\downarrow |\downarrow\rangle .$

We assume that each state is normalised:

$$\alpha_\uparrow^* \alpha_\uparrow + \alpha_\downarrow^* \alpha_\downarrow = 1$$

$$\beta_\uparrow^* \beta_\uparrow + \beta_\downarrow^* \beta_\downarrow = 1. \tag{7.2}$$

The product state $|\psi_\text{PS}\rangle$ describing the combined system is

$$\begin{aligned}
|\psi_\text{PS}\rangle &= [\alpha_\uparrow |\uparrow\rangle + \alpha_\downarrow |\downarrow\rangle] \otimes [\beta_\uparrow |\uparrow\rangle + \beta_\downarrow |\downarrow\rangle] \\
&= \alpha_\uparrow \beta_\uparrow |\uparrow\uparrow\rangle + \alpha_\uparrow \beta_\downarrow |\uparrow\downarrow\rangle + \alpha_\downarrow \beta_\uparrow |\downarrow\uparrow\rangle + \alpha_\downarrow \beta_\downarrow |\downarrow\downarrow\rangle .
\end{aligned} \tag{7.3}$$

The main feature of a product state is that each subsystem behaves independently of the other. If Bob or Alice does an experiment on their own subsystem, the result is exactly the same as it would be if the other’s subsystem did not exist. In other words, product states (sometimes called separable states) are quantum states belonging to a composite space that can be factored into individual states belonging to separate subspaces. Conversely, a state is said to be *entangled* if it is not separable.

## 7.2 Entangled states

Admittedly, a product state is a peculiar state in the sense that we can factor it (or separate it) into two individual states, each having an independent existence in its own subspace (Alice's or Bob's). It is, though, one state among many other possible composite states subtended by the tensor product between Alice's and Bob's subspaces. To write the most general vector in the composite space of states, we can decompose it on its four basis vectors $|\uparrow\uparrow\rangle$, $|\uparrow\downarrow\rangle$, $|\downarrow\uparrow\rangle$ and $|\downarrow\downarrow\rangle$ and write

$$|\psi\rangle = \phi_{\uparrow\uparrow} |\uparrow\uparrow\rangle + \phi_{\uparrow\downarrow} |\uparrow\downarrow\rangle + \phi_{\downarrow\uparrow} |\downarrow\uparrow\rangle + \phi_{\downarrow\downarrow} |\downarrow\downarrow\rangle . \tag{7.4}$$

Here, we used subscripted symbols $\phi$ to write the amplitude of each base state in the most general way. The product state would be obtained if we gave very specific values to those amplitude coefficients $\phi$, namely:

$$\begin{aligned}
\phi_{\uparrow\uparrow} &= \alpha_\uparrow \beta_\uparrow \\
\phi_{\uparrow\downarrow} &= \alpha_\uparrow \beta_\downarrow \\
\phi_{\downarrow\uparrow} &= \alpha_\downarrow \beta_\uparrow \\
\phi_{\downarrow\downarrow} &= \alpha_\downarrow \beta_\downarrow ,
\end{aligned}$$

which would make the same product state as in Eq. (7.3). However, there is no reason for a truly general state to have those specific values of $\phi$. The only relation that coefficients $\phi$ must obey is that of the normalisation

$$\phi_{\uparrow\uparrow}^* \phi_{\uparrow\uparrow} + \phi_{\uparrow\downarrow}^* \phi_{\uparrow\downarrow} + \phi_{\downarrow\uparrow}^* \phi_{\downarrow\uparrow} + \phi_{\downarrow\downarrow}^* \phi_{\downarrow\downarrow} = 1. \tag{7.5}$$

Notice that a product state has two normalisation conditions, as per Eq. (7.2), while the most general composite state has only one. It can be shown that we need four independent parameters to write product states (two parameters to describe the state of a single spin, so four to describe two independent spins). According to Susskind (2014, Section 6.6) each factor requires two complex numbers ($\alpha_\uparrow$ and $\alpha_\downarrow$ for Alice, $\beta_\uparrow$ and $\beta_\downarrow$ for Bob), which means we need four complex numbers altogether. That's equivalent to eight real parameters. But recall that the normalisation conditions in Eq. (7.2) reduce this by two. Furthermore, the overall phases of each state have no physical significance, so the total number of real parameters is four.

On the other hand, the most general state for a two-spin system has six real parameters. Again with reference to Susskind (2014, Section 6.6), we have four complex numbers, but this time we only have one normalisation condition, and only one overall phase to ignore. Those extra two parameters make the general states richer than just those product states − from that richness comes a new concept called *entanglement*.

As an example, consider the so called *singlet* and *triplet* states that cannot be written as product states:

$$\begin{aligned}
\text{Singlet:} \quad & |\psi_\text{S}\rangle = \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \\
\text{Triplet:} \quad & |\psi_{\text{T}1}\rangle = \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \\
& |\psi_{\text{T}2}\rangle = \frac{1}{\sqrt{2}} (|\uparrow\uparrow\rangle + |\downarrow\downarrow\rangle) \\
& |\psi_{\text{T}3}\rangle = \frac{1}{\sqrt{2}} (|\uparrow\uparrow\rangle - |\downarrow\downarrow\rangle) .
\end{aligned} \tag{7.6}$$

Indeed, it is impossible to find the values of $\alpha_\uparrow$, $\alpha_\downarrow$, $\beta_\uparrow$ and $\beta_\downarrow$ that would allow us to factorise those states.

### Spin operators
Recall that the Pauli matrices

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

are the spin operators that act on the states of a single spin. Now let's consider how the operators should be defined when acting on the tensor product states, $|\uparrow\uparrow\rangle$, $|\uparrow\downarrow\rangle$, $|\downarrow\uparrow\rangle$ and $|\downarrow\downarrow\rangle$. The answer is that Alice's operator $\sigma$ acts only on the Alice half of the composite system − the Bob half of the spin state does not change. Similarly, Bob's operator $\tau$ acts only on the Bob half of the composite system, while the Alice half remains passive. Mathematical pedantry dictates us to use the identity operator $1$ in half-space that is unchanged, thus the tensor product versions of our operators are

$$\begin{aligned}
\text{Alice:} \quad & \sigma_z \otimes 1 \\
\text{Bob:} \quad & 1 \otimes \tau_z .
\end{aligned}$$

However, to avoid unnecessary cluttering when dealing with composite systems, we will ignore the identity operator and tensor product, writing only $\sigma_z$ when we really mean $\sigma_z \otimes 1$. As an example, let's calculate the action of $\sigma$ on the kets $|\uparrow\rangle$ and $|\downarrow\rangle$

$$\begin{aligned}
\sigma_z |\uparrow\rangle &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |\uparrow\rangle \\
\sigma_z |\downarrow\rangle &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} = -\begin{pmatrix} 0 \\ 1 \end{pmatrix} = -|\downarrow\rangle \\
\sigma_x |\uparrow\rangle &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\downarrow\rangle \\
\sigma_x |\downarrow\rangle &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |\uparrow\rangle \\
\sigma_y |\uparrow\rangle &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ i \end{pmatrix} = i |\downarrow\rangle \\
\sigma_y |\downarrow\rangle &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -i \\ 0 \end{pmatrix} = -i |\uparrow\rangle .
\end{aligned}$$

As Bob's set-up is identical to Alice's, we obtain the same set of equations with $\tau$. To determine what happens when $\sigma$ or $\tau$ act on the tensor product states $|\uparrow\uparrow\rangle$, $|\uparrow\downarrow\rangle$, $|\downarrow\uparrow\rangle$ and $|\downarrow\downarrow\rangle$, remember that when $\sigma$ acts, it just ignores Bob's half of the state label, and similarly, when $\tau$ acts, it ignores Alice's half of the state label. As an example, let's calculate explicitly the action of operators on a few basis states.

$$\begin{aligned}
\sigma_z |\uparrow\uparrow\rangle &= |\uparrow\uparrow\rangle \\
\sigma_z |\downarrow\uparrow\rangle &= -|\downarrow\uparrow\rangle \\
\sigma_y |\uparrow\uparrow\rangle &= i |\downarrow\uparrow\rangle \\
\tau_z |\uparrow\uparrow\rangle &= |\uparrow\uparrow\rangle \\
\tau_x |\uparrow\downarrow\rangle &= |\uparrow\uparrow\rangle \\
\tau_y |\downarrow\downarrow\rangle &= -i |\downarrow\uparrow\rangle
\end{aligned} \tag{7.7}$$

For emphasis, we coloured in red and blue the action and results occurring in, respectively, Alice's and Bob's half-space, and left in black the parts that remain unchanged.

Let's now study more closely one of the entangled states, for example, let's evaluate the expectation values of $\sigma$ in the singlet state from Eq. (7.6)

$$|\psi_\text{S}\rangle = \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) .$$

We know that the expectation value, $\langle\sigma_z\rangle$, of $\sigma_z$ in that state will be given by

$$\begin{aligned}
\langle\sigma_z\rangle &= \langle\psi_\text{S}| \sigma_z |\psi_\text{S}\rangle \\
&= \left\langle \frac{1}{\sqrt{2}} (\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) \right| \sigma_z \left| \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \right\rangle \\
&= \frac{1}{2} \left\langle (\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) \right| \sigma_z \left| (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \right\rangle \\
&= \frac{1}{2} \langle (\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) (\sigma_z |\uparrow\downarrow\rangle - \sigma_z |\downarrow\uparrow\rangle) \rangle \\
&= \frac{1}{2} \langle (\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) (|\uparrow\downarrow\rangle - (-|\downarrow\uparrow\rangle)) \rangle \\
&= \frac{1}{2} \langle (\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) (|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \rangle \\
&= \frac{1}{2} (\langle\uparrow\downarrow|\uparrow\downarrow\rangle + \langle\uparrow\downarrow|\downarrow\uparrow\rangle - \langle\downarrow\uparrow|\uparrow\downarrow\rangle - \langle\downarrow\uparrow|\downarrow\uparrow\rangle) \\
&= \frac{1}{2} (1 + 0 - 0 - 1) \\
&= 0 ,
\end{aligned}$$

where we used the fact that the four basis states of the composite space are orthonormal. We can evaluate the expectation values of other components of the spins $\sigma$ and $\tau$ and find

$$\begin{aligned}
\langle\sigma_x\rangle = \langle\sigma_y\rangle = \langle\sigma_z\rangle &= 0 \\
\langle\tau_x\rangle = \langle\tau_y\rangle = \langle\tau_z\rangle &= 0.
\end{aligned}$$

If the expectation value of a component of $\sigma$ is zero, it means that the experimental outcome is equally likely to be, for example, $+1$ or $-1$. Even though we know the singlet state $\psi_\text{S}$ perfectly well, we cannot say anything about the outcome of the measurement of any component of spins $\sigma$ and $\tau$. According to the rules of quantum mechanics, there is nothing to know beyond what is encoded in the state-vector − in the present case, $\psi_\text{S}$. The state-vector is as complete a description of a system as it is possible to make. So it seems that, in quantum mechanics, we can know everything about a composite system and still know nothing about its constituent parts. This is the true weirdness of entanglement, which so disturbed Einstein.

## 7.3 Composite observables

We have seen that there are observables that can be measured separately by Alice and Bob, each using their own detector. However, there are also observables that can only be measured using two detectors. The outcome of such measurement can only be known if Alice and Bob share their results.

As the operators $\sigma$ and $\tau$ form a tensor product, they act on separate parts of the combined system and, thus, they commute with each other. That means that we can measure $\sigma$ and $\tau$ in any order, but also that we can measure corresponding observables simultaneously. This is by no means a general property of observables, and there are many non-commuting observables, implying that the order of measurement matters, and that they cannot be measured simultaneously. For example, position and momentum are two observables that do not commute; we cannot know the position and momentum of a particle. Energy and time form another pair of non-commuting observables.

We can make a new *composite observable*, $\tau_z \sigma_z$, by simply multiplying Alice's and Bob's individual operators. To see how those work, let's apply it to the singlet state from Eq. (7.6). The effect of those observables on kets is given in Equation (7.7). We will first apply $\sigma_z$, then $\tau_z$.

$$\begin{aligned}
\tau_z \sigma_z |\psi_S\rangle &= \tau_z \sigma_z \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \\
&= \tau_z \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \\
&= \frac{1}{\sqrt{2}} (-|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \\
&= -|\psi_S\rangle .
\end{aligned}$$

Notice that $|\psi_S\rangle$ is an eigenvector of the observable $\tau_z \sigma_z$ with eigenvalue $-1$, as we have

$$\tau_z \sigma_z |\psi_S\rangle = -|\psi_S\rangle .$$

The meaning of this result is that when Alice and Bob compare their results, they will find that they always measured opposite values. When Alice measures $+1$, Bob will measure $-1$; and when Alice measures $-1$, Bob will measure $+1$. The product of the two measurements will always be $-1$. We should not be surprised by this result. The state vector $|\psi_S\rangle$ is a superposition of two vectors, $|\uparrow\downarrow\rangle$ and $|\downarrow\uparrow\rangle$, both of which comprise two spins with opposite $z$ components.

Something more surprising happens if we make Alice and Bob measure the $x$-components of their spins, $\sigma_x$ and $\tau_x$. Applying the composite observable $\tau_x \sigma_x$ to the same singlet state $|\psi_S\rangle$, we find

$$\begin{aligned}
\tau_x \sigma_x |\psi_S\rangle &= \tau_x \sigma_x \frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \\
&= \tau_x \frac{1}{\sqrt{2}} (|\downarrow\downarrow\rangle - |\uparrow\uparrow\rangle) \\
&= \frac{1}{\sqrt{2}} (|\downarrow\uparrow\rangle - |\uparrow\downarrow\rangle) \\
&= -|\psi_S\rangle .
\end{aligned}$$

Again, we have that $|\psi_S\rangle$ is an eigenvector of $\tau_x \sigma_x$ with eigenvalue $-1$.

$$\tau_x \sigma_x |\psi_S\rangle = -|\psi_S\rangle .$$

Recall that our arrow notation $\uparrow$ and $\downarrow$ relates to the $z$-component of the spin. Looking at the $|\psi_S\rangle$, defined with $z$-component projections of the spin, there is no straightforward way to see how $x$-component observables should behave. Yet, the correlation between results that Alice and Bob measure is still there. Once again, when Alice measures $\sigma_x$ to be $+1$, Bob will measure $\tau_x$ to be $-1$; and when Alice measures $-1$, Bob will measure $+1$.

## 7.4 Application of entanglement in quantum technologies: Quantum key distribution

One practical aspect of the particle entanglement is in the field of quantum cryptography. Nowadays, the security of a cryptogram is not dependent on the secrecy of the encryption and decryption process, but rather on the secrecy of the key. The key must contain a randomly chosen and sufficiently long string of bits in order to guarantee that it would take a very long time to unlock the cryptogram without the key. Even with the most powerful modern computers, brute-force cracking a 128-bit key would take a time comparable to the age of the universe. For all practical purposes, the message encrypted in this way is inviolable. The difficulty resides in safely passing the secret key between the sender (Alice) and receiver (Bob). There is always a possibility that an eavesdropper (Eve) will spy on the communication channels between Alice and Bob, obtain the secret key and decipher Alice's message to Bob.

Luckily, the fundamental laws of quantum physics allow for secure distribution of the secret key. The *no-cloning theorem*, whose proof was published by Bill Wootters, Wojciech Zurek [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-7-quantum-entanglement-and-composite-systems-study#sect5) and Dennis Dieks [[2]](https://canvas.sussex.ac.uk/courses/41954/pages/week-7-quantum-entanglement-and-composite-systems-study#sect6), states that it is impossible to create an independent and identical copy of an arbitrary unknown quantum state. The no-cloning theorem is a vital ingredient in quantum cryptography, as it forbids eavesdroppers from creating copies of a transmitted quantum cryptographic key. Therefore, any attempt to eavesdrop will result in disturbance that can be detected by Alice and Bob, allowing them to stop the communication over the insecure channel. Fundamentally, the no-cloning theorem protects the uncertainty principle in quantum mechanics. According to the Quantiki information portal, 'If one could clone an unknown state, then one could make as many copies of it as one wished, and measure each dynamical variable with arbitrary precision, thereby bypassing the uncertainty principle. This is prevented by the non-cloning theorem' [[3]](https://canvas.sussex.ac.uk/courses/41954/pages/week-7-quantum-entanglement-and-composite-systems-study#sect7).

In 1992, Artur Ekert proposed a method to distribute a key securely based on polarisation-entangled pairs of photons to simultaneously generate, at two distant places, two identical sequences of $0$ and $1$ that will act as a deciphering key. In the previous section we dealt with entangled spins and called the possible outcomes 'up' and 'down'. Now, we will entangle the photons and call two possible outcomes $+1$ and $-1$. Despite different labels and systems − photons instead of spins − all concepts and formalism that we learned with spins will apply to photons. So, how can Alice and Bob obtain identical random series of $0$ and $1$?

A source of entangled photons sends two entangled photons: one photon toward Alice, another toward Bob, as shown in Figure 7.1. Both Alice and Bob have an apparatus, a polariser, that can measure the polarisation of photons, $+1$ or $-1$. At each polariser, the results $+1$ and $-1$ are happening randomly and with equal probabilities. But if the polarisers are aligned along the same direction, there is a total correlation between the random results on both sides. They are either both $+1$ or both $-1$, and the crossed cases ($+1$, $-1$ or $-1$, $+1$) never happen. So, the process itself, in its very fundamental nature, produces two identical random sequences on each side. These can be used as two identical encoding/decoding cases, generated at each side. We can replace the $-1$ outcome of the polariser by $0$, to respect the usual convention in cryptography and write the information as a stream of $1$ and $0$ (rather than $+1$ and $-1$). Of course, this is just a notation convention that doesn't change anything at the fundamental level − we are still working with bits that encode information, whether we call them $+1$/$-1$, up/down, or $+$/$-$.

to respect the usual convention in cryptography and write the information as a stream of $1$ and $0$ (rather than $+1$ and $-1$). Of course, this is just a notation convention that doesn't change anything at the fundamental level — we are still working with bits that encode information, whether we call them $+1/ - 1$, up/down, or $+/-$.

> **Figure 7.1:** Diagram of the Ekert protocol for quantum key distribution. Apdapted from Aspect, A. Closing the Door on Einstein and Bohr's Quantum Debate. Physics 8, p. 123 (2015). DOI:10.1103/Physics.8.123
>
> **Long description:**
> Figure 7.1: Above the image is the Equation 
> $$|\varphi(\nu_1, \nu_2)\rangle = \frac{1}{\sqrt{2}} \{ |x, x\rangle + |y, y\rangle \} .$$
> 
> At the centre of the figure a circle labelled ‘Source’ emits a pair of entangled photons ($\nu$ which shows the Greek letter as it appears in the Figure), $\nu_1$ and $\nu_2$ and sends them in opposite directions: photon $\nu_1$ to the left, toward the polariser A (red block A, aligned along the direction $a$), and photon $\nu_2$ to the right, toward the polariser B (red block B, aligned along the direction $b$). Each polarizer has two output channels, labelled $+1$ and $-1$. A photon $\nu_1$ polarised parallel to $a$ will emerge in the direction labelled $+1$ and will strike the top detector behind the polariser A. A photon $\nu_1$ polarised perpendicular to $a$ will emerge in the direction labelled $-1$ at A and strike the bottom detector behind the polariser A. Similarly, a photon $\nu_2$ polarised parallel to $b$ will emerge in direction labelled $+1$ and will strike the top detector behind the polariser B. A photon $\nu_2$ polarized perpendicular to $b$ will emerge in the direction labelled $-1$ at B and strike the bottom detector behind the polariser B. The signals from all four detectors go to the green box labelled ‘Coincidences detector’.

A remarkable feature of the Ekert protocol is that the eavesdropper, Eve, cannot intercept enough information to get her own copy of the key. The reason is that according to the wave function collapse postulate, the value of each bit of the key is decided only at the last moment, when the measurements are performed on the photons. Indeed, a quantum system made of two entangled photons is described by a wave function that evolves according to the Schrödinger equation [4]. The joint wave function of two entangled objects only contains information about the correlation between those objects, not about their specific values. They only gain specific values when the observed wave function collapses. So, between the source and the polarisers, the key does not exist yet. There is nothing to spy on.

Cryptographers must consider any possibility for a smart eavesdropper to get what they want to hide. Here might be a possibility: let us suppose that the eavesdropper knows a priori what the direction $b$ of the polariser of Bob is. Eve can then insert, between the source and Bob, a polariser oriented along the direction $b$, and observe the results, $+1$ or $-1$, she finds. She then sends a photon polarised along $b$ or perpendicular to $b$ depending on the result. In this scenario, Eve plays the role of the first measurement that makes a wave function of the entangled state collapse, and both Alice and Bob will find the same result as Eve. As a result, the eavesdropper has a third copy of the key.

To beat such a smart and well-equipped eavesdropper, it is possible to use a basic quantum property of single photons: it is not possible to determine the polarisation of a photon, unless one knows a priori along which set of orthogonal axes it is expected to be polarised. To beat the eavesdropper, Alice and Bob will then choose randomly their polarisers' orientations, along directions making relative angles with values $(a, b) \in \{0, \pi/8, 2\pi/8, 3\pi/8\}$, or other orientations. Now, when the sequence is finished, Alice and Bob can communicate on a public channel to know the cases when the angles were $0$, and when they were $\pi/8$ or $3\pi/8$. The first series of data, corresponding to an angle $0$ between the polarisers, allows Alice and Bob to obtain the two identical keys. The second series of data allows them to check that the correlations they find are the ones expected for the entangled pairs, at known angles of the polarisers. If there is an eavesdropper making a measurement along another direction than the one of Bob, the correlations will be different from the ones expected for the entangled pairs. In that case, Alice and Bob know that there is a spy on the line, and they will refrain from using the key.

But what exactly happens if an eavesdropper makes a measurement before Alice and Bob? Then it creates a key, but by doing so, she makes the quantum state become a product state where each photon is in a well-defined polarisation. You may ask why choose specific angles, $\pi/8$ or $3\pi/8$? It is not a bad idea to try these angles, but if it does not work, you can try other angles. In principle, it is enough to find one set, $a, a', b, b'$, of orientations where the measured correlations correspond to the entangled state, to be sure that no spy has a copy of the key.

## Summary

Well done! You have now reached the end of this week’s Study – Week 7: Quantum entanglement and composite systems.

This week, we will covered a captivating branch of quantum mechanics that focuses on composite systems and entangled states. These concepts lie at the heart of quantum physics, presenting us with intriguing phenomena and opening up new avenues for technological advancements.

## References
*(Note: The specific reference list items are cut off at the bottom of the provided view, but correspond to the citations [1] Wootters & Zurek, [2] Dieks, and [3] Quantiki from Section 7.4).*