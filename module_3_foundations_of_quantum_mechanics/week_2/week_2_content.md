# Week 2: The wave functions, operators and observables
## Intro
During Week 1 we gave a brief overview of the most important concepts in quantum mechanics. In Week 2 we will return to some of those concepts and discuss more profoundly their meaning and, where relevant, their implications for quantum technologies. You will learn about the formalism of quantum mechanics that is based on a number of postulates. These postulates represent the minimal set of assumptions needed to develop the theory of quantum mechanics. At the end of the week, you should be able to use those postulates to extract quantitative information about physical systems.

By the end of this week, you will be able to:

describe the state of a quantum system using mathematical language (vectors)
explain the link between observables and operators
perform vector operations using Dirac notation.

## Explore
To start your learning this week, complete the following preparation task. This is for you to self-check what you might already know about this week’s topic. The task might vary from week to week.
This week’s task is:
Read sections 4.1 to 4.3 of Postulates and Principles of Quantum MechanicsLinks to an external site. [1].
References
[1] LibreTexts Chemistry. Postulates and Principles of Quantum Mechanics, 2020 [Online]. Available at: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_(LibreTexts)/04%3A_Postulates_and_Principles_of_Quantum_Mechanics [accessed 10 March 2023].

## Apply
Week 2: The wave functions, operators and observables: Task
As part of your learning this week, you will now take part in the following task. The task should include your response to your fellow students’ posts that will be posted on the discussion board. This task is likely to take approximately 4–6 hours.

*The task:*
- solve the Week 2 Task problems provided.

Make sure you [follow the guidance on the expected way of working in ‘Six steps to problem solving: How to gain marks’ on the Quantum Technology Resources page in the SOSSS](https://canvas.sussex.ac.uk/courses/41954/pages/week-2-the-wave-functions-operators-and-observables-task).

---

#### Problem 1

Using the axioms for inner products:
1. linearity: $\langle C \mid \{ |A\rangle + |B\rangle \} = \langle C \mid A\rangle + \langle C \mid B\rangle$;
2. interchanging bras and kets corresponds to complex conjugation: $\langle B \mid A\rangle = \langle A \mid B\rangle^\star$,

1. prove $\{\langle A\mid + \langle B\mid\} \mid C \rangle = \langle A \mid C\rangle + \langle B \mid C\rangle$,
2. prove $\langle A \mid A\rangle$ is a real number.

---

#### Problem 2

1. Suppose that $f(x)$ and $g(x)$ are two eigenfunctions of an operator $\hat{Q}$ with the same eigenvalue $q$. Show that any linear combination of $f$ and $g$ is itself an eigenfunction of $\hat{Q}$ with eigenvalue $q$.
2. Check that $f(x) = \exp(x)$ and $g(x) = \exp(-x)$ are eigenfunctions of the operator $\mathrm{d}^2 / \mathrm{d}x^2$, with the same eigenvalue. Construct two linear combination of $f$ and $g$ that are orthogonal eigenfunctions on the interval $(-1, 1)$.

---

#### Problem 3

Which of the following functions make good wave functions for describing a particle moving in one dimension? Sketch the probability density for each of them and check whether it is normalisable. Determine the normalisation constant $C_n$ for those that are normalisable. (The parameters $\lambda_n$ are all *real* and *positive*).

1. $\psi_1(x) = \begin{cases} 0 & \text{for } x < 0, \\ C_1 \sin(\lambda_1 x) & \text{for } 0 \le x \le 2\pi/\lambda_1, \\ 0 & \text{for } x > 2\pi/\lambda_1. \end{cases}$
2. $\psi_2(x) = C_2 x + \lambda_2$ for all $x$.
3. $\psi_3(x) = C_3 \exp(\lambda_3 x^2)$ for all $x$.
4. $\psi_4(x) = C_4 \exp(-\lambda_4 |x|)$ for all $x$.

---

Model answers will be provided. Every Wednesday of the week, a hint will be posted on the weekly discussion board to help you solve the problems for each task. Solving these problems will help you when you start developing your portfolio.

Please use the [GO TO DISCUSSION BOARD](https://canvas.sussex.ac.uk/courses/41954/pages/week-2-the-wave-functions-operators-and-observables-task) button to go to the Week 2 Task discussion board to post your response. Once you have contributed to the discussion board, you will be able to see the responses of others. Discuss the solutions and ask questions to help each other. The tutor will provide further feedback/help if needed.

## Consolidate
#### Week 2: The wave functions, operators and observables: Independent study
This is your opportunity for independent research into the weekly topic. The task might vary from week to week.

Having had an opportunity to work collaboratively on solving problems with your peers, your independent study task is to:
- solve the Week 2 Portfolio problems provided.

These problems form part of your Assessment 2: Portfolio. There is an individual Portfolio discussion board that you can use throughout the module to develop your Portfolio. Any work you post there will be visible to your tutor.

You are encouraged to develop these problems throughout the module until the assessment due date. When you are ready to submit your Portfolio, you will only be allowed to submit one file. If you have multiple elements, ensure to condense your files into a single document.

Make sure you [follow the guidance on the expected way of working in ‘Six steps to problem solving: How to gain marks’ on the Quantum Technology Resources page in the SOSSS](https://canvas.sussex.ac.uk/courses/10962/pages/quantum-technology-resources-1#sect2).

#### Problem 1

At time $t = 0$ a particle is represented by the wave function

$$\psi(x, 0) = \begin{cases} 
A \left(\frac{x}{a}\right) & 0 \le x \le a, \\ 
A \frac{(b - x)}{(b - a)} & a \le x \le b, \\ 
0 & \text{otherwise}, 
\end{cases}$$

where $A$, $a$, and $b$ are positive real constants.

1. Normalise $\psi$ (that is, find $A$, in terms of $a$ and $b$).
2. Sketch $\psi(x, 0)$, as a function of $x$.
3. Where is the particle most likely to be found, at $t = 0$?
4. What is the probability of finding the particle to the left of $a$? Check your result in the limiting cases $b = a$ and $b = 2a$.
5. What is the expectation value of $x$?

#### Problem 2

In the concrete representation of bras and kets by row and column vectors, the inner product is defined in terms of components:

$$\langle B \mid A \rangle = (\beta_1^\star \; \beta_2^\star \; \beta_3^\star) \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{pmatrix} = \beta_1^\star \alpha_1 + \beta_2^\star \alpha_2 + \beta_3^\star \alpha_3.$$

The rule for inner products is essentially the same as for dot products: add the products of corresponding components of the vectors whose inner product is being calculated.

Show that the inner product $\langle B \mid A \rangle$, defined as above, satisfies all the axioms of inner products (conjugate symmetry, linearity in the second argument, and positive-definiteness).

---
### Quiz
## Quiz Instructions
As part of your learning this week, complete the following quiz. This week's content has prepared you to be able to answer the quiz questions. If the quiz highlights that there are topics you need to repeat, please go back and review them on the Study page.

#### Question 1
What is the total probability of finding the particle in space ?

Group of answer choices
- (a) Zero
- (b) Unity
- (c) Infinity
- (d) Double

---

#### Question 2
What is the value of the norm of the normalised wave function?

Group of answer choices
- (a) Infinite
- (b) Zero
- (c) Finite
- (d) Complex

---

#### Question 3
What is the square of the magnitude of the wave function called?

Group of answer choices
- (a) Current density
- (b) Probability density
- (c) Probability
- (d) Volume density

---

#### Question 4
The fundamental observables associated with the motion of a single quantum mechanical particle are:

Group of answer choices
- (a) E and P operators
- (b) x and E operators
- (c) L and P operators
- (d) x and P operators

---

#### Question 5
For the wave functions $\psi$ and $\phi$ and operator $\hat{A}$, what is the shorter notation of the integral $\int \phi^\star \hat{A} \psi \, dr$?

Group of answer choices
- (a) $\langle \phi \mid \psi \rangle$
- (b) $\langle \phi^\star \mid \hat{A} \psi \rangle$
- (c) $\langle \phi \mid \hat{A} \psi \rangle$
- (d) $\langle \hat{A} \phi \mid \psi \rangle$

---

#### Question 6
What is an eigenvalue called for which only one corresponding eigenfunction exists?

Group of answer choices
- (a) Non-degenerate
- (b) Degenerate
- (c) Discrete
- (d) Adjoint

---

#### Question 7
Which of the following statements about operators is incorrect?

Group of answer choices
- (a) Any number can be used as an operator.
- (b) Most operators in quantum mechanics are made up of multiplication and differentiations.
- (c) Operators act on the function written after them.
- (d) Operators can be moved around in an expression without altering the result.

---

#### Question 8
Which of these statements about the properties of operators consisting only of multiplication and differentiation is incorrect?

Group of answer choices
- (a) They all obey associativity.
- (b) They all commute.
- (c) All statements are correct.
- (d) They are all linear.

---

#### Question 9
What is the momentum operator (along $x$ direction)?

Group of answer choices
- (a) $-i\hbar \frac{\partial}{\partial x}$
- (b) $\hat{x}$
- (c) $-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}$
- (d) $-\frac{\hat{p}^2}{2m} + V(\hat{x})$

---

#### Question 10
Which of these statements about Hermitian operators is not correct?

Group of answer choices
- (a) All Hermitian operators represent observables.
- (b) The eigenvalues of a Hermitian operator are real.
- (c) All operators which represent observables are Hermitian.
- (d) The eigenfunctions of a Hermitian operator form a complete basis.

---

#### Question 11
Two eigenfunctions of Hermitian operator belonging to different eigenvalues are:

Group of answer choices
- (a) orthonormal.
- (b) normal.
- (c) orthogonal.
- (d) none of these eigenfunctions.