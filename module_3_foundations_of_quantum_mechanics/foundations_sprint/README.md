# Module 3 Foundations Sprint

This is a text-only learning path for Module 3, Foundations of Quantum Mechanics. It is written for a student whose maths is rusty and who needs to follow and solve the problems in Weeks 2 to 7. It has seven Foundation days that teach the named maths "moves" the module's problems actually use (complex numbers, bra-ket linear algebra, 2x2 eigenproblems, a small set of integrals, the oscillator toolkit, tensor products). It also has a five-file Physics Sprint (classical energy, waves, springs, magnetism and spin, measurement) that supplies the physics the lectures assume, and six Week Companions that decode each week's lecture, expand the skipped steps, and link back to the moves. Together this is about 32.5 hours: 7 x 3.5 h of maths plus about 8 h of physics (five files of roughly 1.5 to 2 h each). One [glossary](content/GLOSSARY.md) indexes all the notation. Nothing here needs code or a lab.

## The seven days (maths spine)

| Day | Focus | Feeds Week | Companion |
|---|---|---|---|
| [1](content/day01.md) | Algebra and trig triage; complex numbers (conjugate, modulus, e^{i theta}); double-angle identities | 2, 3 | none |
| [2](content/day02.md) | Vectors, matrices, bra-ket notation, inner products, orthonormal bases, basis expansion | 2, 3, 4 | [Week 2](content/companions/week02_companion.md) (Postulate 1) |
| [3](content/day03.md) | Operators; 2x2 eigenvalues and eigenvectors; Hermitian and adjoint rules; Pauli matrices | 3, 4, 6 | [Week 3](content/companions/week03_companion.md), [Week 6](content/companions/week06_companion.md) (concept) |
| [4](content/day04.md) | Functions as vectors; exponential and sine integrals; integration by parts; Gaussian integral; normalisation; expectation values | 2, 3, 5 | [Week 2](content/companions/week02_companion.md) (Postulate 2), [Week 3](content/companions/week03_companion.md) |
| [5](content/day05.md) | Measurement postulate (probabilities, collapse); Schrodinger equation; stationary states; particle in a box | 4 (Assessment 1) | [Week 4](content/companions/week04_companion.md) |
| [6](content/day06.md) | Oscillator: substitution to xi, Gaussian moments, ladder operators, commutators, uncertainty | 5 | [Week 5](content/companions/week05_companion.md) |
| [7](content/day07.md) | Tensor products; product-state test; partial collapse; then a mixed mock problem set across all weeks | 7 | [Week 7](content/companions/week07_companion.md) |

Week 6 needs no new maths. Its companion is a concept and essay guide for the Stern-Gerlach portfolio piece.

## Combined timetable

Each physics file takes about 1.5 to 2 h (see the Physics Sprint section) and sits beside a maths day. Days 3 and 5 stay maths-only because they are the heaviest.

| Day | Maths | Physics | Day total | Deadline link |
|---|---|---|---|---|
| 1 | [Day 1](content/day01.md) (3.5 h) | [P1](content/physics/P1.md) Energy and classical state | ~5 h | Weeks 2-4, Assessment 1 |
| 2 | [Day 2](content/day02.md) (3.5 h) | [P2](content/physics/P2.md) Waves, light, birth of QM | ~5 h 15 min | Weeks 1, 3, 4, Assessment 1 |
| 3 | [Day 3](content/day03.md) (3.5 h) | none | 3.5 h | Assessment 1 |
| 4 | [Day 4](content/day04.md) (3.5 h) | [P3](content/physics/P3.md) Springs, standing waves, confinement | ~5 h 5 min | Weeks 4-5 |
| 5 | [Day 5](content/day05.md) (3.5 h) | none | 3.5 h | Assessment 1 (Thursday of Week 4, 17:00 UK) |
| 6 | [Day 6](content/day06.md) (3.5 h) | [P4](content/physics/P4.md) Magnetism and spin | ~5 h 10 min | Weeks 6-7 |
| 7 | [Day 7](content/day07.md) (3.5 h) | [P5](content/physics/P5.md) Measurement, interpretations, quantum tech | ~5 h 5 min | Week 7, Portfolio (Monday of Week 8, 10:00 UK) |

Total: about 32.5 hours (24.5 h maths plus about 8 h physics: P1 1 h 30 + P2 1 h 45 + P3 1 h 35 + P4 1 h 40 + P5 1 h 35 = 8 h 5 min).

## Physics Sprint

The lectures lean on physics they never spell out: classical energy, waves and interference, a mass on a spring, magnetic moments, polarisation and interpretations. The Physics Sprint gives just that background, so the lectures can be followed, and ends every idea with a "quantum bridge" from the classical version to the quantum one.

- [P1 — Energy and Classical State](content/physics/P1.md): Newtonian state, force from a potential, classical energy, SI units and eV, and the bridge to the Hamiltonian.
- [P2 — Waves, Light and the Birth of Quantum Mechanics](content/physics/P2.md): waves, interference, the complex plane wave, Planck and de Broglie, and the bridge to $e^{ikx}$ and discrete spectra.
- [P3 — Springs, Standing Waves and Confinement](content/physics/P3.md): the classical spring, standing waves, quantised energies, zero-point energy.
- [P4 — Magnetism and Spin](content/physics/P4.md): magnetic moments, field gradients, the classical prediction for Stern-Gerlach, and spin as a two-beam result.
- [P5 — Measurement, Interpretations and Quantum Technology](content/physics/P5.md): polarisation as a two-state system, entanglement at concept level, neutral interpretations, key distribution, and a physical-reasoning kit.

Each file is roughly 1.5 to 2 h: 10 min warm-up, 40 to 55 min moves, 30 min exercises, 10 min apply and confusion log. Per file: P1 1 h 30 (moves 40), P2 1 h 45 (moves 55), P3 1 h 35 (moves 45), P4 1 h 40 (moves 50), P5 1 h 35 (moves 45). Priority rule: P1 and P2 matter before Assessment 1 (Thursday of Week 4, 17:00 UK). P3 is best done before Week 5. P4 and P5 can slide later without hurting Assessment 1, because Weeks 6 and 7 are a few weeks away; the Portfolio is due Monday of Week 8, 10:00 UK.

## How to use it with the course

Each maths day is about 3.5 hours, in a fixed order:

1. **Warm-up (20 min).** Five closed-book retrieval questions from earlier days. Day 1 opens with a diagnostic instead.
2. **Moves (60 min).** Learn the day's named moves, each a short technique with a worked clone.
3. **Exercises (90 min).** Make a cold attempt first. Only then read the hint, and only after that the solution sketch.
4. **Apply (40 min).** Take the day's moves into the matching lecture using the companion named in the table.
5. **Confusion log (10 min).** Note each symbol, step or concept that stayed unclear, and set up tomorrow. A template is in [STRATEGY.md](STRATEGY.md).

## Suggested weekly rhythm

You have just finished Week 1 and are starting Week 2. This is a suggested rhythm, not a rule. The fast path is to do all seven days in seven consecutive days if time allows.

- **Days 1 and 2:** before or alongside Week 2's task. They cover the complex numbers, bra-ket notation and inner products that Week 2 uses at once.
- **Days 3 and 4:** spread across Weeks 2 and 3, alongside the Week 2 and Week 3 companions.
- **Day 5:** before Assessment 1, which is due Thursday of Week 4 at 17:00 UK. Assessment 1 draws mainly on Days 1 to 5.
- **Days 6 and 7:** before Weeks 5 and 7 respectively, and before the Portfolio, which is due Monday of Week 8 at 10:00 UK (2100 words). The Portfolio draws on all seven days and the companions.

## Directory map

```
foundations_sprint/
├── README.md                    this file
├── STRATEGY.md                  learning strategy, mistakes list, five-pass protocol, six-steps stand-in, confusion log
├── content/
│   ├── GLOSSARY.md              notation-first glossary, grouped by day
│   ├── day01.md ... day07.md    the seven Foundation days
│   ├── physics/
│   │   └── P1.md ... P5.md      the five Physics Sprint files
│   └── companions/
│       └── week02_companion.md ... week07_companion.md
└── docs/superpowers/            design spec and authoring plan (background only)
```

## Reading each lecture: the five-pass protocol

For each week, read the quiz and task problems first (Pass 0, 10 min). Then read the companion summary and skim the lecture for structure only (Pass 1, 20 min). Next read the lecture with the companion's notation decoder open, keeping a confusion log (Pass 2, 45 min). Then re-derive the week's key result from memory, closed book (Pass 3), and finally clone a worked problem, solve a fresh variant and explain it aloud in three sentences (Pass 4). The full protocol, with a worked example, is in [STRATEGY.md](STRATEGY.md#five-pass-lecture-protocol).

## Notes you should know

- **The six-steps template is a stand-in.** The university's own "six steps" page is not in the exported course files. The write-up format in [STRATEGY.md](STRATEGY.md#six-steps-write-up-stand-in) is a clearly labelled substitute, not the university's text. Use the university's version when you have it.
- **Academic integrity.** The days and companions teach method, and they use different objects (functions, matrices, numbers, states) from the assessed problems. Model answers are the university's to provide. Never submit anything from here as your own solution.
- **Lecture quirks.** Some quirks in the course lectures (odd notation choices, skipped steps, apparent inconsistencies) are flagged inside the companions where they arise.
- **More depth later.** If you want more depth, you can attach your existing linear algebra and physics fundamentals courses at `~/git_clone/learning_path/linear_algebra` and `~/git_clone/learning_path/physics_fundamental` (plain text paths). The sprint does not depend on them.
