# Week 02 Companion: Quantum sensors part 1, clocks and magnetometers

**Built on:** [Day 02](../day02.md) (M2 noise density, √Δf and Allan deviation; M3 shot noise, SNR and the inverse-square distance gain) and [Day 03](../day03.md) (M4 two-level frequency reference, E = hν, Q, the lock loop; M5 SQUID, OPM and NV in one line each).
**Feeds:** Assessment 2 via the Week 2 Consolidate piece (300-word quantified gain argument). Not Assessment 1 content.

Lecture line numbers (L…) refer to `week_2/week_2_lecture.md`. Reading protocol: the Five-Pass Lecture Protocol in [STRATEGY](../../STRATEGY.md).

## 1. Read these first (Pass 0)

- **Apply (task, writing):** pick one clock or magnetometer plus one application; 200-300 words on why the quantum approach matters there (F1, M2, M4, M5).
- **Consolidate (portfolio, writing):** one or two quantum advantages against a named classical limitation, 300 words, quantified in sensitivity, bandwidth, dynamic range or practicality (F1, F3, M1-M5).
- **Consolidate (notes):** keep a reflection document; no marking.
- **Explore and Checkpoint quizzes:** four "which devices contain magnetometers / rely on precise timing" items, the same in both quizzes with shuffled options; answers: see inventory key (`docs/problem_inventory.md`, Week 2 rows).

There is no numbered maths problem this week. The "problems" are the numbers you must be able to reproduce and reuse: noise in a bandwidth, signal versus distance, flux quanta, E = hν, fractional uncertainty in seconds per years, and Q.

## 2. What the lecture is doing, in one picture

A sensor is judged by four things before cost: precision (spread), accuracy (offset from truth), bandwidth (how fast a signal it can follow) and dynamic range (how big a signal it can take). Magnetometers turn a magnetic field into something countable: flux quanta in a superconducting loop (SQUID), the spin precession of a pumped atomic vapour (OPM), the spin of a defect in diamond (NV), or the shape of a Bose-Einstein condensate (BEC microscope). Each trades sensitivity against spatial resolution, which is what Figure 2.2 plots. Clocks turn an atomic transition E = hν into a frequency that a loop keeps a local oscillator locked to. Moving that transition from microwave (about 9 GHz) to optical (hundreds of THz) makes the resonance much sharper relative to its frequency, which is why optical clocks now reach about one part in $10^{18}$. The lecture tells this story in words and leaves most of the arithmetic out; §4 puts it back.

## 3. Notation and unit decoder

| As written (line) | Read it as | Unit / size | Move |
|---|---|---|---|
| "precision" (L36) | spread of repeated readings; random error | same unit as the reading | M2 |
| "accuracy" (L36) | closeness of the mean to the true value; systematic error | same unit | M2 |
| "bandwidth" (L47) | frequency at which the response amplitude falls to $1/\sqrt2$ of its low-frequency value (the −3 dB point) | Hz | M2 |
| "dynamic range" (L47) | largest signal the sensor can record before it saturates, usually quoted against its noise floor | ratio, or T | M2 |
| SWaP-C (L55 in words) | size, weight, power and cost | kg, L, W, £ | F2 |
| T, mT, µT, pT, fT (L64-L70) | tesla and its sub-multiples: $10^{-3}$, $10^{-6}$, $10^{-12}$, $10^{-15}$ | T | M1 |
| "100ρT" (L69) | typo for 100 pT $=10^{-10}$ T | T | M1 |
| "$T\sqrt{\text{Hz}}$" (L74) | typo for T/√Hz, a noise **density** | T Hz$^{-1/2}$ | M2 |
| T/Hz$^{1/2}$ (L82, Fig. 2.2 axis) | the same noise density written as a power | T Hz$^{-1/2}$ | M2 |
| $B\propto 1/r^2$ (Eq. 2.1, L92) | field of a current dipole falls with the square of distance | T | M3 |
| $\mathbf B\cdot\mathbf S$ (Eq. 2.2, L115) | magnetic flux $\Phi$ through a loop of area $S$ | Wb $=$ T m² | M5 |
| $\pi\hbar/q_e$ (L115) | the flux quantum $\Phi_0=h/2e\approx2.07\times10^{-15}$ Wb | Wb | M5 |
| $n$ (L113) | number of flux quanta threading the loop (count of voltage oscillations) | none | M5 |
| "κHz" (L119, L127) | typo for kHz | Hz | M1 |
| "$<10\,\mathbb{nm}$", "100 nm", "2 nT" (L135, L149) | blackboard-bold n is a rendering error for the prefix nano | m, T | M1 |
| SERF (L127) | spin-exchange relaxation-free: the most sensitive, slowest OPM regime | none | M5 |
| stability (L155) | how much the clock's frequency wanders over an averaging time $\tau$; quantified as the Allan deviation $\sigma_y(\tau)$ (not named in the lecture) | dimensionless | M2 |
| uncertainty (L157) | how far the clock's frequency may sit from the unperturbed transition (systematics); the clock's "accuracy" | dimensionless, fractional | M1, M4 |
| "one part in $10^{16}$" (L159) | fractional uncertainty $\Delta\nu/\nu=10^{-16}$ | dimensionless | M1 |
| $\Delta\nu_{\mathrm{Cs}}$ (L161) | the caesium hyperfine frequency, exactly 9 192 631 770 Hz by definition | Hz | M4 |
| $E=h\nu$ (Eq. 2.3, L185) | photon energy equals Planck constant times frequency | J (or eV) | M4 |
| $h\approx6.63\times10^{-34}$ J·Hz$^{-1}$ (L187) | J·Hz$^{-1}$ is the same as J·s | J s | M4 |
| "100s of terahertz ($\sim100\times10^{12}$ Hz)" (L193) | optical clock transitions lie at roughly 400-1100 THz | Hz | M4 |
| frequency comb (L195) | a pulsed laser whose spectrum is a ruler of evenly spaced lines; links optical to countable microwave frequencies | Hz | M4 |
| "1019" (L205) | typo for $10^{19}$ (one part in $10^{19}$) | dimensionless | M1 |

## 4. Skipped steps, expanded

### 4.1 Bandwidth as the −3 dB point (L47, M2)

The lecture says the bandwidth is where "the response is reduced by a factor of $1/\sqrt2$". That is an **amplitude** factor. Power goes as amplitude squared, so the power has halved, and in decibels $20\log_{10}(1/\sqrt2)=-3.01$ dB. That is why datasheets say "−3 dB bandwidth". Two consequences the lecture leaves implicit:

1. At the bandwidth frequency the sensor still responds, at 71% amplitude. A signal changing at exactly the bandwidth is under-read by 29%, so you want the bandwidth comfortably above the signal frequency.
2. Bandwidth also sets how much noise you collect (§4.2). Wider bandwidth means you follow faster signals but integrate more noise.

### 4.2 Noise density and noise in a bandwidth (L74, M2)

**Erratum, L74.** The lecture gives the unit as $T\sqrt{\text{Hz}}$. The correct unit is **T/√Hz** (as the lecture itself writes on L82 and L119). The quantity is a noise spectral density $S$ (more precisely its square root, the amplitude spectral density).

The missing line is what you do with it. For white noise, the rms noise you actually see in a measurement bandwidth $\Delta f$ is
$$\delta B_{\mathrm{rms}}=S\sqrt{\Delta f}.$$
With the lecture's own MEG numbers (L119, L127) and a 100 Hz analysis bandwidth: SQUID $1\ \mathrm{fT}/\sqrt{\mathrm{Hz}}\times\sqrt{100}=10$ fT rms; MEG OPM $10\ \mathrm{fT}/\sqrt{\mathrm{Hz}}\times\sqrt{100}=100$ fT rms. The brain field on L70 is about 100 fT, so at equal distance the SQUID sees it at SNR about 10 and the OPM at SNR about 1. That is why §4.3 matters: the OPM has to win back its factor 10 through distance. Over the SQUID's full tens-of-kHz bandwidth you would not use all of it for MEG; at 1 kHz the SQUID's rms noise is $1\times\sqrt{1000}=31.6$ fT.

Averaging is the same law read the other way: a measurement averaged for time $t$ has an effective bandwidth of order $1/t$, so the noise falls as $1/\sqrt t$. To halve the noise you average four times longer.

### 4.3 Distance: the ratio is $(r_1/r_2)^2$ (L94, M3)

**Erratum, L94.** "The amplitude of the signal increases by $r^2$" is not a usable statement. From Eq. 2.1, $B\propto1/r^2$, so the **ratio** of signals at two distances is
$$\frac{B(r_2)}{B(r_1)}=\left(\frac{r_1}{r_2}\right)^2 .$$
Halve the distance and the signal rises 4×. Since the sensor noise does not change with distance (L94 says this correctly), the SNR rises by the same factor.

Apply it to L125 versus L127. The OPM needs to gain a factor 10 in signal to match the SQUID's factor-10 noise advantage. That needs $(r_1/r_2)^2=10$, so $r_2=r_1/\sqrt{10}=0.316\,r_1$: the OPM must sit at about a third of the SQUID's source distance. (Judgement: a current dipole's field falls as $1/r^2$, as Eq. 2.1 says; the field of a small current *loop*, a magnetic dipole, falls faster, as $1/r^3$, so the distance gain is even larger for such sources. See Degen et al., https://arxiv.org/abs/1611.02427, §III, for sensor-to-source distance in general.)

### 4.4 Eq. 2.2 is "n flux quanta" (L113-L117, M5)

Rewrite the right-hand side: $\pi\hbar/q_e=\pi(h/2\pi)/e=h/2e$. That constant is the **magnetic flux quantum**
$$\Phi_0=\frac{h}{2e}=2.07\times10^{-15}\ \mathrm{Wb}.$$
So Eq. 2.2 says: flux through the loop $=n\Phi_0$. Each time the flux changes by one $\Phi_0$ the voltage across the biased SQUID goes through one oscillation, and counting oscillations counts flux quanta. The factor 2 comes from the charge carriers in a superconductor, Cooper pairs of charge $2e$, though the lecture writes $q_e$ as "the charge of an electron" without saying so.

**Erratum, L113.** The lecture says "by measuring the current either side of the loop". A current is applied as a bias; what is **measured** is the voltage across the loop, which oscillates with flux (as the lecture's own previous sentence says).

**Why that gives fT.** For a 1 cm² pickup loop (L119: about 1 cm), one flux quantum corresponds to $B=\Phi_0/S=2.07\times10^{-15}/10^{-4}=2.07\times10^{-11}$ T, about 21 pT. To resolve 1 fT the electronics must resolve about $10^{-15}/2.07\times10^{-11}=4.8\times10^{-5}$ of a flux quantum. SQUIDs do this by working on the steep side of one oscillation rather than by counting whole oscillations (judgement; standard practice, see the lecture's ref. [14], Fagaly 2006).

### 4.5 E = hν with the caesium numbers (L183-L189, M4)

The lecture gives the formula and $h$ but no number. Put in the defined caesium frequency (L161):
$$E=h\nu=6.626\times10^{-34}\times9.193\times10^{9}=6.09\times10^{-24}\ \mathrm{J}=3.80\times10^{-5}\ \mathrm{eV}.$$
That is about 38 µeV, tiny compared with thermal energy at room temperature (about 25 meV), which is why clocks first prepare the atoms in one state (L189). For an optical transition, take strontium's 429 THz clock line (Ludlow et al., https://arxiv.org/abs/1407.3493, §I and tables): $E=2.84\times10^{-19}$ J $=1.78$ eV, a visible-red photon, and a frequency about $4.67\times10^4$ times caesium's.

L187's "the change in energy is extremely small compared with the change in frequency" compares quantities with different units and means nothing as written. The intended point is that $h$ is a tiny number in SI units, so a small energy gap corresponds to a large, easily counted frequency.

### 4.6 The lock loop (interrogation) is described but not named (L189, M4)

L189 describes a feedback loop without naming it. The steps:

1. A local oscillator (quartz, or a laser for optical clocks) produces a probe frequency $f$.
2. The atoms are interrogated at $f$: in a fountain or lattice clock, by two pulses separated by a free-evolution time $T$ (Ramsey interrogation). The fraction of atoms that changed state is measured.
3. The probe is stepped to either side of the line; the difference in excited fraction says whether $f$ is above or below resonance.
4. A servo corrects $f$. Repeat. The oscillator is now **locked** to the atoms, and its output is the clock.

The linewidth the loop locks to is set by the interrogation time: for Ramsey interrogation $\Delta\nu\approx1/(2T)$ (judgement, standard result; Ludlow et al. §I). Longer $T$, narrower line, better lock.

### 4.7 Why optical wins: $Q=\nu/\Delta\nu$ (L193-L195, M4)

L193 says optical clocks "tick faster" and "can be even more stable". The missing quantity is the **quality factor** $Q=\nu/\Delta\nu$. A lock loop measures frequency to some fraction of the linewidth $\Delta\nu$, so the fractional instability scales as $1/Q$ (and improves with $\sqrt{\text{number of atoms}}$ and $\sqrt{\text{averaging time}}$, M2-M3). Both kinds of clock have observed linewidths of order 1 Hz (judgement, order of magnitude; Ludlow et al. §I). Then Cs: $Q\approx9.19\times10^{9}$; Sr: $Q\approx4.29\times10^{14}$. Same linewidth, about $4.7\times10^4$ times higher $Q$: that factor, not "faster ticking" as such, is why optical wins. The comb (L195) is what made the optical $Q$ usable, because it lets you count the optical cycles.

### 4.8 Stability versus averaging time is the Allan deviation (L155, M2)

"The stability of a clock is often given as a function of an averaging time" (L155) is a description of the **Allan deviation** $\sigma_y(\tau)$, the standard plot of fractional frequency instability against averaging time $\tau$. For white frequency noise it falls as $1/\sqrt\tau$:
$$\sigma_y(\tau)=\frac{\sigma_y(1\ \mathrm s)}{\sqrt{\tau/1\ \mathrm s}}.$$
Example: a clock with $\sigma_y(1\ \mathrm s)=10^{-13}$ reaches $10^{-16}$ after $\tau=(10^{-13}/10^{-16})^2=10^6$ s, about 11.6 days. The curve flattens when systematics take over, which is where **uncertainty** (L157) lives. Stability is the precision axis, uncertainty the accuracy axis, exactly as in Figure 2.1.

### 4.9 Fractional uncertainty in seconds and years (L159, L195, L205, M1)

The lecture's "1 second every 300 million years ... one part in $10^{16}$" is a conversion it does not show:
$$\frac{1\ \mathrm s}{300\times10^6\times3.156\times10^7\ \mathrm s}=\frac{1}{9.47\times10^{15}}=1.06\times10^{-16}.$$
Reverse it for L195: one part in $10^{18}$ means 1 s in $10^{18}$ s $=10^{18}/3.156\times10^7=3.17\times10^{10}$ years, about 32 billion years (the lecture says 30 billion; the universe is about 13.8 billion years old, so "longer than double" holds). L205's nuclear clock at one part in $10^{19}$ ("1019" is a typo) is 1 s in about $3.2\times10^{11}$ years.

For engineering use, convert to time error per day and then to distance with $c$: at $10^{-16}$, one day gives $10^{-16}\times86\,400=8.64\times10^{-12}$ s, and light travels $c\times8.64\times10^{-12}=2.6$ mm in that time. Satnav ranging is the reason timing errors are quoted in metres.

### 4.10 Inconsistencies and typos to note

| Line(s) | Lecture says | What to use |
|---|---|---|
| L82 vs L137 | NV centres "around $10^{-6}$ T/√Hz" (Fig. 2.2 text) versus single NV "approximately 100 nT/√Hz" $=10^{-7}$ T/√Hz | The two differ by 10×. Figure 2.2 itself shows NV points from about $10^{-5}$ to $10^{-8}$ T/√Hz, depending on whether one NV or an ensemble is used and on resolution. Quote a primary source with its conditions (Degen et al. §III; the lecture's refs. [25], [26]). |
| L125 vs L127 | OPMs "similar, if not better" than SQUIDs, then MEG OPMs at about 10 fT/√Hz versus SQUIDs at 1 fT/√Hz | Both are true for different devices. "Better" refers to laboratory SERF records (ref. [19], Kominis et al. 2003, sub-fT); MEG-designed OPMs are about 10× noisier but sit closer to the head (§4.3). Say which device you mean. Budker & Romalis (https://arxiv.org/abs/physics/0611246) give the background. |
| L69 | "100ρT" | 100 pT |
| L119, L127 | "κHz" | kHz |
| L205 | "1019" | $10^{19}$ |
| L113 | measure "the current" | measure the voltage (§4.4) |
| L187 | energy "small compared with" frequency | different units; see §4.5 |
| L205 / ref. [37] | nuclear clock claim cites ref. [37] | ref. [37] (Fan et al. 2015) is about atom-based RF electric field sensing, not nuclear clocks. Treat the $10^{-19}$ projection as unsourced in the lecture (observation). |
| L45 vs Fig. 2.1 | text lists four precision/accuracy combinations | the figure draws three; "low precision, high accuracy" (scatter centred on the bullseye) is not drawn (§8). |

## 5. Clones

These have the same *type* as the week's work (quantified gain comparisons and unit conversions) with numbers and cases that are not in the lecture. Quantitative sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer.

### Exercise C2.1 (quantitative)

Two magnetometers are offered for a pipe-inspection survey. Sensor P (classical) has noise density 20 pT/√Hz and a 500 Hz bandwidth. Sensor Q (quantum, vapour cell) has 50 fT/√Hz and a 50 Hz bandwidth. Both would be used over their full bandwidth. (a) Find the rms noise of each. (b) Find the SNR of each for a 5 nT anomaly. (c) The anomaly signal, seen from a moving vehicle, has content up to 120 Hz. What does that do to the comparison?

**Hint:** noise in a bandwidth is $S\sqrt{\Delta f}$ (M2). Then read §4.1 for what happens above the −3 dB point.

**Solution sketch:**
1. *Restate.* Compare rms noise and SNR for two sensors; check that bandwidth covers the signal.
2. *Write state.* $S_P=20\times10^{-12}$ T/√Hz, $\Delta f_P=500$ Hz; $S_Q=50\times10^{-15}$ T/√Hz, $\Delta f_Q=50$ Hz; signal 5 nT.
3. *Name move.* M2 ($\delta B=S\sqrt{\Delta f}$), M3 (SNR $=$ signal/noise).
4. *Algebra.* P: $20\times10^{-12}\times\sqrt{500}=4.47\times10^{-10}$ T $=447$ pT. Q: $50\times10^{-15}\times\sqrt{50}=3.54\times10^{-13}$ T $=354$ fT. SNR: P $=5\times10^{-9}/4.47\times10^{-10}=11.2$; Q $=5\times10^{-9}/3.54\times10^{-13}=1.41\times10^4$. Noise ratio $=447/0.354\approx1.26\times10^3$.
5. *Check.* Q's density is 400× lower, but its bandwidth is 10× smaller, which helps it by a further $\sqrt{10}=3.16$: $400\times3.16=1265$. Consistent.
6. *Answer.* (a) 447 pT and 354 fT. (b) 11.2 and about 14 000. (c) Q's 50 Hz bandwidth is below the 120 Hz content, so Q under-reads the fast part of the anomaly (at 50 Hz it is already down to 71%); P follows it. Q's sensitivity advantage is real only if the survey slows down until the signal fits inside 50 Hz.

Sensitivity numbers mean nothing until you multiply by √bandwidth and check the bandwidth covers the signal.

### Exercise C2.2 (quantitative)

Sensor A has noise density 3 fT/√Hz but needs a cryostat, so its sensing element sits 4.5 cm from a small corrosion current treated as a current dipole ($B\propto1/r^2$). Sensor B, which runs warm, has 12 fT/√Hz and can sit 1.5 cm from the source. (a) By what factor does B's SNR exceed A's? (b) For how long must A average to match the SNR that B achieves in 1 s?

**Hint:** signal ratio $(r_1/r_2)^2$ (§4.3), noise ratio from the densities, then SNR $\propto\sqrt t$ (M2).

**Solution sketch:**
1. *Restate.* Compare SNR of two sensors at different standoffs, then trade averaging time for SNR.
2. *Write state.* $S_A=3$, $S_B=12$ fT/√Hz; $r_A=4.5$ cm, $r_B=1.5$ cm; $B\propto1/r^2$.
3. *Name move.* M3 (inverse-square ratio), M2 ($1/\sqrt t$ averaging).
4. *Algebra.* Signal ratio B/A $=(4.5/1.5)^2=9$. Noise ratio B/A $=12/3=4$. SNR ratio $=9/4=2.25$. A's SNR grows as $\sqrt t$, so it needs $t=2.25^2=5.06$ s.
5. *Check.* Units cancel in every ratio; 3× closer gives 9× signal, the right direction.
6. *Answer.* (a) B's SNR is 2.25× higher. (b) A must average about 5.1 s.

The quieter sensor loses because the distance law is squared and the noise ratio is not.

### Exercise C2.3 (quantitative)

Harrowmere Water & Power (fictional) time-stamps grid measurements at 50 Hz, and its substation clocks must stay within 1 µs of UTC. If satellite timing is lost, each substation runs on its local oscillator; the design case is an 8 h outage. Its fictional options: the installed quartz OCXO with fractional frequency offset $1\times10^{-9}$, or a rubidium clock at $5\times10^{-12}$. (a) What time error does each build up over the 8 h outage? (b) What phase error is that at 50 Hz? (c) How long until each exceeds the 1 µs limit? (d) Express the rubidium clock's 8 h error as a light-travel distance.

**Hint:** time error $=y\times t$ (M1, §4.9); phase in degrees $=360\times f\times\Delta t$.

**Solution sketch:**
1. *Restate.* Turn fractional offsets into time error, phase error, holdover time and distance.
2. *Write state.* $y_q=10^{-9}$, $y_a=5\times10^{-12}$; $t=8\times3600=28\,800$ s; $f=50$ Hz; limit $10^{-6}$ s; $c=3.00\times10^8$ m/s.
3. *Name move.* M1 (fractional error → time → distance via $c$).
4. *Algebra.* (a) Quartz: $10^{-9}\times28\,800=2.88\times10^{-5}$ s $=28.8$ µs. Rubidium: $5\times10^{-12}\times28\,800=1.44\times10^{-7}$ s $=0.144$ µs. (b) Quartz: $360\times50\times2.88\times10^{-5}=0.518^\circ$. Rubidium: $360\times50\times1.44\times10^{-7}=0.00259^\circ$. (c) Quartz: $10^{-6}/10^{-9}=1000$ s, about 17 min. Rubidium: $10^{-6}/5\times10^{-12}=2\times10^5$ s $=55.6$ h. (d) $1.44\times10^{-7}\times3.00\times10^8\approx43$ m.
5. *Check.* The two offsets differ by 200×, and so do all the outputs (28.8/0.144 = 200). Good.
6. *Answer.* Quartz: 28.8 µs, 0.52°, out of spec in 17 min, so it fails the 8 h case by about 29×. Rubidium: 0.14 µs, 0.0026°, out of spec only after 55.6 h, so it passes with a margin of about 7; 0.14 µs is about 43 m of light travel.

Holdover time, not raw stability, is the number a grid operator buys.

### Exercise C2.4 (writing)

Write a 200-250 word gain argument, in the F1 shape, for Harrowmere Water & Power (fictional) replacing its classical magnetometer survey kit with a quantum magnetometer to find faults in buried power cables. Use only the fictional figures below and say where a real figure would need a source.

Fictional figures: current survey kit 30 pT/√Hz, 1 kHz bandwidth, 1.2 kg; candidate warm vapour-cell kit 80 fT/√Hz, 100 Hz bandwidth, 2.5 kg, needs a 15 W heater; survey analysis bandwidth 25 Hz; fault signatures 0.5-5 nT at the surface.

**Hint:** six slots: classical limit, with a number; quantum mechanism, in one sentence of physics; figure of merit named; quantified gain; maturity and practicality (including SWaP-C); verdict, with one honest caveat. Compute the noise in 25 Hz for both sensors before writing.

**Model paragraph:**
Harrowmere's current survey kit has a noise density of 30 pT/√Hz (fictional), so in a 25 Hz analysis bandwidth it sees about 150 pT rms; the weakest 0.5 nT fault signatures appear at an SNR near 3, too low to separate from ground clutter. A vapour-cell magnetometer measures the field through the precession frequency of optically pumped alkali spins, which is fixed by atomic constants rather than by a coil's calibration. The figure of merit is noise in the survey bandwidth: at 80 fT/√Hz (fictional) the candidate kit gives 0.4 pT rms in 25 Hz, roughly 375 times lower, so the same 0.5 nT signature arrives at an SNR above 1000. Its 100 Hz bandwidth still covers the 25 Hz analysis band, so the gain is not paid for in missed signal. The costs are practical: 2.5 kg against 1.2 kg and a 15 W heater, which shortens battery runs. Vapour-cell magnetometers are a commercial product class (cite a datasheet with date and test conditions before using a real number), but survey use outside magnetic shielding is less mature than laboratory figures suggest. Verdict: worth a field trial on the weakest-signature routes, with the caveat that outdoors the limit will probably be magnetic clutter from traffic and other cables, not the sensor, so the realised gain will be far smaller than 375×.

**What a weak answer misses:**
- Compares densities (30 pT versus 80 fT) without multiplying by √bandwidth, or forgets to check that the new sensor's bandwidth covers the signal.
- States "more sensitive" with no ratio and no SNR for the actual signal size.
- Omits SWaP-C (mass, heater power) and the environment caveat: in the field, ambient magnetic noise (L84) often sets the floor.
- Quotes a real vendor number with no source, date or conditions (F3).

## 6. Cold attempt

Attempt this before reading the sketch. Timebox: 15 minutes.

### Exercise C2.5 (quantitative)

A microwave reference at 6.8 GHz is interrogated with an observed linewidth of 2 Hz. An optical reference at 518 THz has an observed linewidth of 4 Hz. (a) Compute $Q$ for each and the ratio. (b) The microwave clock has $\sigma_y(1\ \mathrm s)=2\times10^{-13}$ and white frequency noise. How long must it average to reach $10^{-15}$? (c) The optical clock has $\sigma_y(1\ \mathrm s)=3\times10^{-16}$. How long to reach $10^{-17}$? (d) Express $10^{-17}$ as "1 second in how many years".

**Hint:** $Q=\nu/\Delta\nu$ (§4.7); $\sigma_y\propto1/\sqrt\tau$ (§4.8); 1 year $=3.156\times10^7$ s (§4.9).

*Do not open the sketch below until you have attempted it.*

**Solution sketch:**
1. *Restate.* Two Q values, two averaging times, one conversion.
2. *Write state.* $\nu_m=6.8\times10^9$ Hz, $\Delta\nu_m=2$ Hz; $\nu_o=5.18\times10^{14}$ Hz, $\Delta\nu_o=4$ Hz.
3. *Name move.* M4 ($Q$), M2 (Allan $1/\sqrt\tau$), M1 (fraction → years).
4. *Algebra.* (a) $Q_m=6.8\times10^9/2=3.4\times10^9$; $Q_o=5.18\times10^{14}/4=1.295\times10^{14}$; ratio $3.81\times10^4$. (b) $\tau=(2\times10^{-13}/10^{-15})^2=4\times10^4$ s $=11.1$ h. (c) $\tau=(3\times10^{-16}/10^{-17})^2=900$ s $=15$ min. (d) $10^{17}/3.156\times10^7=3.17\times10^9$ years.
5. *Check.* The optical line is twice as broad yet its Q is still about $4\times10^4$ higher, because its frequency is about $7.6\times10^4$ times higher.
6. *Answer.* $Q$ ratio $\approx3.8\times10^4$; 11.1 h; 15 min; about 3.2 billion years.

## 7. Confusion log prompts

1. In your own words, why is a 10 fT/√Hz sensor at 1 cm able to beat a 1 fT/√Hz sensor at 4 cm? Write the one line of arithmetic.
2. Which of stability and uncertainty is the "precision" of a clock and which is its "accuracy"? Which one does averaging longer improve, and why does the Allan curve eventually flatten?
3. Eq. 2.2 counts flux quanta. Why does a SQUID nonetheless resolve fields far smaller than one flux quantum per loop area?

## 8. Figures

**Figure 2.1 (`week_2/figures/fig2_1.png`), precision versus accuracy (L45-L53).** Look at where the cluster centre sits (accuracy) and how tight the cluster is (precision), separately. Panel (a) is scattered and off-centre, (b) tight but off-centre, (c) tight and centred. Trap: the text on L40-L43 lists four combinations but the figure draws three; the missing one, low precision with high accuracy, is a wide scatter whose *average* sits on the bullseye. That case matters for sensors, because averaging (M2) fixes it and cannot fix (b). For clocks, read the cluster spread as stability and the centre offset as uncertainty (§4.8).

**Figure 2.2 (`week_2/figures/fig2_2.png`), sensitivity versus resolution (L76-L82).** Both axes are logarithmic: sensitivity in T/Hz$^{1/2}$ from $10^{-20}$ to $10^{0}$ (lower is better), resolution in metres from $10^{-8}$ to about $10^{-1.5}$ (smaller is finer). Look at the dashed line: points below it are labelled quantum, above it classical. The trend runs from NV centres and MFM at top left (nm resolution, $10^{-5}$ to $10^{-8}$ T/√Hz) to SQUIDs and OPMs at bottom right (mm-cm resolution, about $10^{-15}$ T/√Hz), with BEC microscopes (red dots) at µm resolution near $10^{-10}$ to $10^{-11}$. Traps: (i) "sensitivity" on this axis is a noise density, so lower is better, the reverse of everyday usage; (ii) the dashed line is a drawn guide, not a physical law, and the hand-drawn split between "classical" and "quantum" is the authors'; (iii) the NV points span three decades, which is the source of the L82 versus L137 inconsistency (§4.10); (iv) no bandwidth or standoff is shown, so a point low on this plot can still lose in practice (§4.3, Exercise C2.1).

**Figure 2.3 (`week_2/figures/fig2_3.png`), BEC magnetic microscope render (L141-L149).** Look at the gold chip with a transparent sample carrying random wires, the cold-atom cloud (white streak) just above it, the probe laser grazing the surface and reflecting to the camera, and the false-colour inset at the top. The inset is an atom-density image: red blobs are where local field minima from the sample's currents pull atoms together, so the cloud's *shape* is the field map. What it shows: imaging the deformed elongated BEC gives a 1D field profile; scanning gives 2D (L141). Trap: this is a render, not data, and the scale is not given; the lecture's numbers for it are about 100 nm resolution with about 2 nT field resolution (L149), and its imaging rate is limited by the time to make and move each BEC, so its bandwidth is low.
