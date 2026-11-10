# Day 01: The Module Map, the Gain Argument and Credible Numbers

**Time:** ~3 h · **Feeds:** Week 1 lecture (`week_1/week_1_lecture.md`, read inside this day), inventory rows W1 Explore, W1 Apply, W1 Consolidate · **Companion:** none. Week 1 has no companion; the section "Decoding the Week 1 lecture" below does that job.

**Cadence (180 min):** 15 min retrieval · 55 min frameworks and moves (F1, F3, M1, plus the lecture decode) · 50 min quantitative drills (Exercises 1.1-1.5) · 45 min writing on the running case (Exercises 1.6-1.9) · 15 min confusion log and pointer to Day 02.

## Why this matters

Module 4 asks one question seven times: *what does the quantum version do better than the classical one, by how much, and how mature is it?* Every Apply and Consolidate task in the module is a version of that question. None of them asks for a derivation. All of them ask for "quantitative or quantifiable measures" (Week 1 Consolidate). So the two skills that pay off in every week are:

1. a fixed shape for the argument (framework **F1**, the gain argument), and
2. a habit of handling numbers so a reader can trust them (framework **F3**, credible numbers, plus move **M1**, units and orders of magnitude).

Today you learn both, and use them to read the Week 1 lecture. That lecture is an overview with no equations and two statements that are wrong as written (L52 and L70). You will learn the correct versions here, because both errors come back later: L52 in Week 4 (communication) and L70 in Weeks 5 and 6 (simulation, computing).

You will not write your own Week 1 pieces today. The exercises use a made-up utility, **Harrowmere Water & Power**, so that your portfolio case stays yours and stays written by you. Every Harrowmere number is labelled (fictional).

## Warm-up (retrieval, closed book, 15 min)

These come from Module 3. Answer on paper, then open the answers.

1. A qubit is in $|\psi\rangle = \tfrac35|0\rangle + \tfrac45|1\rangle$. What are the probabilities of measuring 0 and 1?
2. You measure 1. What is the state straight after the measurement?
3. How many complex amplitudes do you need to write down a general state of 3 qubits?
4. Apply the Hadamard gate $H$ to $|0\rangle$, then apply $H$ again. What state do you get, and why do the $|1\rangle$ contributions vanish?
5. One measurement of a superposition returns how many outcomes?

<details>
<summary>Answers</summary>

1. $P(0) = (3/5)^2 = 0.36$, $P(1) = (4/5)^2 = 0.64$.
2. $|1\rangle$. Measurement replaces the superposition with the outcome's state.
3. $2^3 = 8$.
4. $H|0\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$. Then $H$ again gives $\tfrac12(|0\rangle + |1\rangle) + \tfrac12(|0\rangle - |1\rangle) = |0\rangle$. The two paths to $|1\rangle$ carry amplitudes $+\tfrac12$ and $-\tfrac12$, so they cancel. That is **interference**, and you will need it for the L70 erratum below.
5. One. Keep this in mind when you read "performs multiple calculations simultaneously".

</details>

## Core concepts

### The module map

Seven weeks, four technology types, one maturity week. Each type has its own **figure of merit**: the one number that defines "better" for that type. If you cannot name the figure of merit, you cannot write the gain argument.

| Week | Topic | Type | Figure of merit (what "better" means) | Sprint day |
|---|---|---|---|---|
| 1 | Overview of the four types | all | (this day) | 01 |
| 2 | Magnetometers and clocks | sensing | magnetometers: sensitivity, the smallest detectable field per √Hz of bandwidth (unit T/√Hz); clocks: fractional frequency stability and fractional uncertainty (dimensionless, e.g. $10^{-18}$) | 02, 03 |
| 3 | Atom interferometry, gravity, inertial sensing | sensing | sensitivity to acceleration or gravity (Gal/√Hz, usually µGal), long-term stability (drift), accuracy | 04 |
| 4 | Quantum communication (QKD) | communication | secure key rate (bit/s) at a stated distance (km), with the error rate (QBER) it tolerates; and *what the security rests on* | 06 |
| 5 | Quantum simulation | simulation | largest problem size (number of particles, spins or modes) simulated faithfully, against the classical cost, which grows like $2^N$ | 07 |
| 6 | Quantum computing | computing | how runtime scales with problem size (exponential, quadratic or unproven speed-up), given qubit count and gate fidelity | 08, 09 |
| 7 | Maturity, markets, comparison | all | technology readiness level (TRL), barriers, market size with source and date | 10 |

Sensitivity "per √Hz", Allan deviation and the $1/\sqrt{N}$ laws are Day 02's job. Today you only need to *name* each figure of merit and know its unit.

**Assessments.** Assessment 1 (Problem Set) is due Thu 19 Nov 2026, 17:00 UK; Assessment 2 (Portfolio) is due Mon 21 Dec 2026, 10:00 UK. Both are the planning times from the sprint spec; confirm on Sussex Direct. This sprint is for understanding only. It contains nothing aimed at Assessment 1 and never drafts portfolio text.

**You've got it when** you can fill the "figure of merit" column from memory, with a unit for each row.

### Framework F1: the gain argument (six parts)

**Idea.** Every Apply and Consolidate piece in this module is a gain argument. It has six parts, always in this order:

1. **Classical limit, with a number.** What the best conventional approach achieves, in units.
2. **Quantum mechanism, in one sentence of physics.** What quantum effect does the work.
3. **Figure of merit named.** Which number defines "better" here (the table above).
4. **Quantified gain.** A ratio or a scaling law, sourced, with both sides measured the same way (F3).
5. **Maturity and practicality.** TRL, size, weight, power and cost (SWaP-C), the barriers.
6. **Verdict, with one honest caveat.** Is the gain worth it, for this user, now? What could make you wrong?

Part 1 is the one most often missing. "Quantum sensors are more sensitive" says nothing until you say *than what, by how much, measured how*.

**Worked clone (annotated).** Harrowmere grid timing. Harrowmere Water & Power's substation clocks must stay within 1 µs of UTC for protection and phasor measurement (fictional requirement). At 50 Hz, 1 µs is a phase error of $360° \times 50\ \text{Hz} \times 10^{-6}\ \text{s} = 0.018°$. The clocks are steered by satellite timing. When the satellite signal is lost, a local oscillator has to "hold over" on its own, and Harrowmere designs for an 8 h loss of satellite timing (fictional design case).

> [1] Harrowmere's installed holdover oscillator is an oven-controlled quartz crystal (OCXO) with a fractional frequency offset of $1\times10^{-9}$ after loss of lock (fictional datasheet, 2025, at constant temperature), so it drifts past the 1 µs limit after $10^{-6}/10^{-9} = 10^3$ s, about 17 minutes, and is $10^{-9}\times28\,800\ \text{s} = 28.8\ \mu\text{s}$ out by the end of an 8 h outage. [2] A rubidium atomic clock instead locks its frequency to a transition between two energy levels of an atom, which is identical in every atom of that species and does not age like a crystal. [3] The figure of merit is holdover time within 1 µs, set by the fractional frequency offset. [4] The candidate rubidium unit quotes $5\times10^{-12}$ under the same conditions (fictional datasheet, 2025), a 200-fold improvement, giving $2\times10^{5}$ s, about 2.3 days, of holdover and only $0.144\ \mu\text{s}$ of error after 8 h. [5] Rubidium clocks of this kind are sold as products (judgement: TRL 9 for the clock; lower for Harrowmere's integration), but each costs about 10 times the quartz unit (fictional) and needs its own power and monitoring. [6] For the 8 h design case, the gain turns a clear fail (28.8 µs) into a pass with a margin of about 7, and is worth piloting at the most critical substations; the caveat is that both figures are datasheet values at constant temperature, and a field test in an unheated substation cabinet may show a smaller gain.

Notice what the annotation shows. Part [4] is a ratio of two numbers measured the same way (both datasheets, same conditions), and part [6] says which assumption could break it. The numbers come from M1: fractional offset × time = time error.

**You've got it when** you can take any paragraph about a quantum technology and label each sentence [1]-[6], and spot which part is missing.

### Framework F3: credible numbers

**Idea.** A gain argument is only as good as its two numbers. Three rules:

1. **Source hierarchy.** Prefer, in this order: peer-reviewed paper or national metrology institute > review article > vendor datasheet > press release > market report. Use a lower source only when you say what it is ("vendor-stated").
2. **Date, conditions, units.** Always state when the number was measured, under what conditions (lab or field, shielded or not, averaging time, temperature) and in what units. "1 fT" without "/√Hz", "in a shielded room", "2024" is not a number you can compare.
3. **Like-for-like ratios.** A ratio needs both sides measured the same way. A lab record divided by a fielded product's datasheet is not a gain; it is two different questions.

**Worked clone.** Harrowmere inspects buried cables with a field magnetometer whose noise is $20\ \text{pT}/\sqrt{\text{Hz}}$ (fictional datasheet). A vendor brochure for an optically pumped quantum magnetometer quotes $50\ \text{fT}/\sqrt{\text{Hz}}$ "in a magnetically shielded laboratory" and $1\ \text{pT}/\sqrt{\text{Hz}}$ "in unshielded field use" (fictional brochure, 2025).

- Lab versus field: $20\ \text{pT} / 50\ \text{fT} = 20\times10^{-12} / 50\times10^{-15} = 400$. Tempting, and wrong as a gain, because one side sits in a shielded room and the other in a trench.
- Field versus field: $20\ \text{pT} / 1\ \text{pT} = 20$. This is the like-for-like ratio, and it is still vendor-stated, so the argument says so.

That optically pumped magnetometers reach femtotesla-level sensitivity in shielded conditions is from Budker & Romalis (2007), one of the Target Sources. The specific 50 fT and 1 pT figures here are fictional.

**You've got it when**, given any "N times better" claim, you can ask the three questions (who says so, under what conditions, compared with what measured how) and produce the honest ratio.

### Move M1: orders of magnitude, SI prefixes and the module's units

**Idea.** Every number in this module is a power of ten with a unit. Get the power of ten right and you can sanity-check anything.

**SI prefixes you will meet:**

| Prefix | Symbol | Factor | | Prefix | Symbol | Factor |
|---|---|---|---|---|---|---|
| peta | P | $10^{15}$ | | milli | m | $10^{-3}$ |
| tera | T | $10^{12}$ | | micro | µ | $10^{-6}$ |
| giga | G | $10^{9}$ | | nano | n | $10^{-9}$ |
| mega | M | $10^{6}$ | | pico | p | $10^{-12}$ |
| kilo | k | $10^{3}$ | | femto | f | $10^{-15}$ |
| | | | | atto | a | $10^{-18}$ |

Careful: "T" is both tera and tesla. In "1 T" it is tesla; in "1 TB" it is tera.

**The module's units:**

- **Tesla (T)**, magnetic field. Earth's field is roughly $50\ \mu\text{T}$ (judgement: typical value; it ranges from about 25 to 65 µT). Week 2 quotes sensor noise in pT, fT and aT per √Hz.
- **Gal**, acceleration: $1\ \text{Gal} = 1\ \text{cm/s}^2 = 10^{-2}\ \text{m/s}^2$. So $g \approx 9.81\ \text{m/s}^2 \approx 981\ \text{Gal}$, and $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2 \approx 10^{-9}g$. Week 3 works in mGal and µGal.
- **Eötvös (E)**, gravity gradient (how fast $g$ changes with position): $1\ \text{E} = 10^{-9}\ \text{s}^{-2}$, that is $10^{-9}$ (m/s²) per metre.
- **Fractional uncertainty**, dimensionless: $\delta\nu/\nu$ for a clock, $\delta g/g$ for a gravimeter. It is how clocks are compared (Week 2).

**The clock chain: fractional error → time → distance.** A clock whose frequency is off by a fraction $y = \delta\nu/\nu$ gains or loses time at that fraction:

$$\delta t = y\,\tau, \qquad \delta x = c\,\delta t,$$

where $\tau$ is how long it runs on its own and $c = 299\,792\,458\ \text{m/s}$. The distance step is why timing matters for satellite navigation: a ranging receiver turns a time error into a position error at the speed of light.

**Worked clone.** A clock with $y = 2\times10^{-14}$ runs alone for one week ($\tau = 7 \times 86\,400\ \text{s} = 604\,800\ \text{s}$). Then $\delta t = 2\times10^{-14}\times 604\,800 = 1.2\times10^{-8}\ \text{s} = 12\ \text{ns}$, and $\delta x = c\,\delta t \approx 3.6\ \text{m}$.

**Sanity check habit.** Before you trust any result, say its power of ten aloud and compare with something you know: "12 ns is the time light takes to cross a 3.6 m room". If the comparison sounds absurd, check the prefixes.

**You've got it when** you can convert between µGal, m/s² and fractions of $g$, and run the clock chain, without a calculator for the powers of ten.

### Decoding the Week 1 lecture

Read `week_1/week_1_lecture.md` (153 lines, no equations) with this table open. Line numbers refer to that file.

| Lecture section (lines) | What it does | Use it for | Watch for |
|---|---|---|---|
| 1.1 Introduction (L20-28) | Names the four types | The module map above | Nothing to fix |
| 1.2 Sensing (L30-34) | Lists measured quantities; says sensors "outperform their classical counterparts" in performance, range and practicality | F1 part 3: *which* parameter? The lecture never names one; the figure-of-merit table does | "Unprecedented accuracy" (L32) with no number: an F3 example of a claim without units |
| 1.3 Communication (L36-56) | QKD, no-cloning, eavesdropper detection | Week 4 preview | **Erratum L52** (below); also L38, L44, L50 (judgement notes below) |
| 1.4 Simulation (L58-66) | Classical simulation fails when quantum effects dominate; simulators are special-purpose | Figure of merit: problem size the classical side cannot reach | Nothing to fix; the $2^N$ cost is Day 07 |
| 1.5 Computing (L68-78) | Qubits, superposition, entanglement, gates, error correction | Week 6 preview | **Erratum L70** (below); L74 "database searches" (the speed-up is quadratic, not exponential) |
| 1.6 Capabilities and limitations (L80-96) | Three-by-two list | F1 part 6: ready-made caveats for each type | L86 "much faster" has no qualifier; L92 is the honest version |

**Erratum L52: QKD does not need entanglement.** The lecture says "In QKD, two parties use entangled particles, such as photons, to create a shared secret key". The protocol the lecture itself cites as reference [9], BB84 (Bennett and Brassard, 1984), uses no entanglement. The sender prepares single photons (in practice, weak laser pulses) in one of four polarisation states drawn from two bases; the receiver measures each in a randomly chosen basis. Security comes from the fact that an eavesdropper who does not know the basis disturbs the states and shows up as errors. Entanglement-based QKD (the E91 protocol and its relatives) is a separate family. Source: Pirandola et al., *Advances in quantum cryptography* (2020), BB84 and entanglement-based sections. You run BB84 by hand on Day 06.

**Erratum L70: "multiple calculations simultaneously" is the parallelism myth.** The lecture says quantum computers "perform multiple calculations simultaneously, thanks to the superposition of quantum states". A register of $n$ qubits can hold a superposition of $2^n$ basis states, but a measurement returns *one* outcome at random (warm-up Q5). If you simply computed on all inputs and measured, you would get one random answer, no better than a classical computer guessing. A useful quantum algorithm arranges the amplitudes so that paths to wrong answers **interfere destructively** (cancel, like the $|1\rangle$ paths in warm-up Q4) and paths to the right answer add up. That only works for problems with special structure, which is why the speed-up is problem-specific (L92 says as much). Source: Aaronson, *The Limits of Quantum Computers*. Day 08 traces this on Deutsch-Jozsa.

**Three further notes (judgement; not in the inventory's errata list, but worth knowing):**

- **L38 versus L93.** L38 says the key is "guaranteed to be secure against any eavesdropping attempts"; L93 says interception cannot be prevented entirely. Both are partly right: the *protocol* lets eavesdropping be detected under stated assumptions, while real *devices* have imperfections that attacks can exploit (Pirandola et al., practical-QKD sections). Never write "unbreakable".
- **L50 merges two ideas.** "Measuring disturbs the system" and the no-cloning theorem are related but distinct. No-cloning says you cannot copy an unknown quantum state; it is one reason an eavesdropper cannot keep a perfect copy and pass the original on. Day 06 proves it in four lines.
- **L44, the 2017 data-breach example.** The lecture uses a breach caused by an unpatched web application. The weak point was the application, not the encryption, so QKD would not have prevented it. This is a useful F3 lesson: check that the example supports the conclusion drawn from it.

**Week 1 interactive.** The optional circuit simulator in the Consolidate section is covered on Day 08 with Quirk (https://algassert.com/quirk) as the stand-in.

**You've got it when** you can state both errata and their corrections in one sentence each, without looking.

## Exercises

Attempt each one cold for at least five minutes before opening the hint. Exercises 1.1-1.5 take about 10 minutes each. Exercises 1.6-1.9 share 45 minutes; the word limits are set so that they fit.

### Exercise 1.1 (quantitative)

A buried steel pipe under a Harrowmere access road produces a magnetic anomaly of $0.03\ \mu\text{T}$ at the surface (fictional). A quantum magnetometer can resolve changes of $200\ \text{fT}$ (fictional). (a) Write $0.03\ \mu\text{T}$ in nT. (b) Write $200\ \text{fT}$ in tesla. (c) How many times larger is Earth's field ($50\ \mu\text{T}$) than $200\ \text{fT}$, and how many orders of magnitude is that?

**Hint:** Convert everything to tesla first. Orders of magnitude is $\log_{10}$ of the ratio.

**Solution sketch:**
- *Restate:* three unit conversions and one ratio.
- *Write state:* $0.03\ \mu\text{T} = 0.03\times10^{-6}\ \text{T}$; $200\ \text{fT} = 200\times10^{-15}\ \text{T}$; $B_\oplus = 50\times10^{-6}\ \text{T}$.
- *Name move:* M1 (SI prefixes, orders of magnitude).
- *Algebra:* (a) $0.03\times10^{-6} = 3\times10^{-8}\ \text{T} = 30\ \text{nT}$. (b) $200\times10^{-15} = 2\times10^{-13}\ \text{T}$. (c) $50\times10^{-6} / 2\times10^{-13} = 2.5\times10^{8}$; $\log_{10}(2.5\times10^8) = 8.4$.
- *Check:* micro to femto is 9 orders; 50/200 = 0.25 takes off about 0.6 of an order, giving 8.4. Consistent.
- *Answer:* 30 nT; $2\times10^{-13}$ T; Earth's field is $2.5\times10^8$ times larger, about 8.4 orders of magnitude. A magnetometer that resolves 200 fT must reject a background more than $10^8$ times bigger, which is why dynamic range (Day 02) matters.

### Exercise 1.2 (quantitative)

(a) Express $g = 9.81\ \text{m/s}^2$ in Gal. (b) Express $10\ \mu\text{Gal}$ in m/s². (c) What fraction of $g$ is $10\ \mu\text{Gal}$? (d) One gravimeter datasheet quotes "0.1 mGal"; another quotes "$1\times10^{-6}\ \text{m/s}^2$". Give the ratio of the first to the second.

**Hint:** $1\ \text{Gal} = 10^{-2}\ \text{m/s}^2$. Convert both datasheet values to m/s² before dividing.

**Solution sketch:**
- *Restate:* convert between Gal, m/s² and fractions of $g$; compare two specs in different units.
- *Write state:* $1\ \text{Gal} = 10^{-2}\ \text{m/s}^2$; $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2$; $1\ \text{mGal} = 10^{-5}\ \text{m/s}^2$.
- *Name move:* M1 (module units).
- *Algebra:* (a) $9.81 / 10^{-2} = 981\ \text{Gal}$. (b) $10\times10^{-8} = 1\times10^{-7}\ \text{m/s}^2$. (c) $10^{-7}/9.81 = 1.0\times10^{-8}$. (d) $0.1\ \text{mGal} = 0.1\times10^{-5} = 1\times10^{-6}\ \text{m/s}^2$, so the ratio is 1.
- *Check:* "1 µGal is about a billionth of $g$", so 10 µGal is about $10^{-8}g$. Matches (c).
- *Answer:* 981 Gal; $1\times10^{-7}$ m/s²; $1.0\times10^{-8}$ of $g$; the two specs are identical (ratio 1). Different units can hide equal numbers, and equal-looking numbers can hide different units.

### Exercise 1.3 (quantitative)

Gravity falls off with height. For a spherical Earth, $g = GM/r^2$, so $\mathrm{d}g/\mathrm{d}r = -2g/r$. (a) Take $g = 9.81\ \text{m/s}^2$ and Earth's radius $R = 6.371\times10^{6}\ \text{m}$; compute the size of the vertical gravity gradient in s⁻² and in eötvös. (b) How much does $g$ change, in µGal, when you raise a gravimeter by 1 cm? (c) By how much would you have to raise it to change the reading by $10\ \mu\text{Gal}$?

**Hint:** Differentiate $GM r^{-2}$ and substitute $GM = g r^2$. Then $1\ \text{E} = 10^{-9}\ \text{s}^{-2}$ and $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2$.

**Solution sketch:**
- *Restate:* find $|\mathrm{d}g/\mathrm{d}r|$ at the surface, then use it to turn height into a change in $g$ and back.
- *Write state:* $g = 9.81\ \text{m/s}^2$, $R = 6.371\times10^6\ \text{m}$, $\Delta g = |\mathrm{d}g/\mathrm{d}r|\,\Delta h$.
- *Name move:* M1 (Eötvös, Gal) plus one line of calculus.
- *Algebra:* (a) $2g/R = 2\times9.81/6.371\times10^6 = 3.08\times10^{-6}\ \text{s}^{-2} = 3080\ \text{E}$. (b) $3.08\times10^{-6}\times0.01 = 3.08\times10^{-8}\ \text{m/s}^2 = 3.08\ \mu\text{Gal}$. (c) $\Delta h = 10^{-7}/3.08\times10^{-6} = 0.032\ \text{m} = 3.2\ \text{cm}$.
- *Check:* the measured average free-air gradient is about $0.3086\ \text{mGal/m} = 3086\ \text{E}$ (judgement: standard geodesy value), within 0.2% of ours.
- *Answer:* about $3.1\times10^{-6}\ \text{s}^{-2} = 3080$ E; about 3.1 µGal per cm; 3.2 cm gives 10 µGal. A survey that claims µGal-level results must record the sensor height to a few millimetres. This is the kind of practical caveat F1 part 6 needs.

### Exercise 1.4 (quantitative)

Three free-running oscillators have fractional frequency offsets $y_A = 1\times10^{-9}$, $y_B = 1\times10^{-12}$ and $y_C = 1\times10^{-17}$. (a) For each, find the time error after one day ($86\,400$ s) and the matching ranging error $c\,\delta t$. (b) How many years would oscillator C take to be 1 s out? Use $1\ \text{yr} = 3.156\times10^7\ \text{s}$.

**Hint:** $\delta t = y\tau$ and $\delta x = c\,\delta t$ with $c \approx 3.00\times10^8\ \text{m/s}$. For (b), solve $1\ \text{s} = y_C\,\tau$ for $\tau$.

**Solution sketch:**
- *Restate:* run the clock chain three times, then invert it once.
- *Write state:* $\tau = 86\,400\ \text{s}$; $c = 2.998\times10^8\ \text{m/s}$; $y_A, y_B, y_C$ as given.
- *Name move:* M1 (fractional error → time → distance).
- *Algebra:* (a) A: $\delta t = 8.64\times10^{-5}\ \text{s} = 86.4\ \mu\text{s}$, $\delta x = 2.59\times10^4\ \text{m} \approx 26\ \text{km}$. B: $\delta t = 86.4\ \text{ns}$, $\delta x \approx 25.9\ \text{m}$. C: $\delta t = 8.64\times10^{-13}\ \text{s} = 0.864\ \text{ps}$, $\delta x = 2.6\times10^{-4}\ \text{m} = 0.26\ \text{mm}$. (b) $\tau = 1/10^{-17} = 10^{17}\ \text{s} = 10^{17}/3.156\times10^7 = 3.2\times10^{9}\ \text{yr}$.
- *Check:* each factor of 1000 in $y$ moves $\delta x$ by a factor of 1000: 26 km → 26 m. Consistent.
- *Answer:* 86.4 µs / 26 km; 86.4 ns / 26 m; 0.86 ps / 0.26 mm; about $3.2\times10^9$ years to lose 1 s. "Loses one second in N years" is just $1/y$ rewritten in years, which Exercise 1.5 uses.

### Exercise 1.5 (quantitative)

Two claims about clocks (both fictional). Claim P, a press release: "our clock would lose less than one second in 30 billion years". Claim Q, a metrology-institute paper: "systematic fractional uncertainty $8\times10^{-19}$". (a) Convert P to a fractional figure. (b) What is the ratio P/Q? (c) Separately, a hypothetical quantum gravimeter is quoted at "2 µGal/√Hz (laboratory)" and "10 µGal/√Hz (field)", and Harrowmere's installed relative spring meter has a field noise of 8 µGal/√Hz (all fictional). Give the spring-meter-to-quantum ratio lab-versus-field, and like-for-like.

**Hint:** For (a), $y = 1\ \text{s}/\tau$ with $\tau$ in seconds. For (c), F3 rule 3: put both sides in the same conditions.

**Solution sketch:**
- *Restate:* put a "seconds per years" claim into the module's fractional unit; then compare two numbers fairly.
- *Write state:* $\tau_P = 30\times10^{9}\times3.156\times10^{7}\ \text{s}$; $y_Q = 8\times10^{-19}$; gravimeter numbers as given.
- *Name move:* M1 (clock chain inverted) and F3 (like-for-like).
- *Algebra:* (a) $y_P = 1/(9.47\times10^{17}) = 1.06\times10^{-18}$. (b) $1.06\times10^{-18}/8\times10^{-19} = 1.3$. (c) Lab versus field: $8/2 = 4$. Like-for-like (field versus field): $8/10 = 0.8$.
- *Check:* 30 billion years is about $10^{18}$ s, so $y \approx 10^{-18}$. Matches.
- *Answer:* P is about $1.1\times10^{-18}$, within a factor 1.3 of Q, so the two claims are about the same size, but P does not say whether it means *uncertainty* (how well you know the frequency) or *stability* (how much it wanders), and gives no conditions, so F3 ranks it last. The fair gravimeter "gain" is 0.8×, not 4×: in the field the quantum unit is slightly *noisier* than Harrowmere's spring meter, so any case for it must rest on something else, such as the spring meter's 30 µGal/day drift (fictional; Day 04).

### Exercise 1.6 (writing)

**F1, Consolidate skill.** Harrowmere's control centre is linked to four sites over its own dark fibre, at 12, 38, 95 and 160 km (fictional). Each site's telemetry is encrypted with an AES-256 key refreshed every 60 s; the data must stay confidential for 15 years, and a full cryptographic migration takes 5 years (all fictional). A vendor datasheet quotes a QKD link delivering 10 kbit/s of secure key over 40 km of deployed fibre (fictional, 2025). Write a 150-200-word gain argument in the six-part F1 shape on whether Harrowmere should use QKD for these links.

**Hint:** The figure of merit for communication is not "more secure" but key rate at a distance plus *what the security rests on*. The classical limit is that today's public-key exchange rests on mathematical problems that a large fault-tolerant quantum computer could solve (L74 mentions "cracking of encryption codes"; Day 06 explains). Turn the key rate into something concrete: how many 256-bit keys per second, against the one key per 60 s each site needs? Which sites lie within the quoted 40 km? Add the confidentiality and migration times. For the caveat, look at L93 and the NCSC white paper.

**Model paragraph:** Harrowmere's telemetry keys are exchanged today with public-key cryptography, whose security rests on problems such as factoring that a large fault-tolerant quantum computer could solve. Data recorded now could be decrypted later, and the exposure is long: the data must stay confidential for 15 years and a migration takes 5 (fictional), so a threat arriving within about 20 years matters today. QKD instead creates the key from single-photon states, and an eavesdropper who measures them introduces detectable errors. The figure of merit is secure key rate at the link distance. Each site needs one 256-bit key every 60 s, about 4.3 bit/s; the vendor's 10 kbit/s over 40 km (fictional datasheet, 2025) is about 39 keys per second, a 2300-fold margin, but only for the 12 and 38 km sites. The 95 and 160 km sites would need trusted relay nodes. QKD links of this length are sold commercially (Pirandola et al., 2020), but need dedicated fibre and trusted equipment, and real devices can leak through side channels. The verdict is a pilot on one short link at most: the NCSC white paper recommends post-quantum cryptography, which runs on existing equipment and covers all four sites, as the main defence.

**What a weak answer misses:** It says QKD is "unbreakable" (L38 overclaims; L93 and Pirandola et al. disagree). It gives no key rate and no distance, so there is nothing to compare, and it misses that the 95 and 160 km sites lie beyond the quoted range. It names no classical limit, so the "gain" floats free. It forgets that the encryption itself is still classical: QKD only distributes the key. And it skips post-quantum cryptography, the obvious classical alternative a careful reader will ask about.

### Exercise 1.7 (writing)

**F3, Explore skill.** Harrowmere wants to find a suspected void under its Greystock reservoir embankment with a 150-station gravity survey; the void's target signal is about 5 µGal (fictional). You have five sources on quantum gravimeters (all fictional): (A) a peer-reviewed field-trial paper, 2025: "20 µGal repeatability, 5 min per station, on a quiet rural site"; (B) a 2024 review article summarising several trials; (C) a vendor datasheet: "1 µGal sensitivity"; (D) a press release: "1000 times more sensitive than existing tools"; (E) a market report: "quantum sensing market worth billions by 2030". Rank them by F3, pick the two you would build a 100-word evidence paragraph on, and write that paragraph.

**Hint:** Rule 1 gives the ranking. Rule 2: which sources state date, conditions and units? Rule 3: does D say "than what, measured how"? Does E say anything about *sensitivity*?

**Model paragraph:** The strongest evidence is a 2025 peer-reviewed field trial (source A, fictional), which reports 20 µGal ($2\times10^{-7}$ m/s²) repeatability with 5 minutes per station on a quiet rural site; a 2024 review (source B, fictional) places this within the range of other published trials. I use these two, treating the vendor's "1 µGal" (source C) only as a vendor-stated laboratory figure, since it gives no averaging time or site conditions. Harrowmere's embankment is unlikely to be as quiet (judgement), so the field figure of 20 µGal, not 1 µGal, is the one to compare with the void's 5 µGal signal (fictional), four times smaller.

**What a weak answer misses:** It quotes the press release's "1000 times" because it is the biggest number, though it names no comparison and no conditions. It cites the market report as evidence of performance (market size says nothing about sensitivity). It drops units or the averaging time, so a reader cannot tell 20 µGal in 5 minutes from 20 µGal in a day. It does not notice that the trial site (quiet, rural) differs from Harrowmere's (a reservoir embankment), which is the like-for-like problem again, or that 20 µGal is larger than the 5 µGal target.

### Exercise 1.8 (writing)

**Apply skill (type + application area).** Pick quantum simulation and apply it to Harrowmere's corrosion problem: corrosion of its ductile-iron mains drives £40 million a year of replacement (fictional), and it wants better pipe coatings and corrosion inhibitors. Write 120-150 words on why quantum simulation matters here. Use the classical memory cost of storing a quantum state: about $8\times2^N$ bytes for $N$ two-level particles (single-precision complex amplitudes; Day 07 explains).

**Hint:** Compute $8\times2^{50}$ bytes and put it in petabytes. Name the figure of merit (problem size). Be honest about maturity: this is a research-stage technology for Harrowmere (judgement). Link the chemistry to "quantum effects dominate" in L62.

**Model paragraph:** Corrosion and the inhibitors that slow it are chemistry at metal surfaces, where electrons behave quantum mechanically and the lecture's point applies: classical simulation struggles once quantum effects "matter for the core functionality" (L62). Storing the full quantum state of just 50 interacting two-level particles takes about $8\times2^{50} \approx 9\times10^{15}$ bytes, roughly 9 PB, and every extra particle doubles it. A quantum simulator sidesteps this by using controllable quantum particles to stand in for the ones being modelled (Georgescu et al., 2014), so the figure of merit is the problem size it can handle faithfully beyond the classical reach. For Harrowmere, where corrosion of ductile-iron mains drives £40 million a year of replacement (fictional), even a modest improvement in coating design would matter; but simulators today are research instruments (judgement), so this is a technology to watch through university partnerships, not one to buy.

**What a weak answer misses:** It says quantum simulation is "faster" without saying what scales (memory grows as $2^N$). It confuses a special-purpose simulator with a universal quantum computer (L64 draws the line). It gives no maturity statement, so the reader thinks Harrowmere can buy one. It picks a problem with no quantum core, such as pipe-network flow, where classical simulation already works.

### Exercise 1.9 (writing)

**Errata in practice.** A Harrowmere board slide (fictional) reads: "We should adopt QKD because it uses entangled photons that cannot be intercepted, and a quantum computer will optimise our pump schedules by trying every schedule at the same time." Rewrite it as two to three accurate sentences of no more than 80 words.

**Hint:** Use the L52 and L70 corrections. Interception *can* happen; it is *detected*. For scheduling, what does measurement return, and what kind of speed-up is proven for optimisation problems? (Day 09 covers the taxonomy; for now "no proven exponential speed-up" is enough.)

**Model paragraph:** QKD protocols such as BB84 send single photons and need no entanglement; an eavesdropper can still intercept them, but doing so introduces errors the two ends can detect. A quantum computer does not try every pump schedule at once: a measurement returns one outcome, and any speed-up depends on interference that suits the problem's structure. For scheduling problems like ours, no large proven speed-up is known (judgement; see Aaronson), so this is not a reason to invest yet.

**What a weak answer misses:** It fixes "entangled" but keeps "cannot be intercepted", which is the bigger error. It replaces "tries every schedule" with "explores all schedules in superposition", which is the same myth in new words. It drops the conclusion: the slide was making a decision, so the rewrite must say what the decision should now be.

## Anti-patterns / Common mistakes

- **A gain with no classical side.** "The quantum sensor reaches 1 fT/√Hz." → You notice because part [1] of your F1 labels is empty. → Instead, state the best classical figure first, with units and conditions.
- **Lab versus field ratios.** → You notice because one side says "shielded", "laboratory" or "record" and the other says "datasheet" or "field". → Instead, compare field with field, or lab with lab, and say which.
- **Lost prefixes.** "200 fT is 2×10⁻¹⁵ T." → You notice because the power of ten does not match the prefix table (femto is $10^{-15}$, and 200 is $2\times10^2$). → Instead, write the prefix as a power of ten and combine exponents in one line.
- **Copying the lecture's errors.** "QKD uses entangled photons"; "quantum computers try all answers at once". → You notice because a sentence explains a speed-up by superposition alone, with no interference, or describes QKD with entanglement but cites BB84. → Instead, use the corrected versions in "Decoding the Week 1 lecture".
- **"Unbreakable" and "guaranteed".** → You notice the absolute word. → Instead, say what is detected, under what assumptions, and what the device-level risks are.
- **Market size as evidence of performance.** → You notice a currency where a sensitivity should be. → Instead, keep market figures for the maturity part [5] and cite them with source and date (Day 10).
- **Reading for coverage instead of writing.** → You notice you have read the lecture twice and written nothing. → Instead, write one F1 paragraph on Harrowmere first, then reread to fill the gaps.

## Done when

No notes, 20 minutes, on paper. Pass mark: 8 out of 10.

1. Name the four quantum technology types and the figure of merit for each, with a unit.
2. List the six parts of F1 in order.
3. State the F3 source hierarchy, top to bottom.
4. Give the like-for-like rule in one sentence and an example of breaking it.
5. Convert 30 µGal to m/s² and to a fraction of $g$.
6. Convert 0.5 pT to tesla, and say how many orders of magnitude it is below 50 µT.
7. State $1$ E in SI units, and the vertical gravity gradient near the surface to one significant figure.
8. A clock has $y = 5\times10^{-15}$. What is its time error after one day, and the matching distance?
9. Correct L52 in one sentence.
10. Correct L70 in one sentence, using the word "interference".

<details>
<summary>Answers</summary>

1. Sensing: sensitivity (T/√Hz, Gal/√Hz) and, for clocks, fractional stability or uncertainty (dimensionless); communication: secure key rate (bit/s) at a distance (km); simulation: problem size beyond classical reach (particles, with classical cost $\propto 2^N$); computing: runtime scaling with problem size.
2. Classical limit, with a number; quantum mechanism, in one sentence of physics; figure of merit named; quantified gain; maturity and practicality; verdict, with one honest caveat.
3. Peer-reviewed paper or metrology institute > review > vendor datasheet > press release > market report.
4. Both sides of a ratio must be measured the same way; a shielded-lab result divided by a field datasheet breaks it.
5. $3\times10^{-7}\ \text{m/s}^2$; about $3\times10^{-8}g$.
6. $5\times10^{-13}$ T; $50\times10^{-6}/5\times10^{-13} = 10^8$, so 8 orders.
7. $1\ \text{E} = 10^{-9}\ \text{s}^{-2}$; about $3\times10^{-6}\ \text{s}^{-2}$ (3000 E).
8. $\delta t = 5\times10^{-15}\times86\,400 = 4.3\times10^{-10}$ s (0.43 ns); $\delta x \approx 0.13$ m.
9. BB84 uses single photons in two bases and no entanglement; entanglement-based QKD (E91) is a separate family.
10. Superposition alone gives one random outcome on measurement; algorithms gain by arranging interference so wrong answers cancel and the right one is amplified.

</details>

## Read next

- Degen, Reinhard and Cappellaro, *Quantum sensing* (2017), §I-III: <https://arxiv.org/abs/1611.02427>. This is the lecture's own reference [3] and sets up Day 02's sensitivity language.
- Aaronson, *The Limits of Quantum Computers* (author draft): <https://www.scottaaronson.com/writings/limitsqc-draft.pdf>. Read it for the L70 erratum: what quantum computers do and do not speed up.

## Confusion log

Spend the last 15 minutes here. Note anything you could not do without looking, then write tomorrow's first question. Tomorrow (Day 02) starts the Week 2 companion §1-3.

| Unit or symbol | Step | Concept |
|---|---|---|
| | | |
| | | |
| | | |
