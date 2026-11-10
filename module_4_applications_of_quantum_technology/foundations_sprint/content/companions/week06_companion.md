# Week 06 Companion - Quantum computing

**Built on:** Day 08 (M12 gates and circuits, Bell state, phase kickback, Deutsch-Jozsa as an amplitude sum), Day 09 (M13 speed-up taxonomy, Shor arithmetic, Grover, depth from fidelity, threshold theorem); M11 from Day 07 for the "why classical struggles" background
**Feeds:** Portfolio (Assessment 2) through the Week 6 Consolidate piece. Nothing here is aimed at Assessment 1.

Line numbers `L..` refer to `week_6/week_6_lecture.md`. Task wording is in `week_6/week_6_content.md`. Read this alongside the lecture, not instead of it.

## 1. Read these first (Pass 0)

Before you read the lecture, know what the week asks you to do with it. Types only, no solutions.

1. **Explore (200 words):** the limits of conventional computing, and where high-end computing is used. Type: background summary with numbers (M11 memory scaling, M13 complexity classes in plain words, F3 sourcing).
2. **Apply (forum, 200-300 words):** pick one aspect of quantum computing (an algorithm or tool, or a hardware platform) and explain how it works and what the benefit is. Type: F1 gain argument, short form, built on M12 (how it works) and M13 (how big the gain is).
3. **Consolidate (portfolio, 300 words):** elaborate one or two points; quantify the gain (speed-up, or a problem class that becomes possible) and say what kind of gain it is. Type: F1 gain argument where slot 4 must name the speed-up class (exponential, sub-exponential, quadratic, heuristic).
4. **Optional interactive:** a quantum puzzle game; best identification The Qubit Factory (see §9).
5. **No quiz this week** (inventory: Weeks 1, 6 and 7 have none).

The quantitative side the week expects of you is small: trace a two-qubit circuit by hand, compute a Deutsch-Jozsa amplitude, run the classical half of Shor on a small $N$, count Grover iterations, and turn a gate fidelity into a usable circuit depth. Sections 4-6 drill exactly that. The writing side has one trap above all others: calling every quantum gain "exponential".

## 2. What the lecture is doing, in one picture

A qubit is the two-level system you already own from Module 3, now used as a memory cell: a unit vector $\alpha|0\rangle+\beta|1\rangle$, drawn as a point on the Bloch sphere. Gates are $2\times2$ (or $4\times4$) unitary matrices that rotate these vectors, and the CNOT links two qubits so that they become entangled. An algorithm is a sequence of gates arranged so that the amplitudes of wrong answers cancel and the amplitude of the right answer builds up; then one measurement reads it. Deutsch-Jozsa, Grover and Shor are three examples with three very different sizes of gain (exponential only against an exact classical algorithm; quadratic; super-polynomial against the best known classical method). The second half of the lecture is about why this is hard to build: every gate is slightly wrong, errors multiply over the circuit, and error correction can fix that only if each operation is already better than a threshold, at a cost of many physical qubits per logical one. The lecture ends with platforms (superconducting, ions, photons, NV, topological) and applications, including a quantum-annealing optimisation claim that is not a gate-model result.

The lecture states most of this without derivation and contains several errors (L47, L95, L131, L135, L150, L152, L184, and three inconsistent sets of fidelities). Section 4 fixes each one, with the line.

Free reading if you want more than the lecture: Preskill, *Quantum computing in the NISQ era and beyond*, https://arxiv.org/abs/1801.00862 (all, short); Aaronson, *The Limits of Quantum Computers*, https://www.scottaaronson.com/writings/limitsqc-draft.pdf (the antidote to "tries every answer at once"); Quantum Country essay 1, https://quantum.country/qcvc; IBM Quantum Learning, *Basics of quantum information*, lessons 1-3, https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information.

## 3. Notation and unit decoder

| Symbol as written | Read it as | Unit | Where (lecture line) | Clash / trap | Move |
|---|---|---|---|---|---|
| $\lvert\psi\rangle$ | the qubit's state, a unit vector in $\mathbb{C}^2$ | none | L40 (Eq 6.1) | a state, not a probability | M12 |
| $\lvert0\rangle$, $\lvert1\rangle$ | computational basis states, $(1,0)^T$ and $(0,1)^T$ | none | L40-L44 | the "north" and "south" poles of the Bloch sphere (L47) | M12 |
| $\alpha$, $\beta$ | complex amplitudes; $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$ | none | L44 | amplitudes, not probabilities; they can be negative or complex, which is what makes interference possible | M12 |
| $\theta$, $\varphi$ (written "\theta", "\phi" in L58) | Bloch polar and azimuthal angles: $\lvert\psi\rangle=\cos\frac{\theta}{2}\lvert0\rangle+e^{i\varphi}\sin\frac{\theta}{2}\lvert1\rangle$ | rad | L58 (figure description) | the half-angle $\theta/2$; antipodal points are orthogonal states, not opposite signs | M12 |
| $\lvert+\rangle$, $\lvert-\rangle$ | $(\lvert0\rangle\pm\lvert1\rangle)/\sqrt2$, the equator points on the $x$ axis | none | L58 | $\lvert-\rangle$ is the ancilla state that makes phase kickback work (4E) | M12 |
| $X$, $Y$, $Z$ | Pauli gates: bit flip; bit and phase flip ($Y=iXZ$); phase flip | none (unitary matrices) | L62-L68 (Eq 6.2-6.4) | $X$, $Y$, $Z$ are also the Bloch axes; L68 calls $Y$ only a "phase shift" (4B) | M12 |
| CNOT | controlled-NOT: flips the target if the control is $\lvert1\rangle$ | none | L71-L75 (Eq 6.5) | the matrix assumes basis order $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$ with the **control written first** (4C) | M12 |
| $H$ | Hadamard: $\lvert0\rangle\to\lvert+\rangle$, $\lvert1\rangle\to\lvert-\rangle$; $H^2=I$ | none | L80-L82 (Eq 6.6) | not the Hamiltonian $H$ of Week 5 | M12 |
| $\oplus$ | addition mod 2 (XOR) | none | not printed; needed for the oracle (4E) | not a direct sum here | M12 |
| $f:\{0,1\}^n\to\{0,1\}$ | a Boolean function of an $n$-bit input | none | L89 | $f$ also names $a^x \bmod N$ in Shor (L146) | M12 |
| $U_f$ | the oracle: $U_f\lvert x\rangle\lvert y\rangle=\lvert x\rangle\lvert y\oplus f(x)\rangle$ | none | implied at L95 | L95 says it acts on "the n qubits"; it writes into the **last** qubit (4E) | M12 |
| $n$ | number of input bits (qubits in the input register) | none | L89 | $N=2^n$ in Grover; $N$ the number to factor in Shor | M12, M13 |
| $2^{n-1}+1$ | worst-case classical queries for an exact constant/balanced answer | queries | L91 | exact and deterministic only (4E) | M13 |
| $\mathcal{O}(\cdot)$ | "grows no faster than", constants dropped | none | L102, L152 | $\mathcal{O}(\sqrt N)$ vs $\mathcal{O}(N)$ is quadratic, not exponential | M13 |
| $N$ (Grover) | number of items searched | items | L102 | Grover needs $\approx(\pi/4)\sqrt N$ oracle calls (4F) | M13 |
| $N$ (Shor) | the composite number to factor | none | L144-L152 | its **size** is $\log_2 N$ bits; complexity is quoted in bits | M13 |
| $a$, $x$, $a^x \bmod N$ | random base coprime to $N$; exponent; remainder after dividing by $N$ | none | L146 | "mod" is the remainder, not a modulus of a complex number | M13 |
| $r$ | order (period) of $a$ mod $N$: smallest $r>0$ with $a^r\equiv1 \pmod N$ | none | L148-L150 | L150's $r=2^s r'$ is garbled (4H) | M13 |
| $\gcd$ | greatest common divisor (Euclid's algorithm, cheap) | none | not printed; needed at L146 and L150 | the step L135 calls "computationally expensive" is this cheap step (4H) | M13 |
| QFT | quantum Fourier transform: $\lvert x\rangle\to\frac{1}{\sqrt M}\sum_{y}e^{2\pi i xy/M}\lvert y\rangle$ | none | L82, L135, L148 | a unitary on amplitudes, not an FFT on a list of numbers | M13 |
| $O((\log N)^3)$ | Shor gate count, polynomial in the number of bits | gates | L152 | the classical rival (NFS) is **sub-exponential**, not exponential (4H) | M13 |
| RSA | public-key scheme whose security rests on factoring being hard | none | L133 | Week 4 (M8): PQC is the classical fix | M8 |
| $F$, "fidelity" | overlap of the achieved with the intended state or gate, often quoted as %; error $=1-F$ | dimensionless, % | L160-L170 | "99.5%" two-qubit and "error $10^{-2}$ to $10^{-1}$" (L188) are different machines (4I) | M13 |
| error rate $p$ | probability of an error per operation or time step | dimensionless | L186-L188 | $p=10^{-3}$ means $F=99.9\%$ | M13 |
| coherence time, $T_1$, $T_2$ | how long a qubit keeps its state ($T_1$: energy relaxation; $T_2$: loss of phase). The lecture says "coherence time" only | s (µs for superconducting, up to s for ions) | L114, L164-L166 | not the interferometer $T$ of Week 3 | M13 |
| 20 mK | operating temperature of superconducting qubits | K | L111 | milli-kelvin: 0.02 K above absolute zero | M1 |
| "several hundred microseconds" | coherence time after dynamical decoupling | s | L166 | a time, not a gate count; divide by gate time to get a depth budget | M13 |
| $p_\mathrm{th}$ | threshold error rate of an error-correcting code (not printed, implied at L184) | dimensionless | L184 | L184 states the theorem backwards (4J) | M13 |
| QEC, QECC | quantum error correction; an error-correcting code | none | L180-L182 | physical vs logical qubits; overhead is the price | M13 |
| NISQ | noisy intermediate-scale quantum: roughly 50 to a few hundred qubits, no error correction (Preskill 2018) | none | L172 | an era, not a device type | M13 |
| VQE | variational quantum eigensolver: a short quantum circuit inside a classical optimiser loop | none | L172 | heuristic; no proven speed-up | M13 |
| ZNE | zero-noise extrapolation: run at amplified noise and extrapolate to zero | none | L174 | mitigation, not correction: it does not scale to long circuits | M13 |
| QUBO / annealing | optimisation by slowly changing a Hamiltonian (not printed; the machine at L218 is an annealer) | none | L218 | not a gate-model computer (4L) | M13 |

**Unit and scale conversions you will use.** Error $= 1-F$: 99.9% is $10^{-3}$, 99.99% is $10^{-4}$. A circuit of $g$ gates of fidelity $F$ succeeds with roughly $F^g$. "Bits" of $N$ $=\log_2 N$: a 2048-bit RSA modulus has $N\approx2^{2048}\approx10^{617}$.

## 4. Skipped steps, expanded

Each item gives the lecture line, the gap, the missing lines and the move.

### 4A. L40-L47: the Bloch formula, and the L47 erratum (M12)

1. A global phase is unobservable, so make $\alpha$ real and non-negative. Normalisation $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$ then lets you write $\alpha=\cos\frac{\theta}{2}$, $\beta=e^{i\varphi}\sin\frac{\theta}{2}$:
$$\lvert\psi\rangle=\cos\tfrac{\theta}{2}\lvert0\rangle+e^{i\varphi}\sin\tfrac{\theta}{2}\lvert1\rangle,\qquad 0\le\theta\le\pi,\ 0\le\varphi<2\pi.$$
2. $(\theta,\varphi)$ are the polar and azimuthal angles of a point on a unit sphere (the Bloch sphere, Fig 6.1). $\theta=0$ is $\lvert0\rangle$ (north), $\theta=\pi$ is $\lvert1\rangle$ (south), $\theta=\pi/2,\varphi=0$ is $\lvert+\rangle$, $\theta=\pi/2,\varphi=\pi$ is $\lvert-\rangle$.
3. Measurement probabilities: $P(0)=\cos^2\frac{\theta}{2}$, $P(1)=\sin^2\frac{\theta}{2}$. Example: $\theta=\pi/3$ (60°) gives $P(0)=0.75$. The **latitude** sets the probabilities; the **longitude** $\varphi$ is the relative phase, invisible to a $Z$ measurement but decisive for interference.
4. **Erratum, L47.** "The distance from the centre representing the probability amplitude" is wrong. Every pure state sits **on** the surface (distance 1). Points inside the sphere are mixed states (classical uncertainty about which state was prepared); the centre is the maximally mixed state. Read L47 as: "the position on the sphere (the angle $\theta$ from the north pole) sets the probabilities."
5. Trap: on the sphere, opposite points are **orthogonal** states ($\lvert0\rangle$ and $\lvert1\rangle$ are 180° apart, though they are 90° apart as vectors). That is why the formula uses $\theta/2$.

### 4B. L62-L68: the Paulis, and $Y=iXZ$ (M12)

1. Act on the basis: $X\lvert0\rangle=\lvert1\rangle$, $X\lvert1\rangle=\lvert0\rangle$ (bit flip); $Z\lvert0\rangle=\lvert0\rangle$, $Z\lvert1\rangle=-\lvert1\rangle$ (phase flip); $Y\lvert0\rangle=i\lvert1\rangle$, $Y\lvert1\rangle=-i\lvert0\rangle$.
2. Multiply: $XZ=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, so $iXZ=\begin{pmatrix}0&-i\\i&0\end{pmatrix}=Y$.
3. So $Y$ is "do $Z$, then $X$, times a global phase $i$": a bit flip **and** a phase flip. L68 calls $Y$ a gate that "introduces a phase shift between $\lvert0\rangle$ and $\lvert1\rangle$", which describes $Z$ (or the phase gate $S$), not $Y$. Read L68's $Y$ as "bit-and-phase flip".
4. On the Bloch sphere each Pauli is a 180° rotation about its own axis. $X$ swaps the poles; $Z$ swaps $\lvert+\rangle$ and $\lvert-\rangle$; $Y$ does both.

### 4C. L73-L75: CNOT basis ordering, and the Bell state the lecture never builds (M12)

1. **Ordering.** Eq 6.5 is written in the basis $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$ where the **first** (left) label is the control. Rows 3 and 4 swapped means $\lvert10\rangle\leftrightarrow\lvert11\rangle$: the target flips only when the control is 1. Some software (and Quirk's display) lists the qubits in the other order; then the same gate has a different-looking matrix. Always state which qubit is written first.
2. **Bell state, step by step.** Start in $\lvert00\rangle$.
   - $H$ on the control: $\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\lvert0\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert10\rangle)$.
   - CNOT: $\lvert00\rangle\to\lvert00\rangle$, $\lvert10\rangle\to\lvert11\rangle$. Result $\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$.
   - Amplitudes $1/\sqrt2\approx0.707$; outcomes 00 and 11 each with probability 0.5, never 01 or 10.
3. **Why it is entangled (L75).** A product state $(a\lvert0\rangle+b\lvert1\rangle)(c\lvert0\rangle+d\lvert1\rangle)$ has amplitudes $ac, ad, bc, bd$. For $\lvert\Phi^+\rangle$ we need $ad=0$ and $bc=0$ but $ac=bd=1/\sqrt2\ne0$: impossible. No single-qubit description exists, which is L75's definition.
4. Starting from $\lvert01\rangle$, $\lvert10\rangle$ or $\lvert11\rangle$ gives the other three Bell states; Day 08 drills these.

### 4D. L80-L82: Hadamard identities the lecture uses without stating (M12)

1. $H\lvert0\rangle=\lvert+\rangle$, $H\lvert1\rangle=\lvert-\rangle$; compactly $H\lvert x\rangle=\frac{1}{\sqrt2}\sum_{z\in\{0,1\}}(-1)^{xz}\lvert z\rangle$.
2. $H^2=I$: $H\lvert+\rangle=\lvert0\rangle$ and $H\lvert-\rangle=\lvert1\rangle$. This "undo" is how an algorithm turns phase information back into a readable bit.
3. $n$ qubits: $H^{\otimes n}\lvert0\cdots0\rangle=\frac{1}{\sqrt{2^n}}\sum_{x}\lvert x\rangle$, an equal superposition of all $2^n$ inputs.
4. General input: $H^{\otimes n}\lvert x\rangle=\frac{1}{\sqrt{2^n}}\sum_{z}(-1)^{x\cdot z}\lvert z\rangle$, with $x\cdot z=x_1z_1\oplus\cdots\oplus x_nz_n$. Deutsch-Jozsa's last step is this line.
5. $HZH=X$ and $HXH=Z$: the Hadamard swaps the bit-flip and phase-flip pictures.

### 4E. L89-L99: Deutsch-Jozsa as an amplitude sum, and four slips (M12, M13)

The lecture lists the steps but never shows why they work. Here are the missing lines.

1. **Oracle.** The function is available only as a reversible gate $U_f\lvert x\rangle\lvert y\rangle=\lvert x\rangle\lvert y\oplus f(x)\rangle$. One use of $U_f$ is one "query".
2. **Ancilla $\lvert1\rangle\to\lvert-\rangle$.** Step 1 starts the last qubit in $\lvert1\rangle$; step 2's Hadamard turns it into $\lvert-\rangle$. The input register becomes $\frac{1}{\sqrt{2^n}}\sum_x\lvert x\rangle$ (4D).
3. **Phase kickback.** For each $x$: $U_f\lvert x\rangle\lvert-\rangle=\lvert x\rangle\frac{\lvert f(x)\rangle-\lvert1\oplus f(x)\rangle}{\sqrt2}=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$. If $f(x)=0$ nothing changes; if $f(x)=1$ the two terms swap, which is a minus sign. The ancilla is unchanged and the answer has been written into the **sign** of each input's amplitude.
4. **Interfere.** Apply $H^{\otimes n}$ (4D, item 4). The amplitude of the all-zero outcome is
$$A_{0\cdots0}=\frac{1}{2^n}\sum_{x}(-1)^{f(x)}.$$
5. **Read.** Constant $f$: every term is $+1$ (or every term $-1$), so $A=\pm1$ and you see $0\cdots0$ with certainty. Balanced $f$: half the terms are $+1$, half $-1$, so $A=0$ and you **never** see $0\cdots0$. One query, no error.
6. **Slip, L89.** "Balanced if it outputs a different value for exactly half of the inputs." Read: $f=0$ on exactly half the inputs and $f=1$ on the other half.
7. **Slip, L93.** "Start with $n+1$ qubits in the $\lvert0\rangle$ state: $\lvert0\rangle\cdots\lvert0\rangle\lvert1\rangle$." The last qubit starts in $\lvert1\rangle$ (or in $\lvert0\rangle$ followed by an $X$). Without it there is no $\lvert-\rangle$ and no kickback.
8. **Slip, L95 (step 3).** "Apply the function $f$ to the $n$ qubits and leave the last qubit unchanged." The oracle **writes into** the last qubit ($y\oplus f(x)$); it is the input register whose basis labels are untouched. The confusing truth is that both halves of the sentence are "sort of" right only after kickback: the ancilla stays $\lvert-\rangle$ and the inputs gain signs. Read step 3 as "apply $U_f$ to all $n+1$ qubits", and step 4 (L96) as "Hadamard on the first $n$".
9. **Slip, L99.** "Exponentially faster than any known classical algorithm." True only against an **exact deterministic** classical algorithm, which needs $2^{n-1}+1$ queries in the worst case (L91): 3 for $n=2$, 5 for $n=3$, 513 for $n=10$. A **randomised** classical algorithm that queries $k$ random inputs and says "constant" if they all agree is wrong with probability at most about $2\times2^{-k}$: for $k=10$, about 0.002, independent of $n$. So against a classical machine allowed a tiny error, the gain is a constant. Deutsch-Jozsa demonstrates interference; it is not a practical speed-up (Aaronson's essay makes the same point).

### 4F. L102, L131 vs L139: Grover is quadratic, not exponential (M13, erratum)

1. Grover needs about $\frac{\pi}{4}\sqrt N$ oracle calls to find one marked item among $N$; a classical search needs $N/2$ on average and $N$ in the worst case.
2. Size: $N=10^8$ gives $\frac{\pi}{4}\times10^4\approx7854$ Grover iterations against $5\times10^7$ classical look-ups on average.
3. **Contradiction.** L131 lists "database searches" among problems with "an exponential increase in speed". L102 ($\mathcal{O}(\sqrt N)$ vs $\mathcal{O}(N)$) and L139 ("quadratic speed-up") are correct. Delete "database searches" from L131's list.
4. Why the iteration count is fixed: each Grover step rotates the state by a fixed angle $\approx2/\sqrt N$ towards the marked item; after about $\frac{\pi}{4}\sqrt N$ steps it points at it. Running longer rotates **past** it, so success probability falls again. You cannot just "run until done".
5. L139's caveat is the practical one: the "database" must be supplied as a quantum oracle. Loading $N$ classical records into a quantum memory already costs about $N$ steps, which eats the gain (judgement; Aaronson's essay discusses the limits).
6. Also L131: "superposition allows quantum algorithms to perform multiple calculations simultaneously" is the parallelism myth (Week 1 L70, inventory). The gain comes from interference (4E item 4), then one measured outcome.

### 4G. L102: teleportation needs two classical bits (M12)

1. "Share a quantum state without actually transmitting the state itself" omits two ingredients: a **pre-shared entangled pair** (one half each), and a **classical message of 2 bits** from sender to receiver.
2. The sender does a Bell measurement on the unknown qubit and her half of the pair, getting one of 4 outcomes (2 bits). The receiver applies $I$, $X$, $Z$ or $XZ$ to his half according to those bits.
3. Until the 2 bits arrive, the receiver's qubit is maximally mixed: no information, so no faster-than-light signalling (consistent with the Week 4 quiz key). The original is destroyed by the measurement, so no cloning either (Week 4, M9).

### 4H. L133-L152: Shor, the garbled L150, and three wrong claims (M13, erratum, verified)

1. **The skeleton (L146-L150, corrected).**
   1. Pick random $a$ with $1<a<N$. Compute $\gcd(a,N)$ by Euclid's algorithm (cheap). If it is not 1, you have a factor already (L146 says this).
   2. **Quantum step:** find the order $r$ of $a$ modulo $N$, the smallest $r>0$ with $a^r\equiv1\pmod N$. The function $f(x)=a^x \bmod N$ repeats with period $r$ (L146, L148).
   3. **Check:** if $r$ is odd, or if $a^{r/2}\equiv-1\pmod N$, pick a new $a$.
   4. Otherwise $\gcd(a^{r/2}-1,N)$ and $\gcd(a^{r/2}+1,N)$ are non-trivial factors of $N$.
2. **Why step 4 works.** $a^r-1=(a^{r/2}-1)(a^{r/2}+1)\equiv0\pmod N$, so $N$ divides the product. $N$ does not divide $a^{r/2}-1$ (else the order would be $r/2$), and the check excludes $N$ dividing $a^{r/2}+1$. So $N$ shares a factor with each bracket, and gcd extracts it.
3. **Erratum, L150 (verified).** "$r=2^s\cdot r'$, where $r'$ is the non-trivial factor of $N$" is wrong: $r'$ is just the odd part of $r$, unrelated to the factors. "If $a^{r/2}+1\equiv0 \bmod N$, then we can use the factors" states the **failure** case as the success case. The correct condition: **$r$ even and $a^{r/2}\not\equiv-1\pmod N$**; then take $\gcd(a^{r/2}\pm1,N)$. For a random $a$ this succeeds with probability at least 1/2 when $N$ is odd with at least two distinct prime factors (standard result; Nielsen & Chuang, the Shor chapter), so a few tries suffice.
4. **Tiny example (the lecture gives none; Day 09 does $N=21$).** $N=15$, $a=7$: powers $7,4,13,1$, so $r=4$. $7^2=49\equiv4\pmod{15}$, not $-1\equiv14$. $\gcd(3,15)=3$, $\gcd(5,15)=5$.
5. **QFT in one line (L148).** On $m$ qubits with $M=2^m$: $\mathrm{QFT}\lvert x\rangle=\frac{1}{\sqrt M}\sum_{y=0}^{M-1}e^{2\pi i\,xy/M}\lvert y\rangle$. Applied to a register whose amplitudes repeat with period $r$, it concentrates probability near multiples of $M/r$; a classical continued-fraction step reads $r$ off the measured $y$. (Derivation skipped by the spec.)
6. **Erratum, L135.** "The second step, which involves classical computing, is computationally expensive." Wrong way round. Euclid's gcd and the continued-fraction step are polynomial and cheap on any laptop. The dominant cost is quantum: computing $a^x \bmod N$ in superposition (modular exponentiation), which needs $O(n^3)$ gates for an $n$-bit $N$ with schoolbook arithmetic. The QFT itself is cheaper, $O(n^2)$ gates.
7. **Erratum, L133 and L152.** "All known classical solutions ... grow exponentially" is wrong. The best known classical method, the general number field sieve (NFS), runs in time about $\exp\!\big(1.92\,(\ln N)^{1/3}(\ln\ln N)^{2/3}\big)$: **sub-exponential**, faster than any $2^{cn}$ but slower than any polynomial. So Shor's gain is super-polynomial, not "exponential versus exponential". Order of magnitude for a 2048-bit $N$ (constants and lower-order terms omitted, judgement): NFS about $10^{35}$ operations; $(\log_2 N)^3=2048^3\approx8.6\times10^9$ gate-steps for Shor. Shor's $O((\log N)^3)$ (L152) is fine as stated.
8. **Habit for the portfolio:** call Shor "super-polynomial (sub-exponential classical rival)", Grover "quadratic", Deutsch-Jozsa "exponential only against an exact classical algorithm", annealing and VQE "heuristic, no proven speed-up" (M13 taxonomy).

### 4I. L162, L170, L188: three different fidelity sets, and what they mean for depth (M13, erratum)

1. **The three sets.**
   - L162: superconducting 99.9% (1-qubit) / 99.5% (2-qubit); ions 99.99% / 99.9%; silicon spin 99.96% / 99.4%.
   - L170: superconducting 99.9% / "around 98%"; ions 99.9999% / 99.9%.
   - L188: superconducting error $10^{-4}$-$10^{-3}$ (fidelity 99.9-99.99%) / $10^{-2}$-$10^{-1}$ (fidelity 90-99%).
   For the same platform the two-qubit figure runs from 90% to 99.5%. They come from different years and different devices, and none is dated in the text. **Quote one primary source with its date and conditions (F3)**, and always the two-qubit figure, because two-qubit gates dominate the error budget.
2. **Depth from fidelity (M13).** A circuit of $g$ two-qubit gates succeeds with roughly $F^g$ (independent errors, judgement-level model). For $g=100$:
   - $F=0.995$ (L162): $0.995^{100}=0.61$
   - $F=0.98$ (L170): $0.98^{100}=0.13$
   - $F=0.9$ (L188 worst): $0.9^{100}=2.7\times10^{-5}$
3. **Depth for 50% success:** $g_{1/2}=\ln0.5/\ln F$. That is about 138 gates at 99.5%, 34 at 98%, 6.6 at 90%. The rough rule $g\approx1/(1-F)$ (success about $1/e$) gives 200, 50 and 10. Either way: the lecture's own numbers allow circuits of tens to a couple of hundred two-qubit gates, far below the billions Shor needs for RSA (4H item 7). That gap is why error correction (4J) is not optional.
4. **Coherence (L166).** "Several hundred microseconds" divided by a gate time of tens of nanoseconds (typical for superconducting qubits; judgement) gives thousands of gate slots: here the fidelity, not the coherence time, is the binding limit.

### 4J. L184: the threshold theorem stated correctly (M13, erratum, verified)

1. **Lecture (L184):** "the correction process itself can introduce new errors ... This is known as the threshold theorem." That describes the **problem** the theorem solves, not the theorem.
2. **Correct statement:** if every physical operation fails with probability $p$ below a threshold $p_\mathrm{th}$ (and errors are not too correlated), then by encoding into larger codes a quantum computation of any length can be run with logical error as small as you like, with an overhead that grows only polylogarithmically in the size of the computation. References [30] and [31] at L184 are the right papers for this.
3. **How it looks for the surface code** (standard scaling, judgement-level): logical error per round $p_L\approx A\,(p/p_\mathrm{th})^{(d+1)/2}$ for code distance $d$. With $p/p_\mathrm{th}=0.1$: $d=3$ gives $\approx10^{-2}A$; $d=7$ gives $\approx10^{-4}A$. Each step up in $d$ buys another factor of $p/p_\mathrm{th}$, but only if $p<p_\mathrm{th}$. Above threshold, a bigger code makes things worse. The surface-code threshold is commonly quoted near 1% (judgement; see Preskill's NISQ paper for the overhead discussion).
4. **Overhead.** A distance-$d$ rotated surface-code patch uses $d^2$ data and $d^2-1$ measurement qubits: $2d^2-1=97$ physical qubits per logical qubit at $d=7$. This is L15's "large overhead".
5. L184's last sentence ("sets a practical limit on the size ... without error correction") is the right intuition for 4I, but it is not the threshold theorem.

### 4K. Citation mismatches (F3)

Check the reference before you cite it. In §6.5-§6.7 the numbering appears shifted by one:
- **L170** cites [24], [25] (Kitaev; Alicea, both on topological qubits) for superconducting fidelities, and [26] (Krantz et al., a superconducting-qubit guide) for the trapped-ion 99.9999%. The trapped-ion single-qubit record matches [27] (Harty et al. 2014).
- **L172** cites [27] (Harty, trapped ions) for VQE. The VQE review is [28] (Tilly et al.).
- **L174** cites [28] (the VQE review) for zero-noise extrapolation. ZNE is [29] (Temme, Bravyi, Gambetta).
- **L180** cites [29] (error mitigation) for quantum error correction. A QEC review in the list is [33] (Terhal).
- **L204** cites [28] (the VQE review) for NV centres. The NV/colour-centre review is [34] (Ruf et al.).
- Others to distrust: [10] at L111 is a paper on superconductivity in FeSe films, not on qubits; [21] at L166 is about Raman thermometry.
Rule (F3): cite the paper that actually contains the number, not the lecture's bracket.

### 4L. L218 and around: annealing is not the gate model; other loose claims (M13)

1. **L218.** The Volkswagen charging-station example ran on a D-Wave machine. That is a **quantum annealer**: it encodes an optimisation problem as an Ising/QUBO energy landscape and lets the hardware relax towards low energy. It cannot run Shor, Grover or Deutsch-Jozsa, and there is no proven speed-up for such problems: it belongs in the **heuristic** class. The "20%" is a fewer-stations result from a trade-press source ([37]); the classical baseline it was compared with is not stated, so by F3 it is a weak number. A 20% better plan from a better classical solver would be equally possible.
2. **L220.** "Goldman Sachs is exploring" is a statement of interest, not a result.
3. **L216.** "Simulate molecules much more accurately than classical computers": a future claim for fault-tolerant machines; today's NISQ demonstrations are on molecules small enough for classical exact methods (Preskill, NISQ paper).
4. **L117 and L206.** Topological qubits are "inherently fault tolerant" in principle; no working topological qubit with that protection was demonstrated by the lecture's references. Treat as TRL 1-3 (judgement; Week 7 F2).
5. **L114.** Long coherence times help; but ions' slower gates (microseconds versus tens of nanoseconds) mean "gates per coherence time", not raw coherence, is the fair comparison (judgement).

## 5. Clones

These have the same type as the week's quantitative content and its Consolidate task, but use different numbers, functions and cases. Do them after the lecture, before the cold attempt in §6.

### Exercise C6.1 (quantitative)

Run the classical skeleton of Shor's algorithm on $N=55$ with $a=2$. Find the order $r$ by listing powers, apply the corrected success test, and extract the factors. Then say which step a quantum computer would replace, and why the others are cheap.

**Hint:** List $2^x \bmod 55$ for $x=1,2,\dots$ until you hit 1 (double the previous value and reduce). Check "$r$ even and $a^{r/2}\not\equiv-1$" before taking gcds. $-1\equiv54\pmod{55}$.

**Solution sketch:**
1. *Restate.* Given $N=55$, $a=2$. Want $r$, the test, and $\gcd(a^{r/2}\pm1,N)$.
2. *Write state.* $f(x)=2^x \bmod 55$; $r$ is the smallest $r>0$ with $2^r\equiv1$.
3. *Name move.* M13 (Shor's classical skeleton, corrected L150 condition).
4. *Algebra.*
   - $\gcd(2,55)=1$, so $a$ is coprime: continue.
   - Powers: $2,4,8,16,32,9,18,36,17,34,13,26,52,49,43,31,7,14,28,1$ for $x=1,\dots,20$. So $r=20$.
   - $r$ is even. $a^{r/2}=2^{10}=1024\equiv34\pmod{55}$ ($1024=18\times55+34$), and $34\ne54$, so the test passes.
   - $\gcd(34-1,55)=\gcd(33,55)=11$ and $\gcd(34+1,55)=\gcd(35,55)=5$. (Equivalently, with the unreduced power: $\gcd(1023,55)=11$, $\gcd(1025,55)=5$.)
5. *Check.* $5\times11=55$. The order divides $\varphi(55)=4\times10=40$, and 20 does.
6. *Answer.* $r=20$; factors 5 and 11. The quantum computer replaces only "find $r$", which for a 2048-bit $N$ means a period that may be as large as $N$ itself; listing powers is then hopeless. The gcds take a few divisions each (Euclid).

The habit to keep: test $a^{r/2}\not\equiv-1$ **before** taking gcds; that is the line the lecture got backwards.

### Exercise C6.2 (quantitative)

Run Deutsch-Jozsa for $n=2$ with $f(x_1x_2)=1\oplus x_2$ (the function returns the second bit, flipped). (a) Is $f$ constant or balanced? (b) Write the input register after the oracle (with phase kickback), and describe the oracle in gates. (c) Compute the amplitudes of all four outcomes $00,01,10,11$ after the final Hadamards. (d) How many queries would an exact classical algorithm need in the worst case?

**Hint:** Write out the table $f(00),f(01),f(10),f(11)$. After kickback each $\lvert x\rangle$ carries $(-1)^{f(x)}$. The amplitude of outcome $z$ is $\frac{1}{4}\sum_x(-1)^{f(x)+x\cdot z}$.

**Solution sketch:**
1. *Restate.* $n=2$, $f(x_1x_2)=1\oplus x_2$; qubit 1 is written first. Want the type, the post-oracle state and oracle, four amplitudes, a classical query count.
2. *Write state.* After $H^{\otimes2}$ and the $\lvert-\rangle$ ancilla: $\frac12(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)\lvert-\rangle$.
3. *Name move.* M12 (oracle, phase kickback, DJ amplitude sum), M13 (query counts).
4. *Algebra.*
   - (a) $f=1,0,1,0$ on $00,01,10,11$: two zeros and two ones, so **balanced**.
   - (b) Signs $-,+,-,+$: $\frac12(-\lvert00\rangle+\lvert01\rangle-\lvert10\rangle+\lvert11\rangle)=-\lvert+\rangle\lvert-\rangle$, ancilla still $\lvert-\rangle$. Oracle: a CNOT from qubit 2 onto the ancilla, plus an $X$ on the ancilla (the "$1\oplus$").
   - (c) $A_{00}=\frac14(-1+1-1+1)=0$. $A_{01}=\frac14(-1-1-1-1)=-1$. $A_{10}=\frac14(-1+1+1-1)=0$. $A_{11}=\frac14(-1-1+1+1)=0$. Shortcut: $H\lvert+\rangle=\lvert0\rangle$, $H\lvert-\rangle=\lvert1\rangle$, so the output is $-\lvert01\rangle$.
   - (d) $2^{n-1}+1=3$.
5. *Check.* $\sum\lvert A\rvert^2=1$. $A_{00}=0$, as every balanced $f$ must give. The overall minus sign comes from the "$1\oplus$" and is unobservable: $f=x_2$ gives the same measurement. The outcome $01$ is the bit-string $s$ with $f(x)=s\cdot x\oplus1$.
6. *Answer.* Balanced; post-oracle register $-\lvert+\rangle\lvert-\rangle$; the measurement gives $01$ with certainty (amplitudes $0,-1,0,0$), never $00$; a deterministic classical algorithm needs up to 3 queries, the quantum one needs 1.

Note what did the work: the signs from kickback, then cancellation in the sum. Nothing was "computed in parallel" and read out.

### Exercise C6.3 (quantitative)

A (fictional) superconducting processor has two-qubit fidelity $F=99.8\%$. Ignore single-qubit errors. (a) How many two-qubit gates can a circuit contain and still succeed with probability at least 0.5? (b) What does the rule of thumb $g\approx1/(1-F)$ give, and what success probability does that depth have? (c) An algorithm needs 2000 two-qubit gates. What is its success probability on this device, and what two-qubit fidelity would give it 50%?

**Hint:** Success $\approx F^g$. Solve $F^g=0.5$ with logs: $g=\ln0.5/\ln F$. For (c), $F=0.5^{1/g}$.

**Solution sketch:**
1. *Restate.* $F=0.998$. Want $g_{1/2}$, the rule-of-thumb depth and its success, $F^{2000}$, and the $F$ for 50% at $g=2000$.
2. *Write state.* $P_\mathrm{success}\approx F^g$ (independent errors).
3. *Name move.* M13 (depth from fidelity).
4. *Algebra.*
   - (a) $g=\ln0.5/\ln0.998=346.2$, so at most 346 gates ($0.998^{346}=0.500$).
   - (b) $1/(1-0.998)=500$; $0.998^{500}=0.37$ (about $1/e$).
   - (c) $0.998^{2000}=0.018$. Required $F=0.5^{1/2000}=0.99965$, an error of $3.5\times10^{-4}$, about six times smaller than the device's $2\times10^{-3}$.
5. *Check.* Smaller error, longer circuits: halving the error roughly doubles $g$. $0.018$ is close to $e^{-4}=0.018$, as the rule predicts for $g=4/(1-F)$.
6. *Answer.* About 346 gates at 50% success; the rule of thumb gives 500 gates at 37%; a 2000-gate algorithm succeeds 1.8% of the time and needs $F\approx99.965\%$ to reach 50%.

So when a press release quotes a qubit count, ask for the two-qubit fidelity: it, not the count, sets the depth.

### Exercise C6.4 (writing)

Use the shared Harrowmere fact sheet (`STRATEGY.md`, all fictional): the control centre refreshes an AES-256 telemetry key every 60 s per site, the telemetry and SCADA data must stay confidential for 15 years, and a full cryptographic migration takes 5 years. Assume (fictional) that the keys are agreed with RSA-2048. Harrowmere's security lead asks: "How big a quantum computer would it take to break our key exchange, and how far are today's machines from it?" Size the attacker and write a 150-200 word F1 answer. Take a (fictional) future device with two-qubit fidelity 99.8%, as in C6.3.

**Hint:** Count logical qubits first: a standard Shor construction needs about $2n+3$ for an $n$-bit modulus (judgement). Then use 4J: $p_L\approx A\,(p/p_\mathrm{th})^{(d+1)/2}$ with $A=0.1$ and $p_\mathrm{th}=1\%$ (judgement), and $2d^2-1$ physical qubits per logical. Pick a target $p_L$ so that about $10^{10}$ logical operations (4H item 7) mostly succeed. Compare physical with physical: what the lecture says about today's largest machines (Week 7 L88, L94). Finish with Mosca, $x+y>z$ (Day 06, M8).

**Model paragraph:** Harrowmere agrees each 60-second AES-256 telemetry key with RSA-2048 (fictional). Classically that is safe: the best attack, the number field sieve, costs about $10^{35}$ operations. Shor's algorithm breaks it in polynomial time, about $2048^3\approx10^{10}$ gate steps, but needs about $2n+3=4099$ error-corrected logical qubits (judgement). On a device with 99.8% gates, $p/p_\mathrm{th}=0.2$; for a logical error of $10^{-12}$ per step, so that $10^{10}$ steps fail about 1% of the time (judgement), the surface code needs distance 31, or $2\times31^2-1=1921$ physical qubits per logical. That is about 7.9 million physical qubits. The lecture says today's largest machines have "several thousand" qubits (Week 7 L88), and those are physical annealer qubits that cannot run Shor at all (L94), so the gap is roughly a thousandfold or more, and nobody can date when it closes. That uncertainty is why the decision rests on Mosca: with 15 years of confidentiality ($x$) and a 5-year migration ($y$), $x+y=20$ years. Recorded handshakes are exposed if such a machine arrives within 20 years, so Harrowmere should start moving key exchange to post-quantum algorithms now. The caveat: better gates or codes would shrink the 7.9 million, which only strengthens that verdict.

**What a weak answer misses:** It compares the 4,099 logical qubits Shor needs with a physical headline count (not like for like), or treats annealer qubits as gate-model qubits. It skips the error-correction step, so it never sees that the gate fidelity sets the size of the machine: the same arithmetic at 99.9% gives about 880 physical per logical (Day 09). It invents a date for $z$ instead of reasoning from Harrowmere's own $x+y=20$. It says AES-256 is broken, when Grover only halves its key length; the exposure is the RSA handshake that delivers the key. It forgets to label the figures as fictional.

## 6. Cold attempt

Attempt this on paper before opening the sketch. Same type as §5, fresh numbers.

### Exercise C6.5 (quantitative)

Factor $N=33$ with Shor's classical skeleton. First try $a=2$: find its order and apply the corrected test. If it fails, try $a=5$. Give the factors and say in one sentence why the first base failed.

**Hint:** $-1\equiv32\pmod{33}$. List powers mod 33 until you reach 1. The test is "$r$ even and $a^{r/2}\not\equiv-1$".

**Do not open the sketch until you have a written attempt.**

**Solution sketch:**
1. *Restate.* $N=33$; bases $a=2$, then $a=5$. Want each order, the test result, the factors.
2. *Write state.* $r$ = smallest $r>0$ with $a^r\equiv1\pmod{33}$; success if $r$ even and $a^{r/2}\not\equiv32$.
3. *Name move.* M13 (Shor skeleton, corrected L150 test).
4. *Algebra.*
   - $a=2$: $\gcd(2,33)=1$. Powers $2,4,8,16,32,31,29,25,17,1$, so $r=10$, even. But $2^5=32\equiv-1\pmod{33}$: the test **fails**. (Taking gcds anyway gives $\gcd(31,33)=1$ and $\gcd(33,33)=33$, trivial.)
   - $a=5$: $\gcd(5,33)=1$. Powers $5,25,26,31,23,16,14,4,20,1$, so $r=10$. $5^5\equiv23\ne32$: the test passes.
   - $\gcd(23-1,33)=\gcd(22,33)=11$; $\gcd(23+1,33)=\gcd(24,33)=3$.
5. *Check.* $3\times11=33$. Both orders divide $\varphi(33)=2\times10=20$.
6. *Answer.* $N=33=3\times11$, found with $a=5$ ($r=10$, $5^5\equiv23$). Base 2 failed because $2^{r/2}\equiv-1$, so $N$ divides $a^{r/2}+1$ and the gcds are trivial: exactly the case the lecture's L150 presents as success.

If you took the gcds for $a=2$ without testing, you met the failure the lecture hides. Revisit 4H items 1-3.

## 7. Confusion log prompts

Answer each in writing (two or three sentences) after your pass through the lecture. Log the answer in your confusion log with the date.

1. In your own words, where does the answer "go" in Deutsch-Jozsa between the oracle and the final Hadamards? Why would the algorithm fail if the ancilla started in $\lvert0\rangle$?
2. Write the speed-up class (exponential, super-polynomial/sub-exponential rival, quadratic, heuristic) next to each of: Deutsch-Jozsa, Grover, Shor, VQE, quantum annealing. For each, name the classical algorithm you are comparing against.
3. State the threshold theorem without notes, then explain why L184's version describes the problem rather than the result.
4. (Optional) Pick one of the three fidelity sets (L162, L170, L188) and find the primary paper it should cite. What date and device does the number belong to, and how many two-qubit gates does it allow at 50% success?

## 8. Figures

The lecture has one figure, **Fig 6.1 (the Bloch sphere, L54-L58)**, adapted from Ketterer 2016 [39]. It was not exported to `week_6/figures/`, so there is no reading note from the image. From the long description it would show: a unit sphere with $x$, $y$, $z$ axes; $\lvert0\rangle$ at the north pole and $\lvert1\rangle$ at the south pole; a sample state "v" on the surface with its polar angle $\theta$ and azimuthal angle $\varphi$ marked; and $\lvert+\rangle$, $\lvert-\rangle$ on the equator. What to look for if you find it: the state sits **on** the surface (correcting L47, see 4A), and the angle from the north pole is $\theta$, while the amplitudes use $\theta/2$. Quantum Country essay 1 and IBM Quantum Learning lesson 1 have equivalent drawings.

## 9. Course interactive walkthrough

**Identification.** The course's optional puzzle game (`week_6_content.md`, L35-L55) is not named in the export. The best identification is **The Qubit Factory**, https://www.qubitfactory.io/ (medium-high confidence): it is a browser puzzle game about quantum computing, it has a tutorial, it gets harder level by level, and the course's tips mention an "eraser button", which matches a build-your-circuit puzzle. The site is a JavaScript app that did not render as text when checked on 2026-11-10, so the level and tool names below are given by behaviour; match them to what you see on screen. If the game you are given differs, the mapping and questions still apply. Quirk (https://algassert.com/quirk) is the fallback sandbox.

**How to use it (about 30-45 min).**
1. **Tutorial first.** Play every tutorial level in order. They introduce the mechanics: qubits enter, you place gates on their path, and the level checks whether the outputs match a target.
2. **Map each gate to a Day 08 move as you meet it.**
   - Bit flip / NOT tile → $X$ (4B): swaps $\lvert0\rangle$ and $\lvert1\rangle$.
   - Phase flip tile → $Z$ (4B): no visible change on $\lvert0\rangle$/$\lvert1\rangle$ inputs; visible only after an $H$.
   - Hadamard tile → $H$ (4D): sends a definite bit into an equal superposition; two in a row cancel ($H^2=I$).
   - Controlled tile → CNOT (4C): note which wire is the control.
   - Measurement/output checks → the Born rule: probabilities are squared amplitudes.
3. **Eraser.** Use the eraser button to remove placed tiles and try again (the course tip). Treat each erase as an experiment: change one gate, predict the output, then run.
4. **What to try.** (a) Build a NOT out of $H$, $Z$, $H$ ($HZH=X$, 4D item 5). (b) Build a Bell pair: $H$ on one qubit, then a controlled-NOT onto the other (4C). (c) If a level gives you a "phase" puzzle, solve it with $H\cdots H$ around a $Z$, which is phase kickback in miniature. Write the state after each tile in ket notation in your notes; that is the M12 skill.
5. **Stop rule.** You do not need to finish the game (course tip). Stop when the levels start teaching things not in this week's lecture.

**Reflection questions (the course's three, with answers).**
1. *How many gates and concepts did you recognise?* Expected: $X$, $Z$, $H$ and CNOT from Eq 6.2-6.6, plus superposition, measurement and entanglement. If the game has a gate the lecture skips (for example a SWAP or a phase gate), note it: SWAP is three CNOTs, and a phase gate is "a quarter of" $Z$ in the sense $S^2=Z$.
2. *How does this connect to the theory?* Each tile is a unitary matrix acting on the state vector; a level is a circuit; a solved level is a product of matrices that maps the inputs to the targets. Puzzles that need two $H$ tiles around another gate are interference: amplitudes are steered so the unwanted outputs cancel, the same mechanism as Deutsch-Jozsa (4E).
3. *Can you think of a real-world application?* Bell-pair circuits are the core of entanglement-based QKD (Week 4) and teleportation (4G); the $H$-oracle-$H$ pattern is the skeleton of Grover and of Shor's period finding. An honest answer adds the caveat from 4I: the game's gates are perfect, while real two-qubit gates fail often enough to cap circuits at about 140 two-qubit gates at 99.5% (4I item 3), far short of a useful algorithm.
