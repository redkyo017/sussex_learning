# Week 3: Probabilistic nature of the measurement in Quantum Mechanics: Study

## 3. Probabilistic nature of the measurement in Quantum Mechanics

### Introduction
This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

One of the most intriguing aspects of quantum mechanics is the measurement problem, which refers to the question of how a particle's wave function collapses during measurement. When a quantum particle is measured, the wave function that describes its state collapses into a specific outcome, revealing the particle's position, momentum or other properties. However, the exact nature of this collapse has been a subject of intense debate and research for decades.

In this section, we will explore the measurement problem in quantum mechanics, including the probabilistic nature of the outcome of the measurement. We will discuss the various interpretations of quantum mechanics and how they address the measurement problem. We will guide you through the three postulates of quantum mechanics that relate to measurement.

In this Study you will cover the following topics:
- 3.1 Postulate 3: Measurement in quantum mechanics
- 3.2 Postulate 4: Probabilistic nature of the outcome of the measurement
- 3.3 Postulate 5: Collapse of the wave function
- 3.4 Interpretations of quantum mechanics

---

## 3.1 Postulate 3: Measurement in quantum mechanics

We have seen that in quantum mechanics every observable (measurable quantity) is associated with an operator $\hat{A}$. The third postulate says that the only values that will ever be observed are the eigenvalues $\lambda_n$ that satisfy the eigenvalue equation

$$\hat{A}|\phi_n\rangle = \lambda_n|\phi_n\rangle. \tag{3.1}$$

Said in another way, the only possible result of the measurement of an observable $A$ is one of the eigenvalues of the corresponding operator $\hat{A}$.

This postulate is at the origin of the word *quantum* in quantum mechanics. If the observable has a continuous spectrum of eigenvalues, like the position $x$ or the momentum $p$, then the statement is not surprising. If it has a discrete spectrum, like the Hamiltonian for an electron bound to a proton (the hydrogen atom), then the statement is shocking. A measurement of the energy of the hydrogen atom will yield only one of a discrete set of values. Needless to say, this postulate reflects mountains of experimental evidence such as the discrete spectral lines observed in the radiation from a tube of hot hydrogen gas.

We know that the possible result of any measurement is taken from the spectrum of eigenvalues $\lambda_n$. But how does this result depend on the state described by a wave function $|\psi\rangle$? The answer to this question is by no means trivial and it introduces the famous probabilistic nature of quantum mechanics: it is impossible to predict the outcome of a quantum measurement; all we can predict is its likelihood. In this section we will discuss what happens in quantum mechanics when we measure a physical quantity $A$ that has corresponding operator $\hat{A}$. The quantity could be, for example, the position of a particle, or its momentum, or its energy.

We know from postulate 2 of quantum mechanics that such a physical quantity is associated with a Hermitian operator $\hat{A}$ that is called observable. Postulate 3 means that when we want to measure property $A$, we first need to solve the corresponding eigenvalue equation, Eq. (3.1). This allows us to find all eigenvalues

$$\lambda_1, \lambda_2, \dots, \lambda_n, \dots$$

Whatever state our system is in – described by wave function $|\psi\rangle$ – when we measure $A$ we can only get one of the eigenvalues $\lambda$ as the outcome of the measurement.

The operator $\hat{A}$ encodes all the possible outcomes of the measurement, irrespective of the state $|\psi\rangle$ of the system. However, which specific eigenvalue $\lambda_n$ we will obtain, or, given the probabilistic nature of the quantum measurement, the probability of obtaining a specific outcome $\lambda_n$, does depend on the state $|\psi\rangle$. To answer how, we need to consider postulate 4.

---

## 3.2 Postulate 4: Probabilistic nature of the outcome of the measurement

Postulate 4 says that when a measurement of an observable $\hat{A}$ is made on a normalised state $|\psi\rangle$, the probability of obtaining an eigenvalue $\lambda_n$ is given by the square of the inner product of $|\psi\rangle$ with the eigenstate $|\phi_n\rangle$:

$$P(\lambda_n) = |\langle \phi_n | \psi \rangle|^2. \tag{3.2}$$

To understand where this result comes from, we first decompose the state $|\psi\rangle$ in terms of orthonormal eigenfunctions of operator $\hat{A}$,

$$|\psi\rangle = \sum_n \alpha_n |\phi_n\rangle. \tag{3.3}$$

The expansion coefficients $\alpha_n$ tell us the relative contribution of eigenstate $|\phi_n\rangle$ to state $|\psi\rangle$, which in turn tells us how likely it is to measure the associated eigenvalue $\lambda_n$. We will take both eigenfunctions $|\phi_n\rangle$ and wave function $|\psi\rangle$ to be normalised, which means that $\sum_n |\alpha_n|^2 = 1$. Assuming that the spectrum is non-degenerate, the probability that the result of the measurement gives the answer $\lambda_n$ is given by the Born rule,

$$P(\lambda_n) = |\langle \phi_n | \psi \rangle|^2 = \left| \sum_i \alpha_i \langle \phi_n | \phi_i \rangle \right|^2 = |\alpha_n|^2, \tag{3.4}$$

where we used the orthogonality of eigenfunctions $\langle \phi_n | \phi_i \rangle = \delta_{ni}$.

It is important to understand that for operator $\hat{A}$ we have a list of eigenvalues $\lambda_n$ that correspond to a list of eigenfunctions $|\phi_n\rangle$. These two lists are always the same for operator $\hat{A}$ – they are independent of the state $|\psi\rangle$ of our system. They simply come from the eigenvalue equation of the operator $\hat{A}$, Eq. (3.1). However, when we measure $\hat{A}$ in a system described by a specific state $|\psi\rangle$, postulate 4 tells us that the probability of finding a specific outcome $\lambda_n$ is given by $|\langle \phi_n | \psi \rangle|^2$.

| $\hat{A}:$ | $\lambda_1$ | $\lambda_2$ | $\lambda_3$ | $\dots$ | $\lambda_n$ | $\dots$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | $|\phi_1\rangle$ | $|\phi_2\rangle$ | $|\phi_3\rangle$ | $\dots$ | $|\phi_n\rangle$ | $\dots$ |
| $P(\lambda_i):$ | $|\langle \phi_1 | \psi \rangle|^2$ | $|\langle \phi_2 | \psi \rangle|^2$ | $|\langle \phi_3 | \psi \rangle|^2$ | $\dots$ | $|\langle \phi_n | \psi \rangle|^2$ | $\dots$ |
| | $|\alpha_1|^2$ | $|\alpha_2|^2$ | $|\alpha_3|^2$ | $\dots$ | $|\alpha_n|^2$ | $\dots$ |

It's postulate 4 (the Born rule) that introduces the famous probabilistic nature of quantum mechanics. Rather than telling us the precise outcome of a measurement, it tells us the probability associated with any given outcome. Because of this postulate, in quantum mechanics it is impossible to know the exact outcome of any given measurement before you actually make the measurement – all we can predict is the probability of getting a particular outcome. This is the fundamental difference with classical physics: in classical mechanics, if you know the position and momentum of a particle at some time $t_0$, you can predict its position at any other later time $t > t_0$ even before you measure it. In quantum mechanics, if you know the wave function of a particle at time $t_0$, you can only predict the probabilities of where you might find the particle at later time $t > t_0$, but you cannot know its position until you measure it.

The measurement holds an important role in quantum mechanics. It is still a mystery and matter of debate what exactly is happening with the system during the measurement. And, like a magician pulls a rabbit from the hat, a physicist pulls a cat; Schrödinger’s cat, or postulate number 5.

---

## 3.3 Postulate 5: Collapse of the wave function

The fifth postulate tells us that immediately after the measurement of an observable $\hat{A}$ has yielded a value $\lambda_n$, the state of the system is the normalised eigenstate $|\phi_n\rangle$.

Known picturesquely as the ‘collapse of the wave function', this is the most controversial of the postulates of quantum mechanics, and the most difficult to get comfortable with. It is motivated by experience with repeated measurements. If an experimental sample is prepared in a state $|\psi\rangle$ then it is observed that a measurement of $\hat{A}$ can yield a variety of results $\lambda_n$ with probabilities $|\langle \phi_n | \psi \rangle|^2$. Identically prepared systems can yield different experimental outcomes. This is encompassed by the fourth postulate. However, if $\hat{A}$ is measured with outcome $\lambda_n$ on a given system, and then is immediately remeasured, the results of the second measurement are not statistically distributed – the result is $\lambda_n$ again. Hence postulate 5.

To reflect this behaviour, there is a *collapse of the wave function*, which jumps to

$$|\psi\rangle \longrightarrow |\phi_n\rangle. \tag{3.5}$$

This ensures that if we make a second measurement of $\hat{A}$ immediately after the first one, then we get the same answer: $\lambda_n$ (see Figure 3.1).

**Figure 3.1:** Collapse of the wave function. Initially, at $t = 0$, a system is described by the wave function $|\psi(0)\rangle$ and evolves following the time-dependent Schrödinger equation until time $t_0$ when the measurement is performed. When a measurement at time $t_0$ of the observable $\hat{A}$ gives the result $\lambda_n$, the wave function of the system undergoes an abrupt modification and becomes $|\phi_n\rangle$. This new initial state then evolves following the time-dependent Schrödinger equation.

Let's look at one obvious implication of the measurement procedure described above. Suppose that we measure a (non-degenerate) observable $\hat{A}$ and get a definite result, say $\lambda_6$. Immediately after the measurement, the system sits in the state

$$|\psi\rangle = |\phi_6\rangle. \tag{3.6}$$

We already noted that if we again measure $\hat{A}$, then there's no doubt about the outcome: we get the result $\lambda_6$ again for sure. The general statement is that the system has a definite value for some observable only if it sits in an eigenstate of that observable.

Now we measure a different observable, $\hat{M}$. In general, this will have a different set of eigenstates,

$$\hat{M}|\chi_n\rangle = \mu_n|\chi_n\rangle$$

and a different set of outcomes $\mu_n$. There's no reason why the eigenstates of $\hat{M}$ should have anything to do with the eigenstates of $\hat{A}$: they will typically be entirely different functions. We now have to play the game all over again: we take our state, which we know is $|\phi_6\rangle$, and expand

$$|\phi_6\rangle = \sum_m \beta_m |\chi_m\rangle.$$

There is no certainty about what we get when we measure $\hat{M}$: the result $\mu_m$ appears with probability $P(\mu_m) = |\beta_m|^2$ and the wave function will immediately collapse to the corresponding eigenfunction $|\chi_m\rangle$. Suppose that we do the experiment and find the result $\mu_{17}$. Now the wave function collapses again, to

$$|\phi_6\rangle \longrightarrow |\chi_{17}\rangle.$$

Let's say we decide to go back and measure the original observable $\hat{A}$. It wasn't so long ago that we measured it and found the result $\lambda_6$. But now, having measured $\hat{M}$, there's no guarantee that we'll get $\lambda_6$ again! Instead, we need to go through the same process and expand our wave function

$$|\chi_{17}\rangle = \sum_n \gamma_n |\phi_n\rangle.$$

The probability that we get the result $\lambda_6$ again is $|\gamma_6|^2$. But now it's just one among many options. There is no reason to have $|\gamma_6|^2 = 1$.

There are a number of different ways to explain this. First, it's clear that the measurement of a quantum system is never innocent. You can't just take a small peek and walk away pretending that you've not done anything. Instead, any measurement of a quantum system necessarily disturbs the state.

Moreover, if the state originally had a specific value for one observable $A$ and you measure a different observable $M$, then you destroy the original property of the state. It's tempting to say that there's no way to know the values of both $A$ and $M$ at the same time. But that's not what the mathematics is telling us. Instead, the quantum particle can't have specific values of $A$ and $M$ at the same time. Indeed, most of the time it doesn't have a specific value for either, since its wave function is a superposition of eigenstates. But, providing the eigenstates of the two operators don't coincide, if the quantum state takes a definite value for one observable, then it cannot for the other. We'll quantify this idea later where we introduce the Heisenberg uncertainty relations.

### Expectation values
So far, we have seen that all that quantum mechanics teaches us about the quantum state is the probability distribution associated with a particular observable. However, probability distributions can sometimes be rather complex and often they can obscure understanding. Some problems can be simplified by introducing the quantities that describe macroscopic properties of probability distributions.

The first quantity that we define to characterise probability distributions is the expectation value. We've seen earlier that if we have a very large number of copies of the system, then quantum mechanics tells us the exact fraction of measurements that will give a particular outcome. In this context, *the expectation value tells us the average value of all these measurement outcomes*.

If we take a normalised state $|\psi\rangle$, and measure the observable associated to the operator $\hat{A}$, the eigenstates and eigenvalues are given by

$$\hat{A}|\phi_n\rangle = \lambda_n|\phi_n\rangle. \tag{3.7}$$

As we've seen, if we expand the original state in orthonormal eigenfunctions

$$|\psi\rangle = \sum_n \alpha_n |\phi_n\rangle, \tag{3.8}$$

then the probability that we measure $\lambda_n$ is $P(\lambda_n) = |\alpha_n|^2$. This means that if we have many systems, all in the same state $|\psi\rangle$, and perform the same measurement on each, then the results will differ but the average will be

$$\langle \hat{A} \rangle_\psi = \sum_n \lambda_n P(\lambda_n) = \sum_n \lambda_n |\langle \phi_n | \psi \rangle|^2 = \sum_n \lambda_n |\alpha_n|^2. \tag{3.9}$$

Note the little subscript on the angular brackets, reminding us that the average value depends on the state of the system. We call this average the expectation value. It has a nice expression in terms of the inner product. For a normalised wave function $|\psi\rangle$, the expectation value can be written as

$$\langle \hat{A} \rangle_\psi = \langle \psi | \hat{A} | \psi \rangle = \int \psi^*(\mathbf{r}) \hat{A} \psi(\mathbf{r}) \mathrm{d}^3\mathbf{r}. \tag{3.10}$$

If $|\psi\rangle$ is un-normalised, this should be replaced by

$$\langle \hat{A} \rangle_\psi = \frac{\langle \psi | \hat{A} | \psi \rangle}{\langle \psi | \psi \rangle}. \tag{3.11}$$

To prove this, we can start with a normalised wave function and work backwards:

$$\begin{aligned}
\int \psi^*(\mathbf{r}) \hat{A} \psi(\mathbf{r}) \mathrm{d}^3\mathbf{r} &= \int \left( \sum_n \alpha_n^* \phi_n^*(\mathbf{r}) \right) \hat{A} \left( \sum_m \alpha_m \phi_m(\mathbf{r}) \right) \mathrm{d}^3\mathbf{r} \\
&= \sum_n \sum_m \int \left( \alpha_n^* \phi_n^*(\mathbf{r}) \right) \hat{A} \left( \alpha_m \phi_m(\mathbf{r}) \right) \mathrm{d}^3\mathbf{r} \\
&= \sum_n \sum_m \int \alpha_n^* \alpha_m \phi_n^*(\mathbf{r}) \underbrace{\left( \hat{A} \phi_m(\mathbf{r}) \right)}_{\lambda_m \phi_m(\mathbf{r})} \mathrm{d}^3\mathbf{r} \\
&= \sum_n \sum_m \alpha_n^* \alpha_m \lambda_m \underbrace{\int \phi_n^*(\mathbf{r}) \phi_m(\mathbf{r}) \mathrm{d}^3\mathbf{r}}_{\delta_{nm}} \\
&= \sum_n |\alpha_n|^2 \lambda_n.
\end{aligned}$$

---

## 3.4 Interpretations of quantum mechanics

As [David Tong](http://www.damtp.cam.ac.uk/user/tong/quantum.html) has said:

> ‘Finally, before we proceed, I want to point out that a much better name for the title of this section would be ‘Interpretations of Classical Mechanics'. At the fundamental level, the world is quantum and probabilistic. Yet, from this emerges the classical world with its deterministic laws of physics. If there's a question to answer at all, it's how the latter arises from the former. If, instead, you're looking for an explanation of quantum behaviour in terms of your prejudiced, classical worldview then you've got it backwards. That's like turning to botany in the hope that it will help you understand the properties of quarks.'

The statistical interpretation introduces a kind of indeterminacy into quantum mechanics, for even if you know everything the theory has to tell you about the particle – its wave function – still you cannot predict with certainty the outcome of a simple experiment to measure its position – all quantum mechanics has to offer is statistical information about the possible results. This indeterminacy has been profoundly disturbing to physicists and philosophers alike, and it is natural to wonder whether it is a fact of nature, or a defect in the theory.

Suppose you measure the position of the particle, and you find it to be, say, at point C. Question: Where was the particle just before you made the measurement? There are three plausible answers to this question, and they serve to characterise the main schools of thought regarding quantum indeterminacy:

1. **The realist position:** The particle was at C. This certainly seems reasonable, and it is the response Einstein advocated. Note, however, that if this is true then quantum mechanics is an incomplete theory, since the particle really was at C, and yet quantum mechanics was unable to tell us so. To the realist, indeterminacy is not a fact of nature, but a reflection of our ignorance. As d’Espagnat put it, ‘the position of the particle was never indeterminate, but was merely unknown to the experimenter'. Evidently $|\psi\rangle$ is not the whole story – some additional information (known as a hidden variable) is needed to provide a complete description of the particle.
2. **The orthodox position:** The particle wasn't really anywhere. It was the act of measurement that forced it to ‘take a stand' (though how and why it decided on the point C we dare not ask). Jordan said it most starkly: ‘Observations not only disturb what is to be measured, they produce it … We compel [the particle] to assume a definite position'. This view (the so-called Copenhagen interpretation) is associated with Bohr (1958) and his followers. Among physicists it has always been the most widely accepted position. Note, however, that if it is correct there is something very peculiar about the act of measurement – something that almost a century of debate has done precious little to illuminate.
3. **The agnostic position:** Refuse to answer. This is not quite as silly as it sounds – after all, what sense can there be in making assertions about the status of a particle before a measurement, when the only way of knowing whether you were right is precisely to make a measurement, in which case what you get is no longer ‘before the measurement'? It is metaphysics (in the pejorative sense of the word) to worry about something that cannot, by its nature, be tested. Pauli said: ‘One should no more rack one's brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle'. For decades this was the ‘fall-back' position of most physicists: they'd try to sell you the orthodox answer, but if you were persistent they'd retreat to the agnostic response, and terminate the conversation.

---

## Summary

Well done! You have now reached the end of this week’s Study – Week 3: Probabilistic nature of the measurement in Quantum Mechanics.

In this section, we explored the measurement problem in quantum mechanics, including the probabilistic nature of the outcome of the measurement. We discussed the various interpretations of quantum mechanics and how they address the measurement problem and we guided you through the three postulates of quantum mechanics that relate to measurement.

---

## References

1. D. Tong. *Quantum Mechanics lecture notes*. University of Cambridge, 2017. [Online] Available at: [http://www.damtp.cam.ac.uk/user/tong/quantum.html](http://www.damtp.cam.ac.uk/user/tong/quantum.html) [accessed 24 Jan 2023].
2. Jammer, M. *The Philosophy of Quantum Mechanics*. New York: Wiley, 1974. p. 151.
3. Heisenberg, W. *Physics and Philosophy: The Revolution in Modern Science*. London, England: Prometheus Books, 1958.
4. Bohr, N. *Atomic Physics and Human Knowledge*. New York: Wiley, 1958.
5. Bohr, N. *Atomic Theory and the Description of Nature*. Cambridge: Cambridge University Press, 1934.
6. Pauli, W. *General Principles of Quantum Mechanics*. Berlin: Springer-Verlag, 1980.