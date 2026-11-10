# Day 08: Quantum Computing I: Circuits, Interference and Deutsch-Jozsa

**Time:** ~3 h · **Feeds:** Week 6 lecture (§6.1 and §6.2, L32-104), inventory rows W1 Consolidate (optional circuit simulator), W6 Apply, W6 Consolidate (optional puzzle game) · **Companion:** week06_companion.md §1-§4 (notation, errata) and §9 (The Qubit Factory walkthrough)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min moves M12.1 to M12.8 below · 50 min quantitative drills (Exercises 8.1 to 8.7; skip the ones marked *stretch* if you are past time) and the Quirk lab (steps 0-2; step 3 is optional) · 45 min writing on the running case (Exercises 8.8 to 8.10) · 15 min companion pointer and confusion log.

The core is Moves M12.1 to M12.7, Quirk lab steps 0-2, and Exercises 8.1, 8.3, 8.4, 8.5, 8.6, 8.8 and 8.9. Exercises 8.2 (gate algebra drill) and 8.7 (query counts) are stretch, the lab's Deutsch-Jozsa step 3 is optional, and 8.10 is a short writing piece you can move to Day 09's retrieval block.

## Why this matters

You already own the maths of today from Module 3: kets, Pauli matrices, tensor products, measurement. What you have never done is chain them into a **circuit** and read off an answer. That is the whole skill for Week 6 §6.1-6.2, and it is the only way to see why "a quantum computer tries all answers at once" is wrong. The Week 1 lecture says it (L70), the Week 6 lecture says it again (L131), and a vendor will say it to Harrowmere. Today you will trace a circuit where every input is "in play" and the output is still one random answer, and then a circuit (Deutsch-Jozsa) where amplitudes are arranged to **cancel**, so the right answer comes out with certainty.

The lecture gives the gates as matrices and the Deutsch-Jozsa recipe as five steps, but never shows a single state being multiplied through. It also skips the trick that makes the recipe work (phase kickback), muddles the starting state of the extra qubit (L93), and calls the algorithm "exponentially faster" without saying faster than *what* (L99). Today fills all three gaps.

The engineering view, in one line: a quantum circuit is a sequence of unitary matrix multiplications on a vector of $2^n$ complex amplitudes, followed by one sample from the squared magnitudes. The design problem is to make the sample useful.

## Core concepts

### Move M12.1: The qubit and the Bloch sphere (erratum L47)

**Idea.** A qubit is $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ with $|\alpha|^2+|\beta|^2 = 1$ (lecture Eq 6.1). An overall phase $e^{i\gamma}$ changes no measurement, so only two real numbers matter, and every pure state can be written

$$|\psi\rangle = \cos\tfrac{\theta}{2}\,|0\rangle + e^{i\varphi}\sin\tfrac{\theta}{2}\,|1\rangle, \qquad 0\le\theta\le\pi,\ 0\le\varphi<2\pi .$$

Read $\theta$ as latitude measured down from the north pole and $\varphi$ as longitude. The point on the sphere is the **Bloch vector** $(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)$, which always has length 1.
- North pole ($\theta = 0$): $|0\rangle$. South pole ($\theta = \pi$): $|1\rangle$.
- Equator ($\theta = \pi/2$): equal superpositions. $\varphi = 0$ is $|+\rangle = (|0\rangle+|1\rangle)/\sqrt2$; $\varphi = \pi$ is $|-\rangle = (|0\rangle-|1\rangle)/\sqrt2$.
- Why $\theta/2$: $|0\rangle$ and $|1\rangle$ are orthogonal (90° apart as vectors) but sit at opposite poles (180° apart on the sphere). The half-angle maps one to the other.
- $P(0) = \cos^2(\theta/2)$ is the "height" on the sphere: $P(0) = (1+z)/2$.

**Erratum L47.** The lecture says "the distance from the centre represent[s] the probability amplitude of the state". That is wrong. Every pure state, whatever its amplitudes, sits **on the surface**, at distance exactly 1. The amplitudes set *where* on the surface (latitude gives $|\alpha|^2$ and $|\beta|^2$, longitude gives the relative phase). Points strictly inside the ball are **mixed** states (statistical mixtures, for example a qubit entangled with something you are not tracking); the centre is the completely random 50/50 mixture. So distance from the centre measures purity, not amplitude (standard; IBM Quantum Learning, *Basics of quantum information*, see Read next).

*Link to Day 03 (Move M4).* A resonant $\pi/2$ pulse rotates the Bloch vector by 90° (pole to equator); a $\pi$ pulse rotates it by 180° (pole to pole). Clock, magnetometer and qubit are the same two-level object; a single-qubit gate is a controlled rotation of this sphere.

*Worked clone.* $\theta = \pi/3$, $\varphi = \pi/2$: $|\psi\rangle = \cos(\pi/6)|0\rangle + i\sin(\pi/6)|1\rangle = 0.866|0\rangle + 0.5i|1\rangle$. So $P(0) = 0.75$, $P(1) = 0.25$. Bloch vector $(0,\ 0.866,\ 0.5)$, length 1, in the northern hemisphere on the $+y$ meridian.

*You've got it when* you can place $|0\rangle, |1\rangle, |+\rangle, |-\rangle$ on a sketch of the sphere, and say in one sentence why L47 is wrong.

### Move M12.2: Single-qubit gates X, Z, Y and H

**Idea.** Gates are unitary matrices (lecture Eqs 6.2-6.6). In the basis $|0\rangle = (1,0)^T$, $|1\rangle = (0,1)^T$:

| Gate | Matrix | On the basis | Bloch picture |
|---|---|---|---|
| $X$ (bit flip) | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $|0\rangle\leftrightarrow|1\rangle$ | 180° about $x$ |
| $Z$ (phase flip) | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $|0\rangle\to|0\rangle$, $|1\rangle\to-|1\rangle$ | 180° about $z$; swaps $|+\rangle\leftrightarrow|-\rangle$ |
| $Y = iXZ$ | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$ | $|0\rangle\to i|1\rangle$, $|1\rangle\to -i|0\rangle$ | 180° about $y$ |
| $H$ (Hadamard) | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | $|0\rangle\to|+\rangle$, $|1\rangle\to|-\rangle$ | 180° about the axis halfway between $x$ and $z$ |

Four facts carry the whole day:
1. **$Y = iXZ$.** Multiply it out: $XZ = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and $i$ times that is $Y$. So $Y$ is "a bit flip and a phase flip", which is what the lecture's loose "bit-phase gate" (L68) means. It does not just "introduce a phase shift between" the states; it flips them too (judgement on the lecture's wording).
2. **$H^2 = I.$** $H$ undoes itself. Check: $H(H|0\rangle) = H|+\rangle = \tfrac12(|0\rangle+|1\rangle) + \tfrac12(|0\rangle-|1\rangle) = |0\rangle$.
3. **$HZH = X$ and $HXH = Z$.** $H$ swaps the roles of bit and phase. This is why phase information can be turned into a measurable bit.
4. **$H^{\otimes n}|0\cdots0\rangle$ is uniform.** One $H$ on each of $n$ qubits gives $\frac{1}{\sqrt{2^n}}\sum_{x}|x\rangle$, all $2^n$ bit strings with amplitude $2^{-n/2}$. For $n = 2$: $\tfrac12(|00\rangle+|01\rangle+|10\rangle+|11\rangle)$.

*Worked clone.* $H$ on $|1\rangle$, then $Z$: $Z|-\rangle = (|0\rangle+|1\rangle)/\sqrt2 = |+\rangle$. Then $H$ again: $H|+\rangle = |0\rangle$. So $HZH|1\rangle = |0\rangle = X|1\rangle$, as fact 3 says.

*You've got it when* you can write all four matrices from memory and verify $Y = iXZ$ and $H^2 = I$ in under two minutes.

### Move M12.3: Two qubits, CNOT, the Bell state, and reading circuits right to left

**Basis order.** Two qubits live in a 4-dimensional space. Write the basis in binary order with the **first (control) qubit as the left bit**: $|00\rangle, |01\rangle, |10\rangle, |11\rangle$, as vector entries 1 to 4. The lecture's CNOT (Eq 6.5) uses exactly this order: it leaves entries 1 and 2 alone (control = 0) and swaps entries 3 and 4 (control = 1, target flipped). So $\text{CNOT}|x,y\rangle = |x,\ y\oplus x\rangle$.

**Circuits as products.** A circuit diagram reads left to right in time, but the matrix product reads **right to left**, because the first gate must act on the vector first. "$H$ on qubit 1, then CNOT" is the matrix $\text{CNOT}\cdot(H\otimes I)$. Getting this order wrong is the commonest circuit error.

**The Bell state, derived.** Start in $|00\rangle = (1,0,0,0)^T$.

$$H\otimes I = \frac{1}{\sqrt2}\begin{pmatrix}1&0&1&0\\0&1&0&1\\1&0&-1&0\\0&1&0&-1\end{pmatrix},\qquad (H\otimes I)|00\rangle = \tfrac{1}{\sqrt2}(1,0,1,0)^T = \tfrac{1}{\sqrt2}(|00\rangle+|10\rangle).$$

In words: $H$ put qubit 1 into $|+\rangle$, qubit 2 is still $|0\rangle$, so the state is the product $|+\rangle|0\rangle$. Now CNOT swaps entries 3 and 4:

$$|\Phi^+\rangle = \text{CNOT}\,(H\otimes I)\,|00\rangle = \tfrac{1}{\sqrt2}(1,0,0,1)^T = \tfrac{1}{\sqrt2}\big(|00\rangle+|11\rangle\big).$$

- Measure both: $P(00) = P(11) = \tfrac12$, $P(01) = P(10) = 0$. Each qubit alone is a fair coin; the two coins always agree.
- **Entangled, not just correlated.** A product state $(a|0\rangle+b|1\rangle)(c|0\rangle+d|1\rangle)$ has coefficients $ac, ad, bc, bd$, so (coefficient of $|00\rangle$)×(coefficient of $|11\rangle$) equals (coefficient of $|01\rangle$)×(coefficient of $|10\rangle$). For $|\Phi^+\rangle$: $\tfrac12 \ne 0$. No product state can give it (lecture L75).

*You've got it when* you can write $H\otimes I$ as a 4×4 matrix from the rule "$H$ acts on the left bit", and derive $|\Phi^+\rangle$ on a blank page in three lines.

### Move M12.4: Interference, not parallelism (errata Week 1 L70 and Week 6 L131)

**Idea.** Apply $H$, then $Z$, then $H$ to $|0\rangle$, and follow the amplitudes as **paths**:

| Step | State | Amplitude of $|0\rangle$ | Amplitude of $|1\rangle$ |
|---|---|---|---|
| start | $|0\rangle$ | 1 | 0 |
| $H$ | $|+\rangle$ | $\tfrac{1}{\sqrt2}$ | $\tfrac{1}{\sqrt2}$ |
| $Z$ | $|-\rangle$ | $\tfrac{1}{\sqrt2}$ | $-\tfrac{1}{\sqrt2}$ |
| $H$ | $|1\rangle$ | $\tfrac12 - \tfrac12 = 0$ | $\tfrac12 + \tfrac12 = 1$ |

Without the $Z$ (circuit H-H) the last row is $\tfrac12+\tfrac12 = 1$ for $|0\rangle$ and $\tfrac12-\tfrac12 = 0$ for $|1\rangle$: you get $|0\rangle$ back (Day 01 warm-up Q4). In both cases the qubit was "in both states" in the middle, and in both cases the output is **certain**, decided by whether the two paths into each output **add or cancel**. Swap $Z$ for a general phase $P(\phi) = \text{diag}(1, e^{i\phi})$ and $P(0) = \cos^2(\phi/2)$: this is Day 04's Mach-Zehnder fringe (Move M6.1) with $H$ as the beam splitter.

**Why a uniform superposition alone is useless.** $H^{\otimes n}$ makes all $2^n$ inputs present with equal amplitude. Suppose you also compute $f$ into a second register: $\frac{1}{\sqrt{2^n}}\sum_x|x\rangle|f(x)\rangle$. Now measure. You get **one** pair $(x, f(x))$, with $x$ uniformly random, each with probability $1/2^n$. That is exactly what a classical computer gets by picking one random input and evaluating it. "Doing all calculations at once" buys nothing unless further gates make the wrong answers' amplitudes cancel before you measure. That cancellation needs structure in the problem, which is why quantum speed-ups are problem-specific.

**Correct the lecture.** Week 1 L70 ("able to perform multiple calculations simultaneously, thanks to the superposition") and Week 6 L131 ("superposition... allows quantum algorithms to perform multiple calculations simultaneously") both state the parallelism myth. The correct statement: a quantum algorithm manipulates $2^n$ amplitudes and then samples **one** outcome; it beats a classical algorithm only when interference concentrates the probability on the useful outcomes (Aaronson, *The Limits of Quantum Computers*, named in the spec's sources).

*You've got it when* you can fill in the H-Z-H table from memory and explain, in two sentences to a non-physicist, why measuring a uniform superposition gives one random answer.

### Move M12.5: The oracle and phase kickback

**The oracle.** An algorithm gets $f:\{0,1\}^n\to\{0,1\}$ as a black-box gate. It must be reversible, so it writes $f(x)$ into an extra **ancilla** qubit by XOR:

$$U_f\,|x\rangle|y\rangle = |x\rangle\,|y\oplus f(x)\rangle .$$

If $y = 0$ the ancilla becomes $f(x)$; if $y = 1$ it becomes $\text{NOT}\,f(x)$. One use of $U_f$ is **one query**.

**Kickback.** Prepare the ancilla in $|-\rangle = (|0\rangle - |1\rangle)/\sqrt2$. Then

$$U_f|x\rangle|-\rangle = |x\rangle\,\frac{|f(x)\rangle - |1\oplus f(x)\rangle}{\sqrt2} = (-1)^{f(x)}\,|x\rangle|-\rangle .$$

Check both cases: if $f(x) = 0$ the bracket is $|0\rangle - |1\rangle$ (unchanged); if $f(x) = 1$ it is $|1\rangle - |0\rangle = -(|0\rangle-|1\rangle)$. The ancilla comes out **unchanged**, and the value of $f$ has moved into a **sign** on the input register. On a superposition of inputs each $|x\rangle$ gets its own sign, $\sum_x a_x|x\rangle \to \sum_x (-1)^{f(x)}a_x|x\rangle$, and signs are exactly what interference (Move M12.4) can turn into a measurable answer.

The lecture never names this. Its step 3 (L95), "apply the function $f$ to the $n$ qubits and leave the last qubit unchanged", is describing kickback from the outside: the oracle does act on the ancilla, but because the ancilla is $|-\rangle$ it ends unchanged.

*You've got it when* you can derive $(-1)^{f(x)}|x\rangle|-\rangle$ in two lines and say why the ancilla must be $|-\rangle$, not $|+\rangle$ (for $|+\rangle$, the bracket $|f\rangle + |1\oplus f\rangle$ is the same for both values of $f$, so nothing kicks back).

### Move M12.6: Deutsch's algorithm ($n = 1$)

**Problem.** $f:\{0,1\}\to\{0,1\}$ is either constant ($f(0) = f(1)$) or balanced ($f(0)\ne f(1)$). Classically you must query both inputs: 2 queries.

**Circuit.** Qubit 1 in $|0\rangle$, ancilla in $|1\rangle$. $H$ on both, $U_f$, $H$ on qubit 1, measure qubit 1.
1. $H\otimes H\,|0\rangle|1\rangle = |+\rangle|-\rangle = \tfrac{1}{\sqrt2}(|0\rangle+|1\rangle)|-\rangle$.
2. Kickback: $\tfrac{1}{\sqrt2}\big((-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\big)|-\rangle$.
3. $H$ on qubit 1. The amplitude of $|0\rangle$ collects both paths with a plus sign:

$$\text{amp}(0) = \tfrac12\big[(-1)^{f(0)} + (-1)^{f(1)}\big].$$

Constant: $\pm1$, so you measure 0 with certainty. Balanced: $\tfrac12(1-1) = 0$, so you measure 1 with certainty. **One query** decides a global property ($f(0)\oplus f(1)$) without learning either value.

*You've got it when* you can tabulate $\text{amp}(0)$ for all four one-bit functions without looking.

### Move M12.7: Deutsch-Jozsa for $n = 2$ as an amplitude sum (erratum L93, honest note on L99)

**Problem (lecture L89).** $f:\{0,1\}^n\to\{0,1\}$ is **promised** to be constant or balanced (exactly half the inputs give 1). Decide which. (The lecture spells it "Deutsch-Josza"; the author is Richard Jozsa.)

**The recipe, repaired.** Lecture step 1 (L93) says "start with $n+1$ qubits in the $|0\rangle$ state" and then writes $|0\rangle\cdots|0\rangle|1\rangle$. The written state is the right one: the $n$ input qubits start in $|0\rangle$ and the **ancilla starts in $|1\rangle$** (in hardware: start in $|0\rangle$, apply $X$). The $H$ in step 2 then makes it $|-\rangle$, which is what Move M12.5 needs. If you follow the words instead and leave the ancilla in $|0\rangle$, it becomes $|+\rangle$, nothing kicks back, and the input register returns to $|0\cdots0\rangle$ every time: the algorithm would report "constant" for every $f$.

**The amplitude sum.** After steps 1-3 the input register is $\frac{1}{\sqrt{2^n}}\sum_x(-1)^{f(x)}|x\rangle$. Step 4 applies $H^{\otimes n}$. The amplitude of output $|0\cdots0\rangle$ is the overlap with the uniform state, so

$$\text{amp}(0\cdots0) = \frac{1}{2^n}\sum_x(-1)^{f(x)}, \qquad n = 2:\ \ \text{amp}(00) = \tfrac14\sum_{x\in\{00,01,10,11\}}(-1)^{f(x)} .$$

(More generally $\text{amp}(z) = \frac{1}{2^n}\sum_x(-1)^{f(x)+x\cdot z}$, where $x\cdot z$ is the bitwise dot product mod 2; standard, Nielsen and Chuang §1.4.4.)
- Constant $f$: all four terms have the same sign, $\text{amp}(00) = \pm1$, $P(00) = 1$.
- Balanced $f$: two $+1$ and two $-1$, $\text{amp}(00) = 0$, $P(00) = 0$.

That is lecture step 5 (L97), now with the reason.

*Worked clone 1 (balanced).* Let $f(x_1x_2) = x_1$, the first bit: $f(00) = 0$, $f(01) = 0$, $f(10) = 1$, $f(11) = 1$. Its oracle is a single CNOT from qubit 1 to the ancilla.
- After kickback: $\tfrac12(|00\rangle + |01\rangle - |10\rangle - |11\rangle) = |-\rangle|+\rangle$ (factor it: the sign depends only on $x_1$).
- $\text{amp}(00) = \tfrac14(1+1-1-1) = 0$. So "balanced", with certainty.
- Where does the probability go? $H\otimes H$ maps $|-\rangle|+\rangle$ to $|1\rangle|0\rangle$: you measure $|10\rangle$ every time. Via the general formula, $\text{amp}(10) = \tfrac14\sum_x(-1)^{x_1+x_1} = \tfrac14\times4 = 1$.

*Worked clone 2 (constant).* $f(x) = 1$ for all $x$; the oracle is an $X$ on the ancilla. After kickback every term carries $-1$: $-\tfrac12(|00\rangle+|01\rangle+|10\rangle+|11\rangle)$. $\text{amp}(00) = \tfrac14(-4) = -1$, $P(00) = 1$. The global sign is unobservable.

**Query counts and the honest note (L91, L99).**
- **Deterministic classical**, worst case: you might see $2^{n-1}$ equal outputs in a row from a balanced $f$, so you need $2^{n-1}+1$ queries to be sure (L91 is right). For $n = 2$: 3 queries. Quantum: 1.
- **Randomised classical**: query $k$ inputs chosen at random. If any two outputs differ, $f$ is balanced, for certain. If all agree, answer "constant". A constant $f$ is never misjudged; a balanced $f$ fools you only if all $k$ random outputs agree, probability $2\times(1/2)^k = 2^{1-k}$ (sampling with replacement). With $k = 10$ that is $1/512\approx0.2\%$, **for any $n$**.
- So L99's "exponentially faster than any known classical algorithm" holds only against classical algorithms that must be right **with certainty**. Against a classical algorithm allowed a tiny error rate, the gap is 1 query against about 10: a constant factor. Deutsch-Jozsa is a clean demonstration of interference and a separation in the exact, black-box (query) setting, not evidence of a practical speed-up (standard; judgement on emphasis). Real exponential claims (Shor) are Day 09.

*You've got it when* you can compute $\text{amp}(00)$ for any $f$ on two bits from its truth table, state the ancilla fix for L93, and give the randomised-classical caveat with the $2^{1-k}$ number.

### Move M12.8: Teleportation in one paragraph (lecture L102)

Alice holds an unknown qubit $|\psi\rangle$ and wants Bob to have it. They share one Bell pair $|\Phi^+\rangle$ in advance (Move M12.3), one half each. Alice runs CNOT and $H$ on her two qubits ($|\psi\rangle$ and her half of the pair) and measures both, getting two classical bits $(m_1, m_2)$, each outcome with probability $\tfrac14$. She sends the two bits to Bob by any ordinary channel. Bob applies $X^{m_2}$ then $Z^{m_1}$ to his half, and it is now exactly $|\psi\rangle$. Three consequences: **(1)** before the bits arrive Bob's qubit is a 50/50 mixture with no information, so nothing travels faster than light; **(2)** Alice's measurement destroys her copy, so no-cloning (Day 06) is respected; **(3)** the cost is one Bell pair plus 2 classical bits per qubit moved (standard; IBM Quantum Learning, *Basics of quantum information*, the lesson after "Quantum circuits"). The lecture's "share a quantum state without actually transmitting the state itself" (L102) is loose: the state is carried by the pre-shared entanglement plus two classical bits; no physical carrier of $|\psi\rangle$ crosses, but information does, at light speed or slower.

*You've got it when* you can say what is consumed (one Bell pair, 2 bits) and why it is not faster than light.

### Lab: Quirk walkthrough (stand-in for the Week 1 circuit simulator)

The Week 1 Consolidate section links an optional circuit simulator with a histogram, a "use percentage scale" button and "+"/"–" qubit controls. The export does not name it, and the sprint could not identify it with confidence (best guess in the spec: Quantum Länd Circuit Designer). This walkthrough uses **Quirk**, a free in-browser drag-and-drop simulator: <https://algassert.com/quirk>. The steps carry over to any circuit simulator. Toolbox labels below are as they appear at the time of writing; if your screen differs, hover over a gate to see its name.

Quirk shows **exact** probabilities live as you edit (no sampling), so a "50%" really means $\tfrac12$. Every wire starts in $|0\rangle$.

**0. Calibrate the bit order (2 min).** Drag an $X$ (from "Half Turns") onto the top wire only. Drag a "Chance" or amplitude display (from "Displays") across the top two wires. Note which basis label lights up at 100%. That tells you whether Quirk lists the top wire as the left or the right bit. This sprint writes the **first (top) qubit as the left bit**, so translate if Quirk's labels run the other way. Delete the $X$.

**1. Bell state (5 min).** Put $H$ on wire 1. In the next column put a control dot "•" (from "Probes") on wire 1 and an $X$ on wire 2: that is CNOT. Read the display: 50% on $|00\rangle$, 50% on $|11\rangle$, 0% on the others. Each wire's own "% on" readout shows 50%. Now delete the CNOT: you get 50% on $|00\rangle$ and $|10\rangle$ (in your calibrated order), a product state. The CNOT is what ties the coins together.

**2. Interference (5 min).** On one wire build H-H: the wire returns to 0% on. Insert $Z$ between them (H-Z-H): 100% on. Add a Bloch-sphere display (from "Displays") after each gate and watch the vector go pole → equator → equator (other side) → opposite pole. Then replace $Z$ with a quarter-turn or eighth-turn phase gate and watch the "% on" move along $\sin^2(\phi/2)$.

**3. Deutsch-Jozsa for $f(x) = x_1$ (optional, 10 min).** Skip this step if you are past time: Move M12.7 and Exercise 8.6 cover the same ground on paper. Three wires: inputs on wires 1-2, ancilla on wire 3.
- Column 1: $X$ on wire 3 (ancilla to $|1\rangle$, the L93 fix).
- Column 2: $H$ on all three wires.
- Column 3 (the oracle for $f = x_1$): "•" on wire 1, $X$ on wire 3.
- Column 4: $H$ on wires 1 and 2.
- Read wires 1-2: wire 1 at 100% on, wire 2 at 0%, i.e. $|10\rangle$, matching Move M12.7. Not $|00\rangle$, so "balanced".
- Swap the oracle for a constant one: delete the column 3 gates (that is $f = 0$), or put a lone $X$ on wire 3 ($f = 1$). Wires 1-2 now read $|00\rangle$ at 100%.
- Now break it on purpose: delete the column 1 $X$, restore the $x_1$ oracle, and confirm that wires 1-2 read $|00\rangle$ whatever the oracle is. That is the L93 confusion made visible.

**Reflect (the Week 1 prompt).** In which circuit did superposition alone give a useful answer? (None: in step 1 it gave a random one; in steps 2 and 3 the certainty came from the final $H$ making paths cancel.)

**The Qubit Factory (Week 6 optional game).** The Week 6 Consolidate "game" is, with medium-high confidence, The Qubit Factory: <https://www.qubitfactory.io/>. Its puzzles route qubits through gates on a factory floor and test the same moves as today (X, Z, H, CNOT, interference, Bell pairs). Do the tutorial and the first levels after this lab. The level-by-level walkthrough is in `content/companions/week06_companion.md` §9.

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. Basis order is always $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ with the first qubit on the left.

### Exercise 8.1 (quantitative)

(a) A qubit has $\theta = 2\pi/3$ and $\varphi = \pi/4$. Write its amplitudes, its measurement probabilities and its Bloch vector, and check the vector's length. (b) Which $\theta$ gives $P(0) = 0.9$? (c) A classmate, quoting L47, says "a state with $P(0) = 0.9$ sits at distance 0.9 from the centre". Correct them in one sentence.

**Hint:** $\alpha = \cos(\theta/2)$, $\beta = e^{i\varphi}\sin(\theta/2)$; Bloch vector $(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ (Move M12.1).

**Solution sketch:**
- *Restate:* amplitudes, probabilities and position for one state; invert $P(0)$ for $\theta$; fix L47.
- *Write state:* $\theta = 2\pi/3$ (120°), $\varphi = \pi/4$ (45°).
- *Name move:* M12.1.
- *Algebra:* (a) $\alpha = \cos(\pi/3) = 0.5$, $\beta = e^{i\pi/4}\sin(\pi/3) = 0.866\,e^{i\pi/4}$. $P(0) = 0.25$, $P(1) = 0.75$. $\sin\theta = 0.866$, $\cos\theta = -0.5$, $\cos\varphi = \sin\varphi = 0.707$: Bloch vector $(0.612,\ 0.612,\ -0.5)$; length $\sqrt{0.375+0.375+0.25} = 1$. (b) $\cos^2(\theta/2) = 0.9\Rightarrow\theta = 2\arccos\sqrt{0.9} = 0.644$ rad $= 36.9°$.
- *Check:* $z = -0.5$ and $P(0) = (1+z)/2 = 0.25$. Consistent. A state below the equator should favour $|1\rangle$, and it does.
- *Answer:* (a) $0.5|0\rangle + 0.866e^{i\pi/4}|1\rangle$; $P(0) = 0.25$, $P(1) = 0.75$; vector $(0.612, 0.612, -0.5)$, length 1. (b) $\theta = 36.9°$ (0.644 rad). (c) Every pure state is on the surface at distance 1; $P(0) = 0.9$ fixes the latitude ($\theta = 36.9°$), not the distance, and only mixed states lie inside.

### Exercise 8.2 (quantitative) (stretch)

(a) Verify $Y = iXZ$ and show $ZX = -XZ$. (b) Compute $HXH$ as a matrix and name it. (c) For $n = 3$, apply $H^{\otimes3}$ to $|000\rangle$: what is the amplitude of $|101\rangle$, and the probability of each outcome? (d) For $n = 30$, what is the probability of any one bit string?

**Hint:** Multiply the 2×2 matrices directly (Move M12.2). For (c) and (d) the amplitude is $2^{-n/2}$.

**Solution sketch:**
- *Restate:* two matrix identities, then uniform-superposition amplitudes.
- *Write state:* matrices from Move M12.2.
- *Name move:* M12.2.
- *Algebra:* (a) $XZ = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $i\,XZ = \begin{pmatrix}0&-i\\i&0\end{pmatrix} = Y$. $ZX = \begin{pmatrix}0&1\\-1&0\end{pmatrix} = -XZ$. (b) $XH = \tfrac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$, then $H(XH) = \tfrac12\begin{pmatrix}2&0\\0&-2\end{pmatrix} = Z$. (c) amplitude $1/\sqrt8 = 0.354$; probability $1/8 = 0.125$ for each of the 8 strings, including $|101\rangle$. (d) $1/2^{30} = 9.3\times10^{-10}$.
- *Check:* 8 outcomes × 0.125 = 1. In (a), $ZX = -XZ$ means the order of a bit flip and a phase flip changes only an overall sign, which is unobservable on its own.
- *Answer:* $Y = iXZ$ and $ZX = -XZ$; $HXH = Z$; amplitude 0.354, probability 0.125 each; $9.3\times10^{-10}$ per string for 30 qubits.

### Exercise 8.3 (quantitative)

The Bell circuit $\text{CNOT}\,(H\otimes I)$ is run on the other three basis inputs. (a) Write the matrix product for "$X$ on qubit 1, then $H$ on qubit 1, then CNOT" applied to $|00\rangle$, in the correct order. (b) Compute the outputs for inputs $|10\rangle$, $|01\rangle$ and $|11\rangle$. (c) For each, give $P(00), P(01), P(10), P(11)$. (d) Use the product test to show the $|10\rangle$ output is entangled.

**Hint:** Rightmost acts first. $H$ on the left bit sends $|1\cdot\rangle$ to $(|0\cdot\rangle - |1\cdot\rangle)/\sqrt2$. Then CNOT flips the right bit wherever the left bit is 1 (Move M12.3). Product test: $c_{00}c_{11} = c_{01}c_{10}$.

**Solution sketch:**
- *Restate:* run the Bell circuit on three inputs; probabilities; entanglement test.
- *Write state:* inputs $|10\rangle, |01\rangle, |11\rangle$.
- *Name move:* M12.3.
- *Algebra:* (a) $\text{CNOT}\,(H\otimes I)\,(X\otimes I)\,|00\rangle$, and $(X\otimes I)|00\rangle = |10\rangle$. (b) $|10\rangle\to\tfrac{1}{\sqrt2}(|00\rangle - |10\rangle)\to\tfrac{1}{\sqrt2}(|00\rangle - |11\rangle)$. $|01\rangle\to\tfrac{1}{\sqrt2}(|01\rangle + |11\rangle)\to\tfrac{1}{\sqrt2}(|01\rangle + |10\rangle)$. $|11\rangle\to\tfrac{1}{\sqrt2}(|01\rangle - |11\rangle)\to\tfrac{1}{\sqrt2}(|01\rangle - |10\rangle)$. (c) $|10\rangle$ input: $P(00) = P(11) = 0.5$. $|01\rangle$ and $|11\rangle$ inputs: $P(01) = P(10) = 0.5$. (d) $c_{00}c_{11} = \tfrac{1}{\sqrt2}\times(-\tfrac{1}{\sqrt2}) = -0.5$, $c_{01}c_{10} = 0$. Unequal, so not a product.
- *Check:* $|10\rangle$ and $|00\rangle$ give the same probabilities but different signs. Measurement in the computational basis cannot tell $|\Phi^+\rangle$ from $|\Phi^-\rangle$; an $H$ on each qubit before measuring can. That is interference again.
- *Answer:* the four inputs give the four Bell states $\tfrac{1}{\sqrt2}(|00\rangle\pm|11\rangle)$ and $\tfrac{1}{\sqrt2}(|01\rangle\pm|10\rangle)$; each has two outcomes at 0.5; all are entangled.

### Exercise 8.4 (quantitative)

(a) Trace $H\,P(\phi)\,H|0\rangle$ with $P(\phi) = \text{diag}(1, e^{i\phi})$ and show $P(0) = \cos^2(\phi/2)$. Evaluate for $\phi = \pi$, $\pi/2$ and $\pi/3$. (b) A 3-qubit register is put in $H^{\otimes3}|000\rangle$ and an oracle writes $f(x)$ into a fourth qubit. You then measure all four. What is the probability that you learn $f(101)$? How many runs do you expect before you have seen all 8 values of $f$? Compare with a classical computer.

**Hint:** (a) Two paths into $|0\rangle$, with amplitudes $\tfrac12$ and $\tfrac12e^{i\phi}$ (Move M12.4). $|1+e^{i\phi}|^2 = 2+2\cos\phi$. (b) Each $x$ comes out with probability $1/8$. Collecting all 8 is the coupon-collector problem: $8\,(1+\tfrac12+\cdots+\tfrac18)$ runs on average.

**Solution sketch:**
- *Restate:* interference fringe for a general phase; then the "parallelism" circuit measured.
- *Write state:* (a) $|0\rangle$; (b) $\tfrac{1}{\sqrt8}\sum_x|x\rangle|f(x)\rangle$.
- *Name move:* M12.4.
- *Algebra:* (a) $H|0\rangle = \tfrac{1}{\sqrt2}(|0\rangle+|1\rangle)$; $P(\phi)$ gives $\tfrac{1}{\sqrt2}(|0\rangle+e^{i\phi}|1\rangle)$; $H$ gives $\text{amp}(0) = \tfrac12(1+e^{i\phi})$, so $P(0) = \tfrac14(2+2\cos\phi) = \cos^2(\phi/2)$. $\phi = \pi$: 0 (the H-Z-H case). $\phi = \pi/2$: 0.5. $\phi = \pi/3$: 0.75. (b) $P(\text{see } x = 101) = 1/8 = 0.125$. Expected runs to see all 8: $8\times2.718 = 21.7$. A classical computer needs exactly 8 evaluations.
- *Check:* (a) $\phi = 0$ gives 1 (H-H returns $|0\rangle$). Same $\cos^2(\phi/2)$ as Day 04's Mach-Zehnder.
- *Answer:* (a) $P(0) = \cos^2(\phi/2)$: 0, 0.5, 0.75. (b) 0.125 per run; about 22 runs on average to see all 8 values, against 8 classical evaluations. Superposition without interference is *worse* than classical here.

### Exercise 8.5 (quantitative)

Run Deutsch's algorithm (Move M12.6) for all four one-bit functions: $f_a = 0$, $f_b = 1$, $f_c(x) = x$, $f_d(x) = 1-x$. (a) Give the state of qubit 1 after the oracle, and $\text{amp}(0)$ after the final $H$. (b) What do you measure in each case? (c) How many classical queries would a certain answer need?

**Hint:** After kickback qubit 1 is $\tfrac{1}{\sqrt2}\big((-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\big)$, and $\text{amp}(0) = \tfrac12[(-1)^{f(0)}+(-1)^{f(1)}]$ (Moves M12.5, M12.6).

**Solution sketch:**
- *Restate:* four functions through one circuit.
- *Write state:* $|+\rangle|-\rangle$ before the oracle.
- *Name move:* M12.5 (kickback) and M12.6.
- *Algebra:* (a) $f_a$: $|+\rangle$, $\text{amp}(0) = 1$. $f_b$: $-|+\rangle$, $\text{amp}(0) = -1$. $f_c$: $|-\rangle$, $\text{amp}(0) = 0$. $f_d$: $-|-\rangle$, $\text{amp}(0) = 0$. (b) $f_a, f_b$: measure 0 with probability 1. $f_c, f_d$: measure 1 with probability 1. (c) 2 classical queries (both inputs).
- *Check:* the global sign in $f_b$ and $f_d$ never shows in a probability; the relative sign between $|0\rangle$ and $|1\rangle$ is what $H$ converts into a bit.
- *Answer:* constant → 0, balanced → 1, each with probability 1, using 1 query against 2.

### Exercise 8.6 (quantitative)

Deutsch-Jozsa with $n = 2$. (a) Let $f$ be the parity $f(x_1x_2) = x_1\oplus x_2$. Is it balanced? Compute $\text{amp}(00)$, then factor the post-oracle register and find the measured output. Describe its oracle in gates. (b) Let $f = 0$ for all inputs. Compute $\text{amp}(00)$. (c) Let $f(x) = 1$ only for $x = 11$ (AND), which breaks the promise. Compute $\text{amp}(00)$ and $P(00)$. What would the algorithm wrongly conclude a quarter of the time? (d) Repeat (a) with the ancilla left in $|0\rangle$, as L93's wording suggests. What is measured?

**Hint:** $\text{amp}(00) = \tfrac14\sum_x(-1)^{f(x)}$ (Move M12.7). For (a), $(-1)^{x_1\oplus x_2} = (-1)^{x_1}(-1)^{x_2}$, so the register factors. For (d), an ancilla in $|+\rangle$ is not changed by the oracle and no sign appears.

**Solution sketch:**
- *Restate:* three functions through DJ, then the broken-ancilla version.
- *Write state:* truth tables. Parity: 0, 1, 1, 0. Zero: 0, 0, 0, 0. AND: 0, 0, 0, 1.
- *Name move:* M12.7, with M12.5.
- *Algebra:* (a) two 1s out of four: balanced. $\text{amp}(00) = \tfrac14(1-1-1+1) = 0$. Register $\tfrac12(|00\rangle-|01\rangle-|10\rangle+|11\rangle) = |-\rangle|-\rangle$, and $H\otimes H$ gives $|11\rangle$: measured with probability 1. Oracle: two CNOTs onto the ancilla, one controlled by each input qubit. (b) $\tfrac14(1+1+1+1) = 1$, $P(00) = 1$. (c) $\tfrac14(1+1+1-1) = 0.5$, so $P(00) = 0.25$, and the other 0.75 is spread over the non-zero outputs. A quarter of the time it says "constant" for a function that is neither, which is why DJ is a **promise** problem. (d) Every input returns $|00\rangle$ with probability 1, so DJ says "constant" for every $f$, including the balanced parity.
- *Check:* in (a), the general formula gives $\text{amp}(11) = \tfrac14\sum_x(-1)^{(x_1\oplus x_2) + x_1 + x_2} = \tfrac14\times4 = 1$. Matches.
- *Answer:* (a) balanced, $\text{amp}(00) = 0$, output $|11\rangle$; (b) $\text{amp}(00) = 1$; (c) $\text{amp}(00) = 0.5$, $P(00) = 0.25$; (d) always $|00\rangle$, the L93 confusion breaks the algorithm.

### Exercise 8.7 (quantitative) (stretch)

(a) How many queries does a deterministic classical algorithm need in the worst case for $n = 2$, $n = 10$ and $n = 30$? (b) A randomised classical algorithm makes $k = 10$ random queries. What is the worst-case chance it misjudges a balanced $f$? (c) What is the smallest $k$ for an error below $10^{-6}$? (d) Write one sentence, in F1 part 4 style, stating the speed-up honestly.

**Hint:** Deterministic: $2^{n-1}+1$ (L91). Randomised: a balanced $f$ fools you only if all $k$ outputs agree, probability $2^{1-k}$ (Move M12.7). Solve $2^{1-k} < 10^{-6}$.

**Solution sketch:**
- *Restate:* three deterministic counts, one error probability, one inverse problem, one honest sentence.
- *Write state:* $n = 2, 10, 30$; $k = 10$; target $10^{-6}$.
- *Name move:* M12.7.
- *Algebra:* (a) $2^1+1 = 3$; $2^9+1 = 513$; $2^{29}+1 = 536\,870\,913\approx5.4\times10^{8}$. (b) $2^{-9} = 1/512 = 1.95\times10^{-3}$. (c) $2^{1-k} < 10^{-6}\Rightarrow k-1 > 6\log_2 10 = 19.9$, so $k = 21$ (error $2^{-20} = 9.5\times10^{-7}$; $k = 20$ gives $1.9\times10^{-6}$, too big).
- *Check:* the randomised count does not depend on $n$ at all, while the deterministic count doubles with each extra bit.
- *Answer:* (a) 3, 513, about $5.4\times10^{8}$. (b) about 0.2%. (c) $k = 21$. (d) "Deutsch-Jozsa needs 1 query where an exact classical algorithm needs $2^{n-1}+1$, but a classical algorithm allowed a one-in-a-million error needs only 21, so the separation is exponential only against certainty, and the problem has no practical use."

### Exercise 8.8 (writing)

**Vendor pitch.** A supplier's slide to Harrowmere Water & Power reads: "Our quantum computer tries all pump schedules at once. Your 220 pumps give more on/off combinations than there are atoms in a planet; a classical computer checks them one by one, our machine checks them all in a single step." Harrowmere's facts (fictional, shared fact sheet in STRATEGY.md): 220 pumps, 4 electricity tariff bands, an energy bill of £18 million a year *with* the current classical optimiser, which saves 6% against an unoptimised schedule. Write the correction paragraph (about 200 words) for Harrowmere's operations director. Use the numbers.

**Hint:** Compute $2^{220}$ (one on/off pattern for one tariff band) and what one measurement of a 220-qubit uniform superposition returns. Name what does produce speed-ups (interference on structured problems), and say what is proven for unstructured search: the lecture's $O(\sqrt N)$ Grover bound (L102; Day 09 has the detail). Then find the real baseline: not brute force, but the optimiser already in use. £18 million is the bill *after* its 6% saving, so the unoptimised bill is £18 m / 0.94 and today's saving is the difference, not 6% × £18 m. Say which baseline any further "percentage point" refers to. End with a decision.

**Model paragraph:**
The claim that a quantum computer "checks all schedules in a single step" is wrong, and it should not drive our decision. Our 220 pumps (fictional) have $2^{220}\approx1.7\times10^{66}$ on/off patterns in a single tariff band, and about $10^{265}$ across all four bands. 220 qubits can be placed in an equal superposition of every pattern, but a measurement then returns **one** pattern at random, each with probability about $6\times10^{-67}$: no better than drawing a schedule out of a hat. A quantum algorithm helps only when its gates make the amplitudes of bad schedules cancel, which needs problem structure. For a search with no exploitable structure, the best proven quantum method takes about $\sqrt N$ steps: $2^{110}\approx1.3\times10^{33}$ for one band, still far beyond any machine. Brute force is not our baseline anyway. Our current optimiser never enumerates schedules and already cuts the bill by 6% against an unoptimised schedule: from about £19.1 million to today's £18 million, a saving of about £1.15 million a year (fictional). So the only question that matters for Harrowmere is how many further percentage points of today's £18 million bill a quantum method saves on top of that optimiser; each point is worth about £180,000 a year. Before any trial, we should require the supplier to benchmark against our optimiser on our own pump and tariff data.

**What a weak answer misses:** It replaces "tries every schedule" with "explores every schedule in superposition", the same myth reworded. It gives no numbers, so the director cannot see that one measurement means one random schedule. It overcorrects to "quantum computers are useless", ignoring that a quadratic (Grover) gain is real but, at $10^{33}$ steps, irrelevant here. It compares the quantum machine with brute force instead of with the optimiser that already saves 6% (F3: compare like with like), so it never prices the remaining headroom (about £180,000 per further point of today's £18 million bill). It computes today's saving as 6% × £18 m = £1.08 m, forgetting that £18 m is already the optimised bill (the saving is £18 m / 0.94 − £18 m ≈ £1.15 m). And it ends without a decision.

### Exercise 8.9 (writing)

*Inventory row W6 Apply.* Harrowmere's technology-watch group (fictional) asks for a 200-300-word note on **how a quantum algorithm actually gets an advantage and what the benefit is**, using Deutsch-Jozsa as the worked example, and what that means for the pump-scheduling claim in Exercise 8.8. Include one computed amplitude and the honest caveat.

**Hint:** Follow the structure: the problem (constant versus balanced), the three tricks (uniform superposition, kickback, a final $H$ layer that makes paths interfere), the $n = 2$ amplitude sum for a stated $f$, the query counts, then the caveat (randomised classical). Name the figure of merit: number of queries. Finish with one line on what the vendor in Exercise 8.8 would have to show.

**Model paragraph:**
A quantum algorithm does not win by computing every answer at once; it wins by making wrong answers cancel. Deutsch-Jozsa shows the mechanism on a toy problem. A black box computes a function $f$ of $n$ bits that is promised to be either constant or balanced (half its outputs 1), and the task is to tell which. The figure of merit is the number of calls to the box. The algorithm puts $n$ qubits into an equal superposition of all $2^n$ inputs and calls the box once with a helper qubit prepared so that each input's answer comes back as a sign, $+1$ or $-1$ ("phase kickback"). A final layer of Hadamard gates then adds those signs together in the amplitude of the all-zero output: $\tfrac{1}{2^n}\sum_x(-1)^{f(x)}$. For two bits and the balanced function "first bit", the four signs are $+,+,-,-$ and the amplitude is $\tfrac14(1+1-1-1) = 0$, so the all-zero output never appears; for a constant function it appears every time. One call settles the question, where an algorithm that must be certain needs $2^{n-1}+1$ calls: 513 for ten bits. The honest caveat is that a classical algorithm allowed a 0.2% error needs only ten random calls whatever $n$ is, so the problem is a demonstration, not an application. For Harrowmere the lesson is concrete: pump scheduling across 220 pumps and 4 tariff bands (fictional) has no known structure of the Deutsch-Jozsa kind, so a vendor must name the interference structure its algorithm exploits and then beat our current optimiser on our data, on the baseline set out in Exercise 8.8. Until then this belongs on the watch list, not the budget.

**What a weak answer misses:** It explains the speed-up as parallelism ("evaluates all inputs simultaneously") instead of cancellation of amplitudes. It states "exponentially faster" without saying against what (L99), so it omits the randomised-classical caveat. It gives no computed amplitude and no query count, so nothing is quantitative. It copies the lecture's step 1 with the ancilla in $|0\rangle$ (L93). Its ending is generic ("quantum computing could help utilities") instead of asking what structure, if any, Harrowmere's scheduling problem offers an interference-based algorithm.

### Exercise 8.10 (writing)

Harrowmere's telemetry lead (fictional) has read that "quantum teleportation transmits information instantly" and asks whether it could cut the delay on the control network's longest link, 160 km of dark fibre (fictional fact sheet). Answer in about 100 words. Take light in fibre as $2\times10^{8}$ m/s.

**Hint:** Move M12.8: what must be shared in advance, what must be sent classically, and what the receiver has before the classical bits arrive. Compute the one-way fibre delay.

**Model paragraph:**
No. Teleportation moves a qubit's state, not data faster than light, so it cannot beat the 160 km link's one-way delay of $160\ \text{km}/(2\times10^{8}\ \text{m/s}) = 0.8$ ms (fictional link). The two ends must first share an entangled pair, then the sender must send two ordinary bits over a normal channel, here that same fibre; until they arrive, the receiver's qubit is a random 50/50 state carrying no information. Each teleported qubit therefore costs one pre-shared pair plus two classical bits and arrives no sooner than 0.8 ms. Our telemetry is classical readings, which the fibre already carries at that speed; teleportation has nothing to offer it.

**What a weak answer misses:** It says "it's faster but not practical yet", which keeps the false premise. It forgets the two classical bits, which are the reason there is no speed-up, and so never sees that teleportation over the 160 km link is bounded by the same 0.8 ms. It does not say what the receiver holds before the bits arrive (nothing usable), and it does not answer the actual question about Harrowmere's link.

## Anti-patterns / Common mistakes

- **Reading the circuit product left to right.** How you'd notice: your Bell circuit gives $\tfrac{1}{\sqrt2}(|00\rangle+|10\rangle)$ or a wrong sign. Instead: write the matrices right to left, first gate rightmost: $\text{CNOT}\,(H\otimes I)$.
- **Mixing up the basis order.** How you'd notice: CNOT seems to flip the wrong qubit, or Quirk shows $|01\rangle$ where you expected $|10\rangle$. Instead: fix "first qubit = left bit" and calibrate the simulator with a single $X$ before trusting its labels.
- **"Superposition means it computes everything at once".** How you'd notice: your explanation has no step where amplitudes cancel. Instead: say what one measurement returns, then name the interference step (Week 1 L70, Week 6 L131).
- **Putting the DJ ancilla in $|0\rangle$.** How you'd notice: every function comes out "constant". Instead: ancilla in $|1\rangle$, then $H$ gives $|-\rangle$ (L93 fix).
- **"Distance from the centre of the Bloch sphere = amplitude".** How you'd notice: you place a pure state inside the sphere. Instead: pure states are on the surface; latitude sets $|\alpha|^2$ (L47 fix).
- **Quoting "exponentially faster" for Deutsch-Jozsa without a baseline.** How you'd notice: no mention of randomised algorithms. Instead: "exponential only against exact deterministic classical algorithms; about 10 random queries give 0.2% error" (L99).
- **Treating a global sign as physical.** How you'd notice: you claim $-|00\rangle$ and $|00\rangle$ give different results. Instead: only *relative* signs between terms can interfere.
- **"Teleportation is faster than light".** How you'd notice: you forgot the two classical bits. Instead: one Bell pair + 2 classical bits, at light speed or slower.

## Done when

Without notes, in 40 minutes, you can do all of the following. Pass mark: 7 of 8.

1. Write $|\psi\rangle$ in Bloch form, place $|0\rangle, |1\rangle, |\pm\rangle$, and correct L47.
2. Write $X$, $Y$, $Z$, $H$ from memory and verify $Y = iXZ$, $H^2 = I$ and $HZH = X$.
3. Derive $\text{CNOT}\,(H\otimes I)|00\rangle = \tfrac{1}{\sqrt2}(|00\rangle+|11\rangle)$ with explicit vectors, in the right product order.
4. Fill in the H-Z-H amplitude table and explain why measuring $H^{\otimes n}|0\cdots0\rangle$ gives one random answer.
5. Derive phase kickback $U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$.
6. Compute $\text{amp}(00) = \tfrac14\sum_x(-1)^{f(x)}$ for a given two-bit $f$ and say what is measured; state the L93 ancilla fix.
7. Give deterministic ($2^{n-1}+1$) and randomised ($2^{1-k}$ error) classical query counts, and state DJ's speed-up honestly.
8. Explain teleportation's resources (one Bell pair, 2 classical bits) and why it is not faster than light.

## Companion pointer and confusion log

Open `content/companions/week06_companion.md` §1-§4 and read lecture L32-104 with Moves M12.1 to M12.7 beside you. Do the Qubit Factory tutorial with §9. Log every notation clash (basis order, product order, which qubit is the ancilla, "Josza" versus Jozsa) with its lecture line.

| Where (lecture § / line) | Symbol, unit or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| | | | | |
| | | | | |

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 07 (simulation, M11).**
1. How many bytes does a classical computer need to store the state of 30 spin-½ particles at 8 bytes per amplitude? And for 40 (the corrected Table 5.2 row)?
2. In an optical lattice, which wins in the Mott insulator, tunnelling $J$ or interaction $U$?
3. One sentence: analogue versus digital quantum simulation.

**From Day 05 / Day 04 (sensing checkpoint).**
4. State $\Phi = k_\text{eff}gT^2$ with $T$ defined. By what factor does the phase grow if $T$ goes from 0.2 s to 2 s?
5. A gravimeter has $20\ \mu\text{Gal}/\sqrt{\text{Hz}}$. How long must it average to reach $1\ \mu\text{Gal}$?

**From Day 01 (F1, M1).**
6. Using $2^{10}\approx10^{3}$, estimate $2^{40}$ to an order of magnitude. Name the six parts of F1.

*Answers.* 1. $8\times2^{30} = 8.6\times10^{9}$ bytes, about 8.6 GB; $8\times2^{40} = 8.8\times10^{12}$ bytes, about 8.8 TB (not the lecture's 880 GB). 2. $U$: when interaction dominates tunnelling, each site holds a fixed number of atoms and transport stops. 3. Analogue: a controllable system whose own Hamiltonian mimics the target's; digital: the target's time evolution is broken into a sequence of gates on qubits. 4. $T$ is the time between pulses; $(2/0.2)^2 = 100$. 5. $(20/1)^2 = 400$ s. 6. $2^{40} = (2^{10})^4\approx10^{12}$ (exactly $1.1\times10^{12}$); classical limit with a number, quantum mechanism, figure of merit, quantified gain, maturity and practicality, verdict with a caveat.

## Read next

- Matuschak and Nielsen, *Quantum computing for the very curious* (Quantum Country, essay 1), <https://quantum.country/qcvc>. Read all of it: qubits, $X$, $H$, CNOT and circuits, with built-in spaced-repetition questions. It is the best second pass on Moves M12.2 to M12.4.
- IBM Quantum Learning, *Basics of quantum information*, <https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information>. Read lessons 1-3 (single systems, multiple systems, quantum circuits) for the Bloch-free, matrix-first version of today, and skim the following lesson for teleportation (Move M12.8). Preskill's NISQ paper (<https://arxiv.org/abs/1801.00862>) is for Day 09.
