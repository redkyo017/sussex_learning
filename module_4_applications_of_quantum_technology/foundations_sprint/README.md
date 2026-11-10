# Module 4 Foundations Sprint

This is a text-only learning path for Module 4, Applications of Quantum Technology. It is written for a learner who has finished Module 3 and is starting Week 2, and who wants to follow every lecture step and handle every weekly task "fast, but real". It has ten sprint days of about 3 h each, plus a separate ~2 h Day 10 capstone (about 32 h), six Week Companions that decode the Week 2-7 lectures (and correct their errors), and a glossary. After Day 10, about 3 h per course week runs alongside the Week 4-7 lectures. How and why it works is in [STRATEGY.md](STRATEGY.md).

## Quickstart

1. Read [STRATEGY.md](STRATEGY.md) once (30 min). The parts you will use daily are the F1 gain argument (§6), the six steps (§5) and the Five-Pass Lecture Protocol (§4).
2. Start [Day 01](content/day01.md) on Wed 11 Nov. Each day is about 3 h in a fixed cadence: 15 min retrieval, 55 min moves and frameworks, 50 min quantitative drills, 45 min writing on the running case, 15 min companion pointer and confusion log.
3. Make a cold attempt at every exercise first. Only then read the hint, and only after that the solution sketch or model paragraph.
4. All practice writing uses the fictional utility **Harrowmere Water & Power**, never your own background case. Your own case starts on Day 10 (ways to use AI along the way are in [STRATEGY.md](STRATEGY.md#8-using-ai)).
5. Keep one confusion log per lecture (template in [STRATEGY.md](STRATEGY.md#7-confusion-log-template)).

## Deadlines

| Assessment | `module_4_intro.md` text | Canvas summary table (time zone not stated) | Learner (2026-11-10) | Planning date |
|---|---|---|---|---|
| A1 Problem Set (30%) | Thursday of Week 3, 17:00 UK = Thu 19 Nov 2026 | Fri 20 Nov 2026 "12am" | 20 Nov 00:00 UK | **Thu 19 Nov 17:00 UK**; confirm on Sussex Direct |
| A2 Portfolio (70%, 2,100 words) | Monday of Week 8, 10:00 UK = Mon 21 Dec 2026 | Mon 21 Dec 2026 5pm | 21 Dec 17:00 UK | **Mon 21 Dec 10:00 UK**; confirm on Sussex Direct |

**Time-zone note.** One possibility: the Canvas table shows your local time (UTC+7). In that case "Fri 20 Nov 12am" equals Thu 19 Nov 17:00 UK and "21 Dec 5pm" equals 10:00 UK, and the sources agree. You read them as UK times. Until confirmed, plan to the earlier times. Week 1 began Mon 2 Nov 2026 (derived: Thursday of Week 3 = 19 Nov). Check Sussex Direct (Study > Timetable > Assessment Deadlines) for the official time and whether a 24-hour late period (+1) applies.

## Is this module theory-heavy?

No. It is conceptual and argumentative, not mathematical. The maths is order-of-magnitude reasoning plus about 10 scaling laws. The evidence: the lectures contain roughly 0, 6, 12, 3, 2, 10 and 0 equations in Weeks 1-7, and no week has a numbered maths problem. The weekly work is short, quantified writing plus 4-question quizzes. What the module does demand is that every claim of "better" carries a correct number, a unit and a source, so the sprint teaches the argument shape (F1) first and then the moves that fill it with numbers.

## Day map and timetable

The dates are recommendations. If the sprint starts late, every recommended date shifts by the same delay, except the A1 window, which stays fixed: Days 01-05 are compressed into the days left before it, never into it.

| Day | Date (rec.) | Focus | Moves / frameworks | Companion |
|---|---|---|---|---|
| [01](content/day01.md) | Wed 11 Nov | Module map; four QT types and their figures of merit; F1 gain argument; F3 credible numbers; units and orders of magnitude. Week 1 lecture read with Day 01 as its decoder | F1, F3, M1 | none (Week 1) |
| [02](content/day02.md) | Thu 12 Nov | What makes a good sensor; noise density, √B, 1/√t, Allan deviation; shot noise versus Heisenberg; SNR and distance | M2, M3 | [Week 2](content/companions/week02_companion.md) §1-3 |
| [03](content/day03.md) | Fri 13 Nov | Clocks (lock loop, Q, microwave → optical, comb at concept level) and magnetometers (SQUID, OPM/SERF, NV, BEC microscope): comparison table | M4, M5 | [Week 2](content/companions/week02_companion.md) (full) |
| [04](content/day04.md) | Sat 14 Nov | Interferometry: Mach-Zehnder, matter waves, recoil, Raman pulses, Φ = k_eff g T² step by step, T² gain, Sagnac ratio, classical gravimeter comparison | M6, M7 | [Week 3](content/companions/week03_companion.md) |
| [05](content/day05.md) | Sun 15 Nov | Sensing checkpoint: no-notes mixed test on Days 1-4; one timed 300-word F1 piece on the running case | review | none |
| (A1) | Mon 16 - Thu 19 Nov | Assessment 1 window, separate session. 20 min/day spaced review only | none | none |
| [06](content/day06.md) | Fri 20 Nov | Crypto essentials → no-cloning → BB84 / B92 / E91 → CHSH → loss, trusted nodes, repeaters → PQC versus QKD; QuVis BB84 walkthrough | M8, M9, M10 | [Week 4](content/companions/week04_companion.md) |
| [07](content/day07.md) | Sat 21 Nov | Simulation: why classical fails (2ᴺ), analogue versus digital, bosons/fermions/BEC, optical lattices, J versus U and the Mott insulator, trapped-ion spin models | M11 | [Week 5](content/companions/week05_companion.md) |
| [08](content/day08.md) | Sun 22 Nov | Computing I: circuits, Bell state, phase kickback, Deutsch-Jozsa as an amplitude sum; interference, not parallelism; Quirk and Qubit Factory walkthroughs | M12 | [Week 6](content/companions/week06_companion.md) §1-4 |
| [09](content/day09.md) | Mon 23 Nov | Computing II: speed-up taxonomy, Shor arithmetic, Grover iterations, platforms and fidelities, depth from fidelity, error-correction threshold, NISQ/VQE, annealing versus gate model | M13 | [Week 6](content/companions/week06_companion.md) (full) |
| [10](content/day10.md) | Tue 24 Nov (capstone: Tue 24 Nov evening or Wed 25 Nov morning) | Maturity and comparison: TRL with evidence, five barriers, advantage test, markets, benefit/risk; running-case fact sheet; "map your own background" (you pick the case, no writing done for you); cumulative no-notes capstone in a separate session | F2, M14 | [Week 7](content/companions/week07_companion.md) |
| own pieces | Wed 25 - Sun 29 Nov | Your own Weeks 1-3 Consolidate pieces: about 45 min each | none | none |

**Day 10 runs in two sittings.** The ~3 h core (frameworks, drills, the timed fact sheet) is on Tue 24 Nov. The no-notes capstone (Exercises 10.6-10.16, about 2 h: 50 min items, 40 min timed F1 piece, 30 min marking) is a separate session, either on Tue 24 Nov evening after a break or first thing on Wed 25 Nov before your own pieces. Do not split the capstone itself across days. Day 10 is therefore about 5 h in total, so the sprint is about 32 h rather than a flat 30.

**After Day 10 (course Weeks 4-7 run Mon 23 Nov to Sun 20 Dec; start this rhythm on Mon 30 Nov, after Day 10 and your own Weeks 1-3 pieces on Wed 25-Sun 29 Nov):** about 3 h per course week. Run the Five-Pass Lecture Protocol with that week's companion, do the quiz, write the Apply post, then write your own Consolidate piece in that same course week.

**Spaced review.** Each day's Spaced review pulls from days N−1, N−3 and N−7; Days 05 and 10 are cumulative. After the sprint, a 20-minute retrieval set from [GLOSSARY.md](content/GLOSSARY.md) runs at +7 days (about Tue 1 Dec) and +21 days (about Tue 15 Dec), the second just before the Portfolio deadline.

**No-notes checkpoints.** Day 05: sensing (M1-M7, F1). Day 10: everything, as a mixed 10-item quantitative set plus one 300-word F1 piece and one fact sheet on the running case, each under time.

## Companion map

Each companion decodes one week's lecture: §3 is a notation and unit decoder, §4 lists that week's lecture errors with the correct version, §5 has fresh worked clones. Week 1 has no companion; Day 01 is its decoder.

| Course week | Topic | Companion | Sprint days |
|---|---|---|---|
| 2 | Sensing I: clocks and magnetometers | [week02_companion.md](content/companions/week02_companion.md) | 02, 03 |
| 3 | Sensing II: inertial forces (atom interferometry) | [week03_companion.md](content/companions/week03_companion.md) | 04 |
| 4 | Quantum communication and QKD | [week04_companion.md](content/companions/week04_companion.md) | 06 |
| 5 | Quantum simulation | [week05_companion.md](content/companions/week05_companion.md) | 07 |
| 6 | Quantum computing | [week06_companion.md](content/companions/week06_companion.md) | 08, 09 |
| 7 | Comparing different quantum technologies (maturity, markets) | [week07_companion.md](content/companions/week07_companion.md) | 10 |

## Figures

Lecture figures you export live in `../week_K/figures/` as `figK_N.png` (at present Weeks 2, 3, 4 and 5). The companions are written from the lecture text; §8 of each companion decodes that week's figures with a short "reading the figure" note, added as the figures arrive. The figures themselves are yours and are never edited by the sprint.

## Simulations and interactives

There is no `code/` folder in this version. The course interactives are covered as guided walkthroughs instead:

- **Week 4, QuVis BB84:** walked through in [Day 06](content/day06.md) and the [Week 4 companion](content/companions/week04_companion.md). https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/BB84_photons/BB84_photons.html
- **Week 6, The Qubit Factory** (best identification of the course's puzzle game): walked through in [Day 08](content/day08.md) and the [Week 6 companion](content/companions/week06_companion.md). https://www.qubitfactory.io/
- **Week 1, circuit simulator:** not identified for certain (best guess: Quantum Länd Circuit Designer, https://thequantumlaend.de/quantum-circuit-designer/). The content uses Quirk instead, in [Day 08](content/day08.md): https://algassert.com/quirk

An optional Go or Python mini-lab (BB84 by simulation, state-vector memory) is a possible later extension, on request.

## Free reading list

The lecture exports are the primary source. These free sources were checked live on 2026-11-10; each day's Read next section points to the relevant one.

| Week | Source | Link | Read |
|---|---|---|---|
| 1-3 | Degen, Reinhard, Cappellaro, *Quantum sensing*, RMP 89, 035002 (2017) | https://arxiv.org/abs/1611.02427 | §I-III |
| 2 | Budker & Romalis, *Optical magnetometry*, Nat. Phys. 3, 227 (2007) | https://arxiv.org/abs/physics/0611246 | all (short) |
| 2 | Ludlow et al., *Optical atomic clocks*, RMP 87, 637 (2015) | https://arxiv.org/abs/1407.3493 | §I + applications |
| 2 | NPL, *Optical atomic clocks* | https://www.npl.co.uk/research/time-frequency/optical-atomic-clocks | page |
| 3 | Abend et al., *Atom interferometry and its applications* | https://arxiv.org/abs/2001.10976 | intro, gravimeter, applications |
| 3 | Cronin, Schmiedmayer, Pritchard, *Atom Interferometers*, RMP 81, 1051 | https://arxiv.org/abs/0712.3703 | inertial sensing section only |
| 4 | Pirandola et al., *Advances in quantum cryptography* (2020) | https://arxiv.org/abs/1906.01645 | §1, BB84, practical/satellite sections |
| 4, 7 | NCSC white paper, *Quantum security technologies* | https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies | all |
| 4 | Chapman & Peters, Physics 15, 172 (2022) | https://physics.aps.org/articles/v15/172 | all |
| 5 | Georgescu, Ashhab, Nori, *Quantum simulation*, RMP 86, 153 (2014) | https://arxiv.org/abs/1308.6253 | §I-III |
| 5 | Aspuru-Guzik & Walther, Nat. Phys. 8, 285 (2012), author copy | https://dash.harvard.edu/bitstream/handle/1/11881655/aspuru-guzik-photonic-quantum-simulators.pdf?sequence=1 | intro |
| 6 | Preskill, *Quantum computing in the NISQ era and beyond* (2018) | https://arxiv.org/abs/1801.00862 | all |
| 6 | Aaronson, *The Limits of Quantum Computers* (author draft) | https://www.scottaaronson.com/writings/limitsqc-draft.pdf | all |
| 6 | Quantum Country (Matuschak & Nielsen) | https://quantum.country/qcvc | essay 1 |
| 6 | IBM Quantum Learning, *Basics of quantum information* | https://quantum.cloud.ibm.com/learning/courses/basics-of-quantum-information | lessons 1-3 |
| 7 | UK National Quantum Strategy (DSIT 2023) | https://www.gov.uk/government/publications/national-quantum-strategy | summary + missions |
| 7 | McKinsey Quantum Technology Monitor 2026 (Apr 2026) | https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point | executive summary |

Paid and optional: Bongs et al., Nat. Rev. Phys. 1, 731 (2019), doi:10.1038/s42254-019-0117-4 (Week 3, no free copy found); Nielsen & Chuang (CUP 2010), ch. 1, 4.1-4.3, 12.6 (Week 6).

## Read next index

What each day's `## Read next` section sends you to (links in the table above).

| Day | Read next |
|---|---|
| [01](content/day01.md#read-next) | Degen, Reinhard & Cappellaro, *Quantum sensing*, §I-III; Aaronson, *The Limits of Quantum Computers* (for the L70 erratum) |
| [02](content/day02.md#read-next) | Degen et al. §I-II (sensitivity, $1/\sqrt{\text{time}}$); Budker & Romalis, *Optical magnetometry* (before Day 03) |
| [03](content/day03.md#read-next) | Ludlow et al., *Optical atomic clocks*, §I + applications (NPL page optional); Budker & Romalis, all |
| [04](content/day04.md#read-next) | Abend et al., intro, gravimeter and applications sections; Cronin, Schmiedmayer & Pritchard, inertial sensing section only |
| [05](content/day05.md#read-next) | Degen et al. §I-III and Abend et al. gravimeter section, only the parts behind items you missed |
| [06](content/day06.md#read-next) | Pirandola et al., intro, BB84 and DV sections, repeaterless bound, free-space and satellite; NCSC white paper, all |
| [07](content/day07.md#read-next) | Georgescu, Ashhab & Nori, *Quantum simulation*, §I-III; Aspuru-Guzik & Walther, intro |
| [08](content/day08.md#read-next) | Quantum Country, essay 1; IBM Quantum Learning, *Basics of quantum information*, lessons 1-3 (+ skim the teleportation lesson) |
| [09](content/day09.md#read-next) | Preskill, *Quantum computing in the NISQ era and beyond*, all; Aaronson, *The Limits of Quantum Computers*, all |
| [10](content/day10.md#read-next) | UK National Quantum Strategy, summary + missions; McKinsey *Quantum Technology Monitor 2026*, executive summary (extraction cards); NCSC white paper, all |

## Directory map

```
foundations_sprint/
├── README.md                 this file
├── STRATEGY.md               strategy, kept/skipped fundamentals, mistakes, Five-Pass protocol,
│                             six steps (quantitative), F1 gain argument (writing), confusion log, using AI
├── content/
│   ├── GLOSSARY.md           notation- and unit-first, grouped by day, A-Z index
│   ├── day01.md … day10.md
│   └── companions/
│       └── week02_companion.md … week07_companion.md
└── docs/
    ├── problem_inventory.md          every task, quiz item, quiz key and lecture erratum
    ├── clone_forbidden_entities.txt  the lectures' named cases (kept out of exercises)
    ├── verify_numbers.py             recomputes every numeric answer in the sketches
    ├── check_structure.py            checks the day and companion skeletons
    └── superpowers/{specs,plans}/    design spec and authoring plan (background only)
```

## Checking your work / tooling

Plain Python 3, no packages. Run from `foundations_sprint/`:

- `python3 docs/verify_numbers.py [stem …]` recomputes every numeric answer in the sketches. Each content file has its checks in `docs/checks/check_<stem>.py` (stems `day01` … `day10`, `week02` … `week07`); with no stem it runs them all.
- `python3 docs/check_structure.py` checks that every day and companion has its required sections and that every exercise has a hint plus a sketch (or a model paragraph with a weak-answer note).
- Symbols and units: [GLOSSARY.md](content/GLOSSARY.md), grouped by day, with a "lecture notation vs sprint notation" table and an A-Z index.

## Notes you should know

- **Assessment boundary.** The sprint teaches comprehension only. It contains nothing aimed at Assessment 1 and never drafts Portfolio text; that is this session's scope, with assessment work in its own session.
- **Lecture errors.** About 15 errors in the lectures (units, factors, conventions, one misstated theorem) are listed in [docs/problem_inventory.md](docs/problem_inventory.md) and corrected in each companion's §4. When a lecture number and the companion disagree, check the companion and cite a primary source.
- **Quiz key.** The inventory gives a key by option text for the Week 2-5 quizzes, and flags the questions whose wording is looser than the physics.

## Inventory row map

Every row of [docs/problem_inventory.md](docs/problem_inventory.md), and where the sprint covers it. "C4 §9" means the Week 4 companion, section 9; "Ex" is an exercise in that day file. Rows the sprint deliberately leaves alone say so.

**Writing tasks and activities (24 rows).**

| Week | Inventory row | Day file(s) | Companion section(s) |
|---|---|---|---|
| 1 | Explore: 200-word QT-benefit summary, 2+ publications | [Day 01](content/day01.md) F1, F3, M1, Ex 1.7; [Day 05](content/day05.md) checkpoint | none (Week 1 has no companion) |
| 1 | References page: intro post (background, which QT type) | not covered: orientation post, no moves needed; [Day 01](content/day01.md) module map lists the four types | none |
| 1 | Apply: one QT type + application, 200-300 words | [Day 01](content/day01.md) Ex 1.8 | none |
| 1 | Consolidate: 1-2 quantified advantages, 300 words | [Day 01](content/day01.md) Ex 1.6; M13 parts in [Day 09](content/day09.md); [Day 10](content/day10.md) capstone | none |
| 1 | Consolidate (optional): circuit simulator | [Day 08](content/day08.md) Lab: Quirk walkthrough (stand-in) | none |
| 2 | Apply: clock or magnetometer, 200-300 words | [Day 03](content/day03.md) Ex 3.9, 3.10 | [C2](content/companions/week02_companion.md) §1 |
| 2 | Consolidate: advantages vs classical limitation, 300 words | [Day 02](content/day02.md) M2-M3, Ex 2.8, 2.9; [Day 03](content/day03.md) M4-M5; [Day 05](content/day05.md) | [C2](content/companions/week02_companion.md) §1, §4, §5 (C2.4), §6 |
| 2 | Consolidate: reflection notes | listed only; nothing to teach (the confusion log in [STRATEGY](STRATEGY.md#7-confusion-log-template) is the nearest tool) | [C2](content/companions/week02_companion.md) §1 |
| 3 | Apply (+ live session 2): atom-interferometry application | [Day 04](content/day04.md) Ex 4.9 (stretch) | [C3](content/companions/week03_companion.md) §1 |
| 3 | Consolidate: matter-wave gain, 300 words | [Day 04](content/day04.md) M6-M7, Ex 4.10; [Day 05](content/day05.md) Ex 5.13 | [C3](content/companions/week03_companion.md) §1, §4, §5 (C3.4), §6 |
| 3 | End of week: submit Assessment 1 | out of scope by design (separate session); only the deadline and A1-window plan: [Deadlines](#deadlines), [Day 05](content/day05.md) spaced review | none |
| 4 | Apply: quantum-communication application | [Day 06](content/day06.md) Ex 6.8 | [C4](content/companions/week04_companion.md) §1 |
| 4 | Consolidate: QKD security gain and downsides, 300 words | [Day 06](content/day06.md) M8-M10, Ex 6.9; [Day 09](content/day09.md) Ex 9.8 (crypto angle) | [C4](content/companions/week04_companion.md) §1, §4K, §5 (C4.4), §6 |
| 4 | Consolidate (optional): QuVis BB84 simulation | [Day 06](content/day06.md) "Week 4 quiz and a QuVis pointer" (pointer only) | [C4](content/companions/week04_companion.md) §9 |
| 5 | Apply: a type of quantum simulation | [Day 07](content/day07.md) Ex 7.9 | [C5](content/companions/week05_companion.md) §1 |
| 5 | Consolidate: quantum vs classical numerical simulation, 300 words | [Day 07](content/day07.md) M11, Ex 7.10; M13 parts in [Day 09](content/day09.md) | [C5](content/companions/week05_companion.md) §1, §4, §5 (C5.4), §6 |
| 6 | Explore: limits of conventional computing, 200 words | [Day 07](content/day07.md) Ex 7.8 | [C6](content/companions/week06_companion.md) §1 |
| 6 | Apply: an aspect of quantum computing | [Day 08](content/day08.md) Ex 8.9 | [C6](content/companions/week06_companion.md) §1 |
| 6 | Consolidate: speed-up or new problem classes, 300 words | [Day 08](content/day08.md) M12.4; [Day 09](content/day09.md) M13, Ex 9.7, 9.8 | [C6](content/companions/week06_companion.md) §1, §4, §5 (C6.4), §6 |
| 6 | Consolidate (optional): puzzle game (The Qubit Factory) | [Day 08](content/day08.md) Lab (pointer) | [C6](content/companions/week06_companion.md) §9 |
| 7 | Explore: which QT spreads soonest; largest markets | [Day 10](content/day10.md) F2, "F3 again", Ex 10.5 (stretch) | [C7](content/companions/week07_companion.md) §1, §4D |
| 7 | Apply: one-page A4 fact sheet | [Day 10](content/day10.md) M14.3, Ex 10.3, 10.4 | [C7](content/companions/week07_companion.md) §1, §4A, §5 (C7.1) |
| 7 | Consolidate: benefit to your background, benefit/risk ratio | [Day 10](content/day10.md) M14.1-M14.2, Ex 10.1, 10.2, 10.4, 10.16 | [C7](content/companions/week07_companion.md) §1, §5 (C7.2-C7.4), §6 |
| 7 | End of week: submit Assessment 2 (Portfolio) | not drafted by design (assessment work is a separate session); [Day 10](content/day10.md) "What next" covers the writing plan | [C7](content/companions/week07_companion.md) §1 item 4 |

**Quizzes (one block per week; Weeks 1, 6 and 7 have none).**

| Week | Quiz rows | Day file(s) | Companion section(s) |
|---|---|---|---|
| 2 | Q1-Q4 (magnetometers, timing) | [Day 03](content/day03.md) Read next (companion pointer) | [C2](content/companions/week02_companion.md) §1 |
| 3 | Q1-Q4 (inertial forces, spring, magnetometry, timing; Q1 flagged) | [Day 04](content/day04.md) M7.8 "Week 3 quiz" | [C3](content/companions/week03_companion.md) §1 |
| 4 | Q1-Q4 (encryption, QKD truths, qubit, quantum cryptography; Q4 flagged) | [Day 06](content/day06.md) M8.3, M9.4-M9.5, "Week 4 quiz" | [C4](content/companions/week04_companion.md) §1, §4F, §4K |
| 5 | Q1-Q4 (applications, computer vs simulator, concept, limitation; Q2-Q4 flagged) | [Day 07](content/day07.md) M11.3-M11.4, "Week 5 quiz pointers" | [C5](content/companions/week05_companion.md) §1, §4K |

**Lecture errors (15 rows).**

| Week | Line | Error | Day file(s) | Companion section(s) |
|---|---|---|---|---|
| 1 | L52 | QKD "uses entangled particles" | [Day 01](content/day01.md) Week 1 decode; [Day 06](content/day06.md) M9.5; [Day 05](content/day05.md) Ex 5.12 | none (Week 1) |
| 1 | L70 | "multiple calculations simultaneously" | [Day 01](content/day01.md) Week 1 decode; [Day 08](content/day08.md) M12.4; Day 05 Ex 5.12; Day 10 Ex 10.14 | [C6](content/companions/week06_companion.md) §4F |
| 2 | L74 | "T√Hz" | [Day 02](content/day02.md) M2.3; [Day 03](content/day03.md) M5.4; Day 05 Ex 5.9 | [C2](content/companions/week02_companion.md) §3, §4.2 |
| 2 | L82 vs L137 | NV sensitivity inconsistent | [Day 03](content/day03.md) M5.4 | [C2](content/companions/week02_companion.md) §4.10 |
| 2 | L94 | "amplitude increases by r²" | [Day 02](content/day02.md) M3.2; Day 05 Ex 5.9 | [C2](content/companions/week02_companion.md) §4.3 |
| 3 | L105-110 | $\Phi = k_\text{eff}a\tau^2$, $\tau = 2T$ | [Day 04](content/day04.md) M7.4; Day 05 Ex 5.10; Day 10 Ex 10.9 | [C3](content/companions/week03_companion.md) §3, §4E |
| 3 | L91 | chirp "α = g" | [Day 04](content/day04.md) M7.4; Day 05 Ex 5.10 | [C3](content/companions/week03_companion.md) §4D |
| 3 | L135 | spring sensitivity ∝ 1/T² | [Day 04](content/day04.md) M7.8; Day 05 Ex 5.10 | [C3](content/companions/week03_companion.md) §4K |
| 3 | L99 vs L139 | corner-cube noise 5 vs 50 µGal/√Hz | [Day 04](content/day04.md) M7.8; Day 05 Ex 5.11 | [C3](content/companions/week03_companion.md) §4J |
| 4 | L152 | repeaters "amplify" | [Day 06](content/day06.md) M10.3, Ex 6.10; Day 10 Ex 10.12 | [C4](content/companions/week04_companion.md) §4H; [C7](content/companions/week07_companion.md) §4E |
| 5 | L55 | Table 5.2 rows 840 kB, 880 GB | [Day 07](content/day07.md) M11.1 | [C5](content/companions/week05_companion.md) §4C |
| 6 | L150 | Shor success condition garbled | [Day 09](content/day09.md) M13.2 | [C6](content/companions/week06_companion.md) §4H |
| 6 | L184 | threshold theorem stated backwards | [Day 09](content/day09.md) M13.5; Day 10 spaced review | [C6](content/companions/week06_companion.md) §4J |
| 6 | L131 vs L139 | database search "exponential" | [Day 09](content/day09.md) M13.1; [Day 08](content/day08.md) M12.4 | [C6](content/companions/week06_companion.md) §4F |
| 6 | L162/L170/L188 | three fidelity sets | [Day 09](content/day09.md) M13.4 | [C6](content/companions/week06_companion.md) §4I |
