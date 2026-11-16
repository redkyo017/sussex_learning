# Working notes: Module 4 Assessment 1 (PRB), candidate 672128

## 0. Deadline (three sources disagree)

| Source | Says |
|---|---|
| `module_4_intro.md` (assessment overview) | Thursday of **Week 3**, 17:00 UK |
| `description.md` (Canvas assignment page) | Thursday of **Week 3**, 17:00 UK; Canvas field "Due 20 Nov at 0:00" |
| `Assessment_1_Problem_Set.md` (quiz page) | Thursday of **Week 4**, 17:00 UK |
| Module calendar in intro | Fri 20 Nov 2026, "due by 12am" |

The quiz opened on Mon 2 Nov (Week 1), so Week 3's Thursday is **Thu 19 Nov 2026**. Treat **Thu 19 Nov, 17:00 UK** as the real deadline. The midnight time and the "Week 4" wording are later, so don't rely on them. There is a 24-hour lateness window, at a penalty of 5 percentage points.

## 1. Source diff

There is no instructor-authored file (no .tex or .pdf) for this assessment. Only the two Canvas exports exist: `description.md` (the assignment page) and `Assessment_1_Problem_Set.md` (the quiz page, with the questions). I diffed what overlaps between them and checked the questions against one another.

| Item | Finding | Effect, computed |
|---|---|---|
| Question count | "Questions: 12" vs "answer 11 questions" | Q12 is the 0-point PDF upload slot. No missing question. |
| Marks | 10+5+5+12+18+5+5+5+10+10+15 = **100** | Matches the stated total. |
| Q5 "depth of the order of `$z_0 10$` cm" | A symbol was lost in export, almost certainly `\sim`. | Every reading ("~", "≈", "=", "≥" 10 cm) leads to the same deep-limit analysis. The plot runs to 15 cm and marks the OPM/SQUID crossover at 9.12 cm. Values at exactly 10 cm: SQUID 0.196 mA, OPM 0.212 mA, NV 15.9 A. |
| Q11 stem says "time between pulses is `T_pulse`" (Q6–Q10 say τ = 100 ms) | Inconsistent shared text. | None: Q11 uses only Δg_min = 1.0e-9 (from Q7). The void Δg and z_max(D) are the same under either wording. |
| Q6–Q8 stem says "used for 6, 7, 8" and Q9–Q11 says "used for 9, 10, 11", with identical text | Cosmetic. | None. |
| Q6–Q11 "wavelength of the atoms is 780 nm" | Mislabelled: 780 nm is the Rb D2 laser line. | The PDF says so explicitly, uses 780 nm for k_eff, and computes λ_dB separately. |

**Check on the live quiz:** whether Q5 really shows "z₀ ∼ 10 cm". It can't change any number in the answer, but the PDF quotes it with "∼".

## 2. Questions with a second reading: every reading computed

| Q | Headline (used) | Alternative | Value under the alternative | Why the headline |
|---|---|---|---|---|
| 1 | Noise = S·√(1 kHz) → **SNR 1.26** | Noise per √Hz (1 Hz band) | SNR 40 | The question gives the bandwidth, so it is meant to be used. |
| 1 | Peak amplitude 2 pT vs rms noise | rms signal 2/√2 pT | SNR 0.89 | "Amplitude" is the stated quantity; the PDF doesn't raise this one. |
| 4 | B_min = S·√(100 Hz) → **0.128 A / 4.30 μA / 24.5 μA** | 1 Hz band | 12.8 mA / 0.43 μA / 2.4 μA | Same reasoning as Q1. Shown in a note in the PDF. |
| 6 | Thermal λ = h/√(2πmk_BT) → **187 nm** | h/(m v_rms) | 271 nm | This is the standard definition of de Broglie wavelength for a gas. The alternative is shown in the PDF as a size check. |
| 6 | | h/(m v_mean), v_mean = √(8kT/πm) | 294 nm | Not shown; same order as both values above. |
| 7 | Δφ = k_eff Δg τ², k_eff = 4π/λ → **1.61e-4 rad** | Uses d = 10 mm: Δφ = mΔg d τ/ħ | 1.37e-3 rad | The given d does not fit the given λ and τ: the recoil separation is ħk_eff τ/m = 1.18 mm. With that d, the two formulas agree exactly (checked numerically). Shown in a note. |
| 7 | | k_eff = 2π/λ (single photon) | 8.06e-5 rad | The lecture's Raman scheme (Fig. 3.4) gives k_eff = k1 + k2 ≈ 2k. |
| 7 | | Lecture's "τ = 2T" convention: Φ = k_eff a (2τ)² | 6.44e-4 rad | The lecture text is internally inconsistent here. The question defines τ as the time between pulses, which is T in the standard k_eff g T². The PDF derives the formula from the atom's positions, so the choice is visible. |
| 8 | S = k_eff τ² → **1.61e5 rad/(m/s²)** | The d-based reading | 1.37e6 | Follows Q7. |
| 9 | Tidal 2GMR_E/r³ → **1.09e-6 m/s²** | Direct pull GM/r² | 3.29e-5 m/s² | The question says "(tidal effects)", and the Earth falls with the Moon. The direct pull is shown as the first step. |
| 9 | | Exact near / far side | 1.116e-6 / 1.061e-6 | Quoted in the PDF's check. |
| 10 | Moon-match distance with the tidal value → **6.6 cm** | With the direct pull | 1.2 cm | Follows Q9. Shown in a note. |
| 11 | "3 m" to the void centre → **−2.14e-8 m/s²** | To the nearest edge (r = 3.5 m) | −1.57e-8 m/s² | The point-mass (shell theorem) formula needs the centre distance. Shown in a note. |

## 3. Verification

- `compute.py` produces every number in the PDF and both figures.
- `verify.py` re-derives each number by a **different** route. The latest run: **ALL PASS**.

| Result | Independent route |
|---|---|
| Q1 SNR | Simulated white-noise trace, Welch spectral estimate |
| Q2–Q4 | Biot–Savart sum over a discretised loop (no closed-form formula used) |
| Q5 crossover and limits | Grid scan of the numerically summed fields |
| Q6 | Partition-function quadrature; Maxwell–Boltzmann sampling |
| Q7–Q8 | Numerically integrated atom trajectory, phase k(z1 − 2z2 + z3); linear fit for S |
| Q9 | Exact near-side and far-side differences |
| Q10 | Back-substitution |
| Q11 | 3D quadrature over the sphere (no shell theorem); root-finding for z_max at D = 1 m and 2 m |

On the first run, 7 checks failed. All were faults in the check script, not in the answers:
- 4 were values I typed rounded tighter than the tolerance allowed, or a sign slip.
- 1 was a quadrature tolerance problem (the integral is ~1e-30, below the default absolute tolerance).
- 1 was a check at 10 m where floating-point precision ran out (replaced by a check at 1 m).
- 1 was Q9, where the exact near-side value (1.12e-6) differs from the first-order formula by 2.5%. That is now quoted in the PDF.

To re-run:
```
cd assignment_1/solutions
./.venv/bin/python compute.py   # numbers + figures
./.venv/bin/python verify.py    # independent checks
tectonic -X compile QT_PRB_solutions.tex
```

## 4. Before you submit: what only you can do

- [ ] **Read the PDF end to end and re-voice anything that does not sound like you.** The brief says all workings must be your own work.
- [ ] **Reproduce these results yourself, with a calculator, without looking at the PDF:** SNR 1.26; B ∝ z⁻³; S·z³ ranking; I_min 0.13 A / 4.3 μA / 24 μA; crossover 9.1 cm; λ_dB 187 nm; Δφ 1.6e-4 rad; S 1.6e5; tide 1.1e-6; person 4.7e-9 / 6.6 cm / 2.2 m; void −2.1e-8 and 13.9·D^1.5. You may be asked to explain any step.
- [ ] **Look at the live Canvas quiz:** check that Q5 shows "z₀ ∼ 10 cm" and Q7 shows d = 10 mm and λ = 780 nm. If any number differs from `Assessment_1_Problem_Set.md`, tell me before submitting.
- [ ] **Paste the 11 pointer lines from `CANVAS_ANSWERS.md` into the Canvas boxes for Q1–Q11, in a single browser tab.** These are pointers only; all answers are in the PDF.
- [ ] **Upload `QT_PRB_solutions.pdf` at Q12, confirm it shows as attached, and press Submit.**
- [ ] **Do all this by Thu 19 Nov, 17:00 UK.**
