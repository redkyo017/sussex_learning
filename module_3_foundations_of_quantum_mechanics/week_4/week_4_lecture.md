# Week 4: Schrödinger equation: Study

## 4. Schrödinger equation

### Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

This week, we will consider quantum mechanical systems that involve a single particle moving in one spatial dimension, $x$. This means that the wave function $\Psi(x, t)$ depends on just a single spatial variable, $x$, in addition to time $t$. As a result, the Schrödinger equation becomes:

$$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi \tag{4.1}$$

We will solve this equation for various choices of potential $V(x)$ and interpret the results.

In this Study you will cover the following topics:
- [4.1 The time independent Schrödinger equation](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-study#)
- [4.2 The free particle](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-study#)
- [4.3 The infinite potential well](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-study#)

---

### 4.1 The time independent Schrödinger equation

The Schrödinger equation is a partial differential equation that we can solve using standard mathematical tools. However, there is a straightforward way to deal with the time variable. We can use a specific solution that separates spatial and temporal variables, that is, the ansatz equation:

$$\Psi(x, t) = e^{-i\omega t}\psi(x) \tag{4.2}$$

where $\omega$ is some choice of frequency. Plugging the ansatz Eq. (4.2) in Eq. (4.1), we find

$$i\hbar \frac{\partial}{\partial t}\left( e^{-i\omega t}\psi(x) \right) = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}\left( e^{-i\omega t}\psi(x) \right) + V(x)\left( e^{-i\omega t}\psi(x) \right)$$

$$\left[ i\hbar (-i\omega)\psi(x) \right] e^{-i\omega t} = \left[ -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\psi(x) \right] e^{-i\omega t} + \left[ V(x)\psi(x) \right] e^{-i\omega t}$$

$$\underbrace{\hbar\omega}_{E}\psi(x) = \underbrace{\left[ -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \right]}_{\hat{H}}\psi(x)$$

This is known as the *time independent Schrödinger equation*, for the obvious reason that it does not depend on time. We can rewrite the last line as

$$\hat{H}\psi(x) = E\psi(x) \tag{4.3}$$

where $E = \hbar\omega$. We notice the form of the eigenvalue equation that we met previously. In all the examples that will follow, we'll see that there are solutions to Eq. (4.3) only for very specific values of $E$ (we say that the solutions are in the spectrum $\{E_n\}$). Furthermore, these special values of $E$ will have the interpretation of the possible energies of the system. Separable solutions of the form in Eq. (4.2) are sometimes referred to as stationary states and sometimes as energy eigenstates. They play a special role in quantum mechanics. One might worry that restricting attention to solutions of this kind is too restrictive, and that we are missing a whole bunch of other interesting solutions. In fact, as we go on, we will see that all solutions can be expressed as linear combinations of different stationary states. That means that we will be able at the end to patch together the separable solutions in such a way as to construct the most general solution.

Let's briefly summarise what we will be doing in the following sections. You will be given a (time independent) potential $V(x)$, and the starting wave function $\Psi(x, 0)$; your job is to find the wave function, $\Psi(x, t)$, for any subsequent time $t$. To do this you must solve the (time dependent) Schrödinger equation, Eq. (4.1). The strategy is first to solve the time independent Schrödinger equation, Eq. (4.3); this yields, in general, an infinite set of solutions, $\{\psi_n(x)\}$, each with its own associated energy, $\{E_n = \hbar\omega_n\}$. To fit $\Psi(x, 0)$ we write down the general linear combination of these solutions:

$$\Psi(x, 0) = \sum_{n=1}^{\infty} \alpha_n \psi_n(x) \tag{4.4}$$

You can always match the specified initial state $\Psi(x, 0)$ by appropriate choice of the constants $\alpha_n$. To construct the general, time dependent solution $\Psi(x, t)$, you simply tack onto each term its characteristic time dependence factor $e^{-i\omega_n t}$:

$$\Psi(x, t) = \sum_{n=1}^{\infty} \alpha_n \psi_n(x) e^{-i\omega_n t} = \sum_{n=1}^{\infty} \alpha_n \Psi_n(x, t) \tag{4.5}$$

The separable solutions themselves,

$$\Psi_n(x, t) = \psi_n(x) e^{-i\omega_n t} \tag{4.6}$$

are stationary states, in the sense that all probabilities and expectation values are independent of time, but this property is emphatically not shared by the general solution, Eq. (4.5): the energies are different for different stationary states, and the exponentials do not cancel, when you construct $|\Psi|^2$.

To clarify what we have just seen, let's consider the following example. Suppose a particle starts out in a linear combination of just two stationary states:

$$\Psi(x, 0) = \alpha_1 \psi_1(x) + \alpha_2 \psi_2(x) \tag{4.7}$$

To keep things simple, assume that the constants $\alpha_n$ and the states $\psi_n(x)$ are real.

1. Find the wave function $\Psi(x, t)$ at subsequent time.
2. Find the probability density.
3. Describe its motion.

The first part is easy; we just add characteristic time dependence to time independent solutions:

$$\Psi(x, t) = \alpha_1 \psi_1(x) e^{-i\omega_1 t} + \alpha_2 \psi_2(x) e^{-i\omega_2 t} \tag{4.8}$$

where $\omega_1 = E_1/\hbar$ and $\omega_2 = E_2/\hbar$ are the energies associated with $\psi_1(x)$ and $\psi_2(x)$.

The probability density is:

$$|\Psi(x, t)|^2 = \Psi^*(x, t)\Psi(x, t) = \left(\alpha_1 \psi_1(x) e^{i\omega_1 t} + \alpha_2 \psi_2(x) e^{i\omega_2 t}\right)\left(\alpha_1 \psi_1(x) e^{-i\omega_1 t} + \alpha_2 \psi_2(x) e^{-i\omega_2 t}\right)$$

$$= \alpha_1^2 \psi_1^2(x) + \alpha_2^2 \psi_2^2(x) + 2\alpha_1\alpha_2\psi_1(x)\psi_2(x)\cos[(\omega_2 - \omega_1)t]$$

The probability density oscillates sinusoidally, at an angular frequency $\omega = \omega_2 - \omega_1$; this is certainly not a stationary state. But notice that it took a linear combination of stationary states (with different energies) to produce motion.

I hope that the link with what we have seen during previous weeks is straightforward, but let's repeat it:
1. The coefficients $|\alpha_n|^2$ represent the probability that a measurement of the energy would return the value $E_n = \hbar\omega_n$.
2. The sum of these probabilities should be 1: $\sum_{n=1}^{\infty} |\alpha_n|^2 = 1$.
3. The expectation value of the energy must be: $\langle \hat{H} \rangle = \sum_{n=1}^{\infty} |\alpha_n|^2 E_n$.

---

### 4.2 The free particle

Our first example is the simplest. We take a particle moving in one dimension in the absence of a potential

$$V(x) = 0$$

In this case, the time independent Schrödinger equation reads

$$-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = E\psi \tag{4.9}$$

The solutions to this differential equation are straightforward: there is a different solution for every wave vector $k \in \mathbb{R}$

$$\psi(x) = e^{ikx} \tag{4.10}$$

Plugging this solution into Eq. (4.9) allows us to find the eigenvalue $E$

$$E = \frac{\hbar^2 k^2}{2m} \tag{4.11}$$

From our discussion on the eigenfunctions and eigenstates, we know that the value $E$ has the interpretation of the energy of the state $e^{ikx}$. Let's compare this result with what we could expect from classical physics. In the absence of potential energy, there is only kinetic energy, given by

$$E = \frac{p^2}{2m}$$

where $p = mv$ is the momentum of the particle. Comparing the classical and quantum results suggests that the momentum of the state $\psi(x) = e^{ikx}$ is

$$p = \hbar k \tag{4.12}$$

The wave function, Eq. (4.10), can be viewed as a sum of sine and cosine functions and describes a complex-valued wave of wavelength

$$\lambda = \frac{2\pi}{|k|} \tag{4.13}$$

Here, we use $|k|$ because $k$ can have either sign, while the wavelength is always positive. Combining the equations Eq. (4.12) and Eq. (4.13), we can write

$$|p| = \frac{2\pi\hbar}{\lambda_{\mathrm{dB}}}$$

The wavelength $\lambda_{\mathrm{dB}}$ is called the *de Broglie wavelength* of the particle. Any non-relativistic particle, with momentum $p$, has an associated wavelength $\lambda_{\mathrm{dB}}$ and, in certain situations, exhibits wave-like properties: this is the origin of the *wave-particle duality* at the heart of quantum mechanics.

The most general solution to Eq. (4.9) is a combination of two linearly independent *plane waves* $\psi_+(x) = e^{ikx}$ and $\psi_-(x) = e^{-ikx}$:

$$\psi_k(x) = \alpha_+ e^{ikx} + \alpha_- e^{-ikx} \tag{4.14}$$

where $\alpha_+$ and $\alpha_-$ are two arbitrary constants. Notice that we wrote $\psi_k$ with the index $k$ to highlight the dependence of the wave function on the value of the wave vector $k$. When we tack onto each term its characteristic time dependence factor, we obtain the complete wave function

$$\Psi(x, t) = \alpha_+ e^{i(kx - \omega t)} + \alpha_- e^{-i(kx + \omega t)}$$

$$= \alpha_+ e^{i\left(kx - \frac{\hbar k^2}{2m}t\right)} + \alpha_- e^{-i\left(kx + \frac{\hbar k^2}{2m}t\right)}$$

since $\omega = E/\hbar = \hbar k^2 / 2m$. The first term, $\Psi_+(x, t)$, represents a wave travelling to the right, while the second term, $\Psi_-(x, t)$, represents a wave travelling to the left. The intensities of these waves are given by $|\alpha_+|^2$ and $|\alpha_-|^2$, respectively. We should note that the waves $\Psi_+(x, t)$ and $\Psi_-(x, t)$ are associated, respectively, with a free particle travelling to the right and to the left with *well-defined* momenta and energy: $p_\pm = \pm \hbar k$, $E_\pm = \hbar^2 k^2 / 2m$. We will comment on the physical implications of this in a moment. The free particle problem is simple to solve mathematically, yet it presents a number of physical subtleties. Let us discuss briefly three of these subtleties.

First, the probability densities corresponding to either solution

$$P_\pm(x, t) = |\Psi_\pm(x, t)|^2 = |\alpha_\pm|^2$$

are constant, for they depend neither on $x$ nor on $t$. This is due to the complete loss of information about the position and time for a state with definite values of momentum, $p_\pm = \pm \hbar k$, and energy, $E_\pm = \hbar^2 k^2 / 2m$. This is a consequence of *Heisenberg’s uncertainty principle*, which tells us that the product of uncertainties of the two conjugate variables ($p \leftrightarrow x$ and $E \leftrightarrow t$) must be, at best, equal to $\hbar/2$:

$$\Delta x \cdot \Delta p \ge \frac{\hbar}{2} \tag{4.15}$$

$$\Delta E \cdot \Delta t \ge \frac{\hbar}{2} \tag{4.16}$$

When the momentum and energy of a particle are known exactly, $\Delta p = 0$ and $\Delta E = 0$, there must be total uncertainty about its position and time: $\Delta x \to \infty$ and $\Delta t \to 0$.

The second subtlety pertains to an apparent discrepancy between the speed of the wave and the speed of the particle it is supposed to represent. The speed of the plane waves $\Psi_\pm(x, t)$ is given by

$$v_{\text{wave}} = \frac{\omega}{k} = \frac{E}{\hbar k} = \frac{\hbar^2 k^2 / 2m}{\hbar k} = \frac{\hbar k}{2m}$$

On the other hand, the classical speed of a particle is given by

$$v_{\text{classical}} = \frac{p}{m} = \frac{\hbar k}{m} = 2 v_{\text{wave}}$$

This means that the particle travels twice as fast as the wave that represents it!

Third, the wave function, Eq. (4.10), is not normalisable. If you integrate it, you get

$$\int_{-\infty}^{+\infty} \Psi_\pm^*(x, t) \Psi_\pm(x, t) \mathrm{d}x = |\alpha_\pm|^2 \int_{-\infty}^{+\infty} 1 \mathrm{d}x \to \infty$$

This means that $\Psi_\pm(x, t)$ don't represent physically realisable states, as physical wave functions must be square integrable. A free particle cannot exist in a stationary state. The problem can be traced to this: a free particle cannot have sharply defined momenta and energy – there is no such thing as a free particle with a definite energy.

But that doesn't mean the separable solutions are of no use to us. They play a mathematical role that is entirely independent of their physical interpretation: the general solution to the time dependent Schrödinger equation is still a linear combination of separable solutions (only this time it's an integral over the continuous variable $k$, instead of a sum over the discrete index $n$):

$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} \phi(k) e^{i(kx - \omega t)} \mathrm{d}k \tag{4.17}$$

where $\phi(k)$, the amplitude of the wave packet, is given by the Fourier transform of $\Psi(x, 0)$ as

$$\phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} \Psi(x, 0) e^{-ikx} \mathrm{d}x \tag{4.18}$$

Notice that in the continuous case, $\phi(k)$ plays the same role as $\alpha_n$ in the discrete case. Intuitively, we can understand the behaviour of the wave packets in terms of sinusoidal functions. Sinusoidal waves extend out to infinity, and they are not normalisable. But superpositions of such waves lead to interference, which allows for localisation and normalisability.

The wave packet solution cures and avoids all the subtleties raised above. First, the momentum, the position and the energy of the particle are no longer known exactly; only probabilistic outcomes are possible. Second, the wave packet, Eq. (4.17), and the particle travel with the same speed $v_g = p/m$, called the group speed. The interference between individual waves of the wave packet makes the packet travel more slowly than the individual waves. Third, the wave packet, Eq. (4.17), is normalisable.

To summarise, a free particle cannot be represented by a single (monochromatic) plane wave; it has to be represented by a wave packet. The physical solutions of the Schrödinger equation are thus given by wave packets, not by stationary solutions.

---

### 4.3 The infinite potential well

Now, let's consider a particle trapped in an infinite potential well of width $L$ depicted in Figure 4.1. We can describe such a well mathematically by setting

$$V(x) = \begin{cases} 0 & 0 \le x \le L \\ \infty & \text{otherwise} \end{cases}$$

> **Figure 4.1:** The infinite square well potential. The particle is confined in the central portion, where $V(x) = 0$.
>
> **Long description:** A diagram showing an $x$-axis pointing to the right labelled ‘x’ and a $y$-axis labelled $V(x)$ that starts a third of the way along the horizontal arrow at a point labelled ‘0’. A horizontal red line labelled ‘$V(x < 0) = \infty$’ comes in from the left to meet the vertical arrow near the top. It traces a path down the arrow to the point labelled ‘0’, along the line labelled ‘x’ and goes up vertically when it reaches the point labelled ‘L’ which is two thirds of the way along. It extends horizontally to the right when it reaches the same height as the point at which it started. The last part of the line is labelled ‘$V(x > L) = \infty$’.

You may think that we're no longer dealing with a free particle now that we're subjecting it to an infinite potential energy. However, the effect of an infinite $V(x)$ is very easy to deal with. The Schrödinger equation is

$$-\frac{\hbar^2}{2m} \frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} + V(x)\psi = E\psi$$

and if we're looking for states with finite energy $E$, then we must have $\psi = 0$ in any region where $V(x) = \infty$. Intuitively this is obvious: the infinite potential is just a plot device that allows us to insist that the particle is restricted to lie in the region $0 < x < L$. Within this region, we again have our free Schrödinger equation

$$-\frac{\hbar^2}{2m} \frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = E\psi$$

but now with the restriction that $\psi(x) = 0$ at the two ends of the interval $x = 0$ and $x = L$. Recall that the solutions are

$$\psi_k(x) = \alpha_+ e^{ikx} + \alpha_- e^{-ikx}$$

The requirement that $\psi(x = 0) = 0$ tells us that $\alpha_- = -\alpha_+$, so the wave function must be of the form

$$\psi_k(x) = \alpha_+(e^{ikx} - e^{-ikx}) = 2i\alpha_+ \sin(kx)$$

The factor of $2i\alpha_+$ in front simply changes the normalisation of the wave function and doesn't affect the physics. Now we have to impose the requirement that the wave function vanishes at the other end of the interval, $\psi_k(x = L) = 0$, or

$$\sin(kL) = 0 \implies k = \frac{\pi n}{L} \quad \text{with } n \in \mathbb{Z}^+ \tag{4.19}$$

Finally, if we want the wave function to be normalised correctly, we should take

$$\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{\pi n}{L} x\right)$$

Notice that in the last expression we reverted to indexing our wave function with the index $n$, rather than $k$. This is to highlight the dependence of the wave function on the positive integers $n$. The wave functions for the $n = 1, 2, 3$ and $4$ states are shown in Figure 4.2. In this example, we again see that energy is quantised, taking values

$$E_n = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2 \pi^2 n^2}{2m L^2} \tag{4.20}$$

The lowest energy of the particle is given by its ground state wave function and its value is $E_1 = \frac{\hbar^2 \pi^2}{2m L^2}$. We do not consider the solution for $n = 0$ because it gives us a trivial solution (and we interpret it to mean that there is no particle inside the well).

However, if there were a ground state with zero energy for a square well potential, it would imply that (since the particle has zero energy) it will be at rest inside the square well, and this would violate Heisenberg's uncertainty principle.

By confining a particle to a very small region in space, it acquires a small but finite momentum. So, if the particle is restricted to move in a region of width $\Delta x = \pm L/2$ (that is, the entire length of the well $L$), we can calculate the minimum uncertainty in momentum (using the uncertainty principle) and it comes out to be $\Delta p = \hbar/L$. And this, in turn, gives us the minimum kinetic energy of the order $\hbar^2 / (2m L^2)$. This (qualitatively) agrees with the exact value of the ground state energy.

So physically, the existence of a zero-point energy is a necessary feature of a quantum mechanical system. It indicates that the particle should exhibit a minimum motion due to localisation. Classically, the lowest possible energy of a system corresponds to the minimum value of the potential energy (with kinetic energy being zero). But in quantum mechanics, the lowest energy state corresponds to the minimum value of the sum of both potential and kinetic energy, and this leads to a finite ground state energy or zero-point energy.

> **Figure 4.2:** The wave functions for an infinite potential well: *a*) The ground state wave function $\psi_1$, followed by the first three excited states; *b*) $\psi_2$; *c*) $\psi_3$; and *d*) $\psi_4$. Appropriately normalised, each wave function will reach a maximum value of $\sqrt{2/L}$ and have corresponding energy $E_n = \frac{\hbar^2 \pi^2 n^2}{2m L^2}$.
>
> **Long description:** The infinite square well potential $\psi_1$ with the addition of a curve representing $\psi_2$, $\psi_3$ and $\psi_4$. In all four graphs there is a horizontal dotted line between the vertical lines extending from ‘x=0’ and ‘x=L’ which touches the curve at its highest points. The point at which the dotted line meets the y-axis is labelled $\sqrt{2/L}$ and represents the amplitude of the wavefunction.
> 1. The ground state wave function with a curve plotted as a function of the position $x$, starting at ‘x=0’ and ending at ‘x=L’.
> 2. The excited state $\psi_2$ with a curve starting at ‘x=0’ and ending at ‘x=L’, above the x-axis for half of the distance between ‘x=0’ and ‘x=L’ and below the x-axis for the other half.
> 3. The excited state $\psi_3$ with a curve starting at ‘x=0’ and ending at ‘x=L’, above the x-axis for a third of the distance between ‘x=0’ and ‘x=L’, below for the second third and then above for the last third.
> 4. The excited state $\psi_4$ with a curve starting at ‘x=0’ and ending at ‘x=L’, above the x-axis for a quarter of the distance between ‘x=0’ and ‘x=L’, below for the second quarter, above for the third quarter and then below for the last quarter.

What about the momentum? Recall our previous discussion: the state $e^{ikx}$ has momentum $p = \hbar k$. But, for the current example, we have (ignoring the normalisation) $\psi = e^{ikx} - e^{-ikx}$. This is the superposition of two states, one with momentum $p = +\hbar k$ and the other with momentum $p = -\hbar k$. This means that these states do not have a well-defined momentum. This shouldn't be a surprise because a classical particle in a box bounces back and forth and doesn't have a well-defined sign of the momentum either. Similarly, you can think of the wave functions as standing waves, bouncing backwards and forwards between the two walls but not going anywhere.

This connects nicely with the previous section, where we have seen that a state with definite momentum $e^{ikx}$ doesn't describe a real particle. However, a state that is a superposition of two or many of such definite-momentum states can represent a physical particle.

The discreteness of energy levels in the infinite well has an important application. Consider particles moving, as particles do, in three spatial dimensions. Suppose that you trap them in a well in one dimension, but still allow them to wander in the other two. Then, provided that you can restrict their energies to be small enough, the particles will act, to all intents and purposes, as if they're really two-dimensional objects.

This is in sharp distinction to what happens in classical mechanics, where the particles would move approximately in two dimensions but there would always be small oscillations in the well that can't be ignored. In contrast, the discreteness of quantum mechanics turns an approximate statement into an exact one: if the particle doesn't have enough energy to jump to the $n = 2$ state, then it really should be thought of as a two-dimensional particle. Of course, we can also restrict its motion once more and make it a one-dimensional particle.

This may not seem like a big deal at this stage but interesting things can happen in low dimensions that don't happen in our three-dimensional world. But these things aren't mere mathematical curiosities: they can be constructed in the lab using the method above. For example, in the fractional quantum Hall effect that occurs only in two-dimensional systems, an electron can split into $N$ objects, called quasiparticles, each carrying fractional electric charge $1/N$ [[1]](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-study#).

---

## Summary

Well done! You have now reached the end of this week’s Study – Week 4: Schrödinger equation[cite: 1].

This week, we considered quantum mechanical systems that involve a single particle moving in one spatial dimension[cite: 1]. You will recall that this means that the wave function depends on just a single spatial variable, $x$, in addition to time $t$[cite: 1].