# Day 10: Maturity, Comparison and the Capstone

**Time:** ~3 h core + about 2 h capstone · **Feeds:** Week 7 lecture (all, L9-L137), inventory rows W7 Explore, W7 Apply, W7 Consolidate; through the capstone, every Consolidate row W1-W6 · **Companion:** week07_companion.md §3 (framework decoder), §4A (full TRL checklist), §4D (market numbers), §5-§6 (clones and cold attempt)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min frameworks F2 and F3 and move M14 below · 50 min quantitative drills (Exercises 10.1 and 10.2; 10.2(c) is *stretch*) · 45 min writing: Exercise 10.3 (30 min, timed, on the running case) and Exercise 10.4 (15 min, your own case); 10.5 is *stretch* · 15 min companion pointer, confusion log and What next.

**Capstone (separate session, about 2 h, no notes):** Exercises 10.6 to 10.15 (ten quantitative items, 50 min), then Exercise 10.16 (timed 300-word F1 piece, 40 min), then 30 min marking. Your fact sheet from Exercise 10.3, written under time, is the capstone's fact sheet. Do the capstone this evening after a break, or first thing on Wed 25 Nov before your own pieces. Do not split it across days.

Day 10 is the heaviest day of the sprint. If you run past 3 h in the core, drop Exercise 10.5 and 10.2(c) (stretch), not the capstone. There is no separate self-test today: "Done when" item 9 is the capstone, and items 1-8 are checked inside it.

## Why this matters

Week 7 asks the module's question one last time, but now across all four technology types at once: *which is mature enough to matter, and is the benefit worth the risk?* The Apply task wants a one-page fact sheet. The Consolidate task wants 300 words with "a quantitative assessment of the benefit/risk ratio". The Explore task wants the "largest markets". The lecture gives you a maturity scale (Table 7.1) and five barrier categories. It gives no procedure for assigning a level, no method for a benefit/risk ratio, and no market figure at all.

Those three gaps are where weak Week 7 pieces fail. They score a whole system at its best component's TRL. They quote one confident benefit number with no probability. And they paste a market figure with no date or scope. As a backend engineer you already do this kind of thinking under other names: a TRL is a release-readiness gate, the five barriers are a launch checklist, and a benefit/risk range is an incident-cost model with error bars. Today gives that thinking the module's vocabulary.

Day 10 also closes the sprint. From tomorrow you write on your own case. So today's last writing exercise is a decision table about *your* background with no model answer (only you know its numbers), and the capstone tells you, with a score, what to keep reviewing.

## Core concepts

### Framework F2.1: The TRL scale, verbatim, and three interpretation rules

**Idea.** The lecture uses NASA's nine levels (Table 7.1, L11-L22). Learn the wording exactly, because the distinctions live in single words (laboratory, relevant, operational, qualified, proven):

| TRL | Definition (lecture Table 7.1) |
|---|---|
| 1 | Basic principles observed and reported. |
| 2 | Technology concept and/or application formulated. |
| 3 | Analytical and experimental critical function and/or characteristic proof-of-concept. |
| 4 | Component and/or breadboard validation in laboratory environment. |
| 5 | Component and/or breadboard validation in relevant environment. |
| 6 | System/subsystem model or prototype demonstration in a relevant environment. |
| 7 | System prototype demonstration in an operational environment. |
| 8 | Actual system completed and qualified through test and demonstration. |
| 9 | Actual system proven through successful mission operations. |

Three rules from the lecture's own text:

1. **A sale is not TRL 9 (L24).** The lecture's example is a QKD system that was sold but "is not routinely used because it doesn't fulfil all the requirements of the market", so it sits at the field-test level, TRL 6 or 7. TRL 9 means proven in routine use that meets the user's requirements.
2. **Component TRL is higher than system TRL (L24, L74, L137).** Lasers, vacuum cells and cryostats can be catalogue products while the system built from them is a prototype. Score the system, and never above its weakest essential component (judgement).
3. **Wide ranges are honest (L51, L52, L54, L56).** OPMs appear at TRL 9 and TRL 2-3 in one paragraph because three different technology-application pairs are being scored. The lecture says its levels are "a guideline rather than factual quantitative information" (L24).

**Short checklist** (the full seven-step version, with evidence prompts, is in week07_companion.md §4A):
- Name the pair: technology *for* application.
- Component or system? Only components means a ceiling of TRL 5.
- Where has the most complete version been shown: paper, bench, relevant environment, operational environment?
- Qualified (8) or proven in routine operations (9)? A sale is not proof.
- Write one evidence sentence per level you claim: "TRL N because [what was shown], [where], [source, date]".

*Worked clone (hypothetical, not a course case).* A manufacturer considers an NV-diamond magnetometer to inspect weld seams on a production line. The pair is "NV magnetometer *for* in-line weld inspection". The lecture puts NV magnetometers at TRL 4-7 across implementations (L52). The components (diamond, green laser, microwave source) are bought parts at high TRL. Suppose (hypothetical) the vendor has shown one sensor head on a lab bench next to sample welds, but nothing on a moving line. That is "component validation in laboratory environment": TRL 4 for this pair. A test of the head beside a running line, with vibration and stray fields, would make it 5. An inspection station on the line would be needed for 6.

*You've got it when* you can recite levels 4 to 7 word for word, say what separates 4 from 5 (environment) and 5 from 6 (component versus system), and correct a "TRL 9 because it's for sale" claim in one sentence.

### Framework F2.2: The advantage test (L88)

**Idea.** The lecture defines quantum advantage as the ability "to perform a **relevant** task that cannot be fulfilled (with reasonable effort) by any (known) conventional technology" (L88). Read it as three clauses, each of which can fail:

1. **Relevant.** Someone needs the task done and would pay (this is barrier 2's "pull").
2. **No known conventional technology does it.** The baseline is the *best* classical method, measured the same way (F3). A weak baseline makes a fake advantage.
3. **With reasonable effort.** A classical method that needs a supercomputer for a month may still count as "reasonable" if the quantum route needs ten years of development (judgement: the lecture does not define "reasonable effort").

The verdict has three possible values: *shown*, *shown only in a niche science problem*, *not yet shown*. The lecture's own scoring: clocks and sensors pass "by large margins"; quantum computing has outperformed conventional computing "in niche science problems" (L98), but "clear evidence ... in an industrially relevant problem is still missing" (L99).

*Worked clone (hypothetical).* A courier firm is told a quantum annealer will plan its van routes. Clause 1 passes: routing costs real money. Clause 2 fails on present evidence: no advantage over the best classical solvers on an industrially relevant problem (L99), and annealing speed-ups are heuristic (Day 09, M13). Clause 3 is moot. Verdict: *not yet shown*. The useful next step is a like-for-like benchmark, not a purchase.

*You've got it when* you can state the three clauses from memory and give the lecture's verdict for sensing and for computing, with line numbers.

### Framework F2.3: The five barrier categories, in the lecture's order (L106-L137)

**Idea.** The lecture lists five kinds of obstacle between "feasible in principle" and "routinely used". Map every risk you name onto one of them, and say which one *gates* the decision: the one that, if unresolved, makes the others irrelevant.

| # | Barrier (lecture) | Lines | The question to ask | Evidence that it is cleared |
|---|---|---|---|---|
| 1 | Technological developments | L106-L108 | Does it work under the application's conditions, and at acceptable size, weight, power and cost (SWaP-C)? | performance and robustness figures in the target environment |
| 2 | Proof of relevance and practicality | L110-L112 | Is there market pull, with an advantage shown "in a relevant context" and a credible road map? | a like-for-like benchmark on a task the user needs |
| 3 | Use cases | L114-L123 | Is there a contained-scope, relevant pilot that shows the advantage and gives first performance measures? | a completed pilot with numbers and lessons |
| 4 | Validation of usability | L125-L133 | Does it work in routine use, and are regulation, standards, calibration, documentation and user interface in place? | wider trials; standards and approvals |
| 5 | Scalable and robust production | L135-L137 | Can it be built, repaired and bought again, from modular, high-TRL components and robust supply chains? | multiple suppliers; warranties; modular designs |

The order roughly follows the TRL ladder from bottom to top (judgement: the lecture presents them as types, and several run in parallel).

*You've got it when* you can list the five in order without notes and place "needs a 4 K cryostat on site" (1), "no one has asked for this" (2), "regulator has not approved it" (4) and "one supplier worldwide" (5) correctly.

### Move M14.1: Ranges, expected value, break-even and the weakest assumption

**Idea.** A quantum investment is a bet: a known cost now, an uncertain benefit later. Four numbers make the bet honest.

- **Ranges, not points.** Every uncertain input gets a low, central and high value, and you carry all three through.
- **Expected value.** With cost $C$, benefit $B$ if it works, and probability $p$ that it works: $\mathrm{EV} = pB - C$.
- **Break-even probability.** $p^* = C/B$. If your honest $p$ is below $p^*$, the bet loses money on average.
- **Sensitivity to the weakest assumption.** Change one input at a time from low to high with the others at central, and record how far EV moves (its *swing*). The input with the largest swing is the one your decision rests on; report the value at which it flips EV's sign. (This is a "tornado" analysis, judgement on the name.)

*Worked clone (hypothetical, not a course case).* A pilot costs $C = £200$k. If it works it saves £150k a year for 5 years, so $B = £750$k. Take $p = 0.3$ (range 0.1-0.5).
- $\mathrm{EV} = 0.3\times750 - 200 = +25$ (£k).
- At $p = 0.1$: $75 - 200 = -125$. At $p = 0.5$: $375 - 200 = +175$.
- $p^* = 200/750 = 0.27$: the central $p$ only just clears it.
- Now vary the annual saving from £100k to £200k at $p = 0.3$: $B$ runs from £500k to £1,000k and EV from $-50$ to $+100$.
- Swing: $p$ moves EV by 300; the saving by 150. So $p$ is the weakest assumption, and the case flips negative below $p = 0.27$.

*You've got it when* you can compute EV, its range and $p^*$ in under five minutes, and name the input with the largest swing.

### Move M14.2: Writing a "quantitative benefit/risk ratio" honestly

The Week 7 Consolidate task asks for "a quantitative assessment of the benefit/risk ratio". The phrase has no standard definition, so **define yours in the sentence that uses it**. The cleanest is

$$R = \frac{\text{expected benefit}}{\text{cost committed}} = \frac{pB}{C} = \frac{p}{p^*}.$$

$R > 1$ means a positive expected value. In the worked clone, $R = 225/200 = 1.1$.

Seven rules:
1. Give the definition, the numerator and the denominator. A ratio with no definition cannot be checked.
2. Give the range of $R$ (or of EV), not one point.
3. Give $p^*$. A reader can then supply their own $p$.
4. Name the weakest assumption and the value at which the decision flips.
5. Label every number: sourced (with date), fictional, hypothetical or judgement.
6. Keep two significant figures. A probability you made up does not deserve three.
7. "Best-case benefit over cost" is not a benefit/risk ratio. It leaves out $p$, and with it the chance ($1-p$) that the benefit fails to arrive, which is the risk the ratio exists to weigh.

A usable sentence shape: *"On [labelled] figures, the expected benefit is £X against a cost of £Y, a benefit/risk ratio (expected benefit over cost) of R (range R₁-R₂); it breaks even at a success probability of p\*, and the decision turns on [weakest assumption], which flips it at [value]."*

*You've got it when* you can write that sentence for the worked clone from memory.

### Framework F3 again: credible market numbers (Explore task, L98)

The lecture speaks of "unprecedented large investments" (L98) but gives no figure, and the Explore task asks for the "largest markets". Use one source, and use it carefully: **McKinsey, *Quantum Technology Monitor 2026*, April 2026, executive summary**, <https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point>.

This day does not quote its figures. Copy them yourself, at source, onto an **extraction card**:

| Field | What to write |
|---|---|
| Figure | the number, currency and unit, exactly as printed |
| Kind | investment (start-up or public funding), revenue to date, projected market size, or projected economic value. These are four different things |
| Year | the year the figure *refers to* (2025 actuals? a 2035 projection?), separate from the publication date |
| Segment | computing, communication or sensing, or all three combined |
| Range or scenario | the report's own low-high range or scenario name, if it gives one |
| Where | section or exhibit in the executive summary |
| Caveat | "consultancy projection, April 2026" |

Three rules:
- A market report sits at the bottom of F3's hierarchy. It is a forecast, not a measurement, and the title's "commercial tipping point" is a thesis.
- Never add figures from different reports, years or kinds.
- A market size is not a benefit to *your* case. It tells you who else is investing (barrier 5 and supply), not whether your $p$ is high.

For UK *public* funding, use the UK National Quantum Strategy (DSIT 2023), summary and missions, <https://www.gov.uk/government/publications/national-quantum-strategy>, with the same card. week07_companion.md §4D notes its headline commitment; confirm it on the page before quoting.

*You've got it when* you can fill the card's seven fields for one figure and write it as one sentence with date, kind, segment and caveat.

### Move M14.3: Fact-sheet anatomy (Week 7 Apply)

The Apply task asks for about one A4 page covering "the most relevant features", "the way in which the quantum technology represents an advantage over conventional non-quantum solutions" and "how these advantages promote applications". Those three, plus what Consolidate needs, give six blocks. One A4 page is about 400-450 words with one small table.

| Block | Content | Words (judgement) | F1 part |
|---|---|---|---|
| Header | Technology *for* application, organisation, date, one-line claim | 25 | 6 (preview) |
| 1 Features | 3 bullets: what it is, the physics in one line, what it outputs | 70 | 2 |
| 2 Advantage over the incumbent | a two-column table: figure of merit, incumbent value, quantum value, same conditions (F3); or "not yet shown" | 90 | 1, 3, 4 |
| 3 How the advantage helps | the application chain from figure of merit to money, safety or capability, with numbers | 70 | 4 |
| 4 Maturity | system TRL for the pair with an evidence sentence; component TRL; the gate barrier | 60 | 5 |
| 5 Risks and benefit/risk | the main risks mapped onto barriers 1-5; EV, range, $p^*$, $R$ with its definition | 80 | 5, 6 |
| 6 Sources | 3-5 dated sources in F3 order; labels for fictional, hypothetical and judgement figures | 40 | F3 |

The fact sheet is a *summary of evidence*. The 300-word Consolidate piece is the *argument*: it takes the fact sheet's numbers and runs them through F1 to a verdict.

*You've got it when* you can draw the six blocks on a blank page, with the table in block 2, in under two minutes.

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. All Harrowmere Water & Power figures are from the shared fact sheet in STRATEGY.md and are labelled (fictional). Prices and probabilities the fact sheet does not give are labelled (hypothetical).

### Exercise 10.1 (quantitative)

*Inventory rows W7 Apply and W7 Consolidate.* Harrowmere's materials problem (fictional): corrosion of ductile-iron mains drives £40 million a year of replacement across 2,400 km of mains. A research group offers quantum simulation of corrosion and inhibitor chemistry, aiming to find an inhibitor or lining that slows corrosion. Hypothetical figures:
- If it succeeds, replacement spend falls by $s = 5\%$ (range 2-10%) for 10 years after deployment; no discounting.
- The probability that the quantum route delivers such a result within the horizon, one that classical methods would not have found, is $p = 0.02$ (range 0.005-0.05).
- Option P (partner): a three-year consortium place at £0.5 million.
- Option B (buy): an in-house programme with cloud quantum access and two specialists at £3 million over three years, with the same $p$ (spending more does not mature the hardware faster).

(a) Find the replacement spend per km of main per year. (b) Find the annual saving and the 10-year benefit $B$ if it succeeds. (c) Find EV for option P at central values, and its range when $p$ varies alone and when $s$ varies alone. (d) Find $p^*$ and the benefit/risk ratio $R = pB/C$ for both options, and EV for option B. (e) Which assumption is weakest? (f) What consortium fee makes option P break even at central values?

**Hint:** Work in £ million. $B = 10\times s\times40$. $\mathrm{EV} = pB - C$, $p^* = C/B$, $R = pB/C$. For (e), compare the swing in EV when $p$ runs over its range with the swing when $s$ runs over its range (Move M14.1).

**Solution sketch:**
1. *Restate.* Given £40M a year, 2,400 km, $s = 0.05$ (0.02-0.10), 10 years, $p = 0.02$ (0.005-0.05), $C_P = 0.5$, $C_B = 3$ (£M). Want spend per km, $B$, EVs with ranges, $p^*$, $R$, the weakest assumption, and the break-even fee.
2. *Write state.* $B = 10\times40\,s$; $\mathrm{EV} = pB - C$; $p^* = C/B$; $R = pB/C$.
3. *Name move.* M1 (unit cost), M14.1 (EV, ranges, break-even, swing), M14.2 (ratio with its definition).
4. *Algebra.*
   - (a) $40\times10^{6}/2400 = £16{,}700$ per km per year.
   - (b) Saving $0.05\times40 = £2$M a year; $B = 10\times2 = £20$M.
   - (c) $\mathrm{EV}_P = 0.02\times20 - 0.5 = 0.4 - 0.5 = -0.1$. With $p$ alone: $0.005\times20 - 0.5 = -0.4$; $0.05\times20 - 0.5 = +0.5$. With $s$ alone ($B = 8$ to 40): $0.02\times8 - 0.5 = -0.34$; $0.02\times40 - 0.5 = +0.3$.
   - (d) Option P: $p^* = 0.5/20 = 0.025$; $R = 0.4/0.5 = 0.8$. Option B: $p^* = 3/20 = 0.15$; $R = 0.4/3 = 0.13$; $\mathrm{EV}_B = 0.4 - 3 = -2.6$.
   - (e) Swing for $p$: $0.5 - (-0.4) = 0.9$. Swing for $s$: $0.3 - (-0.34) = 0.64$. So $p$ is the weakest assumption. EV turns positive above $p = 0.025$.
   - (f) $C = pB = 0.02\times20 = £0.4$M.
5. *Check.* $R = p/p^*$: $0.02/0.025 = 0.8$ for P and $0.02/0.15 = 0.13$ for B. Both match. Option B's break-even, 15%, is three times the top of the $p$ range, so no reasonable belief rescues it. Any discounting would push every EV down, because the benefit comes a decade or more after the cost.
6. *Answer.* (a) About £16,700 per km per year. (b) £2M a year, £20M over 10 years. (c) EV for P is −£0.1M; range −£0.4M to +£0.5M in $p$, −£0.34M to +£0.3M in $s$. (d) P: $p^* = 2.5\%$, $R = 0.8$. B: $p^* = 15\%$, $R = 0.13$, EV −£2.6M. (e) The success probability $p$; the case for P flips at 2.5%. (f) A fee of £0.4M or less. Verdict: do not buy. Partnering is close to break-even, so it is a "watch, or partner with a stage gate" decision, not a "buy" one.

### Exercise 10.2 (quantitative)

*Inventory row W7 Consolidate (auditing a ratio).* A vendor's slide to Harrowmere (hypothetical) reads: "Our OPM cable-fault locator eliminates dry digs. You spend £1.2M a year on them; our service costs £100k a year. Benefit/risk ratio 12:1." Harrowmere's buried 11 kV cables lie at 1.0-2.0 m depth, and Earth's field on site is 50 µT (fictional). Hypothetical: Harrowmere makes 300 dry digs a year at £4k each. If the locator works in Harrowmere's conditions, it removes 40% of them (range 20-60%). The probability that it works there is $p = 0.6$. The true cost is £150k a year (the £100k fee plus £50k of training and crew time).

(a) Recompute the expected annual benefit, the ratio $R$ (expected benefit over full cost) and its range. By what factor did the slide overstate $R$? (b) Find the break-even $p$. (c) A 100 A load current (hypothetical) flows in a cable. Using $B = \mu_0 I/(2\pi r)$ with $\mu_0/2\pi = 2\times10^{-7}$ T m/A, find the field at 1.0 m and 2.0 m. Compare with a classical fluxgate noise of about $10\ \text{pT}/\sqrt{\text{Hz}}$ (judgement) in a 1 Hz bandwidth. Does the OPM's extra sensitivity address what limits fault location? *(stretch)*

**Hint:** Expected benefit $= p\times f\times£1.2$M. A long straight cable is a line current, so the field falls as $1/r$ (Day 02, M3, $n = 1$). For (c), compute an SNR.

**Solution sketch:**
1. *Restate.* Given 300 × £4k = £1.2M a year; $f = 0.4$ (0.2-0.6); $p = 0.6$; full cost £150k a year; $I = 100$ A at 1.0 and 2.0 m; fluxgate $10\ \text{pT}/\sqrt{\text{Hz}}$. Want the honest $R$ and its range, the overstatement, $p^*$, and the field and SNR.
2. *Write state.* Benefit $= p f\times1200$ (£k); $R = \text{benefit}/150$; $p^* = 150/(f\times1200)$; $B(r) = 2\times10^{-7}I/r$.
3. *Name move.* M14.2 (ratio with probability), M14.1 (break-even), M3 (distance law), M2 (noise in a bandwidth), F2.2 (relevance).
4. *Algebra.*
   - (a) $0.6\times0.4\times1200 = £288$k a year; $R = 288/150 = 1.9$. At $f = 0.2$: $144/150 = 0.96$. At $f = 0.6$: $432/150 = 2.9$. Net central $= 288 - 150 = +£138$k a year. The slide's 12 against 1.92 is an overstatement by a factor of 6.25.
   - (b) $p^* = 150/(0.4\times1200) = 0.31$.
   - (c) $B(1.0) = 2\times10^{-7}\times100/1.0 = 2.0\times10^{-5}$ T $= 20$ µT. $B(2.0) = 10$ µT. Fluxgate noise in 1 Hz $= 10$ pT. SNR at 2.0 m $= 10^{-5}/10^{-11} = 10^{6}$.
5. *Check.* Doubling depth halves the field, as $1/r$ requires. The slide's 12:1 is $1200/100$: it assumes $p = 1$, $f = 1$ and leaves out £50k of cost. $R = p/p^* = 0.6/0.3125 = 1.92$, consistent.
6. *Answer.* (a) Expected benefit about £288k a year; $R \approx 1.9$ (range 0.96-2.9), not 12. The slide overstates it about sixfold. (b) It breaks even at $p \approx 0.31$, so the bet is reasonable at 0.6. (c) 20 µT and 10 µT, a million times the fluxgate's noise. Sensitivity is not what limits fault location (a cable field comparable with Earth's 50 µT, interference and localisation are). The OPM's quantum advantage does not apply here. If the service works, it works for classical reasons, so judge it as an ordinary service on a trial.

### Exercise 10.3 (writing)

*Inventory row W7 Apply.* **Timed: 30 minutes.** This is the capstone's fact sheet. Write a one-page A4 fact sheet (400-450 words, one table) on *quantum simulation for corrosion of Harrowmere's ductile-iron mains*, using your numbers from Exercise 10.1. Follow the six blocks of Move M14.3.

**Hint:** Block 2 must be honest. The figure of merit is the accuracy of predicted reaction energies for corrosion and inhibitor-binding steps at model sizes classical exact methods cannot reach. The quantum side of the comparison is "not yet shown". Use the $8\cdot2^N$ memory wall (Day 07, M11) for the classical limit, the lecture's simulation TRL (L74) and the L99 verdict for maturity, and Day 09's physical:logical ratio for the hardware gap.

**Model paragraph:** (here, a model fact sheet)

> **Quantum simulation *for* corrosion of ductile-iron mains. Harrowmere Water & Power (fictional), fact sheet, 24 Nov 2026**
> *Claim: a long-term option worth watching, not a purchase.*
>
> **1 Features**
> - A quantum simulator or computer represents interacting electrons with qubits, so its memory grows with the number of particles $N$, not as $2^N$ (Georgescu, Ashhab & Nori 2014, §I).
> - The target is strongly interacting electrons, as in iron oxides and inhibitor molecules bound to iron, where approximate classical methods are least reliable (judgement).
> - Output: reaction and binding energies that rank candidate inhibitors and linings before laboratory tests.
>
> **2 Advantage over the incumbent**
>
> | Figure of merit | Incumbent (classical) | Quantum |
> |---|---|---|
> | Exact model of $N$ interacting electrons | $8\cdot2^N$ bytes: about 9 PB at $N = 50$ | about $N$ logical qubits |
> | Accuracy on a relevant iron-chemistry problem | approximate methods plus lab immersion tests, in use today | not yet shown (Week 7 L99) |
>
> **3 How the advantage would help**
> Replacement costs £40M a year over 2,400 km, about £16,700 per km (fictional). A better inhibitor that cut replacement spend by 5% (range 2-10%, hypothetical) would save £2M a year, £20M over ten years.
>
> **4 Maturity**
> Quantum simulation sits at systems TRL 1-2, with components higher (L74). For this pair: TRL 2, concept formulated, with no proof-of-concept on ductile-iron chemistry (judgement). A useful model may need of order 100 logical qubits, about 88,000 physical qubits at roughly 880 physical per logical (judgement; Day 09). Reported counts reach thousands, but those are annealer qubits (L88), not comparable with gate-model counts (Day 09), and quoted counts are physical, not logical (L94). Gate barrier: 2, proof of relevance.
>
> **5 Risks and benefit/risk**
> Barrier 1: error correction is not yet practical at this scale. Barrier 2: no advantage shown on an industrial chemistry problem. Barrier 3: needs a contained use case, such as one inhibitor-binding energy checked against lab data. Barrier 4: new inhibitor chemicals in drinking water need regulatory approval. Barrier 5: access through cloud providers only.
> On hypothetical figures ($p = 2\%$, range 0.5-5%): a £0.5M consortium place has expected net value −£0.1M (range −£0.4M to +£0.5M) and $R = 0.8$ (expected benefit over cost), breaking even at $p = 2.5\%$. A £3M in-house programme has EV −£2.6M and breaks even only at $p = 15\%$.
>
> **6 Sources**
> Week 7 lecture L74, L88, L94, L99 (2023 references); Georgescu, Ashhab & Nori, RMP 86, 153 (2014), arXiv:1308.6253; McKinsey Quantum Technology Monitor, April 2026, for market context (figure, kind and year to be copied at source). Company figures fictional; prices and probabilities hypothetical; qubit estimates judgement.

**What a weak answer misses:** It fills block 2 with a quantum number that does not exist, instead of writing "not yet shown". It gives "TRL 4-5" because qubits are sold (component ≠ system). It uses "simulation will cut corrosion costs" with no saving, range or probability. It lists risks without mapping them to barriers, or misses barrier 4 (drinking-water regulation is this case's non-technological gate after barrier 2). It cites no dates, or quotes a market figure as if it were a benefit to Harrowmere. It runs past one page.

### Exercise 10.4 (writing)

*Inventory rows W7 Apply and W7 Consolidate (your own case).* **Map your own background.** This exercise has a hint but deliberately no model paragraph: it is your portfolio case, and only you know its numbers. An AI critique against the checklist below is a good use of AI (STRATEGY §8). Fill in this decision table for your own work (15 minutes). One line per cell. Put a number where you can and "unknown: [where I would look]" where you cannot.

| Candidate technology | Does my work have this limitation? | Measurable today? (metric, current value) | Figure of merit | TRL (pair + evidence) | Who would pay? |
|---|---|---|---|---|---|
| Atomic or optical clocks (timing) | | | | | |
| Quantum magnetometers | | | | | |
| Atom interferometers (gravity, inertial) | | | | | |
| QKD (and its rival, post-quantum cryptography) | | | | | |
| Quantum simulation | | | | | |
| Quantum computing (optimisation and other claims) | | | | | |

Question prompts. They are questions to ask yourself, not answers:
- **Precise timing for distributed systems and time-stamping.** Which of my systems order events by timestamp across machines? What synchronisation accuracy do they assume, and where is that number written down? What happens to ordering, logs or audit trails when synchronisation is lost, and how long before it matters? What distributes time to my machines, and which link in that chain sets the error?
- **Post-quantum migration versus QKD for API and TLS security.** Which traffic through my gateways must stay confidential for $x$ years, and how long would a migration take ($y$)? What does Mosca's $x + y > z$ say for it? Which technology fits the path this traffic takes?
- **Optimisation claims.** Which scheduling, routing, capacity or placement problems do we solve with classical solvers today? What is the baseline, measured how and against what? If a vendor quoted a percentage, against which baseline would I have to put it (F3, Day 09)?

Then circle at most two rows. For each, write one sentence: "The limitation is [ ], measured as [ ], and the quantum figure of merit that would address it is [ ]."

**Hint:** Most rows will end "no such limitation" or "not measurable today". That is a useful result, not a failure: the Week 7 piece is stronger on one row with a real number than on three rows with none. Fill the "Measurable today?" column first. If you cannot name a metric you could look up this week, that row is not your case. For the TRL column, name the *pair* (technology *for* your application), not the technology alone (F2.1).

**Solution sketch:** Deliberately a self-check scaffold, not a model answer, because this is your own case. It is a checklist for your filled table and contains no content for your case.
1. Every row has an answer in "Does my work have this limitation?", even if it is "no".
2. Each circled row has a metric with a unit and either a current value or a named place to find it (a dashboard, a config, a contract SLA, a log).
3. The figure of merit is one from Day 01's list (sensitivity per √Hz, fractional frequency stability, secure key rate at a distance, problem size or scaling), or a named physical quantity, not "better" or "faster".
4. The TRL cell names a pair and gives an evidence sentence with a source and date. It is not the technology's best component level (F2.1 rule 2).
5. "Who would pay?" names a budget holder or a customer, not "the industry".
6. For the security row you have written $x$ and $y$ as numbers (or named where to find them), not a guess at $z$, and you have said which technology fits the path the traffic takes, with your reason.
7. For any optimisation row you have written the baseline a vendor's claim would be compared with.
8. You can map at least one risk per circled row onto a barrier (F2.3) and say which barrier gates it.
9. Nothing in it is copied from this day's Harrowmere models: every cell comes from your own work.
If items 2-4 fail for every row, choose a different background angle before Week 7, rather than forcing a weak case.

### Exercise 10.5 (writing) (stretch)

*Inventory row W7 Explore, on the running case.* Harrowmere's board asks: "Which quantum technology will we meet first, and how big is the market behind it?" Write 180-200 words ranking clocks, magnetometers, gravimeters, QKD, simulation and computing by maturity *for Harrowmere's uses*, using the lecture's TRLs with line numbers. Where a market figure belongs, write a bracketed slot for the McKinsey 2026 figure and its card fields, not a number.

**Hint:** Rank by evidence, not by press coverage (F2.1). Use L41-L54 for sensing, L70 for communication, L74 for simulation, L99 and L108 for computing. Give the market slot as "[McKinsey QTM, Apr 2026: figure, kind, year, segment]".

**Model paragraph:** Harrowmere (fictional) will meet quantum *sensing* first, because that is where the lecture finds products in routine use. Single optically pumped magnetometers and SQUIDs are at TRL 9 (L51, L53), and compact atomic clocks are sold for timing (L41). A holdover clock's oscillator is a catalogue product (component TRL 9), but a holdover system in our protection scheme is about TRL 6 until trialled through an outage (judgement). Portable atom gravimeters come next for survey work, with the system TRL for our embankment still to be shown. Quantum communication is "still in the early stages" at TRL below 7 (L70); for our dark-fibre links it competes with post-quantum cryptography, which needs no new hardware. Quantum simulation is at systems TRL 1-2 (L74). Quantum computing still lacks "clear evidence" of advantage on any industrially relevant problem (L99), so neither belongs in a five-year plan. Market context: [McKinsey QTM, Apr 2026: figure, kind, year, segment for computing] against [the same fields for sensing]. These are consultancy projections, and the larger investment in computing does not mean it is nearer to our use. Caveat: the TRLs come from a 2023 lecture and are guidelines, not measurements (L24).

**What a weak answer misses:** It ranks computing first because it gets the most coverage or investment. It invents or half-remembers a market figure instead of leaving a slot to fill at source. It gives TRLs without line numbers or without the pair. It forgets that QKD's competitor is a software migration (PQC). It treats a large market as evidence of maturity.

## Capstone (no notes)

**Rules.** The same as Day 05: clear desk, plain calculator, the constants box below is the only reference, items in order, about 5 minutes each, and no `<details>` block opened until all ten items and Exercise 10.16 are done. Every number here is new: none of these values appears in Days 01-09 or the companions with the same question.

**Scoring.** Items 10.6-10.15 score 1 point each: 1 for every part right (within about 5%) with units and the move named; ½ for a right method with one slip or one part missing; 0 for a wrong law or a missing final unit. **Pass: 7/10.** Exercise 10.16 uses Day 05's F1 rubric (six parts, 0-2 each), with two upgrades: part 4 needs a range and a break-even value, and part 5 needs a TRL with its evidence sentence and the gate barrier. **Pass: 8/12, with at least 1 point in parts 1 and 4.** Score your Exercise 10.3 fact sheet 0-2 on each of the six blocks of M14.3 (2 = complete, numbers labelled; 1 = present but vague or unlabelled; 0 = missing). **Pass: 8/12.**

**Constants.** $h = 6.626\times10^{-34}$ J s; $e = 1.602\times10^{-19}$ C; $c = 3.00\times10^{8}$ m/s; $g = 9.81\ \text{m/s}^2$; $\Phi_0 = h/2e = 2.07\times10^{-15}$ Wb; ⁸⁷Rb $\gamma = 7$ Hz/nT; 1 µGal $= 10^{-8}$ m/s².

### Exercise 10.6 (quantitative)

M1. (a) Write 250 pT in fT. (b) Write 18 µGal in m/s² and as a fraction of $g$. (c) A holdover clock runs at a constant fractional offset of $3\times10^{-11}$ for 6 h. What time error builds up, and what ranging error is that at the speed of light?

<details>
<summary>Hint</summary>

**Hint:** Prefixes as powers of ten; $\delta t = y\,t$; $\delta x = c\,\delta t$; 6 h $= 21{,}600$ s.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $250\times10^{-12}$ T; $18\times10^{-8}$ m/s²; $y = 3\times10^{-11}$, $t = 21{,}600$ s.
- *Name move:* M1.
- *Algebra:* (a) $250\times10^{-12}/10^{-15} = 2.5\times10^{5}$ fT. (b) $1.8\times10^{-7}$ m/s²; $/9.81 = 1.8\times10^{-8}$ of $g$. (c) $\delta t = 3\times10^{-11}\times21{,}600 = 6.5\times10^{-7}$ s $= 0.65$ µs; $\delta x = 3.00\times10^{8}\times6.48\times10^{-7} = 194$ m.
- *Check:* 1 µGal ≈ $10^{-9}g$, so 18 µGal ≈ $1.8\times10^{-8}g$. A microsecond of light travel is 300 m, so 0.65 µs ≈ 195 m.
- *Answer:* $2.5\times10^{5}$ fT; $1.8\times10^{-7}$ m/s² ≈ $1.8\times10^{-8}g$; about 0.65 µs and about 194 m.

</details>

### Exercise 10.7 (quantitative)

M2. (a) A magnetometer has a white noise density of $45\ \text{fT}/\sqrt{\text{Hz}}$. What is its noise in a 25 Hz detection bandwidth? (b) A clock's Allan deviation is $4\times10^{-13}$ at 1 s and falls with slope $-1/2$. What is it at 400 s? (c) What would a slope of 0 mean?

<details>
<summary>Hint</summary>

**Hint:** $\delta B = S\sqrt{\Delta f}$; white frequency noise averages as $1/\sqrt\tau$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $S = 45\ \text{fT}/\sqrt{\text{Hz}}$, $\Delta f = 25$ Hz; $\sigma(1\ \text{s}) = 4\times10^{-13}$, $\tau = 400$ s.
- *Name move:* M2.
- *Algebra:* (a) $45\times\sqrt{25} = 225$ fT. (b) $4\times10^{-13}/\sqrt{400} = 2\times10^{-14}$.
- *Check:* units $\text{fT}/\sqrt{\text{Hz}}\times\sqrt{\text{Hz}} = \text{fT}$; 400 times longer gives 20 times better, not 400.
- *Answer:* (a) 225 fT. (b) $2\times10^{-14}$. (c) A flicker floor: averaging longer stops helping.

</details>

### Exercise 10.8 (quantitative)

M3. (a) An atom sensor uses $N = 9\times10^{6}$ independent atoms per shot. What are the shot-noise and Heisenberg phase limits? (b) You move a sensor from 1.5 m to 0.5 m from a source. By what factor does the signal rise for a magnetic dipole ($1/r^3$) and for a current dipole ($1/r^2$)?

<details>
<summary>Hint</summary>

**Hint:** $1/\sqrt N$ and $1/N$; distance gain $(r_1/r_2)^n$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $N = 9\times10^{6}$; $r_1/r_2 = 3$; $n = 3$ and $n = 2$.
- *Name move:* M3.
- *Algebra:* (a) $1/\sqrt{9\times10^{6}} = 1/3000 = 3.3\times10^{-4}$ rad; $1/(9\times10^{6}) = 1.1\times10^{-7}$ rad. (b) $3^3 = 27$; $3^2 = 9$.
- *Check:* the Heisenberg limit is better by $\sqrt N = 3000$: $3.3\times10^{-4}/1.1\times10^{-7}\approx3000$.
- *Answer:* (a) $3.3\times10^{-4}$ rad and $1.1\times10^{-7}$ rad (the second needs entanglement). (b) 27× and 9×.

</details>

### Exercise 10.9 (quantitative)

M4 and M5. (a) An optical transition at 411 THz has a 0.5 Hz linewidth. What is its $Q$? (b) A Ramsey sequence has a free-evolution time of 0.25 s. What linewidth does it give? (c) What is the ⁸⁷Rb Larmor frequency in a 35 µT field? (d) What field change threads one flux quantum through a 0.25 mm² SQUID loop?

<details>
<summary>Hint</summary>

**Hint:** $Q = \nu/\Delta\nu$; $\Delta\nu\approx1/(2T)$; $f_L = \gamma B$; $\Delta B = \Phi_0/A$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $\nu = 4.11\times10^{14}$ Hz, $\Delta\nu = 0.5$ Hz; $T = 0.25$ s; $B = 35{,}000$ nT; $A = 2.5\times10^{-7}$ m².
- *Name move:* M4 (Q, Ramsey) and M5 (Larmor, flux quantum).
- *Algebra:* (a) $4.11\times10^{14}/0.5 = 8.2\times10^{14}$. (b) $1/(2\times0.25) = 2$ Hz. (c) $7\times35{,}000 = 2.45\times10^{5}$ Hz $= 245$ kHz. (d) $2.07\times10^{-15}/2.5\times10^{-7} = 8.3\times10^{-9}$ T $= 8.3$ nT.
- *Check:* an optical $Q$ near $10^{15}$ is about $10^{5}$ above a microwave clock's; Earth-scale fields give Larmor frequencies of hundreds of kHz.
- *Answer:* (a) $Q\approx8.2\times10^{14}$. (b) About 2 Hz. (c) About 245 kHz. (d) About 8.3 nT per flux quantum.

</details>

### Exercise 10.10 (quantitative)

M6 and M7. (a) A lithium atom interferometer uses counter-propagating Raman beams at 671 nm. Find $k_\text{eff}$. (b) With $T = 0.15$ s between pulses, find $\Phi = k_\text{eff}gT^2$ and the number of fringes $\Phi/2\pi$. (c) What would you get by mistake with the lecture's $\tau = 2T$ in the same formula? (d) A Mach-Zehnder has phase difference $2\pi/5$. What fraction of the light leaves the bright port, $\cos^2(\varphi/2)$?

<details>
<summary>Hint</summary>

**Hint:** $k_\text{eff}\approx2k = 4\pi/\lambda$. $T$ is the time between pulses (Day 04, erratum L105-110).

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $\lambda = 671$ nm, $T = 0.15$ s, $g = 9.81$ m/s², $\varphi = 2\pi/5$.
- *Name move:* M7 (with M6 for the intensity).
- *Algebra:* (a) $4\pi/6.71\times10^{-7} = 1.87\times10^{7}\ \text{m}^{-1}$. (b) $\Phi = 1.87\times10^{7}\times9.81\times0.0225 = 4.13\times10^{6}$ rad; $/2\pi = 6.6\times10^{5}$ fringes. (c) $(2T)^2$ gives 4× too much: $1.65\times10^{7}$ rad. (d) $\cos^2(\pi/5) = 0.655$.
- *Check:* the units of $k_\text{eff}gT^2$ are $\text{m}^{-1}\cdot\text{m/s}^2\cdot\text{s}^2$, dimensionless (radians).
- *Answer:* (a) $1.87\times10^{7}\ \text{m}^{-1}$. (b) $4.1\times10^{6}$ rad, about $6.6\times10^{5}$ fringes. (c) $1.65\times10^{7}$ rad, the factor-4 error. (d) About 65%.

</details>

### Exercise 10.11 (quantitative)

M8 and M9. (a) Data must stay confidential for 8 years and migration takes 6 years. A planning range puts a cryptographically relevant quantum computer 10 to 20 years away. Is the data exposed, and for which part of the range? (b) Eve intercepts and resends 30% of BB84 photons in random bases. What QBER does she cause? (c) If she intercepts all photons, what is the probability that comparing 12 sifted bits catches her?

<details>
<summary>Hint</summary>

**Hint:** Mosca: exposed if $x + y > z$. Full intercept-resend gives 25% QBER; detection with $n$ compared bits is $1-(3/4)^n$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $x = 8$, $y = 6$, $z\in[10, 20]$; fraction $f = 0.3$; $n = 12$.
- *Name move:* M8 (Mosca), M9 (intercept-resend).
- *Algebra:* (a) $x + y = 14$: exposed if $z < 14$, which covers the lower part of the range (10-14 years). (b) $0.3\times0.25 = 0.075$. (c) $1 - 0.75^{12} = 1 - 0.032 = 0.968$.
- *Check:* QBER scales linearly with the intercepted fraction; detection rises towards 1 with $n$.
- *Answer:* (a) Exposed if the machine arrives within 14 years, so start the migration now. (b) 7.5%. (c) About 97%.

</details>

### Exercise 10.12 (quantitative)

M10. (a) A QKD link runs 65 km over fibre at 0.2 dB/km (typical telecom fibre). What is the loss in dB and the transmission? (b) A trusted node is put halfway. What is the transmission per hop, and what security assumption have you added? (c) An experiment reports a CHSH value of 2.6. Does it violate the classical bound, and what fraction of the quantum maximum is it?

<details>
<summary>Hint</summary>

**Hint:** $T = 10^{-\text{dB}/10}$. The classical bound is 2; the quantum maximum is $2\sqrt2$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $L = 65$ km, $\alpha = 0.2$ dB/km; two 32.5 km hops; $S = 2.6$.
- *Name move:* M10.
- *Algebra:* (a) $0.2\times65 = 13$ dB; $10^{-1.3} = 0.050$. (b) $6.5$ dB per hop, $10^{-0.65} = 0.22$. (c) $2.6 > 2$: yes. $2.6/2.83 = 0.92$.
- *Check:* every 10 dB is a factor of 10, so 13 dB is a little over $10^{-1}$ down: 0.05 is right.
- *Answer:* (a) 13 dB, about 5% transmission. (b) About 22% per hop, but the key exists in the clear at the node, which you must now trust. Repeaters would avoid that by entanglement swapping, not by amplifying (erratum W4 L152). (c) A violation, at about 92% of $2\sqrt2$.

</details>

### Exercise 10.13 (quantitative)

M11. Using the module convention of $8\cdot2^N$ bytes for $N$ spins (decimal prefixes): (a) how much memory does an exact state of 42 spins need? (b) What is the largest $N$ that fits in 512 GB?

<details>
<summary>Hint</summary>

**Hint:** $2^{10}\approx10^{3}$. For (b), solve $8\cdot2^N\le5.12\times10^{11}$ with $\log_2$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $N = 42$; budget $5.12\times10^{11}$ B.
- *Name move:* M11.
- *Algebra:* (a) $8\times2^{42} = 8\times4.40\times10^{12} = 3.5\times10^{13}$ B $= 35$ TB. (b) $\log_2(5.12\times10^{11}/8) = \log_2(6.4\times10^{10}) = 35.9$, so $N = 35$: $8\times2^{35} = 2.7\times10^{11}$ B (275 GB). $N = 36$ needs 550 GB.
- *Check:* each extra spin doubles the memory: 275 → 550 GB around the 512 GB line.
- *Answer:* (a) About 35 TB. (b) 35 spins.

</details>

### Exercise 10.14 (quantitative)

M12. Start in $|00\rangle$. Apply X to qubit 2, then H to qubit 1, then CNOT with qubit 1 as control. (a) Write the final state. (b) Give the measurement probabilities of the four outcomes. (c) In one line: does the circuit "compute both branches at once"?

<details>
<summary>Hint</summary>

**Hint:** Track the state after each gate. $H|0\rangle = (|0\rangle+|1\rangle)/\sqrt2$; CNOT flips qubit 2 when qubit 1 is $|1\rangle$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $|00\rangle\to|01\rangle\to(|01\rangle+|11\rangle)/\sqrt2$.
- *Name move:* M12.
- *Algebra:* CNOT maps $|11\rangle\to|10\rangle$, so the final state is $(|01\rangle+|10\rangle)/\sqrt2$. Probabilities $|1/\sqrt2|^2 = 0.5$ for 01 and 10, and 0 for 00 and 11.
- *Check:* the probabilities sum to 1; this is a Bell state, entangled, with the two bits always opposite.
- *Answer:* (a) $(|01\rangle+|10\rangle)/\sqrt2$. (b) 0.5, 0.5, 0, 0. (c) No: one measurement returns one outcome; any speed-up comes from interference (Day 08, erratum W1 L70).

</details>

### Exercise 10.15 (quantitative)

M13. (a) Run Shor's classical skeleton for $N = 51$, $a = 2$: find the order $r$, check both success conditions, and give the factors. (b) How many Grover iterations are optimal for $N = 4\times10^{8}$ items, against how many classical queries on average? (c) At a two-qubit fidelity of $F = 0.9975$, after how many gates does $F^g$ fall to 0.5?

<details>
<summary>Hint</summary>

**Hint:** List $2^x \bmod 51$ until 1. Need $r$ even and $a^{r/2}\not\equiv-1\ (=50)$; then $\gcd(a^{r/2}\pm1, N)$. Grover $\approx(\pi/4)\sqrt N$; $g_{1/2} = \ln0.5/\ln F$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate / Write state:* $N = 51$, $a = 2$, $\gcd(2, 51) = 1$; $N_\text{search} = 4\times10^{8}$; $F = 0.9975$.
- *Name move:* M13.
- *Algebra:* (a) Powers of 2 mod 51: 2, 4, 8, 16, 32, 13, 26, 1, so $r = 8$, even. $y = 2^4 = 16\not\equiv50$. $\gcd(15, 51) = 3$ and $\gcd(17, 51) = 17$. (b) $\sqrt{4\times10^{8}} = 2\times10^{4}$; $(\pi/4)\times2\times10^{4} = 15{,}708$; classical $N/2 = 2\times10^{8}$. (c) $\ln0.5/\ln0.9975 = 277$ (rule of thumb $0.693/0.0025 = 277$).
- *Check:* $3\times17 = 51$. $2^8 = 256 = 5\times51 + 1$.
- *Answer:* (a) $r = 8$, $y = 16$, factors 3 and 17. (b) About 15,700 iterations against $2\times10^{8}$ queries, a query ratio of about 13,000 (not a time ratio). (c) About 277 gates.

</details>

### Exercise 10.16 (writing)

*Inventory row W7 Consolidate, on the running case.* **Timed: 40 minutes, 300 words, no notes except your Exercise 10.3 fact sheet** (on the real task, too, the 300 words build on your own fact sheet). Write a 300-word F1 benefit/risk argument for the Harrowmere board: should Harrowmere invest in quantum simulation for the corrosion of its ductile-iron mains? It must quantify the benefit, give a probability with its range, state a benefit/risk ratio with its definition, give the break-even probability, map the main risk to a barrier, and end with a recommendation and its condition.

<details>
<summary>Hint</summary>

**Hint:** F1 order, about 60 / 30 / 20 / 80 / 60 / 50 words. Part 1: £40M a year, 2,400 km, the $8\cdot2^N$ wall. Part 4: the 10.1 numbers with their range. Part 5: TRL for the pair, logical versus physical qubits, gate barrier. Part 6: the verdict with the weakest assumption and its flip value. Label fictional, hypothetical and judgement figures.

</details>

<details>
<summary>Model paragraph and weak-answer note</summary>

**Model paragraph:** Harrowmere Water & Power spends £40 million a year replacing corroded ductile-iron mains across its 2,400 km network, about £16,700 per km (fictional). Its classical tools, approximate electronic-structure calculations plus laboratory immersion tests, are least reliable for strongly interacting electrons in iron oxides, and an exact classical model of $N$ such electrons needs $8\cdot2^N$ bytes, about 9 PB at $N = 50$. A quantum simulator represents those electrons with qubits, so its memory grows with $N$, not $2^N$. The figure of merit is the accuracy of predicted corrosion and inhibitor-binding energies at model sizes classical exact methods cannot reach. That advantage has not yet been shown on any industrially relevant problem (Week 7 L99). On hypothetical figures, success would cut replacement spend by 5% (range 2-10%), £2 million a year or £20 million over ten years. A three-year consortium place costs £0.5 million, and I put the chance that the quantum route delivers within ten years at 2% (range 0.5-5%). The expected benefit is £0.4 million, so the expected net value is −£0.1 million (range −£0.4 to +£0.5 million). The benefit/risk ratio, expected benefit over cost, is 0.8, and break-even needs a 2.5% chance; a £3 million in-house programme would need 15%. Quantum simulation sits at systems TRL 1-2 (L74); for this pair I judge TRL 2. A useful model may need about 100 logical qubits, roughly 88,000 physical ones (judgement); the thousands reported (L88) are annealer qubits, not comparable with gate-model counts (Day 09). The gate is barrier 2, proof of relevance. Recommendation: do not buy. Watch the field, and join the consortium only if the fee is £0.4 million or less, with a stage gate on one inhibitor-binding energy benchmarked against laboratory data. The caveat: the 2% probability is my weakest assumption and moves the answer most.

**What a weak answer misses:** It gives one benefit number with no probability, so it has no risk in it. It reports a ratio without saying what it divides by what. It omits the break-even probability, so the board cannot substitute its own belief. It cites physical qubit counts as if they were logical. It scores the system at the TRL of the qubits. It recommends "invest" or "ignore" with no condition. It does not label fictional, hypothetical and judgement figures.

</details>

## Anti-patterns / Common mistakes

- **"TRL 9: you can buy one."** How you'd notice: your only evidence is a price list or a press release. Instead: TRL 9 means proven in routine operations; the L24 system was sold and still sits at 6-7.
- **Scoring the system at its best component.** How you'd notice: your TRL is the same as the laser's or the qubit chip's. Instead: name the pair and score the system; never above its weakest essential component (judgement, from L24, L74, L137).
- **One TRL for a whole technology.** How you'd notice: "OPMs are TRL 9" with no application. Instead: a range, with the pair attached to each end (L51, L56).
- **A ratio with no probability.** How you'd notice: your "benefit/risk ratio" is best-case saving over cost. Instead: $R = pB/C$, defined in the sentence, with a range and $p^*$.
- **A point estimate dressed as precision.** How you'd notice: "£1.37M net benefit" from a made-up probability. Instead: two significant figures, a range, and the weakest assumption with its flip value.
- **A weak or mismatched baseline.** How you'd notice: the quantum figure is a lab record and the classical one a field product, or the vendor's percentage is against an unoptimised baseline. Instead: like for like (F3), and convert before comparing.
- **Inventing or blending market figures.** How you'd notice: you cannot name the report, year or kind of each number, or you added two reports together. Instead: one dated source, the extraction card, "projection" in the sentence.
- **Mistaking a big market for maturity or for your benefit.** How you'd notice: "the market is huge, so we should invest". Instead: market size says who else is investing; your EV depends on your $p$, $B$ and $C$.
- **Listing risks without barriers.** How you'd notice: a bullet list of worries with no order. Instead: map each to barriers 1-5 and name the gate.
- **Letting this day's Harrowmere models stand in for your case.** How you'd notice: your portfolio sentence sounds like a Harrowmere paragraph, or reads smoothly with no number from your own work. Instead: start from Exercise 10.4's table and the numbers in it.

## Done when

Item 9 is the capstone; there is no separate self-test. Items 1-8 are checked inside it (Exercise 10.16 and the fact-sheet score test 1-6 and 8; item 7 is checked only if you actually filled the extraction card for the source you cited in block 6, so fill it there rather than just naming the fields): as you mark the capstone, tick each of 1-8 you showed without notes. Done when item 9 passes and at most two of 1-8 are unticked.

1. Write Table 7.1's definitions for TRL 4 to 7 word for word, and say what separates 4 from 5 and 5 from 6.
2. State the three interpretation rules (sale ≠ TRL 9; component > system; ranges are honest) with one lecture line each.
3. State the advantage test's three clauses (L88) and the lecture's verdict for sensing and for computing (L88, L99).
4. List the five barrier categories in the lecture's order, and place four example risks correctly.
5. Given $p$, $B$ and $C$ with ranges, compute EV, its range, $p^*$ and $R$ in under five minutes, and name the weakest assumption.
6. Write the benefit/risk sentence of M14.2 with the ratio defined.
7. Fill the seven fields of a market-figure extraction card and say why market reports sit at the bottom of F3.
8. Draw the six blocks of a fact sheet with the advantage table in block 2.
9. Capstone: at least 7/10 on Exercises 10.6-10.15, at least 8/12 on Exercise 10.16 (with at least 1 point in parts 1 and 4), and at least 8/12 on your Exercise 10.3 fact sheet. Every capstone item you lose goes onto the +7 day review list (README).

## Companion pointer and confusion log

Open `content/companions/week07_companion.md`. Read §3 (the framework decoder) beside the lecture, then §4A (full TRL checklist), §4B (why ranges are honest), §4C ("several thousand qubits") and §4D (market numbers). Do the cold attempt in §6 if you have not already. Log every term you had to look up twice (relevant versus operational environment, use case, enabling technology, logical qubit) with its lecture line.

| Term or line | What confused me | Resolution |
|---|---|---|
| | | |
| | | |

## What next

The sprint ends here. From now on you write on your own case; STRATEGY §8 lists ways to use AI as tutor, examiner and critic.

- **Wed 25 to Sun 29 Nov:** write your own Weeks 1-3 Consolidate pieces, about 45 minutes each, in the F1 shape (README timetable).
- **Course Weeks 4-7:** about 3 h a week. Run the Five-Pass Lecture Protocol (STRATEGY §4) with that week's companion, do the quiz, write the Apply post, then write your own Consolidate piece in the same course week (README, "After Day 10").
- **Week 7 itself:** your Exercise 10.4 table is the starting point for your own fact sheet and 300 words. Re-read M14.2 and M14.3 then, not now.
- **Spaced review:** the 20-minute GLOSSARY retrieval sets at +7 and +21 days (README), with today's lost capstone items added to the first.

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 09 (speed-ups, noise, error correction: M13).**
1. How many Grover iterations are optimal for $N = 2.5\times10^{7}$?
2. At a two-qubit fidelity of 0.996, after about how many gates is the success probability 0.5?
3. State the threshold theorem correctly in one sentence.
4. Which row of the speed-up taxonomy does quantum annealing belong in?

**From Day 07 (simulation: M11).**
5. How much memory does an exact state of 33 spins need at $8\cdot2^N$ bytes?
6. In one line each: analogue versus digital simulation.
7. In the Bose-Hubbard story, which phase wins when $U \gg J$, and what disappears from the time-of-flight picture?

**From Day 03 (clocks and magnetometers: M4, M5).**
8. A clock holds a fractional offset of $10^{-14}$ for one day. What time error is that, and what distance error at $c$?
9. What is the ⁸⁷Rb Larmor frequency in Earth's 50 µT field?
10. What is the flux quantum, in Wb?

*Answers.* 1. $(\pi/4)\times\sqrt{2.5\times10^{7}} = (\pi/4)\times5000\approx3927$. 2. $\ln0.5/\ln0.996\approx173$. 3. If every physical operation's error rate is below a threshold, encoding each logical qubit in more physical qubits makes the logical error rate as small as you like (the lecture's L184 wording is wrong). 4. Heuristic or unproven. 5. $8\times2^{33} = 6.9\times10^{10}$ B, about 69 GB. 6. Analogue: a controllable system whose own Hamiltonian mimics the target model; digital: the evolution is built from gates (Trotter steps) on a universal machine. 7. The Mott insulator (a fixed number of atoms per site); the interference peaks vanish because the phase is random. 8. $10^{-14}\times86{,}400 = 8.6\times10^{-10}$ s $= 0.86$ ns; $\times c = 0.26$ m. 9. $7\times50{,}000 = 3.5\times10^{5}$ Hz $= 350$ kHz. 10. $h/2e = 2.07\times10^{-15}$ Wb.

## Read next

- **UK National Quantum Strategy (DSIT 2023):** <https://www.gov.uk/government/publications/national-quantum-strategy>. Read the summary and the missions. Look for which technologies the UK expects to deploy first and on what timescale, and compare that with your Exercise 10.5 ranking. Use the extraction card for any funding figure.
- **McKinsey, *Quantum Technology Monitor 2026* (April 2026):** <https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point>. Read the executive summary only. Fill one extraction card for computing and one for sensing, and note which figures are investment and which are projections.
- **NCSC white paper, *Quantum security technologies*:** <https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies>. Read it all. It is the UK view on QKD versus post-quantum cryptography, and it is the source to check the security row of your Exercise 10.4 table against.
