# Week 5: Quantum harmonic oscillator
## Intro
This week we will introduce you to the harmonic oscillator. The harmonic oscillator isn’t a particular object like a hydrogen atom or a quark. It’s really a mathematical framework for understanding a huge number of phenomena and is important to all branches of physics. It provides a useful model for a variety of vibrational phenomena that are encountered, for instance, in classical mechanics, electrodynamics, statistical mechanics, solid state, atomic, nuclear and particle physics. In the quantum world, it allows us to study properties of atoms in solids or the behaviour of light. But there is another very important reason why the quantum harmonic oscillator is so important: it is one of only a handful of problems that we know how to solve exactly. It serves as an invaluable tool to illustrate the basic concepts and the formalism in quantum mechanics.

By the end of this week, you will be able to:

describe the critical differences between the classic and the quantum harmonic oscillator
use ladder operators in the context of the quantum harmonic oscillator
solve eigenvalue problems to obtain energy values and states of the quantum harmonic oscillator.


## Explore
To start your learning this week, complete the following preparation task. This is for you to self-check what you might already know about this week’s topic. The task might vary from week to week.

This week’s task is:
To gain an intuitive understanding of the harmonic oscillator. Consider first the classical description.

Read the following sections from Quantum Mechanics: The Theoretical Minimum [1]Links to an external site.:
Lecture 10 – Section 10.1 to 10.7 (6 pages)
Read Chapter 5: The Harmonic Oscillator and the Rigid Rotor – Sections 5.1 to 5.5 [2]Links to an external site..
References
[1] Susskind, L. and Friedman, A. Quantum Mechanics: The Theoretical Minimum. London: Penguin, 2014.
[2] LibreTexts Chemistry. 5: The Harmonic Oscillator and the Rigid Rotor, 2022. [Online] Available at: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_(LibreTexts)/05%3A_The_Harmonic_Oscillator_and_the_Rigid_Rotor [accessed 10 March 2023]

## Apply
### Week 5: Quantum harmonic oscillator: Task

As part of your learning this week, you will now take part in the following task. The task should include your response to your fellow students’ posts that will be posted on the discussion board.
*The task:*

Make sure you [follow the guidance on the expected way of working in ‘ Six steps to problem solving: How to gain marks’ on the Quantum Technology Resources page in the SOSSS](https://canvas.sussex.ac.uk/courses/41954/pages/week-5-quantum-harmonic-oscillator-task).

Model answers will be provided. Solving these problems will help you when you start developing your portfolio.

### Problem 1

The ground state of quantum harmonic oscillator of mass $m$ and angular frequency $\omega$ is

$$\psi_0(x,t) = A \exp\left(-\frac{m\omega}{2\hbar}x^2 - i\omega t\right),$$

where $A$ is a constant. Show that $\psi_0(x,t)$ is a solution of the Schrödinger equation

$$\hat{H}|\psi_0(x,t)\rangle = E|\psi_0(x,t)\rangle, \tag{1}$$

where the Hamiltonian $\hat{H}$ is that of quantum harmonic oscillator, i.e.,

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2,$$

and the energy of the ground state is $E = \hbar\omega / 2$.

---

### Problem 2

The famous Heisenberg uncertainty for position and momentum is given by

$$\Delta x \Delta p \ge \frac{\hbar}{2}. \tag{2}$$

In this problem, we will calculate explicitly the uncertainty $\Delta x \Delta p$ of the quantum harmonic oscillator ground state $\psi_0(x,t) = A \exp\left(-\frac{m\omega}{2\hbar}x^2 - i\omega t\right)$ (the same wave function from the previous question).

1. Find the normalisation constant $A$.
2. The uncertainty $\Delta x$ of an observable $x$ is its standard deviation given by the following expression $\Delta x \equiv \sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$, where $\langle x^2 \rangle$ is the expectation value of $x$-squared, and $\langle x \rangle^2$ is the expectation value squared of $x$. Calculate $\langle x^2 \rangle$ and $\langle x \rangle^2$, and find the uncertainty $\Delta x$.
3. Using the similar strategy as in (b), find the uncertainty in momentum $\Delta p$.
4. Compare the product $\Delta x \Delta p$ to the Heisenberg's uncertainty relation (Eq. (2)). What can you tell about the uncertainty of the harmonic oscillator ground state?

---

### Hints

#### Problem 1: Hint

*Hint: Write $\hat{H}$ in the position representation and substitute $\psi_0(x,t)$ into the Eq. (1).*

#### Problem 2: Hints

*Hints:*

- You will greatly simplify the calculations if you perform the following change of variables:

$$x = \sqrt{\frac{\hbar}{m\omega}}\xi$$

$$\mathrm{d}x = \sqrt{\frac{\hbar}{m\omega}}\mathrm{d}\xi$$

- Integrals

$$\int_{-\infty}^{+\infty} e^{-ax^2} \mathrm{d}x = \sqrt{\frac{\pi}{a}}$$

$$\int_{-\infty}^{+\infty} x^2 e^{-ax^2} \mathrm{d}x = \frac{\sqrt{\pi}}{2a^{3/2}}$$

For an odd function, the integral over a symmetric interval equals zero, i.e.,

$$\int_{-u}^{+u} f_{\text{odd}}(x) \mathrm{d}x = 0.$$
---
Model answers will be provided. On Wednesday this week, a hint will be posted on the discussion board to help you solve the problems for this task. Solving these problems will help you when you start developing your portfolio.

Please use the following button to go to the Week 5 Task discussion board to post your response. Once you have contributed to the discussion board, you will be able to see the responses of others. Discuss the solutions and ask questions to help each other. The tutor will provide further feedback/help if needed.

## Consolidate
#### Week 5: Quantum harmonic oscillator: Independent study

This is your opportunity for independent research into the weekly topic. The task might vary from week to week.

Having had an opportunity to work collaboratively on solving problems with your peers, your independent study task is to:

These problems form part of your Assessment 2: Portfolio. There is an individual Portfolio discussion board that you can use throughout the module to develop your Portfolio. Any work you post there will be visible to your tutor.

You are encouraged to develop these problems throughout the module until the assessment due date. When you are ready to submit your Portfolio, you will only be allowed to submit one file. If you have multiple elements, ensure to condense your files into a single document.

---
### Problem 1
Consider a system whose wave function at time $t = 0$ is given by

$$|\psi(x,0)\rangle = \frac{5}{\sqrt{50}} |\phi_0(x)\rangle + \frac{4}{\sqrt{50}} |\phi_1(x)\rangle + \frac{3}{\sqrt{50}} |\phi_2(x)\rangle,$$

where $|\phi_n(x)\rangle$ is the wave function of the $n^{\text{th}}$ excited state for a harmonic oscillator of energy $E_n = \hbar\omega \left(n + \frac{1}{2}\right)$.

1. Find the average energy of this system.
2. Find the state $|\psi(x,t)\rangle$ at a later time $t$ and the average value of the energy; compare the result with the value obtained in (a).  
   *Hint: the eigenvalue equation for the time-evolution operator is $\hat{U} |\phi_n(x)\rangle \equiv e^{-i\hat{H}t/\hbar} |\phi_n(x)\rangle = e^{-iE_n t/\hbar} |\phi_n(x)\rangle$.*
3. Find the expectation value of the operator $\hat{x}$ with respect to the state $|\psi(x,t)\rangle$ (i.e., find $\langle \psi(x,t) | \hat{x} | \psi(x,t) \rangle$).  
   *Hint: Use $\hat{x} = \sqrt{\frac{\hbar}{2m\omega}} (\hat{a}^\dagger + \hat{a})$.*
---
### Problem 2
Calculate the expectation value of the momentum for a harmonic oscillator prepared in a state which is a superposition of two number states,

$$|\psi\rangle = \frac{1}{\sqrt{2}} (|\psi_1\rangle - i|\psi_2\rangle).$$

---
### Week 5 Quiz: Checkpoint

As part of your learning this week, complete the following quiz. This week's content has prepared you to be able to answer the quiz questions. If the quiz highlights that there are topics you need to repeat, please go back and review them on the Study page.

---
#### Question 1 (1 pt)
What are the ladder operators in the quantum harmonic oscillator?

- [ ] Operators that raise and lower the potential energy.
- [ ] Operators that create and annihilate quanta of energy.
- [ ] Operators that generate angular momentum.
- [ ] Operators that commute with the Hamiltonian.
---
#### Question 2 (1 pt)

What is the commutation relation between the ladder operators in the quantum harmonic oscillator?

- [ ] $[\hat{a}, \hat{a}^\dagger] = 0$
- [ ] $[\hat{a}, \hat{a}^\dagger] = 1$
- [ ] $[\hat{a}, \hat{a}^\dagger] = \hbar$
- [ ] $[\hat{a}, \hat{a}^\dagger] = i\hbar$
---
#### Question 3 (1 pt)
What is the number operator in the quantum harmonic oscillator?

- [ ] An operator that counts the total number of particles.
- [ ] An operator that determines the position of the particle.
- [ ] An operator that measures the momentum of the particle.
- [ ] An operator that measures the total energy of the system.
---
#### Question 4 (1 pt)

What are the eigenvalues of the number operator in the quantum harmonic oscillator?

- [ ] Continuous spectrum
- [ ] Positive integers
- [ ] Complex numbers
- [ ] Negative integers
---
#### Question 5 (1 pt)

What is the ground state energy of the quantum harmonic oscillator?

- [ ] Zero
- [ ] $\hbar\omega$
- [ ] $\frac{\hbar\omega}{2}$
- [ ] $2\hbar\omega$
---
#### Question 6 (1 pt)

What is the energy spacing between adjacent energy levels in the quantum harmonic oscillator?

- [ ] $\hbar\omega$
- [ ] $2\hbar\omega$
- [ ] $\frac{\hbar\omega}{2}$
- [ ] $3\hbar\omega$
---
#### Question 7 (1 pt)

What is the role of ladder operators in the quantum harmonic oscillator?

- [ ] They determine the energy eigenvalues.
- [ ] They diagonalise the Hamiltonian operator.
- [ ] They generate new energy eigenstates.
- [ ] They commute with all other operator.
---
#### Question 8 (1 pt)

What is the role of the zero-point energy in the quantum harmonic oscillator?

- [ ] It represents the lowest possible energy of the system.
- [ ] It determines the spacing between energy levels.
- [ ] It contributes to the total energy of the system.
- [ ] It is equal to the kinetic energy of the system.
---
#### Question 9 (1 pt)

What is the ground state wavefunction of the quantum harmonic oscillator?

- [ ] Plane wave
- [ ] Gaussian function
- [ ] Spherical harmonic
- [ ] Trigonometric function
---
#### Question 10 (1 pt)

What happens to the energy levels of the quantum harmonic oscillator as the frequency increases?

- [ ] The energy levels become denser.
- [ ] The energy levels move closer to zero.
- [ ] The energy levels move further apart.
- [ ] The energy levels remain the same.