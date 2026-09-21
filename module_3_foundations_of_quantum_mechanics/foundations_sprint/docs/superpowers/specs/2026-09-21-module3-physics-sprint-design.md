# Module 3 Physics Sprint — Design Spec (addendum)

**Date:** 2026-09-21
**Location:** `module_3_foundations_of_quantum_mechanics/foundations_sprint/`
**Extends:** `2026-09-21-module3-foundations-sprint-design.md` (the maths spine, Days 1–7). Read that spec first; this addendum only adds what is new and states where it changes existing files.
**Duration:** five physics files (P1–P5), P1 1:30, P2 1:45, P3 1:35, P4 1:40, P5 1:35 (8 h 05), interleaved with the seven maths days → ~32.5 h total (was ~25 h).

## Purpose & Goals

The maths spine treats Module 3 mostly as linear algebra and calculus. That was the right reading of the *problems*, but the *lectures* also lean on unstated physics: classical energy and momentum, waves and interference, a mass on a spring, magnetic moments in a field, photons, and the history and interpretation of quantum mechanics. The learner has "very little" school physics left but learns fast, and wants **only what is needed to follow and pass this module** — not physics for its own sake.

The Physics Sprint gives that background in five short, move-based files, each ending with **the bridge from the classical idea to its quantum version**, because that bridge is what the lectures skip.

**Scope decision on "enhancement":** the learner asked for "foundation and enhancement" and, asked what enhancement means, said "just enough to finish this module". So enhancement is limited to material that (a) the lectures explicitly discuss, (b) supports the Week 6 essay, Week 4 discussion task and Portfolio, or (c) earns method marks in problem sets — namely experiments and interpretations, a light quantum-technology layer already in the syllabus (Week 7 key distribution), and a **physical-reasoning kit**. A general "further reading" map is out of scope beyond a one-line pointer to the learner's existing `physics_fundamental` course.

## Success Criteria

Without notes, the learner can:

1. Convert between SI units and eV, and use dimensional analysis to sanity-check a formula.
2. Compute classical kinetic, potential and total energy for a simple system and explain why Ĥ is "the total-energy operator" (Week 1 §1.1, Hamiltonian).
3. Relate wavelength, frequency, wavenumber and angular frequency; compute the de Broglie wavelength λ = h/p for a given particle; describe the double-slit result and why probability *amplitudes* (not probabilities) add.
4. State E = hf and the photoelectric/blackbody evidence for quantisation, and explain discrete hydrogen spectral lines as evidence for discrete energy eigenvalues (Week 3 §3.1).
5. Derive p = ħk and E = ħ²k²/2m for e^{ikx} and connect them to classical E = p²/2m (Week 4 §4.2); explain qualitatively why confinement gives standing waves and quantised energies E_n ∝ n², and why the ground state has non-zero energy.
6. Describe a classical harmonic oscillator (V = ½kx², ω = √(k/m), energy exchange between kinetic and potential) and contrast its probability distribution with the quantum one (Week 5 §5.1).
7. Explain the Stern-Gerlach experiment physically: a magnetic moment in an inhomogeneous field feels a force; two beams mean quantised spin; predict qualitatively the outcomes of sequential magnets (Week 6).
8. Treat photon polarisation as a two-state system, show Malus's law cos²θ is the same rule as |c|², describe entanglement and the EPR/Bell debate and the main interpretations in neutral language, and outline key distribution at lecture level (Weeks 3, 6, 7).
9. Apply a physical-reasoning check — units, order of magnitude, limiting case — to a quantum-mechanics result.

## Constraints & Environment

Everything in the parent spec's *Constraints & Environment* still applies. Additionally:

- **Source fidelity:** physics claims and equations must agree with the module's lecture files. Constants given in the lecture (ħ = 1.055×10⁻³⁴ J·s) are used as given; other constants (h, c, e, m_e, eV↔J, μ_B if used) are standard values rounded to 4 significant figures and labelled **"(standard value)"**.
- **No claims beyond what was read:** the two PDFs in `../exteral_resources/` (Susskind; Collins, *The Many Interpretations of Quantum Mechanics*) are named as optional reading but must not be summarised unless actually read by the author.
- **Integrity:** as before — nothing solves or partially solves a real Assessment 1, Portfolio or Task problem (parent plan Global Constraints list). The Week 6 essay guidance stays a structure only; P4/P5 must not pre-write essay content or the Week 4 misconceptions post.
- **Exercises:** every exercise ships a **Hint** and a **Solution sketch**. Numerical exercises state units and show the units check.
- **Pure-science, text-only** (no simulations).
- **Anonymity:** no learner name, email or handle in any content file.
- **Authoring branch:** local scratch branch `authoring/module3-physics-sprint`; commits only touch `foundations_sprint/`; never pushed; torn down before handoff.

## Strategy

Same principle as the maths spine: **problem-first, move-based, retrieval over rereading.** A physics "move" is a 10-minute named idea with a formula, its units, a worked example, and its quantum bridge. Chosen over alternatives:

- *Rejected — physics blocks inside every maths day:* would re-open and re-review seven reviewed files and push days to ~5 h.
- *Rejected — physics primer before Day 1:* delays the maths the learner needs first for Assessment 1.
- *Chosen — separate interleaved Physics Sprint:* new files only, existing maths files stay stable, the README owns the combined timetable.

## Physics Move Registry (IDs fixed; used by plan, files, glossary)

| ID | Move | File |
|---|---|---|
| P1.1 | Newtonian state: position, velocity, acceleration, momentum p = mv; determinism (Week 1 §1.1) | P1 |
| P1.2 | Force from potential, F = −dV/dx; Newton's second law as a differential equation | P1 |
| P1.3 | Energy: kinetic p²/2m, potential V, total E = p²/2m + V (the classical Hamiltonian) | P1 |
| P1.4 | SI units, eV, and the size of ħ and h; dimensional analysis | P1 |
| P1.5 | Bridge: classical state (x, p) vs quantum state ψ; Ĥ = p̂²/2m + V with p̂ = −iħ ∂/∂x | P1 |
| P2.1 | Waves: amplitude, wavelength λ, frequency f, wavenumber k = 2π/λ, ω = 2πf, wave speed | P2 |
| P2.2 | Superposition and interference; two-source/double-slit pattern | P2 |
| P2.3 | Complex plane wave e^{i(kx−ωt)}; why physicists use it | P2 |
| P2.4 | Planck E = hf; blackbody and photoelectric effect as the first evidence of quanta; photon momentum p = h/λ | P2 |
| P2.5 | de Broglie λ = h/p; wave–particle duality; electron double-slit and the role of amplitudes | P2 |
| P2.6 | Bridge: e^{ikx} has p = ħk and E = ħ²k²/2m (Week 4 §4.2); discrete spectral lines and E_n (Week 3 §3.1) | P2 |
| P3.1 | Classical spring: F = −kx, ω = √(k/m), x(t), energy ½mv² + ½kx² sloshing back and forth | P3 |
| P3.2 | Classical probability distribution of a mass on a spring (where it spends its time) | P3 |
| P3.3 | Standing waves on a string and confinement ⇒ quantised wavelengths ⇒ quantised energies (box, E_n ∝ n²) | P3 |
| P3.4 | Zero-point energy and the wave form of the uncertainty principle (Δx·Δk ≳ 1/2) | P3 |
| P3.5 | Bridge: Week 5 oscillator energies ħω(n+½); why the quantum ground state is not "at rest" | P3 |
| P4.1 | Magnetic field, magnetic moment, torque, energy of a dipole in a field | P4 |
| P4.2 | Force on a dipole needs a field **gradient** (why Stern-Gerlach uses an inhomogeneous field) | P4 |
| P4.3 | Classical angular momentum L = r × p and its continuous prediction for the deflection | P4 |
| P4.4 | Spin as intrinsic angular momentum; S_z = ±ħ/2 (convention flagged); two beams instead of a smear | P4 |
| P4.5 | Sequential Stern-Gerlach at the level of Week 6 §6.2–6.4; interference; link to spin-½ states and Pauli matrices (Day 3) | P4 |
| P5.1 | Photon polarisation as a two-state system; Malus's law cos²θ = Born rule |c|² | P5 |
| P5.2 | Entanglement, EPR and Bell at concept level; "correlated ≠ communicating" (link Day 7 Move 7.5) | P5 |
| P5.3 | Interpretations in neutral language (Copenhagen and the alternatives named in Week 3 §3.4) | P5 |
| P5.4 | Quantum technology at lecture level: key distribution (Week 7 §7.4), spin sensing (Week 6) | P5 |
| P5.5 | Physical-reasoning kit: units check, order of magnitude, limiting case, symmetry check, worked on QM results | P5 |

## Curriculum and Combined Timetable

Each P-file is planned at about 1.5 h (the honest per-file totals came out after authoring; see the Duration line and the timetable below): **10 min** warm-up (retrieval on earlier P-files and key maths moves) · **40 min** moves · **30 min** exercises · **10 min** apply/bridge and confusion log.

| Day | Maths (existing) | Physics (new) | Day total | Deadline link |
|---|---|---|---|---|
| 1 | Day 1 (3.5 h) | **P1** Energy and classical state | 5:00 | Weeks 2–4, Assessment 1 |
| 2 | Day 2 (3.5 h) | **P2** Waves, light, birth of QM | 5:15 | Weeks 1, 3, 4, Assessment 1 |
| 3 | Day 3 (3.5 h) | — | 3:30 | Assessment 1 |
| 4 | Day 4 (3.5 h) | **P3** Springs, standing waves, confinement | 5:05 | Weeks 4–5 |
| 5 | Day 5 (3.5 h) | — | 3:30 | Assessment 1 (Thu Week 4, 17:00 UK) |
| 6 | Day 6 (3.5 h) | **P4** Magnetism and spin | 5:10 | Weeks 6–7 |
| 7 | Day 7 (3.5 h) | **P5** Measurement, interpretations, quantum tech | 5:05 | Week 7, Portfolio (Mon Week 8, 10:00 UK) |

Priority rule: P1–P2 matter before Assessment 1; P3 before Week 5; P4–P5 can slide later without hurting Assessment 1, because Weeks 6–7 are about three weeks away. Days 3 and 5 stay maths-only (the heaviest).

## Directory Layout (additions in bold)

```
foundations_sprint/
├── README.md                      # MODIFIED: combined maths+physics timetable, physics section
├── STRATEGY.md                    # MODIFIED (small): physics move / bridge principle + reasoning kit pointer
├── content/
│   ├── GLOSSARY.md                # MODIFIED: new "Physics P1–P5" sections + index entries
│   ├── day01.md … day07.md        # MODIFIED (one-line "Physics pair" pointer on days 1, 2, 4, 6, 7 only)
│   ├── physics/                   # NEW
│   │   └── P1.md … P5.md
│   └── companions/                # unchanged
└── docs/superpowers/{specs,plans}/
```

## Physics File Skeleton

```markdown
# P<N> — <Title>

## Why this matters
<which lecture passages / weeks this unlocks; what goes wrong without it>

## Warm-up (retrieval, 5 questions; answers folded at the bottom)
<from earlier P-files and key maths moves>

## Moves
### Move P<N>.<k> — <name> (<minutes>)
<statement in words, formula, units, one worked example on a NEW object, then "Quantum bridge:" line>

## Exercises
1. <task> — **Hint:** … — **Solution sketch:** …   (numerical items show the units check)

## Apply to the lecture
<exact lecture sections to re-read, which companion sections, what to look for>

## Anti-patterns / Common mistakes
<2–3 bullets>

## Confusion log
| Where | Symbol or idea | What I think | What it actually means | Resolved? |
```

## Glossary, README, pointers

- **GLOSSARY.md** gains sections "Physics P1 … P5" in the same entry format (term/symbol · say it as · one plain-English sentence · tiny example · see · confused-with). The A–Z index gains the new entries; the explicit-anchor scheme must be kept (`<a id="…"></a>`), and the file's index-link/anchor self-check must still pass.
- **README.md** gets the combined timetable above, a "Physics Sprint" section, and links to the new files.
- **STRATEGY.md** gets a short paragraph: every physics idea is learned with its quantum bridge; the reasoning kit is the physics half of the "check" step of the six-steps stand-in.
- **Day pointers:** one line at the top of days 1, 2, 4, 6, 7: "Physics pair for today: [P<N>](physics/P<N>.md) (~1.5 h)." Nothing else in the day files changes.

## Verification (per parent spec, plus)

- V1 (hint = sketch counts, non-zero) extended to `content/physics/P*.md`.
- V2 (no learner identity), V3 (no code/labs), V4 (no placeholders) over the whole tree.
- Link check over the whole tree, including the glossary anchor self-check, and README links to the five new files.
- **Physics-specific:** every constant used is either from the lecture or labelled "(standard value)"; every numerical exercise shows a units check; every equation quoted from a lecture matches the lecture text; every P-file names its lecture source sections.
- Integrity sweep: no P-file solves or partially solves a real course task or Portfolio instance; P4/P5 contain no essay text.
