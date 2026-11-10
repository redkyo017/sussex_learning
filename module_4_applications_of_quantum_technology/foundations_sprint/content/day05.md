# Day 05: Sensing Checkpoint (No Notes)

**Time:** ~3 h · **Feeds:** Weeks 1-3 lectures, inventory rows W1 Explore/Apply/Consolidate, W2 Apply/Consolidate, W3 Apply/Consolidate (the A1 problem set is out of scope) · **Companion:** none. After marking, the self-scoring table sends you back to the right Day or companion section.

**Cadence (180 min):**
- 15 min warm-up: the blank-page law sheet (below), closed book.
- 80 min checkpoint items: Exercises 5.1-5.12, no notes, about 6-7 min each.
- 40 min timed writing: Exercise 5.13, one 300-word F1 piece on Harrowmere Water & Power.
- 30 min marking: score the items with the sketches, score the F1 piece with the rubric, fill the self-scoring table.
- 15 min plan: turn every lost point into a confusion-log row and a slot in the A1-window spaced review.

## Why this matters

Days 01-04 gave you seven moves (M1-M7) and two frameworks (F1, F3). Reading them again would feel productive and teach you little. Testing yourself cold is what fixes them in memory (retrieval practice, Roediger & Karpicke 2006, as in STRATEGY.md §9). It also tells you *which* of them have not stuck, so the next three days of 20-minute reviews go where they are needed.

The timing is deliberate. Assessment 1 runs Mon 16 to Thu 19 Nov in a separate session, and the sprint pauses for it. Today is the last full sensing session before that pause. Everything you score below 2 on today goes into the 20-minute daily review slots, not into a fresh read.

The checkpoint mirrors what the module asks of you. Exercises 5.1-5.8 test the numbers you need to follow and reuse Weeks 1-3. Exercises 5.9-5.12 test the habit of catching a wrong or unfair number before you copy it. Exercise 5.13 tests the 300-word gain argument every Consolidate task wants. Every number in Exercises 5.1-5.12 is new: none appears in Days 01-04 or in the lectures, except where a spot-the-error item paraphrases a lecture claim in order to correct it.

## Core concepts

There is nothing new to learn today. This section is the rule book for the checkpoint.

### How to run the checkpoint

1. **Clear the desk.** No day files, no companions, no lecture, no calculator app with history. A plain calculator is allowed: the module never asks you to do $\sqrt{0.0278}$ in your head. The constants box at the top of `## Exercises` is the only reference.
2. **Warm up first (15 min).** Do the blank-page law sheet below before you look at any item.
3. **Items in order, one pass (80 min).** Give each item about 6-7 min. If you are stuck after 8 min, write what you would do next in one line and move on. A partial method still earns half a point.
4. **Do not open any `<details>` block** until all twelve items and the F1 piece are done. The hints are for the second pass, after marking, on items you got wrong.
5. **The F1 piece is timed (40 min).** Start a timer. Stop writing when it rings, mid-sentence if you have to. A 300-word piece written in 55 minutes is not the skill the module tests.
6. **Mark honestly (30 min)** with the rules below, then fill the self-scoring table.

### Warm-up: the blank-page law sheet (15 min, closed book)

On one blank page, write each of the following with its units. Then check against the answers.

1. Noise in a detection (noise) bandwidth from a noise density; the time form. Say how this bandwidth differs from a sensor's own −3 dB bandwidth, and define dynamic range.
2. What slopes of $-1/2$, $0$ and $+1/2$ mean on an Allan plot.
3. Shot-noise and Heisenberg phase limits for $N$ particles.
4. The distance gain for a $1/r^n$ source moved from $r_1$ to $r_2$.
5. $E$ and $\nu$; $Q$; the Ramsey linewidth.
6. Excitation after a resonant pulse; the π/2 and π pulse roles.
7. Fractional error → time → distance.
8. Larmor frequency for ⁸⁷Rb; the flux quantum; the NV dip positions.
9. Mach-Zehnder output; $k_\text{eff}$; the atom-interferometer phase, with $T$ defined.
10. 1 µGal and 1 E in SI units.

<details>
<summary>Warm-up answers</summary>

1. $\delta x = S\sqrt{\Delta f}$ (S in units per √Hz); $\delta x(\tau) \approx S/\sqrt{2\tau}\propto 1/\sqrt\tau$. Here $\Delta f$ is the detection (noise) bandwidth you average over. It is not the sensor bandwidth, which is the −3 dB point of the sensor's response to a changing signal. Dynamic range = full scale / noise floor.
2. White noise, averaging helps; flicker floor, averaging stops helping; random walk or drift, averaging makes it worse.
3. $\delta\phi_\text{SQL} = 1/\sqrt N$; $\delta\phi_\text{HL} = 1/N$ (needs entanglement).
4. $(r_1/r_2)^n$, with $n = 1$ line current, 2 current dipole, 3 magnetic dipole.
5. $E = h\nu$; $Q = \nu/\Delta\nu$; $\Delta\nu \approx 1/(2T)$ for Ramsey free time $T$.
6. $P_1 = \sin^2(\Omega t/2)$; π/2 is the splitter, π is the mirror.
7. $\delta t = y\,\tau$, $\delta x = c\,\delta t$.
8. $f_L = \gamma B$ with $\gamma \approx 7$ Hz/nT; $\Phi_0 = h/2e \approx 2.07\times10^{-15}$ Wb; dips at $2870 \pm 28B$ MHz ($B$ in mT).
9. $I \propto \cos^2(\varphi/2)$; $k_\text{eff} \approx 2k = 4\pi/\lambda$; $\Phi = k_\text{eff} g T^2$, $T$ = time between pulses.
10. $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2 \approx 10^{-9}g$; $1\ \text{E} = 10^{-9}\ \text{s}^{-2}$.

</details>

### Scoring rules for Exercises 5.1-5.12

- Each item is worth **1 point**, so the set is out of 12.
- **1 point:** every part has the right number (within about 5%) *and* the right unit, *and* you can name the move you used.
- **½ point:** the method is right in every part but there is one arithmetic or prefix slip, or one part is missing.
- **0 points:** a wrong law (for example $1/N$ for independent atoms, $\tau = 2T$ in the phase formula), a missing unit on the final answer, or two or more parts missing.
- In the spot-the-error items (5.9, 5.10, 5.12), each error must be *named* and *corrected*. Naming it without the correction is half credit for that error.

A missing unit costs the whole point on purpose. About half the lecture errors in this module are unit or factor errors (`docs/problem_inventory.md`), and an answer without a unit cannot be checked.

### Rubric for the F1 piece (Exercise 5.13)

Six parts, 0-2 points each, out of 12.

| F1 part | 2 points | 1 point | 0 points |
|---|---|---|---|
| 1 Classical limit | Names the classical instrument and gives its limiting number with a unit (fictional label kept) | Names the instrument but the limit has no number, or the number has no unit | No classical baseline |
| 2 Quantum mechanism | One correct sentence of physics (free-falling atoms, three pulses, phase from a wavelength and a time) | Correct but vague ("uses quantum atoms") or more than three sentences | Wrong physics, or the parallelism or "entanglement does it" myth |
| 3 Figure of merit | Names it precisely (absolute repeatability in µGal at a stated time per station, or drift per day) | Names a quantity without saying which (noise or drift or accuracy) | Missing, or "sensitivity" with no meaning |
| 4 Quantified gain | A ratio or a time saved, with both sides measured the same way, plus the target signal size | A number for one side only, or a lab figure compared with a field figure | No number |
| 5 Maturity and practicality | Component vs system TRL (judgement labelled), at least one SWaP-C figure, one named barrier | One of the three | None |
| 6 Verdict and caveat | A clear decision and one specific caveat with a number or a test | A decision with a vague caveat | No decision, or no caveat |

Word count: 270-330 words. Over 330 words, take 1 point off the total. Pass: **8/12 or better, with at least 1 point in parts 1 and 4.** Parts 1 and 4 carry the "quantitative" marks in the module's Consolidate tasks.

## Exercises

**Constants (the only reference allowed).** $h = 6.626\times10^{-34}$ J s; $e = 1.602\times10^{-19}$ C; $c = 3.00\times10^{8}$ m/s; $g = 9.81\ \text{m/s}^2$; 1 day $= 86\,400$ s; 1 year $= 3.156\times10^{7}$ s; ⁸⁷Rb $\gamma = 7$ Hz/nT; NV zero-field splitting 2870 MHz and $\gamma_e = 28$ MHz/mT.

Each solution sketch uses the six steps (Restate, Write state, Name move, Algebra, Check, Answer), shortened. Keep the `<details>` blocks closed until you have finished everything.

### Exercise 5.1 (quantitative)

Quick conversions (M1). (a) Write 0.4 nT in fT. (b) Write 35 µGal in m/s² and as a fraction of $g$. (c) A gradiometer reads 12 E across a 0.8 m vertical baseline. What is $\Delta g$ between the two ends, in µGal? (d) Convert $7\times10^{-8}g$ to µGal.

<details>
<summary>Hint</summary>

**Hint:** Write each prefix as a power of ten. 1 µGal $= 10^{-8}$ m/s². 1 E $= 10^{-9}\ \text{s}^{-2}$, so $\Delta g = (\text{gradient})\times(\text{baseline})$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* four unit conversions. *Write state:* nano $10^{-9}$, femto $10^{-15}$; Gal $= 10^{-2}$ m/s².
- *Name move:* M1.
- *Algebra:* (a) $0.4\times10^{-9}/10^{-15} = 4\times10^{5}$ fT. (b) $35\times10^{-8} = 3.5\times10^{-7}$ m/s²; $/9.81 = 3.6\times10^{-8}$ of $g$. (c) $12\times10^{-9}\times0.8 = 9.6\times10^{-9}$ m/s² $= 0.96$ µGal. (d) $7\times10^{-8}\times9.81 = 6.87\times10^{-7}$ m/s² $= 69$ µGal.
- *Check:* "1 µGal ≈ $10^{-9}g$", so 35 µGal ≈ $3.5\times10^{-8}g$ and $7\times10^{-8}g$ ≈ 70 µGal. Both match.
- *Answer:* $4\times10^{5}$ fT; $3.5\times10^{-7}$ m/s² $\approx 3.6\times10^{-8}g$; 0.96 µGal; about 69 µGal.

</details>

### Exercise 5.2 (quantitative)

Noise density and averaging (M2). A magnetometer has a white noise density of $60\ \text{fT}/\sqrt{\text{Hz}}$. (a) What is its rms noise in a 9 Hz detection (noise) bandwidth? (b) You want to see a steady 40 fT signal with SNR = 4. What detection bandwidth is allowed? (c) Roughly how long must you average, using $\Delta f \approx 1/(2\tau)$?

<details>
<summary>Hint</summary>

**Hint:** $\delta B = S\sqrt{\Delta f}$. For (b), first find the tolerable noise, $40/4$, then invert: $\Delta f = (\delta B/S)^2$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* density to rms noise; then bandwidth and time for a target SNR. *Write state:* $S = 60\ \text{fT}/\sqrt{\text{Hz}}$, $\Delta f = 9$ Hz; target $\delta B = 10$ fT.
- *Name move:* M2 (with M3 for SNR).
- *Algebra:* (a) $60\times\sqrt9 = 180$ fT. (b) $\Delta f = (10/60)^2 = 0.0278$ Hz. (c) $\tau \approx 1/(2\times0.0278) = 18$ s.
- *Check:* units $\text{fT}/\sqrt{\text{Hz}}\times\sqrt{\text{Hz}} = \text{fT}$. A noise 18 times lower needs a bandwidth $18^2 = 324$ times narrower: $9/324 = 0.0278$. Consistent.
- *Answer:* 180 fT rms; $\Delta f \le 0.028$ Hz; about 18 s of averaging, if the noise stays white that long.

</details>

### Exercise 5.3 (quantitative)

Allan-plot reading (M2). A (fictional) rubidium reference is characterised by this Allan deviation table, which is what you would read off its log-log plot:

| $\tau$ (s) | 1 | 10 | 100 | 1000 | $10^{4}$ | $10^{5}$ |
|---|---|---|---|---|---|---|
| $\sigma_y(\tau)$ | $6.0\times10^{-13}$ | $1.9\times10^{-13}$ | $6.0\times10^{-14}$ | $2.2\times10^{-14}$ | $1.5\times10^{-14}$ | $2.4\times10^{-14}$ |

(a) What is the slope between 1 s and 100 s, and what noise does it indicate? (b) If that slope held, how long would you average to reach $3\times10^{-14}$? Is that time inside the region where the slope holds? (c) What is the best stability, and where? (d) The vendor's brochure says "averages to $10^{-15}$ in a day". Is that supported? (e) As an order of magnitude, how much time wander does $\sigma_y$ at the best point imply over that averaging time?

<details>
<summary>Hint</summary>

**Hint:** Slope $= \log_{10}(\sigma_2/\sigma_1)/\log_{10}(\tau_2/\tau_1)$. In the $-1/2$ region, $\tau = (\sigma_1/\sigma_\text{target})^2$ seconds. For (e), time wander $\approx \sigma_y\,\tau$ (an order-of-magnitude estimate only).

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* read slope, extrapolate, find the floor, judge a claim. *Write state:* table above.
- *Name move:* M2 (Allan deviation).
- *Algebra:* (a) $\log_{10}(6.0\times10^{-14}/6.0\times10^{-13})/\log_{10}(100) = -1/2$: white frequency noise. (b) $(6.0\times10^{-13}/3\times10^{-14})^2 = 400$ s. Yes: at 1000 s the table (2.2) is only a little above the white-noise line ($6.0\times10^{-13}/\sqrt{1000} = 1.9\times10^{-14}$), so 400 s is still on the slope. (c) About $1.5\times10^{-14}$ near $10^{4}$ s (the flicker floor). (d) No. After $10^{4}$ s the curve rises ($2.4\times10^{-14}$ at $10^{5}$ s, about a day), so drift dominates; nothing on this plot goes below $1.5\times10^{-14}$. (e) $1.5\times10^{-14}\times10^{4}\ \text{s} = 1.5\times10^{-10}$ s, about 0.15 ns.
- *Check:* $6.0\times10^{-13}/\sqrt{10} = 1.9\times10^{-13}$, which matches the 10 s entry, confirming the white region.
- *Answer:* slope $-1/2$ (white frequency noise); about 400 s, inside the slope; floor about $1.5\times10^{-14}$ at about $10^{4}$ s; the brochure claim is unsupported, because averaging longer than about 3 h makes it worse; about 0.15 ns of wander.

</details>

### Exercise 5.4 (quantitative)

Shot noise versus Heisenberg (M3). A phase sensor reads out $N = 6.4\times10^{5}$ atoms per cycle. (a) Find the phase uncertainty per cycle at the standard quantum limit and at the Heisenberg limit, and their ratio. (b) With independent atoms, how many atoms per cycle would give $2.5\times10^{-4}$ rad? (c) If the atom number is fixed, how many cycles must be averaged to reach $1.25\times10^{-4}$ rad? (d) Which of (a)'s two figures can a sensor with uncorrelated atoms reach, and what does the other require?

<details>
<summary>Hint</summary>

**Hint:** $1/\sqrt N$ and $1/N$. Repeats are more independent samples: $n$ cycles give another $1/\sqrt n$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* compare the two counting limits; trade atoms for repeats. *Write state:* $N = 6.4\times10^{5}$, $\sqrt N = 800$.
- *Name move:* M3 (with M2 for repeats).
- *Algebra:* (a) SQL $1/800 = 1.25\times10^{-3}$ rad; Heisenberg $1/6.4\times10^{5} = 1.56\times10^{-6}$ rad; ratio $\sqrt N = 800$. (b) $N = 1/(2.5\times10^{-4})^2 = 1.6\times10^{7}$. (c) $(1.25\times10^{-3}/1.25\times10^{-4})^2 = 100$ cycles.
- *Check:* $800\times1.56\times10^{-6} = 1.25\times10^{-3}$. Consistent. 25 times more atoms gave 5 times better, as $\sqrt{25} = 5$.
- *Answer:* 1.25 mrad and 1.56 µrad, ratio 800; $1.6\times10^{7}$ atoms; 100 cycles (100 times the measurement time, so a 100 times slower update rate). (d) Only the SQL. The Heisenberg figure needs entangled atoms, and in practice decoherence eats much of that gain (Degen et al. 2017).

</details>

### Exercise 5.5 (quantitative)

Clock $Q$ and fractional error → distance (M4, M1). A mercury-ion optical clock transition sits at about $1.0648\times10^{15}$ Hz (Ludlow et al. 2015 list it); a hydrogen maser runs at $1.4204\times10^{9}$ Hz. (a) Find the photon energy of the optical transition in J and eV. (b) Assume both are interrogated with a 0.5 Hz linewidth. Find each $Q$ and the ratio. (c) What Ramsey free time gives 0.5 Hz? (d) A clock with a constant fractional offset of $3\times10^{-17}$ runs alone for 30 days. Find the time error and the light-travel distance. (e) In a lock loop the low-side probe reads $P_1 = 0.35$ and the high-side probe reads $0.52$. Which way does the servo steer?

<details>
<summary>Hint</summary>

**Hint:** $E = h\nu$; divide by $e$ for eV. $Q = \nu/\Delta\nu$. $\Delta\nu \approx 1/(2T)$. $\delta t = y\tau$, $\delta x = c\,\delta t$. For (e), the side that reads *more* excitation is the side nearer the line centre.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* energy, quality factors, Ramsey time, the clock chain, a servo decision. *Write state:* $\nu_\text{opt} = 1.0648\times10^{15}$ Hz, $\nu_\text{H} = 1.4204\times10^{9}$ Hz, $\Delta\nu = 0.5$ Hz, $y = 3\times10^{-17}$, $\tau = 30\times86\,400 = 2.592\times10^{6}$ s.
- *Name move:* M4 (E = hν, Q, pulse area and Ramsey, lock loop), M1 (clock chain).
- *Algebra:* (a) $6.626\times10^{-34}\times1.0648\times10^{15} = 7.06\times10^{-19}$ J $= 4.40$ eV (an ultraviolet photon, about 282 nm). (b) $Q_\text{opt} = 2.13\times10^{15}$, $Q_\text{H} = 2.84\times10^{9}$, ratio $7.5\times10^{5}$. (c) $T = 1/(2\times0.5) = 1$ s. (d) $\delta t = 3\times10^{-17}\times2.592\times10^{6} = 7.8\times10^{-11}$ s $= 78$ ps; $\delta x = 3.00\times10^{8}\times7.8\times10^{-11} = 2.3$ cm. (e) The high side reads more, so the line centre is above the probe pair: the oscillator runs low, and the servo steers it up.
- *Check:* at equal linewidth the $Q$ ratio is just the frequency ratio: $1.0648\times10^{15}/1.4204\times10^{9} = 7.5\times10^{5}$. 1 ns ↔ 0.30 m, so 78 ps ↔ 2.3 cm.
- *Answer:* $7.1\times10^{-19}$ J (4.4 eV); $Q = 2.1\times10^{15}$ and $2.8\times10^{9}$, ratio $7.5\times10^{5}$ (a ceiling: SNR and systematics cut the delivered gain); 1 s; 78 ps and 2.3 cm; steer up.

</details>

### Exercise 5.6 (quantitative)

Magnetometer choice (M5). (a) Pick SQUID, OPM, NV or fluxgate for each job and give the deciding reason in one line: (i) a wearable array to record a child's heart while the child moves, in a magnetically shielded room; (ii) imaging current paths in a microchip at about 1 µm resolution; (iii) a quick, cheap walk-over check for a buried steel valve producing a 15 nT anomaly in Earth's field. (b) For a scalar ⁸⁷Rb OPM in a 44 µT background, what is the Larmor frequency, and how much does the 15 nT anomaly shift it? (c) A SQUID has a 2 mm × 2 mm loop. What field corresponds to one flux quantum? (d) An NV centre shows dips 84 MHz apart. What is the field along its axis, and where are the dips?

<details>
<summary>Hint</summary>

**Hint:** Rule sensors in or out on standoff, cryogenics, resolution and environment before noise density (Day 03 comparison table). $f_L = \gamma B$; $B_{\Phi_0} = \Phi_0/S$ with $\Phi_0 = h/2e$; NV dips at $2870\pm28B$ MHz, splitting $56B$ MHz.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* choose sensors by job, then three one-line calculations. *Write state:* $B_0 = 44\,000$ nT, $\Delta B = 15$ nT; $S = 4\times10^{-6}$ m²; splitting 84 MHz.
- *Name move:* M5 (Larmor, flux quantum, NV readout, comparison table).
- *Algebra:* (a)(i) OPM: no cryostat, so the sensors sit on the skin and move with the child; SQUIDs sit in a fixed helmet-style cryostat with centimetres of standoff. (ii) NV: nanometre-scale sensor, room temperature, imaging resolution; its high noise is acceptable at chip current densities. (iii) Fluxgate: 15 nT sits far above its ~100 pT/√Hz noise, and it is cheap and robust (a scalar OPM would also work; a SERF OPM or SQUID would not, in Earth's field or without cryogenics). (b) $f_L = 7\times44\,000 = 308$ kHz; shift $7\times15 = 105$ Hz. (c) $\Phi_0 = 6.626\times10^{-34}/(2\times1.602\times10^{-19}) = 2.07\times10^{-15}$ Wb; $B = 2.07\times10^{-15}/4\times10^{-6} = 5.2\times10^{-10}$ T $= 520$ pT. (d) $B = 84/56 = 1.5$ mT; dips at $2870\mp42$, so 2828 and 2912 MHz.
- *Check:* (c) a 4 mm² loop should need more field per $\Phi_0$ than a 1 cm² loop's 20.7 pT, by $100/4 = 25$: $25\times20.7 = 518$ pT. Consistent.
- *Answer:* OPM, NV, fluxgate; 308 kHz with a 105 Hz shift; about 520 pT per $\Phi_0$; 1.5 mT, dips at 2828 and 2912 MHz.

</details>

### Exercise 5.7 (quantitative)

Interferometer phase (M6, M7). A rubidium gravimeter uses Raman beams at 780 nm with pulse spacing $T = 0.06$ s. (a) Find $k_\text{eff}$, the phase $\Phi = k_\text{eff}gT^2$, and the number of fringes. (b) What would the "total interrogation time" convention $\Phi = k_\text{eff}g\tau^2$ with $\tau = 2T$ give? (c) By how much does the phase change for a 5 µGal change in $g$? (d) With $N = 3.6\times10^{5}$ atoms per shot at the SQL and a 0.5 s cycle, find $\delta g$ per shot and the noise density in µGal/√Hz. (e) An optical Mach-Zehnder has $\varphi = 2\pi/3$ between its arms. What fraction of the maximum brightness reaches the bright port?

<details>
<summary>Hint</summary>

**Hint:** $k_\text{eff} = 4\pi/\lambda$. $\Delta\Phi = k_\text{eff}\,\Delta g\,T^2$. $\delta g = (1/\sqrt N)/(k_\text{eff}T^2)$; density $= \delta g\times\sqrt{\text{cycle time}}$. Optical output $\propto\cos^2(\varphi/2)$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* phase, wrong-convention phase, phase per µGal, shot-noise sensitivity, one optical fringe. *Write state:* $\lambda = 780$ nm, $T = 0.06$ s, $T^2 = 3.6\times10^{-3}\ \text{s}^2$, $N = 3.6\times10^{5}$, cycle 0.5 s.
- *Name move:* M7 (phase formula, sensitivity), M6 (cos² fringe), M3 (SQL).
- *Algebra:* (a) $k_\text{eff} = 4\pi/780\times10^{-9} = 1.61\times10^{7}\ \text{m}^{-1}$; $\Phi = 1.61\times10^{7}\times9.81\times3.6\times10^{-3} = 5.69\times10^{5}$ rad; $\Phi/2\pi = 9.06\times10^{4}$ fringes. (b) $4\times5.69\times10^{5} = 2.28\times10^{6}$ rad. (c) $1.61\times10^{7}\times5\times10^{-8}\times3.6\times10^{-3} = 2.9\times10^{-3}$ rad. (d) $\delta\varphi = 1/600 = 1.67\times10^{-3}$ rad; $\delta g = 1.67\times10^{-3}/(1.61\times10^{7}\times3.6\times10^{-3}) = 2.87\times10^{-8}$ m/s² $= 2.87$ µGal per shot; density $2.87\times\sqrt{0.5} = 2.0\ \mu\text{Gal}/\sqrt{\text{Hz}}$. (e) $\cos^2(\pi/3) = 0.25$.
- *Check:* (c) and (d) agree: 5 µGal gives 2.9 mrad of phase, slightly more than the 1.67 mrad shot noise, so a single shot resolves about 2.9 µGal, matching (d).
- *Answer:* $1.61\times10^{7}\ \text{m}^{-1}$, $5.7\times10^{5}$ rad, about $9.1\times10^{4}$ fringes; $2.3\times10^{6}$ rad in the factor-4 convention (use the standard one); 2.9 mrad; 2.9 µGal per shot, about 2.0 µGal/√Hz; 0.25 of the maximum.

</details>

### Exercise 5.8 (quantitative)

$T^2$ scaling (M7). (a) What is the sensitivity gain of a space instrument with $T = 4$ s over a ground instrument with $T = 0.12$ s? (b) How far do atoms fall during the ground sequence (length $2T$, dropped from rest)? (c) For equal $\delta g$, by what factor could the space instrument cut its atom number? (d) A ground lab has 1.5 m of usable vacuum height. What is the largest $T$ for a simple drop? (e) If instead the atoms are launched upwards as a fountain, with the mirror pulse at the top of their flight and the final pulse back at the bottom, what is the largest $T$, and what phase gain does that give over the drop?

<details>
<summary>Hint</summary>

**Hint:** Gain $= (T_2/T_1)^2$. Drop distance $\tfrac12g(2T)^2 = 2gT^2$. At fixed $\delta g$, $\delta\varphi\propto T^2$ may grow and $\delta\varphi = 1/\sqrt N$, so $N\propto T^{-4}$. For the fountain, rising to height $H$ takes $\sqrt{2H/g}$ (standard kinematics, judgement: not in the lecture).

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* $T^2$ gain, drop height, atom budget, two height-limited $T$ values. *Write state:* $T_g = 0.12$ s, $T_s = 4$ s, $H = 1.5$ m.
- *Name move:* M7 ($T^2$ scaling), with M3.
- *Algebra:* (a) $(4/0.12)^2 = 1.11\times10^{3}$. (b) $2\times9.81\times0.0144 = 0.28$ m. (c) $(4/0.12)^4 = 1.23\times10^{6}$. (d) $2gT^2 = 1.5$ gives $T = \sqrt{1.5/19.62} = 0.28$ s. (e) $T = \sqrt{2\times1.5/9.81} = 0.55$ s, twice the drop value, so $2^2 = 4$ times the phase.
- *Check:* (d) agrees with the lecture's "a few hundreds of milliseconds on the ground". The fountain uses the height twice (up and down), hence the factor 2 in $T$.
- *Answer:* about 1100×; 0.28 m; about $1.2\times10^{6}$ times fewer atoms; 0.28 s; 0.55 s, a 4× phase gain. Long $T$ means fewer shots per second (a lower update rate) and needs colder atoms.

</details>

### Exercise 5.9 (quantitative)

Spot the error, Week 2 style (M2, M3). A slide makes two claims. Name each error, correct it, and redo the number. (i) "The sensor's noise is $3\ \text{fT}\sqrt{\text{Hz}}$, so in a 25 Hz band it shows 75 fT." (ii) "The field of a current dipole falls as $1/r^2$, so moving the sensor from 36 mm to 16 mm increases the amplitude by $r^2$." Then (iii): what gain would you get if the source were a small magnetised object (magnetic dipole) instead?

<details>
<summary>Hint</summary>

**Hint:** Check the units of (i) by multiplying through by $\sqrt{\text{Hz}}$. In (ii), only a *ratio* of distances can be raised to a power. A magnetic dipole falls as $1/r^3$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* two wrong claims; correct forms and numbers. *Write state:* $S = 3$ fT/√Hz, $\Delta f = 25$ Hz; $r_1 = 36$ mm, $r_2 = 16$ mm.
- *Name move:* M2 (noise density units), M3 (distance gain).
- *Algebra:* (i) The unit is T/√Hz, not T√Hz (Week 2 erratum L74). With the typo, $\text{fT}\sqrt{\text{Hz}}\times\sqrt{\text{Hz}} = \text{fT·Hz}$, which is not a field; and 75 is $3\times25$, multiplying by the bandwidth instead of its square root. Correct: $3\times\sqrt{25} = 15$ fT. (ii) The gain is $(r_1/r_2)^2$, not "$r^2$" (Week 2 erratum L94): $(36/16)^2 = 2.25^2 = 5.1$. (iii) $(36/16)^3 = 11.4$.
- *Check:* "$r^2$" would give a different answer in mm and in m, which a physical ratio cannot do.
- *Answer:* (i) 15 fT, unit T/√Hz; (ii) 5.1× for a current dipole; (iii) 11.4× for a magnetic dipole. Sensor noise is unchanged, so SNR rises by the same factors.

</details>

### Exercise 5.10 (quantitative)

Spot the error, Week 3 style (M7). A slide on a potassium-39 gravimeter (Raman light at 767 nm) makes three claims. Name each error and correct it, with a number. (i) "$\Phi = k_\text{eff}g\tau^2$, where $\tau$ is the total interrogation time." (ii) "The chirp rate that nulls the phase for every $T$ is $\alpha = g$." (iii) "A spring gravimeter's sensitivity scales as $1/T^2$, where $T$ is its natural period, so a 0.5 s spring is more sensitive than a 2 s spring."

<details>
<summary>Hint</summary>

**Hint:** (i) The standard $T$ is the time between pulses and $\tau = 2T$. (ii) Check the units of $\alpha$ (Hz/s) against $g$ (m/s²); the null is at $\alpha_0 = k_\text{eff}g/2\pi$. (iii) $\delta L = gT^2/4\pi^2$.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* three wrong claims, each with a corrected number. *Write state:* $\lambda = 767$ nm; spring periods 0.5 s and 2 s.
- *Name move:* M7 (phase formula and chirp), M7 classical gravimeter table.
- *Algebra:* (i) With $\tau = 2T$ the phase is $k_\text{eff}g(2T)^2 = 4k_\text{eff}gT^2$: 4 times the standard result $\Phi = k_\text{eff}gT^2$, $T$ = pulse spacing (Week 3 erratum L105-110). (ii) $k_\text{eff} = 4\pi/767\times10^{-9} = 1.64\times10^{7}\ \text{m}^{-1}$, so $\alpha_0 = 1.64\times10^{7}\times9.81/2\pi = 2.56\times10^{7}$ Hz/s, about 25.6 MHz/s, not "9.81" of anything (erratum L91). (iii) Displacement per unit $\Delta g$ is $T^2/4\pi^2$, so the 2 s spring moves $(2/0.5)^2 = 16$ times more: sensitivity *rises* as $T^2$ (erratum L135).
- *Check:* (ii) potassium's wavelength is close to rubidium's 780 nm, so $\alpha_0$ should be close to rubidium's 25.2 MHz/s, slightly higher. It is.
- *Answer:* factor 4 too large; $\alpha_0\approx25.6$ MHz/s; the long-period spring is 16 times more sensitive.

</details>

### Exercise 5.11 (quantitative)

Credible numbers (F3, M1). A consultant's note compares a laboratory atom gravimeter at $12\ \mu\text{Gal}/\sqrt{\text{Hz}}$ with a falling-corner-cube gravimeter, quoting one source for the corner cube as "$6\ \mu\text{Gal}/\sqrt{\text{Hz}}$ (ideal conditions, maximum drop rate)" and another as "$6\times10^{-8}g/\sqrt{\text{Hz}}$ (typical)" (all fictional). (a) Put both corner-cube figures in µGal/√Hz. (b) Give the atom-versus-corner-cube ratio each way. (c) Which comparison, if either, may go in a gain argument, and what must the note add?

<details>
<summary>Hint</summary>

**Hint:** $6\times10^{-8}g = 6\times10^{-8}\times9.81$ m/s², then divide by $10^{-8}$. F3 rule: a ratio needs both sides measured the same way.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* convert, compute two ratios, judge them. *Write state:* atom 12, corner cube 6 and $6\times10^{-8}g$ per √Hz.
- *Name move:* M1 (units), F3 (like-for-like).
- *Algebra:* (a) 6 µGal/√Hz and $6\times10^{-8}\times9.81/10^{-8} = 58.9$ µGal/√Hz. (b) Against the ideal figure the atom instrument is $12/6 = 2$ times *worse*; against the typical figure it is $58.9/12 = 4.9$ times *better*.
- *Check:* the two corner-cube numbers differ by about 10, the same kind of tenfold gap as the Week 3 lecture's two corner-cube figures (inventory erratum L99 vs L139).
- *Answer:* 6 and 59 µGal/√Hz; "2× worse" or "4.9× better" depending on which source you pick. Neither ratio is fair as written, because a lab atom figure is compared with an ideal or a typical classical figure. The note must state conditions for both sides and compare like with like (lab with lab, or field with field), or say that the comparison is not yet possible.

</details>

### Exercise 5.12 (quantitative)

Spot the error, mixed (Week 1 errata, M3, M2). A briefing slide says: (i) "QKD works because the two parties share entangled particles." (ii) "A quantum computer performs many calculations simultaneously, so it tries every answer at once." (iii) "Our sensor uses $4\times10^{6}$ independent atoms, so its phase noise per cycle is $2.5\times10^{-7}$ rad." (iv) "The clock's stability is $2\times10^{-15}$, so it can never be more than 0.17 ns out after a day." Name and correct each error; give the right number in (iii).

<details>
<summary>Hint</summary>

**Hint:** (i) Which protocol does the lecture cite? (ii) What does one measurement return? (iii) Independent atoms give $1/\sqrt N$. (iv) A stability figure needs a $\tau$, and stability is not the same as frequency offset.

</details>

<details>
<summary>Solution sketch</summary>

**Solution sketch:**
- *Restate:* four claims, each corrected. *Write state:* $N = 4\times10^{6}$; $y = 2\times10^{-15}$, 1 day.
- *Name move:* Week 1 errata (F3 habit), M3, M2 (Allan), M1 (clock chain).
- *Algebra:* (i) BB84 uses single photons in two bases and no entanglement; entanglement-based QKD (E91) is a separate family (erratum L52). (ii) A measurement returns one outcome; algorithms gain by arranging interference so wrong answers cancel (erratum L70). (iii) $1/\sqrt{4\times10^{6}} = 1/2000 = 5\times10^{-4}$ rad. $2.5\times10^{-7} = 1/N$ is the Heisenberg limit, which needs entanglement. (iv) $2\times10^{-15}\times86\,400 = 1.7\times10^{-10}$ s, which is where 0.17 ns comes from, but the reasoning fails twice. A stability figure without $\tau$ cannot be used. And stability is how much the rate wanders, not how far it sits from the true rate: a constant offset or drift adds time error the stability figure does not show.
- *Check:* (iii) the stated figure is $\sqrt N = 2000$ times too optimistic, exactly the SQL-to-Heisenberg ratio.
- *Answer:* no entanglement in BB84; interference, not parallelism; $5\times10^{-4}$ rad; ask for the Allan curve to one day and the frequency offset and drift before claiming any holdover.

</details>

### Exercise 5.13 (writing)

**Timed: 40 minutes, 300 words, no notes.** Harrowmere Water & Power suspects an air-filled void forming in the fill of its Greystock reservoir embankment. It must decide how to run the void survey now and the re-surveys that will show, years later, whether the void is growing. Write a 300-word F1 gain argument: should Harrowmere use a quantum (atom) gravimeter? Use only these figures from the shared Harrowmere fact sheet (STRATEGY.md, all fictional), plus one survey choice:
- target signal: a gravity deficit of about 5 µGal above the suspected void;
- survey: 150 stations, with 5 min of averaging per station (fictional survey choice);
- installed relative spring meter: noise 8 µGal/√Hz, drift 30 µGal/day, 14 kg;
- candidate portable atom gravimeter: absolute, noise 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation.

Score yourself with the rubric in `## Core concepts` before reading the model.

<details>
<summary>Hint</summary>

**Hint:** Per-station noise is $S/\sqrt{\tau}$ with $\tau = 300$ s for both instruments. The $\Delta f\approx1/(2\tau)$ factor is the same for both, so leaving it out keeps the comparison fair. Compare each result with the 5 µGal target. Then convert the spring meter's drift to µGal per 8-hour survey day. Ask which instrument is limited by noise and which by drift. Finally, ask what a re-survey years later needs: readings that can be compared directly. Keep every number labelled (fictional).

</details>

<details>
<summary>Model paragraph</summary>

**Model paragraph:** (1) *Classical limit.* Harrowmere Water & Power suspects a void in its Greystock reservoir embankment that would lower gravity above it by about 5 µGal (fictional). The installed spring gravimeter is not limited by noise: 8 µGal/√Hz averages to 0.46 µGal in 5 minutes per station. Its limit is drift. At 30 µGal per day (fictional) it drifts about 10 µGal over an 8-hour survey day, twice the signal, so the 150 stations must be tied repeatedly to a base station and corrected by hand. (2) *Mechanism.* An atom gravimeter splits, reflects and recombines free-falling atoms with three laser pulses. Its phase $\Phi = k_\text{eff}gT^2$ depends only on a laser wavelength and a time. (3) *Figure of merit.* Absolute repeatability in µGal per station, held across surveys years apart. (4) *Quantified gain.* At 30 µGal/√Hz (fictional), 5 minutes per station gives 1.7 µGal. The 5 µGal void therefore shows at about three times the noise, with no drift correction. On noise alone the spring meter is nearly four times better, so the gain is not sensitivity. It is that a reading taken in five years can be subtracted directly from one taken now, while two spring surveys can only be compared through chains of base-station ties. (5) *Maturity and practicality.* Portable atom gravimeters are sold as products, so component TRL is high. A survey workflow on an embankment crest is untested, so system TRL is about 6 (judgement). At 110 kg against 14 kg (fictional), plus vibration isolation, the atom gravimeter needs a vehicle and a level pad at each station. (6) *Verdict.* Keep the spring meter for the dense station grid, and use one atom gravimeter as the absolute reference at a few stations in each re-survey. The caveat: the 30 µGal/√Hz figure assumes a quiet site. Vibration from the reservoir's pumps should be measured on a trial day before buying.

</details>

<details>
<summary>What a weak answer misses</summary>

**What a weak answer misses:**
- It never sets the instruments against the 5 µGal target, so neither can be judged "good enough".
- It claims the atom gravimeter is "more sensitive". On these figures it is nearly four times *noisier* than the spring meter; the gain is absoluteness and no drift.
- It mixes noise (µGal/√Hz, averages down) with drift (µGal per day, does not).
- It uses a lab figure, the Week 3 lecture's Eq 3.1 with $\tau = 2T$, or the $10^{10}$ Sagnac ratio, none of which fits a field gravity survey.
- It ignores the 110 kg and vibration isolation, gives a TRL with no evidence and no component/system split, or offers a vague caveat ("quantum is expensive") instead of the vibration test.

</details>

## Self-scoring table

Fill in your score, then revisit the Day and move for every item below 1. Repeat the item on the given A1-window day (see `## Spaced review`) with the numbers changed.

| Item | What it tests | Move / framework | Revisit | Your score |
|---|---|---|---|---|
| 5.1 | Unit conversions (fT, µGal, E, fraction of $g$) | M1 | Day 01 M1; Day 04 M7.8 | /1 |
| 5.2 | Noise density, bandwidth, averaging time | M2 | Day 02 M2.3 | /1 |
| 5.3 | Reading an Allan plot | M2 | Day 02 M2.4 | /1 |
| 5.4 | Shot noise vs Heisenberg; atoms vs repeats | M3 | Day 02 M3.1 | /1 |
| 5.5 | $E = h\nu$, $Q$, Ramsey, clock chain, lock loop | M4, M1 | Day 03 M4.1-M4.5 | /1 |
| 5.6 | Magnetometer choice; $f_L$, $\Phi_0$, NV dips | M5 | Day 03 M5.1-M5.4 | /1 |
| 5.7 | $\Phi = k_\text{eff}gT^2$; sensitivity; cos² fringe | M6, M7 | Day 04 M6.1, M7.1-M7.5 | /1 |
| 5.8 | $T^2$ scaling, drop height, atom budget | M7 | Day 04 M7.6 | /1 |
| 5.9 | Errata L74 and L94 | M2, M3 | Day 02 M2.3, M3.2; Week 2 companion §4 | /1 |
| 5.10 | Errata L105-110, L91, L135 | M7 | Day 04 M7.4, M7.8; Week 3 companion §4 | /1 |
| 5.11 | Like-for-like ratios | F3, M1 | Day 01 F3; Day 04 M7.8 | /1 |
| 5.12 | Errata L52, L70; SQL misuse; stability without $\tau$ | M3, M2, M1 | Day 01 lecture decode; Day 02 M2.4, M3.1 | /1 |
| 5.13 | 300-word F1 piece (Greystock, shared fact sheet) | F1, M7, M2 | STRATEGY.md §6; Day 04 Exercise 4.10 | /12 |

**Reading your score.**
- 11-12 items and F1 ≥ 10: the sensing half is solid. Spend the A1-window slots on spaced review only.
- 9-10 items and F1 ≥ 8: pass. Redo the missed items with changed numbers.
- Below 9 items, or F1 below 8: list the Days that appear most often in your "Revisit" column, and redo that Day's `## Done when` on Fri 20 Nov before starting Day 06.

## Anti-patterns / Common mistakes

- **Opening the hints during the first pass.** *How you'd notice:* your score is high but you could not have started item 5.7 without the formula. *Instead:* close the `<details>` blocks; a half-point honestly earned tells you more than a full point borrowed.
- **Generous marking.** *How you'd notice:* you gave a point to an answer with no unit, or to "about 4×" when the factor was 16. *Instead:* apply the scoring rules literally; a missing unit is 0.
- **Letting the F1 timer slide.** *How you'd notice:* you "just finished the last sentence" for ten more minutes. *Instead:* stop at 40 minutes and score what is on the page; the clock is part of the skill.
- **Treating the checkpoint as a reading list.** *How you'd notice:* after marking you reread Days 02-04 from the top. *Instead:* revisit only the moves in your "Revisit" column, then redo the item with new numbers.
- **Scoring a gain argument on its prose.** *How you'd notice:* the paragraph reads well, but part 4 has no ratio. *Instead:* score each F1 part against the rubric row, not the whole piece on impression.
- **Re-using today's numbers in tomorrow's review.** *How you'd notice:* you remember "308 kHz" rather than recompute it. *Instead:* change one input (a field, a $T$, an $N$) every time you redo an item.

## Done when

- **Items:** 9/12 or better on Exercises 5.1-5.12, marked by the scoring rules.
- **Writing:** 8/12 or better on Exercise 5.13 by the rubric, with at least 1 point in F1 parts 1 and 4, written in 40 minutes and 270-330 words.
- **Plan:** every item below 1 has a confusion-log row and a slot in the A1-window review below.

If you pass both, Days 01-04 are done; the next new material is Day 06 (Week 4, communication). If you miss either, use the "Reading your score" rules above before Day 06.

## Spaced review

Cumulative, closed book. Today's set pulls from Day 04 (N−1), Day 02 (N−3) and Day 01 (the earliest day; N−7 is before the sprint started). Do it in the last 15 minutes or first thing tomorrow. Then use the A1-window plan below.

**From Day 04.**
1. Find $k_\text{eff}$ for counter-propagating beams at 689 nm.
2. In one sentence, why do the starting height and velocity drop out of $\Phi$?
3. Write the atom-to-light Sagnac ratio. What reduces it in practice, and why do the lecture's round flux numbers not show that atoms lose?

**From Day 03.**
4. A Ramsey sequence uses a 0.4 s free time. What is the linewidth?
5. Why can a SERF OPM not work in an open field?

**From Day 02.**
6. A sensor has $25\ \text{pT}/\sqrt{\text{Hz}}$. What is its noise in a 64 Hz detection (noise) bandwidth?
7. Why is "stability $10^{-14}$" not yet a usable number?

**From Day 01.**
8. A clock has a constant offset of $4\times10^{-16}$. What is its time error after one year, and the light-travel distance?
9. Name the six F1 parts in order.

<details>
<summary>Answers</summary>

1. $4\pi/689\times10^{-9} = 1.82\times10^{7}\ \text{m}^{-1}$.
2. The phase is a second difference of position, $z(0) - 2z(T) + z(2T) = -gT^2$, which cancels constant and linear terms.
3. $m\lambda c/h$ (about $10^{10}$). In practice the atom interferometer encloses far less area than a fibre coil, and the particle flux differs too. The lecture's round flux numbers set a cold-atom source against an idealised 1 W laser, which is not like-for-like. The lecture also reports a thermal-beam atom gyroscope competitive with the best optical gyroscopes, so do not conclude that atoms lose.
4. $1/(2\times0.4) = 1.25$ Hz.
5. It works only near zero field, where spin-exchange collisions stop scrambling the precession; Earth's tens of µT destroy that regime.
6. $25\times\sqrt{64} = 200$ pT.
7. It has no averaging time $\tau$, and it is a stability, not an offset or accuracy.
8. $4\times10^{-16}\times3.156\times10^{7} = 1.26\times10^{-8}$ s $= 12.6$ ns; $3.00\times10^{8}\times1.26\times10^{-8} = 3.8$ m.
9. Classical limit with a number; quantum mechanism; figure of merit; quantified gain; maturity and practicality; verdict with a caveat.

</details>

**A1-window plan (Mon 16 - Thu 19 Nov, 20 minutes a day, nothing else).** The Assessment 1 work happens in its separate session; these slots are retrieval only.

| Day | 20-minute slot |
|---|---|
| Mon 16 Nov | Redo your lowest-scoring item from 5.1-5.4 with one input changed; then the warm-up law sheet, items 1-4. |
| Tue 17 Nov | Redo your lowest-scoring item from 5.5-5.8 with one input changed; then law sheet items 5-8. |
| Wed 18 Nov | Redo one spot-the-error item (5.9, 5.10 or 5.12) from memory: state each erratum and its correction with the lecture line. |
| Thu 19 Nov | Write F1 parts 1 and 4 only (about 140 words) for Exercise 5.13 from memory, then compare with the model. |

## Read next

- Degen, Reinhard and Cappellaro, *Quantum sensing*, <https://arxiv.org/abs/1611.02427>, §I-III. Reread only the parts behind items you missed: the definitions of sensitivity and the $1/\sqrt{\text{time}}$ scaling (5.2-5.4), and the standard quantum limit versus the Heisenberg limit (5.4, 5.12).
- Abend et al., *Atom interferometry and its applications*, <https://arxiv.org/abs/2001.10976>, the gravimeter section, if you lost points on 5.7, 5.8, 5.10 or the F1 piece: the Mach-Zehnder sequence, the phase formula with $T$ as pulse spacing, and vibration as the main field noise source.
