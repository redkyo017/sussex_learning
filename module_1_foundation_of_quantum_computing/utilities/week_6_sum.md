This week, we learn about quantum computing’s remarkable power to efficiently factorise integers; which is not possible with classical computers, by any known means. We will see how this is achieved by the extraction of eigenvalue information from a unitary operator via phase kicks. This process uses procedures which nominally compute classical functions reversibly, but does so in a way that is impossible for a classical computer.

By the end of this week, you will be able to:

- describe the chain of problem reductions that would allow a large enough quantum computer to crack the RSA cryptosystem
- explain the order finding problem in general terms
- explain the high-level intuition behind how order finding relates to phase estimation
- describe the ways in which we generalise phase estimation in order to be able to solve order finding.

#### How to approach this week’s studies

Much of this week’s Study material involves more than a little technical detail. You may benefit from skimming much of the Study material that follows, spending more time on one or two aspects which you find more interesting afterwards.

#### Framing this week’s studies:

This week’s Study is a presentation of the following problems, with a chain of connections between them:

RSA → Integer factorisation → ‘Order finding’ → Phase estimation.

We try to present each of these connections (or ‘problem reductions’ as they are called in computer science), in a way that could be understood in detail with enough time and to provide intuitions for them.

- Sections 6.1 and 6.2 consist entirely of motivation, intuitions, number theory and classical algorithms. They are there essentially to motivate the way that quantum computers could use phase estimation to solve the ‘order finding’ problem, but you may read these in more detail if you wish: they are provided only for the sake of completeness.
- Section 6.3 generalises what we have already seen about phase estimation from Week 4, to solve the ‘order finding’ problem – a problem that we do not know how to solve efficiently by classical means, which would allow you to solve the integer factorisation problem.

What you should aim to learn this week is: what these problems are, a high-level understanding of how we can reduce from one problem to the next, and the ways in which we elaborate on phase estimation to solve the order finding problem.

### Interactive Optional Resource
**Fourier making waves simulation**
- https://phet.colorado.edu/sims/html/fourier-making-waves/latest/fourier-making-waves_all.html

### Week 6: Additional resources discussion board
Discussion board task instructions

Complete the task, then share your findings and reflections with peers via the discussion board.

The task:
- Identify which of the simulations you found most useful/ insightful? 
    - Bloch sphere simulatorLinks to an external site.: https://bloch.kherb.io/
    - Quantum measurement simulationLinks to an external site.: https://phet.colorado.edu/sims/html/quantum-measurement/latest/quantum-measurement_all.html
    - Fourier making waves simulationLinks to an external site.: https://phet.colorado.edu/sims/html/fourier-making-waves/latest/fourier-making-waves_all.html
- Post your thoughts on the Task discussion board.

Please read and reply to your fellow learners to encourage discussions and debates. Think of the following questions to establish best practice: 
- What is it that you particularly liked about the chosen activity? 
- Are there any things you can think of that would improve the other activities? 
- Can you create an idea for another simulation that would be useful? 