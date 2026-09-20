# Week 6: Stern-Gerlach experiment: Study

## Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

This week, we will cover the intriguing Stern-Gerlach experiment. This experiment is pivotal in the history of quantum mechanics and provides profound insights into the nature of particles and their intrinsic properties.

The Stern-Gerlach experiment, conducted by Otto Stern and Walther Gerlach in 1922, revolutionised our understanding of quantum physics. It involves passing a beam of particles, typically silver atoms or electrons, through an inhomogeneous magnetic field. What makes this experiment truly remarkable is its ability to demonstrate the discrete and quantised nature of certain properties of particles.

The significance of the Stern-Gerlach experiment lies in its direct confirmation of the existence of intrinsic angular momentum and the quantisation of spin. This groundbreaking discovery shattered the classical notion of continuous properties and laid the foundation for the development of quantum mechanics.

Furthermore, the Stern-Gerlach experiment serves as a fundamental building block for understanding more complex quantum phenomena. It has profound implications in various areas of quantum physics, including the study of electron spin, the behaviour of atoms and subatomic particles, quantum entanglement and the development of quantum information technologies.

By exploring the Stern-Gerlach experiment, we will gain a deeper appreciation for the nature of quantum physics.

In this Study you will cover the following topics:
- [6.1 Stern-Gerlach experiment](#61-stern-gerlach-experiment)
- [6.2 Repeated measurements of the same type](#62-repeated-measurements-of-the-same-type)
- [6.3 Repeated measurements of the different types](#63-repeated-measurements-of-the-different-types)
- [6.4 Quantum interference](#64-quantum-interference)

---

## 6.1 Stern-Gerlach experiment

Particles have various properties, such as position, mass, charge, etc. The *spin* is another property, whose concept comes from the field of particle physics. Naively, the spin can be pictured as a vector that points in some direction, but that classical picture is misleading and cannot represent accurately the real situation. The spin of an electron is a pure quantum mechanical concept, and any attempt to understand it using classical imagery will deceive you sooner or later.

The existence of spin was confirmed experimentally by Stern and Gerlach in 1922 [[1]](#references) using silver ($\text{Ag}$) atoms. Silver has 47 electrons; 46 of them form a spherically symmetric charge distribution, and the 47th electron occupies a $5s$ orbital. For practical purposes relevant to the Stern-Gerlach experiment, such internal configuration of electrons makes a silver atom behave like a heavy electron. In the standard Stern-Gerlach experiment, as illustrated in Figure 6.1, particles are fired through a gap between the poles of two magnets, which are arranged to provide an inhomogeneous magnetic field $\mathbf{B} = B(z) \hat{\mathbf{e}}_z$, thus creating a net force on a particle with magnetic dipole $\boldsymbol{\mu}$:

$$F = \boldsymbol{\mu} \cdot \frac{d\mathbf{B}}{dz} = \langle \mu_z \rangle \frac{dB_z}{dz}$$

where $\langle \mu_z \rangle$ is the average of the $z$-component of the magnetic dipole. The amount of deflection depends on the relative orientation between the magnetic momentum and the magnetic field. If $\boldsymbol{\mu}$ and $\mathbf{B}$ are perpendicular, the force on the particle is zero and there will be no deflection. Conversely, if $\boldsymbol{\mu}$ and $\mathbf{B}$ are aligned (or anti-aligned), the deflection will be maximal. We would expect classically to see on the screen a continuous band that is symmetric about the undeflected direction, $z = 0$, corresponding to all possible orientation between $\boldsymbol{\mu}$ and $\mathbf{B}$. Instead, it splits into two distinct components, as shown in Figure 6.2. Such an observation would be consistent with particles whose $\mu$ can take only two discrete values.

> **Figure 6.1: Stern-Gerlach experiment.**
> 
> *Long Description:*
> A diagram showing a box on the left side of the figure which is labelled 'Oven (source of atoms)' from where an atomic beam emerges moving to the right. The atomic beam passes through an inhomogeneous magnetic field produced by two magnets, one on top of the other, labelled 'N (North)' at the top and 'S (South)' at the bottom. The atomic beam is split into two beams, one deviates upwards and hits the screen positioned on the right-hand side at the top half, while the second atomic beam is deviated toward the bottom and hits the same screen at the bottom half. The screen shows two spots, one at the top, and another at the bottom of the screen, representing the locations where atomic beams hit it.

Despite the fact that the Stern-Gerlach experiment measures magnetic dipole moment, it is conventional to regard it as a measurement of a component of the particle's spin angular momentum. This follows since the spin angular momentum of the particle, $\mathbf{S}$, is related to the magnetic dipole moment via

$$\boldsymbol{\mu} = \frac{g q}{2 m} \mathbf{S}$$

where $q$ is the charge of the particle, $m$ its mass and $g$ the so-called $g$-factor for the particle.

> **Figure 6.2: Stern-Gerlach experiment. Classical expectations vs quantum observations.**
> 
> *Long Description:*
> A diagram containing two sub-figures, one at the top, representing what classical physics predicts about the Stern-Gerlach experiment labelled 'Classical prediction', and one at the bottom, representing the observations that demonstrate the quantum behaviour of the system labelled 'Observation'. In both figures, a beam emerges from a box which is labelled 'Oven (source of atoms)' and contains a number of small arrows pointing in all directions. The beam moves to the right and passes through the region of the inhomogeneous magnetic field produced by two magnets one on top of the other. The top magnet is labelled 'N (North)', and the bottom one is labelled 'S (South)'. In the top sub-figure, the atomic beam emerges from the region of an inhomogeneous magnetic field deviating at different angles, creating a continuous spot on the screen which is represented by an ellipse elongated in the vertical direction. The screen also contains a set of blue arrows radiating outwards from the right-hand convex side of the spot representing the electron magnetic dipole moment. Those arrows make different angles with respect to the vertical direction of the screen. The top arrow is directed upwards, the bottom downwards, and the middle one horizontally to the right. In the bottom sub-figure, the atomic beam is split into only two beams that hit the screen at two spots. Next to the top spot is a blue arrow representing the electron magnetic dipole moment, which is oriented upwards. Next to the bottom spot is a different blue arrow representing the electron magnetic dipole moment, which is oriented downwards.

As illustrated in Figure 6.2, in the standard Stern-Gerlach experiment, there is no control over the spins of the particles prior to their entry into the region between the two magnetic poles; the best assumption is that the spins are randomly oriented, although the total magnitude of the spin is the same for each particle. It is typical to consider this entire experiment as nothing other than a measurement of the orientation of the spin of particles with respect to the orientation of the magnetic field (north-south). Formalism of quantum mechanics tells us that such measurement can be represented by an operator that we will label either $\hat{S}_x$ or $\hat{S}_z$, depending on the orientation of the measuring instrument.

To understand the Stern-Gerlach experiment in its full quantum picture, we need to probe the nature a little harder. We will consider what happens when we add more Stern-Gerlach instruments and vary the relative orientation between them. In the following sections we are going to consider all sorts of combinations and orientations, so it is prudent to first define some notations and labels to keep things straight.

As illustrated in Figure 6.3, the unit Stern-Gerlach element will be represented by a box, labelled $\hat{S}_x$ or $\hat{S}_z$, where indices $x$ and $z$ refer to the direction of the magnetic field. From that box emerge two particle trajectories that we will label $S_x = +$ and $S_x = -$, for the case of magnetic field along the *x*-axis. Similarly, if the magnetic field is along the *z*-axis, we will denote the two trajectories $S_z = +$ and $S_z = -$. With these notations now in mind, we can start experimenting with multiple Stern-Gerlach apparatuses.

> **Figure 6.3: Symbolic representation of Stern-Gerlach devices.**
> 
> A single Stern-Gerlach apparatus consists of a magnet producing an inhomogeneous magnetic field whose gradient is in the $n$-direction. In this topic, we will consider the particles that travel along the $y$-axis, while the magnetic fields will be aligned either along the $x$-axis ($\hat{S}_x$) or the $z$-axis ($\hat{S}_z$).
> 
> *Long Description:*
> A diagram with three parts:
> - A box labelled '$\hat{S}_n$' with two lines coming from it to the right. At the end of the first is $S_n = +$. At the end of the second is $S_n = -$.
> - A box labelled '$\hat{S}_x$' with two lines coming from it to the right. At the end of the first is $S_x = +$. At the end of the second is $S_x = -$. To the left, a circle with a cross in it has an arrow pointing up coming from it labelled '$x$' and an arrow pointing to the right coming from it labelled '$y$'.
> - A box labelled '$\hat{S}_z$' with two lines coming from it to the right. At the end of the first is $S_z = +$. At the end of the second is $S_z = -$. To the left, a circle with a cross in it has an arrow pointing up coming from it labelled '$z$' and an arrow pointing to the right coming from it labelled '$x$'.

## 6.2 Repeated measurements of the same type

One can imagine a sequence of Stern-Gerlach experiments performed on the same particle. The particle is fired into one Stern-Gerlach apparatus, emerges in one of the two trajectories, and is then directed through another Stern-Gerlach apparatus. In such sequences, it is possible to ask about the outcomes of later measurements given a knowledge of outcomes of earlier measurements in the sequence.

An example of the combination of three apparatuses is shown in Figure 6.4. We can make the notation even shorter by writing that the particle, described by the wave function $|\psi\rangle$, after passing through three Stern-Gerlach instruments, will be described by a different wave function $|\psi'\rangle$ such that

$$|\psi'\rangle = [\hat{S}_z [\hat{S}_x (\hat{S}_z |\psi\rangle)]] = \hat{S}_z \hat{S}_x \hat{S}_z |\psi\rangle$$

Be mindful that the first $\hat{S}_z$ operator (the left-most) in the equation above corresponds to the action of the last apparatus, while the first apparatus action is described by the third operator (the right-most), also $\hat{S}_z$.

Let's start with the experiment where the particle is subjected to a succession of two $\hat{S}_z$ measurements as illustrated in Figure 6.5. The experimental evidence indicates that any particle that emerges from the first apparatus in the upper trajectory, for which $S_z = +$, will emerge from the second apparatus in the upper trajectory, again giving $S_z = +$ with certainty. Similarly, a particle that emerges from the first apparatus in the lower trajectory will always emerge from the second apparatus in the lower trajectory.

> **Figure 6.4: Schematic representation of three Stern-Gerlach experiments in series $\hat{S}_z \hat{S}_x \hat{S}_z$ (Adapted from MJasK, WikiWand. Used under CC BY-SA 4.0).**
> 
> Symbolic representation of Stern-Gerlach devices. A single Stern-Gerlach apparatus consists of a magnet producing an inhomogeneous magnetic field whose gradient is in the $n$-direction. In this topic, we will consider the particles that travel along the $y$-axis, while the magnetic fields will be aligned either along the $x$-axis ($\hat{S}_x$) or the $z$-axis ($\hat{S}_z$).
> 
> *Long Description:*
> A diagram with two parts:
> A vector graphic with a box on the left labelled 'Source' with lines coming from it leading through interlocking shapes and plates to a plate in the top right-hand corner of the graphic. Underneath is a diagram of three linked boxes labelled (from the left) '$\hat{S}_z$', '$\hat{S}_x$' and '$\hat{S}_z$'.
> The top part of the figure shows (from close to the 'Source' box) interlocking shapes representing the magnets and labelled 'S' (for south pole) and 'N' (for north pole). The first magnet is labelled 'S-G z-axis' with a small, right-facing arrow above the $z$; a square plate where the line stops labelled 'Z−'; interlocking shapes labelled 'S' and 'N', 'N' is also labelled S-G x-axis with a small, right-facing arrow above the $x$; a square plate where the line stops labelled 'X−' which has the label 'Z+' earlier on the line that leads to it; a third set of interlocking shapes labelled 'S' and 'N', with 'N' also having the label S-G z-axis with a small, right-facing arrow above the $z$; a rectangular plate where two lines end: the top line is labelled 'Z+' and the bottom line is labelled 'Z−' with two red lines below it.
> At the bottom right of the image, three arrows come from a central point representing the $z$, $y$ and $x$ axes of a co-ordinate system.
> The bottom part of the figure shows a box labelled '$\hat{S}_z$' with two lines coming from it to the right. The bottom line is a short line with a red vertical line across the end labelled '$S_z = -$'. The top line is labelled '$S_z = +$' and leads to the second box labelled '$\hat{S}_x$' which also has two lines coming from it to the right; the bottom line is a short line with a red vertical line across the end labelled '$S_x = -$'. The top line is labelled '$S_x = +$' and leads to the third box labelled '$\hat{S}_z$' which also has two lines coming from it to the right. The bottom line is a short line with a red vertical line across the end labelled '$S_z = -$'. The top line is labelled '$S_z = +$'.

This correlation between the two successive measurement outcomes is independent of the particle's state prior to entering the first apparatus.

It follows that if the first measurement yields $S_z = +$ then, if the only subsequent actions on the particle are measurements of $S_z$, these will always yield $S_z = +$. A similar statement applies to $S_z = -$. In this sense, one can say that after the first $\hat{S}_z$ measurement the particle has a definite value of $S_z$. That is, any subsequent measurement of $S_z$ will yield just one of the values with certainty.

To use the language of quantum mechanics, the action of measuring the state of a particle with $\hat{S}_z$ makes a wave function describing the particle collapse into one of the two eigenstates, $|\psi_+\rangle$ or $|\psi_-\rangle$, that correspond to the two possible eigenvalues $S_z = +$ or $S_z = -$ of the operator $\hat{S}_z$.

Using the first Stern-Gerlach apparatus to prepare the particle initially in a specific state $S_z = +$ (respectively, $S_z = -$) described by the wave function $|\psi_z^+\rangle$ (respectively, $|\psi_z^-\rangle$), we can calculate the probabilities of finding the particle in each of the $S_z = +$ or $S_z = -$ states after the second apparatus. Recall that $\langle b | a \rangle$ is the amplitude that a particle that is in state $a$ will get through an apparatus into the $b$ state. We can say: $\langle b | a \rangle$ is the amplitude for an atom in the state $a$ to get into the state $b$. Furthermore, to obtain the probability $P(b | a)$ of obtaining the state $b$, knowing that the particle is in state $a$, we need to take the modulus square of the corresponding amplitude: $P(b | a) = |\langle b | a \rangle|^2$. Observing the experimental outcomes in Figure 6.5, we can write the following results for the amplitudes:

$$\begin{aligned}
\langle \psi_z^+ | \psi_z^+ \rangle = 1 &\longrightarrow P(\psi_z^+ | \psi_z^+) = |\langle \psi_z^+ | \psi_z^+ \rangle|^2 = 1 \\
\langle \psi_z^- | \psi_z^+ \rangle = 0 &\longrightarrow P(\psi_z^- | \psi_z^+) = |\langle \psi_z^- | \psi_z^+ \rangle|^2 = 0 \\
\langle \psi_z^+ | \psi_z^- \rangle = 0 &\longrightarrow P(\psi_z^+ | \psi_z^-) = |\langle \psi_z^+ | \psi_z^- \rangle|^2 = 0 \\
\langle \psi_z^- | \psi_z^- \rangle = 1 &\longrightarrow P(\psi_z^- | \psi_z^-) = |\langle \psi_z^- | \psi_z^- \rangle|^2 = 1
\end{aligned} \tag{6.1}$$

We can write those results more succinctly under their matrix form, whose elements are the amplitudes:

$$\hat{S}_z = \begin{pmatrix} |\langle \psi_z^+ | \psi_z^+ \rangle| & |\langle \psi_z^+ | \psi_z^- \rangle| \\ |\langle \psi_z^- | \psi_z^+ \rangle| & |\langle \psi_z^- | \psi_z^- \rangle| \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

> **Figure 6.5: A repeated $\hat{S}_z$ measurement will give the same outcome as the first $\hat{S}_z$ measurement.**
> 
> *Long Description:*
> A two-part diagram. The top part shows (from the left) a circle with a dot in the centre labelled 'x' has an arrow pointing up coming from it labelled 'z' and an arrow pointing to the right coming from it labelled 'y'. To the right of this a box labelled '$\hat{S}_z$' has two lines coming from it to the right. The bottom line is a short line with a red vertical line across the end labelled '$S_z = -$'. The top line is labelled '$S_z = +$' and leads to the second box labelled '$\hat{S}_z$' which also has two lines coming from it to the right; the bottom line is a short line with a red vertical line across the end labelled '$S_x = -$' which is crossed out and the word 'none' written below it. The bottom part shows (from the left) a circle with a dot in the centre labelled 'x' has an arrow pointing up coming from it labelled 'z' and an arrow pointing to the right coming from it labelled 'y'. To the right of this a box labelled '$\hat{S}_z$' has two lines coming from it to the right. The bottom line is a short line with a red vertical line across the end labelled '$S_z = -$'. The top line is labelled '$S_z = +$' and leads to the second box labelled '$\hat{S}_z$' which also has two lines coming from it to the right; the bottom line is a short line with a red vertical line across the end labelled '$S_x = -$' and the top line is labelled '$S_z = +$' which is crossed out and the word 'none' written below it.

There are a few important points to recognise following this discussion. The first is that the Stern-Gerlach apparatus is both a spin preparation device and a spin measurement device. Thus, if an atom should emerge in a beam corresponding to a spin component $S_z = +$, then we can claim that the Stern-Gerlach apparatus has prepared the atom to have this specific value for $S_z$. More than that, we can also claim that the apparatus is a spin measuring device; in other words, if we wish to determine what the $z$ component of the particle spin happens to be for a given particle, we would pass that particle through a Stern-Gerlach apparatus, and the beam in which it emerges will tell us what the value is of this component. This relationship between preparation and measurement is, of course, not purely classical, but it acquires a heightened level of significance in quantum mechanics.

## 6.3 Repeated measurements of the different types

The Stern-Gerlach device presents a possible way of both preparing and measuring the various components of particle spin. Thus, if a particle emerges in the $S_z = +$ trajectory, then the statement can be made that a particle has been prepared such that the $z$ component of the spin is $S_z = +$.

To understand how the many possible states are related to each other, consider successive Stern-Gerlach measurements of different types, say $\hat{S}_z$ then $\hat{S}_x$, as illustrated in Figure 6.6.

> **Figure 6.6: If the atoms are in a definite state with respect to $\hat{S}_z$, they are not in the same state with respect to $\hat{S}_x$. A $\hat{S}_x$ measurement that follows an $\hat{S}_z$ measurement will give equal probability of measuring $S_x = +$ as $S_x = -$, independently of the value after $\hat{S}_z$ measurement.**
> 
> *Long Description:*
> A box labelled '$\hat{S}_z$' has two lines coming from it to the right.
> 1. The top line is labelled '$S_z = +$' and leads to the second box labelled '$\hat{S}_x$' which also has two lines coming from it to the right; the top line is labelled '$S_x = +$' and the bottom line is labelled '$S_x = -$'.
> 2. The bottom line is labelled '$S_z = -$' and leads to the second box labelled '$\hat{S}_x$' which also has two lines coming from it to the right; the top line is labelled '$S_x = +$' and the bottom line is labelled '$S_x = -$'.

Experiments show that if the particle emerges from the $\hat{S}_z$ apparatus in the upper trajectory ($S_z = +$), then it can subsequently emerge in either (but not simultaneously both) of the trajectories after the $\hat{S}_x$ apparatus. Unlike successive $\hat{S}_z$ measurements, no final trajectory after $\hat{S}_x$ is excluded. Furthermore, the probability with which it emerges in the upper trajectory $S_x = +$ is $1/2$ and the probability with which it emerges in the lower trajectory $S_x = -$ is found to be $1/2$.

As in the previous section, we can write the amplitudes of possible outcomes of the measurements with $\hat{S}_z$ then $\hat{S}_x$:

$$\begin{aligned}
\langle \psi_x^+ | \psi_z^+ \rangle = \frac{1}{\sqrt{2}} &\longrightarrow P(\psi_x^+ | \psi_z^+) = |\langle \psi_x^+ | \psi_z^+ \rangle|^2 = \frac{1}{2} \\
\langle \psi_x^- | \psi_z^+ \rangle = \frac{1}{\sqrt{2}} &\longrightarrow P(\psi_x^- | \psi_z^+) = |\langle \psi_x^- | \psi_z^+ \rangle|^2 = \frac{1}{2} \\
\langle \psi_x^+ | \psi_z^- \rangle = \frac{1}{\sqrt{2}} &\longrightarrow P(\psi_x^+ | \psi_z^-) = |\langle \psi_x^+ | \psi_z^- \rangle|^2 = \frac{1}{2} \\
\langle \psi_x^- | \psi_z^- \rangle = \frac{1}{\sqrt{2}} &\longrightarrow P(\psi_x^- | \psi_z^-) = |\langle \psi_x^- | \psi_z^- \rangle|^2 = \frac{1}{2}
\end{aligned} \tag{6.2}$$

If the atoms are in a definite state with respect to $\hat{S}_z$, they are not in the same state with respect to $\hat{S}_x$ — a $|\psi_z^+\rangle$ state is not also a $|\psi_x^+\rangle$ state.

In general, a particle can be subjected to an $\hat{S}_m$ apparatus followed by an $\hat{S}_n$ apparatus where $\mathbf{m}$ and $\mathbf{n}$ are any two unit vectors with an arbitrary angle between them. Suppose that the particle emerges from $\hat{S}_m$ with $S_m = +$. Thus, the state immediately after the first Stern-Gerlach apparatus is $|\psi_m^+\rangle$. The experimental evidence is that it will emerge from $\hat{S}_n$ with $S_n = +$ with probability $(1 + \mathbf{m} \cdot \mathbf{n}) / 2$, where $\mathbf{m} \cdot \mathbf{n}$ denotes a dot product between unit vectors $\mathbf{m}$ and $\mathbf{n}$. Thus, the general rules are:

$$|\psi_m^+\rangle \text{ into } \hat{S}_n \longrightarrow \begin{cases} S_n = + & \text{with probability } \frac{1 + \mathbf{m} \cdot \mathbf{n}}{2} \\ S_n = - & \text{with probability } \frac{1 - \mathbf{m} \cdot \mathbf{n}}{2} \end{cases} \tag{6.3}$$

and

$$|\psi_m^-\rangle \text{ into } \hat{S}_n \longrightarrow \begin{cases} S_n = + & \text{with probability } \frac{1 - \mathbf{m} \cdot \mathbf{n}}{2} \\ S_n = - & \text{with probability } \frac{1 + \mathbf{m} \cdot \mathbf{n}}{2} \end{cases} \tag{6.4}$$

An unusual feature of quantum mechanics is evident when one considers two Stern-Gerlach measurements of the same type interspersed with a single Stern-Gerlach measurement along an orthogonal direction. An example is illustrated in Figure 6.4, in which it is assumed that the particle emerged with $S_z = +$ after the first $\hat{S}_z$ measurement.

Applying the rules from Eq. (6.3), one can deduce that the probability with which the particle emerges with $S_z = +$ after either of the latter $\hat{S}_z$ measurements is 1/2. Similarly, the probability with which the particle emerges with $S_z = -$ after either of the latter $\hat{S}_z$ measurements is 1/2.

The implication is that it makes sense to speak of a particle as having a definite value for $S_z$ in the context where the only subsequent operations are $\hat{S}_z$ measurements but not where subsequent operations include $\hat{S}_n$ measurements, where $\mathbf{n}$ is distinct from $z$. It is impossible to speak of a particle as having a definite value of $S_z$ for arbitrary general scenarios: the state that we observe depends not only on some intrinsic property of the particle, but also on the operations that we perform to measure that state.

## 6.4 Quantum interference

(Adapted from lecture notes by J. D. Cresser [2011] [[2]](https://canvas.sussex.ac.uk/courses/41954/pages/week-6-stern-gerlach-experiment-study))

We have seen previously that in the case of the double slit experiment, there are two ways that a particle can pass from the particle source to the observation screen: via one slit or the other. Provided the slit through which the particle passes is not observed, the particles do not strike the screen in a way that is consistent with our intuitive notion of the way a particle should behave: the particles strike the observation screen at random but with a preference to accumulate in certain regions, and not at all in other regions, so as to form a pattern identical to the interference pattern that would be associated with waves passing through the slits. In contrast, if the slit through which each particle passes is observed in some fashion, the interference pattern is replaced by the expected result for particles.

To explain the double slit experiment, we associated with the particle a wave function which, for a point $x$ on the observation screen, could be written as the sum of two contributions originating from each slit $-\psi(x, t) = \psi_1(x, t) + \psi_2(x, t)-$ and whose intensity $|\psi(x, t)|^2$ gave the probability density of observing a particle at a particular position $x$ on the observation screen. Interference is a signature of quantum mechanics even when, as in the case of particle spin, the property of the particle being observed is not its position, a continuous variable, but rather its spin, which can only have discrete values. Such interference arises when there is more than one path that a particle can follow between its source and its final observation. The Stern-Gerlach experiment provides further evidence that there is an underlying commonality between different examples of quantum behaviour, evidence of some fundamental law or laws that apply to all physical systems, though superficially realised in different ways for different systems (p. 95) [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-6-stern-gerlach-experiment-study).

Let's consider the following experiment, represented in Figure 6.7. Atoms emerge from the oven and are then passed through a Stern-Gerlach device whose magnetic field is oriented so as to separate the atoms into two beams according to their $z$ component of spin. The atoms emerge in two separate beams corresponding to the atomic spin component $S_z = +$ and $S_z = -$. The atoms in one of the beams ($S_z = +$) are then selected and passed through a Stern-Gerlach device, where the magnetic field further separates this beam according to its $x$ component of spin. The atoms emerge in one or the other of two beams corresponding to $S_x = +$ or $S_x = -$. The two beams are then recombined into a single beam. This is done using a third Stern-Gerlach device in which the magnetic field is equal and opposite to the preceding device. This does not scramble the spins of the atoms — the sole purpose is to recombine the beams and could equally well have been done by some other technique. Finally, this beam is passed through a further Stern-Gerlach apparatus with its magnetic field oriented in the $z$ direction so that atoms will emerge from this device with either $S_z = +$ or $S_z = -$.

> **Figure 6.7: Atomic beam prepared in the $S_z = +$ state is split into two trajectories, $S_x = +$ and $S_x = -$, with $\hat{S}_x$ Stern-Gerlach apparatus. The two trajectories are recombined with a $-\hat{S}_x$ device (north/south magnetic poles direction inverted from that of $\hat{S}_x$) and finally passed through a final Stern-Gerlach apparatus with magnetic field in the $z$ direction ($\hat{S}_z$).**
> 
> *Long Description:*
> A diagram showing four Stern-Gerlach devices arranged sequentially from left to right:
> 1. An orange box labelled '$\hat{S}_z$' receives the initial atomic beam. Two lines emerge to the right: the top line labelled '$S_z = +$' leads to the next box, while the bottom line labelled '$S_z = -$' stops with a red barrier line.
> 2. A blue box labelled '$\hat{S}_x$' with sub-label 'Split' divides the '$S_z = +$' beam into two paths: an upper line labelled '$S_x = +$' and a lower line labelled '$S_x = -$'.
> 3. A second blue box labelled '$-\hat{S}_x$' with sub-label 'Combine' recombines both '$S_x = +$' and '$S_x = -$' trajectories into a single line labelled '$S_x = \pm$'.
> 4. An orange box labelled '$\hat{S}_z$' receives the recombined beam and separates it into two emerging paths: a top path labelled '$S_z = +$' and a bottom path labelled '$S_z = -$'.

It is important to see the analogy between this setup and the double-slit interference experiment. The oven plus the first Stern-Gerlach device is the equivalent of the source of identically prepared particles in the double-slit experiment. Here, the atoms are all identically prepared to have $S_z = +$. The next two Stern-Gerlach devices are analogous to the two slits in that the atoms can, in principle, follow two different paths corresponding to $S_x = +$ and $S_x = -$, before they are recombined to emerge in one beam. The analogue is, of course, with a particle passing through one or the other of two slits before the position where it strikes the observation screen is observed. We can tell which path an atom follows (i.e., via the $S_x = +$ or the $S_x = -$ beam) by monitoring which beam an atom emerges from after it passes through the first $x$ oriented Stern-Gerlach device ($\hat{S}_x\text{-SPLIT}$) in much the same way that we can monitor which slit a particle passes through in the double-slit experiment. Watching to see in which beam an atom finally emerges after passing through the last Stern-Gerlach device is then analogous to seeing where on the observation screen a particle lands after passing through the double-slit device (p. 86).

The results of such an experiment are as follows. If the intervening state of the atoms is not observed, i.e., we don't know whether atoms pass via beam $S_x = +$ or $S_x = -$, the results obtained are the same as if the beam splitter-recombiner were not there, i.e., the results are the same as in the case of repeated measurement of the same type (Figure 6.5), and the associated probabilities are given by Eq. (6.1). However, if the $x$ component of the spin is observed, then it is effectively an atom with a known $x$ component of spin that enters the last Stern-Gerlach device, as for Figure 6.6, and hence the probability of the atom having either value of $S_z$ becomes $1/2$, as in Eq. (6.2) (p. 96) [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-6-stern-gerlach-experiment-study#sect5).

This behaviour is reminiscent of what was observed in the double-slit experiment – if we do not observe through which slit the particles pass, then we observe an interference pattern. If we do observe through which slit the particles pass, then there is no interference pattern. So, in that sense, the results found above for the Stern-Gerlach experiment can be interpreted as the presence of interference in the first case and no interference in the second (p. 96) [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-6-stern-gerlach-experiment-study#sect5).

## Summary
Well done! You have now reached the end of this week’s Study – Week 6: Stern-Gerlach experiment.

This week, we delved into the intriguing realm of the Stern-Gerlach experiment. This experiment is pivotal in the history of quantum mechanics and provides profound insights into the nature of particles and their intrinsic properties. 