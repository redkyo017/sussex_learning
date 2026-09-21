# Module 3 Foundations Sprint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author a text-only learning path (7 Foundation days, 6 Week Companions, glossary, strategy, README) that gets a maths-rusty MSc student able to follow and solve Module 3 (Foundations of Quantum Mechanics) Weeks 2–7.

**Architecture:** Problem-first reverse engineering. Each day teaches named maths "moves" (fixed IDs below) that the module's problems use. Each Week Companion decodes one week's lecture and links back to the moves. One glossary, notation-first, indexes everything.

**Tech Stack:** Markdown with LaTeX (`$…$`, `$$…$$`), matching the existing week files. No code, no labs.

**Spec:** `foundations_sprint/docs/superpowers/specs/2026-09-21-module3-foundations-sprint-design.md` (read it first; it is the source of truth for structure, skeletons and success criteria).

All paths below are relative to `module_3_foundations_of_quantum_mechanics/foundations_sprint/` unless they start with `week_` or `module_`, which are relative to `module_3_foundations_of_quantum_mechanics/` (the local exports).

## Global Constraints

- **Path type:** pure science, text only. Do NOT create `code/`, `labs/`, or any script.
- **Every exercise ships a hint AND a solution sketch.** Format, one numbered item each: `N. <task> — **Hint:** <hint> — **Solution sketch:** <sketch>`. Never a bare problem.
- **Academic integrity (hard rule):** never solve, partially solve, or reproduce a real Assessment 1 / Portfolio / Task problem. Worked clones and exercises use **different functions, numbers and states** than the course's own. Before writing a day or companion, read the assigned week's `## Apply` and `## Consolidate` sections in `week_N/week_N_content.md` and check that nothing you write duplicates those problems. Known task problems to stay clear of:
  - W2: bra additivity + ⟨A|A⟩ real (P1); common-eigenvalue combinations and e^x, e^{−x} orthogonal on (−1,1) (P2); normalising ψ₁…ψ₄ = sin bump / Cx+λ / Cexp(λx²) / Cexp(−λ|x|) (P3).
  - W3: (|u⟩±|d⟩)/√2 orthogonal (P1); eigenproblem of σ_n = [[cosθ, sinθ],[sinθ, −cosθ]] (P2); acceptability of 3sin(πx), 4−|x|, 5x, x² (P3); x̂, p̂ Hermitian and the hydrogen e^{−r/a₀} probability ratio (portfolio).
  - W4: the four-state expansion with E=(2n−1)E₀ and A=(n+2)a₀ (P1); adjoints of x, i, d/dx and (QR)† = R†Q† (P2).
  - W5: ψ₀ = A exp(−mωx²/2ħ − iωt) solves Ĥψ=Eψ; find A; ⟨x²⟩, σ_x, σ_p, Δx Δp.
  - W7: singlet (↑↓−↓↑)/√2 is not a product state (P1); state A(½|00⟩+½|01⟩+½|11⟩) (P2); σ⊗1 on a product state (P3).
  - Portfolio problems for every week are in each week's `## Consolidate` section — read and avoid those too.
  - Teaching the *technique* is allowed and expected; solving the *instance* is not. When a technique needs an example, change the object (different matrix, different function, different coefficients).
- **Source fidelity:** notation, equation conventions and definitions must match the module's own lecture files (`week_N/week_N_lecture.md`). In particular Week 5 defines the ladder operators via x̂, p̂ (Eqs. 5.6–5.11): `â = (1/√2)(√(mω/ħ) x̂ + i p̂/√(mħω))`, `N̂ = â†â`. Use those, not a textbook variant.
- **"Six steps" page is not exported locally** (`module_3_resources.md` is empty). Use the clearly labelled stand-in in `STRATEGY.md` (Task 1) and never claim it is the university's text.
- **Anonymity:** no learner name, email or user handle in any file under `content/`, `README.md`, `STRATEGY.md`.
- **No git commands in any subagent dispatch** (no `git status/diff/log/add/commit`). Commits are made only by the controller at the checkpoints named in this plan.
- **No real infrastructure, no network calls, no credentials.**
- **Each subagent writes exactly the files assigned to its task, nothing more.**
- **Style:** plain-English first, then notation; every symbol said aloud on first use; short paragraphs; Feynman-style intuition before formalism; LaTeX consistent with the week files (`\hat{}`, `\langle\cdot|\cdot\rangle`, `\mathrm{d}`).
- **Time boxes:** each day file must total ~3.5 h: 20 min warm-up · 60 min moves · 90 min exercises · 40 min apply · 10 min confusion log.

## Target Layout

```
foundations_sprint/
├── README.md                      # Task 16
├── STRATEGY.md                    # Task 1
├── content/
│   ├── GLOSSARY.md                # Task 15
│   ├── day01.md … day07.md        # Tasks 2–8
│   └── companions/
│       └── week02_companion.md … week07_companion.md   # Tasks 9–14
└── docs/superpowers/{specs,plans}/
```

## Move Registry (interface between tasks — IDs are fixed)

| ID | Move | Day |
|---|---|---|
| 1.1 | Algebra triage: rearrange, exponent rules, square roots, fractions | 1 |
| 1.2 | Complex numbers: i, a+ib, conjugate z*, modulus, |z|² = z*z | 1 |
| 1.3 | Euler: e^{iθ} = cosθ + i sinθ, |e^{iθ}| = 1, global phase | 1 |
| 1.4 | Trig identities: sin²+cos²=1, double-angle, half-angle | 1 |
| 2.1 | Column vectors, dot product, length | 2 |
| 2.2 | Ket, bra (conjugate transpose), inner product ⟨φ|ψ⟩ | 2 |
| 2.3 | Inner-product axioms: linearity in ket, conjugate symmetry, ⟨A|A⟩ ≥ 0 | 2 |
| 2.4 | Orthonormal basis, expansion |ψ⟩ = Σ cₙ|n⟩, cₙ = ⟨n|ψ⟩, normalisation | 2 |
| 2.5 | Matrix × vector, matrix multiplication (2×2) | 2 |
| 3.1 | Operators as matrices; how an operator acts on a ket | 3 |
| 3.2 | Eigenvalue equation; 2×2 characteristic polynomial; eigenvector solve; normalise it | 3 |
| 3.3 | Adjoint A†, Hermitian A†=A, (AB)†=B†A†, real eigenvalues, orthogonal eigenvectors | 3 |
| 3.4 | Pauli matrices σₓ σ_y σ_z: eigenvectors, spin-up/down, ±x, ±y states | 3 |
| 3.5 | Commutator [A,B] = AB − BA for matrices | 3 |
| 4.1 | Functions as vectors: ⟨φ|ψ⟩ = ∫φ*ψ dx | 4 |
| 4.2 | Integrals: ∫eᵃˣ, ∫e^{−a|x|}, ∫sin², ∫ over half-lines; sketching |ψ|² | 4 |
| 4.3 | Integration by parts; boundary terms vanish for normalisable ψ | 4 |
| 4.4 | Gaussians: ∫e^{−ax²}dx = √(π/a); ∫x²e^{−ax²}dx = √π/(2a^{3/2}); odd integrands vanish | 4 |
| 4.5 | Normalisation: find C so ∫|ψ|²dx = 1 | 4 |
| 4.6 | Expectation ⟨x⟩ = ∫ψ*xψ dx; probability in an interval; variance | 4 |
| 4.7 | Acceptable wave function checklist: finite, continuous, single-valued, continuous derivative (with finite potentials), normalisable | 4 |
| 4.8 | Derivative operator; p̂ = (ħ/i)d/dx on exponentials; e^{ikx} as momentum eigenfunction | 4 |
| 5.1 | State expansion in an eigenbasis; probabilities |cₙ|²; sum to 1 | 5 |
| 5.2 | Expectation ⟨A⟩ = Σ|cₙ|²aₙ | 5 |
| 5.3 | Collapse: measurement returns an eigenvalue, state becomes that eigenstate, repeat measurement is certain | 5 |
| 5.4 | Time-dependent vs time-independent Schrödinger equation; separation of variables; phases e^{−iEt/ħ}; stationary states | 5 |
| 5.5 | Particle in a box: solve ψ″ = −k²ψ with boundary conditions | 5 |
| 6.1 | Substitution ξ = x√(mω/ħ) and rewriting integrals and Ĥ in ξ | 6 |
| 6.2 | Differentiating a Gaussian twice; checking Ĥψ = Eψ by matching terms | 6 |
| 6.3 | Gaussian moments ⟨ξ²⟩; σ_x, σ_p; uncertainty product | 6 |
| 6.4 | Ladder operators â, â†, N̂ (lecture Eqs. 5.6–5.11); [â,â†]=1; Ĥ=ħω(N̂+½) | 6 |
| 6.5 | Commutator algebra: [x̂,p̂]=iħ, [A,BC]=[A,B]C+B[A,C] | 6 |
| 7.1 | Two-qubit basis |00⟩,|01⟩,|10⟩,|11⟩; tensor product of kets (Kronecker) | 7 |
| 7.2 | Tensor product of operators; (σ⊗1)(|a⟩⊗|b⟩) = (σ|a⟩)⊗|b⟩ | 7 |
| 7.3 | Product-state test: a|00⟩+b|01⟩+c|10⟩+d|11⟩ is a product iff ad = bc | 7 |
| 7.4 | Partial measurement: project, renormalise, read off the other qubit's state and probabilities | 7 |
| 7.5 | Bell states, correlations, what entanglement does and does not imply | 7 |

## Verification Commands (used at each checkpoint by the controller)

Run from `module_3_foundations_of_quantum_mechanics/foundations_sprint/`. Scope of each check equals scope of its rule; if a check fails on **every** file, suspect the check first.

```bash
# V1: every day file has a hint and a solution sketch per exercise (counts equal, non-zero)
for f in content/day0*.md content/companions/*.md; do
  h=$(grep -o '\*\*Hint:\*\*' "$f" | wc -l); s=$(grep -o '\*\*Solution sketch:\*\*' "$f" | wc -l)
  echo "$f hints=$h sketches=$s"; [ "$h" -eq "$s" ] && [ "$h" -gt 0 ] || echo "  ^ FAIL"
done

# V2: no learner identity anywhere the learner will read
grep -rniE 'hung|hunghd|le\.hoang|redkyo' content README.md STRATEGY.md && echo "FAIL: identity found" || echo "V2 ok"

# V3: no code scaffold
[ ! -e code ] && [ ! -e labs ] && echo "V3 ok" || echo "V3 FAIL"

# V4: no unfilled placeholders
grep -rnE 'TBD|TODO|FIXME|lorem|\.\.\.\]|<[A-Z][a-z]+ ?[a-z]*>' content README.md STRATEGY.md && echo "V4 FAIL" || echo "V4 ok"
```

## Tasks

### Task 1: STRATEGY.md (strategy, mistakes, reading protocol, six-steps stand-in)

**Files:**
- Create: `STRATEGY.md`

**Interfaces:**
- Produces: sections named exactly `## The Strategy`, `## Mistakes That Waste 80% of Beginners' Time`, `## Five-Pass Lecture Protocol`, `## Six-Steps Write-Up (stand-in)`, `## Confusion Log Template`. Later tasks link to these headings.

- [ ] **Step 1: Read the spec** sections *Strategy* and *Lecture reading protocol*.
- [ ] **Step 2: Write `STRATEGY.md`** with these sections, content taken from the spec and expanded into usable prose:
  1. `## The Strategy` — the four principles (learn moves not subjects; problems before theory; retrieval over rereading; six-steps from day 1), each with one paragraph on *why* it works and one concrete instruction. Include a short "what we rejected and why" (weekly primers; compressed bottom-up).
  2. `## Mistakes That Waste 80% of Beginners' Time` — the seven mistakes from the spec, each with a one-line *fix*.
  3. `## Five-Pass Lecture Protocol` — passes 0–4 with time boxes, and a worked example applying it to Week 2 Postulate 1 (read the quiz first, what to write in the confusion log, what to re-derive closed-book).
  4. `## Six-Steps Write-Up (stand-in)` — begin with a boxed note: *"The university's own 'Six steps to problem solving: How to gain marks' page is not in the local exports. This is a stand-in built on standard good practice. If you paste the real page into `module_3_resources.md`, replace this section."* Then six steps: (1) restate what is asked and list givens; (2) draw/sketch or write the state in the right notation; (3) name the principle or move you will use; (4) do the algebra with every step shown; (5) check — units, normalisation, limiting case, sign, sanity of probability ∈ [0,1]; (6) state the answer in a full sentence. Include a 6-line example on a trivial problem (normalising ψ = C e^{−|x|}) written in that format.
  5. `## Confusion Log Template` — the table `| Where (lecture § / eq.) | Symbol or step | What I think it means | What it actually means | Resolved? |`.
- [ ] **Step 3: Verify** — `grep -c '^## ' STRATEGY.md` returns 5; run V2 and V4 from the Verification section.

### Task 2: Day 1 — Complex numbers and trig triage

**Files:**
- Create: `content/day01.md`

**Interfaces:**
- Produces: Moves 1.1–1.4 (IDs from the registry as `### Move 1.x — <name>` headings). Glossary terms to be defined here: *complex number, real part, imaginary part, complex conjugate, modulus, phase, Euler's formula, unit circle, double-angle identity*.

- [ ] **Step 1: Read** the spec's day skeleton, then `week_2/week_2_lecture.md` §2.1 and `week_3/week_3_lecture.md` to see where complex numbers and trig appear.
- [ ] **Step 2: Write `content/day01.md`** following the Content Day Skeleton in the spec. Specifics:
  - *Warm-up:* Day 1 has no previous days; make it a **diagnostic** of five school-level questions (fractions, exponents, solving a quadratic, sin/cos of 30°/45°/60°, expanding (a+b)²), answers folded in a `<details>` block at the bottom.
  - *Moves 1.1–1.4* as in the registry; each with statement, why it works, one worked example.
  - *Exercises:* 8–10, covering: modulus and conjugate computation; showing |z|² = z*z is real and ≥ 0; (a+ib)(a−ib); e^{iθ} at θ = 0, π/2, π; showing |e^{iθ}|=1 and why a global phase changes nothing measurable; double-angle rewrites like 2sinθcosθ; simplify cos²θ − sin²θ; find the modulus of (1+i)/√2; write −i in the form e^{iφ}; one problem asking the learner to spot that (cosθ, sinθ) has unit length.
  - *Apply to the lecture:* point to Week 2 §2.1 (ψ*ψ, and why the probability density is real) and Week 3 (trig in eigenvectors). Say which companion sections to read afterwards (Week 2, Week 3 notation decoders).
  - *Anti-patterns:* forgetting the conjugate flips the sign of i everywhere; treating |z|² as z².
- [ ] **Step 3: Verify** — V1 on this file (hints = sketches > 0); heading list contains `Move 1.1`…`Move 1.4`; time boxes add to ~3.5 h.

### Task 3: Day 2 — Vectors, bra-ket, inner products

**Files:**
- Create: `content/day02.md`

**Interfaces:**
- Consumes: Move 1.2 (conjugate/modulus).
- Produces: Moves 2.1–2.5. Glossary terms: *vector, column vector, ket, bra, inner product, orthogonal, orthonormal, basis, expansion coefficient, normalisation, matrix, matrix–vector product*.

- [ ] **Step 1: Read** `week_2/week_2_lecture.md` §2.1 (Postulate 1, superposition) and the Week 2/3/4 Apply sections (to avoid duplicating them).
- [ ] **Step 2: Write `content/day02.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-1 questions (conjugate, modulus, Euler at π, double-angle, |z|² real).
  - Use the spin basis |u⟩,|d⟩ as the running example (same as Week 3), written as columns (1,0)ᵀ and (0,1)ᵀ.
  - Explain **bra = conjugate transpose of ket** and **why** the inner product conjugates the first slot, then state the two axioms in the same wording the course uses (linearity in the ket; ⟨B|A⟩ = ⟨A|B⟩*).
  - *Exercises:* 8–10 covering: compute ⟨φ|ψ⟩ for 2-component complex vectors; find a normalisation constant; check orthonormality of a given pair (use **different** vectors from the W3 task); expand a ket in the |u⟩,|d⟩ basis and read off cₙ = ⟨n|ψ⟩; prove **anti**linearity in the bra slot (⟨αA|B⟩ = α*⟨A|B⟩) from the two axioms; show ⟨A|B⟩ + ⟨B|A⟩ is real; 2×2 matrix × vector; compute |⟨u|ψ⟩|² and check that |c_u|²+|c_d|² = 1.
  - **Do not** ask the learner to prove the exact statements in W2 P1.
  - *Apply:* Week 2 §2.1 superposition and the interpretation of cₙ; forward-point to Week 2 and Week 4 companions.
  - *Anti-patterns:* forgetting the conjugate on the bra; assuming ⟨A|B⟩ = ⟨B|A⟩; using the row vector without conjugating.
- [ ] **Step 3: Verify** — V1; headings contain `Move 2.1`…`Move 2.5`.

### Task 4: Day 3 — Operators, eigenproblems, Hermitian, Pauli

**Files:**
- Create: `content/day03.md`

**Interfaces:**
- Consumes: Moves 1.2–1.4, 2.2, 2.5.
- Produces: Moves 3.1–3.5. Glossary terms: *operator, eigenvalue, eigenvector, eigenstate, characteristic polynomial, adjoint, Hermitian, Pauli matrices, spin-up/spin-down, commutator, degenerate*.

- [ ] **Step 1: Read** `week_3_lecture.md` (spin, eigen), `week_6_lecture.md` §Pauli/spin sections, and W3/W4 Apply sections (avoid duplication).
- [ ] **Step 2: Write `content/day03.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-2 questions.
  - Teach the 2×2 eigen recipe as a **five-line algorithm**: write det(A−λI)=0 → solve for λ → plug back → solve one row for the ratio → normalise. Make the algorithm visually distinct.
  - Prove in words and one example that Hermitian ⇒ real eigenvalues and orthogonal eigenvectors.
  - *Exercises:* 9–11 covering: eigenpairs of [[2,1],[1,2]], [[0,−i],[i,0]] (σ_y), [[1,i],[−i,1]]; check Hermiticity of three given matrices; compute a specific (AB)† and B†A† and compare (use explicit 2×2 matrices unlike the W4 task); show σₓσ_y = iσ_z and [σₓ,σ_y] = 2iσ_z; find the ±x eigenstates and check they are orthonormal and that |⟨u|+x⟩|² = ½; one problem that asks *why* eigenvalues of a Hermitian matrix must be real, with hint pointing back to Move 2.3.
  - **Do not** use σ_n = [[cosθ, sinθ],[sinθ, −cosθ]].
  - *Apply:* Week 3 (measurement and eigenvalues) and Week 6 (spin-½ matrices); name the companion sections to read.
  - *Anti-patterns:* forgetting to normalise; treating a matrix's eigenvalues as its entries; dropping the conjugate when taking † .
- [ ] **Step 3: Verify** — V1; headings contain `Move 3.1`…`Move 3.5`.

### Task 5: Day 4 — Calculus as the module uses it

**Files:**
- Create: `content/day04.md`

**Interfaces:**
- Consumes: Moves 1.2, 1.3, 2.2.
- Produces: Moves 4.1–4.8. Glossary terms: *wave function, probability density, normalisable, normalisation constant, expectation value, variance, standard deviation, Gaussian, odd/even function, integration by parts, momentum operator, plane wave, eigenfunction, single-valued, continuous*.

- [ ] **Step 1: Read** `week_2_lecture.md` (Postulates 1–2, normalisation, acceptability), `week_3_lecture.md`, `week_5_lecture.md` (Gaussian and integral hints).
- [ ] **Step 2: Write `content/day04.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-3 questions.
  - Frame it as "**functions are just infinite-length vectors**": ⟨φ|ψ⟩=∫φ*ψ dx is the dot product you already know (Move 4.1).
  - Give a **one-page integral cheat sheet** covering exactly Moves 4.2–4.4 (no more calculus than that), each with a one-line "when the module needs it".
  - *Exercises:* 10–12 covering: normalise C e^{−3|x|}; normalise C e^{−x²/2}; check acceptability of five functions (use x e^{−x²}, 1/x, e^{x}, a step function, sin x on all of ℝ); compute ⟨x⟩ for a function on [0,L]; probability of finding the particle in an interval for a given ψ; apply p̂ = (ħ/i)d/dx to e^{ikx} and to sin(kx) and say which is an eigenfunction; integrate by parts once to move a derivative from ψ to φ and state when the boundary term vanishes; sketch |ψ|² for a given piecewise ψ; ∫x e^{−x²} = 0 by symmetry.
  - **Do not** use the W2 P3 functions or the hydrogen e^{−r/a₀} ratio.
  - *Apply:* Week 2 Postulate 2 and Week 3 measurement; Week 5 Gaussians; name the companion sections.
  - *Anti-patterns:* forgetting |ψ|² = ψ*ψ (integrating ψ instead); dropping limits; forgetting a factor of 2 for the even function on (−∞,∞).
- [ ] **Step 3: Verify** — V1; headings contain `Move 4.1`…`Move 4.8`.

### Task 6: Day 5 — Measurement, Schrödinger equation, stationary states

**Files:**
- Create: `content/day05.md`

**Interfaces:**
- Consumes: Moves 2.4, 3.2, 3.3, 4.5, 4.8.
- Produces: Moves 5.1–5.5. Glossary terms: *measurement postulate, collapse, expectation value (discrete), Hamiltonian, Schrödinger equation, stationary state, separation of variables, boundary condition, energy level, time evolution, potential well*.

- [ ] **Step 1: Read** `week_4_lecture.md` in full and Week 4 Apply/Consolidate (avoid duplication).
- [ ] **Step 2: Write `content/day05.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-4 questions.
  - Teach measurement as a **three-line recipe**: expand → square the coefficients → collapse. Emphasise *probabilities come from coefficients*, values from eigenvalues.
  - Derive the box solution fully: ψ″=−k²ψ, boundary conditions ψ(0)=ψ(L)=0, quantised k, normalisation √(2/L), energies Eₙ = n²π²ħ²/(2mL²).
  - Include a short **Assessment 1 readiness checklist** (skills only; no problems from the course): a list of "I can…" statements drawn from Days 1–5.
  - *Exercises:* 9–11, all on **new** states and operators: three-state expansion with different coefficients and eigenvalues (e.g. energies 1,4,9 units); find P(E) and ⟨E⟩; measure A then B when they share/do not share eigenstates; collapse then re-measure; show that |ψ(x,t)|² is time-independent for a single stationary state, and time-dependent for a superposition of two; box-ground-state normalisation and probability of finding the particle in the left third; check the ground state's energy scaling with L.
  - **Do not** reuse E=(2n−1)E₀ or A=(n+2)a₀ or the coefficients 2, √2, √3, 1.
  - *Apply:* Week 4 (all sections) and the Week 4 quiz themes; name companion sections.
  - *Anti-patterns:* mixing up coefficients and probabilities; forgetting to renormalise after collapse; treating time as an observable (Week 4 Q3 theme).
- [ ] **Step 3: Verify** — V1; headings contain `Move 5.1`…`Move 5.5`.

### Task 7: Day 6 — The oscillator toolkit

**Files:**
- Create: `content/day06.md`

**Interfaces:**
- Consumes: Moves 4.4, 4.5, 4.6, 4.8, 5.4, 3.5.
- Produces: Moves 6.1–6.5. Glossary terms: *harmonic oscillator, ladder operator, raising operator, lowering operator, number operator, zero-point energy, uncertainty relation, standard deviation, commutator relation, dimensionless variable*.

- [ ] **Step 1: Read** `week_5_lecture.md` in full (especially Eqs. 5.6–5.11 and §5.3–5.5) and Week 5 Apply/Consolidate.
- [ ] **Step 2: Write `content/day06.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-5 questions.
  - Move 6.1: substitution ξ=x√(mω/ħ), showing how it turns every ħ, m, ω into 1 (the whole point: fewer symbols).
  - Move 6.4 **must** use the lecture's convention: â = (1/√2)(√(mω/ħ) x̂ + i p̂/√(mħω)), â† its adjoint, N̂ = â†â, [â,â†]=1, Ĥ=ħω(N̂+½). Include the lecture's inverse relations for x̂ and p̂ in terms of â, â†.
  - Move 6.5: derive [x̂,p̂]=iħ from p̂=(ħ/i)d/dx acting on a test function; state the product rule for commutators.
  - *Exercises:* 9–11 covering: substitution ξ in an integral of a **different** Gaussian-type function; differentiate e^{−ξ²/2}, ξe^{−ξ²/2} twice; verify that ψ₁ ∝ ξe^{−ξ²/2} satisfies Ĥψ=Eψ with E=3ħω/2 (**not** ψ₀); ⟨ξ²⟩ for ψ₁ via the Gaussian moment formulas; check [â,â†]=1 for one line of algebra given x̂, p̂ commutator; compute [N̂,â†] and [N̂,â]; show â†|n⟩ raises energy by ħω; compute [x̂²,p̂].
  - **Do not** solve the W5 tasks for ψ₀ (verify Hψ=Eψ, find A, ⟨x²⟩, σ_x, σ_p, uncertainty product).
  - *Apply:* Week 5 §5.2–5.5; name the companion sections.
  - *Anti-patterns:* mixing dimensionful x with dimensionless ξ; forgetting a Jacobian dx = √(ħ/mω) dξ; assuming â is Hermitian.
- [ ] **Step 3: Verify** — V1; headings contain `Move 6.1`…`Move 6.5`; grep `√(mω/ħ)` or the LaTeX equivalent present in the ladder-operator definition.

### Task 8: Day 7 — Tensor products, entanglement, mock problem set

**Files:**
- Create: `content/day07.md`

**Interfaces:**
- Consumes: Moves 2.4, 3.1, 3.4, 5.1, 5.3.
- Produces: Moves 7.1–7.5 and a `## Mock Problem Set` section. Glossary terms: *tensor product, Kronecker product, composite system, product state, entangled state, Bell state, singlet, partial measurement, correlation, qubit*.

- [ ] **Step 1: Read** `week_7_lecture.md` in full and Week 7 Apply/Consolidate.
- [ ] **Step 2: Write `content/day07.md`** per the skeleton. Specifics:
  - *Warm-up:* five Day-6 questions.
  - Kronecker product done by hand on kets first (|0⟩⊗|1⟩ = |01⟩ = (0,1,0,0)ᵀ), then on operators; the 4×4 for σₓ⊗1.
  - Move 7.3: prove "product iff ad = bc" in five lines; apply it to a **new** state (e.g. (|00⟩+|11⟩)/√2, (|00⟩+|01⟩+|10⟩+|11⟩)/2, (|01⟩+|10⟩)/√2).
  - Move 7.4: project, renormalise, read off the second qubit's distribution — on a **new** state.
  - Move 7.5: four Bell states; distinguish "correlated" from "communicates" (no faster-than-light signalling); align wording with the Week 7 lecture and quiz themes.
  - *Exercises:* 8–10 as above.
  - `## Mock Problem Set` — 10 mixed problems covering Days 1–7, in the style of a timed problem set, **each with hint and solution sketch**, all on new material. Add a scoring rubric (method, algebra, check, answer) and a "which move do I retry?" table mapping wrong answers to Move IDs.
  - **Do not** use the W7 states or the W7 P3 σ⊗1 statement.
  - *Apply:* Week 7 lecture; Week 6 link (spin as the qubit); name companion sections.
  - *Anti-patterns:* treating any 2-term superposition as entangled; forgetting to renormalise after partial collapse; mixing up the ordering of tensor factors.
- [ ] **Step 3: Verify** — V1; headings contain `Move 7.1`…`Move 7.5` and `## Mock Problem Set`; mock set has 10 numbered items.

> **CHECKPOINT A (controller only, no subagent running):** after Tasks 1–8 are complete, run V1–V4, then `git add module_3_foundations_of_quantum_mechanics/foundations_sprint/ && git commit -m "WIP: strategy + days 1-7 (scratch)"` and record `git rev-parse --short HEAD`.

### Task 9: Week 2 Companion

**Files:**
- Create: `content/companions/week02_companion.md`

**Interfaces:**
- Consumes: Moves 1.2, 1.3, 2.2–2.4, 4.1–4.7, 4.8. Links to `../day01.md`, `../day02.md`, `../day04.md` and `../../STRATEGY.md#six-steps-write-up-stand-in`.

- [ ] **Step 1: Read** `week_2/week_2_lecture.md`, `week_2/week_2_content.md` (Apply, Consolidate, Quiz).
- [ ] **Step 2: Write the companion** using the Week Companion Skeleton in the spec. Specifics:
  - *What this week is really saying:* postulate 1 (the wave function *is* the state; |ψ|² is a probability density) and postulate 2 (every observable is an operator; measured values are eigenvalues). Add a physical picture (a "probability cloud", a ket as an arrow whose components are amplitudes).
  - *Notation decoder:* at least 12 rows including ψ, ψ*, |ψ|², d³**r**, ê_x, ⟨φ|ψ⟩, Ô, eigenvalue equation Ôψ = qψ, normalisation ∫|ψ|²=1.
  - *Skipped steps, expanded:* the lecture's normalisation argument, superposition, and the eigenfunction/eigenvalue statement — every step justified.
  - *Worked clones* (different objects from W2 tasks): (1) prove a bra/ket identity of the same *type* as W2 P1 using the two axioms, on a **different** identity (e.g. ⟨αA|B⟩ = α*⟨A|B⟩ and ⟨A|B⟩+⟨B|A⟩ real); (2) eigenfunction combination of the same *type* as W2 P2 with a **different** operator (e.g. d²/dx² on sin(kx), cos(kx)); (3) normalisation of the same *type* as W2 P3 with **different** functions (e.g. C e^{−2|x|}, C x for 0≤x≤1, C e^{+x} on all ℝ). Each written in the six-steps stand-in format.
  - *Retrieval questions:* 8–10, quiz-style, aligned with the Week 2 quiz themes; each names the misconception it traps.
  - *Six-steps template* for a "normalise / check acceptability" problem.
  - Every worked clone and retrieval question has **Hint** and **Solution sketch** where the learner is meant to attempt it; fully worked clones may show the solution but must still end with a "Try it yourself" exercise with hint + sketch.
- [ ] **Step 3: Verify** — V1 on the file; grep that no line reproduces the W2 problem instances (`Cx + \lambda`, `\lambda_3 x^2`, `e^{x}` with `e^{-x}` on `(-1, 1)`).

### Task 10: Week 3 Companion

**Files:**
- Create: `content/companions/week03_companion.md`

**Interfaces:**
- Consumes: Moves 2.2–2.5, 3.1–3.4, 4.1–4.7. Links to Days 2, 3, 4 and STRATEGY.

- [ ] **Step 1: Read** `week_3/week_3_lecture.md`, `week_3/week_3_content.md`.
- [ ] **Step 2: Write the companion** per the skeleton. Specifics:
  - *Really saying:* measurement outcomes are eigenvalues; outcomes are random with probabilities |⟨n|ψ⟩|²; the wave function is not the "actual position"; expectation values are averages.
  - *Decoder:* ⟨A⟩, Δ, eigenvector/eigenstate, σₙ, |u⟩,|d⟩, Hermitian, ĥ, x̂, p̂, ℏ (≥12 rows).
  - *Skipped steps:* the probability rule and expectation value derivation; why Hermitian ⇒ real.
  - *Worked clones (different objects):* (1) orthogonality check of two kets of the W3 P1 *type* with **different** vectors (e.g. (|u⟩+i|d⟩)/√2 and (|u⟩−i|d⟩)/√2); (2) 2×2 eigenproblem with an angle parameter of the W3 P2 *type* on a **different** matrix (e.g. [[cosθ, −i sinθ],[i sinθ, −cosθ]] or [[1,e^{−iφ}],[e^{iφ},1]]); (3) acceptability of the W3 P3 *type* with **different** functions (e.g. e^{−|x|}, 1/(1+x²), tan x, |x|e^{−x²}); (4) technique for Hermiticity proofs (integration by parts, conjugation) shown on **d²/dx²** or i d/dx — not on x̂ or p̂ — plus the *method* for a "relative probability in a tiny volume" problem using a different wave function (e.g. e^{−2r/a}). 
  - *Retrieval + six-steps template* as in Task 9.
- [ ] **Step 3: Verify** — V1; grep that `\sin(\pi x)`, `4 - |x|`, and `\cos(\theta) & \sin(\theta)` do not appear as worked instances.

### Task 11: Week 4 Companion

**Files:**
- Create: `content/companions/week04_companion.md`

**Interfaces:**
- Consumes: Moves 3.2–3.5, 5.1–5.5. Links to Days 3, 5 and STRATEGY.

- [ ] **Step 1: Read** `week_4/week_4_lecture.md`, `week_4/week_4_content.md` (both tasks, the portfolio problems, quiz).
- [ ] **Step 2: Write the companion** per the skeleton. Specifics:
  - *Really saying:* the Schrödinger equation is the rule for how states change in time; energy eigenstates are the special states that only pick up a phase; everything else is a superposition of them.
  - *Decoder:* Ĥ, iħ∂/∂t, E_n, |φₙ⟩, e^{−iEt/ħ}, †, ≥12 rows.
  - *Skipped steps:* separation of variables; why stationary states have constant |ψ|²; the adjoint rules with the reversed-order reason.
  - *Worked clones:* (1) state-expansion measurement problem of the W4 P1 *type* with **different** numbers (three states, energies (n²)E₀, coefficients 1/√6, √2/√6…, and an operator with eigenvalues that are **not** an affine function of n), including the "measure E, then measure A" collapse logic; (2) adjoint problem of the W4 P2 *type* on **different** objects (adjoint of x̂², of d²/dx², of i d/dx, and (ABC)†); (3) a time-evolution problem: given ψ(0) as a two-eigenstate superposition, write ψ(t) and show the probability of each energy is constant.
  - *Task 2 misconception discussion:* provide a **framework** (list of common misconceptions, why each arises, and what to check), not a finished post; tell the learner to write their own.
  - *Assessment 1 tip section:* method-only guidance (how to structure answers, what to check), no solutions to course problems.
- [ ] **Step 3: Verify** — V1; grep that `2n - 1`, `n + 2`, `\sqrt{10}` do not appear as worked instances.

### Task 12: Week 5 Companion

**Files:**
- Create: `content/companions/week05_companion.md`

**Interfaces:**
- Consumes: Moves 4.4–4.6, 6.1–6.5. Links to Days 4, 6 and STRATEGY.

- [ ] **Step 1: Read** `week_5/week_5_lecture.md` (all), `week_5/week_5_content.md`.
- [ ] **Step 2: Write the companion** per the skeleton. Specifics:
  - *Really saying:* the oscillator's energy comes in equal steps ħω; â† climbs the ladder, â descends; the ground state is where the ladder stops and still has energy ħω/2.
  - *Decoder:* â, â†, N̂, |n⟩, ξ, ω, ħω(n+½), [â,â†]=1, ≥14 rows, using the lecture's Eqs. (5.6)–(5.11).
  - *Skipped steps:* expand the lecture's [â, â†] = 1 derivation line by line; N̂ eigenvalues n = 0,1,2…; â|n⟩=√n|n−1⟩ and â†|n⟩=√(n+1)|n+1⟩ from the commutator; build |1⟩ from |0⟩.
  - *Worked clones (different objects):* (1) "show ψ satisfies Ĥψ=Eψ" of the W5 P1 *type* using ψ₁ ∝ ξe^{−ξ²/2}, plus the *technique* for a Gaussian ground state stated generally with different parameter symbols; (2) expectation/uncertainty problem of the W5 P2 *type* on ψ₁ (⟨ξ²⟩, σ_x, σ_p, product vs ħ/2), and one on a simple **box** ground state for contrast; (3) ladder-operator manipulation: compute ⟨n|x̂²|n⟩ using â, â† (no integrals).
  - *Hints from the course:* the substitution and Gaussian integrals are in the task's Hints — explain the *why*, not the answer.
- [ ] **Step 3: Verify** — V1; ladder-operator definitions match the lecture (grep `\sqrt{\frac{m\omega}{\hbar}}`); no worked instance for ψ₀'s A, ⟨x²⟩, or Δx Δp.

### Task 13: Week 6 Companion (concept + portfolio-essay method)

**Files:**
- Create: `content/companions/week06_companion.md`

**Interfaces:**
- Consumes: Moves 3.1, 3.4, 5.1. Links to Days 3, 7 and STRATEGY.

- [ ] **Step 1: Read** `week_6/week_6_lecture.md`, `week_6/week_6_content.md` (the Apply task and quiz), and `module_3_foundations_of_quantum_mechanics/exteral_resources/` file names (do not summarise files you did not read).
- [ ] **Step 2: Write the companion** per the skeleton, adapted (no worked maths problems beyond spin-½ checks). Specifics:
  - *Really saying:* silver atoms in an inhomogeneous magnetic field split into discrete beams; spin is quantised and has no classical analogue; the second measurement can undo the first (sequential SG).
  - *Decoder:* S_z, S_x, ħ/2, |↑⟩,|↓⟩, σ matrices, inhomogeneous B-field, magnetic moment (≥12 rows).
  - *Skipped steps:* why the field must be *inhomogeneous*; what "two beams, not a smear" implies; the sequential-measurement paradox in spin-state language (Moves 3.4, 5.1).
  - *Worked clones:* 3 short spin-½ exercises with hint + sketch (e.g. probabilities after S_z then S_x; three sequential magnets).
  - *Portfolio essay guide (method only):* a **planning skeleton** for the Stern-Gerlach discussion — questions to answer, evidence types, a paragraph-by-paragraph outline with word-budget suggestions within the 2100-word portfolio, and a checklist for citing sources. **Do not write the essay or any paragraph of it.** State explicitly: "This is a structure, not text to submit."
  - *Retrieval questions:* 8, aligned to the Week 6 quiz themes, each naming its misconception.
- [ ] **Step 3: Verify** — V1; grep the file for the phrase `not text to submit`; confirm no continuous prose passage longer than 120 words is written *as* essay text (manual read).

### Task 14: Week 7 Companion

**Files:**
- Create: `content/companions/week07_companion.md`

**Interfaces:**
- Consumes: Moves 2.4, 3.1, 3.4, 5.3, 7.1–7.5. Links to Days 2, 3, 7 and STRATEGY.

- [ ] **Step 1: Read** `week_7/week_7_lecture.md`, `week_7/week_7_content.md` (Apply, Consolidate, quiz), and `external_resources` names only (do not summarise unread files).
- [ ] **Step 2: Write the companion** per the skeleton. Specifics:
  - *Really saying:* two particles need one shared state; some shared states cannot be split into "state of A × state of B"; measuring one instantly fixes the other's *statistics* but sends no message.
  - *Decoder:* ⊗, |↑↓⟩, |00⟩, ψ_AB, (σ⊗1), product state, entangled, Bell state, singlet, ≥12 rows.
  - *Skipped steps:* why the Kronecker product is the right rule; the product-state test; the projection and renormalisation in a partial measurement.
  - *Worked clones (different objects):* (1) product/entangled test of the W7 P1 *type* on **different** states; (2) partial-measurement problem of the W7 P2 *type* on a **different** three-term state with a different normalisation; (3) composite-operator action of the W7 P3 *type* using **σ_z⊗σ_x** (or another two-operator product) on a product state, showing it stays a product state or not.
  - *Misconception traps:* faster-than-light communication, "hidden information," "entangled = correlated."
  - *Portfolio method note:* method-only, no answers.
- [ ] **Step 3: Verify** — V1; grep that the W7 instances (`\frac{1}{\sqrt{2}} (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)`, `A \left( \frac{1}{2} |00\rangle`) do not appear as worked cases.

> **CHECKPOINT B (controller only):** after Tasks 9–14, run V1–V4 and commit `WIP: companions W2-W7 (scratch)`. Record the hash.

### Task 15: GLOSSARY.md

**Files:**
- Create: `content/GLOSSARY.md`

**Interfaces:**
- Consumes: the term lists in Tasks 2–8 and the decoder tables in the companions (read those files, do not guess).
- Produces: sections `## A–Z Index` and `## Day 1 … Day 7` plus `## Companion-only terms`.

- [ ] **Step 1: Read** all seven day files and six companions; extract every term listed under "Glossary terms" in the tasks above plus every decoder row.
- [ ] **Step 2: Write `GLOSSARY.md`** with:
  1. `## A–Z Index` — alphabetical list linking to entries (`[term](#anchor)`).
  2. Sections **by the day that introduces the term** (`## Day 1 — …` to `## Day 7 — …`), then `## Companion-only terms`.
  3. Each entry: `**term / symbol** — *say it as:* … — *meaning:* one plain-English sentence — *tiny example:* … — *see:* Day N §…; Week N companion §… — *Commonly confused with:* … (only where a real trap exists, e.g. bra vs ket, Hermitian vs adjoint, eigenvalue vs eigenstate, product vs entangled state, ψ vs |ψ|²).
  4. Include the notation symbols: ψ, ψ*, |ψ|², ⟨φ|ψ⟩, |ψ⟩, ⟨ψ|, Ô, Ĥ, †, ħ, ⊗, ∂/∂t, [·,·], σ matrices, â, â†, N̂, ξ, |↑⟩, |↓⟩, |0⟩, |1⟩.
- [ ] **Step 3: Verify** — every term listed in Tasks 2–8 "Glossary terms" appears in the file (`for t in "complex conjugate" "orthonormal" … ; do grep -qi "$t" content/GLOSSARY.md || echo "MISSING $t"; done`, list assembled from those task lines); ≥ 90 entries; the index has one link per entry.

### Task 16: README.md and final verification

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`** with: one-paragraph purpose; a 7-day table (Day / Focus / Feeds Week / Companion); a "how to use with the course" section (order: warm-up → moves → exercises → apply); a **weekly rhythm** section (which day to do around each Sussex week and the Assessment 1 (Thu Week 4, 17:00 UK) and Portfolio (Mon Week 8, 10:00 UK) deadlines); a directory map; the five-pass protocol in one paragraph linking to `STRATEGY.md`; a note that **the six-steps stand-in** is not the university's text; an integrity note (companions teach method and never answer assessed problems); a "how to attach your existing `linear_algebra` / `physics_fundamental` courses later if you want depth" pointer.
- [ ] **Step 2: Run V1–V4** from the Verification section, plus:
  - `ls content/day0*.md | wc -l` → 7; `ls content/companions/*.md | wc -l` → 6.
  - `grep -c 'Move ' content/day0*.md` shows each day has its registry moves.
  - Spot-check three companions against their week's `## Apply` text for accidental duplication.
- [ ] **Step 3: Fix** anything that fails at its source file, then re-run the failing check only.

> **CHECKPOINT C / TEARDOWN (controller only):** commit `WIP: glossary + readme (scratch)`, then hand the learner the five-line teardown from `skill.md` (`git reset --soft master` → `git switch master` → `git reset` → `git branch -D authoring/module3-foundations-sprint` → `git status`) and ask them to paste back `git status`. Confirm the path is untracked on `master`, the learner's own edits are untouched, and nothing was pushed.
