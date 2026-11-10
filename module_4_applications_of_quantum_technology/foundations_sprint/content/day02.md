# Day 02: What Makes a Good Sensor

**Time:** ~3 h · **Feeds:** Week 2 lecture §2.1-2.2 (plus L94 in §2.3), inventory row W2 Consolidate (sensitivity, bandwidth, dynamic range, practicality) · **Companion:** `companions/week02_companion.md` §1-3

**Cadence (180 min):** 15 min retrieval (§Spaced review) · 55 min moves M2 and M3 (§Core concepts) · 50 min quantitative drills (Exercises 2.1-2.7) · 45 min writing on the running case (Exercises 2.8-2.9) · 15 min companion pointer and confusion log.

## Why this matters

Every Week 2 Consolidate answer, and later the Week 3 and Week 7 ones, has to say *how much* better a quantum sensor is. The inventory row for Week 2 Consolidate names the yardsticks: sensitivity, bandwidth, dynamic range and practicality. The lecture introduces them in two pages (§2.1-2.2) and then quotes numbers such as "$1\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$" and "bandwidths of less than 200 Hz" without explaining how to use them.

Today you learn to read and combine those numbers. That means three things:

- the vocabulary of a sensor datasheet (precision, accuracy, resolution, bandwidth, dynamic range, SWaP-C);
- **M2**, the noise-density rule $\delta x = S\sqrt{\Delta f}$ and its time form, $1/\sqrt{t}$ averaging, and Allan deviation;
- **M3**, the two counting limits (shot noise $1/\sqrt{N}$, Heisenberg $1/N$), signal-to-noise ratio, and the distance gain the lecture states incorrectly at L94.

You already know most of this as an engineer. You have read a latency histogram, watched a moving average hide a spike, and noticed that a p99 estimate settles down as the sample count grows. Today puts physics units on those instincts. The analogies are there to help you remember; the physics statements stand on their own.

## Core concepts

### Move M2.1: Precision, accuracy and resolution

**Idea.** The lecture (§2.1, L36-45) separates two qualities that everyday English blurs:

- **Precision** is how much the readings scatter when the true value is fixed. You measure it as the standard deviation of repeated readings. Low scatter means high precision.
- **Accuracy** is how close the readings are, on average, to the true value. You measure it as the bias: mean reading minus reference value.

A sensor can be precise but biased (the tight cluster off the bullseye in the lecture's Figure 2.1), or unbiased but noisy. The two fixes are different. **Calibration** against a reference removes bias. Only **averaging** reduces scatter, and averaging costs time, which means bandwidth (Move M2.2). The lecture says the same at L36: processing can beat the random variation, "however, this processing would limit the response of the sensor to fast changes".

**Resolution** has two meanings, and the lecture uses the second:

1. *Readout resolution:* the smallest change the instrument can register, often one least-significant bit (LSB) of its analogue-to-digital converter (ADC).
2. *Spatial resolution:* how close two sources can be and still be told apart. In §2.2 (L76) and Figure 2.2 this is set by sensor size, which limits pixel spacing in an array. Bigger sensors are usually more sensitive but give coarser images.

**Engineer's bridge.** Two servers' clocks report request timestamps. One is consistently 40 ms fast but has 1 ms jitter: precise, inaccurate. The other is centred on true time but jitters by 30 ms: accurate, imprecise. NTP-style offset correction fixes the first. Only averaging many samples helps the second.

**Worked clone.** A reference field is $10.00\,\mu\mathrm{T}$. Sensor X reads 10.21, 10.19, 10.20 $\mu$T: bias $+0.20\,\mu$T, scatter about $0.01\,\mu$T. Sensor X is precise but biased by $0.20\,\mu$T; one calibration offset of $-0.20\,\mu$T makes it both precise and accurate.

**You've got it when** you can look at a set of readings and a reference, name which quality is poor, and say whether calibration or averaging is the fix.

### Move M2.2: Bandwidth, the −3 dB point, and dynamic range

**Bandwidth.** The lecture (L47) defines it as the signal frequency at which the sensor's response falls by a factor $1/\sqrt{2}$. Three facts make this usable:

- $1/\sqrt{2} \approx 0.707$ of the **amplitude** is $1/2$ of the **power**, because power goes as amplitude squared.
- In decibels, $20\log_{10}(1/\sqrt{2}) = -3.01\,\mathrm{dB}$. That is why the bandwidth is also called the "−3 dB point" or cut-off frequency $f_c$.
- Many sensors behave roughly like a first-order low-pass filter (judgement: a common model, not true of every sensor). Its amplitude response is

$$|H(f)| = \frac{1}{\sqrt{1 + (f/f_c)^2}},$$

which equals $1/\sqrt{2}$ exactly at $f = f_c$ and falls further above it.

The rule from L47: choose a sensor whose bandwidth is **above** the fastest change you care about.

**Worked clone.** A sensor has $f_c = 20\,\mathrm{Hz}$ and the signal varies at $10\,\mathrm{Hz}$. Then $|H| = 1/\sqrt{1 + 0.5^2} = 0.894$: the sensor shows about 89% of the true amplitude.

**Dynamic range.** This is the span of signal amplitudes the sensor can record (L47). Above the top of the range the output saturates and is meaningless. Below the bottom, the signal sinks into the noise. A useful number is full scale divided by noise floor, often given in decibels as $20\log_{10}(\text{ratio})$ for amplitudes.

**Worked clone.** Full scale $1\,\mathrm{mT}$, noise floor $1\,\mathrm{nT}$: ratio $10^{6}$, which is $120\,\mathrm{dB}$.

**Why dynamic range bites in magnetometry.** The background is huge. The Earth's field is tens of $\mu$T (lecture Table 2.1), while the signals of interest can be pT or fT. The most sensitive schemes, such as SERF optically pumped magnetometers, work only near zero field, so they need shielding or active field cancellation (Budker & Romalis, arXiv physics/0611246). A sensor can have superb sensitivity and still be useless outdoors because it saturates.

**SWaP-C.** This stands for size, weight, power and cost. The lecture lists mass, volume, power, reliability and cost per sensor at L55. It is the practicality clause of every F1 argument (part 5). A cryogenic sensor and a palm-sized one can have similar noise yet be different products.

**Engineer's bridge.** Bandwidth is your dashboard's smoothing window: a 5-minute moving average cannot show a 10-second spike. Dynamic range is your histogram's bucket range plus integer width: values beyond the top bucket all look the same, and differences below one bucket vanish.

**You've got it when** you can convert between "−3 dB", "$1/\sqrt{2}$ amplitude" and "half power" without thinking, and can say for a stated signal whether bandwidth, dynamic range or noise is the binding limit.

### Move M2.3: Noise spectral density, $\delta x = S\sqrt{\Delta f}$, and $1/\sqrt{t}$ averaging

**Idea.** The lecture (L74) says the precision of a magnetometer is quoted as a noise spectral density, "with units of $T\sqrt{\mathrm{Hz}}$".

> **Lecture erratum (L74, inventory W2).** The unit is $\mathrm{T}/\sqrt{\mathrm{Hz}}$ (tesla **per** root hertz), not $\mathrm{T}\sqrt{\mathrm{Hz}}$. The lecture's own Figure 2.2 description (L82) and its later sensitivities (L119, L127, L137) use the correct form.

Why "per root hertz"? For white noise, the noise *power* is spread evenly over frequency. If you let a band $\Delta f$ through, the power you collect grows as $\Delta f$, so the root-mean-square (rms) noise amplitude grows as $\sqrt{\Delta f}$. Hence:

$$\delta x = S\sqrt{\Delta f},$$

where $S$ is the amplitude noise density (here in $\mathrm{T}/\sqrt{\mathrm{Hz}}$) and $\delta x$ is the rms noise in tesla. The spec writes this as $\delta x = S\sqrt{B}$; here **$\Delta f$** stands for bandwidth so that $B$ can stay the magnetic field.

**Unit check.** $[\mathrm{T}/\sqrt{\mathrm{Hz}}]\times[\sqrt{\mathrm{Hz}}] = [\mathrm{T}]$. With the lecture's typo you would get $\mathrm{T}\cdot\mathrm{Hz}$, which is not a field. Doing this unit check every time is the cheapest error detector in the module.

**Time form.** Averaging for a time $\tau$ is a low-pass filter with bandwidth of order $1/\tau$. A common convention is $\Delta f \approx 1/(2\tau)$ (judgement: some authors drop the 2; the scaling is what matters). So for white noise

$$\delta x(\tau) \approx \frac{S}{\sqrt{2\tau}} \propto \frac{1}{\sqrt{\tau}}.$$

Four times longer averaging halves the noise; a hundred times longer cuts it by ten. Quantum sensing reviews state sensitivity the same way, as the smallest signal detectable in unit time, scaling as $1/\sqrt{\text{time}}$ (Degen, Reinhard & Cappellaro, arXiv 1611.02427).

**Worked clone.** A sensor has $S = 200\,\mathrm{pT}/\sqrt{\mathrm{Hz}}$ and you use $\Delta f = 25\,\mathrm{Hz}$. The rms noise is $200 \times \sqrt{25} = 1000\,\mathrm{pT} = 1\,\mathrm{nT}$.

**Engineer's bridge.** This is the standard error of the mean, $\sigma/\sqrt{n}$. Your p50 latency estimate from 10,000 requests is ten times steadier than from 100. "Per root hertz" is the noise you would get after one second's worth of averaging, written so it can be rescaled to any window.

**You've got it when** you can turn a quoted $\mathrm{T}/\sqrt{\mathrm{Hz}}$ figure and a bandwidth into a noise in tesla, and say how long you must average to reach a target noise.

### Move M2.4: Allan deviation, stability versus averaging time

**Idea.** $1/\sqrt{\tau}$ averaging works only while the noise is white (uncorrelated from one sample to the next). Real instruments also drift: temperature, ageing, slow systematic effects. The **Allan deviation** $\sigma_y(\tau)$ shows how far averaging gets you before drift takes over. The lecture points to this at L155, where it says stability "is often given as a function of an averaging time". It is the standard plot for clocks (Ludlow et al., arXiv 1407.3493, use it throughout) and is used for magnetometers and accelerometers too.

**Definition, in words.** Cut the record of fractional frequency $y$ (or of any measured quantity) into consecutive windows of length $\tau$. Average each window. Take the differences between neighbouring window averages. Then

$$\sigma_y^2(\tau) = \tfrac12\left\langle(\bar y_{k+1} - \bar y_k)^2\right\rangle.$$

Repeat for many $\tau$ and plot $\sigma_y$ against $\tau$ on log-log axes.

**How to read the plot** (judgement: standard time-and-frequency practice; slopes are on log-log axes):

| Slope of $\sigma_y(\tau)$ | Dominant noise | What averaging does |
|---|---|---|
| $-1/2$ | white frequency noise (the $1/\sqrt{\tau}$ regime of Move M2.3) | helps: 100× longer gives 10× better |
| $0$ (flat floor) | flicker noise | stops helping; this is the best stability the device reaches |
| $+1/2$ or steeper | random walk and drift | makes things worse |

So you read three things off any Allan plot: the value at a short reference time (often $\tau = 1\,\mathrm{s}$), the $-1/2$ slope region, and the height and position of the floor. A one-number claim such as "stability $10^{-13}$" is incomplete without the $\tau$ at which it holds.

**Worked clone.** A clock shows $\sigma_y(1\,\mathrm{s}) = 2\times10^{-11}$ with a $-1/2$ slope. At $\tau = 100\,\mathrm{s}$: $2\times10^{-11}/\sqrt{100} = 2\times10^{-12}$, provided the floor has not been reached yet.

**Engineer's bridge.** Compute the mean latency for every 1-minute window, then the spread of differences between consecutive windows. Repeat with 10-minute and 1-hour windows. At first the spread shrinks like $1/\sqrt{\text{window}}$. Then diurnal load and deploys start to dominate, and longer windows stop helping. That turning point is the flicker floor.

**You've got it when** you can take $\sigma_y$ at one $\tau$ and the slope, predict $\sigma_y$ at another $\tau$, find where a given floor is reached, and say why a stability figure without $\tau$ cannot be compared.

### Move M3.1: Shot noise $1/\sqrt{N}$ versus the Heisenberg limit $1/N$

**Idea.** A quantum sensor reads out a phase (or a population) by measuring $N$ particles: atoms, photons or spins. If the particles are **independent**, each measurement is a coin flip with outcome probabilities set by the phase (Module 3: the Born rule). The statistical error of an average of $N$ independent coin flips falls as $1/\sqrt{N}$. For phase estimation this gives

$$\delta\phi_{\mathrm{SQL}} = \frac{1}{\sqrt{N}}\ \mathrm{rad},$$

the **standard quantum limit** (SQL), also called shot noise or projection noise.

If the $N$ particles are **entangled** in a suitable state, the phase they pick up adds coherently, and the limit becomes

$$\delta\phi_{\mathrm{HL}} = \frac{1}{N}\ \mathrm{rad},$$

the **Heisenberg limit**. The gain over the SQL is a factor $\sqrt{N}$ (Degen et al., arXiv 1611.02427, which discusses both limits). In practice, entangled states are fragile, and decoherence usually eats much of that gain (judgement). Most fielded quantum sensors today work at or above the SQL. Their advantage comes from other things: an absolute atomic reference, low intrinsic noise, or the ability to get close to the source.

**Repetition.** Repeating the measurement $n$ times is another $1/\sqrt{n}$, which is just Move M2.3 again: total independent samples $N n$ give $1/\sqrt{Nn}$.

**Worked clone.** $N = 10^4$ atoms: SQL $= 10^{-2}$ rad; Heisenberg $= 10^{-4}$ rad; ratio $\sqrt{10^4} = 100$.

**Engineer's bridge.** You estimate an error rate from $N$ independent requests. The uncertainty falls as $1/\sqrt{N}$, which is why 4× the traffic gives only 2× the confidence. The Heisenberg limit has **no** classical analogue: it needs correlations that independent samples cannot have. Do not stretch the analogy there.

**You've got it when** you can say how many particles (or repeats) buy a 10× improvement at the SQL (100×) and at the Heisenberg limit (10×).

### Move M3.2: Signal-to-noise ratio and the distance gain (lecture L94 corrected)

**SNR.** Signal-to-noise ratio is signal amplitude divided by rms noise in the same bandwidth: $\mathrm{SNR} = B_{\mathrm{signal}}/\delta B$. In decibels for amplitudes, $20\log_{10}\mathrm{SNR}$. An SNR of 1 means the signal is as big as the noise. A common detection rule of thumb is SNR ≥ 3 to 5 (judgement).

There are two ways to raise SNR. You can lower the noise: a better $S$, a narrower $\Delta f$, longer averaging, more particles. Or you can raise the signal, and often the cheapest way to do that is to **get closer**.

**Distance gain.** The lecture models active brain regions as current dipoles whose field falls as $B \propto 1/r^2$ (Eq. 2.1, L92). Then at L94 it says the signal amplitude "increases by $r^2$".

> **Lecture erratum (L94, inventory W2).** With $B \propto 1/r^2$, moving the sensor from $r_1$ to a closer $r_2$ multiplies the signal by
> $$\frac{B(r_2)}{B(r_1)} = \left(\frac{r_1}{r_2}\right)^2.$$
> Halve the distance and you get 4× the signal. Sensor noise is unchanged (as L94 rightly says), so SNR also rises 4×. It is the *ratio* of distances that is squared, not "$r^2$".

**The exponent depends on the source geometry** (judgement: standard magnetostatics, beyond the lecture): about $1/r$ for a long straight current such as a cable, $1/r^2$ for the lecture's current-dipole model, $1/r^3$ for a small magnetised object (a magnetic dipole). Use the right one for your source, or the distance gain will be badly over- or understated.

**Worked clone.** Current-dipole source, sensor moved from 40 mm to 10 mm: gain $(40/10)^2 = 16$.

**Combining.** A noisier sensor that can sit closer can win. The SNR ratio of sensor 2 over sensor 1 is (signal gain) × ($S_1/S_2$). This is the quantitative core of why standoff appears next to sensitivity in every magnetometer comparison (Day 03).

**You've got it when** you can compare two sensors with different noise densities and standoffs, for a stated field law, and say which gives the higher SNR and by what factor.

## Exercises

Attempt each one cold for at least five minutes before opening the hint. Exercises 2.1-2.7 are quantitative (about 50 min; 2.7(b) is stretch). Exercises 2.8-2.9 are writing on the running case (about 45 min). All Harrowmere Water & Power figures are invented for practice and labelled (fictional).

### Exercise 2.1 (quantitative)

A reference coil produces a field of exactly $20.00\,\mu\mathrm{T}$. Sensor P reads 20.41, 20.39, 20.40, 20.42, 20.38 $\mu$T. Sensor Q reads 19.7, 20.3, 20.1, 19.8, 20.2 $\mu$T. (a) Find each sensor's bias and sample standard deviation. (b) Which is more precise and which more accurate? (c) How many readings must Q average for the standard deviation of its mean to match a single reading of P?

**Hint:** Bias = mean − reference. Sample standard deviation uses $n-1$. The standard deviation of a mean of $n$ readings is $\sigma/\sqrt{n}$.

**Solution sketch:**
- *Restate:* separate scatter (precision) from offset (accuracy), then use $1/\sqrt{n}$ averaging.
- *Write state:* P: mean $20.40$, deviations $+0.01, -0.01, 0, +0.02, -0.02$. Q: mean $20.02$, deviations $-0.32, +0.28, +0.08, -0.22, +0.18$.
- *Name move:* M2.1 (precision vs accuracy), M2.3 ($1/\sqrt{n}$).
- *Algebra:* P: bias $+0.40\,\mu$T; $\sigma_P = \sqrt{0.0010/4} = 0.0158\,\mu$T. Q: bias $+0.02\,\mu$T; $\sigma_Q = \sqrt{0.268/4} = 0.259\,\mu$T. For (c): $\sigma_Q/\sqrt{n} = \sigma_P$ gives $n = (\sigma_Q/\sigma_P)^2 = (0.259/0.0158)^2 = 268$.
- *Check:* P's spread is visibly tiny and its offset obvious; Q straddles the true value. A ratio of about 16 in $\sigma$ means about $16^2$ readings.
- *Answer:* (a) P: bias $+0.40\,\mu$T, $\sigma = 0.016\,\mu$T; Q: bias $+0.02\,\mu$T, $\sigma = 0.26\,\mu$T. (b) P is more precise, Q is more accurate. (c) About 268 readings. Calibrating P (subtract $0.40\,\mu$T) is far cheaper than averaging Q 268 times, provided the bias is stable.

### Exercise 2.2 (quantitative)

A magnetometer behaves as a first-order low-pass filter with a −3 dB bandwidth of $f_c = 100\,\mathrm{Hz}$. It is used to watch a cable carrying 50 Hz current, which also has a third-harmonic component at 150 Hz. (a) What fraction of the true amplitude does the sensor report at 50 Hz and at 150 Hz? (b) Express the 150 Hz response in dB. (c) Confirm that the response at $f_c$ is −3 dB.

**Hint:** $|H(f)| = 1/\sqrt{1 + (f/f_c)^2}$, and dB $= 20\log_{10}|H|$ for amplitude.

**Solution sketch:**
- *Restate:* evaluate the low-pass response at two frequencies and at the cut-off.
- *Write state:* $f/f_c = 0.5$ and $1.5$.
- *Name move:* M2.2 (bandwidth, −3 dB).
- *Algebra:* at 50 Hz, $|H| = 1/\sqrt{1.25} = 0.894$. At 150 Hz, $|H| = 1/\sqrt{3.25} = 0.555$, which is $20\log_{10}0.555 = -5.1\,\mathrm{dB}$. At $f_c$, $|H| = 1/\sqrt{2} = 0.707$, which is $-3.01\,\mathrm{dB}$.
- *Check:* the response falls monotonically above $f_c$, and 0.555 < 0.707 < 0.894. ✓
- *Answer:* (a) 89% at 50 Hz, 55% at 150 Hz. (b) about −5.1 dB. (c) −3.0 dB. The harmonic is under-reported by nearly half, so this sensor distorts the waveform even though 150 Hz looks "close" to its bandwidth. Choose $f_c$ well above the highest frequency you need.

### Exercise 2.3 (quantitative)

A sensor has a white noise density of $S = 30\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$. (a) What is the rms noise in a 40 Hz bandwidth? (b) You want to see a steady $50\,\mathrm{fT}$ signal with SNR = 5. What bandwidth is allowed, and roughly how long must you average (use $\Delta f \approx 1/(2\tau)$)? (c) A colleague writes the density as "$30\,\mathrm{fT}\sqrt{\mathrm{Hz}}$", copying the lecture's L74. What goes wrong with the units in (a)?

**Hint:** $\delta B = S\sqrt{\Delta f}$. For (b), first find the noise you can tolerate, $\delta B = 50/5$.

**Solution sketch:**
- *Restate:* convert a density into an rms noise, then invert for bandwidth and time.
- *Write state:* $S = 30\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$; $\Delta f = 40\,\mathrm{Hz}$; target $\delta B = 10\,\mathrm{fT}$.
- *Name move:* M2.3 (noise density, $1/\sqrt{\tau}$), M3.2 (SNR).
- *Algebra:* (a) $\delta B = 30\sqrt{40} = 190\,\mathrm{fT}$. (b) $\Delta f = (\delta B/S)^2 = (10/30)^2 = 0.111\,\mathrm{Hz}$, so $\tau \approx 1/(2\times0.111) = 4.5\,\mathrm{s}$. (c) $\mathrm{fT}\sqrt{\mathrm{Hz}}\times\sqrt{\mathrm{Hz}} = \mathrm{fT\cdot Hz}$, which is not a field.
- *Check:* in (a) the noise exceeds the 50 fT signal (SNR about 0.26), so narrowing the band is necessary. In (b), 0.111 Hz is far below 40 Hz, so the factor of 19 in noise needs a factor of about 360 in bandwidth, consistent with the square law.
- *Answer:* (a) $\approx 190\,\mathrm{fT}$ rms. (b) $\Delta f \le 0.11\,\mathrm{Hz}$, about 4.5 s of averaging, provided the signal is steady and the noise stays white that long. (c) the typo gives tesla-hertz; the correct unit is $\mathrm{T}/\sqrt{\mathrm{Hz}}$.

### Exercise 2.4 (quantitative)

A digital magnetometer has a range of $\pm100\,\mu\mathrm{T}$ digitised by a 24-bit ADC, and a noise density of $50\,\mathrm{pT}/\sqrt{\mathrm{Hz}}$. You use it in a 10 Hz bandwidth. (a) What is one LSB in tesla? (b) What is the rms noise? (c) Which limits the smallest detectable change, the ADC or the noise? (d) What is the dynamic range, full span over rms noise, as a ratio and in dB?

**Hint:** One LSB = span / $2^{24}$, where the span is 200 $\mu$T. Dynamic range in dB $= 20\log_{10}$ of the amplitude ratio.

**Solution sketch:**
- *Restate:* compare readout resolution with the noise floor; then compute the span-to-noise ratio.
- *Write state:* span $= 2\times10^{-4}\,\mathrm{T}$; $2^{24} = 16\,777\,216$; $S = 5\times10^{-11}\,\mathrm{T}/\sqrt{\mathrm{Hz}}$; $\Delta f = 10\,\mathrm{Hz}$.
- *Name move:* M2.1 (readout resolution), M2.2 (dynamic range), M2.3 ($S\sqrt{\Delta f}$).
- *Algebra:* (a) LSB $= 2\times10^{-4}/16\,777\,216 = 1.19\times10^{-11}\,\mathrm{T} = 11.9\,\mathrm{pT}$. (b) $\delta B = 50\sqrt{10} = 158\,\mathrm{pT}$. (d) $2\times10^{-4}/1.58\times10^{-10} = 1.26\times10^{6}$, and $20\log_{10}(1.26\times10^{6}) = 122\,\mathrm{dB}$.
- *Check:* the noise is about 13 LSB, so the ADC is fine-grained enough. A rule of thumb is that the LSB should sit below the noise (judgement).
- *Answer:* (a) 11.9 pT. (b) 158 pT rms. (c) The noise limits, not the ADC. (d) about $1.3\times10^{6}$, or 122 dB.

### Exercise 2.5 (quantitative)

A (fictional) timing reference has this Allan deviation: $\sigma_y = 4\times10^{-12}$ at $\tau = 1\,\mathrm{s}$, falling with slope $-1/2$, until it meets a flat floor at $6\times10^{-14}$. (a) What is $\sigma_y$ at 100 s? (b) How long must you average to reach $1\times10^{-13}$? (c) At what $\tau$ does the floor begin? (d) Does averaging for one day reach $10^{-14}$?

**Hint:** In the $-1/2$ region, $\sigma_y(\tau) = \sigma_y(1\,\mathrm{s})/\sqrt{\tau/1\,\mathrm{s}}$. Invert for $\tau$: $\tau = (\sigma_y(1\,\mathrm{s})/\sigma_{\text{target}})^2$ seconds.

**Solution sketch:**
- *Restate:* read and extrapolate an Allan plot.
- *Write state:* $\sigma_1 = 4\times10^{-12}$; slope $-1/2$; floor $6\times10^{-14}$.
- *Name move:* M2.4 (Allan deviation).
- *Algebra:* (a) $4\times10^{-12}/\sqrt{100} = 4\times10^{-13}$. (b) $(4\times10^{-12}/10^{-13})^2 = 40^2 = 1600\,\mathrm{s}$. (c) $(4\times10^{-12}/6\times10^{-14})^2 = 66.7^2 \approx 4400\,\mathrm{s}$, about 1.2 h. (d) No. Beyond about 4400 s the curve is flat at $6\times10^{-14}$, so no amount of averaging reaches $10^{-14}$.
- *Check:* $1\times10^{-13}$ is above the floor, so (b) is reachable, and 1600 s < 4400 s. ✓
- *Answer:* (a) $4\times10^{-13}$. (b) 1600 s (about 27 min). (c) about 4400 s. (d) No: the flicker floor sets a hard limit of $6\times10^{-14}$. To do better you need a better device, not more patience.

### Exercise 2.6 (quantitative)

An atom-based sensor reads out a phase using $N = 2.5\times10^{5}$ atoms per cycle. (a) What is the phase uncertainty per cycle at the SQL and at the Heisenberg limit? (b) What is the ratio? (c) At the SQL, how many atoms per cycle would give a 10× improvement? (d) If the atom number cannot grow, how many cycles must be averaged for the same 10× improvement?

**Hint:** $\delta\phi_{\mathrm{SQL}} = 1/\sqrt{N}$, $\delta\phi_{\mathrm{HL}} = 1/N$; repeats add as more independent samples.

**Solution sketch:**
- *Restate:* compare the two counting limits, then trade atoms for repeats.
- *Write state:* $N = 2.5\times10^{5}$, $\sqrt{N} = 500$.
- *Name move:* M3.1 (shot noise vs Heisenberg), M2.3 ($1/\sqrt{n}$).
- *Algebra:* (a) SQL: $1/500 = 2\times10^{-3}$ rad. Heisenberg: $1/(2.5\times10^{5}) = 4\times10^{-6}$ rad. (b) ratio $= \sqrt{N} = 500$. (c) 10× better at the SQL needs $10^2 = 100$ times more atoms: $2.5\times10^{7}$. (d) 100 cycles.
- *Check:* $500\times4\times10^{-6} = 2\times10^{-3}$. ✓
- *Answer:* (a) 2 mrad (SQL) and 4 µrad (Heisenberg). (b) 500. (c) $2.5\times10^{7}$ atoms. (d) 100 cycles, which costs 100× the measurement time and so 100× less bandwidth.

### Exercise 2.7 (quantitative)

(a) A test rig contains a small source that behaves as a current dipole ($B \propto 1/r^2$). Sensor A has $15\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$ but must sit 50 mm from the source. Sensor B has $45\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$ but can sit at 20 mm. In the same bandwidth, which gives the higher SNR, and by what factor?

(b) **(stretch)** A long straight buried cable carries a (fictional) unbalanced current of 2 A. Its field is $B = \mu_0 I/(2\pi r) = 2\times10^{-7}\,I/r$ (in tesla, with $I$ in amperes and $r$ in metres). Compare the field at $r = 1.2\,\mathrm{m}$ and at $r = 2.1\,\mathrm{m}$. What gain would you wrongly claim by using the lecture's $1/r^2$ law here?

**Hint:** SNR ratio = signal gain × $(S_A/S_B)$. The distance ratio is squared only for $1/r^2$; for a line current it enters to the first power.

**Solution sketch:**
- *Restate:* combine distance gain with noise-density ratio; then apply the correct field law for a line current.
- *Write state:* (a) $r_A/r_B = 50/20 = 2.5$; $S_A/S_B = 15/45 = 1/3$. (b) $I = 2\,\mathrm{A}$, $r = 1.2$ and $2.1\,\mathrm{m}$.
- *Name move:* M3.2 (SNR and distance gain, lecture L94 corrected).
- *Algebra:* (a) signal gain for B $= 2.5^2 = 6.25$; SNR ratio $= 6.25\times\tfrac13 = 2.08$. (b) $B(1.2) = 2\times10^{-7}\times2/1.2 = 3.33\times10^{-7}\,\mathrm{T} = 333\,\mathrm{nT}$; $B(2.1) = 1.90\times10^{-7}\,\mathrm{T} = 190\,\mathrm{nT}$; ratio $2.1/1.2 = 1.75$. The $1/r^2$ law would wrongly claim $1.75^2 = 3.06$.
- *Check:* in (a), B's noise is 3× worse but its signal is 6.25× bigger, so B should win by about 2. In (b), the fields are hundreds of nT, far above fT-level noise, so for this cable, sensitivity is not the binding constraint.
- *Answer:* (a) Sensor B, by a factor of about 2.1 in SNR. (b) 333 nT versus 190 nT, a 1.75× gain. Using $1/r^2$ would overstate the gain at 3.06×. Note that for a line current, 2.5× closer would give only 2.5×, and sensor A would win at $2.5/3 = 0.83$.

### Exercise 2.8 (writing)

Harrowmere Water & Power is assessing a vehicle-towed magnetic survey to find sheath faults on its buried 11 kV cables. All figures are fictional: about 1,400 km of cable; burial depth 1.0-2.0 m; a typical fault causes a 0.5 A unbalanced 50 Hz current; the sensor rides just above the ground, so design for the deepest cable, about 2 m away; Earth's field on site is 50 µT; at survey speed the van passes over a fault in about a second. Write a 150-200-word **requirements paragraph** (F1 parts 1, 3 and 4 only) stating the figures of merit a sensor must meet, with numbers, and whether a quantum magnetometer is needed.

**Hint:** Work out the signal ($2\times10^{-7}\,I/r$). Then keep two bandwidths apart. The *sensor* bandwidth must pass the 50 Hz carrier and a harmonic. The *detection* (noise) bandwidth is different: the fault is a 50 Hz tone, picked out with a lock-in amplifier whose bandwidth, about 1 Hz, is set by how quickly the van passes the fault. Find the noise density needed to resolve, say, 1% of the signal in the detection bandwidth ($S = \delta B/\sqrt{\Delta f}$), and the dynamic range by Move M2.2's definition (full scale over noise floor). Then compare with the classical fluxgate level in the lecture's Figure 2.2 description (L82, about $10^{-10}\,\mathrm{T}/\sqrt{\mathrm{Hz}}$).

**Model paragraph:** For Harrowmere's cable survey (all figures fictional), the classical baseline is a fluxgate at roughly $10^{-10}\,\mathrm{T}/\sqrt{\mathrm{Hz}}$ (Week 2 lecture, Figure 2.2). A 0.5 A fault current seen from 2 m produces $2\times10^{-7}\times0.5/2 = 50\,\mathrm{nT}$, falling as $1/r$ for a line current, not $1/r^2$. Two bandwidths matter. The sensor's −3 dB bandwidth must be at least about 200 Hz to pass the 50 Hz carrier and its 150 Hz harmonic. But the figure of merit is noise in the detection bandwidth: the fault is a 50 Hz tone, picked out by a lock-in whose bandwidth, about 1 Hz, is set by how fast the van passes the fault. Resolving 1% of the signal (0.5 nT) in 1 Hz needs $S \le 0.5\,\mathrm{nT}/\sqrt{\mathrm{Hz}}$. The sensor must also sit in the 50 µT background without saturating: full scale over noise floor is $50\,\mu\mathrm{T}/0.5\,\mathrm{nT} = 10^{5}$, or 100 dB. The fluxgate already beats the noise requirement about five times over, so the quantified gain from a femtotesla-class quantum sensor is nil here, and its near-zero-field operation counts against it. A quantum sensor matters only if the requirement tightens by orders of magnitude, for example to find much smaller fault currents.

**What a weak answer misses:** It quotes a sensor's fT/√Hz figure without converting it to noise in the actual bandwidth. It treats the 200 Hz sensor bandwidth as the noise bandwidth, which overstates the noise requirement by $\sqrt{200} \approx 14$; a lock-in at 50 Hz needs only about 1 Hz. It uses $1/r^2$ for a cable. It computes dynamic range as background over signal instead of full scale over noise floor, and ignores the 50 µT background that rules out the most sensitive near-zero-field schemes. And it assumes "quantum" is needed, when the numbers show a fluxgate already meets the requirement, so the honest verdict is "probably not, unless the requirement tightens".

### Exercise 2.9 (writing)

Harrowmere's control engineers (fictional figures) need substation clocks to stay within ±1 µs of UTC for 8 h if satellite timing is lost (holdover). A vendor datasheet says only "stability $5\times10^{-13}$". Write a 150-200-word note to Harrowmere's (non-specialist) board explaining (i) what fractional frequency the requirement implies, (ii) why the vendor figure cannot yet be judged, and (iii) what to ask for. Use F3 (credible numbers).

**Hint:** A constant fractional frequency offset $y$ gives a time error $y\,t$ after time $t$ (judgement: this ignores drift and noise). So $y \le 10^{-6}\,\mathrm{s}/28\,800\,\mathrm{s}$. Stability without $\tau$ is not a number you can compare (Move M2.4). Stability is not accuracy (Move M2.1; the lecture's "uncertainty", L157).

**Model paragraph:** Harrowmere's holdover target (fictional) is ±1 µs over 8 h, which is 28,800 s. A clock whose rate is off by a fixed fraction $y$ gains $y$ seconds every second. So the target needs $y \le 10^{-6}/28\,800 \approx 3.5\times10^{-11}$, averaged over the whole outage. The vendor's "stability $5\times10^{-13}$" cannot be judged yet, for three reasons. First, stability is quoted as an Allan deviation, and it changes with averaging time: a clock can reach $5\times10^{-13}$ at 1,000 s and drift far worse at 8 h. Second, stability says how steadily the clock ticks, not whether it ticks at the right rate. A steady but offset clock (poor accuracy) fails the holdover just as surely. Third, the conditions are missing: temperature range, warm-up time and ageing. We should ask for the full Allan deviation plot from 1 s to at least $10^{5}$ s, the frequency accuracy (offset) after calibration and its drift per day, and the test conditions, preferably from an independent or metrology-institute measurement rather than the datasheet alone. As a rough check, a clock holding $\sigma_y = 10^{-12}$ at $\tau = 8\,\mathrm{h}$ would wander by about $10^{-12}\times28\,800 \approx 29\,\mathrm{ns}$ (judgement: order of magnitude only), comfortably inside 1 µs.

**What a weak answer misses:** It compares $5\times10^{-13}$ directly with $3.5\times10^{-11}$ and declares victory, ignoring that the figure has no $\tau$ and is a stability, not an offset. It forgets drift and temperature. It never converts the 1 µs requirement into a fractional frequency. And it treats the datasheet as top-tier evidence, when F3 ranks a vendor datasheet below a peer-reviewed or metrology-institute measurement.

## Anti-patterns / Common mistakes

- **Quoting T/√Hz as if it were a field.** *How you'd notice:* you compare "$10\,\mathrm{fT}/\sqrt{\mathrm{Hz}}$" directly with a "$50\,\mathrm{fT}$" signal. *Instead:* multiply by $\sqrt{\Delta f}$ first; only tesla can be compared with tesla.
- **Copying the lecture's "T√Hz" (L74).** *How you'd notice:* your noise comes out in T·Hz. *Instead:* write $\mathrm{T}/\sqrt{\mathrm{Hz}}$ and do the unit check.
- **Reading L94 as "signal grows by $r^2$".** *How you'd notice:* your gain depends on the absolute distance rather than on a ratio. *Instead:* gain $= (r_1/r_2)^n$, with $n$ set by the source (1 line current, 2 current dipole, 3 magnetic dipole).
- **Confusing precision with accuracy, or stability with uncertainty.** *How you'd notice:* you propose averaging to remove a bias. *Instead:* calibration fixes bias; averaging fixes scatter.
- **Averaging forever.** *How you'd notice:* your $1/\sqrt{\tau}$ extrapolation promises $10^{-18}$ from a device with a $10^{-14}$ floor. *Instead:* read the Allan plot and stop at the floor.
- **Forgetting that averaging costs bandwidth.** *How you'd notice:* you claim both low noise and fast response from the same averaging. *Instead:* state the bandwidth or averaging time next to every noise figure.
- **Claiming Heisenberg scaling for an unentangled sensor.** *How you'd notice:* your $N$ independent atoms give $1/N$. *Instead:* independent particles give $1/\sqrt{N}$; $1/N$ needs entanglement and usually loses much of its gain to decoherence.
- **Ignoring dynamic range.** *How you'd notice:* you pick the most sensitive sensor for an outdoor job in the Earth's field. *Instead:* check that background plus signal fits the range before you compare sensitivity.

## Done when

No notes, 25 minutes, pass mark 8/10:

1. Define precision and accuracy in one sentence each, and say which calibration fixes.
2. Give the bandwidth definition as an amplitude factor, a power factor and in dB.
3. A sensor has $S = 80\,\mathrm{pT}/\sqrt{\mathrm{Hz}}$; give the rms noise in 16 Hz. (Answer: 320 pT.)
4. Write the correct unit of noise density and name the lecture line that gets it wrong.
5. How much longer must you average to cut white noise by 5×? (25×.)
6. On an Allan plot, what do slopes $-1/2$, $0$ and $+1/2$ mean?
7. $\sigma_y(1\,\mathrm{s}) = 3\times10^{-12}$, slope $-1/2$: what is $\sigma_y(400\,\mathrm{s})$? ($1.5\times10^{-13}$.)
8. SQL and Heisenberg phase error for $N = 10^{6}$. ($10^{-3}$ and $10^{-6}$ rad.)
9. $B \propto 1/r^2$, sensor moved from 30 mm to 10 mm: signal gain? (9×.)
10. Expand SWaP-C and say which F1 part it belongs to. (Part 5.)

## Spaced review

From Day 01, closed book, 15 minutes. Answers are folded below.

1. **F1:** list the six parts of the gain argument in order.
2. **F3:** rank these sources from most to least credible: vendor datasheet, market report, peer-reviewed or metrology-institute paper, press release, review article.
3. **F3:** name the three things every quoted number needs alongside it, and the rule for a ratio.
4. **M1:** how many femtotesla are in $50\,\mu\mathrm{T}$?
5. **M1:** express $3\,\mu\mathrm{Gal}$ in $\mathrm{m/s^2}$.
6. **M1:** a clock has a fractional frequency offset of $2\times10^{-15}$. How much time does it gain in one year ($3.156\times10^{7}$ s), and how far does light travel in that time?

<details>
<summary>Show answers</summary>

1. Classical limit, with a number; quantum mechanism, in one sentence of physics; figure of merit named; quantified gain (sourced); maturity and practicality (TRL, SWaP-C, barriers); verdict, with one honest caveat.
2. Peer-reviewed or metrology-institute paper > review article > vendor datasheet > press release > market report.
3. Date, conditions and units. A ratio needs both sides measured the same way.
4. $50\times10^{-6}/10^{-15} = 5\times10^{10}\,\mathrm{fT}$.
5. $1\,\mathrm{Gal} = 10^{-2}\,\mathrm{m/s^2}$, so $3\,\mu\mathrm{Gal} = 3\times10^{-8}\,\mathrm{m/s^2}$.
6. $2\times10^{-15}\times3.156\times10^{7} = 6.3\times10^{-8}\,\mathrm{s} = 63\,\mathrm{ns}$; light covers $3.0\times10^{8}\times6.3\times10^{-8} \approx 19\,\mathrm{m}$.

</details>

## Read next

- Degen, Reinhard & Cappellaro, *Quantum sensing*, https://arxiv.org/abs/1611.02427, §I-II: what counts as a quantum sensor, and the definitions of sensitivity and the $1/\sqrt{\text{time}}$ scaling you used today.
- Budker & Romalis, *Optical magnetometry*, https://arxiv.org/abs/physics/0611246 (short; read before Day 03): sensitivity limits and why the most sensitive schemes need near-zero field.

**Companion pointer and confusion log (15 min).** Open `companions/week02_companion.md` §1-3 and re-read lecture §2.1-2.2 with today's moves beside you. Note the two errata (L74, L94) in your own words. Log anything you could not do without looking:

| Symbol or unit | Step | Concept |
|---|---|---|
| | | |
| | | |
