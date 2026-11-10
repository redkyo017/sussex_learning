# Module 4 Foundations Sprint (Applications of Quantum Technology): Design Spec

**Date:** 2026-11-10
**Location:** `module_4_applications_of_quantum_technology/foundations_sprint/`
**Duration:** 10 sprint days at about 3 h/day (about 30 h). After that, about 3 h per course week for Weeks 4-7 runs alongside the lectures.
**Type:** Hybrid that leans qualitative. The unit of teaching is a named **framework**, used to write quantified quantum-vs-classical arguments, backed by a small set of named quantitative **moves**, used to follow and reuse the lectures' numbers. Days use the hybrid cadence below. The layout is Module 3's.

## Purpose & Goals

The learner is a senior backend engineer who has finished Module 3 (bra-ket, 2×2 eigenproblems, measurement, tensor products). Their physics and engineering background beyond that is thin. They are at the start of Week 2 of a 7-week applications survey: sensing (clocks, magnetometers, atom interferometers), communication, simulation, computing, and maturity. They want to follow every lecture step and handle every weekly task in the module "fast, but real".

The module asks one question in seven forms: *what does the quantum version do better than the classical one, by how much, and how mature is it?* It does not assess derivations. Full reads of all seven lectures (2026-11-10) show three things. The lectures assert advantages with few numbers. They skip the few derivations they rely on, most importantly Φ = k_eff g T² in Week 3. And they contain about 15 errors that a careful reader will trip over (listed in `../../problem_inventory.md`). So the sprint teaches the **argument shape** first, then the **handful of scaling laws** that put numbers into it, then decodes each lecture against both.

The learner asked whether the module is "more theory". The answer: it is conceptual and argumentative, not mathematical. The maths is order-of-magnitude reasoning plus about 10 scaling laws. Evidence: the equation counts per lecture (0, ~6, ~12, 3, 2, ~10, 0) and the fact that no week contains a numbered maths problem.

## Success Criteria

By the end of Day 10, without notes, the learner can:

1. State the four quantum technology types and, for each, the figure of merit that defines "better" (sensitivity per √Hz, fractional frequency stability, secure key rate and distance, problem size or scaling).
2. Convert between the module's units and scales (fT, aT, µGal, Eötvös, fractional uncertainty to seconds and metres, dB/km to transmission) and sanity-check any number to an order of magnitude.
3. Explain and apply the averaging laws: noise density × √bandwidth, 1/√t averaging, shot noise 1/√N versus the Heisenberg limit 1/N.
4. Explain how an atomic clock locks to a transition, why optical beats microwave (Q = ν/Δν), and how SQUID, OPM and NV magnetometers differ in sensitivity, bandwidth, standoff and SWaP-C.
5. Derive Φ = k_eff g T² from three pulses at concept level, compute a phase or sensitivity from it, and explain why atom-versus-light gains of ~10¹⁰ shrink to "a few orders" in practice.
6. Run BB84 by hand, including sifting, the 25% intercept-resend QBER and (3/4)ⁿ detection. Prove no-cloning in four lines. Compute the CHSH values 2 versus 2√2. Explain fibre loss and trusted nodes versus repeaters. Place QKD against post-quantum cryptography.
7. Compute classical memory for N spins (8·2ᴺ bytes), explain analogue versus digital simulation, and explain the superfluid-to-Mott story as tunnelling J versus interaction U.
8. Trace a Bell-state circuit and Deutsch-Jozsa as amplitude sums. Sort speed-ups into exponential, sub-exponential, quadratic and unproven/heuristic. Estimate circuit depth from gate fidelity and explain error-correction overhead.
9. Assign a TRL with evidence, map risks onto the module's five barrier categories, and produce a one-page fact sheet plus a quantified benefit/risk paragraph, all on a fictional case.
10. For each week, write a 300-word gain argument in the F1 shape (below) on the fictional running case in under 40 minutes.

## Constraints & Environment

- Text only. Markdown in the repo; British English; maths in `$...$` like Module 3.
- **Syllabus exports are read-only.** Everything new lives in `foundations_sprint/`.
- **Assessment boundary (the learner's choice).** This sprint teaches comprehension only. It contains nothing aimed at Assessment 1 items (brief not exported; separate session). It never drafts Portfolio text.
- **Clone integrity.** No exercise or model paragraph uses a named case from the lectures as its case (`../../clone_forbidden_entities.txt`). Companions may name lecture cases in §2-§4 when decoding.
- **Simulations: no `code/` folder in v1.** The three course interactives are covered as guided walkthroughs inside companions or days. An optional Go or Python mini-lab (BB84, state-vector memory) is a later extension if asked.
- **Figures.** The learner may add `week_K/figures/figK_N.png` (priority Weeks 3, 4, 5, 2). The companions are written from the text now. When figures arrive, each gets a short "reading the figure" note added in a later pass.
- Scratch branch `authoring/module4`; never pushed; torn down before handoff.

## Deadlines (recorded per skill rule; earlier time treated as real)

| Assessment | `module_4_intro.md` text | Canvas summary table (time zone not stated) | Learner (2026-11-10) | Planning date |
|---|---|---|---|---|
| A1 Problem Set (30%) | Thursday of Week 3, 17:00 UK = Thu 19 Nov 2026 | Fri 20 Nov 2026 "12am" | 20 Nov 00:00 UK | **Thu 19 Nov 17:00 UK**; confirm on Sussex Direct |
| A2 Portfolio (70%, 2,100 words) | Monday of Week 8, 10:00 UK = Mon 21 Dec 2026 | Mon 21 Dec 2026 5pm | 21 Dec 17:00 UK | **Mon 21 Dec 10:00 UK**; confirm on Sussex Direct |

One possibility: the Canvas table shows the learner's local time (UTC+7). In that case "Fri 20 Nov 12am" equals Thu 19 Nov 17:00 UK and "21 Dec 5pm" equals 10:00 UK, and the sources agree. The learner reads them as UK times. Until confirmed, plan to the earlier times. Week 1 began Mon 2 Nov 2026 (derived: Thursday of Week 3 = 19 Nov).

## Target Sources (checked 2026-11-10)

Primary: the seven lecture exports. Free external reading, verified live on 2026-11-10 (IDs confirmed through the arXiv API):

| Use | Source | Link | Read |
|---|---|---|---|
| Sensing core (W1-3) | Degen, Reinhard, Cappellaro, *Quantum sensing*, RMP 89, 035002 (2017) | https://arxiv.org/abs/1611.02427 | §I-III |
| Magnetometers (W2) | Budker & Romalis, *Optical magnetometry*, Nat. Phys. 3, 227 (2007) | https://arxiv.org/abs/physics/0611246 | all (short) |
| Clocks (W2) | Ludlow et al., *Optical atomic clocks*, RMP 87, 637 (2015) | https://arxiv.org/abs/1407.3493 | §I + applications |
| Clocks, light (W2) | NPL, *Optical atomic clocks* | https://www.npl.co.uk/research/time-frequency/optical-atomic-clocks | page |
| Atom interferometry (W3) | Abend et al., *Atom interferometry and its applications* | https://arxiv.org/abs/2001.10976 | intro, gravimeter, applications |
| Reference (W3) | Cronin, Schmiedmayer, Pritchard, RMP 81, 1051 (arXiv title "Atom Interferometers") | https://arxiv.org/abs/0712.3703 | inertial sensing section only |
| Paid, optional (W3) | Bongs et al., Nat. Rev. Phys. 1, 731 (2019) | doi:10.1038/s42254-019-0117-4 | no free copy found |
| QKD (W4) | Pirandola et al., *Advances in quantum cryptography* (2020) | https://arxiv.org/abs/1906.01645 | §1, BB84, practical/satellite sections |
| QKD vs PQC (W4, W7) | NCSC white paper, *Quantum security technologies* | https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies | all |
| Satellite (W4) | Chapman & Peters, Physics 15, 172 (2022) | https://physics.aps.org/articles/v15/172 | all |
| Simulation (W5) | Georgescu, Ashhab, Nori, *Quantum simulation*, RMP 86, 153 (2014) | https://arxiv.org/abs/1308.6253 | §I-III |
| Simulation (W5) | Aspuru-Guzik & Walther, Nat. Phys. 8, 285 (2012); author copy (draft title "Photonic Quantum Orreries") | https://dash.harvard.edu/bitstream/handle/1/11881655/aspuru-guzik-photonic-quantum-simulators.pdf?sequence=1 | intro |
| Computing (W6) | Preskill, *Quantum computing in the NISQ era and beyond* (2018) | https://arxiv.org/abs/1801.00862 | all |
| Computing (W6) | Aaronson, *The Limits of Quantum Computers* (author draft) | https://www.scottaaronson.com/writings/limitsqc-draft.pdf | all |
| Refresher (W6) | Quantum Country (Matuschak & Nielsen) | https://quantum.country/qcvc | essay 1 |
| Refresher (W6) | IBM Quantum Learning, *Basics of quantum information* | https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information | lessons 1-3 |
| Paid, optional (W6) | Nielsen & Chuang (CUP 2010) | buy | ch. 1, 4.1-4.3, 12.6 |
| Maturity (W7) | UK National Quantum Strategy (DSIT 2023) | https://www.gov.uk/government/publications/national-quantum-strategy | summary + missions |
| Market (W7) | McKinsey Quantum Technology Monitor 2026 (Apr 2026) | https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point | executive summary |

Course interactives:
- **Week 4:** QuVis BB84 (high confidence): https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/BB84_photons/BB84_photons.html
- **Week 6:** The Qubit Factory (medium-high confidence): https://www.qubitfactory.io/
- **Week 1:** circuit simulator, not identified. Best guess: Quantum Länd Circuit Designer, https://thequantumlaend.de/quantum-circuit-designer/. Quirk (https://algassert.com/quirk) is the fallback used in the content.

## Strategy (the core design decision)

**Problem-first, argument-first.** Every weekly writing task has the same skeleton. So the sprint teaches that skeleton (F1) on Day 1 and has the learner write it every day on one fictional case. The physics is pulled in as needed to fill the slots with correct numbers. This follows the learner's standard from Module 3: problem-first reverse engineering, retrieval over rereading, a fixed write-up shape from Day 1.

### Frameworks (qualitative unit)

- **F1 Gain argument (six parts; the writing twin of Module 3's six steps):**
  1. Classical limit, with a number
  2. Quantum mechanism, in one sentence of physics
  3. Figure of merit named
  4. Quantified gain (ratio or scaling, sourced)
  5. Maturity and practicality (TRL, SWaP-C, barriers)
  6. Verdict with one honest caveat
- **F2 Maturity lens:**
  - NASA TRL 1-9, using the lecture's Week 7 table verbatim
  - The module's quantum-advantage test (a relevant task no known conventional technology does with reasonable effort)
  - The five barrier categories, in the lecture's order: technology (performance, SWaP-C, robustness); proof of relevance and practicality; use cases; validation of usability (regulation, standards, UI); scalable and robust production
  - The rule that component TRL is higher than system TRL
- **F3 Credible numbers:** source hierarchy (peer-reviewed or metrology institute > review > vendor datasheet > press release > market report); always state date, conditions and units; the rule that a ratio needs both sides measured the same way.

### Moves (quantitative unit, about 10 min each, drilled cold)

| ID | Move |
|---|---|
| M1 | Orders of magnitude, SI prefixes, module units (T, Gal, E, fractional), fractional error → time → distance via c |
| M2 | Noise density and bandwidth: δx = S·√B; 1/√t averaging; Allan deviation as "stability versus averaging time" (concept and reading plots) |
| M3 | Shot noise 1/√N versus Heisenberg 1/N; SNR; the inverse-square distance gain |
| M4 | Two-level system as a frequency reference: E = hν, Q = ν/Δν, pulse area (π/2 splitter, π mirror), the lock loop |
| M5 | Magnetometer physics in one line each: Larmor frequency γB (OPM), flux quantum Φ₀ = h/2e (SQUID), NV spin readout |
| M6 | Interference: phase → cos² intensity; k = 2π/λ; de Broglie λ = h/mv |
| M7 | Atom interferometry: photon recoil ħk, k_eff ≈ 2k; Φ = k_eff g T²; T² scaling (ground vs space); Sagnac ratio and why real gain is smaller |
| M8 | Crypto in one page: symmetric key and one-time pad, public key and the Shor threat, harvest-now-decrypt-later and Mosca's x + y > z, PQC vs QKD |
| M9 | BB84 by hand; QBER 25% under intercept-resend; (3/4)ⁿ detection; no-cloning in four lines |
| M10 | CHSH 2 versus 2√2 (arithmetic only); fibre loss in dB/km → transmission; key rate falls with distance; trusted node versus repeater |
| M11 | 2ᴺ amplitudes and 8·2ᴺ bytes; Hamiltonian evolution as a matrix; analogue versus digital simulation; J versus U |
| M12 | Gates and circuits: H, X, Z, CNOT, Bell state; phase kickback; Deutsch-Jozsa as an amplitude sum; interference, not parallelism |
| M13 | Speed-up taxonomy (Shor exponential versus sub-exponential NFS; Grover (π/4)√N; heuristic: annealing, VQE); depth from fidelity (F^g); physical:logical overhead; threshold theorem stated correctly |
| M14 | Benefit/risk quantification: ranges not points, expected value, sensitivity to the weakest assumption; fact-sheet anatomy |

### Load-bearing fundamentals kept (and why)

- **M1** units and orders of magnitude: every task demands "quantitative measures".
- **M2-M3** the √ averaging laws: they define "sensitivity" in Weeks 2, 3 and 7.
- **M4** the two-level resonance: clocks, OPMs, NV, Raman pulses and qubits are all the same object, and the learner already owns its maths from Module 3.
- **M6** interference phase: Weeks 3, 4 and 6 run on it.
- **M11/M13** exponential versus polynomial scaling: the entire simulation and computing argument.
- **F2** TRL: Week 7 and every "practical aspects" clause.

### Skipped (and why)

Each item below is labelled as judgement: none is examined by any inventory row.
- Atomic structure derivations (hyperfine, Zeeman beyond one line)
- Josephson and BCS theory
- Laser-cooling mechanics (the MOT is named only)
- Bose-Hubbard and BKT mathematics (story level only)
- The QFT and continued-fraction derivation of Shor (arithmetic of the classical part only)
- Complexity classes beyond the taxonomy
- Full CHSH derivation
- Security proofs of QKD

### Where to use AI

- **For learning and writing:** as tutor, examiner, number generator, critic, co-writer and source finder (STRATEGY §8).
- **The Day 10 handoff:** the learner switches to their own case.

### Evidence for the method

These are standard findings, cited by name, and the Module 3 strategy already uses them:
- Retrieval practice (Roediger & Karpicke 2006)
- Spacing (Cepeda et al. 2006)
- Productive failure / problem-first (Kapur 2008)

The specific 10-day split and the 3 h/day sufficiency are **judgement**. They are based on lecture length (about 380 KB of text, light on maths) and on Module 3's 32.5 h sprint for a more mathematical module.

### Rejected alternatives

- **Week-by-week just-in-time study:** the learner is a week behind and Weeks 3 and 4 introduce physics and crypto at once.
- **A physics-first strand like Module 3's `physics/`:** this module needs about 10 scaling laws, not a physics course, so the physics is folded into the days.

## Curriculum

**Fictional running case (used in every Apply block and every model paragraph): "Harrowmere Water & Power",** a made-up regional utility. It is deliberately outside the learner's own field, so the learner's portfolio case stays theirs. It offers one hook per week:

| Week | Hook in the running case |
|---|---|
| 1 | survey |
| 2 | grid timing; magnetic pipe and cable inspection |
| 3 | gravity survey for leaks and voids |
| 4 | securing control-network telemetry |
| 5 | catalyst and corrosion materials |
| 6 | pump and maintenance scheduling claims |
| 7 | fact sheet and benefit/risk |

| Day | Date (rec.) | Focus | Moves / frameworks | Inventory rows covered | Companion |
|---|---|---|---|---|---|
| 01 | Wed 11 Nov | Module map; four QT types and their figures of merit; F1 gain argument; F3 credible numbers; M1 units/orders. Week 1 lecture read with Day 01 as its decoder (no Week 1 companion). Lecture errors W1 L52/L70 | F1, F3, M1 | W1 Explore, Apply, Consolidate | none (Week 1) |
| 02 | Thu 12 Nov | What makes a good sensor: precision vs accuracy, bandwidth, dynamic range, SWaP-C; noise density, √B, 1/√t, Allan; shot vs Heisenberg; SNR and distance | M2, M3 | W2 Consolidate (sensitivity, bandwidth, dynamic range) | Week 2 §1-3 |
| 03 | Fri 13 Nov | Clocks (lock loop, Q, microwave → optical, comb at concept level) and magnetometers (SQUID Φ₀, OPM/SERF Larmor, NV, BEC microscope): comparison table | M4, M5 | W2 Apply, Consolidate, quizzes | Week 2 (full) |
| 04 | Sat 14 Nov | Interferometry: optical Mach-Zehnder, matter waves, recoil, Raman pulses as splitters and mirrors, Φ = k_eff g T² built step by step, T² gain, Sagnac ratio, classical gravimeter comparison | M6, M7 | W3 Apply, Consolidate, quizzes | Week 3 |
| 05 | Sun 15 Nov | Sensing checkpoint: no-notes mixed test on Days 1-4; one timed 300-word F1 piece on the running case; spaced review | review | W1-W3 rows | none |
| (A1) | Mon 16 - Thu 19 Nov | Assessment 1 window, separate session. 20 min/day spaced review only | none | none | none |
| 06 | Fri 20 Nov | Crypto essentials → qubit encoding → no-cloning → BB84 / B92 / E91 → CHSH → channels, loss, trusted nodes, repeaters → PQC vs QKD; QuVis BB84 walkthrough | M8, M9, M10 | W4 all rows + interactive | Week 4 |
| 07 | Sat 21 Nov | Simulation: why classical fails (2ᴺ, with the corrected Table 5.2), analogue vs digital, bosons/fermions/BEC, optical lattices, J vs U and Mott, trapped-ion spin models | M11 | W5 all rows, W6 Explore | Week 5 |
| 08 | Sun 22 Nov | Computing I: circuits, Bell state, phase kickback, Deutsch-Jozsa as amplitude sum; interference not parallelism; Quirk walkthrough (stands in for the W1 simulator); Qubit Factory walkthrough | M12 | W1 interactive, W6 Apply, game | Week 6 §1-4 |
| 09 | Mon 23 Nov | Computing II: speed-up taxonomy, Shor arithmetic on a fresh N, Grover iterations, platforms and fidelities, depth from fidelity, QEC threshold (correct statement), NISQ/VQE, annealing vs gate model | M13 | W6 Consolidate | Week 6 (full) |
| 10 | Tue 24 Nov | Maturity and comparison: TRL with evidence, five barriers, advantage test, markets (sourced), M14 benefit/risk; running-case fact sheet + benefit/risk paragraph; "map your own background" exercise (the learner picks their case; no writing for them); cumulative no-notes capstone | F2, M14 | W7 all rows | Week 7 |

**After Day 10 (course Weeks 4-7):** about 3 h per week. Run the Five-Pass Lecture Protocol with that week's companion, do the quiz, write the Apply post, then the learner's own Consolidate piece.

**Spaced review:** each day's §Spaced review pulls from N−1, N−3 and N−7, and Day 05 and Day 10 are cumulative. After the sprint, a 20-minute retrieval set from `GLOSSARY.md` runs at +7 and +21 days, the second landing just before the Portfolio deadline.

**No-notes checkpoints:**
- **Day 05:** sensing (M1-M7, F1).
- **Day 10:** everything. A mixed 10-item quantitative set plus one 300-word F1 piece and one fact sheet on the running case, each under time.

## Directory Layout (Module 3's, exactly)

```
foundations_sprint/
├── README.md                 quickstart, day map, companion map, timetable incl. A1 window, deadline table
├── STRATEGY.md               strategy, kept/skipped fundamentals, mistakes, Five-Pass protocol,
│                             six-steps (quantitative) + F1 gain argument (writing), confusion log
├── content/
│   ├── GLOSSARY.md           notation- and unit-first, grouped by day, A-Z index
│   ├── day01.md … day10.md
│   └── companions/
│       └── week02_companion.md … week07_companion.md
└── docs/
    ├── problem_inventory.md          (done) every task, portfolio and quiz item + quiz key + lecture errata
    ├── clone_forbidden_entities.txt  (done) lecture named cases
    ├── verify_numbers.py             stdlib-only recomputation of every numeric answer in the sketches
    └── superpowers/{specs,plans}/
```

There is no `physics/` strand and no `code/` in v1.

## Content Day Skeleton (hybrid)

```markdown
# Day NN: <Title>

**Time:** ~3 h · **Feeds:** Week K lecture, inventory rows … · **Companion:** weekKK_companion.md §…

## Why this matters
## Core concepts
### Move MN.x / Framework Fx: <name>   (each: idea → one worked clone → "you've got it when…")
## Exercises
1. (quantitative) <problem> — **Hint:** … — **Solution sketch:** six-steps form, numbers checked in verify_numbers.py
2. (writing) <application prompt on the running case> — **Hint:** … — **Model paragraph:** … — **What a weak answer misses:** …
## Anti-patterns / Common mistakes   (mistake → how you'd notice → instead)
## Done when    (no-notes self-check with pass mark)
## Spaced review   (from Day 02; recall prompts from N−1, N−3, N−7)
## Read next    (one or two links from Target Sources, with sections)
```

Cadence (180 min):
- 15 min retrieval
- 55 min moves/frameworks
- 50 min quantitative drills
- 45 min writing on the running case
- 15 min companion pointer and confusion log

Each day has 6-10 exercises, at least 2 of them writing.

**Companions** follow `references/companion-skeleton.md`:
- §3 is a notation **and unit** decoder.
- §4 includes every lecture erratum for that week, from the inventory, with the correct version.
- §5 clones use different numbers, functions and cases from anything in the lecture.
- Each companion with figures adds §8 "Figures" (figures were supplied 2026-11-10 for Weeks 2-5).
- Week 4 and Week 6 add §9 "Course interactive walkthrough" (Week 4 QuVis; Week 6 Qubit Factory).

## Verification (Phase 4)

1. `check_clones.py module_4_.../week_*/ module_4_.../foundations_sprint/content/`. It passes almost vacuously, since the course has no maths problems. Run it anyway.
2. Entity check:
   - `check_clones.py --entities docs/clone_forbidden_entities.txt` over `content/day*.md`.
   - For companions, the same check runs over §5-§6 only, extracted to scratch. Decoding sections may name lecture cases.
3. `python3 docs/verify_numbers.py` recomputes every numeric answer in the solution sketches and must print 0 mismatches.
4. Every exercise has a hint plus a sketch or model paragraph. Every day has Done when; Days 02-10 have Spaced review. A grep check covers both.
5. Every inventory row is cited by at least one day or companion (row → file map in README), and every move is cited by an inventory row.
6. `git status` shows no change outside `foundations_sprint/`.

## Settled after the builder check (author's calls, flagged for the learner)

1. **Build once, check in two batches.**
   - Batch 1: README, STRATEGY, GLOSSARY (Days 1-5 part), Days 01-05, Week 2-3 companions.
   - Batch 2: Days 06-10, Week 4-7 companions, GLOSSARY completion, README row map.
   - Each batch runs the full Verification list.
   - There is a single handoff after Batch 2.
   - If the build is not finished by the morning of Wed 11 Nov, every recommended date shifts by the same delay. The A1 window stays fixed, and Days 01-05 are compressed into the days left before it, never into it.
2. **End state.**
   - The branch was cut from `master` at d579c1e, so the lecture exports are already on `master`.
   - Teardown follows the engine's sequence (`reset --soft master` → `switch master` → `reset` → `branch -D`). It leaves `foundations_sprint/` as untracked files on `master` for the learner to commit.
   - Nothing is pushed; no export is touched.
3. **The learner's own Weeks 1-3 Consolidate pieces.**
   - The README timetable gives them a slot in the week after Day 10, Wed 25 - Sun 29 Nov: about 45 min each.
   - Weeks 4-7 pieces are written in their own course week.

## Left to the builder

- Exercise numbers and wording.
- The fictional case's internal figures. They must be plausible and labelled fictional.
- Glossary grouping detail.
- Splitting heavy days, Day 04 and Day 06, into "core" and "stretch" exercises if they run past 3 h.
