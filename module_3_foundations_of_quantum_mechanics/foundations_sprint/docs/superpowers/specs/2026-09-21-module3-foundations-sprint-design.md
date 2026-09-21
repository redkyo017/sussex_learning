# Module 3 Foundations Sprint — Design Spec

**Date:** 2026-09-21
**Location:** `module_3_foundations_of_quantum_mechanics/foundations_sprint/`
**Duration:** 7 days, ~3.5 h/day (~25 h total), plus six Week Companions used alongside the course

## Purpose & Goals

The learner is a Sussex MSc Quantum Technology student, very rusty on school maths and physics, who has just finished Week 1 of Module 3 (Foundations of Quantum Mechanics). The university lectures are hard for them to follow. This path has two layers:

1. **Foundation Sprint** — teaches only the maths "moves" that Weeks 2–7 problems actually use, in the shortest workable form.
2. **Lecture Mastery Method** — a reusable reading protocol plus a Week Companion for each of Weeks 2–7 that decodes the lecture, expands skipped derivations, and rehearses the week's problem types.

Mastery means the learner can read a Module 3 lecture, follow every step, and solve the week's task-style problems on a blank page in the course's "six steps" write-up format.

**Why the lectures are hard (diagnosis that drives the design):**
- postulate-first, intuition-never;
- dense notation with no decoding (ψ*ψ, d³**r**, ê_x, Ô, [â, â†]);
- derivations with steps skipped;
- maths and physics arriving in the same paragraph.

**Key finding from the syllabus audit:** the problems are mostly *linear algebra in Dirac notation* (bra-ket proofs, 2×2 eigenproblems, adjoints, tensor products), with calculus limited to exponential/sine integrals, integration by parts and Gaussians. So bra-ket linear algebra is taught early (Day 2), not late.

## Success Criteria

Without notes, the learner can:

1. Manipulate complex numbers (conjugate, modulus, e^{iθ}) and use trig double-angle identities.
2. Write and manipulate kets, bras and inner products; expand a state in an orthonormal basis; prove basic bra-ket identities from the inner-product axioms.
3. Find eigenvalues and eigenvectors of a 2×2 matrix; use Pauli matrices; state and use Hermitian and adjoint rules, including (QR)† = R†Q†.
4. Normalise a wave function; evaluate exp/sin/Gaussian integrals and expectation values; judge whether a function is a physically acceptable wave function.
5. Turn a state expansion into measurement probabilities |c_n|², apply collapse, and state the time-independent Schrödinger equation with stationary states.
6. Solve the oscillator ground-state problems (verify Hψ = Eψ, normalise, compute ⟨x²⟩, σ_x, σ_p, and the uncertainty product) and use ladder operators and commutators.
7. Build tensor products, test for product states, and compute partial collapse in a two-qubit state.
8. Apply the five-pass lecture-reading protocol to any lecture and produce a confusion log.
9. Write solutions in the course's "six steps to problem solving" structure.

## Constraints & Environment

- **Path type:** pure science. Text content only — no `code/`, `labs/` or simulations (learner chose text-only).
- **Every exercise ships with a hint and a solution sketch.** No bare problems.
- **Academic integrity:** companions teach method and understanding. They never contain worked solutions to the *actual* Assessment 1 or Portfolio problems. Worked clones use **different numbers and functions** than the course's task/portfolio problems. Model answers are the university's to provide.
- **Sources:** all module material is quoted from the local exports in `module_3_foundations_of_quantum_mechanics/week_N/`; problem *types* are referenced by week and problem number.
- **No credentials, no git pushes.** Authoring uses a local scratch branch `authoring/module3-foundations-sprint`; it is torn down before handoff. Commits only touch `foundations_sprint/`. The learner's unrelated working-tree edits must remain untouched.
- **Submission anonymity:** nothing in the path bears the learner's name (Sussex assessments are anonymous by candidate number).

## Strategy (the core design decision)

**Chosen: problem-first reverse engineering.** Mine every task/portfolio/quiz item for the exact maths moves; teach each move as a named 10-minute technique; drill on a cold attempt first; order days by deadline (Assessment 1 due Thursday of Week 4) then by dependency.

**Rejected:**
- *Weekly just-in-time primers* — too gentle; with rusty maths the learner meets each tool in the same week they must use it.
- *Compressed bottom-up prerequisites* — the traditional path in a smaller box; 80% of the time goes on material the module never touches. The learner's existing `linear_algebra` and `physics_fundamental` courses already cover that depth.

**Principles (go in `STRATEGY.md`):**
1. Learn moves, not subjects.
2. Problems before theory (cold attempt → fail → explanation lands).
3. Retrieval over rereading (5 closed-book questions open each day).
4. Six-steps write-up format from Day 1.

**Mistakes that waste 80% of beginners' time (go in `STRATEGY.md`):**
- rebuilding all of calculus/linear algebra "properly" first;
- watching and rereading instead of solving;
- skipping the boring algebra and then failing at the same step repeatedly;
- treating ψ as a wave picture only and missing that the maths is linear algebra;
- memorising formulas without checking normalisation, units and limiting cases;
- confusing a bra with its ket, or forgetting complex conjugation in inner products;
- reading solutions before a real attempt.

**Lecture reading protocol (five passes, go in `STRATEGY.md`):**
- *Pass 0 (10 min):* read the quiz and task problems first.
- *Pass 1 (20 min):* read the companion summary and picture; skim the lecture for structure only.
- *Pass 2 (45 min):* read the lecture with the companion's notation decoder open; keep a confusion log (symbol / step / concept).
- *Pass 3 (closed book):* re-derive the week's key result from memory; failures are the gaps to fix.
- *Pass 4:* clone a worked problem, solve a fresh variant, explain aloud in three sentences (Feynman check).

## Curriculum

Each day ≈ 3.5 h: **20 min** retrieval warm-up · **60 min** moves (learn) · **90 min** problem drills (cold attempt first) · **40 min** apply to the week's lecture via the companion · **10 min** confusion log + tomorrow's setup.

| Day | Moves taught | Feeds | Companion use |
|---|---|---|---|
| 1 | Algebra/trig triage; complex numbers (conjugate, modulus, e^{iθ}); double-angle identities | W2, W3 | — |
| 2 | Vectors, matrices, **bra-ket notation**, inner products, orthonormal bases, basis expansion | W2 P1, W3 P1, W4 P1 | W2 §Postulate 1 |
| 3 | Operators; 2×2 eigenvalues/eigenvectors; Hermitian and adjoint rules; Pauli matrices | W3 P2, W4 P2, W6 | W3, W6 (concept) |
| 4 | Functions as vectors; exp/sin integrals; integration by parts; Gaussian integral; normalisation; expectation values | W2 P3, W3, W5 | W2 §Postulate 2, W3 |
| 5 | Measurement postulate (|c|², collapse); Schrödinger equation; stationary states; particle in a box | W4 → **Assessment 1** | W4 |
| 6 | Oscillator: substitution ξ = x√(mω/ħ); Gaussian moments; ladder operators; commutators; uncertainty | W5 | W5 |
| 7 | Tensor products; product-state test; partial collapse; then a mixed mock problem set across all weeks | W7 | W7 |

Week 6 needs no new maths; its companion is a concept and essay guide for the Stern-Gerlach portfolio piece.
Assessment 1 (Thursday Week 4, 17:00 UK) draws mainly on Days 1–5; Assessment 2 Portfolio (Monday Week 8, 10:00 UK, 2100 words) draws on all days and the companions.

### Companion ← Day dependencies

| Companion | Built on |
|---|---|
| Week 2 | Days 1, 2, 4 |
| Week 3 | Days 2, 3, 4 |
| Week 4 | Days 3, 5 |
| Week 5 | Days 4, 6 |
| Week 6 | Day 3 (Pauli) + concept notes |
| Week 7 | Days 2, 3, 7 |

## Directory Layout

```
foundations_sprint/
├── README.md                      # quickstart, 7-day map, companion map, how to use
├── STRATEGY.md                    # top-1% strategy, mistakes list, five-pass reading protocol
├── content/
│   ├── GLOSSARY.md                # notation-first, grouped by day, A–Z index, links to day + lecture section
│   ├── day01.md … day07.md        # Foundation Sprint days
│   └── companions/
│       └── week02_companion.md … week07_companion.md
└── docs/superpowers/
    ├── specs/                     # this file
    └── plans/                     # implementation plan
```

No `code/` or `labs/` (pure science, text-only).

## Content Day Skeleton

```markdown
# Day N — <Title>

## Why this matters
<one short paragraph: which lecture steps and problems this unlocks>

## Warm-up (retrieval, 5 questions from previous days, closed book)
<questions; answers folded at the bottom of the file>

## Moves
### Move N.1 — <name>
<10-minute technique: statement, why it works, one worked example>

## Core concepts
<short intuition + notation decoded>

## Exercises
1. <task> — **Hint:** <hint> — **Solution sketch:** <sketch>

## Apply to the lecture
<which companion sections to read next; what to look for>

## Anti-patterns / Common mistakes
<2–3 bullets>

## Confusion log
<empty table: symbol / step / concept>
```

## Week Companion Skeleton

```markdown
# Week N Companion — <Topic>

## What this week is really saying
<plain English + physical picture>

## Notation decoder
| Symbol | Say it as | Means | Tiny example |

## Skipped steps, expanded
<the lecture's derivations with every step justified>

## Moves used this week
<list, each linked to the day that teaches it>

## Worked clones
<worked problems of the same TYPE as the week's task/portfolio problems, different numbers/functions>

## Retrieval questions
<quiz-style; each notes the misconception it traps>

## Six-steps write-up template
<the course format applied to this week's problem type>
```

## Glossary Skeleton

- Top: A–Z index.
- Body: sections grouped **by the day that introduces the term**.
- Each entry: term/symbol · say it as · plain-English meaning · tiny example · "see Day N / Week N §x" · optional **Commonly confused with:** flag.

## Verification (Phase 3 checks)

Each check's scope must match its rule's scope (per `skill.md`):

- Every `## Exercises` entry has both `**Hint:**` and `**Solution sketch:**` — `grep -rc` across `content/`.
- No worked solution to a real course problem: manual check per companion against the week's content file.
- No learner name anywhere: `grep -ril` over the whole tree.
- Every glossary term used in a day file appears in `GLOSSARY.md`.
- When a check fails across *every* file, suspect the check first.
