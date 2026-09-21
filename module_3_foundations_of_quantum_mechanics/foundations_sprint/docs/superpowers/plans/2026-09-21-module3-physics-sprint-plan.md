# Module 3 Physics Sprint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author five short physics files (P1–P5), extend the glossary, README, STRATEGY and five day files, so a learner with very little school physics can follow the physics that Module 3 (Foundations of Quantum Mechanics) assumes.

**Architecture:** Move-based, problem-first, same style as the maths days. Each P-file teaches fixed physics moves (registry below) and ends every move with a "Quantum bridge". P-files are new files only; existing reviewed maths files change only by one-line pointers.

**Tech Stack:** Markdown with LaTeX (`$…$`, `$$…$$`), matching the existing files. No code, no labs.

**Spec:** `foundations_sprint/docs/superpowers/specs/2026-09-21-module3-physics-sprint-design.md` (source of truth; read it first). It extends `…/specs/2026-09-21-module3-foundations-sprint-design.md`. The earlier plan `…/plans/2026-09-21-module3-foundations-sprint-plan.md` (header lines 1-112) holds the list of known course task problems — read those lines too.

All paths are relative to `module_3_foundations_of_quantum_mechanics/foundations_sprint/` unless they start with `week_` or `module_` or `exteral_resources` (spelled that way on disk), which are relative to the parent `module_3_foundations_of_quantum_mechanics/`.

## Global Constraints

- **Path type:** pure science, text only. No `code/`, `labs/`, or scripts.
- **Every exercise ships a hint AND a solution sketch.** Format: `N. <task> — **Hint:** <hint> — **Solution sketch:** <sketch>`. Numerical exercises show a units check.
- **Academic integrity (hard rule, unchanged):** never solve, partially solve or reproduce a real Assessment 1 / Portfolio / Task problem. Teach the *technique/physics* on a **different object**. Read `## Apply` and `## Consolidate` of the relevant `week_N/week_N_content.md` before writing. Physics-specific traps:
  - **W3 portfolio P2** (hydrogen ground-state e^{−r/a₀}, probability ratio in 1.0 pm³ at the nucleus vs a₀ away): do not compute anything with that wave function.
  - **W5 tasks** (ψ₀ = A exp(−mωx²/2ħ − iωt); Ĥψ=Eψ, normalise A, ⟨x²⟩, σ_x, σ_p, Δx Δp): P3 gives the classical oscillator and energy quantisation *ideas* only; do not evaluate ⟨x²⟩, σ_x, σ_p or the uncertainty product for ψ₀.
  - **W6 Apply task** ("research the key results and implications of the Stern-Gerlach experiment, including quantised spin, violation of classical principles, development of QM; identify what you consider the most important results and implications"): P4 explains the *mechanism and what is observed*. It must NOT rank or judge which results/implications are "most important", must not list them as a ready-made essay outline, and contains no essay prose. The learner does that judgement.
  - **W4 Task 2** ("identify common misconceptions and discuss why they occur"): P5 may name interpretations neutrally but must not write a misconceptions post or a list of misconceptions with causes.
  - **W7** (singlet not a product state; A(½|00⟩+½|01⟩+½|11⟩) measurement; σ⊗1 on a product state; the portfolio singlet with σ_x, τ_y and a correlation): P5 may name Bell/singlet states as entangled *because the lecture does*, but must not perform the ad = bc product-state proof, any partial-measurement calculation on those states, or the portfolio correlation.
  - Existing files already teach related maths; P-files must not duplicate maths exercises from `content/day0*.md` or `content/companions/*.md` (e.g. the three-box 1/8 sequence in the W6 companion; 60° spin probabilities 3/4, 1/4, 1/4). Use different angles/objects when a physics exercise resembles one.
- **Source fidelity:** equations and notation agree with the lecture files. Lecture anchors to read and stay consistent with:
  - W1 `week_1/week_1_lecture.md` §1.1 (Newton's F=ma, F=−∂V/∂x, determinism, Eq. 1.4 Schrödinger equation, ħ = 1.055×10⁻³⁴ J·s), Hamiltonian (Eq. 1.11), momentum operator (Eq. 1.23, p̂ = −iħ∇); `week_1/week_1_references.md`.
  - W3 `week_3/week_3_lecture.md` §3.1 (discrete spectra, hydrogen spectral lines), §3.4 (interpretations).
  - W4 `week_4/week_4_lecture.md` §4.2 (e^{ikx}, E = ħ²k²/2m, p = ħk, λ = 2π/|k|), §4.3 (infinite well).
  - W5 `week_5/week_5_lecture.md` §5.1 (V = ½kx² = ½mω²x², ω = √(k/m)).
  - W6 `week_6/week_6_lecture.md` §6.1–6.4 (silver atoms, inhomogeneous B-field, Stern & Gerlach 1922, quantised spin, repeated measurements, interference; lecture notation |ψ_z^±⟩, |ψ_x^±⟩).
  - W7 `week_7/week_7_lecture.md` §7.2 (entanglement), §7.4 (quantum key distribution).
  - Existing conventions already in this path: p̂ = −iħ ∂/∂x and (ħ/i) d/dx are the same (Day 4 Move 4.8); ħ/2 spin convention is flagged as a convention (Day 3, W6 companion); Eq. 6.2 is a table of magnitudes with phase a convention (W6 companion); lecture quirks flagged in the companions (W2 Eq. 2.21, W5 Eqs. 5.5/5.10/5.26).
- **Constants:** ħ = 1.055×10⁻³⁴ J·s is given by the lecture. Every other constant is a standard value rounded to 4 significant figures, labelled **(standard value)**: h = 6.626×10⁻³⁴ J·s, c = 2.998×10⁸ m/s, e = 1.602×10⁻¹⁹ C, 1 eV = 1.602×10⁻¹⁹ J, m_e = 9.109×10⁻³¹ kg, m_p = 1.673×10⁻²⁷ kg, μ_B = 9.274×10⁻²⁴ J/T, k_B not needed. Recompute every derived number by hand; a reviewer will.
- **No claims beyond what was read:** `exteral_resources/` (Susskind PDF, Collins PDF) may be named as optional reading only; do not summarise files you did not read.
- **Anonymity:** no learner name, email or user handle in any content file.
- **No git commands in any subagent dispatch.** Commits only by the controller at checkpoints. No network. No subagents spawned by implementers.
- **Each subagent writes exactly the files assigned to its task, nothing more.**
- **Style:** plain-English first, then symbols; say every symbol aloud on first use; short paragraphs; picture/intuition before formalism; keep `\hat{}`, `\langle\cdot|\cdot\rangle`, `\mathrm{d}` conventions of the existing files. Glance at `content/day02.md` (first ~80 lines) for tone.
- **Time box per P-file (~90 min):** warm-up 10 · moves 40 · exercises 30 · apply/bridge + confusion log 10. Target 2500–3800 words.
- **Verification is scoped to the rule** (V-checks below run over the whole tree, not just new files).

## Target Layout (additions in bold)

```
foundations_sprint/
├── README.md            MODIFIED (Task 7)
├── STRATEGY.md          MODIFIED (Task 7)
├── content/
│   ├── GLOSSARY.md      MODIFIED (Task 6)
│   ├── day01.md day02.md day04.md day06.md day07.md   MODIFIED: one-line pointer only (Task 7)
│   ├── physics/         NEW
│   │   ├── P1.md  P2.md  P3.md  P4.md  P5.md          (Tasks 1–5)
│   └── companions/      unchanged
```

## Physics Move Registry (IDs fixed — copied from the spec)

| ID | Move | File |
|---|---|---|
| P1.1 | Newtonian state: x, v, a, p = mv; determinism (W1 §1.1) | P1 |
| P1.2 | Force from potential F = −dV/dx; Newton's second law as a differential equation | P1 |
| P1.3 | Energy: p²/2m + V (the classical Hamiltonian) | P1 |
| P1.4 | SI units, eV, sizes of ħ and h; dimensional analysis | P1 |
| P1.5 | Bridge: classical (x,p) vs quantum ψ; Ĥ = p̂²/2m + V, p̂ = −iħ∂/∂x | P1 |
| P2.1 | Waves: A, λ, f, k = 2π/λ, ω = 2πf, v = fλ | P2 |
| P2.2 | Superposition, interference, double-slit pattern | P2 |
| P2.3 | Complex plane wave e^{i(kx−ωt)} | P2 |
| P2.4 | Planck E = hf; blackbody, photoelectric effect; photon p = h/λ | P2 |
| P2.5 | de Broglie λ = h/p; wave–particle duality; amplitudes add, not probabilities | P2 |
| P2.6 | Bridge: e^{ikx} has p = ħk, E = ħ²k²/2m (W4 §4.2); discrete lines and E_n (W3 §3.1) | P2 |
| P3.1 | Classical spring: F = −kx, ω = √(k/m), x(t), energy exchange | P3 |
| P3.2 | Classical probability distribution of a mass on a spring | P3 |
| P3.3 | Standing waves and confinement ⇒ quantised λ ⇒ E_n ∝ n² | P3 |
| P3.4 | Zero-point energy; wave form of the uncertainty principle | P3 |
| P3.5 | Bridge: E_n = ħω(n + ½); the ground state is not "at rest" | P3 |
| P4.1 | Magnetic field, magnetic moment, torque, dipole energy | P4 |
| P4.2 | Force on a dipole needs a field gradient | P4 |
| P4.3 | Classical angular momentum and the classical (continuous) deflection prediction | P4 |
| P4.4 | Spin as intrinsic angular momentum; S_z = ±ħ/2 (convention); two beams | P4 |
| P4.5 | Sequential Stern-Gerlach; interference; link to spin-½ states and Pauli matrices (Day 3) | P4 |
| P5.1 | Photon polarisation as a two-state system; Malus cos²θ = Born |c|² | P5 |
| P5.2 | Entanglement/EPR/Bell at concept level; correlated ≠ communicating | P5 |
| P5.3 | Interpretations in neutral language (W3 §3.4) | P5 |
| P5.4 | Quantum tech at lecture level: key distribution (W7 §7.4), spin sensing | P5 |
| P5.5 | Physical-reasoning kit: units, order of magnitude, limiting case, symmetry | P5 |

## Verification Commands (controller runs these at checkpoints)

From `foundations_sprint/`. Each check's scope equals its rule's scope; if a check fails on every file, suspect the check first.

```bash
# V1: hint = sketch counts, non-zero, over ALL content files
for f in content/day0*.md content/companions/*.md content/physics/*.md; do
  h=$(grep -o '\*\*Hint:\*\*' "$f" | wc -l); s=$(grep -o '\*\*Solution sketch:\*\*' "$f" | wc -l)
  [ "$h" -eq "$s" ] && [ "$h" -gt 0 ] || echo "FAIL $f h=$h s=$s"
done; echo V1 done
# V2: no learner identity in anything the learner reads
grep -rniE 'hung|hunghd|le\.hoang|redkyo' content README.md STRATEGY.md && echo "V2 FAIL" || echo "V2 ok"
# V3: no code scaffold
[ ! -e code ] && [ ! -e labs ] && echo "V3 ok" || echo "V3 FAIL"
# V4: no placeholders
grep -rnE 'TBD|TODO|FIXME|lorem|\.\.\.\]|<[A-Z][a-z]+ ?[a-z]*>' content README.md STRATEGY.md && echo "V4 FAIL" || echo "V4 ok"
# V5: physics files only — lecture sources named, constants labelled, units check present
for f in content/physics/P*.md; do
  grep -q 'week_' "$f" || echo "V5 no lecture source named: $f"
  grep -qi 'standard value' "$f" || echo "V5 note: no '(standard value)' label in $f (ok only if it uses no non-lecture constants)"
  grep -qi 'units' "$f" || echo "V5 FAIL no units discussion: $f"
done; echo V5 done
# V6: glossary anchors — every ](#id) has an id="…"
python3 - <<'EOF'
import re
t=open('content/GLOSSARY.md',encoding='utf-8').read()
ids=set(re.findall(r'id="([^"]+)"',t)); links=re.findall(r'\]\(#([^)\s]+)\)',t)
print('V6 ids',len(ids),'links',len(links),'unresolved',[l for l in links if l not in ids][:5])
EOF
# V7: relative links to files resolve everywhere
python3 - <<'EOF'
import re,os,glob
bad=0
for f in glob.glob('**/*.md',recursive=True):
    if f.startswith('docs/'): continue
    for m in re.finditer(r'\]\(([^)\s#]+)(#[^)\s]*)?\)',open(f,encoding='utf-8').read()):
        t=m.group(1)
        if t.startswith(('http','mailto:')): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f),t))): print('MISSING',f,t); bad+=1
print('V7 missing files:',bad)
EOF
```

## Tasks

### Task 1: P1 — Energy and classical state

**Files:**
- Create: `content/physics/P1.md`

**Interfaces:**
- Consumes: maths Moves 1.x–2.x only for warm-up (Day 1 complex numbers, Day 2 kets).
- Produces: Moves P1.1–P1.5 as `### Move P1.k — <name>` headings. Glossary terms defined here: *Newton's second law, force, potential energy, kinetic energy, momentum, total energy (classical Hamiltonian), determinism, SI units, joule, electron-volt, dimensional analysis, Planck's constant h, reduced Planck constant ħ, classical state*.

- [ ] **Step 1: Read** the spec's *Physics File Skeleton* and Success Criteria 1–2; `week_1/week_1_lecture.md` §1.1, Hamiltonian (Eq. 1.11) and momentum operator (Eq. 1.23); `week_4/week_4_lecture.md` §4.1 (why Ĥ appears).
- [ ] **Step 2: Write `content/physics/P1.md`** per the skeleton, ~90 min. Specifics:
  - *Warm-up:* 5 questions from Day 1 (conjugate, modulus, Euler at π, double-angle) and Day 2 (ket/bra) — no earlier P-file exists; answers folded.
  - *Moves:* P1.1–P1.5 exactly as in the registry; worked examples on **new objects** (a 2 kg trolley, a ball thrown upward, a 1 kg mass in a linear potential V = αx, an electron at 1 eV). P1.4 must include: SI base units used in QM, joule, eV↔J (standard value 1 eV = 1.602×10⁻¹⁹ J), sizes of ħ (from the lecture) and h (standard value), and the dimensional-analysis method as a 4-step recipe. P1.5 must give the bridge: classical Hamiltonian E = p²/2m + V ↔ operator Ĥ = p̂²/2m + V with p̂ = −iħ ∂/∂x (lecture Eq. 1.23 in 1D) and the sentence that both p̂ forms in the path are the same; state that determinism (given x(0), v(0)) becomes "given ψ(x,0)" (lecture §1.1) — do not solve any Schrödinger equation here.
  - *Exercises (9–11), all with hints and sketches, numerical ones with a units check:* (1) kinetic energy of an electron at 2.0×10⁶ m/s in J and eV; (2) F = −dV/dx for V = αx and V = ½kx² (state the force on the mass); (3) constant force → x(t) from x(0), v(0) (Newton's second law integrated twice); (4) energy conservation for a ball thrown upward (max height); (5) unit check of ω = √(k/m) and of E = p²/2m; (6) the units of ħ from ħ = h/2π and check J·s = kg·m²/s; (7) momentum of a 1.0 g bullet at 300 m/s vs an electron at 1.0×10⁶ m/s, and the ratio of ħ to each momentum·(1 nm) as an order-of-magnitude "how quantum is it?" comparison; (8) write the classical Hamiltonian for a free particle and for V = ½mω²x², then write the corresponding Ĥ by replacing p → p̂ (no solving); (9) explain in two sentences what changes between "state = (x, p)" and "state = ψ(x)" — a short-answer with a checklist-style sketch; (10) a limiting-case check: does E = p²/2m + V reduce correctly when V = 0.
  - *Apply to the lecture:* re-read W1 §1.1 and the Hamiltonian/momentum operator passages; name what to look for; name the Day 4 Move 4.8 and Day 1 pointers.
  - *Anti-patterns:* mixing p and v; forgetting eV↔J; treating ħ as small "so ignore it".
- [ ] **Step 3: Verify:** V1 on this file; headings `Move P1.1`…`Move P1.5` present; word count 2500–3800; grep the file for `week_1` (source named) and `standard value`.

### Task 2: P2 — Waves, light and the birth of QM

**Files:**
- Create: `content/physics/P2.md`

**Interfaces:**
- Consumes: Move 1.3 (Euler), P1.4 (units, eV), P1.5 (bridge).
- Produces: Moves P2.1–P2.6. Glossary terms: *wave, amplitude, wavelength, frequency, wavenumber, angular frequency, wave speed, interference (constructive/destructive), double-slit experiment, plane wave, photon, Planck relation, photoelectric effect, work function, blackbody radiation, de Broglie wavelength, wave–particle duality, probability amplitude (physical), spectral line*.

- [ ] **Step 1: Read** `week_1/week_1_lecture.md` §1.1 and `week_1/week_1_references.md`; `week_3/week_3_lecture.md` §3.1 (spectral lines); `week_4/week_4_lecture.md` §4.2 (e^{ikx}, Eqs. 4.9–4.13); `week_6/week_6_lecture.md` §6.4 (quantum interference); success criteria 3–5.
- [ ] **Step 2: Write `content/physics/P2.md`** per the skeleton. Specifics:
  - *Warm-up:* five questions on P1 (units, KE in eV, dimensional check) and Day 1 (e^{iθ}).
  - *Moves* as in the registry, with worked examples on new objects: a 5.0 Hz rope wave; 500 nm light (photon energy in J and eV; standard values); a photoelectric threshold with a work function of 2.30 eV (state the numerical threshold wavelength; standard values); the electron de Broglie wavelength at 150 eV (≈ 0.100 nm — recompute exactly); a baseball's de Broglie wavelength for contrast (≈ 10⁻³⁴ m scale).
  - P2.2 must explain **why amplitudes add** (two-path picture with signs) without any numeric interference result that a course task asks for; P2.3 must show e^{i(kx−ωt)} as cos + i sin and explain modulus-squared constancy; P2.5 must state the double-slit electron result in words and connect to "single electrons build up an interference pattern one dot at a time".
  - P2.6 bridge (must agree exactly with W4 §4.2): substituting ψ = e^{ikx} into −(ħ²/2m)ψ″ = Eψ gives E = ħ²k²/2m; comparing with E = p²/2m gives p = ħk; λ = 2π/|k| ⇒ p = h/λ = de Broglie. Discrete spectral lines (W3 §3.1) as evidence that energy eigenvalues are discrete. Do NOT compute anything with the hydrogen wave function e^{−r/a₀}.
  - *Exercises (9–11):* f, λ, k, ω conversions (light and sound); photon energy of 450 nm light; threshold frequency for a 3.10 eV work function; kinetic energy of the ejected electron for 250 nm light on it (standard values, show units check); de Broglie wavelength of a 1.0 keV electron and a proton at the same kinetic energy; two-slit fringe spacing Δy = λL/d for numbers of your choice (state the formula as a standard result); two amplitudes 0.6 and ±0.6 added: which gives darkness, and why probabilities cannot be added first; show |e^{i(kx−ωt)}|² = 1; check p = ħk for a plane wave at k = 5.0×10⁹ m⁻¹ (electron speed); a short-answer: why does a double-slit with individual electrons still show interference?
  - *Apply:* W1 §1.1/references (history), W3 §3.1, W4 §4.2, W6 §6.4; pointers to Day 4 Move 4.8, P1.
  - *Anti-patterns:* adding probabilities instead of amplitudes; mixing f and ω; treating "wave–particle duality" as "sometimes a wave, sometimes a particle".
- [ ] **Step 3: Verify:** V1; headings `Move P2.1`…`Move P2.6`; grep `week_4` and `standard value`; recompute every numeric value in the file (a reviewer will).

### Task 3: P3 — Springs, standing waves and confinement

**Files:**
- Create: `content/physics/P3.md`

**Interfaces:**
- Consumes: P1.3 (energy), P2.1/P2.5 (waves, de Broglie), Day 5 Move 5.5 and Day 6 (box and oscillator maths).
- Produces: Moves P3.1–P3.5. Glossary terms: *simple harmonic motion, spring constant, period, turning point, standing wave, node, confinement, quantisation (physical), energy level, zero-point energy, uncertainty principle (Δx Δk form), Heisenberg's relation*.

- [ ] **Step 1: Read** `week_5/week_5_lecture.md` §5.1; `week_4/week_4_lecture.md` §4.3; `week_5/week_5_content.md` (Apply/Consolidate — for the integrity list only, not to solve); `content/day05.md` Move 5.5 and `content/day06.md` Moves 6.1/6.4 (to stay consistent); success criteria 5–6.
- [ ] **Step 2: Write `content/physics/P3.md`** per the skeleton. Specifics:
  - *Warm-up:* five questions on P1–P2 (energy units, de Broglie, k↔λ) and Day 5 (state expansion probabilities).
  - *Moves:* P3.1: F = −kx, ω = √(k/m) (lecture §5.1), x(t) = A cos(ωt+φ), period T = 2π/ω, energy ½mv² + ½kx² constant; worked example on a 0.50 kg block and k = 200 N/m (compute ω, T, total energy for A = 0.10 m). P3.2: classical probability of finding the mass in dx ∝ time spent ∝ 1/|v|, so larger near turning points (qualitative sketch description; state the result, no derivation of the arcsine law needed). P3.3: standing waves on a string of length L fixed at both ends, λ_n = 2L/n; apply de Broglie λ = h/p and E = p²/2m ⇒ E_n = n²h²/(8mL²) = n²π²ħ²/(2mL²); state that this agrees with Day 5 Move 5.5 (which derives it from the Schrödinger equation with boundary conditions); numeric example: electron in a 1.00 nm box (ground energy ≈ 0.376 eV — recompute). P3.4: zero-point energy from confinement (E_1 ≠ 0) and a wave-form uncertainty relation Δx Δk ≳ ½ (state as a standard result); a rough estimate E ~ ħ²/(2m(Δx)²) for Δx = L. P3.5 bridge: the quantum oscillator's energies E_n = ħω(n+½) (lecture §5.4, Eq. as numbered there — check) are equally spaced, non-zero at n=0; contrast with the classical oscillator's continuum of energies and its 1/|v| distribution; do NOT evaluate ⟨x²⟩, σ_x, σ_p, or the uncertainty product for the ground state.
  - *Exercises (9–11):* ω and T for two (m, k) pairs; total energy and max speed for given A; turning points from E = ½kx²; classical time-averaged claim: at which x is the mass fastest/slowest and where is it most likely found; standing-wave wavelengths for n = 1,2,3 on L = 0.80 m; box energy of an electron for L = 0.50 nm at n = 1,2,3 (eV) and the wavelength of the photon emitted for 2→1 (standard values, units check); how the ground energy scales when L is halved; a proton in a 1 fm box (order of magnitude of E_1 in MeV, recompute); order-of-magnitude zero-point energy of an electron confined to an atom-sized region (0.1 nm); a limiting-case check: E_n spacing as L → ∞ (levels merge → classical continuum); a short-answer contrasting classical and quantum probability distributions for an oscillator.
  - *Apply:* W4 §4.3 and W5 §5.1–5.5; Day 5 Move 5.5; Day 6; the Week 5 companion (name sections).
  - *Anti-patterns:* thinking the ground state has zero energy; using ħ where h is needed; confusing n=0 and n=1 labelling between box and oscillator.
- [ ] **Step 3: Verify:** V1; headings `Move P3.1`…`Move P3.5`; grep `week_5` and `week_4`; recompute all numbers; grep the file for `\\sigma_x` and `\\langle x\^2` — neither may be *evaluated* for ψ₀ (a mention in a "not here" note is fine).

### Task 4: P4 — Magnetism and spin

**Files:**
- Create: `content/physics/P4.md`

**Interfaces:**
- Consumes: P1.3 (energy), Day 3 Move 3.4 (Pauli matrices, ±z/±x states), W6 companion conventions (ħ/2 flagged; Eq. 6.2 phase note).
- Produces: Moves P4.1–P4.5. Glossary terms: *magnetic field, magnetic moment, torque, dipole energy, inhomogeneous field, field gradient, angular momentum (orbital), spin, quantised spin, Stern-Gerlach apparatus, Bohr magneton (standard value), beam splitting, sequential measurement*.

- [ ] **Step 1: Read** `week_6/week_6_lecture.md` in full; `week_6/week_6_content.md` Apply (for the integrity rule) and quiz; `content/companions/week06_companion.md` (so P4 is consistent with it and does not duplicate its clones or its essay structure); `content/day03.md` Move 3.4; success criterion 7.
- [ ] **Step 2: Write `content/physics/P4.md`** per the skeleton. Specifics:
  - *Warm-up:* five questions on P3 (box energy scaling, zero-point) and Day 3 (Pauli σ_z eigenvalues).
  - *Moves:* P4.1: field B, magnetic moment μ, torque τ = μ × B, dipole energy U = −μ·B; worked example with μ = μ_B (standard value 9.274×10⁻²⁴ J/T) in B = 1.00 T (energy in J and eV, ≈ 5.79×10⁻⁵ eV — recompute); P4.2: force F_z = μ_z ∂B_z/∂z — uniform field gives torque but no net force, so an *inhomogeneous* field is required (link W6 §6.1); P4.3: classical angular momentum L = r × p, classical moment orientation is arbitrary ⇒ a **continuous smear** of deflections is predicted; P4.4: spin as intrinsic angular momentum, observed **two** beams, S_z = ±ħ/2 (label: convention, not given in the lecture); silver atoms (as in the lecture) — one unpaired outer electron carries the moment (state as standard background); P4.5: sequential magnets at the level of W6 §6.2–6.4 using the lecture's |ψ_z^±⟩, |ψ_x^±⟩ notation, magnitude table Eq. 6.2 with the phase caveat from the W6 companion; short explanation of why removing the middle magnet's blocking restores the beam (interference) — physics description, no numeric result the course task asks for.
  - **Integrity:** describe *what is observed and why*; do not rank the results or write "the most important implications"; no essay outline; no essay prose.
  - *Exercises (8–10):* torque and dipole energy numbers for a given μ and angle; force on a moment in a gradient of 10 T/m (standard value μ_B; compute the force and the acceleration of a silver atom of mass 1.79×10⁻²⁵ kg (standard value) — recompute); why a uniform field gives no beam splitting (short answer); classical prediction vs observed pattern (short answer); the eigenvalues of S_z = (ħ/2)σ_z and probabilities for a given spin state using **new angles** (e.g. a state (√3/2)|↑⟩ + (1/2)|↓⟩ — check normalisation first); a two-magnet sequence z then x (probability of "up" after each) — different states than the W6 companion's 60° example; a "predict the beam pattern" question for three magnets with new orientations described qualitatively; a units check for F = μ dB/dz.
  - *Apply:* W6 lecture §6.1–6.4; W6 companion sections (name them); Day 3; the Week 6 quiz themes (do not answer quiz items).
  - *Anti-patterns:* thinking spin is a literal spinning ball; forgetting the gradient; assuming a second magnet "does nothing" to a spin-polarised beam.
- [ ] **Step 3: Verify:** V1; headings `Move P4.1`…`Move P4.5`; grep `week_6`; grep the file for the phrases `most important` and `key implication` — must appear only inside a "left to you" note or not at all; recompute all numbers.

### Task 5: P5 — Measurement, interpretations and quantum technology

**Files:**
- Create: `content/physics/P5.md`

**Interfaces:**
- Consumes: P2.5 (amplitudes), P4.4/P4.5 (spin-½ as two-state), Day 7 Moves 7.1–7.5 (tensor products, product-state test, Bell states, correlation ≠ communication).
- Produces: Moves P5.1–P5.5. Glossary terms: *polarisation, polariser, Malus's law, qubit (physical), photon polarisation state, EPR paradox, Bell inequality (concept), hidden variables, Copenhagen interpretation, many-worlds (as named in the lecture), decoherence (only if the lecture uses it), key distribution, eavesdropper, sifted key, quantum sensing, order of magnitude, limiting case, symmetry check*.

- [ ] **Step 1: Read** `week_3/week_3_lecture.md` §3.4 (interpretations — use exactly what it names); `week_7/week_7_lecture.md` §7.2 and §7.4 in full; `content/day07.md` Move 7.5; `content/companions/week07_companion.md`; `week_7/week_7_content.md` (Apply/Consolidate, for the integrity list); `week_4/week_4_content.md` Task 2 (integrity list); success criteria 8–9. If the lecture does not name an interpretation or protocol, do not add detail beyond one neutral sentence and a pointer to the optional reading in `exteral_resources/`.
- [ ] **Step 2: Write `content/physics/P5.md`** per the skeleton. Specifics:
  - *Warm-up:* five questions on P2 (amplitudes), P4 (two-state spin) and Day 7 (product state test statement).
  - *Moves:* P5.1: photon polarisation as a 2-state system with |H⟩,|V⟩; Malus's law I = I₀cos²θ; identification with |c|² = cos²θ (Born rule); numeric example with polarisers at 0°, 35°, 90° (recompute); P5.2: EPR/Bell at concept level — what "local hidden variables" means, that Bell-type experiments rule them out (state at the level the lecture does), correlated ≠ communicating (no faster-than-light signalling), link to Day 7 Move 7.5; do NOT perform product-state proofs or any partial-measurement calculation on the course's W7 states; P5.3: interpretations in **neutral language, two sentences each**, only those named in W3 §3.4, plus the statement that all agree on the measurement statistics; no misconceptions post; P5.4: quantum key distribution as described in W7 §7.4 (say what the lecture says, then a plain-English recap: choose random bases, keep matching-basis results, disturbance reveals an eavesdropper; give the sifting fraction as ½ with a small numeric example on new numbers); spin sensing: one paragraph linking to W6 (magnetic-field sensitivity of spin states) at the level of the module's aim, flagged as background; P5.5: the physical-reasoning kit as a 4-step recipe with three worked checks on QM results *not* in the course tasks (e.g. units of the box energy, the limit L → ∞, a symmetry check of a two-qubit state under swapping the qubits, order-of-magnitude of the de Broglie wavelength of a room-temperature electron).
  - **Integrity:** no essay prose; no ready-made misconceptions list; nothing that solves W7 P1–P3 or the portfolio correlation problem.
  - *Exercises (9–11):* three-polariser intensity with new angles (0°, 30°, 90°) and the intensity with the middle polariser removed; identify θ for a given fraction transmitted; a photon polarisation state (cosα|H⟩ + sinα|V⟩) → probabilities of H and V at α = 20°; sifting: how many bits survive out of 400 with random bases, and what an intercept-resend eavesdropper does to the error rate as stated in the lecture (only if the lecture states it; otherwise say "outside this module"); a units check on a new QM formula; a limiting-case check (Malus at θ = 0° and 90°; box energies as L → ∞); a symmetry check on a given two-qubit state (new state); an order-of-magnitude estimate (electron de Broglie wavelength at 300 K thermal kinetic energy, standard k_B if used — label it); a short-answer "correlated vs communicates" scenario question.
  - *Apply:* W3 §3.4, W6, W7 §7.2/7.4; W7 companion sections; the two optional PDFs by name only.
  - *Anti-patterns:* saying "measurement needs a conscious observer"; saying entanglement sends signals; treating an interpretation as a different set of predictions.
- [ ] **Step 3: Verify:** V1; headings `Move P5.1`…`Move P5.5`; grep `week_7` and `week_3`; recompute all numbers; grep for `\\frac\{1\}\{\\sqrt\{2\}\} \(\|\\uparrow\\downarrow` — the W7 singlet must not be worked.

> **CHECKPOINT A (controller only, after Tasks 1–5, no agent running):** run V1–V5, then commit `WIP: physics P1-P5 (scratch)` on the scratch branch. Then dispatch two batch reviewers (P1–P3; P4–P5) who hand-recompute every number and check integrity, constants, lecture fidelity. Fix in one round; controller recomputes changed numbers.

### Task 6: GLOSSARY — physics sections

**Files:**
- Modify: `content/GLOSSARY.md` (append; do not reorder or delete existing entries)

**Interfaces:**
- Consumes: the "Glossary terms" lines of Tasks 1–5 and the final text of `content/physics/P1.md`–`P5.md`.
- Produces: new sections `## Physics P1 — Energy and classical state` … `## Physics P5 — Measurement, interpretations and quantum technology`; new A–Z index links; every new entry has an explicit anchor `<a id="…"></a>` with a unique id.

- [ ] **Step 1: Read** all five P-files (final text) and the existing GLOSSARY entry format and anchor scheme (first ~40 lines of the Day-1 section, and the index).
- [ ] **Step 2: Append** the five physics sections after the existing Day sections and before "Companion-only terms" is *not* required — put them after "Companion-only terms". Entries follow `**term / symbol** — *say it as:* … — *meaning:* one sentence — *tiny example:* … — *see:* [P<N>](physics/P<N>.md), Move P<N>.k — *Commonly confused with:* (only where a real trap exists: wavelength vs wavenumber, frequency vs angular frequency, momentum vs velocity, kinetic vs total energy, force vs field gradient, spin vs orbital angular momentum, correlated vs communicating, interpretation vs prediction). Every term listed in Tasks 1–5 must have an entry; add every symbol first used in the P-files (λ, f, k, ω, h, ħ, eV, μ, τ, U, B, L, S_z). Add the new entries to the A–Z index in alphabetical position among existing links. Tiny examples must use objects not in the course problems. Where a term already exists in the glossary (e.g. *plane wave*, *uncertainty relation*, *zero-point*), do not duplicate it: add a "Physics view:" sentence and a link to the P-file inside the existing entry instead.
- [ ] **Step 3: Verify:** V6 (`ids` = number of unique anchors, `links` = index links, `unresolved` empty); every term named in Tasks 1–5 "Glossary terms" appears (loop with `grep -qi`); no duplicate `id="…"`; V2 and V4.

### Task 7: README, STRATEGY and day pointers

**Files:**
- Modify: `README.md`, `STRATEGY.md`, `content/day01.md`, `content/day02.md`, `content/day04.md`, `content/day06.md`, `content/day07.md`

**Interfaces:**
- Consumes: the spec's timetable and the P-file titles.
- Produces: README section `## Physics Sprint`, a combined 7-day timetable, links `[P<N>](content/physics/P<N>.md)`; STRATEGY paragraph; five one-line pointers.

- [ ] **Step 1: Read** README.md and STRATEGY.md in full; the first 12 lines of each of the five day files.
- [ ] **Step 2: Edit `README.md`:** replace the 7-day table with the combined timetable from the spec (Day / Maths / Physics / Day total / Deadline link); add `## Physics Sprint` (why it exists in two sentences, the five files with one line each, the ~1.5 h shape, the priority rule: P1–P2 before Assessment 1, P4–P5 can slide later); update the total time (~32 h), the directory map, and add `content/physics/P1–P5.md` links. Keep the existing integrity, six-steps-stand-in and lecture-quirks notes.
- [ ] **Step 3: Edit `STRATEGY.md`:** add one short paragraph (under `## The Strategy`) — every physics idea is learned with its quantum bridge (classical version → quantum version → what breaks), and the physical-reasoning kit (P5.5: units, order of magnitude, limiting case, symmetry) is the physics half of step 5 ("Check") of the six-steps stand-in. Do not rename or renumber any existing heading (other files link to `#five-pass-lecture-protocol` and `#six-steps-write-up-stand-in`).
- [ ] **Step 4: Add exactly one line** near the top of each of `day01.md` (P1), `day02.md` (P2), `day04.md` (P3), `day06.md` (P4), `day07.md` (P5): `> **Physics pair for today:** [P<N> — <title>](physics/P<N>.md) (~1.5 h).` Change nothing else in those files.
- [ ] **Step 5: Verify:** V1, V2, V4, V7; README links to all five P-files; the day files still have equal hint/sketch counts; `git`-free diff check by grep that only the one line was added (count lines containing `Physics pair for today` = 5 across `content/day0*.md`).

> **CHECKPOINT B / FINAL (controller only, no agent running):** run V1–V7 over the whole tree; one final reviewer pass (Sonnet, scoped to: README/STRATEGY/glossary additions, the five pointers, and a re-verification of any numbers changed in the checkpoint-A fix round); commit; then the five-line teardown from `skill.md` (`git reset --soft master` → `git switch master` → `git reset` → `git branch -D authoring/module3-physics-sprint` → `git status`), and delete the plan's SDD workspace.
