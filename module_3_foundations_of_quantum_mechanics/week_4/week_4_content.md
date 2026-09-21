# Week 4: Schrödinger equation
## Intro
So far, we have presented the formalism and basic postulates of quantum mechanics, focusing on how the system is depicted at a given time. The last postulate, which we will cover this week, specifies how this picture changes with time. We are going to explore a few simple examples of the Schrödinger equation that governs the time evolution of the wave function. The simplicity will not prevent us from establishing important results unique to quantum mechanics. Rather, the aim is to preclude mathematical distractions and allow us to appreciate the substance and implications of quantum mechanics.

By the end of this week, you will be able to:

solve the Schrödinger equation for simple choices of potential
interpret the meaning behind the results of the Schrödinger equation.


## Explore
To start your learning this week, complete the following preparation task. This is for you to self-check what you might already know about this week’s topic. The task might vary from week to week.

This week’s task is:
Read ‘What does the new double-slit experiment actually show?’ [1].Download Read ‘What does the new double-slit experiment actually show?’ [1].
Watch the video Double Slit Experiment explained! by Jim Al-Khalili [2]Links to an external site..
References
[1] Francis, M. What does the new double-slit experiment actually show? Scientific American, 2011. [Online] Available at: https://blogs.scientificamerican.com/guest-blog/what-does-the-new-double-slit-experiment-actually-show/ [accessed 17 February 2023].
[2] The Royal Institution. Double Slit Experiment explained! by Jim Al-Khalili (n.d.) [Online video] Available at: https://www.youtube.com/watch?v=A9tKncAdlHQ [accessed 17 February 2023].

## Apply
### Week 4: Schrödinger equation: Task

As part of your learning this week, you will now take part in the following task. The task should include your response to your fellow students’ posts that will be posted on the discussion board. This task is likely to take approximately 4–6 hours.

### Task 1:
1. solve the two Week 4 Task problems provided.

Make sure you [follow the guidance on the expected way of working in ‘Six steps to problem solving: How to gain marks’ on the Quantum Technology Resources page in the SOSSS](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-task).

#### Problem 1

A system is initially in the state

$$|\psi_0\rangle = \frac{1}{\sqrt{10}} \left[ 2 |\varphi_1\rangle + \sqrt{2} |\varphi_2\rangle + \sqrt{3} |\varphi_3\rangle + |\varphi_4\rangle \right],$$

where the states $|\varphi_n\rangle$ (for $n = 1, 2, 3, 4$) are eigenstates of the Hamiltonian $\hat{H}$ with eigenvalues given by

$$\hat{H} |\varphi_n\rangle = (2n - 1) E_0 |\varphi_n\rangle.$$

Thus, the energy eigenvalues are $E_1 = E_0$, $E_2 = 3E_0$, $E_3 = 5E_0$, $E_4 = 7E_0$.

a. If an energy measurement is performed on the system in the state $|\psi_0\rangle$, what energy values will be obtained and with what probabilities?

b. Consider an operator $\hat{A}$ defined by

$$\hat{A} |\varphi_n\rangle = (n + 2) a_0 |\varphi_n\rangle.$$

If a measurement of $A$ is performed on the system in the state $|\psi_0\rangle$, what values will be obtained and with what probabilities?

c. Suppose that an energy measurement yields $3E_0$. If a measurement of $A$ is performed immediately afterwards, what value will be obtained?

#### Problem 2

a. Find the hermitian conjugates of $x$, $i$, and $\mathrm{d}/\mathrm{d}x$.

b. Show that $(\hat{Q}\hat{R})^\dagger = \hat{R}^\dagger \hat{Q}^\dagger$ (note the reversed order), $(\hat{Q} + \hat{R})^\dagger = \hat{Q}^\dagger + \hat{R}^\dagger$ and $(c\hat{Q})^\dagger = c^* \hat{Q}^\dagger$.

---

Model answers will be provided. On Wednesday this week, a hint will be posted on the discussion board to help you solve the problems for this task. Solving these problems will help you when you start developing your portfolio.

Please use the following button to go to the Week 4 Task 1 discussion board for this task to post your response. Discuss the solutions and ask questions to help each other. The tutor will provide further feedback/help if needed.

### Task 2:

- **Discuss:** Due to the non-intuitive nature of quantum mechanics, misconceptions are not rare. Identify some of the most common misconceptions and discuss why these occur.

Please use the following button to go to the Week 4 Task 2 discussion board to post your response. Once you have contributed to the discussion board, you will be able to see the responses of others. Discuss the solutions and ask questions to help each other. The tutor will provide further feedback/help if needed.

[GO TO WEEK 4 TASK 1 DISCUSSION BOARD](https://canvas.sussex.ac.uk/courses/41954/pages/week-4-schrodinger-equation-task)

## Consolidate
#### Week 4: Schrödinger equation: Independent study
This is your opportunity for independent research into the weekly topic. The task might vary from week to week.
Having had an opportunity to work collaboratively on solving problems with your peers, your independent study task is to:

- solve the Week 4 Portfolio problems provided.

These problems form part of your Assessment 2: Portfolio. There is an individual Portfolio discussion board that you can use throughout the module to develop your Portfolio. Any work you post there will be visible to your tutor.

You are encouraged to develop these problems throughout the module until the assessment due date. When you are ready to submit your Portfolio, you will only be allowed to submit one file. If you have multiple elements, ensure to condense your files into a single document.

Make sure you [follow the guidance on the expected way of working in ‘Six steps to problem solving: How to gain marks’ on the Quantum Technology Resources page in the SOSSS](https://canvas.sussex.ac.uk/courses/10962/pages/quantum-technology-resources-1#sect2).

#### Problem 1

Consider a system whose state is given in terms of an orthonormal set of three vectors: $|\phi_1\rangle$, $|\phi_2\rangle$, $|\phi_3\rangle$ as

$$|\psi\rangle = \frac{\sqrt{3}}{3} |\phi_1\rangle + \frac{2}{3} |\phi_2\rangle + \frac{\sqrt{2}}{3} |\phi_3\rangle.$$

a. Verify that $|\psi\rangle$ is normalised. Then, calculate the probability of finding the system in any one of the states $|\phi_1\rangle$, $|\phi_2\rangle$ and $|\phi_3\rangle$. Verify that the total probability is equal to one.

b. Consider now an ensemble of 810 identical systems, each one of them in the state $\psi$. If measurements are done on all of them, how many systems will be found in each of the states $|\phi_1\rangle$, $|\phi_2\rangle$ and $|\phi_3\rangle$.

---

#### Problem 2

a. Show that the sum of two hermitian operators is hermitian.

b. Suppose $\hat{Q}$ is hermitian, and $\alpha$ is a complex number. Under what condition (on $\alpha$) is $\alpha\hat{Q}$ hermitian?

c. When is the product of two hermitian operators hermitian?

d. Show that the Hamiltonian operator $\hat{H} = -\frac{\hbar^2}{2m} \frac{\mathrm{d}^2}{\mathrm{d}x^2} + V(x)$ is hermitian.

---

### Week 4 Quiz: Checkpoint
#### Quiz instructions
As part of your learning this week, complete the following quiz. This week's content has prepared you to be able to answer the quiz questions. If the quiz highlights that there are topics you need to repeat, please go back and review them on the Study page.

- This quiz has 6 questions.
#### Question 1 (1 pts)

What is the role of the Hamiltonian operator in the Schrödinger equation?

- [ ] (a) It describes the position of the particle.
- [ ] (b) It describes the momentum of the particle.
- [ ] (c) It describes the energy of the particle.
- [ ] (d) It describes the angular momentum of the particle.
---
#### Question 2 (1 pts)

What is the time-evolution operator in the Schrödinger equation?

- [ ] (a) A mathematical operator that describes the position of the particle.
- [ ] (b) A mathematical operator that describes the momentum of the particle.
- [ ] (c) A mathematical operator that describes the energy of the particle.
- [ ] (d) A mathematical operator that describes how the wave function changes with time.
---
#### Question 3 (1 pts)

Which of the following statements is *true* in quantum mechanics?

- [ ] (a) Unlike position, time is not an observable.
- [ ] (b) There is no Hermitian operator whose eigenvalues were the time of the system.
- [ ] (c) Time appears only as a parameter, not as a measurable quantity.
- [ ] (d) All of the above.
---
#### Question 4 (1 pts)

What is the significance of the normalisation condition of the wave function?

- [ ] (a) It ensures that the wave function is complex.
- [ ] (b) It ensures that the wave function is continuous.
- [ ] (c) It ensures that the wave function is finite.
- [ ] (d) It ensures that the probability of finding the particle is equal to 1.
---
#### Question 5 (1 pts)

What is the energy of a quantum particle in a square potential?

- [ ] (a) It is infinite.
- [ ] (b) It is zero.
- [ ] (c) It depends on the momentum of the particle.
- [ ] (d) It is quantised.
---
#### Question 6 (1 pts)

What is the probability density of finding a quantum particle in a square potential when the particle is in its ground state?

- [ ] (a) It is a constant.
- [ ] (b) It is zero.
- [ ] (c) It is maximum at the centre of the potential.
- [ ] (d) It depends on the energy of the particle.

---

### Week 4 wrap up for assigment:
This week, you are required to submit an assessment task that you have worked on. Please use the following button to go to the submission point to submit your work for this assessment: Assessment 1: Problem set.

Remember to check the requirements for this assessment task on the assignments page.

If you have any questions about your assessment, please post them to the Assessment 1 questions discussion board for your tutor and peers to reply to or email your Module Leader.

Please note:

All due dates and times are scheduled in UK time.
You will only be allowed to submit one file; so if you have multiple elements, you will need to condense them.
You will be able to use this point to submit work while it is open for submission and review feedback once it has been released to you by your tutor.
For support in submitting your work, please see the assessment submission guide . If you have any problems submitting your work, please send it within the deadline to your Student Success Advisor. Do not send it to your tutor.