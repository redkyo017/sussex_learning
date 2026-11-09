# Week 6: Quantum computing: Study

## 6: Quantum computing
## Introduction
This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

### Introduction

The journey from the first room-filling computers less than a century ago to modern super-computing farms is an incredible success story in which the devices have become ever more powerful in their quantitative and qualitative capabilities in ways that were never imagined in the beginning [\[1\]](#sect9). The driver of this development has been a steady increase in the density of electronic elements on chips and circuit boards. This is based on an empirical exponential law of decreasing structure sizes with a halving time of only a few years, often dubbed as Moore’s law [\[2\]](#sect10). On such a pathway, it is natural to extrapolate to the size scales of the constituent, most basic, electronic elements. One finds that the regime governed by quantum physics is inevitably reached very soon if Moore’s law continues to hold as it has done for decades.

The realisation that quantum phenomena can be exploited rather than having to be avoided in computing is an ingenious concept that forms the basis of quantum computing. The core idea is that, in quantum systems, binary encoding of information in bits can now occur in so-called quantum bits, or qubits for short. While a bit is either on or off, set or not set, zero or one, a qubit can be in (infinitely) many states that contain both basis states to a varying degree. This is known as superposition. As a second key novelty in quantum computing, two qubits can be linked to each other in a peculiar way that is only possible in quantum physics, known as entanglement. These two properties, superposition and entanglement, together with a basic set of operations performed on one or two qubits, so-called quantum gates, are the fundamental ingredients of universal quantum computing [\[3\]](#sect11).

The interest in quantum computing started to grow quickly when its potential power became apparent through quantum algorithms that could exclusively be run on a quantum computer and would be able to solve tasks that a classical computer could not solve in a reasonable time. Key early examples concern database searches and cracking of encryption codes. Quantum computing is now expected to have an impact in many sectors across technologies ranging from the pharmaceutical industry to artificial intelligence.

Despite tremendous advances, the physical implementation of quantum computers remains difficult due to the fragility of quantum bits and fidelities of operations on them [\[4\]](#sect12). Quantum error correction will be a central tool that will enable the implementation of quantum algorithms with inevitably imperfect implementations. However, it will have a large overhead of the number of physical qubits needed in order to implement a smaller set of logical qubits on an actual quantum computer.

In the following section, we will cover qubits and quantum gates in more detail. For more information about these concepts, refer to the well-known and highly regarded text book on quantum computing and quantum information by Nielsen and Chuang [\[3\]](#sect11).

This week we will introduce quantum computing in more detail in terms of basic principles, arising opportunities, advances and challenges of implementations, and the current state of the art in this field of quantum technologies.

 The Study topics this week are: 

-   [6.1 The basics of qubits and quantum gates](#sect1)
-   [6.2 Simple algorithms to demonstrate the power of quantum computing](#sect2)
-   [6.3 Physical implementation platforms](#sect3)
-   [6.4 Core principles and significance of fundamental algorithms](#sect4)
-   [6.5 Limited fidelity of quantum state preparation](#sect5)
-   [6.6 Basic principles of quantum error correction](#sect6)
-   [6.7 An overview of physical implementation platforms of quantum computers](#sect7)
-   [6.8 Application areas of quantum computers](#sect8)

## 6.1 Qubits and quantum gates

At the heart of quantum computing are quantum bits (or qubits for short) and quantum gates.

**Qubits**  
A qubit is the fundamental building block of quantum computing. It is the quantum analogue of a classical bit, which can be either a 0 or a 1. In contrast, a qubit can be in a superposition of states, which means that it can be in a state that is a linear combination of the 0 and 1 states. Mathematically, a qubit can be written as

$$
\mid{\psi}\rangle = \alpha|0\rangle + \beta |1\rangle,
$$ 
(6.1)

where $\alpha$ and $\beta$ are complex numbers such that $|\alpha|^2 + |\beta|^2 = 1$, and $|0\rangle$ and $|1\rangle$ are orthonormal basis states.

**Bloch sphere**  
The Bloch sphere is a useful tool for visualising qubits. It is a three-dimensional sphere where the north pole represents $|0\rangle$ and the south pole represents $|1\rangle$. Any qubit state can be represented as a point on the surface of the sphere, with the distance from the centre representing the probability amplitude of the state.

**Quantum gates**  
A quantum gate is a unitary operator that operates on one or more qubits. It is the quantum analogue of a classical logic gate, which operates on classical bits [\[3\]](#sect11). Quantum gates are used to manipulate qubits and perform operations that are necessary for quantum algorithms. We will now explore some examples of simple gates acting as building blocks for the implementation of quantum algorithms. We will use the matrix and vector notation for this to clarify the concepts more sharply for those of you who are familiar with this type of notation. However, these basic principles should also become clear to those of you without a full grasp of the mathematical notation.

**Pauli gates**

Figure 6.1: The Bloch sphere representation of a qubit state. Adapted from Ketterer, 2016, p. 33 [\[39\]](#sect47).

Long description

The image shows a sphere drawn as a circle with the equator drawn as an ellipse (half solid line where visible and half as a dashed line where invisible). The centre of the sphere coincides with the origin of a rectilinear coordinate system with the axes labelled as x, y, z. Two basis quantum states in a two-level system are represented as dots on the two poles of the sphere. |0> at the North pole, |1> at the South Pole. Any possible superposition state can now be represented as a point on the surface of this so called Bloch sphere. As an example, a state labelled as 'v' is shown at a random position. This position can then be characterised through a unique polar angle \\theta and azimuthal angle \\phi, which are shown as an illustration in the graphic. Further more, specific equatorial states |+>,|-> are also indicated with their definition of superposition and their corresponding position on the Bloch Sphere.

The Pauli gates are a family of single-qubit gates that are named after the physicist Wolfgang Pauli. There are three Pauli gates: the Pauli-X gate, the Pauli-Y gate and the Pauli-Z gate [\[3\]](#sect11). They are defined as

$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},$ (6.2) 

$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},$ (6.3) 

$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$ (6.4)

The Pauli-X gate is a bit-flip gate, which means that it flips the state of a qubit from $|0\rangle$ to $|1\rangle$ and vice versa. The Pauli-Y gate is a bit-phase gate, which means that it introduces a phase shift between the $|0\rangle$ and $|1\rangle$ states. The Pauli-Z gate is a phase-flip gate, which means that it flips the sign of the $|1\rangle$ state.

**CNOT gate**  
The CNOT gate is a two-qubit gate that is essential for many quantum algorithms. It is also known as the controlled-NOT gate, as it performs a NOT operation on the target qubit if and only if the control qubit is in the $|1\rangle$ state. The CNOT gate is defined as

$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}.$ (6.5)

The CNOT gate can be used to create entangled states, which are a key feature of quantum computing. An entangled state is a state in which the qubits are correlated in such a way that the state of one qubit cannot be described independently of the other qubits.

**Hadamard gate**  
The Hadamard gate is another single-qubit gate that is widely used in quantum algorithms. It is defined as

$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$ (6.6)

The Hadamard gate transforms the $|0\rangle$ state to a superposition of $|0\rangle$ and $|1\rangle$, and the $|1\rangle$ state to a superposition of $|0\rangle$ and −$|1\rangle$. The Hadamard gate is used in many quantum algorithms, including the famous quantum Fourier transform [\[5\]](#sect13).

## 6.2 Simple algorithms

One of the key features of quantum computing is the ability to perform certain computations exponentially faster than any known classical algorithm. To illustrate this, we will explore a simple quantum algorithm (the Deutsch–Josza algorithm) and other examples.

**Deutsch–Josza algorithm**  
The Deutsch–Josza algorithm [\[6](#sect14), [7\]](#sect15) is a simple quantum algorithm that can determine whether a function $f:\{0,1\}^n\rightarrow\{0,1\}$ is constant or balanced by just one query to the function, where n is the number of bits in the input. A function is constant if it outputs the same value for all inputs, and it is balanced if it outputs a different value for exactly half of the inputs.

The classical version of the problem requires $2^{n-1}+1$ queries to determine whether a function is constant or balanced, but the Deutsch–Josza algorithm can solve the problem with just one query. The algorithm works as follows.

1.  Start with n+1 qubits in the $|0\rangle$ state: $|0\rangle$ $|0\rangle$...$|0\rangle$ $|1\rangle$.
2.  Apply a Hadamard gate to each qubit.
3.  Apply the function f to the n qubits and leave the last qubit unchanged.
4.  Apply a Hadamard gate to each qubit except the last one.
5.  Measure the first n qubits. If the result is $|0\rangle|0\rangle...|0\rangle$, then the function is constant. If the result is any other state, then the function is balanced.

The Deutsch–Josza algorithm has a 100% success rate and is exponentially faster than any known classical algorithm for the same problem.

**Other examples**  
There are many other simple quantum algorithms that can be used to demonstrate the power of quantum computing. One example is Grover's algorithm [\[8\]](#sect16), which can be used to search an unsorted database of N items in $\mathcal{O}(\sqrt{N})$ queries, whereas a classical algorithm requires $\mathcal{O}(N)$ queries. Another example is the quantum teleportation algorithm [\[9\]](#sect17), which allows two parties to share a quantum state without actually transmitting the state itself. 

These algorithms demonstrate the power of quantum computing and the potential for solving problems that are currently intractable with classical computers. Quantum computing is a rapidly growing field, and these algorithms are just the tip of the iceberg in terms of what can be achieved with quantum computers.

## 6.3 Physical implementation platforms

As discussed above, quantum computers rely on the use of qubits, which are **physical** systems that can represent quantum information. There are several platforms that can be used to implement qubits, each with its own advantages and disadvantages. We will now discuss some of the most promising platforms for qubit implementation and their physical properties.

**Superconducting qubits**  
Superconducting qubits are based on superconducting circuits that can store and manipulate quantum information [\[10\]](#sect18). These qubits are relatively easy to fabricate and can be integrated with classical electronic circuits, making them a promising platform for quantum computing. One of the key advantages of superconducting qubits is that they can be fabricated using standard semiconductor fabrication techniques, which enables large-scale manufacturing. However, these qubits require low temperatures (typically around 20 millikelvin) to operate, which can make them challenging to use in practical applications.

**Trapped ions**  
Trapped-ion qubits [\[11\]](#sect19) use lasers to trap ions in a vacuum chamber and manipulate their quantum states. These qubits have very long coherence times, which makes them a promising platform for quantum computing. Preparing and manipulating the quantum state of individual qubits and between two qubits with high fidelity is as important as maintaining and controlling the quantum states over many operation times, and this is only possible with long coherence times. In addition, trapped-ion qubits can be arranged in a linear array, which allows the implementation of quantum error correction codes. However, trapped-ion qubits require highly stable and precise optical set-ups, which can make them difficult to scale up.

**Topological qubits**  
Topological qubits are based on the principles of topological quantum field theory, which predicts the existence of quasiparticles known as anyons [\[12\]](#sect20). These anyons can be used to store and manipulate quantum information, and they are highly robust against environmental noise. One of the key advantages of topological qubits is their potential for fault tolerance, which would allow error correction without the need for active feedback. However, topological qubits are still in the experimental stage, and their implementation requires a high degree of control over the underlying physical system.

In summary, there are several promising platforms for qubit implementation, each with its own advantages and challenges.

-   Superconducting qubits are relatively easy to fabricate and integrate with classical electronic circuits.
-   Trapped-ion qubits have very long coherence times, but are more difficult to scale up.
-   Topological qubits have the potential for fault tolerance, but are still in the experimental stage.

As quantum computing continues to develop, it is likely that multiple qubit platforms will be used in combination to achieve the best possible performance.

## 6.4 Fundamental algorithms

The core of quantum computing is to use quantum mechanics to process information. This allows the development of new algorithms that can potentially solve problems faster than classical computers. Some of the most significant quantum algorithms are Shor's algorithm [\[13\]](#sect21) for factorising large numbers and the above-mentioned Grover's algorithm for searching unsorted databases. We will now explore the main principles and significance of these fundamental quantum computing algorithms, focusing primarily on Shor's algorithm.

As discussed above, at its core, quantum computing relies on the manipulation of qubits, which can exist in a superposition of states, unlike classical bits which can only exist in either a 0 or 1 state. The superposition of qubits allows quantum algorithms to perform multiple calculations simultaneously, which results in an exponential increase in speed compared with classical algorithms for certain problems, such as database searches, (periodic) pattern identification/recognition and, famously, the factorising of large numbers [\[13\]](#sect21), as we discuss now.

Shor's algorithm is one of the most famous quantum algorithms, as it solves the problem of factorising large numbers in polynomial time, a task that is believed to be computationally infeasible for classical computers. This is because all known classical solutions rely on algorithms whose execution time grows exponentially with the number of input bits or, equivalently, the size of the number to be factorised. The significance of factorising large numbers lies in its use in modern cryptography, specifically, in the Rivest–Shamir–Adleman (RSA) encryption scheme. If one can efficiently factorise large numbers, then they can break RSA encryption, which is used for secure online transactions, email encryption and other applications.

Shor's algorithm uses a combination of classical and quantum computing to factorise large numbers. It involves two major steps: first, the algorithm finds the period of a function; and second, it uses the period to factorise the number. The period-finding step is performed using quantum Fourier transforms, which exploit the superposition and entanglement properties of qubits to perform calculations faster than classical algorithms. The period-finding step can be performed efficiently on a quantum computer, but the second step, which involves classical computing, is computationally expensive.

The significance of Shor's algorithm lies in the fact that it demonstrates the potential of quantum computing to solve problems that are intractable for classical computers. By factorising large numbers efficiently, Shor's algorithm breaks RSA encryption, which is the backbone of secure communication in the digital age. This has significant implications for national security and data privacy, as it poses a threat to any information that is encrypted using RSA encryption.

Apart from Shor's algorithm, another important quantum algorithm is Grover's algorithm, which is used for searching unsorted databases. Grover's algorithm offers a quadratic speed-up over classical algorithms, which makes it faster for large databases. However, its practical applications are limited, as it requires the database to be represented by quantum states.

In conclusion, Shor's algorithm is a fundamental quantum algorithm that demonstrates the potential of quantum computing to solve problems that are intractable for classical computers. By factorising large numbers efficiently, Shor's algorithm breaks RSA encryption, which poses a threat to national security and data privacy. The significance of quantum computing lies in its potential to revolutionise various fields, from cryptography to drug discovery, by providing exponential speed-up over classical algorithms. As quantum computing continues to advance, it will be interesting to see how these fundamental algorithms are further developed and applied to real-world problems.

**Mathematical details of Shor's algorithm**  
Shor's algorithm is based on the principles of modular arithmetic and the quantum Fourier transform. Given a large composite number N, Shor's algorithm aims to find its prime factors.

The first step of Shor's algorithm involves selecting a random number a that is coprime with N. This can be done efficiently using classical algorithms. If a is not coprime with N, then its factors can be easily found using classical algorithms, and the problem is reduced to factorising smaller numbers. Once we have a coprime number a, we can define a function $f(x) = a^x\ mod \ N$.

The second step involves finding the period of the function $f(x)$. This is done using the quantum Fourier transform (QFT), which is a quantum analogue of the classical Fourier transform. The QFT exploits the superposition and entanglement properties of qubits to perform calculations faster than classical algorithms. The period of $f(x)$ is related to the frequency component of the Fourier transform, which can be determined using the QFT.

Once the period is found, the third step involves using it to factorise N. The period can be written as $r = 2^s \cdot r'$, where $r'$ is the non-trivial factor of N. If r is odd, then we can use another random a and repeat the process until we find an even r. If $a^{r/2} + 1 \equiv 0 \ mod\ N$, then we can use the factors $(a^{r/2} - 1)$ and $(a^{r/2} + 1)$ to factorise N.

The time complexity of Shor's algorithm is $O((\log N)^3)$ on a quantum computer, which is polynomial in the size of the input. In contrast, the best classical algorithms for factorising large numbers have an exponential time complexity, which makes them impractical for large inputs.

## 6.5 Fidelity

Any practical realisation of the potential of quantum computing requires precise control over the quantum states and their evolution, which is often limited by the presence of noise and decoherence. We now discuss the limitations of quantum state preparation and coherent evolution, and the challenges they pose for quantum computing.

One of the biggest challenges in building a quantum computer is achieving high **fidelity** in the preparation and manipulation of quantum states. Even small deviations from ideal behaviour can quickly lead to large errors, which makes the computation meaningless. This is due to the fundamental principles of quantum mechanics, where a quantum state can exist in a superposition of multiple states, and any measurement on the state will cause a collapse to one of the possible states with a probability determined by the state's coefficients.

The fidelity of a quantum state is a measure of how closely it matches the desired state. It can be affected by various factors, including decoherence, imperfect state preparation and limited control over the system. Decoherence is the process by which the quantum state interacts with its environment, which causes it to lose coherence and information. Imperfect state preparation can result from errors in qubit initialisation, readout or gate operations. Limited control over the system can arise from imprecise tuning of qubit frequencies, coupling strengths or gate timings.

The fidelity of quantum states has been a major focus of experimental efforts in various qubit platforms, including superconducting qubits, ion traps and silicon-based spin qubits [\[14\]](#sect22). Superconducting qubits have been a popular platform due to their high coherence times and scalability, and recent experiments have achieved fidelities of up to 99.9% for single qubit operations and 99.5% for two-qubit operations [\[15](#sect23), [16\]](#sect24). Ion traps have also demonstrated high fidelity operations, with fidelities of up to 99.99% achieved for single qubit gates and 99.9% for two-qubit gates [\[17\]](#sect25). Silicon-based spin qubits have shown promise for long coherence times and low error rates, with fidelities of up to 99.96% achieved for single qubit gates and 99.4% for two-qubit gates [\[18\]](#sect26).

In addition to achieving high fidelity in state preparation and manipulation, it is also important to maintain the coherence of the quantum state during the computation. Coherence time, also known as the decoherence time, is the time during which the quantum state remains coherent before losing its coherence owing to interaction with the environment. It is an important parameter for assessing the performance of a quantum system. Various techniques have been developed to extend coherence times, including dynamical decoupling, quantum error correction and topological protection.

Dynamical decoupling is a technique that involves applying a series of pulses to the qubits to periodically refocus the phase accumulation due to environmental interactions. This technique has been demonstrated to extend the coherence time of superconducting qubits to several hundred microseconds [\[19\]](#sect27). Quantum error correction is a more sophisticated technique that uses redundancy to protect the quantum state from errors. It requires a large number of physical qubits to implement, and its performance is limited by the achievable fidelity of the qubits and gates [\[20\]](#sect28). We will discuss this in more detail in the next section. Topological protection is a promising approach that exploits the topological properties of the quantum state to protect against errors. It has been proposed for various qubit platforms, including superconducting qubits and Majorana fermions [\[21](#sect29), [22\]](#sect30).

Despite the progress made in improving the fidelity of quantum state preparation and coherent evolution, current quantum hardware still falls short of the theoretical ideal. The level of fidelity achieved in different qubit platforms varies significantly and is often limited by different sources of noise and errors. For example, in superconducting qubits, the main sources of error include flux noise, charge noise and quasiparticle excitations, while in trapped ions, the main sources of error include laser intensity, frequency noise and motional heating [\[23\]](#sect31).

Quantitative measurements of the achieved fidelities in different qubit platforms have been reported in many studies. For example, recent experiments on superconducting qubits have achieved single-qubit gate fidelities of 99.9% and two-qubit gate fidelities of around 98% [\[24](#sect32), [25\]](#sect33). Trapped-ion systems have achieved single-qubit gate fidelities of up to 99.9999% and two-qubit gate fidelities of up to 99.9% [\[26\]](#sect34). However, it is important to note that these fidelities are typically achieved under ideal conditions and are often lower in real-world applications due to various sources of noise and errors.

Despite the limited fidelity of current quantum hardware, there has been significant progress in developing quantum algorithms and applications that are robust to noise and errors. For example, the recently proposed variational quantum eigensolver (VQE) algorithm [\[27\]](#sect35) is designed to work with noisy intermediate-scale quantum (NISQ) devices and can provide useful solutions to practical problems even with limited quantum resources and noisy quantum operations. The VQE algorithm employs a hybrid classical–quantum approach that combines classical optimisation with quantum measurements to find the ground state energy of a given Hamiltonian.

Another approach to dealing with limited fidelity in quantum hardware is to develop error mitigation techniques that can correct or reduce the impact of errors on quantum computations. One such technique is zero noise extrapolation (ZNE) [\[28\]](#sect36), which extrapolates the results of quantum computations at different levels of noise to estimate the ideal result. ZNE has been shown to be effective in improving the accuracy of quantum simulations on NISQ devices, and it is being actively researched and developed.

In summary, the limited fidelity of quantum state preparation and coherent evolution is a significant challenge for quantum computing, and it is a major focus of research and development in the field. While current quantum hardware falls short of the theoretical ideal, there has been significant progress in improving the fidelity of quantum operations and developing quantum algorithms and applications that are robust to noise and errors.

## 6.6 Quantum error correction

Quantum error correction (QEC) [\[29\]](#sect37) is a fundamental technique for protecting quantum information from the harmful effects of noise and decoherence in quantum systems. QEC is necessary for practical quantum computing because the quantum hardware is inherently noisy due to environmental interactions, and errors can propagate rapidly through the system. The goal of QEC is to detect and correct errors in quantum states and operations in a way that preserves the overall coherence and fidelity of the system.

QEC works by encoding the quantum information into a larger quantum state, called a quantum error-correcting code (QECC), that is designed to be resistant to certain types of errors. When errors occur, the QECC can be probed and measurements can be performed to diagnose the error and apply the appropriate correction. There are several types of QECCs, including the surface code, the colour code and the topological code, which are designed to be robust against different types of errors.

One of the key challenges of QEC is that the correction process itself can introduce new errors, and these errors can accumulate over time and lead to a loss of fidelity. This is known as the threshold theorem [\[30](#sect38), [31](#sect39), [32\]](#sect40), which provides a quantitative limit on the amount of noise that can be corrected by a QECC before the errors become too large to correct. The threshold theorem sets a practical limit on the size and complexity of quantum computers that can be built without error correction.

The threshold theorem is based on the concept of the error rate, which is the probability of a bit or qubit flip error occurring during a single operation or time step. The error rate is a fundamental quantity that determines the overall fidelity of the quantum system, and it can be measured using various techniques, such as randomised benchmarking and gate set tomography. In practice, the error rate depends on the specific hardware platform and the details of the control and measurement procedures.

Achieving a low error rate is a critical requirement for practical quantum computing, and significant progress has been made in recent years in improving the fidelity of quantum systems. For example, superconducting qubits, which are one of the leading hardware platforms for quantum computing, have achieved error rates as low as $10^{-4}$ to $10^{-3}$ for single-qubit gates and $10^{-2}$ to $10^{-1}$ for two-qubit gates [\[33](#sect41), [34\]](#sect42). Other platforms, such as ion traps and photonic qubits, have also demonstrated high fidelities [\[35\]](#sect43).

Despite these improvements, achieving fault-tolerant quantum computing using QEC is still a significant challenge, and much work remains to be done to increase the fidelity and scalability of quantum hardware. In addition to improving the hardware, there is also ongoing research on the development of new QECCs and error correction protocols that are more efficient and robust against a wider range of errors [\[36\]](#sect44).

In summary, quantum error correction is a crucial technique for protecting quantum information from noise and decoherence in quantum systems. The threshold theorem provides a quantitative limit on the amount of noise that can be corrected by a QECC, and the error rate is a fundamental quantity that determines the overall fidelity of the quantum system. Improving the fidelity of quantum hardware is a critical requirement for practical quantum computing, and ongoing research is focused on developing more efficient and robust QECCs and error correction protocols.

## 6.7 Physical implementation of quantum computers

Building a large-scale quantum computer is an extremely difficult task because of the fragile and complex nature of quantum systems. The physical implementation platforms of quantum computers can be classified into several categories, each with its own advantages and disadvantages. Here we will explore a brief overview of some of the physical platforms currently being developed for quantum computers. This discussion continues the above outline of qubit implementation platforms, but with a view towards a fully scaled-up quantum computer system.

One of the most widely studied platforms for quantum computing is based on trapped ions. In this approach, ions are confined in a vacuum and manipulated with electromagnetic fields. The ions can be used as qubits, and their state can be read out using laser pulses. This method has been successful in demonstrating basic quantum algorithms and error correction protocols. However, the challenge is to scale up the system to thousands or even millions of qubits while maintaining high fidelity.

Superconducting circuits are another popular platform for quantum computing [\[26\]](#sect34). In this approach, the qubits are made of superconducting loops or junctions that can be controlled with microwave pulses. The advantage of this platform is that it can be integrated with classical electronics, making it possible to scale up the system and perform complex quantum operations. However, the superconducting qubits are sensitive to environmental noise, which can lead to decoherence and limit the coherence time.

Photonic qubits are another promising platform for quantum computing. In this approach, the qubits are encoded in the polarisation of single photons, which can be manipulated using optical components such as beam splitters and phase shifters. The advantage of this platform is that photons can travel long distances without significant decoherence, making it possible to implement quantum communication protocols. However, the challenge is to build efficient photon sources and detectors and to achieve high fidelity in the manipulation of the photons.

Diamond-based platforms are also being developed for quantum computing. In this approach, the qubits are based on defects in diamond crystals, such as nitrogen-vacancy (NV) centres. The NV centres can be manipulated using microwave and laser pulses, and their state can be read out optically. The advantage of this platform is that it can be used to build hybrid systems that combine the benefits of different physical platforms. For example, NV centres [\[28\]](#sect36) can be coupled to superconducting qubits or to optical cavities. However, the challenge is to improve the coherence time of the NV centres and to achieve high fidelity in the manipulation and readout of their state.

Other platforms that are being studied for quantum computing include topological qubits, which are based on non-Abelian anyons, and quantum dots, which are semiconductor devices that can be used as qubits. Topological qubits are attractive because they are inherently fault tolerant, but they are also very challenging to build and manipulate. Quantum dots have the advantage of being compatible with standard semiconductor technology, but they are also sensitive to environmental noise.

In summary, the physical implementation platforms of quantum computers are diverse and each has its own advantages and challenges. The choice of platform depends on many factors, including the scalability, coherence time and fidelity requirements of the quantum computation task. As the field of quantum computing continues to advance, it is likely that new platforms will be developed and existing platforms will be improved to overcome the current limitations.

## 6.8 Some applications of quantum computers

Quantum computers have shown potential to solve problems that are intractable for classical computers. While quantum computers are still in their infancy, there are already several practical applications that are being explored.

One area where quantum computers are expected to have significant impact is in cryptography. Shor's algorithm, which can efficiently factorise large numbers on a quantum computer, has the potential to break many commonly used public-key encryption schemes. This has led to research into developing post-quantum cryptography schemes that are secure against attacks by quantum computers [\[35\]](#sect43).

Another area where quantum computers are expected to be useful is in pharmaceutical drug development. Quantum computers can simulate the behaviour of molecules much more accurately than classical computers [\[36\]](#sect44), which enables faster discovery of new drugs and materials. Researchers are already using quantum computers to study the behaviour of small molecules, with the hope of scaling up to larger and more complex molecules.

Quantum computers can also be used for optimisation problems, such as finding the shortest path between multiple points or scheduling tasks to minimise time or cost. For example, Volkswagen used a D-wave quantum computer to optimise the placement of charging stations for electric vehicles, which reduced the number of stations needed by 20 % [\[37\]](#sect45).

In finance, quantum computers can be used to optimise portfolios and reduce risk. For example, Goldman Sachs is exploring the use of quantum computing to optimise its portfolio of stocks and bonds [\[38\]](#sect46).

In addition to these practical applications, quantum computers can be used to improve machine-learning algorithms. Quantum machine learning is a rapidly growing field that uses quantum computers to improve the efficiency and accuracy of machine-learning algorithms. This has the potential to lead to significant improvements in fields such as natural language processing, image recognition and robotics.

## Summary

Overall, while quantum computers are still in their early stages of development, there are already several practical applications that are being explored. From cryptography to pharmaceutical drug development to optimisation and machine learning, quantum computers have the potential to revolutionise many fields and provide new solutions to previously unsolvable problems.

Well done! You have now reached the end of this week’s Study – Week 6: Quantum computing

## References
1.  [\[1\]](#sect0) Haigh, T. and Ceruzzi, P. E. A New History of Modern Computing. Cambridge, MA: The MIT Press, 2021.
2.  [\[2\]](#sect0) Moore, G. E. Cramming more components onto integrated circuits. Electronics, 1965. \[Online\], 38 (8), pp. 114–117. Available at: https://hasler.ece.gatech.edu/Published\_papers/Technology\_overview/gordon\_moore\_1965\_article.pdf \[accessed 26 May 2023\].
3.  [\[3\]](#sect0) Nielsen, M. A. and Chuang, I. L. Quantum Computation and Quantum Information. Cambridge: Cambridge University Press, 2010.
4.  [\[4\]](#sect0) Aaronson, S. The limits of quantum computers. Scientific American, 2008. \[Online\], 304 (4), pp. 62–67. Available at: https://www.cs.virginia.edu/robins/The\_Limits\_of\_Quantum\_Computers.pdf \[accessed 26 May 2023\].
5.  [\[5\]](#sect1) Weinstein, Y. S., Pravia, M. A., Fortunato, E. M., Lloyd, S. and Cory, D. G. Implementation of the quantum Fourier transform. Physical Review Letters, 2001. \[Online\], 86 (9), pp. 1889-1891. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.86.1889 \[accessed 26 May 2023\].
6.  [\[6\]](#sect2) Deutsch, D. Quantum theory, the Church-Turing principle and the universal quantum computer. Proceedings of the Royal Society of London, 1985. \[Online\], 400, pp. 97-117. Available at: https://www.daviddeutsch.org.uk/wp-content/deutsch85.pdf \[accessed 26 May 2023\].
7.  [\[7\]](#sect2) Jozsa, R. Quantum algorithms and the Fourier transform. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences, 1998. \[Online\], 454 (1969), pp. 323–337. Available at: https://arxiv.org/abs/quant-ph/9707033 \[accessed 26 May 2023\].
8.  [\[8\]](#sect2) Grover, L. K. A fast quantum mechanical algorithm for database search. STOC, 1996. \[Online\], 96 (212), pp. 212–219. Available at: https://arxiv.org/abs/quant-ph/9605043 \[accessed 26 May 2023\].
9.  [\[9\]](#sect2) Bennett, C. H., Brassard, G., Crepeau, C., Jozsa, R., Peres, A. and Wootters, W. K. Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. Physical Review Letters, 1993. \[Online\], 70 (13), pp. 1895–1899. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.70.1895 \[accessed 26 May 2023\].
10.  [\[10\]](#sect3) Rademaker, L., Wang, Y., Berlijn, T. and Johnston, S. Enhanced superconductivity due to forward scattering in FeSe thin films on SrTiO3 substrates. New Journal of Physics, 2016. \[Online\], 18 (2), p. 023024. Available at: https://iopscience.iop.org/article/10.1088/1367-2630/18/2/022001 \[accessed 26 May 2023\].
11.  [\[11\]](#sect3) Monroe C. and Kim, J. Scaling the ion trap quantum processor. Science, 2014. \[Online\], 339 (6124), pp. 1164–1169. Available at: https://www.science.org/doi/10.1126/science.1231298 \[accessed 26 May 2023\].
12.  [\[12\]](#sect3) Li, A. Topological Quantum Computing, 2019. \[Online\]. Available at: https://medium.com/swlh/topological-quantum-computing-5b7bdc93d93f \[accessed 26 May 2023\].
13.  [\[13\]](#sect4) Shor, P. W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM Journal on Computing, 1997. \[Online\], 26 (5), pp. 1484–1509. Available at: https://arxiv.org/abs/quant-ph/9508027 \[accessed 26 May 2023\].
14.  [\[14\]](#sect5) Zhu, D., Cian, Z. P., Noel, C., Risinger, A., Biswas, D., Egan, L., Zhu, Y., Green, A. M., Huerta Alderete, C., Nguyen, N. H., Wang, Q., Maksymov, A., Nam, Y., Cetina, M., Linke, N. M., Hafezi, M. and Monroe, C. Cross-platform comparison of arbitrary quantum states. Nature Communications, 2022. \[Online\],13, p. 6620. Available at: https://www.nature.com/articles/s41467-022-34279-5 \[accessed 26 May 2023\].
15.  [\[15\]](#sect5) Barends, R., Kelly, J., Megrant, A., Veitia, A., Sank, D., Jeffrey, E., White, T., Mutus, J., Fowler, A., Campbell, Chen, B. Y., Chen, Z., Chiaro, B., Dunsworth, A., Neill, C., O’Malley, P., Roushan, P., Vainsencher, A., Wenner, J., Korotkov, A. N., Cleland, A. N. and Martinis, J. M. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature, 2014. \[Online\], 508 (7497), pp. 500–503. Available at: https://www.nature.com/articles/nature13171 \[accessed 26 May 2023\].
16.  [\[16\]](#sect5) Kelly, J., Barends, R., Fowler, A. G., Megrant, A., Jeffrey, E., White, T. C., Sank, D., Mutus, J. Y., Campbell, B., Chen, Y., Chiaro, B., Dunsworth, A., Hoi, I.-C., Neill, C., O’Malley, P. J. J., Quintana, C., Roushan, P., Vainsencher, A., Wenner, J., Cleland, A. N. and Martinis, J. M. State preservation by repetitive error detection in a superconducting quantum circuit. Nature, 2015. \[Online\], 519 (7541), pp. 66–69. Available at: https://www.nature.com/articles/nature14270 \[accessed 26 May 2023\].
17.  [\[17\]](#sect5) Ballance, C. J., Harty, T. P., Linke, N. M., Sepiol, M. A., Lucas, D. M., Hempel, C., Sewell, R. J., Leroux, I. D. and Biercuk, M. J. High-fidelity quantum logic gates using trapped-ion hyperfine qubits. Physical Review Letters, 2016. \[Online\], 117 (6), pp. 060504. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.117.060504 \[accessed 26 May 2023\].
18.  [\[18\]](#sect5) Srinivas, R., Burd, S. C., Knaack, H. M., Sutherland, R. T., Kwiatkowski, A., Glancy, S., Knill, E., Wineland, D. J., Leibfried, D., Wilson, A. C., Allcock, D. T. C. and Slichter, D. H. High-fidelity laser-free universal control of trapped ion qubits. Nature, 2021. \[Online\], 597, pp. 209–213. Available at: https://www.nature.com/articles/s41586-021-03809-4 \[accessed 26 May 2023\].
19.  [\[19\]](#sect5) Bækkegaard, T., Kristensen, L. B., Loft, N. J. S., Andersen, C. K., Petrosyan, D., Zinner, N. T. Realization of efficient quantum gates with a superconducting qubit-qutrit circuit. Scientific Reports, 2018. \[Online\], 9 (13389), pp. 1-27. Available at: https://arxiv.org/abs/1802.04299 \[accessed 26 May 2023\].
20.  [\[20\]](#sect5) Qi, R., Sun, Z., Lin, Z., Niu, P., Hao, W., Song, L., Huang, Q., Gao, J., Yin, L. and Long, G.-L. Implementation and security analysis of practical quantum secure direct communication. Light: Science & Applications, 2019. \[Online\], 8 (22), pp. 8055. Available at: https://www.nature.com/articles/s41377-019-0132-3 \[accessed 26 May 2023\].
21.  [\[21\]](#sect5) Dang, N. C., Bolme, C. A., Moore, D. S. and McGrane, S. D. Femtosecond stimulated Raman scattering picosecond molecular thermometry in condensed phases. Physical Review Letters, 2011. \[Online\], 107 (4), pp. 043001. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.107.043001 \[accessed 26 May 2023\].
22.  [\[22\]](#sect5) Bialczak, R., Ansmann, M., Willomee, M. T. D., Hofheinz, M., Lucero, E., Neeley, M., O’Connell, A. D., Sank, D., Wang, H., Wenner, J., Cleland, A. N., and Martinis, J. M. Fast tunable coupler for superconducting qubits. Nature Physics, 2011. \[Online\], 7 (4), pp. 361–365. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.106.060501 \[accessed 26 May 2023\].
23.  [\[23\]](#sect5) Ferretti, S., Savona, V. and Gerace, D. Optimal antibunching in passive photonic devices based on coupled nonlinear resonators. New Journal of Physics, 2013. \[Online\], 15, pp. 025012. Available at: https://iopscience.iop.org/article/10.1088/1367-2630/15/2/025012 \[accessed 26 May 2023\].
24.  [\[24\]](#sect5) Kitaev, A. Y. Fault-tolerant quantum computation by anyons. Annals of Physics, 2003. \[Online\], 303, pp. 2-30. Available at: https://arxiv.org/abs/quant-ph/9707021 \[accessed 26 May 2023\].
25.  [\[25\]](#sect5) Alicea, J. New directions in the pursuit of Majorana fermions in solid state systems. Reports on Progress in Physics, 2012. \[Online\], 75, pp. 076501. Available at: https://iopscience.iop.org/article/10.1088/0034-4885/75/7/076501 \[accessed 26 May 2023\].
26.  [\[26\]](#sect5) Krantz, P., Kjaergaard, M., Yan, F., Orlando, T. P., Gustavsson, S. and Oliver, W. D. A quantum engineer’s guide to superconducting qubits. Applied Physics Reviews, 2019. \[Online\], 6 (2), p. 021318. Available at: https://arxiv.org/abs/1904.06560 \[accessed 26 May 2023\].
27.  [\[27\]](#sect5) Harty, T., Allcock, D., Ballance, C., Janacek, H., Linke, N., Stacey, D., Lucas, D. High-fidelity preparation, gates, memory, and readout of a trapped-ion quantum bit. Physical Review Letters, 2014. \[Online\], 113 (22), p. 220501. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.113.220501 \[accessed 26 May 2023\].
28.  [\[28\]](#sect5) Tilly, J., Chen, H., Cao, S., Picozzi, D., Setia, K., Li, Y., Grant, E., Wossnig, L., Rungger, I., Booth, G. H. and Tennyson, J. The variational quantum eigensolver: a review of methods and best practices. Physics Reports, 2022. \[Online\], 986, pp. 1-128. Available at: https://www.sciencedirect.com/science/article/pii/S0370157322003118 \[accessed 26 May 2023\].
29.  [\[29\]](#sect6) Temme, K., Bravyi, S. and Gambetta, J. Error mitigation for short-depth quantum circuits. Physical Review Letters, 2017. \[Online\], 119 (18), p. 180509. Available at: https://arxiv.org/abs/1612.02058 \[accessed 26 May 2023\].
30.  [\[30\]](#sect6) Aharonov D. and Ben-Or, M. Fault-tolerant quantum computation with constant error rate. SIAM Journal on Computing, 2008. \[Online\], 38 (4), pp. 1207–1282. Available at: https://arxiv.org/abs/quant-ph/9906129 \[accessed 26 May 2023\].
31.  [\[31\]](#sect6) Knill, E., Laflamme, R. and Zurek, W. H. Resilient quantum computation: error models and thresholds. Proceedings of the Royal Society A, 1998. \[Online\], 454 (1969), pp. 1471-2946. Available at: https://royalsocietypublishing.org/doi/10.1098/rspa.1998.0166 \[accessed 26 May 2023\].
32.  [\[32\]](#sect6) Field, B. and Simula, T. Introduction to topological quantum computation with non-Abelian anyons. Quantum Science and Technology, 2018. \[Online\], 3 (4), pp. 045004. Available at: https://iopscience.iop.org/article/10.1088/2058-9565/aacad2 \[accessed 26 May 2023\].
33.  [\[33\]](#sect6) Terhal, B. M. Quantum error correction for quantum memories. Reviews of Modern Physics, 2015. \[Online\], 87 (2), pp. 307. Available at: https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.87.307 \[accessed 26 May 2023\].
34.  [\[34\]](#sect6) Ruf, M., Wan, N. H., Choi, H., Englund, D. and Hanson, R. Quantum networks based on color centers in diamond. Journal of Applied Physics, 2021. \[Online\], 130 (7), pp. 070901. Available at: https://pubs.aip.org/aip/jap/article/130/7/070901/1061464/Quantum-networks-based-on-color-centers-in-diamond \[accessed 26 May 2023\].
35.  [\[35\]](#sect6) Bernstein, D. J. Introduction to post-quantum cryptography. In: Bernstein, D. J., Buchmann, J. and Dahmen, E. (eds) Post-Quantum Cryptography. Berlin, Heidelberg: Springer, 2009.
36.  [\[36\]](#sect6) Outeiral, C., Strahm, M., Shi, J., Morris, G. M., Benjamin, S. C. and Deane, C. M. The prospects of quantum computing in computational molecular biology. WIREs Computational Molecular Science, 2020. \[Online\], 11 (1), pp. 1-23. Available at: https://arxiv.org/abs/2005.12792 \[accessed 26 May 2023\].
37.  [\[37\]](#sect8) Automotive Purchasing and Supply Chain. Volkswagen takes quantum computing from the lab to the factory, 2021. \[Online\]. Available at: https://www.automotivepurchasingandsupplychain.com/volkswagen-takes-the-quantum-computing-revolution-from-the-lab-to-the-factory/l \[accessed 26 June 2023\].
38.  [\[38\]](#sect8) Goldman Sachs. Engineering Quantum Algorithms, 2023. \[Online\]. Available at: https://www.goldmansachs.com/careers/possibilities/quantum-computing/ \[accessed 26 May 2023\].
39.  [\[39\]](#sect1) Ketterer, A. Modular variables in quantum information. PhD diss. Universite Sorbonne Paris Cite, 2016.