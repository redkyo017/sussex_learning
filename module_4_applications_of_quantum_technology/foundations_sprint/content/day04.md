# Day 04: Interferometry to Atom Interferometry

**Time:** ~3 h · **Feeds:** Week 3 lecture (§3.1 to §3.4), inventory rows W3 Apply, W3 Consolidate, W3 quiz Q1 to Q4 · **Companion:** week03_companion.md §3 (notation and units), §4 (errata L91, L99/L139, L105-110, L135), §5 (clones)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min moves M6 and M7 below · 50 min quantitative drills (Exercises 4.1 to 4.8; skip the ones marked *stretch* if you are past time) · 45 min writing on the running case (Exercise 4.10; 4.9 is *stretch*) · 15 min companion pointer and confusion log.

This is the heaviest day of the sprint. The core reading is all of Moves M6.1 to M7.8: M6.1 to M7.5 build the phase formula and its noise, M7.8 (units, the classical gravimeter table and the spring erratum) feeds Exercises 4.8 and 4.10, and M7.6 and M7.7 carry the $T^2$ gain and the $10^{10}$ walk-down that Done-when items 7 and the anti-patterns test. The core exercises are 4.1, 4.2, 4.3, 4.5, 4.8 and 4.10 (4.10 is the core writing task). Exercises 4.4, 4.6, 4.7 and 4.9 are stretch work: do them today if time allows, otherwise on Day 05 before the checkpoint.

## Why this matters

Week 3 is the only week of the module that rests on a derivation, and the lecture skips it. Its central formula, Eq 3.1 (L105), is also written in a convention that makes the phase 4 times larger than the standard textbook result. If you take it at face value, every number you put in a Week 3 Apply or Consolidate post will be off by that factor. Today you build $\Phi = k_\text{eff} g T^2$ yourself from three laser pulses. Once you have it, the rest of the week becomes arithmetic: why the gain grows as $T^2$, why space helps, why the lecture's "$10^{10}$" atom-versus-light ratio shrinks to "a few orders", and how an atom gravimeter compares with springs, superconducting spheres and falling corner cubes.

The engineering view, in one line: an atom interferometer is a ruler made of light, read three times while an atom falls past it. The phase it returns is a **finite-difference second derivative** of the atom's position. That is why it measures acceleration and nothing else.

## Core concepts

### Move M6.1: Mach-Zehnder interference, phase to output intensity

**Idea.** A beam splitter sends light down two arms. One arm gains an extra phase $\varphi$ (for example from a cell of length $L$ whose refractive index differs by $\Delta n$, so $\varphi = \Delta n\,kL$ with wavenumber $k = 2\pi/\lambda$). The arms recombine on a second splitter, and the detector sees the sum of the two fields (lecture L26):

$$E_0\sin(\omega t+\varphi) + E_0\sin(\omega t).$$

Use the sum-to-product identity $\sin A + \sin B = 2\sin\!\big(\tfrac{A+B}{2}\big)\cos\!\big(\tfrac{A-B}{2}\big)$ with $A=\omega t+\varphi$ and $B=\omega t$:

$$E_0\sin(\omega t+\varphi) + E_0\sin(\omega t) = 2E_0\cos\!\big(\tfrac{\varphi}{2}\big)\,\sin\!\big(\omega t+\tfrac{\varphi}{2}\big).$$

The output is still a wave at frequency $\omega$, but its amplitude is $2E_0\cos(\varphi/2)$. A detector cannot follow optical oscillations, so it reports the time average of the square. The average of $\sin^2$ over a cycle is $\tfrac12$:

$$I \propto \big(2E_0\cos\tfrac{\varphi}{2}\big)^2\cdot\tfrac12 = 2E_0^2\cos^2\!\big(\tfrac{\varphi}{2}\big) = 2I_0\cos^2\!\big(\tfrac{\varphi}{2}\big),$$

with $I_0 = E_0^2$ in the lecture's shorthand. So $\varphi = 0$ gives a bright port, $\varphi = \pi$ a dark port, and the response repeats every $2\pi$. In a real interferometer the second output port carries the complement, $\propto\sin^2(\varphi/2)$, so no energy is lost (standard optics; judgement on the level of detail the lecture omits).

The one thing to remember: **an interferometer turns a phase into a brightness via $\cos^2(\varphi/2)$.** Everything later today is about which physical quantity ends up in $\varphi$.

*Worked clone.* Red laser, $\lambda = 633$ nm, cell $L = 2$ cm, $\Delta n = 3\times10^{-5}$. Then $k = 2\pi/\lambda = 9.93\times10^{6}\ \text{m}^{-1}$ and $\varphi = 3\times10^{-5}\times9.93\times10^{6}\times0.02 = 5.96$ rad (just under $2\pi$). Output fraction $\cos^2(5.96/2) = 0.97$ of the maximum.

*You've got it when* you can derive $\cos^2(\varphi/2)$ from two sines on a blank page in under two minutes, and say which $\varphi$ gives dark.

### Move M6.2: Matter waves, $\lambda_\text{dB} = h/(mv)$

**Idea.** Atoms are waves too, with de Broglie wavelength $\lambda_\text{dB} = h/p = h/(mv)$ (lecture L66). Heavy, slow things have short wavelengths, but cold atoms are slow enough for the wavelength to become optical-scale.

*Worked clone (rubidium-87, $m = 1.443\times10^{-25}$ kg).*
- Thermal beam at 300 m/s: $\lambda_\text{dB} = 6.626\times10^{-34}/(1.443\times10^{-25}\times300) = 1.5\times10^{-11}$ m, far smaller than the atom itself.
- Laser-cooled atom at 1 cm/s: $\lambda_\text{dB} = 4.6\times10^{-7}$ m, comparable to visible light.

This is why cold atoms are used: slow atoms mean long, large wavelengths, and (more importantly for sensing) long flight times $T$ inside the apparatus.

*You've got it when* you can compute $\lambda_\text{dB}$ in one line and explain why "slow" matters more than "small".

### Move M7.1: Photon recoil $\hbar k$ and $k_\text{eff}\approx 2k$

**Idea.** A photon carries momentum $p = \hbar k = h/\lambda$. When an atom absorbs one, it recoils with the **single-photon recoil velocity** $v_\text{rec} = \hbar k/m$.

*Worked clone (rubidium-87 on its 780 nm line).*
- $k = 2\pi/780\ \text{nm} = 8.06\times10^{6}\ \text{m}^{-1}$
- $v_\text{rec} = \hbar k/m = (1.055\times10^{-34}\times8.06\times10^{6})/1.443\times10^{-25} = 5.9\times10^{-3}$ m/s, about 5.9 mm/s (single-photon).

A Raman transition (lecture L64-66, Fig 3.4) uses **two counter-propagating beams**. The atom absorbs a photon from one beam and is stimulated to emit into the other, which runs the opposite way. Both momentum transfers push in the same direction, so the kick is $\hbar(\mathbf{k}_1 - \mathbf{k}_2)$ with $\mathbf{k}_2\approx-\mathbf{k}_1$:

$$k_\text{eff} = |\mathbf{k}_1-\mathbf{k}_2| \approx 2k = \frac{4\pi}{\lambda}.$$

For rubidium, $k_\text{eff}\approx 1.61\times10^{7}\ \text{m}^{-1}$ and the **two-photon (Raman) kick** is $\hbar k_\text{eff}/m = 2v_\text{rec}\approx 11.8$ mm/s. Below, $v_\text{rec}$ always means the single-photon value and "kick" the two-photon one. Small, but over a tenth of a second it opens a gap of about a millimetre between the two arms.

*You've got it when* you can say why counter-propagating beams double the kick, and compute $v_\text{rec}$ for any atom and wavelength.

### Move M7.2: Raman pulses as beam splitter and mirror (link to Day 03)

**Idea.** With the lasers far detuned from the excited level $e$, the three-level atom behaves as a two-level system $|a\rangle\leftrightarrow|b\rangle$ (lecture L60, Fig 3.3b). This is Day 03's Move M4 object. A resonant drive makes the population oscillate (Rabi oscillation):

$$P_b(t) = \sin^2\!\Big(\frac{\Omega_R t}{2}\Big),$$

where $\Omega_R$ is the Rabi frequency and $\Omega_R t$ is the **pulse area**.
- **$\pi/2$ pulse** ($\Omega_R t = \pi/2$): $P_b = \sin^2(\pi/4) = \tfrac12$. An equal superposition: a **50:50 beam splitter**.
- **$\pi$ pulse** ($\Omega_R t = \pi$): $P_b = 1$. It swaps $a\leftrightarrow b$: a **mirror**.

The new ingredient is that the internal state and the momentum are locked together. Each $a\to b$ flip adds $\hbar k_\text{eff}$, and each $b\to a$ flip removes it:

$$|a, p\rangle \;\leftrightarrow\; |b, p+\hbar k_\text{eff}\rangle .$$

So the $\pi/2$ pulse splits the atom into a "kicked" and an "unkicked" arm. The $\pi$ pulse at time $T$ swaps them (the kicked arm loses its kick, the unkicked arm gains one), which steers the arms back together. The final $\pi/2$ pulse at $2T$ recombines them (lecture Fig 3.2 and Fig 3.6). This $\pi/2$-$\pi$-$\pi/2$ sequence is the atomic Mach-Zehnder. **$T$ is the time between pulses**, so the whole sequence lasts $2T$.

*You've got it when* you can draw the two arms on a $z$-versus-$t$ sketch, label each pulse "splitter / mirror / splitter", and say what $T$ is.

### Move M7.3: Deriving $\Phi = k_\text{eff} g T^2$ (concept level)

This is the step the lecture skips. Three facts are enough.

**Fact 1 (the laser is a ruler).** The two Raman beams form a light pattern whose phase at height $z$ is $\phi_\text{laser} = k_\text{eff}\,z$. Every time a pulse flips an atom's state, the atom's wave picks up the laser phase at the atom's position: $+k_\text{eff}z$ for $a\to b$, $-k_\text{eff}z$ for $b\to a$. (Standard result; Cronin et al., inertial sensing section, and Abend et al., gravimeter section, see Read next. We take it as given.)

**Fact 2 (bookkeeping).** Follow both arms to the $b$ output port.
- Upper arm: flipped $a\to b$ at $t=0$ ($+k_\text{eff}z(0)$), flipped back $b\to a$ at $T$ ($-k_\text{eff}z_\text{up}(T)$), flipped $a\to b$ at $2T$ ($+k_\text{eff}z(2T)$).
- Lower arm: no flip at $t=0$, flipped $a\to b$ at $T$ ($+k_\text{eff}z_\text{low}(T)$), no flip at $2T$.

The difference between the two arms is

$$\Phi = k_\text{eff}\big[z(0) - z_\text{up}(T) - z_\text{low}(T) + z(2T)\big].$$

In a uniform gravity field the propagation phase (gathered between pulses) and the separation phase (from the arms' small mismatch at the last pulse) cancel in total, so only the laser phases remain (judgement on depth; see Cronin et al., inertial sensing section).

**Fact 3 (free fall).** Ignore the small recoil for a moment and let both arms follow the mid-point trajectory $z(t) = z_0 + v_0 t - \tfrac12 g t^2$. Then $z_\text{up}(T)+z_\text{low}(T)\approx 2z(T)$, and:

$$
\begin{aligned}
z(0) - 2z(T) + z(2T) &= z_0 \;-\; 2\big(z_0 + v_0T - \tfrac12 gT^2\big) \;+\; \big(z_0 + 2v_0T - 2gT^2\big)\\
&= (z_0 - 2z_0 + z_0) + (-2v_0T + 2v_0T) + (gT^2 - 2gT^2)\\
&= -gT^2 .
\end{aligned}
$$

The starting height $z_0$ cancels, and so does the starting velocity $v_0$. Only the acceleration survives. Therefore

$$\boxed{\;|\Phi| = k_\text{eff}\,g\,T^2\;}$$

(the sign depends on which way $k_\text{eff}$ points; we quote magnitudes). The output population is $P_b = \tfrac12(1-\cos\Phi)$, which is the $\cos^2/\sin^2$ fringe of Move M6.1 again.

*Why the recoil drops out (check it once).* With the two-photon (Raman) kick $v_r = \hbar k_\text{eff}/m$ included, $z_\text{up}(T) = z_0 + (v_0+v_r)T - \tfrac12gT^2$ and $z_\text{low}(T) = z_0 + v_0T - \tfrac12gT^2$, so their sum is $2z_0 + 2v_0T + v_rT - gT^2$. Both arms meet at $z(2T) = z_0 + 2v_0T + v_rT - 2gT^2$. The $v_rT$ terms cancel in the combination, which again equals $-gT^2$.

*Engineer's reading.* $\big[z(0) - 2z(T) + z(2T)\big]/T^2$ is the central finite-difference estimate of $\ddot z$. For a parabola it is exact. The interferometer samples the atom's position three times with a ruler whose ticks are $2\pi/k_\text{eff} = \lambda/2$ apart, and returns the second difference.

*Worked clone (rubidium, $T = 0.1$ s, $g = 9.81\ \text{m/s}^2$).* $\Phi = 1.61\times10^{7}\times9.81\times0.01 = 1.58\times10^{6}$ rad. That is about a quarter of a million fringes. Meanwhile, the arms separate by (two-photon kick) $\times T = 2v_\text{rec}T = 1.18$ mm at the mirror pulse.

*You've got it when* you can reproduce Facts 1-3 and the three-line cancellation from memory, and say in one sentence why the interferometer ignores $z_0$ and $v_0$.

### Move M7.4: Reconciling the lecture's conventions (errata L105-110 and L91)

**Eq 3.1 (L105-110).** The lecture writes $\Phi = k_\text{eff}a\tau^2$ with $\tau = 2T$, the total interrogation time. Substituting gives $k_\text{eff}a(2T)^2 = 4k_\text{eff}aT^2$: **4 times the standard result**. The standard formula, derived above, is $\Phi = k_\text{eff}gT^2$ with $T$ the time *between* pulses. Use the standard one and say so when you quote it. The scaling ($\propto$ time squared) is right either way; only the prefactor is off. The rotation term of Eq 3.1, $2k_\text{eff}(\Omega\times v)\tau^2$, uses the same $\tau = 2T$, so it inherits the same factor of 4: the standard form is $2k_\text{eff}(\Omega\times v)T^2$ (companion §4E, item 7). The lecture's own L114, $2\Omega k_\text{eff}LT$, already uses $T$ as the time between gratings.

**Chirp (L91).** Falling atoms see the Raman lasers Doppler-shifted. To stay resonant, the lab ramps the frequency difference of the two beams at a rate $\alpha$ (in Hz/s, a "chirp"). That ramp adds its own laser phase $2\pi\alpha T^2$, so the measured phase becomes

$$\Phi = (k_\text{eff}\,g - 2\pi\alpha)\,T^2 .$$

At $\alpha_0 = k_\text{eff}g/2\pi$ the phase is zero **for every $T$**: the fringes from different $T$ all line up at one chirp value. Finding that $\alpha_0$ measures $g$. The lecture's "$\alpha = g$" (L91) cannot be literally right, because $\alpha$ is in Hz/s and $g$ in m/s². The correct statement is $\alpha_0 = k_\text{eff}g/2\pi$.

*Worked clone (rubidium).* $\alpha_0 = 1.61\times10^{7}\times9.81/2\pi = 2.52\times10^{7}$ Hz/s, about 25.2 MHz/s.

*You've got it when* you can explain the factor 4 in one sentence and write the chirp-null condition with units.

### Move M7.5: Sensitivity, shot noise and averaging (links Day 02)

**Idea.** Invert the phase formula. A phase uncertainty $\delta\varphi$ becomes an acceleration uncertainty

$$\delta g = \frac{\delta\varphi}{k_\text{eff}T^2}.$$

With $N$ uncorrelated atoms per shot, the best phase resolution is the **shot-noise limit** $\delta\varphi = 1/\sqrt N$ (Day 02, Move M3). Repeating shots and averaging for a time $t$ improves the result as $1/\sqrt t$ (Day 02, Move M2). That is why resolution is quoted per $\sqrt{\text{Hz}}$ (lecture L123): multiply the per-shot noise by $\sqrt{\text{cycle time}}$ to get a noise density, then divide by $\sqrt t$ to get the noise after averaging for $t$.

*Worked clone (rubidium, $N = 10^{6}$, $T = 0.1$ s).* $\delta\varphi = 10^{-3}$ rad, so $\delta g = 10^{-3}/(1.61\times10^{7}\times0.01) = 6.2\times10^{-9}\ \text{m/s}^2 = 0.62\ \mu\text{Gal}$ per shot.

*Check the lecture's own numbers.* L99 reports a measured $20\ \mu\text{Gal}/\sqrt{\text{Hz}}$ for the lab atom gravimeter. After 60 s that averages down to $20/\sqrt{60} = 2.6\ \mu\text{Gal}$, and $5\ \mu\text{Gal}$ is reached after $(20/5)^2 = 16$ s. That is consistent with L123's "attains [5 µGal] in less than 1 minute". Real instruments sit well above the shot-noise limit because ground vibration shakes the retro-reflecting mirror, which is the ruler (judgement; Abend et al. discuss vibration as a main noise source).

*You've got it when* you can go from $N$, $T$ and cycle time to a noise density in $\mu\text{Gal}/\sqrt{\text{Hz}}$, and say why real instruments do worse.

### Move M7.6: Ground versus space, the $T^2$ gain

**Idea.** Phase, and so sensitivity, scales as $T^2$. On the ground the atoms fall out of the apparatus. In a simple drop they fall $\tfrac12g(2T)^2 = 2gT^2$ during the sequence. A fountain does better: launch the atoms upward so they rise for $T$ and fall for $T$, as the lecture's instrument does (L95), and the apex is only $\tfrac12gT^2 = g(2T)^2/8$ above the launch point, four times less than the drop. Either way $T$ is limited to a few hundred milliseconds by the height of the vacuum chamber (lecture L191: "a few hundreds of milliseconds on the ground"). In orbit the atoms and the apparatus fall together, so $T$ can reach about 10 s (L191).

*Worked clone.* Against ground values of 0.1 s and 0.3 s, a space value of $T = 10$ s gains $(10/0.1)^2 = 10^{4}$ and $(10/0.3)^2 \approx 1.1\times10^{3}$ in phase per unit $g$.

The catch: long $T$ means fewer shots per second (lower bandwidth), and the cloud spreads out thermally, so it needs colder atoms and fewer of them (lecture L159). A space mission also has to shrink the whole apparatus (L191).

*You've got it when* you can state the drop-height constraint and compute a $T^2$ gain for any pair of $T$ values.

### Move M7.7: The Sagnac ratio, and why $10^{10}$ becomes "a few orders"

**Idea.** For rotation $\Omega$ and enclosed area $A$ (lecture L114-117):

$$\Phi_\text{atom} = \frac{4\pi\Omega mA}{h}, \qquad \Phi_\text{light} = \frac{4\pi\Omega A}{\lambda c}, \qquad \frac{\Phi_\text{atom}}{\Phi_\text{light}} = \frac{m\lambda c}{h}.$$

The lecture's form $\lambda c/(\lambda_\text{dB}v)$ is the same thing, because $\lambda_\text{dB}v = h/m$. The ratio is set by $h/m$, a property of the atom, not by how fast it moves.

*Worked clone (rubidium-87, light at 780 nm).*
- $h/m = 6.626\times10^{-34}/1.443\times10^{-25} = 4.6\times10^{-9}\ \text{m}^2/\text{s}$
- ratio $= \lambda c/(h/m) = 780\times10^{-9}\times3.00\times10^{8}/4.6\times10^{-9} = 5.1\times10^{10}$

That is the lecture's "$\approx10^{10}$" (L117). Now apply the lecture's own caveats (L121):
1. **Area.** A fibre gyroscope coil encloses about $10^{3}\ \text{m}^2$; an atom interferometer about $10^{-4}\ \text{m}^2$. That is a factor $10^{7}$ against the atoms, which leaves a response factor of $5.1\times10^{10}/10^{7} = 5.1\times10^{3}$: "a few orders".
2. **Count rate.** One watt of light is about $10^{19}$ photons/s, against about $10^{7}$ atoms/s. Shot-noise phase resolution scales as $1/\sqrt{\text{rate}}$, which costs the atoms another $\sqrt{10^{19}/10^{7}} = 10^{6}$.

On the lecture's round numbers (L121) the area and flux penalties eat almost all of the $10^{10}$: taken literally they leave $5.1\times10^{3}/10^{6} = 5.1\times10^{-3}$, which would put atoms behind on a pure shot-noise budget. But those two inputs are not like-for-like (F3). The $10^{7}$ atoms/s is a cold-atom figure, while the best rotation sensors use thermal atomic beams, which the lecture says deliver far more atoms per second (L103, L110). And $10^{19}$ photons/s assumes a full watt reaching a shot-noise-limited detector. Measured performance is the better guide: a thermal-beam atom gyroscope has reached $6\times10^{-10}$ rad/s/√Hz (L151), and the lecture places atom inertial sensors comparable to, or better than, the best sensors of any technology (L103). So the $10^{10}$ is a response factor at equal area and equal flux, not a delivered gain. What atoms add on top of their measured noise is a scale factor fixed by $k_\text{eff}$ and $h/m$, and good bias stability (judgement; see Cronin et al., inertial sensing section).

*You've got it when* you can compute $m\lambda c/h$ for any atom, and walk a reader from $10^{10}$ down through the area and flux factors without hand-waving.

### Move M7.8: Units and the classical gravimeter table

**Units (M1 applied).**
- $1\ \text{Gal} = 10^{-2}\ \text{m/s}^2$; $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2 \approx 1.02\times10^{-9}g$ (round to $10^{-9}g$).
- Gravity gradient: $1\ \text{E}$ (Eötvös) $= 10^{-9}\ \text{s}^{-2}$, i.e. $10^{-9}$ m/s² of $\Delta g$ per metre.
- Noise is per $\sqrt{\text{Hz}}$ (Move M7.5); drift is per month or year; accuracy is a bare fraction.

**Classical competitors (lecture L133-139, Fig 3.7).** Values are as the lecture states them; fractions are of $g$.

| Instrument | Absolute or relative | Principle | Noise | Stability / accuracy | Size / mass / power |
|---|---|---|---|---|---|
| Pendulum (1930s surveys) | absolute | period $T = 2\pi\sqrt{L/g}$ | not stated | accuracy $\Delta g/g\approx10^{-4}$ | not stated |
| Spring | relative | $k\,\delta L = mg$ | $5\times10^{-9}/\sqrt{\text{Hz}}$ | drift up to $1.5\times10^{-6}$/month; needs frequent recalibration | 0.04 m³ / 14 kg / 24 W |
| Superconducting | relative | levitated sphere, voltage readout | $10^{-12}/\sqrt{\text{Hz}}$ | drift $\approx10^{-9}$/year | 1.5 m³ / 320 kg / 400 W (not portable) |
| Falling corner cube | absolute | Michelson fringes from a falling mirror | $5\times10^{-8}/\sqrt{\text{Hz}}$ (L139) | accuracy $4\times10^{-9}$ | 1.5 m³ / 130 kg / 350 W (lab grade; portable versions exist) |
| Atom (lab instrument, L91-99) | absolute | $\Phi = k_\text{eff}gT^2$ | $20\ \mu\text{Gal}/\sqrt{\text{Hz}}\approx2\times10^{-8}/\sqrt{\text{Hz}}$ | $10^{-9}$ (L91); later $1.3\times10^{-9}$ (L147) | not stated |

**Two errata to carry.**
- **L135, spring sensitivity.** The lecture says sensitivity $\propto 1/T^2$. From $k\,\delta L = mg$ and $T = 2\pi\sqrt{m/k}$, $\delta L = mg/k = gT^2/4\pi^2$. A change $\Delta g$ moves the mass by $\Delta(\delta L) = \Delta g\,T^2/4\pi^2$, so the **response** (stretch per unit $\Delta g$) **rises** as $T^2$. Turn it round: with a fixed length resolution $\delta L_\text{min}$, the smallest detectable change is $\Delta g_\text{min} = 4\pi^2\delta L_\text{min}/T^2$, which **falls** as $1/T^2$. The lecture's "$1/T^2$" is a loose statement of that second quantity, not simply wrong; say which one you mean. Either way a soft, long-period spring is the sensitive one, which is why survey meters use long, "zero-length" spring designs (L135).
- **L99 versus L139, corner-cube noise.** L99 gives the commercial corner-cube gravimeter used for comparison $5\ \mu\text{Gal}/\sqrt{\text{Hz}}$ ($\approx5.1\times10^{-9}g/\sqrt{\text{Hz}}$), under ideal conditions at its maximum drop rate. L139 gives falling corner cubes $5\times10^{-8}g/\sqrt{\text{Hz}}$ ($\approx49\ \mu\text{Gal}/\sqrt{\text{Hz}}$). That is a factor of 10 apart. The lecture does not reconcile them; the difference may be ideal versus typical conditions. Quote whichever you use with its conditions (F3), and never mix them in one ratio.

**Week 3 quiz (inventory rows W3 Q1-Q4).** Do the quiz cold, then check it against the key in `docs/problem_inventory.md` (Quizzes table, Week 3). The physics behind Q1 and Q2 is today's: gravity counts as an inertial force because it cannot be told apart from acceleration (the equivalence principle), and a calibrated spring measures it (the spring gravimeter above). Read the inventory's flag on Q1 before you argue with the marker.

*You've got it when* you can rebuild the table's "absolute or relative" column and its SWaP figures from memory, convert any µGal figure to a fraction of $g$, and state both errata.

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. Constants: $h = 6.626\times10^{-34}$ J s, $\hbar = 1.055\times10^{-34}$ J s, $c = 3.00\times10^{8}$ m/s, $g = 9.81\ \text{m/s}^2$, caesium-133 mass $m_\text{Cs} = 2.207\times10^{-25}$ kg.

### Exercise 4.1 (quantitative)

A Mach-Zehnder uses infrared light at $\lambda = 1550$ nm. One arm passes through a gas cell of length $L = 5$ cm. (a) What index difference $\Delta n$ puts the bright port at its first dark fringe? (b) For $\Delta n = 5\times10^{-6}$, what fraction of the maximum brightness reaches that port?

**Hint:** Dark means $\varphi = \pi$; $\varphi = \Delta n\,kL$ with $k = 2\pi/\lambda$. Then use $\cos^2(\varphi/2)$ from Move M6.1.

**Solution sketch:**
- *Restate:* find $\Delta n$ for $\varphi = \pi$, and $I/I_\text{max}$ at a given $\Delta n$.
- *Write state:* $\lambda = 1.55\times10^{-6}$ m, $L = 0.05$ m.
- *Name move:* M6.1, phase to $\cos^2$.
- *Algebra:* (a) $\Delta n\,(2\pi/\lambda)L = \pi \Rightarrow \Delta n = \lambda/(2L) = 1.55\times10^{-6}/0.1 = 1.55\times10^{-5}$. (b) $\varphi = 5\times10^{-6}\times(2\pi/1.55\times10^{-6})\times0.05 = 1.01$ rad; $\cos^2(0.507) = 0.76$.
- *Check:* $\Delta n$ in (b) is about a third of the dark value, so $\varphi\approx\pi/3$ and $\cos^2(\pi/6) = 0.75$. Consistent.
- *Answer:* (a) $\Delta n = 1.55\times10^{-5}$; (b) about 0.76 of the maximum.

### Exercise 4.2 (quantitative)

Caesium-133 is driven on its 852 nm line. (a) Find $k$ and the single-photon recoil velocity. (b) With counter-propagating Raman beams, what is the velocity kick? (c) Find $\lambda_\text{dB}$ for a thermal caesium atom at 200 m/s and for a cold one at 2 cm/s.

**Hint:** $v_\text{rec} = \hbar k/m$; counter-propagating beams double it (Move M7.1); $\lambda_\text{dB} = h/(mv)$ (Move M6.2).

**Solution sketch:**
- *Restate:* recoil, two-photon kick, two de Broglie wavelengths.
- *Write state:* $\lambda = 852$ nm, $m = 2.207\times10^{-25}$ kg.
- *Name move:* M7.1 and M6.2.
- *Algebra:* (a) $k = 2\pi/852\ \text{nm} = 7.37\times10^{6}\ \text{m}^{-1}$; $v_\text{rec} = 1.055\times10^{-34}\times7.37\times10^{6}/2.207\times10^{-25} = 3.5\times10^{-3}$ m/s. (b) $2v_\text{rec} = 7.0\times10^{-3}$ m/s. (c) $\lambda_\text{dB} = 6.626\times10^{-34}/(2.207\times10^{-25}\times200) = 1.5\times10^{-11}$ m; at 2 cm/s, $1.5\times10^{-7}$ m.
- *Check:* caesium is heavier than rubidium and its light is slightly redder, so its recoil (3.5 mm/s) should be smaller than rubidium's 5.9 mm/s. It is.
- *Answer:* $k = 7.37\times10^{6}\ \text{m}^{-1}$, $v_\text{rec} = 3.5$ mm/s, kick 7.0 mm/s; $\lambda_\text{dB} = 15$ pm (thermal) and 150 nm (cold).

### Exercise 4.3 (quantitative)

A caesium gravimeter runs $\pi/2$-$\pi$-$\pi/2$ with pulse spacing $T = 0.2$ s. (a) Show numerically that $z(0) - 2z(T) + z(2T) = -gT^2$ for $z(t) = v_0t - \tfrac12gt^2$ with $v_0 = 0.3$ m/s. (b) Compute $k_\text{eff}$ and $\Phi$, and the number of fringes $\Phi/2\pi$. (c) What would Eq 3.1 with $\tau = 2T$ give? (d) How far apart are the arms at the mirror pulse?

**Hint:** Plug $t = 0, T, 2T$ into $z(t)$. Then $k_\text{eff} = 4\pi/\lambda$ and $\Phi = k_\text{eff}gT^2$ (Moves M7.3 and M7.4). The arm gap is the kick times $T$.

**Solution sketch:**
- *Restate:* check the second difference, then the phase in both conventions, then the arm gap.
- *Write state:* $\lambda = 852$ nm, $T = 0.2$ s, $v_0 = 0.3$ m/s, kick $7.0$ mm/s (from 4.2).
- *Name move:* M7.3 and M7.4.
- *Algebra:* (a) $z(T) = 0.06 - 0.196 = -0.136$ m; $z(2T) = 0.12 - 0.785 = -0.665$ m. So $0 - 2(-0.136) + (-0.665) = -0.392$ m, and $-gT^2 = -9.81\times0.04 = -0.392$ m. (b) $k_\text{eff} = 4\pi/852\ \text{nm} = 1.47\times10^{7}\ \text{m}^{-1}$; $\Phi = 1.47\times10^{7}\times9.81\times0.04 = 5.79\times10^{6}$ rad; $\Phi/2\pi = 9.2\times10^{5}$ fringes. (c) $k_\text{eff}g(2T)^2 = 2.32\times10^{7}$ rad, 4 times larger. (d) $7.0\ \text{mm/s}\times0.2\ \text{s} = 1.4$ mm.
- *Check:* $v_0$ dropped out of (a) as Move M7.3 predicts; the answer depends only on $g$ and $T$.
- *Answer:* (a) $-0.392$ m $= -gT^2$; (b) $\Phi = 5.79\times10^{6}$ rad, about $9.2\times10^{5}$ fringes; (c) $2.32\times10^{7}$ rad in the lecture's convention (4×, erratum L105-110); (d) 1.4 mm.

### Exercise 4.4 (quantitative) (stretch)

For the caesium gravimeter of 4.3: (a) at what chirp rate $\alpha_0$ does the phase vanish for every $T$? (b) If the chirp can be set to a resolution of 1 Hz/s, what change in $g$ does one step correspond to, in m/s² and µGal? (c) And at 0.01 Hz/s?

**Hint:** $\alpha_0 = k_\text{eff}g/2\pi$ (Move M7.4), so $\Delta g = 2\pi\,\Delta\alpha/k_\text{eff}$. Note that $2\pi/k_\text{eff} = \lambda/2$.

**Solution sketch:**
- *Restate:* chirp null, then $g$ per chirp step.
- *Write state:* $k_\text{eff} = 1.47\times10^{7}\ \text{m}^{-1}$; $\lambda/2 = 426$ nm.
- *Name move:* M7.4 (chirp null), M1 units.
- *Algebra:* (a) $\alpha_0 = 1.47\times10^{7}\times9.81/2\pi = 2.30\times10^{7}$ Hz/s. (b) $\Delta g = (\lambda/2)\times1\ \text{Hz/s} = 4.26\times10^{-7}\ \text{m/s}^2 = 42.6\ \mu\text{Gal}$. (c) $0.43\ \mu\text{Gal}$.
- *Check:* units: m $\times$ Hz/s $=$ m/s². Rubidium's $\alpha_0$ was 25.2 MHz/s; caesium's longer wavelength gives a slightly smaller value. Consistent.
- *Answer:* $\alpha_0\approx23.0$ MHz/s; one 1 Hz/s step is $42.6\ \mu\text{Gal}$, and 0.01 Hz/s is $0.43\ \mu\text{Gal}$. In practice $\alpha_0$ is found by fitting fringes, not by stepping, so this is a scale-factor feel, not a resolution limit.

### Exercise 4.5 (quantitative)

A caesium gravimeter detects $N = 4\times10^{5}$ atoms per shot, uses $T = 0.15$ s, and repeats every 0.8 s. (a) Find the shot-noise phase and $\delta g$ per shot. (b) Convert to a noise density in µGal/√Hz. (c) How long must it average to reach 0.1 µGal? (d) The lecture's lab instrument measured $20\ \mu\text{Gal}/\sqrt{\text{Hz}}$ (L99). How far is that above your shot-noise figure, and why?

**Hint:** $\delta\varphi = 1/\sqrt N$, $\delta g = \delta\varphi/(k_\text{eff}T^2)$. Noise density = per-shot noise $\times\sqrt{\text{cycle time}}$. After time $t$, noise = density$/\sqrt t$ (Move M7.5).

**Solution sketch:**
- *Restate:* per-shot $\delta g$, density, averaging time, comparison.
- *Write state:* $N = 4\times10^{5}$, $T = 0.15$ s, cycle 0.8 s, $k_\text{eff} = 1.47\times10^{7}\ \text{m}^{-1}$.
- *Name move:* M7.5 with M3 (shot noise) and M2 ($1/\sqrt t$).
- *Algebra:* (a) $\delta\varphi = 1/\sqrt{4\times10^{5}} = 1.58\times10^{-3}$ rad; $\delta g = 1.58\times10^{-3}/(1.47\times10^{7}\times0.0225) = 4.8\times10^{-9}\ \text{m/s}^2 = 0.48\ \mu\text{Gal}$. (b) $0.48\times\sqrt{0.8} = 0.43\ \mu\text{Gal}/\sqrt{\text{Hz}}$. (c) $t = (0.43/0.1)^2\approx18$ s. (d) $20/0.43\approx47$ times worse.
- *Check:* doubling $T$ would cut $\delta g$ by 4; quadrupling $N$ only by 2. That is the $T^2$ versus $\sqrt N$ asymmetry that makes $T$ the lever designers fight for.
- *Answer:* $0.48\ \mu\text{Gal}$ per shot, $0.43\ \mu\text{Gal}/\sqrt{\text{Hz}}$, about 18 s to 0.1 µGal. A real instrument is roughly 47 times worse because ground vibration of the reference mirror, not atom counting, sets the noise (judgement; Abend et al.).

### Exercise 4.6 (quantitative) (stretch)

Compare a ground gravimeter with $T = 0.25$ s and a space instrument with $T = 8$ s. (a) What is the $T^2$ gain? (b) How far do atoms fall during a ground drop sequence of length $2T$, and how tall must a fountain be instead (atoms launched upward, as in the lecture's instrument, L95)? (c) For equal $\delta g$, by what factor could the space instrument reduce its atom number? (d) Why can't the ground instrument simply use $T = 8$ s?

**Hint:** Drop distance $\tfrac12g(2T)^2 = 2gT^2$; fountain apex $g(2T)^2/8 = \tfrac12gT^2$, four times less. At fixed $\delta g$, $\delta\varphi \propto T^2$ is allowed to grow, and $\delta\varphi = 1/\sqrt N$, so $N\propto T^{-4}$ (Moves M7.5 and M7.6).

**Solution sketch:**
- *Restate:* sensitivity gain, drop height, atom budget, and the ground limit.
- *Write state:* $T_\text{g} = 0.25$ s, $T_\text{s} = 8$ s.
- *Name move:* M7.6, with M7.5.
- *Algebra:* (a) $(8/0.25)^2 = 1024$. (b) Drop: $2\times9.81\times0.0625 = 1.23$ m; fountain: $\tfrac12\times9.81\times0.0625 = 0.31$ m. (c) $(8/0.25)^4 = 1.05\times10^{6}$. (d) At $T = 8$ s the atoms would fall $2\times9.81\times64\approx1256$ m in a drop, or need a fountain $\tfrac12\times9.81\times64\approx314$ m tall.
- *Check:* the fountain is exactly a quarter of the drop. A 1.2 m drop (or a 0.3 m fountain) fits in a lab vacuum chamber, which matches "a few hundred milliseconds on the ground" (L191).
- *Answer:* a gain of about $10^{3}$; a 1.23 m drop or a 0.31 m fountain; up to a million times fewer atoms for the same $\delta g$; and the ground version would need a drop tower over a kilometre tall, or a fountain about 314 m tall.

### Exercise 4.7 (quantitative) (stretch)

(a) Compute $h/m$ for caesium-133 and the Sagnac ratio $m\lambda c/h$ for light at 852 nm. (b) A compact atom gyroscope encloses $2\times10^{-4}\ \text{m}^2$; a fibre gyroscope coil encloses 500 m². What response ratio is left? (c) The atom source gives $5\times10^{6}$ atoms/s; the fibre gyroscope's light gives $10^{18}$ photons/s. Including shot-noise phase resolution, which instrument comes out ahead on these numbers, and by how much?

**Hint:** Follow Move M7.7 step by step: intrinsic ratio, times the area ratio, divided by $\sqrt{\text{flux ratio}}$.

**Solution sketch:**
- *Restate:* intrinsic Sagnac ratio, then corrected for area, then for flux.
- *Write state:* $m = 2.207\times10^{-25}$ kg, $\lambda = 852$ nm, areas $2\times10^{-4}$ and 500 m², rates $5\times10^{6}$ and $10^{18}$ /s.
- *Name move:* M7.7.
- *Algebra:* (a) $h/m = 6.626\times10^{-34}/2.207\times10^{-25} = 3.0\times10^{-9}\ \text{m}^2/\text{s}$; ratio $= 852\times10^{-9}\times3.00\times10^{8}/3.0\times10^{-9} = 8.5\times10^{10}$. (b) Area factor $500/2\times10^{-4} = 2.5\times10^{6}$, so $8.5\times10^{10}/2.5\times10^{6} = 3.4\times10^{4}$. (c) $\sqrt{10^{18}/5\times10^{6}} = 4.5\times10^{5}$, so $3.4\times10^{4}/4.5\times10^{5} = 0.076$.
- *Check:* heavier atom, larger $m/h$, larger ratio than rubidium's $5.1\times10^{10}$. Consistent. But the inputs to (c) are assumptions, not like-for-like (F3): $5\times10^{6}$ atoms/s is cold-atom flux, and a thermal beam delivers far more (L110).
- *Answer:* $h/m = 3.0\times10^{-9}\ \text{m}^2/\text{s}$; intrinsic ratio $8.5\times10^{10}$; $3.4\times10^{4}$ after area; on these assumed numbers the light gyroscope is ahead by about 13 times on shot-noise resolution. That is not a verdict on the technology: the real outcome depends on the flux and area actually achieved, so for a real comparison cite a measured figure, such as the thermal-beam atom gyroscope's $6\times10^{-10}$ rad/s/√Hz (L151), against a measured fibre-gyroscope figure taken under the same conditions (judgement).

### Exercise 4.8 (quantitative)

(a) A simple spring gravimeter has period 0.4 s. How far does the mass move for $\Delta g = 10\ \mu\text{Gal}$? Repeat for a 4 s period, and state the ratio. Which way does this correct the lecture's L135? (b) A gradiometer reads 25 E across a 0.5 m vertical baseline. What is $\Delta g$ between the two clouds, in µGal? (c) Convert $3\times10^{-8}g$ to µGal. (d) An air-filled void of radius 1.5 m sits with its centre 6 m below the surface, in soil of density 1900 kg/m³. Treat it as a missing sphere of mass and find the peak gravity deficit directly above it, in µGal.

**Hint:** (a) $\Delta(\delta L) = \Delta g\,T^2/4\pi^2$ (Move M7.8). (b) E is $10^{-9}\ \text{s}^{-2}$ = m/s² per metre. (d) Point mass: $\Delta g = G\,\Delta M/d^2$ with $\Delta M = \tfrac43\pi R^3\Delta\rho$ and $G = 6.674\times10^{-11}$ (standard Newtonian gravity; judgement, not in the lecture).

**Solution sketch:**
- *Restate:* spring response at two periods; gradient to $\Delta g$; a unit conversion; a void signal.
- *Write state:* $T = 0.4$ and 4 s; 10 µGal $= 10^{-7}$ m/s²; 25 E, 0.5 m; $R = 1.5$ m, $d = 6$ m, $\Delta\rho = 1900$ kg/m³.
- *Name move:* M7.8 and M1.
- *Algebra:* (a) $10^{-7}\times0.16/39.5 = 4.1\times10^{-10}$ m; $10^{-7}\times16/39.5 = 4.1\times10^{-8}$ m; ratio 100. (b) $25\times10^{-9}\times0.5 = 1.25\times10^{-8}\ \text{m/s}^2 = 1.25\ \mu\text{Gal}$. (c) $3\times10^{-8}\times9.81 = 2.9\times10^{-7}\ \text{m/s}^2 = 29\ \mu\text{Gal}$. (d) $\Delta g = \tfrac43\pi\times6.674\times10^{-11}\times1900\times1.5^3/6^2 = 5.0\times10^{-8}\ \text{m/s}^2 = 5.0\ \mu\text{Gal}$.
- *Check:* (a) a 10× longer period gives 100× more motion, so the response rises as $T^2$. L135's $1/T^2$ describes the other quantity: at fixed length resolution the smallest detectable $\Delta g = 4\pi^2\delta L_\text{min}/T^2$ falls 100× over the same change. (d) A few µGal for a metre-scale void is why survey instruments are judged at the µGal level.
- *Answer:* (a) $4.1\times10^{-10}$ m and $4.1\times10^{-8}$ m, ratio 100: the response rises as $T^2$, so the smallest detectable $\Delta g$ (at fixed length resolution) falls as $1/T^2$, which is what L135 loosely calls sensitivity. (b) 1.25 µGal. (c) 29 µGal. (d) about 5.0 µGal.

### Exercise 4.9 (writing) (stretch)

*Inventory row W3 Apply.* Write a 200-300-word post on how the quantum approach matters for one atom-interferometry application: a gravity survey for voids under a reservoir embankment owned by **Harrowmere Water & Power**. Use the void signal from Exercise 4.8(d) and the fact-sheet instruments (all fictional): the installed relative spring meter (8 µGal/√Hz, drift 30 µGal/day, 14 kg) and a candidate portable atom gravimeter (absolute, 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation).

**Hint:** Use F1 in short form: the classical baseline with a number; the mechanism in one sentence ($\Phi = k_\text{eff}gT^2$); the figure of merit (µGal repeatability and absoluteness); the gain; maturity; a caveat. Name the classical instrument you are comparing against, and compare like with like (field instrument with field instrument).

**Model paragraph:**
Harrowmere Water & Power has seen seepage at the toe of its Greystock reservoir embankment (fictional), and engineers suspect a void forming in the fill. A void of radius 1.5 m centred 6 m down would lower gravity directly above it by about 5 µGal (point-mass estimate), and the survey covers 150 stations (fictional). The installed spring gravimeter is not short of sensitivity: at 8 µGal/√Hz (fictional) one minute of averaging gives about 1.0 µGal. Its weakness is that it is relative. It drifts by 30 µGal a day (fictional), which is 1.25 µGal an hour, a quarter of the target signal every hour, and a knock in transport can shift its zero without warning. So every reading only means something relative to base-station visits, and an uncorrected offset can look like a void. An atom gravimeter measures $g$ absolutely: three laser pulses read the position of free-falling atoms against a ruler of light, and the phase $\Phi = k_\text{eff}gT^2$ depends only on the laser wavelength and a time, not on a spring that ages. The gain is therefore not lower noise but readings that do not depend on the instrument's history, so an anomaly at a station is in the ground, not in the meter (judgement). The caveat is practical and numerical: the candidate is noisier, so one minute gives only about 3.9 µGal (a signal-to-noise of about 1.3 on the void), and at 110 kg against 14 kg, with vibration isolation at each set-up, it is far slower to move. A sensible pilot pairs one atom gravimeter as an absolute anchor at a few stations with the spring meter for the grid.

**What a weak answer misses:** It claims the atom gravimeter is "more sensitive" than a spring meter without numbers, when on Harrowmere's figures the spring meter is the quieter one (8 against 30 µGal/√Hz). It does not say *which* limitation (drift and relative-only readings) the quantum sensor removes. It quotes the lecture's Eq 3.1 with $\tau = 2T$ or a lab record as if it were a field figure. It gives no size of the target signal (about 5 µGal), so the reader cannot judge whether any instrument is good enough.

### Exercise 4.10 (writing)

*Inventory row W3 Consolidate.* In 300 words, give the main matter-wave-interferometry gain for Harrowmere's Greystock reservoir embankment survey, using all six parts of F1. Cover sensitivity, noise, long-term accuracy and practical aspects. Use only the fact-sheet figures (all fictional): suspected void signal about 5 µGal; 150 survey stations; installed relative spring meter at 8 µGal/√Hz, drift 30 µGal/day, 14 kg; candidate portable atom gravimeter, absolute, 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation. The new question: Harrowmere wants to repeat the survey a year from now and tell, station by station, whether the anomaly has changed.

**Hint:** This is a change between two surveys, so the two survey errors add in quadrature. For a 5 µGal change at SNR 3, each survey needs $\sigma \le 5/(3\sqrt2)$ per station. Turn that into averaging time per station for each instrument ($t = (S/\sigma)^2$, Move M7.5), then into hours per survey. Then ask what a year of 30 µGal/day drift does to a relative meter, and what "absolute" buys instead. Finish with one honest caveat.

**Model paragraph:**
(1) *Classical limit.* Harrowmere's question is a change, not a detection: is the roughly 5 µGal anomaly under the Greystock embankment (fictional) different a year from now? Two surveys are compared, so to see a 5 µGal change at SNR 3 each needs about 1.2 µGal per station. The installed spring meter (8 µGal/√Hz, fictional) gets there in about 46 s per station, under 2 hours of averaging for all 150 stations. Its weakness is not noise but that it is relative: at 30 µGal/day (fictional) a year of drift is about $1.1\times10^{4}$ µGal, over 2,000 times the signal. Each survey must therefore be tied to a base station whose own gravity is simply assumed unchanged, on a structure where ground movement is the very thing being tested (judgement). (2) *Mechanism.* An atom gravimeter splits, reflects and recombines free-falling atoms with three laser pulses; the phase $\Phi = k_\text{eff}gT^2$ depends on a laser wavelength and a time. (3) *Figure of merit.* Absolute repeatability over a year, with noise in µGal/√Hz setting the time per station. (4) *Gain.* Readings a year apart compare directly, with no base-station assumption and negligible drift (fictional). The price is noise: at 30 µGal/√Hz (fictional) each station needs about 648 s (10.8 min), so all 150 stations take about 27 hours of averaging per survey. (5) *Maturity and practicality.* The candidate is a portable product, but it weighs 110 kg against 14 kg, nearly 8 times more, and needs vibration isolation set up at every station. (6) *Verdict.* Use the atom gravimeter as the absolute reference on the stations that matter: re-occupying 20 stations over the anomaly costs about 3.6 hours of averaging, while the spring meter covers the full grid tied to those absolute points. The caveat: 30 µGal/√Hz is a specification; the embankment's own vibration, not the physics, will set what Harrowmere actually gets.

**What a weak answer misses:** It skips part (1)'s number, so the "gain" floats free. It confuses noise (µGal/√Hz, improves with averaging) with drift (µGal per day, does not average away). It claims the atom gravimeter is quieter, when on these figures the spring meter is about 4 times quieter. It brings in lecture lab figures or the $10^{10}$ Sagnac ratio (about rotation) instead of Harrowmere's own numbers, and it has no caveat, or a caveat with no number.

## Anti-patterns / Common mistakes

- **Using the lecture's $\tau = 2T$ with the standard formula.** How you'd notice: your phase is exactly 4× a textbook value. Instead: write "$\Phi = k_\text{eff}gT^2$, $T$ = time between pulses" every time, and flag L105-110.
- **Using $k$ instead of $k_\text{eff}$.** How you'd notice: your phase or recoil is half the expected value. Instead: counter-propagating Raman beams give $k_\text{eff}\approx2k = 4\pi/\lambda$.
- **Calling $\alpha = g$.** How you'd notice: the units do not match (Hz/s against m/s²). Instead: the chirp null is $\alpha_0 = k_\text{eff}g/2\pi$ (L91 erratum).
- **Quoting the $10^{10}$ Sagnac ratio as the real advantage.** How you'd notice: no mention of area or flux. Instead: walk it down through the area factor ($\sim10^{7}$) and the $\sqrt{\text{flux}}$ factor ($\sim10^{6}$), and say what is left.
- **Mixing noise, drift and accuracy.** How you'd notice: a µGal/√Hz figure compared with a µGal/month figure. Instead: noise averages down as $1/\sqrt t$; drift and accuracy do not.
- **Comparing a lab atom record with a fielded classical product.** How you'd notice: the atom figure comes from a research paper, the classical one from a survey meter. Instead: compare like with like and state conditions (F3).
- **Copying "spring sensitivity $\propto 1/T^2$" (L135) without saying which quantity.** How you'd notice: it seems to contradict $\delta L = gT^2/4\pi^2$. Instead: the response (stretch per $\Delta g$) rises as $T^2$; the smallest detectable $\Delta g$ at fixed length resolution, $4\pi^2\delta L_\text{min}/T^2$, falls as $1/T^2$. Name the one you mean.
- **Treating µGal as $10^{-6}g$.** How you'd notice: answers off by $10^{3}$. Instead: $1\ \mu\text{Gal} = 10^{-8}\ \text{m/s}^2\approx10^{-9}g$.

## Done when

Without notes, in 40 minutes, you can do all of the following. Pass mark: 7 of 8.

1. Derive $I\propto\cos^2(\varphi/2)$ from two sine waves, showing the sum-to-product step.
2. Compute the recoil velocity and $k_\text{eff}$ for a given atom and wavelength.
3. Explain the $\pi/2$-$\pi$-$\pi/2$ sequence as splitter-mirror-splitter, using $P_b = \sin^2(\Omega_Rt/2)$.
4. Show that $z(0) - 2z(T) + z(2T) = -gT^2$ and state $\Phi = k_\text{eff}gT^2$ with $T$ defined.
5. Explain the factor 4 in Eq 3.1 and write the chirp null $\alpha_0 = k_\text{eff}g/2\pi$.
6. Go from $N$, $T$ and cycle time to a noise density in µGal/√Hz.
7. Compute $m\lambda c/h$ for an atom and explain, with numbers, why it shrinks to "a few orders".
8. Fill in the classical gravimeter table (type, absolute or relative, SWaP) and state the L135 and L99/L139 errata.

## Companion pointer and confusion log

Open `content/companions/week03_companion.md` (§3 notation and units, §4 errata). Read lecture L83-99 and L103-121 with Moves M7.3 to M7.7 beside you. Log every symbol you had to look up twice ($\tau$, $T$, $k_\text{eff}$, $\alpha$, $\Theta$) in your confusion log with the lecture line.

| Symbol or line | What confused me | Resolution |
|---|---|---|
| | | |
| | | |

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 03 (clocks and magnetometers).**
1. Write $P_b(t)$ for a resonant Rabi drive. What pulse areas give $P_b = \tfrac12$ and $P_b = 1$?
2. An optical transition at 429 THz and a microwave transition at 9.19 GHz both have a 1 Hz linewidth. By what factor is the optical $Q = \nu/\Delta\nu$ larger?
3. What is the flux quantum $\Phi_0 = h/2e$, in Wb?

**From Day 02 (sensor figures of merit).**
4. A sensor has $30\ \mu\text{Gal}/\sqrt{\text{Hz}}$. What is its noise after averaging 100 s?
5. With $N = 10^{4}$ particles, what are the shot-noise and Heisenberg phase limits?

**From Day 01 (units and F1).**
6. Convert 1 µGal to m/s², and name the six parts of F1.

*Answers.* 1. $P_b = \sin^2(\Omega_Rt/2)$; $\pi/2$ and $\pi$. 2. $429\times10^{12}/9.19\times10^{9}\approx4.7\times10^{4}$. 3. $2.07\times10^{-15}$ Wb. 4. $30/\sqrt{100} = 3\ \mu\text{Gal}$. 5. $1/\sqrt N = 10^{-2}$ rad and $1/N = 10^{-4}$ rad. 6. $10^{-8}\ \text{m/s}^2$; classical limit with a number, quantum mechanism, figure of merit, quantified gain, maturity and practicality, verdict with a caveat.

## Read next

- Abend et al., *Atom interferometry and its applications*, <https://arxiv.org/abs/2001.10976>. Read the introduction, the gravimeter section (Mach-Zehnder sequence, phase formula with $T$ as pulse spacing, noise sources) and the applications section.
- Cronin, Schmiedmayer and Pritchard, *Atom Interferometers*, <https://arxiv.org/abs/0712.3703>. Read the inertial sensing section only (gravimeters, gyroscopes and the Sagnac comparison). This is the review the lecture's Eq 3.1 and 3.2 come from.
