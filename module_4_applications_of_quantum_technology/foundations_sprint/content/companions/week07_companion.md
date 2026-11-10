# Week 07 Companion - Comparing different quantum technologies

**Built on:** [Day 10](../day10.md) (F2 maturity lens: TRL with evidence, the advantage test, the five barriers; M14 benefit/risk: ranges, expected value, the weakest assumption, fact-sheet anatomy) and [Day 01](../day01.md) (F1 gain argument; F3 credible numbers).
**Feeds:** Assessment 2 (Portfolio) through the Week 7 Apply fact sheet and the Week 7 Consolidate piece, and the Portfolio submission at the end of the week. Nothing here is aimed at Assessment 1, and nothing here is Portfolio text.

Line numbers `L..` refer to `week_7/week_7_lecture.md`. Read this alongside the lecture, not instead of it. This is a qualitative week: the lecture has no equations (inventory, "What kind of module this is"), so §3 decodes **frameworks** rather than symbols, §4 expands the **arguments the reading leaves implicit**, and §5 applies both to the fictional running case.

## 1. Read these first (Pass 0)

Before you read the lecture, know what the week asks you to do with it. Types only, no solutions. There is no quiz this week (inventory, "Quizzes").

1. **Explore (task, 200 words):** which quantum technology from Weeks 1-6 is likely to be widespread soonest; contrast all the types; name the largest markets. Type: F2 ranking with evidence, plus F3 for the market figures, which the lecture does not supply (see 4D).
2. **Apply (task, one A4 page):** a fact sheet on the quantum technology most relevant to your own background: its most relevant features, its advantage over conventional solutions (or the new opportunity), and how that advantage helps. Type: F1 compressed into fact-sheet anatomy (M14, Day 10), with an F2 maturity line. It feeds the Consolidate piece.
3. **Consolidate (portfolio, 300 words + the fact sheet):** how beneficial the technology could be in your background, quantified, with "a quantitative assessment of the benefit/risk ratio". Type: F1 verdict plus M14 (ranges, expected value, sensitivity to the weakest assumption), with risks mapped onto the five barriers (F2).
4. **End of week:** submit Assessment 2 (Portfolio, 2,100 words). Out of scope for this companion: the sprint does not draft Portfolio text, and your own case stays yours.

The quantitative side the week expects of you is small but easy to fake: "quantify the benefit/risk ratio" means ranges, a probability, an expected value and a named weakest assumption, not one confident number. Exercise C7.3 and the cold attempt drill exactly that.

## 2. What the lecture is doing, in one picture

Picture a ladder with nine rungs, and every technology from the last six weeks standing on it somewhere. The lecture first defines the rungs (Table 7.1, NASA's TRL scale) and immediately warns that placing a technology on them is a judgement, not a measurement (L24). It then walks through clocks, magnetometers, communication, simulation and computing, and gives each a position or a range (L39-L100): clocks and magnetometers near the top, communication in the middle, simulation and computing near the bottom at the systems level. Along the way it introduces the test that separates hype from progress, quantum advantage on a *relevant* task (L88). The second half (L102-L137) lists what blocks the climb: five barrier categories, from making the device work at all to producing it at scale. The one idea that ties both halves together is that components climb faster than systems (L24, L74, L137).

## 3. Framework decoder

This table is the one to keep open. Each row is a framework the lecture uses: what you feed it, what it gives you, how it goes wrong, and where the week leans on it.

| Framework (lecture lines) | Inputs | Outputs | Failure mode | Where the week uses it |
|---|---|---|---|---|
| NASA TRL 1-9 (Table 7.1, L11-L22) | a specific technology for a specific application; the most demanding environment it has been demonstrated in; whether it is a component or a whole system | one level, or an honest range | scoring a system at its best component's level; treating a sale as TRL 9 | every technology in §7.1; Apply fact sheet maturity line; Consolidate risk |
| TRL interpretation rules (L24, L56, L74, L137) | the claimed level and the evidence behind it | a corrected level with its evidence, read "as a guideline rather than factual quantitative information" (L24) | quoting a lecture TRL as a measured fact | the Swiss bank QKD system (L24): "TRL 9" by sale, "TRL 6 or 7" by use |
| Maturity spectrum (L108) | the TRL range of each technology | an ordering, from "still low-TRL quantum computing" to clocks and magnetometers where "commercial devices are sold at a profit" | ordering by hype or press coverage instead of by evidence | Explore ("widespread sooner"); comparing technologies |
| Quantum-advantage test (L88) | a task; why it is relevant; the best known conventional method and the effort it needs | "advantage shown", "shown in a niche science problem only", or "not yet shown" | a weak classical baseline; a task nobody needs; a lab record compared with a fielded product (STRATEGY mistake 2) | clocks and sensors pass "by large margins"; computing does not yet (L88, L99) |
| Quantum computing, three messages (L98-L100) | the state of quantum computing | (1) large investment has made processors that outperform conventional computing "in niche science problems"; (2) "clear evidence ... in an industrially relevant problem is still missing"; (3) many platforms, no clear "winner" | reading message 1 as "quantum computers beat classical ones" | the computing TRL; any claim that a use case is ready now |
| Why qubit counts matter (L90-L92) and physical ≠ logical (L94) | a quoted qubit number | three reasons the number is significant: classical emulation cost grows exponentially (L90); qubit counts have grown (L91); error-correction overhead is falling (L92). Then the caveat: quoted counts are **physical**; **logical** qubits are "substantially smaller" (L94) | comparing physical counts across platforms or machine types (see 4C) | the "several thousand qubits" claim (L88) |
| Barrier 1: Technological developments (L106-L108) | the application's conditions (temperature, geometry, infrastructure) and the device's current performance | the adaptation and performance work still needed; the shift from lab performance to "robustness, and reduced size, weight, power and cost (SWAP-C)" as TRL rises | treating feasibility "in principle" as readiness | biomedical magnetometry must suit the body; cryogenic quantum computers suit a cloud service, not an office |
| Barrier 2: Proof of relevance and practicality (L110-L112) | technology push versus market or application pull; a demonstrated advantage "in a relevant context" | a credible path to near-term viability, cast into "a robust technology development and deployment road map" | push without pull: a capability looking for a problem | quantum computing's race for logical qubits and new algorithms; IBM's 100×100 challenge (L112, ref [7]) |
| Barrier 3: Use cases (L114-L123) | a contained-scope but relevant slice of an application sector | four things: (1) demonstrate the main advantages; (2) early iterative feedback between development and need; (3) first measures of performance and limits in context; (4) groundwork for standardisation and calibration, so platforms, or quantum and incumbent, can be compared | a use case too large to finish or too small to matter | OPM-based MEG (L123, refs [8], [9]): better signal-to-noise and source localisation, and participants can move |
| Barrier 4: Validation of usability (L125-L133) | a technology already shown to have an advantage in use cases | robustness in routine operation and wider scope, plus three non-technological items: regulatory and legal; standardisation, calibration and benchmarking; documentation and user interface | stopping at the impressive demo | multi-patient schizophrenia studies with OPM-MEG; a quantum simulation subscription service (L133, ref [10]) |
| Barrier 5: Scalable and robust production (L135-L137) | the gap between component TRL and system TRL | enabling technologies; a modular design (swap components without redesigning the system; lower investment risk in high-TRL components; warranties that de-risk the system level); robust supply chains | a one-off system that cannot be rebuilt, repaired or bought twice | why the field funds lasers, vacuum, cryogenics and photonics as products in their own right |

**Table 7.1, verbatim (L14-L22).** Learn these word for word; the wording carries the distinctions.

| TRL | Definition (lecture) | The word that moves you up |
|---|---|---|
| 1 | Basic principles observed and reported. | observed |
| 2 | Technology concept and/or application formulated. | formulated |
| 3 | Analytical and experimental critical function and/or characteristic proof-of-concept. | proof-of-concept |
| 4 | Component and/or breadboard validation in laboratory environment. | laboratory |
| 5 | Component and/or breadboard validation in relevant environment. | relevant environment |
| 6 | System/subsystem model or prototype demonstration in a relevant environment. | system prototype |
| 7 | System prototype demonstration in an operational environment. | operational environment |
| 8 | Actual system completed and qualified through test and demonstration. | qualified |
| 9 | Actual system proven through successful mission operations. | proven in operations |

Two pairs carry the most confusion. Levels 4 and 5 differ only in the environment (laboratory versus relevant). Levels 5 and 6 differ in what is tested (component or breadboard versus system or subsystem). In NASA's usage a *relevant* environment reproduces the key stresses of the real one, while an *operational* environment is the real one (ref [1], Tzinis 2021, www.nasa.gov/directorates/heo/scan/engineering/technology/technology_readiness_level).

**The five barriers, in the lecture's order (F2).** Technological developments → proof of relevance and practicality → use cases → validation of usability → scalable and robust production. Roughly, each one dominates a band of the ladder, from the bottom to the top (judgement: the lecture lists them as types of challenge, not as stages, and several run in parallel).

## 4. Arguments the reading leaves implicit

### 4A. How to assign a TRL with evidence (Table 7.1, L24)

The lecture gives levels but never the procedure, and its own example (L24) shows two people reaching TRL 9 and TRL 6-7 for the same system. Use this checklist, in order, and write the evidence next to each answer.

1. **Name the pair.** Technology *for* application: "an OPM array for whole-head MEG", not "OPMs". Different pairs have different TRLs (4B).
2. **Component or system?** If only components exist, the ceiling is TRL 5. A system or subsystem prototype is needed for 6 and above.
3. **Where has the most complete version been shown?** On paper (2), as an analytical or experimental proof-of-concept (3), on a lab bench (4), in a relevant environment (5 for components, 6 for a system), in the real operational environment (7).
4. **Has the actual system been completed and qualified by test and demonstration?** If yes, 8.
5. **Is it proven in mission operations, meaning routine use that meets the user's requirements?** Only then 9. A sale is not enough: the L24 system was sold but "is not routinely used because it doesn't fulfil all the requirements of the market" (too slow, no guaranteed security advantage), so it sits at the field-test level, 6 or 7.
6. **Check the components.** Their TRL is normally higher than the system's (L24, L74, L137). If you have scored the system above its weakest essential component, you have made an error.
7. **Report a range when the evidence conflicts**, give the source for each end, and say which end you would act on.

The habit: a TRL without its evidence sentence is an opinion. Write "TRL 6: system prototype demonstrated at [where], [date], [source]".

### 4B. Why the wide ranges are honest (L51, L52, L54, L56)

OPMs appear at TRL 9 *and* TRL 2-3 in the same paragraph (L51). That is not a contradiction. Three different pairs are being scored: single atomic magnetometers in geophysics, medicine and navigation (TRL 9); "commercial prototypes ... on the basis of assemblies of individual commercial sensors" (TRL 8); and "fully scalable" multi-sensor imaging arrays (TRL 2-3, "with a higher TRL at the constituent component level"). NV magnetometers at TRL 4-7 (L52) and quantum dots at TRL 2-5 (L54) are ranges for the opposite reason: one name covers many implementations at very different stages. L56 says so: the levels "can vary based on the specific implementation, performance criteria and targeted application". A single number would hide which pair you mean. When you quote a range, attach the pair to each end.

The same reasoning resolves a puzzle the lecture leaves open. It says "specific quantum simulators are more advanced than today's quantum computers" (L88), yet it puts simulation at systems TRL 1-2 (L74). The TRL here scores readiness for practical industrial or commercial use; a simulator can be scientifically powerful and still be "scientific tools with applicability in the academic context" (L74).

### 4C. "Several thousand qubits" (L88): annealing versus the gate model

L88 reports a company that has "built quantum computers with several thousand qubits" (D-Wave Systems) right after the paragraph on quantum advantage. Three caveats the lecture does not spell out:

1. **Different machine.** D-Wave builds quantum **annealers**: special-purpose machines that relax a programmable network of coupled qubits towards a low-energy state of an optimisation or spin-model problem. They do not run arbitrary gate sequences, so they are not universal computers in the L86 sense, and their speed-up is heuristic, not proven (M13, Day 09). The cited result (ref [6], King et al. 2023, "Quantum critical dynamics in a 5,000-qubit programmable spin glass") is, as L88 itself concedes, closer to quantum simulation.
2. **Physical, not logical.** Even on gate-model machines the quoted counts are physical qubits (L94). As an illustration, at an error-correction overhead of 100 to 1,000 physical qubits per logical qubit (judgement; Day 09, M13), 1,000 physical qubits give between 1 and 10 logical qubits.
3. **Not comparable across types.** An annealer's qubit count and a gate-model processor's count measure different resources. Comparing them is F3's "both sides measured the same way" rule broken.

Why the count still matters (L90): a classical emulation stores $2^N$ complex amplitudes. At 8 bytes each (the spec's convention, $8\cdot2^N$ bytes, M11, Day 07) that is $8\cdot2^{30}\approx8.6\times10^{9}$ bytes (8.6 GB) for 30 qubits and $8\cdot2^{50}\approx9.0\times10^{15}$ bytes (9.0 PB) for 50. That is what "tens of qubits stops being feasible" means. Note that this argument applies to faithful emulation of a general state, not to every problem an annealer is given.

### 4D. Missing numbers: markets and investment (L98, Explore)

L98 speaks of "unprecedented large investments" and the Explore task asks for the "largest markets", but the lecture gives no figure for either. Get them from the spec's market source and treat them with F3:

- **Source:** McKinsey, *Quantum Technology Monitor 2026* (April 2026), executive summary: https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point
- **What to copy, with its label:** the year of the figure; whether it is *investment* (start-up funding, public funding) or *projected market size* (revenue by a future year); which segment it covers (computing, communication, sensing); and the report's own range if it gives one. Cite as "McKinsey Quantum Technology Monitor, April 2026".
- **Quote cautiously:** a consultancy projection is at the bottom of F3's source hierarchy, below peer-reviewed work, reviews and datasheets. It is a forecast, not a measurement, and the report's subtitle ("a commercial tipping point") is a thesis. Give it as a range, say it is a projection, and never add segments from different reports together.
- **For UK public investment,** use the UK National Quantum Strategy (DSIT 2023), summary and missions: https://www.gov.uk/government/publications/national-quantum-strategy. It sets out a ten-year public programme (£2.5 billion over 2024-2034; confirm the figure on the page before quoting it).

I have not reproduced the McKinsey figures here: copy them yourself from the executive summary, with the date, so the number in your piece is one you have read at source.

### 4E. Terms the lecture uses without defining

| Term (line) | Read it as | Why it matters this week |
|---|---|---|
| CPT, coherent population trapping (L41) | two laser frequencies whose difference equals the atom's microwave (hyperfine) splitting pump the atoms into a "dark" superposition that stops absorbing; the transmitted light shows a narrow resonance, so no microwave cavity is needed | why chip-scale clocks can be tiny (SWaP) but drift (warm vapour cell) |
| Doppler broadening (L43) | atoms in a warm vapour move randomly; each sees the laser shifted by its own velocity, so the line is smeared and the clock is less precise | why next-generation chip clocks need cold atoms, trapped ions or two-photon tricks |
| $100~\text{aT}/\sqrt{\text{Hz}}$ (L53) | attotesla, $10^{-18}$ T, per root hertz of bandwidth: 100 aT = 0.1 fT. A noise density: multiply by $\sqrt{\Delta f}$ for the noise in bandwidth $\Delta f$ (M2, Day 02) | a lower-TRL improvement on a TRL 9 technology: both can be true at once |
| SWaP / SWaP-C (L41, written "SWAP-C" in L108) | size, weight and power, plus cost | the industrial needs that replace raw performance as TRL rises (barrier 1) |
| LEO, low Earth orbit (L41) | orbits a few hundred to about 2,000 km up | radiation-hardened clocks synchronising small-satellite constellations |
| GNSS (L41) | global navigation satellite system (GPS, Galileo and others) | clocks in receivers; magnetometers for navigation where GNSS is denied (L51, ref [20]) |
| Quantum repeater (L64) | a relay that extends quantum links by entanglement swapping between stored pairs, not by amplifying (amplifying is forbidden by no-cloning; Week 4 erratum L152, Day 06 M10) | why communication stays below TRL 7 (L70): practical quantum memories are still missing |
| Logical qubit (L94) | an error-corrected qubit encoded in many physical ones | the honest unit for computing capacity (4C) |
| NG-CSAC (L43) | next-generation chip-scale atomic clock, targeting about 1,000× better long-term stability | an example of a low-TRL successor to a TRL 9 product |

**Wording slips to read past.** L123 says "optically pumped magnetometers (MEGs)": read (OPMs). L127 says "there are no directly technological aspects to consider now, such as": read "there are also non-technological aspects to consider". L43 "phontons" is "photons". L88 cites "[6] [6]" twice. L64 places entanglement distribution "exceeding 1,000 kilometres" under repeaters; the result it most likely refers to is the satellite link in L65, not a repeater chain (judgement), so do not use it as evidence of repeater maturity. L45's "within the next five years" was written in 2023 (the references were accessed in June 2023), so check what has happened since before you repeat it.

### 4F. TRL by technology, from the lecture's own lines

| Technology (as the lecture names it) | TRL in the lecture | Line | Evidence the lecture gives | Note |
|---|---|---|---|---|
| Chip-scale atomic clocks (CSACs), current generation | no number; commercially available since 2011 | L41 | sold and used in defence backpack equipment; radiation-hardened versions for space | TRL 9 by 4A step 5 for those uses (inferred); poor long-term stability limits other uses |
| Next-generation CSACs | no number; a mercury-ion chip clock "could reach the fully integrated prototype stage within the next five years" | L43-L45 | several platforms "at different levels of maturity" | a prototype target is around TRL 6 (judgement) |
| OPMs, single sensors | 9 | L51 | geophysical surveys, medical imaging, navigation | |
| OPM arrays from commercial sensors | 8 | L51 | commercial prototypes | |
| OPM arrays, fully scalable | 2-3 (components higher) | L51 | ongoing work | the component > system rule |
| NV centres in diamond | 4-7 | L52 | research and laboratory use; commercial devices "within a few years" | range = many implementations |
| SQUIDs | 9 (improvements at lower TRL) | L53 | research, medical diagnostics, industry | 100 aT/√Hz work is lower TRL |
| Quantum dots | 2-5 | L54 | experimental demonstrations | |
| Quantum communication (QKD and beyond) | below 7 | L70 | rates from kbit/s to above 1 Gbit/s (L62, distance and conditions not stated: an F3 gap) | the sold-but-not-routine system: 6 or 7 (L24) |
| Quantum simulation | 1-2 at systems level (components higher) | L74 | academic scientific tools | see 4B |
| Quantum computing | no number; "still low-TRL" | L86, L108 | advantage in an industrially relevant problem "still missing" (L99) | a cloud-access service is a product, but "useful industrial computation" is low TRL (judgement) |

## 5. Applications to the running case

These exercises use **Harrowmere Water & Power** (fictional), the running case from the shared fact sheet at the end of [STRATEGY](../../STRATEGY.md). Every company figure comes from that sheet and is fictional. Prices and probabilities that the sheet does not give are **hypothetical** and labelled so; they are the only things these exercises vary. No exercise uses a lecture case. Do them after the lecture, before the cold attempt in §6.

### Exercise C7.1 (writing)

Harrowmere (fictional) has three quantum-related candidates on its list: (a) a rubidium holdover clock in each of its 38 substations, to keep within 1 µs of UTC through an 8 h loss of satellite timing; (b) a portable atom gravimeter (absolute, 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation) for the 150-station survey of the Greystock reservoir embankment; (c) QKD on the dark fibre from the control centre to its four sites at 12, 38, 95 and 160 km (all fictional). Assign a system TRL to each candidate *for Harrowmere's use*, with the evidence sentence, and say what would move each up one level. 150-200 words.

**Hint:** Run 4A's checklist for each pair. Separate component from system. Rubidium frequency standards are long-established products (judgement), but "a holdover system in Harrowmere's protection scheme" is a different pair. For (c), apply the lecture's communication TRL (L70) and work out the fibre loss at 0.2 dB/km (typical telecom fibre; Day 06, M10) before choosing a level for the long links.

**Model paragraph:** For (a), rubidium oscillators are mature products, so the component is at TRL 9 (judgement), but Harrowmere is buying a holdover system wired into substation protection, and no substation has run an 8 h loss of satellite timing with one (fictional). That makes the system TRL 6 at best: a prototype in a relevant environment once it has been bench-tested against a simulated outage. One live substation trial through a deliberate 8 h outage would make it TRL 7. For (b), portable atom gravimeters are sold for field surveys (judgement; Abend et al., arXiv:2001.10976, applications section), but at 110 kg with vibration isolation on a reservoir embankment the pair "Greystock survey" has not been shown; I would call it TRL 7 for the instrument and TRL 6 for Harrowmere's survey procedure, rising to 7 after a repeat survey over a few stations. For (c), the lecture puts quantum communication below TRL 7 (L70). The 12 km and 38 km links lose 2.4 dB and 7.6 dB at 0.2 dB/km, which is workable; the 160 km link loses 32 dB, a transmission of about $6\times10^{-4}$, and would need a trusted node, a security assumption nobody has qualified for Harrowmere. So TRL 6 for the short links and lower for the long ones; a qualified trial on the 12 km link would move it up.

**What a weak answer misses:** It gives each candidate one number without the evidence sentence. It scores the clock system at TRL 9 because rubidium oscillators are TRL 9 (component ≠ system). It calls QKD TRL 9 because products are sold. It gives the four fibre links one TRL although their losses differ by about 30 dB. It does not say what evidence would move each level, which is what a board can act on.

### Exercise C7.2 (writing)

Take the atom-gravimeter candidate for the Greystock embankment survey: target signal about 5 µGal, 150 stations, against the installed spring meter (8 µGal/√Hz, drift 30 µGal/day, 14 kg) (all fictional). Map its risks onto the five barrier categories, in the lecture's order, and say which barrier gates the decision. Keep the comparison like-for-like: compare both instruments at the same per-station resolution. Take that resolution as 2.5 µGal, a signal-to-noise of 2 on the target (assumption). 150-200 words.

**Hint:** First compute two numbers: the averaging time per station for each meter to reach 2.5 µGal, $t = (S/R)^2$ (M2, Day 02), and how long the spring meter's drift takes to reach 2.5 µGal. Then use the order in §3: technology, relevance and practicality, use cases, validation of usability, production.

**Model paragraph:** Like for like at 2.5 µGal per station (assumption), the atom meter needs $(30/2.5)^2 = 144$ s per station, or 6 h for 150 stations; the spring meter needs about 10 s, but its 30 µGal/day drift (1.25 µGal/h) reaches 2.5 µGal in 2 h, so the crew must loop back to a base station every 2 h (all fictional). Barrier 1, technological developments: 110 kg and vibration isolation on an embankment is a SWaP-C problem the spring meter (14 kg) does not have. Barrier 2, proof of relevance and practicality: the atom meter is noisier (30 versus 8 µGal/√Hz); its only advantage is an absolute, drift-free reading, which matters only if Harrowmere repeats the survey and compares months. Barrier 3, use cases: one contained job, a repeat survey of a few stations over a known void, would show whether that advantage is real and give a first calibration. Barrier 4, validation of usability: a survey standard, a calibration routine against the spring meter, and crew training on a heavier instrument. Barrier 5, production: a single supplier and specialist vibration isolation; a modular set-up reduces the risk. The gate is barrier 2: without a repeat-survey need, the quieter, lighter spring meter wins.

**What a weak answer misses:** It compares noise densities without converting to time per station, or compares at different resolutions (not like for like). It ignores drift, which is the spring meter's real limitation. It claims the atom meter is "more sensitive" (it is noisier here). It puts weight and vibration under "relevance" instead of technology. It forgets the non-technological items of barrier 4 or does not name the gate.

### Exercise C7.3 (quantitative)

Harrowmere's 38 substation clocks must stay within 1 µs of UTC; the design case is an 8 h loss of satellite timing; the installed quartz holdover drifts at a fractional frequency offset of $1\times10^{-9}$; the candidate rubidium clock at $5\times10^{-12}$ costs 10× the quartz unit (all fictional). Hypothetical prices and probabilities: a quartz unit costs £2k; each substation suffers a design-case outage with probability 0.02 a year (range 0.01-0.04); each outage that breaches 1 µs costs £150k (protection and phasor data unusable, possible maloperation); the clocks last 10 years; no discounting. Assume a constant fractional offset, so time error = offset × elapsed time. (a) Find the time error of each clock after 8 h, and the time each takes to reach 1 µs. (b) Find the extra cost of fitting rubidium in all 38 substations. (c) Find the expected avoided loss over 10 years and the expected net value at $p = 0.02$, with its range. (d) Find the break-even outage probability, and the benefit/risk ratio, defined as expected avoided loss divided by extra cost. (e) The weakest assumption is the £150k per breach. At what cost per breach does the expected net value fall to zero at $p = 0.02$?

**Hint:** 8 h = 28,800 s. Time error $\Delta t = y\,t$, where $y$ is the fractional offset. A clock "breaches" if $\Delta t > 1$ µs within the outage. Expected avoided loss = sites × $p$ × cost per breach × years, if rubidium avoids every breach that quartz would cause. Work in £k.

**Solution sketch:**
1. *Restate.* Given $y_q = 10^{-9}$, $y_{Rb} = 5\times10^{-12}$, $t = 28{,}800$ s, limit 1 µs, 38 sites, quartz £2k and rubidium 10× (£20k), $p = 0.02$ (0.01-0.04), £150k per breach, 10 years. Want time errors, times to 1 µs, extra cost, expected values, break-even $p$, ratio, break-even breach cost.
2. *Write state.* $\Delta t = y\,t$; $t_{1\mu s} = 10^{-6}/y$. Extra cost $= 38\times(20 - 2)$. Benefit $B = 38\times p\times150\times10$. Net $= B - \text{extra cost}$.
3. *Name move.* M1 (fractional offset to time), M14 (EV, ranges, weakest assumption), F3 (like for like: both clocks judged on the same 8 h case with the same drift model).
4. *Algebra.*
   - (a) Quartz: $10^{-9}\times28{,}800 = 2.88\times10^{-5}$ s $= 28.8$ µs, a breach. Rubidium: $5\times10^{-12}\times28{,}800 = 1.44\times10^{-7}$ s $= 0.144$ µs, within limits. Time to 1 µs: quartz $10^{-6}/10^{-9} = 1000$ s (about 16.7 min); rubidium $10^{-6}/5\times10^{-12} = 2\times10^{5}$ s (about 55.6 h).
   - (b) $38\times18 = 684$.
   - (c) $B = 38\times0.02\times150\times10 = 1140$. Net $= 1140 - 684 = 456$. At $p = 0.01$: $570 - 684 = -114$. At $p = 0.04$: $2280 - 684 = 1596$.
   - (d) Break-even $p = 684/(38\times150\times10) = 684/57{,}000 = 0.012$. Ratio $= 1140/684 = 1.67$.
   - (e) $38\times0.02\times10\times c = 684 \Rightarrow c = 684/7.6 = 90$, i.e. £90k per breach.
5. *Check.* Units: s for times, £k for money. The two time errors differ by $10^{-9}/5\times10^{-12} = 200$, the ratio of the offsets, as they must under a linear drift model. Quartz breaches after 17 minutes, so every design-case outage is a breach; rubidium has 55 h of margin, about seven times the design case. The net value is positive at the central $p$ but negative at the bottom of the range, so the decision depends on $p$ and on the breach cost. A real jamming event would hit all substations at once: that changes the spread of outcomes, not the expected value.
6. *Answer.* After 8 h: quartz 28.8 µs (breach), rubidium 0.144 µs (pass); quartz breaches after about 17 min, rubidium after about 56 h. Extra cost £684k; expected avoided loss £1.14M over 10 years; net +£456k (range −£114k to +£1.6M); break-even outage probability 0.012 per substation-year; benefit/risk ratio about 1.7. The decision flips if a breach costs less than £90k.

The habit to keep: report the net value as a range, name the assumption that flips its sign, and state the value at which it flips.

### Exercise C7.4 (writing)

Using your results from C7.3 and your TRL for the clock from C7.1, write the 200-250-word benefit/risk paragraph Harrowmere's project lead would put in front of the board. It must quantify the benefit, give the probability and its range, state a benefit/risk ratio with its definition, map the main risk to a barrier, and end with a recommendation and its condition.

**Hint:** F1 order, compressed: classical limit (quartz after loss of satellite timing), mechanism in one sentence, figure of merit (time error after the 8 h design case), quantified gain, maturity (TRL) and gate barrier, verdict with the weakest assumption. Label the fact-sheet figures fictional and the prices and probabilities hypothetical.

**Model paragraph:** Harrowmere's 38 substation clocks must stay within 1 µs of UTC, and the design case is an 8 h loss of satellite timing (fictional). The installed quartz holdover, at a fractional offset of $10^{-9}$, breaches that limit after about 17 minutes and is 28.8 µs out after 8 h. A rubidium clock locks its oscillator to a hyperfine transition of rubidium atoms; at $5\times10^{-12}$ it is only 0.144 µs out after 8 h, with about 55 h of margin. On hypothetical figures (a £2k quartz unit, so £20k for rubidium; a 2% chance per substation per year of a design-case outage; £150k per breach; 10-year life), fitting all 38 sites costs £684k extra and avoids an expected £1.14M of losses: a net value of +£456k, with a range from −£114k to +£1.6M as the outage probability runs from 1% to 4%. The benefit/risk ratio, expected avoided loss over extra cost, is about 1.7, and the investment breaks even at an outage probability of 1.2% a year. The oscillators are mature, but the holdover system is at about TRL 6 for Harrowmere, so the gate is barrier 4, validation of usability: protection engineers must accept it. Recommendation: trial one substation through a deliberate 8 h outage, then roll out if a breach is judged to cost more than £90k, the value at which the case turns negative.

**What a weak answer misses:** It gives one value with no range, or a ratio with no definition. It quotes the 200× offset ratio as the benefit instead of turning it into breaches avoided and money. It omits the TRL and the gate barrier. It recommends without a condition. It forgets that quartz breaches within minutes, so the comparison is "every outage a breach" against "none". It does not label which figures are fictional and which are hypothetical.

## 6. Cold attempt

Attempt this on paper before opening the sketch. Same type as §5, a fresh decision.

### Exercise C7.5 (quantitative)

Harrowmere runs 220 pumps across 4 electricity tariff bands; its energy bill is £18 million a year, and its current classical optimiser already saves 6% (all fictional; read the £18 million as the bill *with* the optimiser running). A vendor (hypothetical) offers a three-year quantum-optimisation programme at £250k and claims its method "saves 8% of pump energy", measured against an unoptimised schedule. Hypothetical: the probability that the claim holds on Harrowmere's problem is 0.05 (range 0.02-0.10), and the board counts three years of the incremental saving if it does. (a) Give the system TRL for "quantum pump scheduling" and the barrier that gates it. (b) Put the vendor's claim on a like-for-like basis: what is the incremental saving a year against Harrowmere's current optimised bill? (c) Find the expected net value and its range. (d) Find the break-even probability, and recommend, with the condition under which you would revisit.

**Hint:** Unoptimised bill $= 18/0.94$. The vendor's bill would be 92% of that. The incremental saving is the difference from £18M. Then $\mathrm{EV} = p\,B - C$, with $B$ = three years of incremental saving. Use L88 and L98-L100 for (a).

**Do not open the sketch until you have a written attempt.**

**Solution sketch:**
1. *Restate.* Given a bill of £18M with a 6% saving already in it; vendor claim 8% against unoptimised; $C = £250$k; $p = 0.05$ (0.02-0.10); 3 years. Want a TRL and gate barrier, the like-for-like saving, EV and range, break-even $p$, a recommendation.
2. *Write state.* $U = 18/0.94$; vendor bill $= 0.92\,U$; incremental saving $s = 18 - 0.92\,U$; $B = 3s$; $\mathrm{EV} = pB - C$; $p^* = C/B$.
3. *Name move.* F3 (both sides of a ratio measured the same way), F2 (TRL, advantage test, barriers), M14 (EV, ranges).
4. *Algebra.*
   - (a) No quantum advantage has been shown on an industrially relevant problem (L99), and nothing on Harrowmere's problem: TRL 2-3 (concept formulated, at most a proof-of-concept). The gate is barrier 2, proof of relevance and practicality.
   - (b) $U = 18/0.94 = 19.15$ £M. Vendor bill $= 0.92\times19.15 = 17.62$ £M. $s = 18 - 17.62 = 0.383$ £M a year, about 2.1% of the current bill, not 8%.
   - (c) $B = 3\times383 = 1149$ £k. $\mathrm{EV} = 0.05\times1149 - 250 = 57.4 - 250 = -192.6$. At $p = 0.02$: $23.0 - 250 = -227.0$. At $p = 0.10$: $114.9 - 250 = -135.1$.
   - (d) $p^* = 250/1149 = 0.22$.
5. *Check.* The like-for-like saving is the gap between 8% and 6% of the unoptimised bill: $0.02\times19.15 = 0.383$ £M, which matches (b). The EV is negative across the whole range, because break-even (0.22) is more than double the top of the range (0.10).
6. *Answer.* (a) TRL 2-3, gated by barrier 2. (b) About £383k a year (2.1%), not the 8% headline. (c) EV −£193k (range −£227k to −£135k). (d) Break-even needs a 22% chance of success. Recommendation: decline. Revisit if a published benchmark shows a quantum method beating the best classical solver on a scheduling problem of Harrowmere's size, which would raise both $p$ and the TRL.

If you took the vendor's 8% at face value, reread F3's like-for-like rule: the 6% Harrowmere already saves is part of the vendor's 8%.

## 7. Confusion log prompts

Answer each in writing (two or three sentences) after your pass through the lecture. Log the answer in your confusion log with the date.

1. Without notes, write Table 7.1's definitions for TRL 4, 5, 6 and 7, then state in one sentence each what separates 4 from 5 and 5 from 6.
2. L51 gives OPMs both TRL 9 and TRL 2-3. Explain in your own words why both are right, and write the "pair" you would name for the technology in your own Apply fact sheet (the pair only, not the fact sheet).
3. A news item says "a quantum computer with 5,000 qubits". List the three questions you would ask before using that number in your Explore post (machine type, physical or logical, relevant task).
4. Name the five barrier categories in the lecture's order from memory, and for your own background say which one you expect to be the gate. Do not draft the Portfolio text; one line is enough.
5. (Optional) Which market figure will you quote in the Explore post, from which dated source, and is it investment or projected revenue?

## 8. Figures

There are no figures this week. The Week 7 lecture contains one table (Table 7.1, decoded in §3) and no figure files were supplied for `week_7/`.
