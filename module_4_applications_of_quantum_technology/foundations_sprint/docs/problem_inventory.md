# Module 4 Problem Inventory (Phase 0)

**Built:** 2026-11-10 from `week_*/week*_content.md`, `module_4_intro.md`, `module_4_resources.md` and all seven `week_K_lecture.md` files (read in full).
**Rule:** a move or framework appears in the sprint only if a row below cites it, and every row is covered by some day or companion. Move and framework IDs (M1-M14, F1-F3) are defined in the spec, `superpowers/specs/2026-11-10-module4-foundations-design.md`.

## What kind of module this is

There are no numbered maths problems in any week. The weekly work is short evidence-backed writing plus 4-question multiple-choice quizzes. The only equations live in the lectures (Week 1: 0, Week 2: about 6, Week 3: about 12, Week 4: 3, Week 5: 2, Week 6: about 10, Week 7: 0). So the "problems" this sprint trains for are:

1. writing a quantified quantum-vs-classical gain argument (every Apply and Consolidate row), and
2. following each lecture's numbers and derivations well enough to reuse them correctly (the quantitative moves).

Assessment 1 (Problem Set) has no brief in the exports. The learner will bring it to a separate session, so it is listed but not mined.

## Writing tasks and activities

| Week | Source section | Item | Type | Moves / frameworks needed | Feeds assessment |
|---|---|---|---|---|---|
| 1 | Explore (Prepare) | 200-word summary of a QT benefit in an area of your interest, citing 2+ key publications | task (writing) | F1, F3, M1 | no |
| 1 | References page | Intro post: background, motivation, which of the 4 QT types interests you | task (forum) | none (orientation) | no |
| 1 | Apply | Pick one QT type + an application area; 200-300 words on why it matters | task (writing) | F1, F3 | no |
| 1 | Consolidate | 1-2 quantum advantages vs a classical limitation, 300 words, quantified (speed-up, cost, sensitivity, scaling) | portfolio | F1, F3, M1, M3, M13 | Assessment 2 |
| 1 | Consolidate (optional) | Circuit simulator: insert gates, read the histogram | interactive | M12 | no |
| 2 | Apply | Pick a clock or magnetometer + application; 200-300 words on why the quantum approach matters | task (writing) | F1, M2, M4, M5 | no |
| 2 | Consolidate | 1-2 advantages vs classical limitation, 300 words; sensitivity, bandwidth, dynamic range, practicality | portfolio | F1, F3, M1, M2, M3, M4, M5 | Assessment 2 |
| 2 | Consolidate | Reflection notes (keep a notes document) | task (notes) | none | indirect |
| 3 | Apply (+ live session 2) | Pick an application of atom interferometry; 200-300 words | task (writing) | F1, M6, M7 | no |
| 3 | Consolidate | Matter-wave interferometry gain, 300 words; sensitivity, reduced noise, long-term accuracy, practical aspects | portfolio | F1, F3, M2, M3, M6, M7 | Assessment 2 |
| 3 | End of week | Submit Assessment 1 (Problem Set) | assessment | brief not exported; out of scope this session | Assessment 1 |
| 4 | Apply | Pick an application of quantum communication; 200-300 words | task (writing) | F1, M8, M9 | no |
| 4 | Consolidate | How QKD gives more security than classical, gains and downsides, 300 words; bit rates, required fidelities, practicality | portfolio | F1, F3, M8, M9, M10 | Assessment 2 |
| 4 | Consolidate (optional) | QuVis BB84 simulation: controls, eavesdrop button, challenges page | interactive | M9 | no |
| 5 | Apply | Pick a type of quantum simulation; 200-300 words on why it matters and what applications follow | task (writing) | F1, M11 | no |
| 5 | Consolidate | 1-2 advantages of quantum over classical numerical simulation, 300 words; speed, newly possible simulations, practical aspects | portfolio | F1, F3, M11, M13 | Assessment 2 |
| 6 | Explore | 200-word summary of the limits of conventional computing; where high-end computing is used | task (writing) | M11, M13, F3 | no |
| 6 | Apply | Pick an aspect of quantum computing (algorithm/tool or hardware); 200-300 words on how it works and the benefits | task (writing) | M12, M13, F1 | no |
| 6 | Consolidate | Elaborate 1-2 points, 300 words; speed-up or new problem classes, quantitative and qualitative | portfolio | F1, F3, M12, M13 | Assessment 2 |
| 6 | Consolidate (optional) | Puzzle game (best identification: The Qubit Factory) | interactive | M12 | no |
| 7 | Explore | 200 words: which QT will spread soonest; contrast all types; largest markets | task (writing) | F2, F3 | no |
| 7 | Apply | One-page A4 fact sheet on the QT most relevant to your background: features, advantage, how it helps | task (writing) | F1, F2, F3, M14 | Assessment 2 (input) |
| 7 | Consolidate | 300 words on the benefit to your background, with a quantitative benefit/risk assessment; upload fact sheet + text to the portfolio | portfolio | F1, F2, F3, M14 | Assessment 2 |
| 7 | End of week | Submit Assessment 2 (Portfolio, 2,100 words) | assessment | all Consolidate rows | Assessment 2 |

## Quizzes (formative, 4 questions each, multiple attempts)

Each week's Explore quiz and Checkpoint quiz contain the same questions with the options shuffled, so the key is given by **option text**, not letter. Weeks 1, 6 and 7 have no quiz. Seen as practice, these are cheap points. Seen as signals, the flagged ones show where the course's wording is looser than the physics.

| Week | Q | Question (short) | Answer (by option text) | Why | Flag |
|---|---|---|---|---|---|
| 2 | 1 | Devices containing magnetometers (phones, ABS, drones, traction control) | All of the above | Compass in phones and drones; ABS and traction control read wheel speed with magnetic (Hall or magnetoresistive) sensors; Week 2 lecture lists car traction control among classical magnetic sensors | none |
| 2 | 2 | Devices containing magnetometers (BCI, mineral drills, heart diagnosis, battery diagnostics) | All of the above | MEG-based brain interfaces, drill-steering magnetometers, magnetocardiography, battery current imaging (lecture §2.5) | none |
| 2 | 3 | Rely on precise timing (satnav, weather, power grids, finance) | All of the above | Satnav ranging, time-stamped sensor data, grid phase sync, trade time-stamping (§2.11) | none |
| 2 | 4 | Rely on precise timing (sensor networks, UTC, computer networks) | All of the above | Same idea | none |
| 3 | 1 | Example(s) of inertial forces | Gravitational pull on massive objects | Gravity is indistinguishable from acceleration (equivalence principle), which is why the week's gravimeters are "inertial sensors". Friction and molecules cooling in a fridge are not inertial effects | Arguable: a setter might intend "All of the above". The Explore version also has no option "d" (labels jump c to e) |
| 3 | 2 | Suitable tool to measure an inertial force | A (calibrated) spring | A spring stretches under an inertial force (spring gravimeter, lecture §3.2) | none |
| 3 | 3 | Magnetometry is done by | Quantum sensors | Week 1 taxonomy | none |
| 3 | 4 | Rely on precise timing | All of the above | Repeats Week 2 Q3 | none |
| 4 | 1 | Where encryption is needed | All of the above | All four exchange sensitive data | none |
| 4 | 2 | True about quantum communication | Quantum physics provides fundamental mechanisms for preventing undetected eavesdropping | Messages can be intercepted, but interception is detectable. Nothing is instantaneous: the no-signalling principle holds | none |
| 4 | 3 | What is a qubit | A quantum bit | Definition | none |
| 4 | 4 | What is quantum cryptography | The process of using quantum mechanics to encrypt data | Intended answer | Loose: QKD distributes a key; the encryption itself is classical (one-time pad or AES) |
| 5 | 1 | Potential future applications (finance, drugs, crypto) | All of the above | All three are standard claimed areas | none |
| 5 | 2 | Quantum computers vs simulators | Quantum computers can be universal, while quantum simulators only address a specific set of problems | Matches lecture §5 intro: a simulator is a special-purpose machine | Option "solved problems classical can't" is contested (sampling-advantage claims), so "All of the above" is also wrong |
| 5 | 3 | Fundamental concept in quantum computing | Most defensible: "entanglement allows for the encoding and manipulation of information in qubits" | "Superposition allows simultaneous computation of all outcomes" is the parallelism myth: you only read one outcome, and the gain comes from interference | **Ambiguous:** the setter may intend the superposition option (Week 1 lecture L70 repeats the myth). If one is marked wrong, try the other and note which the course wants |
| 5 | 4 | A "fundamental limitation" in quantum computing | "Quantum computers can break cryptographic systems using Shor's algorithm" | It is the only true statement among the options | **Badly posed:** it is a capability, not a limitation. The other three are false claims |

## Lecture errors that affect understanding (verified or flagged by full reads)

The companions must teach the correct version and say so. The two errors marked *verified* were checked line by line in this session; the rest come from full-read mining reports.

| Week | Line | Lecture says | Correct version |
|---|---|---|---|
| 1 | L52 | QKD uses entangled particles | BB84 (the lecture's own reference) uses none; entanglement-based QKD (E91) is a separate family |
| 1 | L70 | Quantum computers do multiple calculations simultaneously | Interference of amplitudes, then one measured outcome |
| 2 | L74 | Noise unit "T√Hz" | T/√Hz |
| 2 | L82 vs L137 | NV sensitivity 10⁻⁶ vs 100 nT/√Hz | Inconsistent; quote a primary source |
| 2 | L94 | "Amplitude increases by r²" | The ratio scales as (r₁/r₂)²: halve the distance, get 4× the signal |
| 3 | L105-110 *(verified)* | Φ = k_eff a τ² with τ = 2T | Standard: Φ = k_eff g T², T = time between pulses; the lecture's convention is 4× larger |
| 3 | L91 | Chirp α = g | Null at α = k_eff g / 2π |
| 3 | L135 | Spring sensitivity ∝ 1/T² | Rises as T² (δL = gT²/4π²) |
| 3 | L99 vs L139 | FG5 noise 5 vs 50 µGal/√Hz | Inconsistent; flag |
| 4 | L152 | Repeaters "amplify" the signal | Amplifying is forbidden by no-cloning; repeaters use entanglement swapping plus memories |
| 5 | L55 *(verified)* | Table 5.2: 20 particles 840 kB, 40 particles 880 GB | 8·2ᴺ bytes: 8.4 MB and 8.8 TB |
| 6 | L150 *(verified)* | r = 2ˢr′ with r′ a factor; a^{r/2}+1 ≡ 0 mod N is the success case | Need r even and a^{r/2} ≢ −1 mod N; then gcd(a^{r/2} ± 1, N) |
| 6 | L184 *(verified)* | Threshold theorem = correction introduces errors | Below a threshold error rate, logical error can be made arbitrarily small |
| 6 | L131 vs L139 | Database search listed as an exponential speed-up | Grover is quadratic |
| 6 | L162/L170/L188 | Three different fidelity sets | Quote one primary source with a date |
