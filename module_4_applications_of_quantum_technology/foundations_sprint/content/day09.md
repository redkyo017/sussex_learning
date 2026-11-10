# Day 09: Computing II, Speed-ups, Noise and Error Correction

**Time:** ~3 h · **Feeds:** Week 6 lecture (§6.3 to §6.8), Week 7 lecture L84-100 (qubit counts, advantage), inventory rows W6 Consolidate (also the M13 parts of W1 Consolidate and W5 Consolidate) · **Companion:** week06_companion.md §3 (notation and units), §4 (errata L131/L139, L150, L162/L170/L188, L184), §5 (clones)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min Move M13 below · 50 min quantitative drills (Exercises 9.1 to 9.6; 9.1(d) and 9.6 are *stretch*) · 45 min writing on the running case (Exercises 9.7 to 9.9) · 15 min companion pointer and confusion log.

The core is Moves M13.1 to M13.6 and Exercises 9.2, 9.3, 9.4, 9.5, 9.7 and 9.8. Exercise 9.1(a)-(c) and (e) are short if you did Move M13.1 carefully; 9.1(d), 9.6 and 9.9 are stretch work for today or for Day 10's warm-up.

## Why this matters

The Week 6 Consolidate task asks for "speed-up or new problem classes, quantitative and qualitative". Every number you need for it is in today's six moves, and the lecture gets several of them wrong. It lists database search as an *exponential* speed-up (L131) and then, eight lines later, correctly as *quadratic* (L139). It calls the best classical factoring algorithm exponential (L133, L152) when it is sub-exponential. It garbles the last step of Shor's algorithm (L150) and states the threshold theorem backwards (L184). And it gives three different sets of gate fidelities on three pages (L162, L170, L188).

As a backend engineer you already think in big-O, and you have deployed RSA. Today turns that into four habits:
- sorting any quantum claim into the right speed-up class;
- running Shor's classical skeleton by hand;
- converting a gate fidelity into a usable circuit depth;
- converting "1,000 qubits" into how many *logical* qubits that buys.

With those four, you can price a vendor's claim in a paragraph.

The engineering view, in one line: a quantum computer is a co-processor that is exponentially good at a very few structured problems, quadratically good at brute force, unproven at everything else, and today too noisy to run long programs.

## Core concepts

### Move M13.1: The speed-up taxonomy (sort before you quote)

**Idea.** "Faster" means nothing until you say *faster than what, on which problem, by what scaling*. Write $n$ for the input size in bits ($n = \log_2 N$ for a number $N$). Four classes cover every claim in the module:

| Class | Example | Quantum cost | Best known classical cost | Status | Lecture |
|---|---|---|---|---|---|
| **Exponential** (super-polynomial) | Shor: factoring, discrete log | $O(n^3)$ gates, polynomial (L152 gives $O((\log N)^3)$, the same thing) | Number field sieve (NFS): $\exp\!\big(c\,n^{1/3}(\log n)^{2/3}\big)$, **sub-exponential** | Proven quantum algorithm; no proof that no fast classical algorithm exists | L133-152 |
| **Simulation** | Time evolution of a generic quantum many-body system | Polynomial in particle number and time | Exponential memory, $8\cdot2^N$ bytes (Day 07, M11) | Strong for generic dynamics; clever classical methods win on many special cases | L216; Week 5 |
| **Quadratic** | Grover: unstructured search, $\approx(\pi/4)\sqrt N$ queries | $O(\sqrt N)$ | $O(N)$, $N/2$ on average | Proven optimal for black-box search | L102, L139 |
| **Heuristic / unproven** | Annealing, VQE, QAOA, quantum machine learning | Unknown in general | Mature classical heuristics | No proven speed-up on practical problems | L172, L218-222 |

Three errata ride on this table.
- **L131 versus L139, database search.** L131 lists "database searches" among exponential speed-ups; L139 says quadratic. Grover is quadratic, and for black-box search no quantum algorithm can do better (standard result; Aaronson draft). The same sentence (L131) repeats the "multiple calculations simultaneously" myth from Week 1 L70: the gain comes from interference, then one measured outcome (Day 08).
- **L133 and L152, "exponential" classical factoring.** The best classical algorithm, the number field sieve, runs in time $\exp\!\big((64/9)^{1/3}(\ln N)^{1/3}(\ln\ln N)^{2/3}\big)$ (standard number-theory result; judgement on dropping the lower-order term). That grows faster than any polynomial but slower than $2^{cn}$. The gap between Shor and the NFS is still enormous, but "sub-exponential" is the correct word. "Exponential" is right only for naive trial division, about $\sqrt N = 2^{n/2}$ steps.
- **"Exponential speed-up" is a claim about the best *known* classical algorithm.** Nobody has proved that factoring has no fast classical algorithm (Aaronson draft makes this point at length).

*Worked clone (RSA-1024, $n = 1024$).*
- Trial division: $\sqrt N = 2^{512}\approx10^{154}$ steps.
- NFS: $\ln N = 1024\ln2 = 709.8$, $\ln\ln N = 6.565$, exponent $= 1.923\times709.8^{1/3}\times6.565^{2/3} = 60.1$, so about $e^{60.1}\approx1.3\times10^{26}\approx2^{87}$ operations.
- Shor: $n^3 = 1024^3\approx1.1\times10^{9}$ gates.

These are scaling shapes with constants dropped, not runtimes (judgement). The lesson is the *shape*: polynomial against sub-exponential against exponential.

*You've got it when* you can place any claim in one of the four rows, say which line of the lecture misplaces database search, and say why "sub-exponential" is not a pedantic correction.

### Move M13.2: Shor's classical skeleton, on $N = 21$

**Idea.** Shor's algorithm is mostly classical number theory. The quantum computer does one job: find the **period** (order) $r$ of $f(x) = a^x \bmod N$, the smallest $r>0$ with $a^r\equiv1 \pmod N$. It does this with the quantum Fourier transform, which turns the periodic pattern into peaks at multiples of $1/r$ (L148; the QFT derivation is skipped on purpose). Everything around that step is cheap classical code.

The recipe (corrected; see erratum below):
1. Pick a random $a$ with $1 < a < N$. Compute $\gcd(a, N)$. If it is not 1, you have a factor already (L146).
2. **Quantum step:** find the order $r$ of $a$ modulo $N$.
3. If $r$ is odd, go back to step 1.
4. Compute $y = a^{r/2} \bmod N$. If $y\equiv-1 \pmod N$ (that is, $y = N-1$), go back to step 1.
5. Otherwise $\gcd(y-1, N)$ and $\gcd(y+1, N)$ are non-trivial factors of $N$.

Why step 5 works: $a^r - 1 = (a^{r/2}-1)(a^{r/2}+1)\equiv 0 \pmod N$, so $N$ divides the product. $N$ does not divide $a^{r/2}-1$ (otherwise the order would be $r/2$), and step 4 ensured $N$ does not divide $a^{r/2}+1$. So each bracket shares a proper factor with $N$.

*Worked clone ($N = 21$, $a = 2$).* $\gcd(2, 21) = 1$. Powers of 2 modulo 21:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $2^x \bmod 21$ | 2 | 4 | 8 | 16 | 11 | 1 |

($2^5 = 32 = 21 + 11$; $2^6 = 2\times11 = 22 = 21+1$.) So $r = 6$, which is even. Then $y = 2^{3} = 8$, and $8\not\equiv -1$ (that would be 20). So $\gcd(7, 21) = 7$ and $\gcd(9, 21) = 3$. Indeed $21 = 3\times7$.

**Erratum L150.** The lecture writes the period as $r = 2^s r'$ "where $r'$ is the non-trivial factor of N", and gives "$a^{r/2}+1\equiv0 \bmod N$" as the condition for success. Both are wrong. The period is not built from a factor of $N$ (here $r = 6$ and the factors are 3 and 7). And $a^{r/2}\equiv-1$ is the **failure** case: it makes $\gcd(a^{r/2}+1, N) = N$, a trivial factor. The correct condition is $r$ even **and** $a^{r/2}\not\equiv-1 \pmod N$; then take $\gcd(a^{r/2}\pm1, N)$.

**Erratum L135.** The lecture says the classical second step "is computationally expensive". It is not. Euclid's algorithm computes a gcd of $n$-bit numbers in $O(n^2)$ bit operations, and fast modular exponentiation is similarly cheap (standard; judgement on the exact exponent). The **only** expensive step is the period finding, which is exactly why it is the one handed to the quantum computer.

*You've got it when* you can run steps 1-5 on a fresh $N$ with a pencil, and name both conditions that send you back to step 1.

### Move M13.3: Grover in numbers, $\approx(\pi/4)\sqrt N$

**Idea.** Grover's algorithm searches $N$ unsorted items for one marked item using an oracle that recognises it. Each iteration rotates the state a small angle $2\theta$ towards the marked item, where $\sin\theta = 1/\sqrt N$. After $k$ iterations the success probability is

$$P_k = \sin^2\!\big((2k+1)\theta\big),$$

which peaks near $k\approx\frac{\pi}{4}\sqrt N$ (standard result; Aaronson draft for the $\sqrt N$ optimality).

*Worked clone ($N = 10^{6}$).*
- $\theta\approx10^{-3}$, so $k\approx(\pi/4)\times10^{3} = 785$ iterations, with $P_{785}\approx1.0$.
- Classical search checks $N/2 = 5\times10^{5}$ items on average.
- The ratio is about $5\times10^{5}/785\approx640$.

Two catches the lecture leaves out.
- **Overshoot.** Grover is not "run longer, get better". At $k = 1570$ (double the optimum) the state has rotated past the target and $P\approx0$.
- **Clock speed.** The ratio counts queries, not seconds. Suppose a classical query costs 1 ns, and an error-corrected Grover iteration costs 1 µs (judgement: an optimistic order of magnitude). Then the quantum machine wins only when $(\pi/4)\sqrt N\times10^{-6} < (N/2)\times10^{-9}$, that is $N > \big((\pi/2)\times10^{3}\big)^2\approx2.5\times10^{6}$. At $N = 10^{6}$ the classical search (0.5 ms) beats Grover (0.785 ms).

L139 adds the practical catch: the data must be loaded into an oracle the quantum computer can query in superposition, which is itself costly.

*You've got it when* you can compute the iteration count for any $N$ in one line, and explain why a quadratic speed-up can lose to a faster clock.

### Move M13.4: Fidelity to depth, success $\approx F^{g}$

**Idea.** If every two-qubit gate succeeds with fidelity $F$ and errors are independent, a circuit of $g$ such gates succeeds with probability roughly $F^{g}$ (judgement: a crude model that ignores single-qubit gates, readout and error correlations, but good to an order of magnitude). Setting $F^{g} = \tfrac12$:

$$g_{1/2} = \frac{\ln 0.5}{\ln F}\approx\frac{0.693}{1-F}.$$

*Worked clone.*
- $F = 0.995$ (L162, superconducting two-qubit): $g_{1/2} = 0.693/0.00501 = 138$. After about 138 gates the result is a coin toss.
- $F = 0.999$ (L162 and L170, trapped-ion two-qubit): $g_{1/2}\approx693$.

A useful algorithm needs millions to billions of gates (judgement). So without error correction, today's devices run circuits that are wide but very shallow.

**Erratum L162/L170/L188, three fidelity sets.** For superconducting two-qubit gates the lecture gives 99.5% (L162), "around 98%" (L170), and error rates of $10^{-2}$ to $10^{-1}$, that is 90-99% (L188). For trapped-ion single-qubit gates it gives 99.99% (L162) and 99.9999% (L170). These come from different papers, years and conditions, and some citation numbers do not match their references: L170's [24] and [25] point to topological-qubit papers, and L162's silicon figure cites [18], a trapped-ion paper. Pick one primary source, quote it with its date and conditions (F3), and never compare platforms using figures from different lines. In $g_{1/2}$ terms the spread is large: 34 gates at 98%, about 7 at 90%, 138 at 99.5%.

**Coherence, $T_1$ and $T_2$.** $T_1$ is the energy-relaxation time ($|1\rangle$ decays to $|0\rangle$). $T_2$ is the dephasing time (the relative phase of a superposition is lost), and $T_2\le2T_1$ (standard; judgement on depth). What matters is the ratio of coherence time to gate time. L166 gives superconducting coherence of "several hundred microseconds" with dynamical decoupling. With two-qubit gates of order 50 ns (judgement), that is a few thousand gate times. The per-gate fidelity already includes decoherence during the gate, so in practice the $F^g$ budget, not $T_2$ alone, is the binding limit (judgement).

*You've got it when* you can turn any fidelity into $g_{1/2}$ in your head with $0.693/(1-F)$, and list the three inconsistent fidelity lines.

### Move M13.5: Error correction, the threshold theorem stated correctly

**Idea.** Quantum error correction (QEC) encodes one **logical** qubit in many **physical** qubits. Repeated parity checks ("syndrome measurements") detect errors without measuring, and so destroying, the encoded state (L182).

**The threshold theorem (correct statement).** There is a threshold error rate $p_\text{th}$ such that if every physical operation fails with probability $p < p_\text{th}$, the logical error rate can be made **arbitrarily small**. The cost in extra qubits and gates grows only polylogarithmically in $1/\varepsilon$, where $\varepsilon$ is the target logical error. So it is polynomial overall (this is what the lecture's own references [30] and [31] prove).

**Erratum L184.** The lecture says that "the correction process itself can introduce new errors ... This is known as the threshold theorem". That is the *problem* the theorem solves, not the theorem. Its last sentence, "a practical limit on the size ... of quantum computers that can be built without error correction", inverts the message. Below threshold, error correction lets the computer grow without limit. Above it, adding correction makes things worse.

**Numbers to carry (judgement; consistent with Preskill 2018).**
- The surface code, the leading code for 2D chips, has a threshold of about $p_\text{th}\approx10^{-2}$ (1%).
- Below threshold, a working rule for its logical error per cycle is $p_L\approx0.1\,(p/p_\text{th})^{(d+1)/2}$, where the code distance $d$ is odd (judgement: a standard heuristic, not a law).
- A distance-$d$ patch uses about $2d^2$ physical qubits.
- Realistic physical:logical ratios come out at order $10^{2}$ to $10^{3}$, and worse near threshold.

*Worked clone.* Physical error $p = 10^{-3}$ (a 99.9% gate), target $p_L\le10^{-12}$:
- $0.1\times(0.1)^{(d+1)/2}\le10^{-12}$ needs $(d+1)/2 = 11$, so $d = 21$.
- That is $2\times21^2 = 882$ physical qubits per logical qubit.

At $p = 5\times10^{-3}$ (the 99.5% gate) the ratio $p/p_\text{th} = 0.5$ forces $d = 73$ and about $1.1\times10^{4}$ physical per logical. Better gates shrink the overhead enormously. That is why "99.5% versus 99.9%" is not a rounding detail.

**Physical versus logical (Week 7 L94).** Headline qubit counts are physical. Week 7 L88 reports annealers "with several thousand qubits". Those are annealing qubits, not gate-model logical qubits: at about $10^{3}$ physical per logical they would not make even a handful of logical qubits (judgement).

*You've got it when* you can state the threshold theorem in one sentence without the word "limit", and estimate $d$ and the physical:logical ratio from $p$.

### Move M13.6: NISQ, VQE, error mitigation, annealing versus gate model, platforms

**NISQ**: *noisy intermediate-scale quantum*. That means machines of roughly 50 to a few hundred physical qubits (Preskill 2018) with no error correction, limited to shallow circuits (Move M13.4).

**VQE** (L172), in one sentence: a classical optimiser tunes the parameters of a short quantum circuit to minimise the measured energy of a Hamiltonian. It is a hybrid loop that fits NISQ depth, with no proven speed-up.

**Zero-noise extrapolation (ZNE)** (L174), in one sentence: run the same circuit with the noise deliberately amplified by factors $\lambda = 1, 2, \ldots$ and extrapolate the measured result back to $\lambda = 0$. *Worked clone (fictional numbers).* $E(1) = -1.00$, $E(2) = -0.90$. A straight line gives $E(0) = 2E(1) - E(2) = -1.10$. The price is many more shots, and error mitigation does not scale to long circuits the way error correction does (judgement).

**Annealing versus the gate model.**
- *Gate model:* a universal digital machine. Circuits of gates, any algorithm (Shor, Grover), and error correction is possible.
- *Quantum annealing:* an analogue machine. It slowly changes a Hamiltonian so that the system settles towards the low-energy state of an optimisation problem.
- Annealers are special-purpose, cannot run Shor or Grover, have no general proven speed-up, and their qubit counts are not comparable with gate-model counts (judgement; Preskill 2018 discusses the open question).
- The lecture's optimisation example (L218) is an annealer result presented inside a gate-model chapter. The lecture does not state the classical baseline its "20%" was measured against, so by F3 it is a weak number and says nothing about the best classical optimiser. Read it as a heuristic result, row 4 of the taxonomy.

**Platforms** (values as the lecture states them, with lines; the trend column is judgement).

| Platform | Qubit | Operating conditions | Fidelities in the lecture | Strength | Main barrier |
|---|---|---|---|---|---|
| Superconducting | Josephson circuit, microwave control (L111, L200) | dilution fridge, about 20 mK (L111) | 1q 99.9%, 2q 99.5% (L162); 2q about 98% (L170); 2q error $10^{-2}$-$10^{-1}$ (L188); coherence several hundred µs with decoupling (L166) | chip fabrication, integrates with electronics (L111, L200) | noise: flux, charge, quasiparticles (L168); wiring and cooling at scale (judgement) |
| Trapped ion | ions held in vacuum, lasers or microwaves (L114, L198) | ultra-high vacuum; stable optics (L114) | 1q 99.99% (L162) or 99.9999% (L170); 2q 99.9% (L162, L170) | long coherence, highest fidelities (L114) | scaling the optics; slow gates (L114, L198; slow gates judgement) |
| Photonic | polarisation of single photons (L202) | photons travel at room temperature; detectors often cryogenic (judgement) | "high" but not quantified (L188) | low decoherence in flight; networking (L202) | efficient sources and detectors; two-photon gates (L202) |
| Spin qubits (silicon, quantum dots) | electron spins in semiconductor dots (L162, L206) | cryogenic, roughly 0.1-1 K (judgement) | 1q 99.96%, 2q 99.4% (L162; citation [18] mismatched, see M13.4) | semiconductor-industry compatible (L206) | sensitive to environmental noise (L206) |
| Neutral atoms | atoms in optical tweezers, Rydberg interactions for 2q gates | vacuum, laser-cooled (judgement) | not in the lecture | large reconfigurable arrays (judgement) | 2q fidelity and atom loss (judgement) |
| NV centres / topological | diamond defects (L204); anyons (L117, L206) | varied | not quantified | hybrid links (L204); built-in fault tolerance in principle (L117) | coherence and readout (L204); still experimental (L117) |

Week 7's summary (L98-100) is the honest frame. Processors now beat classical computers on niche science problems. Clear evidence of quantum advantage in an industrially relevant problem is still missing. And there is no winning platform yet.

*You've got it when* you can say what NISQ, VQE and ZNE are in one sentence each, why an annealer's qubit count is not comparable, and give one strength and one barrier per platform with a lecture line.

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. All Harrowmere Water & Power figures are invented for practice and labelled (fictional).

### Exercise 9.1 (quantitative)

For RSA-2048 ($n = 2048$ bits): (a) estimate the trial-division cost $\sqrt N$ as a power of 10; (b) estimate the NFS cost $\exp\!\big(1.923(\ln N)^{1/3}(\ln\ln N)^{2/3}\big)$ as a power of 10 and of 2; (c) estimate Shor's $n^3$. (d) *(stretch)* Repeat (b) and (c) for $n = 4096$, and give the factor by which each grows when the key length doubles. (e) Which row of the taxonomy is each?

**Hint:** $\ln N = n\ln2$. Work in logarithms: $\log_{10}$ of $e^{x}$ is $x/2.303$. Move M13.1.

**Solution sketch:**
- *Restate:* three cost shapes at two key sizes.
- *Write state:* $n = 2048$: $\ln N = 1419.6$, $\ln\ln N = 7.258$. $n = 4096$: $\ln N = 2839.2$, $\ln\ln N = 7.951$.
- *Name move:* M13.1.
- *Algebra:* (a) $\sqrt N = 2^{1024}\approx10^{308}$. (b) Exponent $1.923\times1419.6^{1/3}\times7.258^{2/3} = 81.0$, so $e^{81.0}\approx1.5\times10^{35}\approx2^{117}$. (c) $2048^3\approx8.6\times10^{9}$. (d) NFS exponent $= 108.5$, $e^{108.5}\approx1.3\times10^{47}\approx2^{156}$. Growth factor $1.3\times10^{47}/1.5\times10^{35}\approx8.4\times10^{11}$. Shor: $4096^3\approx6.9\times10^{10}$, a factor of 8.
- *Check:* doubling $n$ multiplies a cubic by $2^3 = 8$. The NFS grows by a factor that itself grows with $n$, the signature of super-polynomial cost. $2^{117}$ is close to the "112-bit security" usually quoted for RSA-2048 (judgement), so the formula is sane.
- *Answer:* (a) about $10^{308}$; (b) about $10^{35}$, or $2^{117}$; (c) about $8.6\times10^{9}$; (d) NFS about $10^{47}$ ($\times8.4\times10^{11}$), Shor $\times8$; (e) trial division is exponential, the NFS sub-exponential, Shor polynomial. So the Shor-versus-NFS gap is super-polynomial ("exponential" in the loose sense of the taxonomy), not exponential-versus-polynomial as L152 says.

### Exercise 9.2 (quantitative)

Run Shor's classical skeleton by hand. (a) $N = 21$, $a = 4$. (b) $N = 21$, $a = 5$. (c) $N = 39$, $a = 2$. For each, find $r$, decide whether it succeeds, and if so give the factors. (d) For (b), what does the lecture's L150 condition tell you to do, and why is that wrong?

**Hint:** List $a^x \bmod N$ until you hit 1 (multiply the previous value by $a$ and reduce). Then check "$r$ even" and "$a^{r/2}\not\equiv-1$" (Move M13.2).

**Solution sketch:**
- *Restate:* three order-finding runs, then the corrected success test.
- *Write state:* $-1\equiv20 \pmod{21}$; $-1\equiv38 \pmod{39}$.
- *Name move:* M13.2.
- *Algebra:* (a) Powers of 4 mod 21: 4, 16, 1. So $r = 3$, odd: fail, pick another $a$. (b) Powers of 5 mod 21: 5, 4, 20, 16, 17, 1. So $r = 6$, even, but $5^3\equiv20\equiv-1$: fail. (c) $\gcd(2, 39) = 1$. Powers of 2 mod 39: 2, 4, 8, 16, 32, 25, 11, 22, 5, 10, 20, 1. So $r = 12$, even, and $y = 2^6 = 64\equiv25\not\equiv38$. Then $\gcd(24, 39) = 3$ and $\gcd(26, 39) = 13$. (d) L150 treats $a^{r/2}+1\equiv0$ as the success case, so it would tell you to use $\gcd(21, 21) = 21$ and $\gcd(19, 21) = 1$: both trivial.
- *Check:* $3\times13 = 39$. In (a), $\gcd(4, 21) = 1$ and $\gcd(5, 21) = 1$, so step 1 was passed correctly.
- *Answer:* (a) $r = 3$, odd, retry. (b) $r = 6$ but $a^{r/2}\equiv-1$, retry; L150 has this backwards. (c) $r = 12$, $y = 25$, factors 3 and 13.

### Exercise 9.3 (quantitative)

(a) For $N = 10^{6}$, how many Grover iterations are optimal, and how many classical queries are needed on average? What is the ratio? (b) What is the success probability if you stop at 785 iterations, and if you run 1570? (c) With a 1 ns classical query and a 1 µs quantum iteration (judgement), find the crossover $N$ and the two times at $N = 10^{6}$. (d) A search space of $2^{40}$: how many iterations?

**Hint:** $k\approx(\pi/4)\sqrt N$; $P_k = \sin^2((2k+1)\theta)$ with $\theta\approx1/\sqrt N$; crossover where $(\pi/4)\sqrt N\,t_q = (N/2)\,t_c$ (Move M13.3).

**Solution sketch:**
- *Restate:* iteration count, overshoot, wall-clock crossover, one more size.
- *Write state:* $\sqrt N = 10^{3}$, $\theta\approx10^{-3}$; $t_c = 10^{-9}$ s, $t_q = 10^{-6}$ s.
- *Name move:* M13.3.
- *Algebra:* (a) $k = (\pi/4)\times1000 = 785$; classical $N/2 = 5\times10^{5}$; ratio $\approx640$. (b) $P_{785} = \sin^2(1571\times10^{-3})\approx1.0$; $P_{1570} = \sin^2(3141\times10^{-3})\approx0$. (c) $\sqrt N = (\pi/2)(t_q/t_c) = 1571$, so $N\approx2.5\times10^{6}$. At $N = 10^{6}$: classical $5\times10^{5}\times1$ ns $= 0.5$ ms; quantum $785\times1$ µs $= 0.785$ ms. (d) $\sqrt{2^{40}} = 2^{20}$, so $k = (\pi/4)\times2^{20}\approx8.2\times10^{5}$.
- *Check:* a 1,000× slower clock cancels a $\sqrt N$ advantage until $\sqrt N\approx10^{3}$, consistent with (c).
- *Answer:* (a) 785 against $5\times10^{5}$, about 640×; (b) about 1.0, then about 0 (overshoot); (c) crossover near $2.5\times10^{6}$ items, and at $10^{6}$ the classical search wins, 0.5 ms against 0.785 ms; (d) about $8.2\times10^{5}$ iterations.

### Exercise 9.4 (quantitative)

Using success $\approx F^{g}$: (a) how many two-qubit gates before success falls below 0.5 at $F = 0.995$ (L162) and $F = 0.999$ (L162/L170)? (b) Repeat for L170's 98% and the worst case of L188 (error $10^{-1}$). (c) A 50-qubit circuit applies 25 two-qubit gates per layer. How many layers fit at $F = 0.995$? (d) What two-qubit error rate would let $10^{4}$ gates run at 50% success?

**Hint:** $g_{1/2} = \ln0.5/\ln F\approx0.693/(1-F)$; for (d) solve $F^{10^4} = 0.5$ (Move M13.4).

**Solution sketch:**
- *Restate:* gate budgets at four fidelities, a layer budget, an inverse problem.
- *Write state:* $F\in\{0.995, 0.999, 0.98, 0.9\}$.
- *Name move:* M13.4.
- *Algebra:* (a) $0.693/0.00501 = 138$ (check: $0.995^{138} = 0.501$, $0.995^{139} = 0.498$); $0.693/0.0010005\approx693$. (b) $\ln0.5/\ln0.98 = 34$; $\ln0.5/\ln0.9 = 6.6$, so about 7. (c) $138/25 = 5.5$, so about 5 layers. (d) $1-F = 1-0.5^{10^{-4}} = 6.9\times10^{-5}$.
- *Check:* ten times lower error, ten times more gates: 138 against roughly 1,380 at 99.95%. The $1/(1-F)$ scaling is linear.
- *Answer:* (a) about 138 and about 693; (b) about 34 and about 7, so the lecture's own figures span a factor of 20 in usable depth (erratum L162/L170/L188); (c) about 5 layers of a 50-qubit circuit; (d) an error rate of about $7\times10^{-5}$ per gate, beyond any figure in the lecture, which is why long algorithms need error correction rather than better NISQ hardware.

### Exercise 9.5 (quantitative)

Use the surface-code rule $p_L\approx0.1\,(p/p_\text{th})^{(d+1)/2}$ with $p_\text{th} = 10^{-2}$ and $2d^2$ physical qubits per logical (Move M13.5, judgement). Target $p_L\le10^{-12}$. (a) Find $d$ and the physical:logical ratio at $p = 10^{-3}$. (b) Repeat at $p = 5\times10^{-3}$. (c) A Shor circuit for RSA-2048 needs about $2n+3 = 4099$ logical qubits (judgement: a standard construction). How many physical qubits at the ratio from (a)? (d) Compare with the "several thousand qubits" of Week 7 L88.

**Hint:** Solve $(p/p_\text{th})^{k}\le10^{-11}$ for the integer $k = (d+1)/2$, then $d = 2k-1$.

**Solution sketch:**
- *Restate:* code distance and overhead at two error rates, then a machine size.
- *Write state:* $p/p_\text{th} = 0.1$ and $0.5$.
- *Name move:* M13.5.
- *Algebra:* (a) $0.1^{k}\le10^{-11}\Rightarrow k = 11$, $d = 21$, $2\times441 = 882$. (b) $0.5^{k}\le10^{-11}\Rightarrow k\ge36.5$, so $k = 37$, $d = 73$, $2\times5329 = 10\,658\approx1.1\times10^{4}$. (c) $4099\times882\approx3.6\times10^{6}$ physical qubits. (d) $3.6\times10^{6}/3\times10^{3}\approx10^{3}$.
- *Check:* (a) lands inside the $10^{2}$-$10^{3}$ physical:logical range; five times worse gates cost about twelve times more qubits.
- *Answer:* (a) $d = 21$, about 880:1; (b) $d = 73$, about $1.1\times10^{4}$:1; (c) about $3.6\times10^{6}$ physical qubits, before the extra qubits for magic-state factories and routing (judgement); (d) about a thousand times more than the largest counts in the lecture, which are annealer qubits that could not run Shor anyway.

### Exercise 9.6 (quantitative) (stretch)

(a) A superconducting qubit has $T_2 = 300$ µs (L166: "several hundred microseconds") and two-qubit gates take 50 ns (judgement). How many gate times fit in $T_2$? (b) A circuit of 100 sequential layers takes how long, and what coherence factor $e^{-t/T_2}$ remains? (c) Compare with the $F^g$ budget at $F = 0.995$ and say which limit binds. (d) ZNE: at noise scales $\lambda = 1, 3$ an energy reads $-0.84$ and $-0.62$ (fictional). Extrapolate linearly to $\lambda = 0$.

**Hint:** $t = 100\times50$ ns; linear fit through two points; $E(0) = E(1) - \big(E(3)-E(1)\big)/2$ (Moves M13.4 and M13.6).

**Solution sketch:**
- *Restate:* coherence budget, decay over a circuit, which limit binds, one extrapolation.
- *Write state:* $T_2 = 3\times10^{-4}$ s, gate $5\times10^{-8}$ s.
- *Name move:* M13.4 and M13.6.
- *Algebra:* (a) $3\times10^{-4}/5\times10^{-8} = 6000$. (b) $t = 5$ µs; $e^{-5/300} = 0.98$. (c) 100 layers of even one two-qubit gate each is already 100 gates, and $0.995^{100} = 0.61$; with several gates per layer it falls below 0.5 (Exercise 9.4(c)). (d) Slope $(-0.62+0.84)/2 = 0.11$ per unit $\lambda$, so $E(0) = -0.84-0.11 = -0.95$.
- *Check:* $e^{-t/T_2}$ near 1 while $F^g$ is near 0.5 means gate error, not idle decoherence, dominates.
- *Answer:* (a) 6000 gate times; (b) 5 µs, about 0.98 coherence left; (c) the gate-fidelity budget binds first (judgement: the simple model); (d) $E(0)\approx-0.95$, paid for with extra circuit runs at amplified noise.

### Exercise 9.7 (writing)

*Inventory row W6 Consolidate.* A vendor tells **Harrowmere Water & Power** that "our quantum computer gives an exponential speed-up on pump scheduling: it searches every schedule at once, so it will beat your classical optimiser" (fictional claim). From the shared fact sheet (all fictional): Harrowmere schedules 220 pumps across 4 electricity tariff bands, and a classical optimiser already sets the schedule every day. Write a 300-word F1 assessment of the claim. Place it in the speed-up taxonomy, give a Grover estimate for brute-force search with a wall-clock time, and separate annealing from the gate model. The baseline question (which bill any saving is measured against) was settled in Exercise 8.8: reuse that conclusion in one line rather than redoing it.

**Hint:** Count the schedules if each pump is on or off in each tariff band ($2^{220\times4}$). Ask which taxonomy row a scheduling speed-up falls in, and what Grover would need even if it applied: iterations, then time at an optimistic 1 µs per error-corrected iteration (Move M13.3, judgement). Then ask which kind of machine the vendor sells, and what depth today's gates allow (Move M13.4). Tie the verdict to Harrowmere's own numbers.

**Model paragraph:**
(1) *Classical limit.* Harrowmere's 220 pumps, each on or off in each of 4 tariff bands, give $2^{880}\approx8\times10^{264}$ possible daily schedules (all figures fictional). No computer, classical or quantum, searches them all; the current optimiser works because it exploits structure (tariffs, reservoir levels, minimum run times). (2) *Mechanism.* A gate-model quantum computer does not "search every schedule at once": measuring a superposition returns one schedule at random. It gains only when interference cancels wrong answers, which buys an exponential speed-up for a few structured problems such as factoring and a quadratic one for unstructured search. A quantum annealer is a different, analogue machine: it relaxes coupled qubits towards a low-energy state that encodes the problem, and it cannot run Grover or Shor at all. (3) *Figure of merit.* The cost of the schedule found within the planning deadline, against Harrowmere's current optimiser on the same data, measured on today's optimised bill (Exercise 8.8). (4) *Gain.* Scheduling is not in the exponential row. Brute-force Grover search would need about $(\pi/4)\times2^{440}\approx2\times10^{132}$ iterations; at 1 µs each that is $2\times10^{126}$ s, against about $4\times10^{17}$ s since the Big Bang. Any gain must therefore come from heuristics (annealing, QAOA), row 4 of the taxonomy, where no speed-up has been proven, and the Week 7 lecture finds no clear advantage on any industrially relevant problem yet (L99). (5) *Maturity and practicality.* Gate-model machines are NISQ devices: at 99.5% two-qubit fidelity they manage about 138 gates before the answer is a coin toss, far short of a 220-pump model. If the vendor's machine is an annealer, its qubit count is not comparable with a gate-model chip's. (6) *Verdict.* "Exponential" is the wrong word, and Harrowmere should not budget for a quantum speed-up. The caveat: a blind benchmark on last year's tariff and demand data, against the current optimiser under the same time limit, would test the claim cheaply.

**What a weak answer misses:** It accepts "exponential" for a scheduling problem, or puts scheduling in the exponential row. It treats the quantum computer as trying every schedule at once (the parallelism myth, L131). It applies Grover without turning iterations into time, so it never sees that a quadratic gain on $2^{880}$ schedules is still hopeless. It does not ask whether the machine is an annealer or a gate-model computer, and so compares qubit counts that measure different things. Its verdict could be pasted into any company's report because it never uses Harrowmere's pump count or tariff bands.

### Exercise 9.8 (writing)

*Inventory row W6 Consolidate (crypto angle) with M8 from Day 06.* From the shared fact sheet (all fictional): Harrowmere's control centre links four sites over dark fibre and refreshes an AES-256 telemetry key every 60 s per site. The telemetry must stay confidential for 15 years, and a full cryptographic migration takes 5 years. For this exercise, assume (fictional) that each AES key is agreed with RSA-2048 key exchange and that pump commands are signed with RSA-2048. Write a 250-300-word briefing on how urgent the migration to post-quantum cryptography is. Quantify the attacker's machine, and treat key exchange, the AES layer and signatures separately.

**Hint:** Use Mosca's inequality $x+y>z$ (Day 06, M8). Size the attacker with Exercise 9.5: logical qubits, physical:logical ratio, physical qubits, compared with today's physical counts (like with like). AES-256 faces only Grover's quadratic speed-up. Do not invent a date for $z$: use a planning range and say so.

**Model paragraph:**
Harrowmere's control network (all figures fictional) encrypts telemetry from its four fibre-linked sites with AES-256 keys refreshed every 60 s, agreed with RSA-2048, and signs pump commands with RSA-2048. Classically RSA-2048 is safe: the best known attack, the number field sieve, costs about $2^{117}$ operations. Shor's algorithm would break it in polynomial time, but only on a fault-tolerant machine with about 4,100 logical qubits. At roughly 880 physical qubits per logical qubit, which assumes 99.9% gates and surface-code error correction (judgement), that is about 3.6 million physical qubits. Today's largest machines report thousands of *physical* qubits (Week 7 L88, L94), so on a like-for-like physical count the gap is about a thousandfold. Nobody can date when it closes. Our planning range is 10 to 30 years (fictional planning assumption, not a forecast). The three layers carry different risks. **Key exchange** is exposed now: an adversary can record today's handshakes and recover every 60-second key later. With a 15-year confidentiality requirement ($x$) and a 5-year migration ($y$), $x+y = 20$ years. Any machine arriving in under 20 years, which is half our planning range, exposes telemetry we send today. Key exchange should therefore move to post-quantum algorithms first, starting this year. **AES-256** itself stays safe: Grover only halves its effective key length to 128 bits. **Signatures** are exposed only once the machine exists, because a forged pump command must be sent in real time. They can follow later in the same 5-year programme. The caveat: the 3.6 million estimate assumes 99.9% gates; at 99.5% it rises about twelvefold, and better codes could lower it. That uncertainty is why the decision rests on $x+y$, which Harrowmere controls, not on a guess at $z$.

**What a weak answer misses:** It says "quantum computers already break RSA" or "it is decades away, so wait", without the physical-versus-logical arithmetic. It compares a logical-qubit requirement with a physical-qubit headline (not like for like). It treats key exchange, AES and signatures as one risk, and so misses that the 60-second AES keys are only as safe as the RSA handshake that delivers them. It invents a precise date for $z$ instead of reasoning from Harrowmere's $x+y = 20$.

### Exercise 9.9 (writing) (stretch)

A Harrowmere board slide (fictional) reads: "Vendor's 1,000-qubit machine with 99.5% gates is error-corrected thanks to the threshold theorem, so it can run our 10,000-gate network-planning circuit." Rewrite it as an accurate 100-150-word note for the board.

**Hint:** Use $g_{1/2}$ at 99.5% (Exercise 9.4), the correct threshold statement (Move M13.5), and the physical:logical ratio at $p = 5\times10^{-3}$ (Exercise 9.5), with the target $p_L$ set so that $10^{4}$ steps succeed at least half the time: $(1-p_L)^{10^4}\ge\tfrac12$.

**Model paragraph:**
The vendor's machine (fictional figures) has 1,000 physical qubits with 99.5% two-qubit gates. Without error correction, a circuit at that fidelity is down to a 50% chance of a correct answer after about 138 gates. A 10,000-gate circuit would return noise. The threshold theorem does not make the machine error-corrected. It says that *if* every operation's error rate is below a threshold (about 1% for the leading code), encoding each logical qubit in many physical ones can push logical errors as low as we like. At a 0.5% error rate, a logical error of $10^{-4}$ per step is not good enough: over 10,000 steps it leaves only about $e^{-1}\approx37\%$ success. A better-than-even chance needs about $\ln2/10^{4}\approx7\times10^{-5}$ per step (judgement: independent errors). With the surface-code rule that needs code distance 21, about 880 physical qubits per logical qubit, so the 1,000 qubits would give one logical qubit. That is far too few for a network-planning problem. We should ask the vendor for logical-qubit counts and logical error rates, not physical counts.

**What a weak answer misses:** It repeats the lecture's L184 wording ("correction introduces errors") as the theorem. It confuses physical with logical qubits. It gives no depth number, so the board cannot see that 10,000 gates is about 72 times past the uncorrected budget of 138.

## Anti-patterns / Common mistakes

- **Calling Grover exponential (L131).** How you'd notice: you wrote "exponential" next to "search". Instead: Grover is quadratic, $\approx(\pi/4)\sqrt N$, and provably no better for black-box search.
- **Calling classical factoring exponential (L133, L152).** How you'd notice: you cannot name the classical algorithm. Instead: the number field sieve is sub-exponential, about $2^{117}$ for RSA-2048. Only trial division is exponential.
- **Copying L150's success condition.** How you'd notice: your gcd returns 1 or $N$. Instead: you need $r$ even **and** $a^{r/2}\not\equiv-1$, then $\gcd(a^{r/2}\pm1, N)$.
- **Thinking the classical gcd step is the hard part (L135).** How you'd notice: you cannot say why the quantum computer is needed. Instead: Euclid is $O(n^2)$; only period finding is hard.
- **Mixing fidelities from different lecture lines.** How you'd notice: a platform comparison that cites L162 for one side and L170 for the other. Instead: one primary source, one date, one set of conditions (F3).
- **Quoting the threshold theorem as a limit (L184).** How you'd notice: the sentence contains "limit on the size". Instead: below threshold, logical error can be made arbitrarily small at polylogarithmic overhead.
- **Treating physical qubits as logical (W7 L94).** How you'd notice: you compared a headline qubit count with the logical-qubit needs of an algorithm. Instead: divide by $10^{2}$-$10^{3}$ before comparing.
- **Treating annealers as gate-model machines.** How you'd notice: you claimed an annealer could run Shor, or compared its qubit count with a gate-model chip's. Instead: an annealer is an analogue heuristic optimiser (taxonomy row 4).
- **Quoting a query ratio as a time ratio.** How you'd notice: no clock speeds in your Grover claim. Instead: include the per-iteration time and the overhead of error correction.

## Done when

Without notes, in 40 minutes, you can do all of the following. Pass mark: 7 of 8.

1. Draw the four-row speed-up taxonomy with one example and one scaling per row, and fix L131 and L152.
2. Run Shor's classical skeleton on a fresh $N$ (try $N = 35$, $a = 2$), stating both failure conditions.
3. State the L150 erratum and the L135 erratum in one sentence each.
4. Compute Grover's optimal iteration count for a given $N$, and the crossover $N$ for given clock speeds.
5. Convert a two-qubit fidelity into $g_{1/2}$ with $0.693/(1-F)$, and list the three inconsistent fidelity lines.
6. State the threshold theorem correctly and estimate the physical:logical ratio from $p$ and $p_\text{th}$.
7. Define NISQ, VQE and ZNE in one sentence each, and contrast annealing with the gate model.
8. Fill in the platform table (conditions, one fidelity with its line, one strength, one barrier) for superconducting, trapped-ion and spin qubits.

(For item 2 with $N = 35$, $a = 2$: $r = 12$, $2^6 = 64\equiv29\not\equiv34$, so $\gcd(28, 35) = 7$ and $\gcd(30, 35) = 5$.)

## Companion pointer and confusion log

Open `content/companions/week06_companion.md` (§3 notation and units, §4 errata, §9 The Qubit Factory). Read lecture L127-152 with Moves M13.1 and M13.2 beside you, then L154-192 with M13.4 and M13.5. Log every symbol and term you had to look up twice ($r$, $\gcd$, $\theta$, $T_2$, $p_\text{th}$, $d$, "logical qubit") in your confusion log, with the lecture line.

| Symbol or line | What confused me | Resolution |
|---|---|---|
| | | |
| | | |

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 08 (gates and circuits, M12).**
1. Apply H to the first qubit of $|00\rangle$, then CNOT (first qubit controls). Write the state.
2. In Deutsch-Jozsa with $n = 2$ and a balanced $f$, what is the final amplitude of $|00\rangle$, and what does measuring it tell you?
3. In one sentence: why is "a quantum computer tries all answers in parallel" wrong?

**From Day 06 (crypto and QKD, M8-M10).**
4. Under intercept-resend, what QBER does Eve cause, and what is the probability she is detected if Alice and Bob compare 20 sifted bits?
5. Fibre loses 0.2 dB/km. What fraction of photons survives 100 km?
6. State Mosca's inequality and what each letter means.

**From Day 02 (sensor figures of merit, M2-M3).**
7. A sensor has a noise density of $2\ \text{pT}/\sqrt{\text{Hz}}$. What is its noise in a 100 Hz bandwidth?
8. With $N = 10^{6}$ particles, what are the shot-noise and Heisenberg phase limits?

*Answers.* 1. $(|00\rangle+|11\rangle)/\sqrt2$. 2. 0, so you never measure $|00\rangle$, which proves $f$ is balanced in one query. 3. You read out only one outcome; the speed-up comes from arranging interference so that wrong answers cancel. 4. 25%; $1-(3/4)^{20} = 0.997$. 5. $20$ dB, so $10^{-2}$, 1%. 6. $x+y>z$: if the shelf life of the data ($x$) plus the migration time ($y$) exceeds the time until a cryptographically relevant quantum computer exists ($z$), you are already exposed. 7. $2\times\sqrt{100} = 20$ pT. 8. $1/\sqrt N = 10^{-3}$ rad and $1/N = 10^{-6}$ rad.

## Read next

- Preskill, *Quantum computing in the NISQ era and beyond* (2018), <https://arxiv.org/abs/1801.00862>. Read all of it; it is short. Focus on the definition of NISQ, the discussion of noise limiting circuit size, error correction and its overhead, and the honest assessment of optimisation and annealing.
- Aaronson, *The Limits of Quantum Computers* (author draft), <https://www.scottaaronson.com/writings/limitsqc-draft.pdf>. Read all of it. It is the best antidote to the parallelism myth, and it explains why Grover's $\sqrt N$ is the best possible for black-box search and why factoring is special.
