# Day 03: Clocks and Magnetometers

**Time:** ~3 h · **Feeds:** Week 2 lecture §2.3-2.15 (`week_2/week_2_lecture.md` L86-205); inventory rows W2 Apply, W2 Consolidate (sensitivity, bandwidth, dynamic range, practicality), W2 quiz Q1-Q4 · **Companion:** `companions/week02_companion.md` (full)

**Cadence (180 min):**
- 15 min retrieval: do `## Spaced review` (near the end of this file) first, closed book.
- 55 min moves: M4.1-M4.4, M1 revisited (fractional error → time → distance) and M5.1-M5.4 below.
- 50 min quantitative drills: Exercises 3.1-3.8. Exercises 3.3, 3.4, 3.5 and 3.8 are marked (stretch); do 3.1, 3.2, 3.6 and 3.7 first, and leave the stretch ones for tomorrow if you pass 50 min.
- 45 min writing on the running case: Exercises 3.9 and 3.10.
- 15 min companion pointer and confusion log (`## Read next`).

## Why this matters

Week 2 has two halves that look unrelated: atomic clocks and quantum magnetometers. They are the same object. Both use a two-level system whose transition frequency is set by physics. A clock asks "what is this frequency?" and uses it as a ruler for time. A magnetometer asks "how much has a magnetic field shifted this frequency?" and reads the field from the shift. You already own the maths from Module 3: a 2×2 Hamiltonian, Pauli matrices and $P = |\langle 1|\psi\rangle|^2$.

The lecture asserts that optical clocks beat microwave clocks and that OPMs, SQUIDs and NV centres each win somewhere. It gives few numbers and some of them disagree. Today you build the scaling laws that turn those assertions into numbers: $E = h\nu$, $Q = \nu/\Delta\nu$, pulse area, the lock loop, fractional error → time → distance, $f = \gamma B$ and $\Phi_0 = h/2e$. Then you build one comparison table you can reuse in both Week 2 writing tasks. Every Week 2 Apply or Consolidate answer needs at least one row of that table and one of these conversions.

## Core concepts

### Move M4.1: Energy, frequency and quality factor ($E = h\nu$, $Q = \nu/\Delta\nu$)

**Idea.** An atom's two levels differ in energy by $E$. Light or microwaves at frequency $\nu = E/h$ drive the transition (lecture Eq. 2.3, L185; $h = 6.626\times10^{-34}$ J s). The atom answers only near $\nu$. The width of that response, $\Delta\nu$ (full width at half maximum, in Hz), is the **linewidth**. The **quality factor** is

$$Q = \frac{\nu}{\Delta\nu}.$$

A clock steers an oscillator to the centre of the line. You can find the centre of a line to some fraction of its width, so the fractional error is roughly $\Delta\nu/\nu = 1/Q$ divided by the signal-to-noise ratio. **At equal linewidth, a higher $\nu$ means a higher $Q$ and a better clock.** That is the whole reason optical (about $4\times10^{14}$ to $1\times10^{15}$ Hz) beats microwave (about $10^{10}$ Hz). The linewidths achieved are similar, about 1 Hz or below, for both (Ludlow et al. 2015). The lecture (L193) says "100s of terahertz" and "can be even more stable" but never gives this reason.

**Worked clone.** Caesium, the SI definition (L161): $\nu = 9\,192\,631\,770$ Hz.
- $E = h\nu = 6.626\times10^{-34}\times9.193\times10^{9} = 6.09\times10^{-24}$ J, which is $3.80\times10^{-5}$ eV. That is tiny: a visible photon carries about 2 eV.
- An optical strontium lattice-clock transition sits at about $4.29\times10^{14}$ Hz (Ludlow et al. 2015). Its photon carries $2.84\times10^{-19}$ J, about 1.78 eV.
- With a 1 Hz linewidth for both: $Q_{\rm Cs} = 9.2\times10^{9}$ and $Q_{\rm Sr} = 4.3\times10^{14}$. The ratio is $4.67\times10^{4}$, simply $\nu_{\rm Sr}/\nu_{\rm Cs}$.

**You've got it when** you can say, without notes, "same linewidth, about 47 000 times higher frequency, so about 47 000 times higher $Q$", and you know this is a ceiling. Real optical clocks gain less than $Q$ alone suggests, because they count fewer atoms and so have lower SNR (Exercise 3.5).

### Move M4.2: Pulse area. The π/2 splitter and the π mirror (bridge to your 2×2 maths)

**Idea.** Shine resonant radiation on a two-level atom for a time $t$. In the frame rotating with the drive, on resonance, the Hamiltonian is

$$H = \frac{\hbar\Omega}{2}\sigma_x,$$

where $\Omega$ is the **Rabi frequency** (angular, rad/s), set by how strong the drive is. You know $\sigma_x^2 = I$, so the time evolution is

$$U(t) = e^{-i\Omega t\sigma_x/2} = \cos\!\left(\tfrac{\Omega t}{2}\right)I - i\sin\!\left(\tfrac{\Omega t}{2}\right)\sigma_x .$$

Start in $|0\rangle = (1, 0)^{\mathsf T}$. Then $U|0\rangle = \big(\cos(\Omega t/2),\ -i\sin(\Omega t/2)\big)^{\mathsf T}$, and the probability of finding the atom excited is

$$P_1(t) = \sin^2\!\left(\frac{\Omega t}{2}\right).$$

The product $\Omega t$ is the **pulse area**. Two areas matter (this is standard; the lecture does not derive it):
- **π/2 pulse** ($\Omega t = \pi/2$): $P_1 = 1/2$. The atom is in an equal superposition. This is a **beam splitter** for the atom's state.
- **π pulse** ($\Omega t = \pi$): $P_1 = 1$. The atom swaps $|0\rangle \leftrightarrow |1\rangle$. This is a **mirror**.

Day 04 reuses both: the atom interferometer is π/2, π, π/2.

**Ramsey method.** A good clock uses π/2, then free evolution for time $T$, then π/2 again. If the drive is detuned from the atom by $\delta f$ (in Hz), the atom and the drive drift apart in phase by $2\pi\,\delta f\,T$ during the wait, and $P_1 = \cos^2(\pi\,\delta f\,T)$. The central fringe falls to half height at $\delta f = \pm 1/(4T)$, so its width is

$$\Delta\nu \approx \frac{1}{2T}.$$

Longer free time means a narrower line. This is why caesium fountains toss atoms upwards: it buys about half a second of $T$ (standard; Ludlow et al. 2015, §I, covers Ramsey spectroscopy).

**Worked clone.** A drive with $\Omega/2\pi = 50$ kHz. A π pulse needs $\Omega t = \pi$, so $t_\pi = 1/(2\times50\,\text{kHz}) = 10$ µs. The π/2 pulse takes 5 µs. A Ramsey wait of $T = 0.5$ s gives $\Delta\nu = 1/(2\times0.5) = 1$ Hz, so on caesium $Q = 9.2\times10^{9}$.

**You've got it when** you can write $U(t)$ from $\sigma_x^2 = I$ on a blank page, read off $\sin^2(\Omega t/2)$, and say which pulse is the splitter and which is the mirror.

### Move M4.3: The lock loop (a control loop you already know)

**Idea.** The lecture (L189) describes "maximising the fraction of atoms that changed state". Done naively, that fails: at the top of a peak the slope is zero, so you cannot tell which way you are off. Real clocks probe **both sides** of the line and subtract. Read it as a feedback controller:

| Control-loop part | In an atomic clock |
|---|---|
| Plant (the thing that drifts) | local oscillator: a quartz crystal or a laser |
| Sensor | the atoms: excitation probability at the probe frequency |
| Error signal | $e = P_1(\text{probe at } -\Delta\nu/2) - P_1(\text{probe at } +\Delta\nu/2)$ |
| Controller | an integrator (PI servo) in software |
| Actuator | the oscillator's frequency tuning |
| Output | the steered oscillator, counted to give time |

If the oscillator runs high by $\varepsilon$, the low-side probe lands nearer the centre and sees more excitation, so $e > 0$ and the servo pulls the frequency down. At lock $e = 0$. Between corrections the oscillator free-runs, so a better oscillator lets the loop run slower. With no atoms (GNSS outage, broken laser) you are left with the bare plant. That state is **holdover**, and it is the subject of Exercises 3.6 and 3.9.

**Worked clone.** Model the line as a Lorentzian $P_1(\delta) = 1/\big(1 + (2\delta/\Delta\nu)^2\big)$ (a simple line shape, used here for arithmetic; judgement). Take $\Delta\nu = 1$ Hz and an oscillator high by $\varepsilon = 0.1$ Hz. The probes land at detunings $\varepsilon - 0.5 = -0.4$ Hz and $\varepsilon + 0.5 = +0.6$ Hz:
- $P_1(-0.4) = 1/(1 + 0.64) = 0.610$
- $P_1(+0.6) = 1/(1 + 1.44) = 0.410$
- $e = 0.200 > 0$, so steer down.

The linear estimate is $e \approx 2\varepsilon/\Delta\nu = 0.2$, because the Lorentzian's slope at half height is $1/\Delta\nu$ per Hz. Narrower line, steeper slope, bigger error per hertz of mistuning: $Q$ again.

**You've got it when** you can draw the table above from memory and explain why the probes sit on the line's sides, not its peak.

### Move M4.4: The frequency comb (part of M4, concept level only)

**Idea.** Electronics count up to about $10^{10}$ Hz, not $10^{14}$ (L195). A mode-locked laser emits a train of short pulses at repetition rate $f_{\rm rep}$ (radio or microwave, countable). In frequency, the train is a comb of sharp lines:

$$f_n = n\,f_{\rm rep} + f_{\rm ceo},$$

where $n$ is an integer of order $10^6$ and $f_{\rm ceo}$ is an offset, also countable. Beat the clock laser against the nearest tooth and you get a third countable frequency, $f_{\rm beat}$. Then

$$\nu_{\rm clock} = n\,f_{\rm rep} + f_{\rm ceo} + f_{\rm beat}.$$

Every number on the right is either an integer or below a gigahertz. That is the "ruler" in L195. (Sign conventions for $f_{\rm ceo}$ and $f_{\rm beat}$ vary; take them as positive here.) Learn the idea, not comb physics: the comb is a gearbox from optical to microwave.

**Worked clone.** $f_{\rm rep} = 250$ MHz, $f_{\rm ceo} = 35$ MHz, nearest tooth $n = 1\,716\,912$, $f_{\rm beat} = 40$ MHz. Then $\nu = 1\,716\,912\times250\ \text{MHz} + 75\ \text{MHz} = 429\,228\,075$ MHz $= 4.29228075\times10^{14}$ Hz. You never counted anything faster than 250 MHz.

**You've got it when** you can explain in one sentence why optical clocks only overtook microwave clocks after about 2000 (L195): no gearbox, no counting.

### Move M1 revisited: Fractional uncertainty → time error → distance error

**Idea.** This is Day 01's move M1 applied to clocks; it is not a new move. A clock with fractional frequency error $y = \delta\nu/\nu$ gains or loses $y$ seconds per second. After time $t$ the error is $\delta t = y\,t$, assuming the offset is constant; real oscillators also drift, which adds a $t^2$ term (judgement). Light travels $c\,\delta t$ in that time, and ranging systems such as satnav turn time into distance this way. Keep three anchors:
- 1 ns of time error ↔ 0.30 m of range error.
- 1 day ≈ $8.64\times10^{4}$ s; 1 year ≈ $3.156\times10^{7}$ s.
- In a 50 Hz grid, 1 µs is $360°\times50\times10^{-6} = 0.018°$ of phase.

**Worked clone (checking the lecture).**
- L159 claims "1 second every 300 million years, roughly one part in $10^{16}$". Check: $1/(3\times10^{8}\times3.156\times10^{7}) = 1.06\times10^{-16}$. Consistent.
- L195 claims "$10^{18}$, about 1 second every 30 billion years". Check: $1/(10^{-18}\times3.156\times10^{7}) = 3.17\times10^{10}$ years. Consistent.
- A $10^{-16}$ clock run for one day: $\delta t = 10^{-16}\times86\,400 = 8.64$ ps, which is $c\,\delta t = 2.6$ mm of light travel.

**You've got it when** you can go from any "one part in $10^{x}$" to seconds per day and millimetres in under a minute.

### Move M5.1: Larmor precession and the OPM (with SERF in one line)

**Idea.** An atom with spin in a magnetic field $B$ has its levels split by an energy proportional to $B$ (the Zeeman effect). The pumped spins precess at the **Larmor frequency**

$$f_L = \gamma B,$$

where $\gamma$ is the gyromagnetic ratio in Hz per tesla. For the ⁸⁷Rb ground state ($F = 2$), $\gamma \approx 7$ Hz/nT, which is 7 GHz/T (standard value; Budker & Romalis 2007 review OPM schemes). An OPM (lecture §2.7, L121-129):
1. **Pump** the vapour with resonant light so the atoms share one spin state (L123). This is the "prepare" step of the clock, done with light.
2. Let the spins **precess** at $f_L$.
3. **Read** the precession from the transmitted light's intensity or polarisation (L123).

Measure a frequency, divide by $\gamma$, and you have $B$. Frequency is the quantity physics lets you measure best (Move M4.1). This is the clock idea turned round.

**SERF in one line.** Spin-exchange relaxation-free OPMs run a dense, hot vapour in near-zero field, where spin-exchange collisions no longer scramble the precession. That gives the lowest noise (sub-fT in the lab, Budker & Romalis 2007), at the cost of magnetic shielding and under 200 Hz of bandwidth (L127).

**Worked clone.** In Earth's field, 50 µT (Table 2.1, L68): $f_L = 7\ \text{Hz/nT}\times50\,000\ \text{nT} = 350$ kHz. That is easy to count (Move M4.4 is not needed).

**You've got it when** you can say why a SERF OPM cannot work in an open field (it needs near-zero field) and what a non-SERF, "scalar" OPM measures instead (the total field, via $f_L$).

### Move M5.2: The SQUID and the flux quantum $\Phi_0 = h/2e$

**Idea.** Lecture Eq. 2.2 (L115) is $\mathbf B\cdot\mathbf S = n\,\pi\hbar/q_e$. It never names the constant. Since $\pi\hbar = h/2$,

$$\frac{\pi\hbar}{q_e} = \frac{h}{2e} = \Phi_0 \approx 2.07\times10^{-15}\ \text{Wb},$$

the **magnetic flux quantum** (Wb = T m²). The factor 2 appears because the current is carried by electron pairs (standard; BCS theory is skipped in this sprint). The SQUID voltage oscillates once per $\Phi_0$ of flux through the loop (L113), so counting oscillations counts flux quanta. Real SQUIDs resolve a tiny fraction of one oscillation using a feedback "flux-locked loop", the same lock idea as M4.3 (standard practice; judgement, not in the lecture).

**Worked clone.** A 1 cm² pickup loop ($10^{-4}$ m²):
- One flux quantum corresponds to $B = \Phi_0/S = 2.07\times10^{-11}$ T, which is 20.7 pT.
- A brain-scale 1 fT field (L70 lists 100 fT for the brain; 1 fT is the SQUID noise floor at L119) is $10^{-15}\times10^{-4}/\Phi_0 = 4.8\times10^{-5}\,\Phi_0$.

So "fT sensitivity" means resolving about one twenty-thousandth of an oscillation.

**You've got it when** you can rewrite Eq. 2.2 as $BS = n\Phi_0$ and explain why the SQUID needs cryogenics (superconductivity, L113, L117) and why that costs standoff (thick insulation, L117).

### Move M5.3: The NV centre, read by fluorescence

**Idea.** An NV centre in diamond (L133) has a spin-1 ground state: $m_s = 0$ and $m_s = \pm1$. At zero field, $\pm1$ sit about 2.87 GHz above 0. A field $B$ along the NV axis shifts them by $\pm\gamma_e B$ with $\gamma_e \approx 28$ GHz/T, which is 28 MHz/mT (standard values; Degen, Reinhard & Cappellaro 2017, in the spec's Target Sources). Readout:
- Green laser light pumps the spin into $m_s = 0$ and makes it glow. $m_s = 0$ glows brighter than $\pm1$.
- Sweep a microwave frequency. When it hits a $0\to\pm1$ transition, the spin flips and the glow dims.
- Two dips appear at $2.87\ \text{GHz} \pm \gamma_e B$. Their separation, $2\gamma_e B$, gives $B$.

This is "inferred by fluorescence" (L133) unpacked. The sensor is one atom-sized defect, so resolution reaches nanometres (L135). One spin gives little light, so the noise is high (L137).

**Worked clone.** $B = 1$ mT on axis: dips at $2870 - 28 = 2842$ MHz and $2870 + 28 = 2898$ MHz, a splitting of 56 MHz.

**You've got it when** you can explain why NV wins on resolution and loses on sensitivity (one tiny sensor, few photons), and why averaging many NVs trades one for the other (L137).

### Move M5.4: The comparison table (Week 2's reusable asset)

The numbers come from the lecture, with line references. Cells marked (judgement) are not in the lecture.

| Sensor | Sensitivity | Bandwidth | Resolution / standoff | Cryogenics | SWaP-C |
|---|---|---|---|---|---|
| **SQUID** (quantum) | ~1 fT/√Hz for MEG (L119); ~$10^{-15}$ T/√Hz (L82) | tens of kHz (L119, L127) | pickup coil ~1 cm (L119); standoff set by thick cryostat insulation (L117), a few cm (judgement) | yes, superconductor (L113, L117) | large; cryogen upkeep raises cost (L117) |
| **OPM** (quantum) | ~10 fT/√Hz for MEG-grade sensors (L127); SERF lab results "similar or better" than SQUID (L125) | SERF < 200 Hz (L127) | vapour cell ~1 cm (L127); can sit much closer to the source (L125) | no; the cell is heated (L123) | compact, portable (L125); needs magnetic shielding for best performance (L84) |
| **NV centre** (quantum) | single NV ~100 nT/√Hz (L137); Fig. 2.2 places NV at ~$10^{-6}$ T/√Hz (L82) | not stated in the lecture | < 10 nm (L135); ~$10^{-8}$ m (L82); standoff nanometres (judgement) | no; works at room temperature (judgement; Degen et al. 2017) | small diamond, but needs a laser, microwaves and optics (L133) |
| **Fluxgate** (classical) | ~$10^{-10}$ T/√Hz = 100 pT/√Hz (L82) | not stated in the lecture | ~$10^{-2}$ m (L82) | no | small, robust, cheap (judgement) |
| **BEC microscope** (quantum) | ~2 nT at ~100 nm resolution (L149); a field resolution, not a noise density | limited by the time to make and move the BEC (L149) | ~100 nm, scanned near the sample surface (L141, L149) | no cryostat, but ultracold atoms in ultra-high vacuum with lasers (L141) | lab-scale (judgement) |

**Lecture inconsistencies to flag (do not copy them):**
1. **NV sensitivity, L82 vs L137.** $10^{-6}$ T/√Hz is 1000 nT/√Hz, ten times worse than the 100 nT/√Hz at L137. The two can only be reconciled by different devices and conditions. Quote a primary source with its conditions (F3).
2. **OPM vs SQUID, L125 vs L119/L127.** "Similar, if not better" (L125) cites a lab SERF result. The MEG-grade figures the lecture gives are 10 fT/√Hz for OPMs (L127) against 1 fT/√Hz for SQUIDs (L119), so the SQUID is 10× better. The OPM's real MEG advantage is standoff, not noise density (L125). A ratio needs both sides measured the same way (F3).
3. **Resolution, L82 vs L119/L127.** Fig. 2.2 places SQUIDs and OPMs at ~$10^{-3}$ m, but the text says ~1 cm for both. Treat it as "mm to cm".
4. **BEC "2 nT" (L149)** has no per-√Hz, so it cannot go in the same column as the others without an averaging time.
5. **Typos to read through:** "T√Hz" means T/√Hz (L74, inventory erratum); "κHz" means kHz (L119, L127); "ρT" means pT (L69); "1019" at L205 means $10^{19}$.
6. **Clock citations.** The $10^{-18}$ claim at L195 cites reference [36], whose title (L251) reports an absolute frequency at $1.8\times10^{-16}$. That is a different quantity, limited by the caesium reference. For $10^{-18}$, use Ludlow et al. 2015. The nuclear-clock sentence (L205) cites reference [37], which is about RF electric-field sensing (L252). "Currently theoretical" is also dated: a thorium nuclear transition was laser-excited in 2024 (judgement; check a primary source before quoting it).

**You've got it when** you can fill in the sensitivity and cryogenics columns from memory and say both inconsistencies (NV, OPM) in one sentence each.

## Exercises

### Exercise 3.1 (quantitative)

Two field-deployable clock references: the ⁸⁷Rb ground-state hyperfine transition at 6.834 682 611 GHz (used in rubidium vapour-cell clocks; standard value) and the ytterbium optical lattice-clock transition at 518.295 836 THz (Ludlow et al. 2015). For each, find the photon energy in joules and in eV. Then assume both are interrogated with the same 2 Hz linewidth and find each $Q$ and the ratio.

**Hint:** $E = h\nu$ with $h = 6.626\times10^{-34}$ J s; divide by $1.602\times10^{-19}$ J/eV. $Q = \nu/\Delta\nu$, so at equal linewidth the $Q$ ratio is just the frequency ratio.

**Solution sketch:**
- *Restate:* photon energies of two transitions, and their $Q$ at equal linewidth.
- *Write state:* $\nu_{\rm Rb} = 6.8347\times10^{9}$ Hz, $\nu_{\rm Yb} = 5.1830\times10^{14}$ Hz, $\Delta\nu = 2$ Hz.
- *Name move:* M4.1.
- *Algebra:* $E_{\rm Rb} = 6.626\times10^{-34}\times6.8347\times10^{9} = 4.53\times10^{-24}$ J $= 2.83\times10^{-5}$ eV. $E_{\rm Yb} = 3.43\times10^{-19}$ J $= 2.14$ eV, a yellow photon (578 nm). $Q_{\rm Rb} = 6.8347\times10^{9}/2 = 3.42\times10^{9}$; $Q_{\rm Yb} = 2.59\times10^{14}$.
- *Check:* ratio $5.183\times10^{14}/6.835\times10^{9} = 7.58\times10^{4}$, the same as $Q_{\rm Yb}/Q_{\rm Rb}$. A visible photon near 2 eV is right for an optical clock.
- *Answer:* $4.53\times10^{-24}$ J ($2.83\times10^{-5}$ eV) and $3.43\times10^{-19}$ J (2.14 eV). $Q = 3.42\times10^{9}$ and $2.59\times10^{14}$, a ratio of about 76 000.

### Exercise 3.2 (quantitative)

A microwave drive has Rabi frequency $\Omega/2\pi = 25$ kHz on resonance. (a) How long are the π and π/2 pulses? (b) What is $P_1$ after 5 µs? (c) A Ramsey sequence on the Rb transition of Exercise 3.1 uses a free time $T = 0.25$ s. What is the central fringe width, and what $Q$ does it give?

**Hint:** $\Omega t = \pi$ gives $t_\pi = 1/(2 f_{\rm Rabi})$, where $f_{\rm Rabi} = \Omega/2\pi$. For (b), compute $\Omega t/2$ in radians first. Ramsey width is $\Delta\nu \approx 1/(2T)$.

**Solution sketch:**
- *Restate:* pulse durations, an excitation probability, and a Ramsey linewidth.
- *Write state:* $\Omega = 2\pi\times25\times10^{3}$ rad/s; $t = 5\times10^{-6}$ s; $T = 0.25$ s; $\nu = 6.8347\times10^{9}$ Hz.
- *Name move:* M4.2, then M4.1.
- *Algebra:* (a) $t_\pi = 1/(2\times25\,000) = 20$ µs and $t_{\pi/2} = 10$ µs. (b) $\Omega t = 2\pi\times25\,000\times5\times10^{-6} = \pi/4$, so $\Omega t/2 = \pi/8$ and $P_1 = \sin^2(\pi/8) = 0.146$. (c) $\Delta\nu = 1/(2\times0.25) = 2$ Hz and $Q = 6.8347\times10^{9}/2 = 3.42\times10^{9}$.
- *Check:* 5 µs is a quarter of a π pulse, so $P_1$ should be well below the π/2 value of 0.5. It is.
- *Answer:* $t_\pi = 20$ µs, $t_{\pi/2} = 10$ µs; $P_1 = 0.146$; $\Delta\nu = 2$ Hz and $Q = 3.4\times10^{9}$ (this is the 2 Hz assumed in Exercise 3.1).

### Exercise 3.3 (quantitative) (stretch)

A clock's line has $\Delta\nu = 2$ Hz (Lorentzian model, as in M4.3). The local oscillator runs high by $\varepsilon = 0.15$ Hz. The servo probes at $\pm\Delta\nu/2$ from where it thinks the centre is. Compute both excitation probabilities, the error signal, and the linear estimate. Which way does the servo steer?

**Hint:** The probes land at detunings $\varepsilon - 1$ and $\varepsilon + 1$ Hz. $P_1(\delta) = 1/\big(1 + (2\delta/\Delta\nu)^2\big)$. Linear estimate: $e \approx 2\varepsilon/\Delta\nu$.

**Solution sketch:**
- *Restate:* the lock-loop error for a known mistuning.
- *Write state:* $\Delta\nu = 2$ Hz; probes at $-0.85$ Hz and $+1.15$ Hz from the true centre.
- *Name move:* M4.3.
- *Algebra:* $P_1(-0.85) = 1/(1 + 0.85^2) = 1/1.7225 = 0.581$; $P_1(+1.15) = 1/(1 + 1.15^2) = 1/2.3225 = 0.431$; $e = 0.150$.
- *Check:* linear estimate $2\times0.15/2 = 0.150$, which agrees, because 0.15 Hz is small compared with the 2 Hz linewidth.
- *Answer:* $e \approx 0.15 > 0$: the low-side probe sees more excitation, so the oscillator is high and the servo steers it down. Compare the worked clone: half the $Q$ (2 Hz instead of 1 Hz) gives a smaller error per hertz of mistuning.

### Exercise 3.4 (quantitative) (stretch)

A frequency comb has $f_{\rm rep} = 200$ MHz and $f_{\rm ceo} = 15$ MHz. A clock laser beats with tooth $n = 2\,591\,479$ at $f_{\rm beat} = 62$ MHz. What is the clock laser's frequency? What is the fastest signal your electronics had to count?

**Hint:** $\nu = n f_{\rm rep} + f_{\rm ceo} + f_{\rm beat}$. Do $n f_{\rm rep}$ in MHz first.

**Solution sketch:**
- *Restate:* read an optical frequency off a comb.
- *Write state:* $n = 2\,591\,479$; $f_{\rm rep} = 200$ MHz; $f_{\rm ceo} = 15$ MHz; $f_{\rm beat} = 62$ MHz.
- *Name move:* M4.4.
- *Algebra:* $2\,591\,479\times200$ MHz $= 518\,295\,800$ MHz; add 15 + 62 = 77 MHz to get $518\,295\,877$ MHz.
- *Check:* $5.18\times10^{14}$ Hz is the ytterbium transition of Exercise 3.1, to within 41 MHz, so $n$ is the right tooth.
- *Answer:* $\nu = 5.18295877\times10^{14}$ Hz. Nothing faster than 200 MHz was counted.

### Exercise 3.5 (quantitative) (stretch)

A simple model of clock instability (Ludlow et al. 2015 give this form with an order-one prefactor; the prefactor is dropped here as a judgement) is

$$\sigma_y(\tau) \approx \frac{1}{Q\cdot\text{SNR}}\sqrt{\frac{T_c}{\tau}},$$

where SNR is per measurement cycle, $T_c$ is the cycle time and $\tau$ the averaging time. This is the Day 02 $1/\sqrt{t}$ law (M2) with SNR from atom number (M3). Compare a caesium fountain ($Q = 9.19\times10^{9}$ at 1 Hz, SNR = 1000) with a strontium lattice clock ($Q = 4.29\times10^{14}$ at 1 Hz, SNR = 30), both with $T_c = 1$ s. Find $\sigma_y(1\ \text{s})$ for each, the ratio, and how long each must average to reach $1\times10^{-17}$.

**Hint:** At $\tau = T_c$ the square root is 1. To reach a target, solve $\sigma_y(\tau) = \sigma_1\sqrt{1\,\text{s}/\tau}$ for $\tau$: $\tau = (\sigma_1/\sigma_{\rm target})^2$ seconds.

**Solution sketch:**
- *Restate:* short-term stability and time to reach $10^{-17}$, microwave vs optical.
- *Write state:* the two $Q$ and SNR values; $T_c = 1$ s; target $10^{-17}$.
- *Name move:* M4.1 with M2 (1/√t) and M3 (SNR).
- *Algebra:* Cs: $\sigma_1 = 1/(9.19\times10^{9}\times1000) = 1.09\times10^{-13}$. Sr: $\sigma_1 = 1/(4.29\times10^{14}\times30) = 7.8\times10^{-17}$. Ratio about 1400. Time to $10^{-17}$: Cs $(1.09\times10^{-13}/10^{-17})^2 = 1.18\times10^{8}$ s, about 3.7 years. Sr $(7.8\times10^{-17}/10^{-17})^2 = 60$ s.
- *Check:* the $Q$ ratio alone is 47 000. The SNR ratio (1000/30) eats a factor of 33 of it, leaving 1400. The squaring in the averaging time turns 1400 into about $2\times10^{6}$.
- *Answer:* $1.1\times10^{-13}$ vs $7.8\times10^{-17}$ at 1 s, a ratio of 1400. Reaching $10^{-17}$ takes about 3.7 years for caesium and about 1 minute for strontium. This is why "optical beats microwave" is real, and also why it is less than the bare $Q$ ratio (F3: state conditions).

### Exercise 3.6 (quantitative)

Harrowmere Water & Power (fictional) needs substation clocks within 1 µs of UTC. During a loss of satellite timing each substation free-runs on its own oscillator (holdover). Fractional frequency offsets (fictional datasheet figures): quartz OCXO $1\times10^{-9}$; rubidium vapour-cell clock $5\times10^{-12}$; a hypothetical optical clock $1\times10^{-15}$. Assume a constant offset. (a) How long can each hold 1 µs? (b) What is the error of quartz and rubidium after Harrowmere's 8 h outage design case (fictional)? (c) What is 1 µs in grid phase at 50 Hz, and in light-travel distance?

**Hint:** $\delta t = y\,t$, so $t_{\max} = 1\ \mu\text{s}/y$. 8 h = 28 800 s. Phase: $360°\times f\times\delta t$. Distance: $c\,\delta t$.

**Solution sketch:**
- *Restate:* holdover time and error from fractional offsets.
- *Write state:* $y = 10^{-9}$, $5\times10^{-12}$, $10^{-15}$; $\delta t_{\max} = 10^{-6}$ s; $t_{\rm out} = 28\,800$ s.
- *Name move:* M1 (fractional error → time → distance).
- *Algebra:* (a) Quartz $10^{-6}/10^{-9} = 1000$ s, about 17 min. Rubidium $10^{-6}/(5\times10^{-12}) = 2\times10^{5}$ s, about 2.3 days. Optical $10^{9}$ s, about 32 years. (b) Quartz $10^{-9}\times28\,800 = 28.8$ µs (fails by 29×). Rubidium $5\times10^{-12}\times28\,800 = 0.144$ µs (passes with a 6.9× margin). (c) $360\times50\times10^{-6} = 0.018°$; $c\times10^{-6}$ s $= 300$ m.
- *Check:* the holdover ratio rubidium/quartz is 200, which equals the offset ratio $10^{-9}/(5\times10^{-12})$, as it must for a linear law.
- *Answer:* 17 min, 2.3 days, 32 years; 28.8 µs vs 0.14 µs after 8 h; 0.018° and 300 m. The optical clock's 32 years is irrelevant here: drift and other failures dominate long before (judgement).

### Exercise 3.7 (quantitative)

(a) A scalar ⁸⁷Rb OPM sits in a 48 µT background. What is its Larmor frequency? A buried steel object adds a 20 nT anomaly. How much does the frequency shift? (b) A SQUID has a 3 mm × 3 mm loop. What field change corresponds to one flux quantum? How many flux quanta does a 10 nT change thread? (c) Show that the lecture's $\pi\hbar/q_e$ equals $h/2e$ numerically.

**Hint:** $f_L = \gamma B$ with $\gamma = 7$ Hz/nT. $B_{\Phi_0} = \Phi_0/S$. $\Phi_0 = 6.626\times10^{-34}/(2\times1.602\times10^{-19})$.

**Solution sketch:**
- *Restate:* Larmor frequency and shift; field per flux quantum; the Eq. 2.2 constant.
- *Write state:* $B = 48\,000$ nT; $\Delta B = 20$ nT; $S = 9\times10^{-6}$ m²; $\Delta B_2 = 10^{-8}$ T.
- *Name move:* M5.1, M5.2.
- *Algebra:* (a) $f_L = 7\times48\,000 = 336$ kHz; shift $7\times20 = 140$ Hz. (b) $\Phi_0 = 2.07\times10^{-15}$ Wb, so $B_{\Phi_0} = 2.07\times10^{-15}/9\times10^{-6} = 2.3\times10^{-10}$ T $= 230$ pT, and $n = 10^{-8}\times9\times10^{-6}/2.07\times10^{-15} = 43.5$. (c) $\pi\hbar = \pi h/2\pi = h/2$, so $\pi\hbar/q_e = h/2e = 2.07\times10^{-15}$ Wb.
- *Check:* a smaller loop (9 mm² vs 1 cm²) needs a larger field per $\Phi_0$: 230 pT vs 20.7 pT, a factor $100/9 = 11$. Correct direction and size.
- *Answer:* 336 kHz with a 140 Hz shift; 230 pT per $\Phi_0$ and about 44 $\Phi_0$; $\Phi_0 = 2.07\times10^{-15}$ Wb.

### Exercise 3.8 (quantitative) (stretch)

(a) An NV centre sees $B = 0.5$ mT along its axis. Where are the two fluorescence dips? (b) Another NV shows dips 196 MHz apart. What is $B$ along its axis? (c) By what factor do the lecture's two NV sensitivities (L82, L137) disagree?

**Hint:** Dips at $2870 \pm 28\,B$ MHz with $B$ in mT. The splitting is $2\times28\,B$. For (c), convert $10^{-6}$ T/√Hz to nT/√Hz first.

**Solution sketch:**
- *Restate:* ODMR line positions, field from a splitting, and the lecture's inconsistency.
- *Write state:* $\gamma_e = 28$ MHz/mT; $D = 2870$ MHz; $B = 0.5$ mT; splitting 196 MHz; $10^{-6}$ T/√Hz vs 100 nT/√Hz.
- *Name move:* M5.3, M5.4 (and F3).
- *Algebra:* (a) $28\times0.5 = 14$ MHz, so dips at 2856 MHz and 2884 MHz. (b) $B = 196/(2\times28) = 3.5$ mT. (c) $10^{-6}$ T/√Hz $= 1000$ nT/√Hz, and $1000/100 = 10$.
- *Check:* (a) splitting 28 MHz $= 2\times14$. Consistent with the worked clone, which had 56 MHz at 1 mT.
- *Answer:* 2856 and 2884 MHz; 3.5 mT; a factor of 10. Quote one primary source, with conditions, rather than either lecture number.

### Exercise 3.9 (writing)

Harrowmere Water & Power (fictional) time-stamps phasor measurements at its substations. Write a 150-200-word F1 gain argument: should Harrowmere replace its satellite-disciplined quartz holdover with a quantum clock? Use your Exercise 3.6 numbers.

**Hint:** Walk the six F1 parts in order. The classical limit is quartz holdover time. The mechanism is the lock loop (M4.3) to an atomic line. The figure of merit is holdover time to 1 µs. The honest maturity call is that a rubidium clock (mature, commercial) is the quantum answer here, not an optical clock. The caveat is the constant-offset assumption.

**Model paragraph:** Harrowmere Water & Power's substation clocks must stay within 1 µs of UTC, 0.018° of phase at 50 Hz (fictional requirement). When satellite timing is lost, each substation's quartz OCXO free-runs at a fractional offset of $1\times10^{-9}$ (fictional), so it breaks the budget after about 17 minutes, and the 8 h outage design case (fictional) leaves it 28.8 µs out. A rubidium clock locks the same kind of oscillator to the ⁸⁷Rb hyperfine transition at 6.834 GHz, a frequency set by atomic physics rather than by a cut crystal. The figure of merit is holdover time to 1 µs. At a $5\times10^{-12}$ offset (fictional), the 8 h error is 0.144 µs, a sevenfold margin, and holdover stretches to about 2.3 days, 200 times the quartz figure. Rubidium clocks are commercial products (TRL 9, judgement) costing about 10 times the quartz unit (fictional); an optical clock would add laboratory-grade risk for no operational gain. Verdict: fit rubidium holdover at the substations whose protection depends on synchronised measurements. The caveat is the constant-offset assumption: real oscillators age and drift with temperature, so test against a holdover specification measured under stated conditions.

**What a weak answer misses:**
- No number for the classical limit. "Quartz drifts" is not a limit; "1 µs lost after 17 minutes" is.
- Reaching for the optical clock because it has the best headline uncertainty. That ignores that the requirement is already met about 7× over by a mature device (maturity framework, Day 10).
- Quoting the $10^{-18}$ lab uncertainty (L195) as if it were a holdover specification. Uncertainty and holdover drift are different quantities measured under different conditions (F3).
- No caveat, or a vague one ("quantum is expensive") instead of the specific constant-offset assumption.

### Exercise 3.10 (writing)

Harrowmere (fictional) suspects a stray DC leakage current along a buried steel water main, which drives corrosion. Its survey team uses fluxgates. Write a 150-200-word F1 argument on whether a quantum magnetometer improves detection. Use these fictional figures: leakage current 5 mA, depth 2 m, survey bandwidth 10 Hz. Use the comparison table to rule sensors in or out.

**Hint:** A long straight current gives $B = \mu_0 I/(2\pi r)$, falling as $1/r$, not the $1/r^2$ of the lecture's dipole (Eq. 2.1). This is a standard result, not in the lecture. Noise in a bandwidth is $S\sqrt{\Delta f}$ (M2). Rule out SERF (needs near-zero field), SQUID (cryogenics on a survey van) and NV (built for nanometre imaging, high noise). For the caveat, ask what else near a steel main produces a *static* field, and how a survey team would make the leakage signal distinguishable from it.

**Model paragraph:** Harrowmere Water & Power (fictional) suspects a 5 mA DC leakage current along a steel main 2 m down. A line current gives $B = \mu_0 I/2\pi r = 500$ pT at the surface. Its fluxgates, about 100 pT/√Hz (L82), give 316 pT of noise in the 10 Hz survey bandwidth: SNR 1.6, marginal. A scalar optically pumped magnetometer reads the field from the Larmor precession of pumped rubidium atoms, 7 Hz per nT, so the signal is a 3.5 Hz shift on about 350 kHz; it senses only the anomaly's component along Earth's field. The figure of merit is noise in the survey bandwidth: an Earth-field OPM at about 1 pT/√Hz (judgement; Budker & Romalis 2007) gives 3.2 pT and an SNR near 160, a hundredfold gain. SERF (zero field), SQUIDs (cryogenics) and NV (noise) are ruled out. Scalar OPMs are sold for survey (judgement). Verdict: the sensor gain is real but undelivered. A static 500 pT field cannot be told apart from the main's own magnetisation, typically tens to thousands of nT (judgement), or from geology. The fix is to inject a known AC current and lock in to it, after which a fluxgate may suffice.

**What a weak answer misses:**
- Using $1/r^2$ for a line current. The lecture's Eq. 2.1 is for a compact (dipole-like) source.
- Quoting the 1 fT/√Hz SQUID or SERF number for a field survey. Those figures need cryogenics or shielding and near-zero field, which a trench does not offer (L84, L117, L127).
- Comparing noise densities without a bandwidth. SNR needs $S\sqrt{\Delta f}$, not $S$ alone (M2).
- Claiming the 100× sensor gain is the delivered gain. A DC field is buried in static clutter (the main's own magnetisation, geology) that no sensor noise figure addresses; the standard remedy is to inject a known AC current and lock in to it.
- Forgetting that a scalar OPM measures only the component of the anomaly along Earth's field.

## Anti-patterns / Common mistakes

- **Treating "optical is 47 000× better" as the delivered gain.** You notice when your stability ratio equals the frequency ratio. Instead, include SNR (Exercise 3.5): the practical gain is about $10^{3}$ at 1 s, and a different factor at each averaging time.
- **Locking to the peak.** You notice when you cannot say which way to steer. Instead, probe both sides and subtract (M4.3).
- **Mixing ordinary and angular frequency.** You notice a stray $2\pi$: a π pulse that comes out 6.28× too long. Instead, write $\Omega = 2\pi f_{\rm Rabi}$ and keep units on every line.
- **Copying the lecture's table numbers without the conditions.** You notice two lecture lines that disagree (NV at L82 vs L137; OPM at L125 vs L127). Instead, quote one primary source with its date, device and conditions (F3).
- **Choosing the most sensitive sensor regardless of environment.** You notice your answer needs a shielded room or a cryostat in the field. Instead, rule sensors in or out on bandwidth, standoff, cryogenics and SWaP-C before noise density (M5.4).
- **Leaving Eq. 2.2 as "πħ/q_e" with no name.** Instead, write $\Phi_0 = h/2e = 2.07\times10^{-15}$ Wb. Now you can compute field per flux quantum.

## Done when

No notes, 25 minutes. Pass mark: 8 of 10.

1. Write $E$ for the caesium transition to 2 significant figures.
2. State $Q$, and why optical beats microwave at equal linewidth.
3. From $H = (\hbar\Omega/2)\sigma_x$, derive $P_1 = \sin^2(\Omega t/2)$, and name the π/2 and π pulses' roles.
4. Ramsey free time 0.1 s: give the linewidth (answer: 5 Hz).
5. Draw the lock loop as a control loop with all six parts.
6. Write the comb equation and say what it is for.
7. Convert $10^{-15}$ over one day into seconds and metres (answer: 86.4 ps, 2.6 cm).
8. Write $f_L = \gamma B$ with the Rb value, and $\Phi_0 = h/2e$ with its value.
9. Explain NV readout in three steps.
10. Fill in the SQUID, OPM and NV rows of the comparison table (sensitivity, bandwidth, cryogenics) and name one lecture inconsistency.

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 02 (M2, M3):**
1. An OPM has 10 fT/√Hz noise. What is its noise in a 100 Hz bandwidth?
2. A measurement averages for 100 s instead of 1 s. By what factor does white noise fall?
3. A sensor uses $N = 10^{6}$ independent atoms. What is the shot-noise-limited relative uncertainty? What would the Heisenberg limit give?
4. A dipole-like source field falls as $1/r^2$. You halve the distance. By what factor does the signal rise? (The lecture's L94 wording is wrong here.)

**From Day 01 (F1, M1):**
5. List the six parts of the F1 gain argument in order.
6. How many femtotesla is Earth's field of 50 µT?
7. Name the source hierarchy in F3, top to bottom.

**Answers:**
1. $10\ \text{fT/√Hz}\times\sqrt{100\ \text{Hz}} = 100$ fT.
2. $\sqrt{100} = 10$.
3. $1/\sqrt{N} = 10^{-3}$; Heisenberg $1/N = 10^{-6}$.
4. 4×, because $(r_1/r_2)^2 = 2^2$. The lecture says the amplitude "increases by $r^2$" (L94); the correct statement is the ratio.
5. Classical limit, with a number; quantum mechanism, in one sentence of physics; figure of merit named; quantified gain; maturity and practicality; verdict, with one honest caveat.
6. $50\times10^{-6}/10^{-15} = 5\times10^{10}$ fT.
7. Peer-reviewed or metrology institute > review > vendor datasheet > press release > market report.

## Read next

- **Ludlow, Boyd, Ye, Peik & Schmidt, *Optical atomic clocks*, RMP 87, 637 (2015):** <https://arxiv.org/abs/1407.3493>. Read §I (introduction) and the applications section. Look for the stability formula behind Exercise 3.5 and the list of optical transitions behind Exercise 3.1. Optional light companion: the NPL page, <https://www.npl.co.uk/research/time-frequency/optical-atomic-clocks>.
- **Budker & Romalis, *Optical magnetometry*, Nat. Phys. 3, 227 (2007):** <https://arxiv.org/abs/physics/0611246>. Read all of it (it is short). Look for Larmor precession, SERF, and the sensitivity comparison with SQUIDs. Check it against M5.4 lines 1-2.

**Companion pointer (15 min).** Open `companions/week02_companion.md` and read its §4 (lecture errata for Week 2, including L74, L82 vs L137 and L94). Then do the Week 2 quiz. All four items are general-knowledge "which devices" questions; the key is in `docs/problem_inventory.md`, Quizzes table, rows Week 2 Q1-Q4. Answer first, then check. Log any symbol, step or concept that stuck today in your confusion log (STRATEGY.md template).
