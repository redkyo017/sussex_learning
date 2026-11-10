# Strategy: How to Get Fluent in Module 4 Fast

This file explains how the sprint works, what it teaches and skips, which traps to avoid, how to read a lecture so it sticks, and the two write-up shapes you will use every day: the six steps for numbers and the F1 gain argument for prose. Read it once now. Come back to the reading protocol at the start of each course week.

## 1. The strategy

Module 4 asks one question in seven forms: *what does the quantum version do better than the classical one, by how much, and how mature is it?* Every Apply and Consolidate task in Weeks 1-7 is a short, quantified answer to that question (see `docs/problem_inventory.md`). There are no numbered maths problems. So the sprint is **argument-first**: it teaches the shape of the answer on Day 1, then the small set of scaling laws that put correct numbers into it, then decodes each lecture against both.

Two kinds of unit carry the content:

- **Frameworks (qualitative).** F1 gain argument (the six-part writing shape, Section 6 below); F2 maturity lens (NASA TRL 1-9, the module's quantum-advantage test, the five barrier categories, and the rule that component TRL is higher than system TRL); F3 credible numbers (source hierarchy, date, conditions and units on every figure, and both sides of a ratio measured the same way).
- **Moves (quantitative).** Fourteen small techniques, each about ten minutes, drilled cold:

| ID | Move | First taught |
|---|---|---|
| M1 | Orders of magnitude, SI prefixes, module units (T, Gal, E, fractional); fractional error → time → distance via $c$ | Day 01 |
| M2 | Noise density and bandwidth: $\delta x = S\sqrt{\Delta f}$; $1/\sqrt{t}$ averaging; Allan deviation as stability versus averaging time | Day 02 |
| M3 | Shot noise $1/\sqrt{N}$ versus Heisenberg $1/N$; SNR; the inverse-square distance gain | Day 02 |
| M4 | Two-level system as a frequency reference: $E = h\nu$, $Q = \nu/\Delta\nu$, pulse area, the lock loop | Day 03 |
| M5 | Magnetometer physics in one line each: Larmor $\gamma B$, flux quantum $\Phi_0 = h/2e$, NV spin readout | Day 03 |
| M6 | Interference: phase → $\cos^2$ intensity; $k = 2\pi/\lambda$; de Broglie $\lambda = h/mv$ | Day 04 |
| M7 | Atom interferometry: recoil $\hbar k$, $k_\text{eff} \approx 2k$, $\Phi = k_\text{eff} g T^2$, $T^2$ scaling, Sagnac ratio | Day 04 |
| M8 | Crypto in one page: one-time pad, public key and the Shor threat, harvest-now-decrypt-later, PQC versus QKD | Day 06 |
| M9 | BB84 by hand; 25% QBER under intercept-resend; $(3/4)^n$ detection; no-cloning in four lines | Day 06 |
| M10 | CHSH 2 versus $2\sqrt{2}$; fibre loss in dB/km → transmission; trusted node versus repeater | Day 06 |
| M11 | $2^N$ amplitudes and $8 \cdot 2^N$ bytes; analogue versus digital simulation; $J$ versus $U$ | Day 07 |
| M12 | Gates and circuits, Bell state, phase kickback, Deutsch-Jozsa as an amplitude sum | Day 08 |
| M13 | Speed-up taxonomy; Grover $(\pi/4)\sqrt{N}$; depth from fidelity $F^g$; error-correction overhead; threshold theorem stated correctly | Day 09 |
| M14 | Benefit/risk quantification: ranges, expected value, the weakest assumption; fact-sheet anatomy | Day 10 |

Four principles hold it together. They are Module 3's, adapted.

### Principle 1: Learn the argument shape, then the moves

**Why it works.** A topic ("quantum sensing") is huge. A shape ("classical limit with a number, mechanism, figure of merit, quantified gain, maturity, verdict") is small and reusable, and every weekly task uses it. The moves are the minimum physics that lets you fill each slot with a correct number.

**Do this.** Each day names its moves and frameworks. At the end of the day you should be able to say each one's name and perform it on a blank page.

### Principle 2: Problems before theory

**Why it works.** Trying a task cold and failing turns a vague topic into a precise question. The explanation that follows then lands on a prepared gap (Kapur 2008). A smooth first read of the lecture feels like understanding but mostly is not.

**Do this.** Before a day's core concepts, spend five to ten minutes on its first exercise with no help. With a lecture, read the week's tasks and quiz first (Pass 0 below).

### Principle 3: Retrieval over rereading

**Why it works.** Pulling an idea out of memory strengthens it far more than looking at it again (Roediger & Karpicke 2006). Spacing those recalls over days beats massing them (Cepeda et al. 2006).

**Do this.** Every day opens with 15 minutes of closed-book retrieval from earlier days, and from Day 02 a Spaced review section pulls from days N−1, N−3 and N−7. Wrong answers go on tomorrow's list.

### Principle 4: Fixed write-up shapes from Day 1

**Why it works.** A fixed shape removes decisions about presentation, leaving attention for the physics, and makes gaps visible: an empty slot is an error you can see (judgement).

**Do this.** Write every quantitative answer in the six steps (Section 5) and every prose answer in F1 (Section 6), even the easy ones. Every day has at least two writing exercises on the fictional running case, **Harrowmere Water & Power**.

### Rejected alternatives

- **Week-by-week just-in-time study.** You are a week behind, and Weeks 3 and 4 introduce new physics and cryptography at the same time.
- **A physics-first strand like Module 3's `physics/`.** This module needs about ten scaling laws, not a physics course, so the physics is folded into the days.

## 2. What we keep and what we skip

### Load-bearing fundamentals kept (and why)

- **M1 units and orders of magnitude:** every task asks for "quantitative measures".
- **M2-M3 the square-root averaging laws:** they define "sensitivity" in Weeks 2, 3 and 7.
- **M4 the two-level resonance:** clocks, optically pumped magnetometers, NV centres, Raman pulses and qubits are all the same object, and you already own its maths from Module 3.
- **M6 interference phase:** Weeks 3, 4 and 6 run on it.
- **M11 and M13 exponential versus polynomial scaling:** the entire simulation and computing argument.
- **F2 TRL:** Week 7 and every "practical aspects" clause.

### Skipped (and why)

Each item below is skipped on judgement: no inventory row examines it.

- Atomic structure derivations (hyperfine, Zeeman beyond one line)
- Josephson and BCS theory
- Laser-cooling mechanics (the magneto-optical trap is named only)
- Bose-Hubbard and BKT mathematics (story level only)
- The quantum Fourier transform and continued-fraction derivation of Shor (only the arithmetic of the classical part)
- Complexity classes beyond the speed-up taxonomy
- The full CHSH derivation
- Security proofs of QKD

If a lecture leans on one of these, the companion gives the one-sentence version you need and moves on.

## 3. The 7 mistakes that waste most beginners' time in this module

Each is written as mistake → how you notice → fix.

1. **Quoting a gain without units, conditions or a source.**
   *How you notice:* your sentence says "1000 times more sensitive" and you cannot say sensitive to what, in what unit, over what bandwidth or averaging time, or who measured it.
   *Fix:* apply F3 to every number: unit, conditions (bandwidth, averaging time, environment), date, source. If one is missing, the number does not go in.
2. **Comparing a lab record with a fielded classical product.**
   *How you notice:* the quantum figure comes from a shielded laboratory paper and the classical figure from a product datasheet, or the other way round.
   *Fix:* compare like with like (lab with lab, field with field) or say plainly that you are not, and shrink the claimed gain accordingly. F3's rule: a ratio needs both sides measured the same way.
3. **Believing the "parallel computation" myth.**
   *How you notice:* you write "a quantum computer tries all answers at once". The Week 1 lecture says this too (L70; see the inventory's errata).
   *Fix:* a measurement returns one outcome. The gain, where there is one, comes from arranging amplitudes to interfere so that wrong answers cancel (M12). Say "interference", never "parallelism".
4. **Treating QKD as unbreakable.**
   *How you notice:* you write "provably secure" with no qualifier, or forget that the key still feeds classical encryption.
   *Fix:* the physics makes eavesdropping detectable (M9). Real systems are attacked through devices, trusted nodes and side channels, key rates fall with distance (M10), and post-quantum cryptography is the competing answer (M8).
5. **TRL inflation.**
   *How you notice:* you give a whole system the TRL of its best component, or call something "commercially available" on the strength of a press release.
   *Fix:* use F2. Component TRL is higher than system TRL. Cite the evidence for each level you claim, using the Week 7 table.
6. **Copying lecture numbers without checking them.**
   *How you notice:* the same quantity appears twice in a lecture with different values, or a unit looks odd. About 15 such errors are listed in `docs/problem_inventory.md`, for example "T√Hz" for T/√Hz (Week 2 L74) and the Week 5 memory table, whose entries are 10 times too small (L55).
   *Fix:* recompute any number you reuse with M1, check it against the companion's §4, and cite a primary source rather than the lecture when they disagree.
7. **Reading for coverage instead of writing.**
   *How you notice:* you have "read Week 3" but cannot write five sentences about it with one correct number.
   *Fix:* the ratio is at least one part writing to one part reading. Every day ends with a timed F1 paragraph, and Pass 3 below is closed book.

## 4. Five-Pass Lecture Protocol

Use this for every weekly lecture from Week 2 on, together with that week's companion in `content/companions/`. It takes about 2 hours, plus the Apply and Consolidate writing.

| Pass | Time | What you do |
|---|---|---|
| 0 | 10 min | Read the week's Apply and Consolidate tasks and the quiz in `week_K/week_K_content.md`. Do not answer them; note what the week wants you to be able to argue. |
| 1 | 20 min | Read the companion's summary and picture. Skim the lecture for structure only: headings, figure captions, equations, tables of numbers. |
| 2 | 45 min | Read the lecture properly with the companion's notation and unit decoder (§3) open. Keep a confusion log (Section 7). Check each number you might reuse against the companion's errata (§4). |
| 3 | 20 min, closed book | Reproduce the week's key result from memory, and write the F1 skeleton for one application with one number per slot. Where you fail is the gap to fix. |
| 4 | as needed | Redo one companion clone with the solution covered, then a fresh variant, then explain the week's idea aloud in three sentences (the Feynman check). |

### Worked example: Week 2, clocks and magnetometers

**Pass 0 (10 min).** Open `week_2/week_2_content.md`. Apply asks for 200-300 words on a clock or magnetometer in an application area. Consolidate asks for one or two advantages over a classical limitation, quantified by "sensitivity, bandwidth or dynamic range ... or more practical use". The quiz is about which everyday devices contain magnetometers and which systems rely on precise timing. Note the target: *for one clock or magnetometer, name its figure of merit and put a number on its gain.*

**Pass 1 (20 min).** Read the Week 2 companion summary. Skim the lecture headings: §2.1 what makes a good sensor; §2.2-2.9 magnetic sensing and four quantum magnetometer types; §2.10-2.14 timing and clocks. The equations you will need are few: $B \propto 1/r^2$ in §2.3 and $E = h\nu$ in §2.13. Mark the comparison figure in §2.2 (sensitivity against spatial resolution) as one to read slowly.

**Pass 2 (45 min).** Read with the decoder open. Typical confusion-log rows:

| Where (lecture § / line) | Symbol, unit or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| §2.2, L74 | noise "T√Hz" | a unit I have to learn | a typo: the unit is T/√Hz, a noise density; multiply by $\sqrt{\Delta f}$ to get the noise in tesla over bandwidth $\Delta f$ (M2) | yes |
| §2.3, L94 | "amplitude increases by $r^2$" | moving closer multiplies the signal by $r^2$ | the ratio scales as $(r_1/r_2)^2$: halve the distance, get 4× the signal (M3) | yes |
| §2.10 | stability versus uncertainty | two words for accuracy | stability is how steadily it ticks (precision, improves with averaging); uncertainty is how far the rate may sit from the true transition (accuracy, set by systematic effects) | yes |
| §2.13 | "monitoring and maximising the fraction of atoms" | the atoms are the clock | the atoms are the reference; a local oscillator is steered so the excited fraction stays on resonance (the lock loop, M4) | not yet |

Write the row the moment you get stuck, then keep reading.

**Pass 3 (closed book, 20 min).** On a blank page:

- define precision, accuracy, bandwidth and dynamic range in one line each;
- turn a noise density into a noise figure: $\delta B = S\sqrt{\Delta f}$, with units;
- explain the lock loop in three steps, and why an optical transition (hundreds of THz) beats a microwave one (about 9 GHz) through $Q = \nu/\Delta\nu$;
- write the F1 skeleton for one application, one number per slot, leaving a slot empty if you lack a sourced number.

What you cannot reproduce goes back into the log as "not yet" and becomes tomorrow's retrieval.

**Pass 4.** Redo the companion's noise-density clone with the solution covered, then change the bandwidth and redo it. Finally say aloud: what a magnetometer's sensitivity number means, why distance to the source matters so much, and why optical clocks beat microwave ones.

## 5. Six-steps write-up (quantitative)

Use this for every numerical exercise. It is the same stand-in as Module 3's (the university's own "six steps" page is not in the exports), with step 2 widened to "write the setup".

1. **Restate** what is asked, and list the givens with units.
2. **Write the state or setup**: the quantities, the system and any sketch.
3. **Name the move** (M1-M14) you will use, in words.
4. **Algebra**, every step shown, units carried through.
5. **Check**: units, order of magnitude (M1), a limiting case, and whether the answer is physically plausible.
6. **Answer** in a full sentence, with units and a sensible number of significant figures.

### Example on a trivial problem (not a course case)

Problem: a magnetometer has a flat noise density of 2 nT/√Hz. What noise, in nT, does it show over a 25 Hz measurement bandwidth?

1. **Restate.** Find the noise $\delta B$ over bandwidth $\Delta f$. Given: $S = 2\ \text{nT}/\sqrt{\text{Hz}}$, $\Delta f = 25\ \text{Hz}$.
2. **Setup.** White (frequency-independent) noise, so the density is the same across the 25 Hz band.
3. **Name the move.** M2: noise over a bandwidth is density times the square root of the bandwidth, $\delta B = S\sqrt{\Delta f}$.
4. **Algebra.** $\delta B = 2\ \text{nT}/\sqrt{\text{Hz}} \times \sqrt{25\ \text{Hz}} = 2 \times 5\ \text{nT} = 10\ \text{nT}$.
5. **Check.** Units: $\sqrt{\text{Hz}}$ cancels, leaving nT. Limit: as $\Delta f \to 0$, $\delta B \to 0$, as averaging forever should give. Scaling: four times the bandwidth would double the noise, not quadruple it.
6. **Answer.** Over a 25 Hz bandwidth the magnetometer shows about 10 nT of noise.

## 6. F1 gain argument (writing)

F1 is the writing twin of the six steps. Every Apply and Consolidate piece in this module fits it.

1. **Classical limit, with a number.** What the best classical option achieves and why that is not enough.
2. **Quantum mechanism, in one sentence of physics.**
3. **Figure of merit named.** The quantity that defines "better" here (sensitivity per √Hz, fractional frequency stability, secure key rate at a distance, problem size or scaling).
4. **Quantified gain.** A ratio or a scaling, sourced, with both sides measured the same way (F3).
5. **Maturity and practicality.** TRL with evidence, SWaP-C (size, weight, power and cost), the main barrier (F2).
6. **Verdict, with one honest caveat.**

Budget for 300 words: about 60 / 30 / 20 / 80 / 60 / 50 (judgement). Parts 1 and 4 carry the marks for "quantitative".

### Annotated 300-word example: Harrowmere Water & Power

All Harrowmere figures are invented for practice and labelled (fictional). In a real piece every figure in parts 1 and 4 needs a citation. The part labels in brackets are annotations, not part of the word count.

> **Holding grid time through a satellite-timing outage at Harrowmere Water & Power**
>
> **[1 Classical limit]** Harrowmere Water & Power time-stamps measurements at its 38 substations (fictional) from satellite timing, with oven-controlled quartz oscillators as back-up. Its protection and phasor measurement need every substation clock within 1 µs of UTC (fictional requirement), and it designs for an 8 h loss of satellite timing (fictional). After loss of lock the quartz units hold a fractional frequency offset of about $1\times10^{-9}$ (fictional datasheet figure). Taking that offset as constant, the 1 µs budget is spent in about 17 minutes, and an 8 h outage leaves the clock $10^{-9} \times 28\,800\ \text{s} = 28.8\ \mu\text{s}$ out.
>
> **[2 Mechanism]** An atomic clock steers its oscillator to an atomic transition whose frequency is fixed by nature through $E = h\nu$, so its rate does not wander with crystal ageing and temperature the way quartz does.
>
> **[3 Figure of merit]** The relevant figure is holdover: how long the clock stays inside the 1 µs budget with no external reference. It is set by the fractional frequency offset.
>
> **[4 Quantified gain]** A compact rubidium clock holding $5\times10^{-12}$ (fictional datasheet figure) gathers only 0.144 µs over the same 8 h, so it passes where quartz fails, and holdover rises from about 17 minutes to about 56 hours, a factor of 200. The comparison is fair only because both offsets are quoted after the same warm-up and over the same temperature range.
>
> **[5 Maturity and practicality]** Compact atomic clocks are sold as products, so component TRL is 9. Harrowmere's integrated substation timing system has not been trialled, so system TRL is about 6 (judgement). Each unit costs about ten times a quartz oscillator (fictional), which is affordable at 38 substations but not at 4,000 pole-mounted sensors.
>
> **[6 Verdict]** For the substations the gain is decisive: the 8 h outage design case becomes survivable, with a margin of about 7. The caveat is that holdover depends on temperature control in unheated roadside cabinets, which the datasheet figure does not cover, so a winter field trial should come before purchase.

**Annotations.**

- **Part 1** gives the requirement *and* the classical shortfall as numbers, and shows the M1 conversion (fractional offset → time error over the outage → time to exhaust the budget).
- **Part 2** is one sentence of physics. It does not explain hyperfine structure (skipped on purpose).
- **Part 3** names the figure of merit. Here it is holdover, not the record stability of a laboratory clock, which would be mistake 2.
- **Part 4** gives a ratio (200×) and states why both sides are comparable (F3). The arithmetic: $1\ \mu\text{s} / 10^{-9} = 1000\ \text{s} \approx 17$ min; $1\ \mu\text{s} / (5\times10^{-12}) = 2\times10^{5}\ \text{s} \approx 56$ h; over 8 h, $5\times10^{-12} \times 28\,800\ \text{s} = 0.144\ \mu\text{s}$.
- **Part 5** separates component TRL from system TRL (F2) and names SWaP-C through cost.
- **Part 6** commits to a verdict and names the weakest assumption, which is what M14 later turns into a benefit/risk range.

## 7. Confusion-log template

Copy this table into your notes for each lecture. Fill a row the moment you are stuck; resolve it at the end of the session or in the next retrieval block. The "unit" in the second column matters in this module: about half the lecture errors are unit or factor errors.

| Where (lecture § / line) | Symbol, unit or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## 8. Using AI

AI is a strong study partner for this module. Ways to use it:

- **Tutor on a stuck step.** Paste one lecture line and your confusion-log row, and ask for the missing step.
- **Examiner for Pass 3 and the Spaced review.** "Ask me 5 closed-book questions on M7, one at a time; don't give answers until I've replied."
- **Fresh numbers.** "Give me a new instance of the M2 noise-density move with different numbers, no solution." Unlimited clone practice.
- **Critic and co-writer.** Paste a paragraph with the F1 six parts and the F3 rules and ask "which part is missing or weakest, and which number is not sourced?", or draft and iterate together.
- **Source finder.** Ask for primary sources on a claim, then fill the F3 extraction card from the source itself.

**The handoff.** Every model paragraph here uses the fictional Harrowmere case. From Day 10 you switch to your own case.

## 9. Where's the evidence?

The method rests on three standard findings, the same ones Module 3's strategy uses:

- **Retrieval practice:** testing yourself beats rereading for long-term retention (Roediger & Karpicke 2006). Hence the daily retrieval block and the closed-book Pass 3.
- **Spacing:** recall spread over days beats the same amount massed together (Cepeda et al. 2006). Hence the N−1, N−3, N−7 Spaced review and the +7 and +21 day sets after the sprint.
- **Productive failure / problem-first:** a struggled-with problem before instruction improves transfer (Kapur 2008). Hence the cold first exercise and Pass 0.

The specific 10-day split and the claim that about 3 h a day is enough are **judgement**. They are based on the lecture length (about 380 KB of text, light on maths) and on Module 3's 32.5 h sprint for a more mathematical module. The F1 word budget and the "one part writing to one part reading" ratio are also judgement.

## Harrowmere Water & Power: the shared fact sheet (fictional)

Every figure here is invented for practice and is labelled (fictional) wherever it is used. Days and companions quote these values; only clearly hypothetical candidate devices may vary per exercise.

| Area | Fact (all fictional) |
|---|---|
| Company | Regional water and power utility; 1.2 million customers; 38 substations; 2,400 km of water mains (ductile iron and steel) |
| Timing requirement | Substation clocks must stay within 1 µs of UTC for protection and phasor measurement |
| Timing outage design case | 8 h loss of satellite timing (jamming or antenna fault) |
| Installed holdover oscillator | Quartz (OCXO), fractional frequency offset 1×10⁻⁹ after loss of lock |
| Candidate holdover clock | Rubidium, fractional offset 5×10⁻¹²; costs 10× the quartz unit |
| Cable and main inspection | Buried 11 kV cables and mains at 1.0-2.0 m depth; Earth's field 50 µT on site |
| Gravity survey site | Greystock reservoir embankment; suspected void target signal about 5 µGal; 150 survey stations |
| Installed gravimeter | Relative spring meter: noise 8 µGal/√Hz, drift 30 µGal/day, 14 kg |
| Candidate quantum gravimeter | Portable atom gravimeter: absolute, noise 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation |
| Control network | Control centre linked to four sites over dark fibre at 12, 38, 95 and 160 km |
| Telemetry keys | AES-256 key refreshed every 60 s per site; data must stay confidential for 15 years; a full cryptographic migration takes 5 years |
| Materials problem | Corrosion of ductile-iron mains drives £40 million a year of replacement |
| Pump scheduling | 220 pumps, 4 electricity tariff bands; energy bill £18 million a year **with** the current classical optimiser, which already saves 6% against an unoptimised schedule (so the unoptimised bill would be about £19.1 million and today's saving about £1.15 million) |
