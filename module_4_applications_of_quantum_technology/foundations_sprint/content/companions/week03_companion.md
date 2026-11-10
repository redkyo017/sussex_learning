# Week 03 Companion - Quantum sensors part 2: Inertial forces (atom interferometry)

**Built on:** Day 02 (M2 noise density and averaging, M3 shot noise), Day 03 (M4 two-level system and pulse area), Day 04 (M6 interference, M7 atom interferometry)
**Feeds:** Portfolio (Assessment 2) through the Week 3 Consolidate piece. Nothing here is aimed at Assessment 1.

Line numbers `L..` refer to `week_3/week_3_lecture.md`. Figure numbers refer to `week_3/figures/fig3_N.png`. Read this alongside the lecture, not instead of it.

## 1. Read these first (Pass 0)

Before you read the lecture, know what the week asks you to do with it. Types only, no solutions.

1. **Explore quiz (4 MCQ):** spot an inertial force; pick an instrument that measures one; which QT type does magnetometry; which systems rely on precise timing. Answers: see the inventory key (`docs/problem_inventory.md`, Week 3 rows). Q1 is flagged there as arguable.
2. **Apply (forum, 200-300 words):** pick one application area of atom interferometry and argue why the quantum approach matters there. Type: F1 gain argument, short form.
3. **Live session 2:** quantum versus conventional sensors, with a tutor. Type: discussion; bring one number you could not reconcile (L99 vs L139 is a good one).
4. **Consolidate (portfolio, 300 words):** one or two advantages of a matter-wave sensor over a classical limitation, with quantified measures (sensitivity, noise, long-term accuracy) and practical aspects. Type: F1 gain argument with numbers from M2, M3 and M7.
5. **Checkpoint quiz:** the same four questions as Explore with the options shuffled. See the inventory key.
6. **End of week:** Assessment 1 submission. Out of scope for this companion.

The quantitative side the week expects of you is small: compute a phase or a sensitivity from $\Phi = k_\mathrm{eff} g T^2$, turn a noise density into "how long to reach X µGal", and explain why a 10¹⁰ ratio shrinks to "a few orders". Sections 4-6 drill exactly that.

## 2. What the lecture is doing, in one picture

Light interferometers turn a path difference into a brightness change: $\cos^2(\varphi/2)$. Atoms are waves too, so the lecture swaps the roles. Laser pulses become the beam splitters and mirrors, and a cloud of cold atoms becomes the thing that travels the two arms. Each laser pulse kicks part of each atom upward by a photon recoil and also "stamps" the laser's local phase onto it. If the atoms fall under gravity while this happens, the stamps at the three pulses no longer cancel, and what is left over is a phase proportional to $g$ and to the square of the time between pulses: $\Phi = k_\mathrm{eff} g T^2$. The rest of the lecture is about how good that is in practice (noise density, drift, size, cost), comparing it with spring, superconducting and falling corner cube gravimeters, and listing where it is used.

The lecture never derives $\Phi = k_\mathrm{eff} g T^2$, and the one formula it does print (Eq 3.1) uses a convention that makes the answer four times too big. Section 4E fixes both.

Free reading if you want more than the lecture: Abend et al., *Atom interferometry and its applications*, https://arxiv.org/abs/2001.10976 (intro and gravimeter sections), and Cronin, Schmiedmayer, Pritchard, https://arxiv.org/abs/0712.3703 (inertial sensing section only).

## 3. Notation and unit decoder

Many symbols in this lecture mean two or three different things. The "clash" column is the reason this table exists.

| Symbol as written | Read it as | Unit | Where (lecture line) | Clash / trap | Move |
|---|---|---|---|---|---|
| $E_0\sin(\omega t)$ | electric field of the light in one arm | V/m | L26 | $E$ is also the Eötvös (L153) | M6 |
| $\varphi = \Delta n\,kL$ | optical phase difference: index difference × wavenumber × length | rad | L26, Fig 3.1 | $L$ means four different lengths this week | M6 |
| $k$ | wavenumber $2\pi/\lambda$ of one laser beam | rad/m (written m⁻¹) | L26, L64 | $k$ is the spring constant in L135 and Fig 3.7 | M6 |
| $\hbar\mathbf{k}$ | momentum of one photon | kg·m/s | L64 | bold means vector; the sign matters (see 4C) | M7 |
| $\mathbf{k}_\mathrm{eff} = \mathbf{k}_1-\mathbf{k}_2$ | effective wave vector of the Raman pair | m⁻¹ | L66, Fig 3.4 | for counter-propagating beams $\lvert\mathbf{k}_\mathrm{eff}\rvert \approx 2k$, not "nearly zero" | M7 |
| $\omega_1,\omega_2$, $\omega_\mathrm{eff}$ | angular frequencies of the two Raman beams; their difference drives a→b | rad/s | L52, L60, Fig 3.3 | $\hbar\omega$ is an energy, not a frequency | M4 |
| $\Delta$ (Fig 3.3a) | detuning of the virtual level from the excited level e | rad/s | L60 | not the same $\Delta$ as $\Delta p$, $\Delta n$, $\Delta g$ | M4 |
| $\Omega_R$ (Fig 3.3c) | Rabi frequency: how fast population swings a ↔ b | rad/s | Fig 3.3c | $\Omega$ in Eq 3.1 and L114 is the **rotation rate** of the instrument | M4 |
| $\pi/2$, $\pi$ pulse | pulse area $\Omega_R t$: 50:50 splitter, full swap (mirror) | rad (dimensionless) | L60 | a pulse "angle", not a geometric angle | M4 |
| $\lambda_\mathrm{dB} = h/p$ | de Broglie wavelength of the atom | m | L66, L114 | $\lambda_\mathrm{ph}$ in Eq 3.2 is the light's wavelength | M6 |
| $\Delta p = nh/d$ | momentum given by the $n$th diffraction order of a grating of period $d$ | kg·m/s | L66 | L66 calls $\Delta\mathbf{p}$ a "diffraction angle"; it is a momentum | M7 |
| $\Theta = \Delta p/p_\mathrm{beam}$ | diffraction **angle** (small-angle) | rad | L64 | L64 says "momentum changes by $\Theta$"; $\Theta$ is an angle | M7 |
| $T$ | time between successive pulses ($\pi/2$ at 0, $\pi$ at $T$, $\pi/2$ at $2T$) | s | L89, L91, L114, Fig 3.6 | also the pendulum period (L133) and the spring period (L135) | M7 |
| $\tau$ | the lecture's "total interrogation time" $= 2T$ | s | L110 | Eq 3.1 with $\tau$ is 4× the standard result; see 4E | M7 |
| $\alpha$ | chirp rate: how fast the Raman frequency difference is ramped | Hz/s | L91 | $\alpha$ is also the fine-structure constant (L181) and the spring angle in Fig 3.7 | M7 |
| $\Phi$ | interferometer phase (atoms) | rad | Eq 3.1, L114 | not magnetic flux (Week 2) | M7 |
| $a$, $g$ | acceleration; local gravitational acceleration ≈ 9.81 m/s² | m/s² | Eq 3.1, L91 | "$10^{-9}g$" uses $g$ as a **unit** | M1 |
| $\Omega$ | rotation rate of the instrument | rad/s | Eq 3.1, L114 | see $\Omega_R$ | M7 |
| $v$ | atom velocity between gratings | m/s | L110, Eq 3.2 | in Eq 3.2, $v$ appears via $\lambda_\mathrm{dB}v = h/m$ | M7 |
| $L$ | separation between gratings | m | L114 | also optical length (L26), pendulum length (L133), spring length (L135) | M7 |
| $A$ | area enclosed by the two paths | m² | L114, L121 | in a vertical gravimeter the "diamond" is in the $z$-$t$ plane and encloses no spatial area | M7 |
| $m$, $h$, $c$ | atom mass, Planck's constant, speed of light | kg, J·s, m/s | Eq 3.2 | $h/m$ for ⁸⁷Rb ≈ 4.6 × 10⁻⁹ m²/s | M7 |
| Gal, µGal | 1 Gal = 1 cm/s² = 0.01 m/s²; 1 µGal = 10⁻⁸ m/s² ≈ 1.0 × 10⁻⁹ $g$ | m/s² | L99, L123 | "5 µGal" and "$5\times10^{-9}g$" are the same size (L123) | M1 |
| µGal/√Hz, $g$/√Hz | noise **density**: divide by √(averaging time in s) to get the resolution | (m/s²)/√Hz | L99, L135, L163 | Week 2's "T√Hz" slip has the same shape; it is always "per" √Hz | M2 |
| $\Delta g/g$ | fractional change or uncertainty in $g$ | dimensionless | L133-L139 | multiply by 9.81 m/s² to get m/s² | M1 |
| /month, /year | drift rate of a relative meter | fractional per time | L135, L137 | drift adds linearly; it does not average down | M2 |
| E, mE | Eötvös: 1 E = 10⁻⁹ s⁻² (gravity gradient) | s⁻² | L153, L191 | E is also the electric field (L26) | M1 |
| $g$/m/√Hz | gradient noise density | s⁻²/√Hz | L153, L171 | $4\times10^{-9}\,g$/m/√Hz ≈ 39 E/√Hz | M1, M2 |
| rad/s/√Hz | rotation-rate noise density | (rad/s)/√Hz | L151, L171 | same reading rule as µGal/√Hz | M2 |
| $\hbar k_\mathrm{eff}$ per pulse | momentum given by one Raman pulse | kg·m/s | L167 | L167 says the pulses transfer "$2\hbar k_\mathrm{eff}$"; one pulse gives $\hbar k_\mathrm{eff} \approx 2\hbar k$ | M7 |

**Unit conversions you will use every time.** $1\,\mu\mathrm{Gal} = 10^{-8}\,\mathrm{m/s^2}$. $10^{-9}g = 9.81\times10^{-9}\,\mathrm{m/s^2} \approx 1\,\mu\mathrm{Gal}$. A noise density $S$ averaged for $t$ seconds gives resolution $S/\sqrt{t}$ (M2).

## 4. Skipped steps, expanded

Each item gives the lecture line, the gap, the missing lines and the move. Items E and F are the reason this companion exists.

### 4A. L26: why the Mach-Zehnder output is $\cos^2(\varphi/2)$ (M6)

The lecture jumps from the sum of two fields to $2I_0\cos^2(\varphi/2)$.

1. Sum-to-product: $\sin A + \sin B = 2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$. With $A = \omega t+\varphi$, $B = \omega t$: $E_0\sin(\omega t+\varphi)+E_0\sin(\omega t) = 2E_0\cos(\varphi/2)\,\sin(\omega t+\varphi/2)$.
2. Square: $4E_0^2\cos^2(\varphi/2)\,\sin^2(\omega t+\varphi/2)$.
3. Time-average: a detector cannot follow light's oscillation, and the average of $\sin^2$ over a cycle is $\tfrac12$. Result: $2E_0^2\cos^2(\varphi/2)$.
4. Read $I_0$ as $E_0^2$ and this is the lecture's $2I_0\cos^2(\varphi/2)$. If you read $I_0$ as one arm's time-averaged intensity $E_0^2/2$, it is $4I_0\cos^2(\varphi/2)$. The **shape** is what matters: bright at $\varphi = 0$, dark at $\varphi = \pi$, one full fringe per $2\pi$ of phase.
5. The second output port (Fig 3.1 has two detectors) gets $\sin^2(\varphi/2)$. The two add to a constant, so no light is lost; it is moved between ports. Atom interferometers read out the same way: the fraction of atoms in state b is $\tfrac12(1-\cos\Phi)$ in the simplest model.

### 4B. L52-L60: three levels become two, and pulse area makes splitters and mirrors (M4)

1. Two lasers $\omega_1$, $\omega_2$ are both far detuned (by $\Delta$) from the excited level e (Fig 3.3a). The atom never really sits in e, so e can be "eliminated": the pair acts like one field at $\omega_\mathrm{eff} = \omega_1-\omega_2$ that drives a ↔ b directly (Fig 3.3b). This is the two-level system you met in Module 3 and Day 03.
2. Driven on resonance with Rabi frequency $\Omega_R$, the population in b after time $t$ is $P_b = \sin^2(\Omega_R t/2)$ (Day 03, M4). The lecture shows the curve (Fig 3.3c) but not the formula.
3. $\pi/2$ pulse: $\Omega_R t = \pi/2$ gives $P_b = \sin^2(\pi/4) = 0.5$. An atom starting in a ends in an equal superposition: a 50:50 **beam splitter**.
4. $\pi$ pulse: $\Omega_R t = \pi$ gives $P_b = \sin^2(\pi/2) = 1$. a → b and b → a: a **mirror**.
5. "The phase evolution ... only depends on the pulse duration" (L60) means: at fixed laser intensity $\Omega_R$ is fixed, so you choose $\pi/2$ or $\pi$ by choosing the pulse length. A $\pi$ pulse is twice as long as a $\pi/2$ pulse.

### 4C. L64-L66: recoil, $k_\mathrm{eff}$ and the minus sign (M7)

1. Every change from a to b is paired with a momentum kick, because the atom absorbs a photon from one beam and is stimulated to emit into the other. Momentum conservation: $\Delta\mathbf{p} = \hbar\mathbf{k}_1-\hbar\mathbf{k}_2 = \hbar\mathbf{k}_\mathrm{eff}$.
2. **The minus sign hides a factor 2.** The beams counter-propagate: $\mathbf{k}_1 = +k\,\hat{z}$, $\mathbf{k}_2 \approx -k\,\hat{z}$. So $\mathbf{k}_\mathrm{eff} = k\hat{z}-(-k\hat{z}) = 2k\hat{z}$, and $\lvert\mathbf{k}_\mathrm{eff}\rvert \approx 2k$. If you read $k_1-k_2$ as a difference of two nearly equal magnitudes, you get almost zero, which is wrong.
3. Fig 3.4's story ("a photon from each beam absorbed, two of beam 2 emitted") gives the same vector sum, $\hbar\mathbf{k}_1+\hbar\mathbf{k}_2-2\hbar\mathbf{k}_2 = \hbar(\mathbf{k}_1-\mathbf{k}_2)$. The simpler standard picture is one absorbed from beam 1 and one emitted into beam 2.
4. Size, for ⁸⁷Rb at 780 nm (typical values, the lecture does not state them): $k = 2\pi/\lambda = 8.06\times10^6\ \mathrm{m^{-1}}$, $k_\mathrm{eff} = 1.61\times10^7\ \mathrm{m^{-1}}$. Two-photon (Raman) kick velocity $\hbar k_\mathrm{eff}/m = 11.8$ mm/s; the single-photon recoil velocity $\hbar k/m$ is half that, 5.9 mm/s. Say which one you mean. After $T = 160$ ms the two arms are $11.8\ \mathrm{mm/s}\times0.16\ \mathrm{s} = 1.9$ mm apart. Small, which is why Fig 3.6 is a stretched cartoon.
5. **Two labelling slips.** L66 says "the resulting diffraction angles are $\Delta\mathbf{p} = \hbar\mathbf{k}_\mathrm{eff}$". $\Delta\mathbf{p}$ is a momentum. The angle is $\Theta = \Delta p/p_\mathrm{beam}$ (L64). L64 in turn says the momentum "changes by $\Theta$", which is the angle again. Read them as: momentum kick $\hbar k_\mathrm{eff}$; deflection angle $\hbar k_\mathrm{eff}/p_\mathrm{beam}$. For a grating, $\Delta p = nh/d$ so $\Theta = n\lambda_\mathrm{dB}/d$.
6. L167 says the standard sequence transfers "$2\hbar k_\mathrm{eff}$". One Raman pulse transfers $\hbar k_\mathrm{eff}$ (that is, about $2\hbar k$). Read L167 as "$2\hbar k$".

### 4D. L91: the chirp null is $\alpha = k_\mathrm{eff}g/2\pi$, not "$\alpha = g$" (M7, erratum)

1. A falling atom sees the counter-propagating beams Doppler-shifted. At time $t$ its velocity has changed by $-gt$, so the resonance shifts by $k_\mathrm{eff}gt$ (in rad/s).
2. To keep the pulses resonant, the lab ramps the frequency difference of the two beams at rate $\alpha$ (Hz/s), which is $2\pi\alpha$ in rad/s².
3. Doppler shift and chirp cancel when $2\pi\alpha = k_\mathrm{eff}g$, so $\alpha = k_\mathrm{eff}g/2\pi$. With the chirp included the phase becomes $\Phi = (k_\mathrm{eff}g-2\pi\alpha)T^2$, which is zero at the same $\alpha$ for every $T$. That is how the experiment finds $g$: scan $\alpha$, find the fringe that does not move when $T$ changes.
4. "$\alpha = g$" cannot be right: $\alpha$ is in Hz/s, $g$ in m/s². Read the lecture as "$\alpha$ is proportional to $g$".
5. Size for ⁸⁷Rb: $\alpha = 1.61\times10^7\times9.81/2\pi = 2.52\times10^7$ Hz/s, about 25 MHz/s. A waveform generator can set this to many digits, which is why "finding $\alpha$" measures $g$ precisely.
6. Also in L91: "$T = 160\ ms$ ms" has a doubled unit. It is 160 ms.

### 4E. The core missing derivation: $\Phi = k_\mathrm{eff} g T^2$, and reconciling Eq 3.1 (M7, erratum, verified)

The lecture shows the pulses (Fig 3.6, L83-L89) and then jumps to Eq 3.1. Here are the missing lines, at concept level. This is the standard result (Cronin et al., inertial sensing section; Abend et al., gravimeter section).

1. **Rule: each pulse stamps the laser phase.** When a pulse changes an atom's state, the atom picks up the phase of the light at its position, $\phi = k_\mathrm{eff}z(t_i)$ (plus a fixed laser offset that cancels). Sign: $+$ for a → b, $-$ for b → a.
2. **Bookkeeping over the two paths** (Fig 3.6 labels these $\phi_1^A$, $\phi_2^A$, $\phi_2^B$, $\phi_3^A$). Path A is kicked at $t = 0$ and returned at $T$. Path B is kicked at $T$. At $2T$ the paths recombine and one is switched again. Adding the stamps with their signs, the phase difference at the output is
$$\Phi = \phi_1 - 2\phi_2 + \phi_3 = k_\mathrm{eff}\,[\,z(0) - 2z(T) + z(2T)\,].$$
For a uniform field the extra free-propagation phases of the two arms cancel, so this laser term is the whole answer (standard result; take it on trust, it is not examined).
3. **Insert free fall.** $z(t) = z_0 + v_0t - \tfrac12 gt^2$. Then
   - $z(0) = z_0$
   - $-2z(T) = -2z_0 - 2v_0T + gT^2$
   - $z(2T) = z_0 + 2v_0T - 2gT^2$
   
   Sum: the $z_0$ terms cancel ($1-2+1 = 0$), the $v_0$ terms cancel ($-2+2 = 0$), and the $g$ terms give $gT^2-2gT^2 = -gT^2$.
4. **Result.** $\Phi = -k_\mathrm{eff}gT^2$. The sign depends on which way $\mathbf{k}_\mathrm{eff}$ points; the size is $\lvert\Phi\rvert = k_\mathrm{eff}gT^2$.
5. **Why this is the right intuition.** $z(0)-2z(T)+z(2T)$ is a second difference: it equals $\ddot{z}\,T^2$ for any parabola. The interferometer is a ruler made of light that reads the atom's position three times and subtracts in a way that kills position and velocity and keeps only acceleration. Starting height, launch speed and the recoil kick do not matter, to this order.
6. **Size** (⁸⁷Rb, $T = 160$ ms, the value at L91): scale factor $k_\mathrm{eff}T^2 = 1.61\times10^7\times0.0256 = 4.12\times10^5$ rad per m/s². Total phase $\Phi = 4.12\times10^5\times9.81 = 4.05\times10^6$ rad. You never read that number directly; the chirp (4D) removes almost all of it and the fringe measures what is left.
7. **Reconciling Eq 3.1 (L105-L110).** The lecture writes $\Phi = k_\mathrm{eff}a\tau^2$ and defines $\tau = 2T$. Substituting: $k_\mathrm{eff}a(2T)^2 = 4k_\mathrm{eff}aT^2$, four times the result above. For our numbers the lecture's convention would give $1.62\times10^7$ rad instead of $4.05\times10^6$ rad. **The correct form is $\Phi = k_\mathrm{eff}aT^2 + 2k_\mathrm{eff}(\Omega\times v)T^2$ with $T$ the time between pulses.** The lecture's own L114 ($2\Omega k_\mathrm{eff}LT$, $T$ = time between gratings) agrees with this $T$ convention, so Eq 3.1 is the odd one out. In your own writing, always say which $T$ you mean.

### 4F. L110: why the rotation phase is linear in $\tau$ (M7)

1. In a beam (space-domain) interferometer the atoms fly at speed $v$ through gratings a distance $L$ apart, so $vT = L$.
2. Rotation term: $2k_\mathrm{eff}\Omega vT^2 = 2k_\mathrm{eff}\Omega(vT)T = 2k_\mathrm{eff}\Omega LT$. At fixed instrument length $L$, it grows only **linearly** in the time.
3. Acceleration term: $k_\mathrm{eff}aT^2$ has no $v$ in it, so it stays **quadratic**.
4. Consequence (L110): slow, cold atoms (large $T$ for a given $L$) win big for acceleration; fast thermal beams lose only linearly for rotation and bring far more atoms per second. That is why thermal-beam gyroscopes (L151) are competitive.

### 4G. L114: the Sagnac area step $A = L\cdot\hbar k_\mathrm{eff}T/m$ (M7)

1. After the first pulse one arm drifts sideways at the two-photon (Raman) kick velocity $\hbar k_\mathrm{eff}/m$. After time $T$ (at the mirror) the arms are $d = \hbar k_\mathrm{eff}T/m$ apart.
2. The paths form a diamond of length $2L$ and maximum width $d$. Its area is $\tfrac12\times2L\times d = Ld$, so $A = L\hbar k_\mathrm{eff}T/m$.
3. Check the lecture's equality: $4\pi\Omega mA/h = 4\pi\Omega m\,L\hbar k_\mathrm{eff}T/(m\,h) = 4\pi\Omega Lk_\mathrm{eff}T\,(\hbar/h) = 2\Omega k_\mathrm{eff}LT$, since $\hbar/h = 1/2\pi$. The two forms in L114 agree.
4. Trap: a vertical gravimeter (Fig 3.6) has arms separated in height only. Its "diamond" is drawn in the $z$-$t$ plane and encloses no spatial area, so it has no Sagnac response unless the instrument is tilted or moving sideways.

### 4H. L117: Eq 3.2 as a number, and why the practical gain is "a few orders" (M7, M3)

1. Divide the two L114 phases with equal areas: $\dfrac{\Phi_\mathrm{atom}}{\Phi_\mathrm{light}} = \dfrac{4\pi\Omega mA/h}{4\pi\Omega A/\lambda_\mathrm{ph}c} = \dfrac{m\lambda_\mathrm{ph}c}{h}$.
2. Equivalent form: $\lambda_\mathrm{dB}v = (h/mv)v = h/m$, so the ratio is also $\lambda_\mathrm{ph}c/(\lambda_\mathrm{dB}v)$, the lecture's last form. Light covers the loop at $c$, atoms at $v$; the atoms "feel" the rotation for longer.
3. Numbers (⁸⁷Rb at 780 nm, the usual case; the lecture gives none): $h/m = 4.59\times10^{-9}$ m²/s; $\lambda c = 780\times10^{-9}\times3.00\times10^8 = 234$ m²/s. Ratio $= 234/4.59\times10^{-9} = 5.1\times10^{10}$. The lecture's "≈ 10¹⁰" is right to an order of magnitude.
4. **Area penalty (L121).** A fibre gyroscope encloses about $10^3$ m²; a large atom interferometer about $10^{-4}$ m². That costs a factor $10^7$: $5.1\times10^{10}/10^7 = 5.1\times10^3$. This is the lecture's "only a few orders larger".
5. **Flux penalty (L121).** Phase noise at the shot-noise limit scales as $1/\sqrt{\text{count rate}}$ (M3). Photons: $10^{19}$/s per watt; atoms: $10^7$/s. Penalty $\sqrt{10^{19}/10^7} = 10^6$. On the lecture's round numbers the area and flux penalties eat almost all of the 10¹⁰: taken literally, $5.1\times10^3/10^6 \approx 5\times10^{-3}$, which would leave atoms behind on a pure shot-noise budget.
6. **But the inputs are not like-for-like (F3).** The $10^7$ atoms/s is a cold-atom figure, while rotation sensing uses thermal atomic beams with far higher flux (L103, L110). The $10^{19}$ photons/s assumes a full watt reaching a shot-noise-limited detector. Measured performance is the better guide: a thermal-beam atom gyroscope reached $6\times10^{-10}$ rad/s/√Hz (L151), and the lecture places atom inertial sensors comparable to, or better than, the best sensors of any technology (L103). So the 10¹⁰ is a response factor at equal area and flux, not a delivered gain; atoms add a scale factor fixed by $k_\mathrm{eff}$ and $h/m$, and good bias stability (judgement).
7. "(For acceleration ... $\propto (c/v)^2$)" in L121: acceleration phases go as time², and the time to cross a fixed length is $L/v$ for atoms and $L/c$ for light.

### 4I. L123: resolution = response × phase noise, and what "per √Hz" means (M2, M3)

1. Response: $\partial\Phi/\partial g = k_\mathrm{eff}T^2$ (from 4E). Resolution per shot: $\delta g = \delta\Phi/(k_\mathrm{eff}T^2)$.
2. Phase noise at the shot-noise limit with $N$ atoms: $\delta\Phi = 1/\sqrt{N}$ (M3). For $N = 10^6$ (the top of L93's range), $\delta\Phi = 10^{-3}$ rad.
3. Per shot: $\delta g = 10^{-3}/4.12\times10^5 = 2.4\times10^{-9}$ m/s² ≈ 0.24 µGal (⁸⁷Rb, $T = 160$ ms).
4. Per √Hz: averaging $n$ shots divides by $\sqrt{n}$. With one shot every $T_c$ seconds, $n = t/T_c$, so $\delta g(t) = \delta g_\mathrm{shot}\sqrt{T_c}/\sqrt{t}$. The noise density is $S = \delta g_\mathrm{shot}\sqrt{T_c}$, and "resolution after $t$ seconds" is $S/\sqrt{t}$. At 40 drops/min ($T_c = 1.5$ s): $S = 2.4\times10^{-9}\times\sqrt{1.5} = 3.0\times10^{-9}$ (m/s²)/√Hz ≈ 0.30 µGal/√Hz.
5. The **measured** figure at L99 is 20 µGal/√Hz, about 70 times worse. The instrument was limited by vibration, not by atom number. That gap is a good portfolio point: the quantum limit is far below what fielded instruments reach.
6. L123 check: at 20 µGal/√Hz, one minute gives $20/\sqrt{60} = 2.6$ µGal, below the 5 µGal that classical survey meters need 15 minutes for. Time to reach 5 µGal: $(20/5)^2 = 16$ s. The lecture's "less than 1 minute" is consistent.

### 4J. L99 vs L139: inconsistent noise figures for the corner cube meter (erratum, flag)

1. L99 quotes the falling corner cube meter at 5 µGal/√Hz in ideal conditions (60 drops/min).
2. L139 quotes the same class of instrument at $\Delta g/g \approx 5\times10^{-8}$/√Hz, which is $5\times10^{-8}\times9.81 = 4.9\times10^{-7}$ (m/s²)/√Hz ≈ 49 µGal/√Hz. That is ten times worse.
3. One possible reading: L99 is a best-case spec; L139 a typical value. Another: at the normal 4 drops/min instead of 60, the density rises by $\sqrt{15} = 3.9$, giving about 19 µGal/√Hz, which is neither. **Do not quote either without saying which conditions it is for.** For portfolio use, take the figure from a primary source with the date and conditions (F3).
4. Unit check on L135 and L137 while you are here: $5\times10^{-9}g$/√Hz ≈ 4.9 µGal/√Hz (spring); $10^{-12}g$/√Hz ≈ 0.001 µGal/√Hz (superconducting).

### 4K. L135: spring sensitivity rises as $T^2$, it does not fall as $1/T^2$ (erratum)

1. Equilibrium: $k\,\delta L = mg$, so $\delta L = mg/k$.
2. Period: $T = 2\pi\sqrt{m/k}$, so $m/k = T^2/4\pi^2$. Hence $\delta L = gT^2/4\pi^2$.
3. Sensitivity (stretch per unit change in $g$): $\mathrm{d}(\delta L)/\mathrm{d}g = T^2/4\pi^2$. It **rises** as $T^2$: a softer, slower spring stretches more for the same change in $g$.
4. Size: $T = 1$ s gives $1/4\pi^2 = 0.025$ m per m/s², so a 1 µGal change stretches the spring by $2.5\times10^{-10}$ m. That tiny length is why zero-length springs and long levers (Fig 3.7, left) are used.
5. The lecture's "$\propto 1/T^2$" is true of the **smallest detectable** $\Delta g$ for a fixed length resolution. Same physics, opposite quantity. Say which one you mean.
6. Note the $T$ here is a spring period, not the interferometer $T$. Same letter, same $T^2$ scaling, different object.

### 4L. L191: the $T^2$ gain, ground versus space (M7)

1. Phase per unit $g$ is $k_\mathrm{eff}T^2$, so sensitivity improves as $T^2$ (4E).
2. Ground: a few hundred ms, say $T = 0.3$ s. Space: $T$ up to 10 s (L191). Gain $(10/0.3)^2 = 1.1\times10^3$, about $10^3$.
3. Why the ground is limited: in a fountain the atoms rise and fall for $2T$, reaching a height $\tfrac12gT^2$. For $T = 0.3$ s that is 0.44 m; for $T = 10$ s it would be 490 m. The 10 m tower at L163 corresponds to $T = \sqrt{2\times10/9.81} = 1.43$ s.
4. Caveat (judgement): longer $T$ means fewer shots per second and a colder, sparser cloud (L159), so the per-√Hz gain is smaller than $10^3$ unless the cycle rate is kept up.

### 4M. Smaller decodes

- L133: the pendulum period $T = 2\pi\sqrt{L/g}$ and its $10^{-4}$ accuracy are history; the $T$ here is a period again.
- L147: "agreement with the falling corner cube measurement of $\sim10^{-8}$" means a fractional difference $\Delta g/g \sim 10^{-8}$.
- L153: gradiometer sensitivity $4\times10^{-9}g$/m/√Hz $= 4\times10^{-9}\times9.81$ s⁻²/√Hz $= 3.9\times10^{-8}$ s⁻²/√Hz ≈ 39 E/√Hz. The "10 E" is an accuracy, not a noise density.
- L91: "determines local gravity to $10^{-9}g$ accuracy" is about 1 µGal.
- L185: "precision of $1.4\times10^{-4}$" for $G$ is fractional.

## 5. Clones

These have the same type as the week's quantitative content and its Consolidate task, but use a different atom, different times and different instruments. Do them after the lecture, before the cold attempt in §6.

### Exercise C3.1 (quantitative)

A caesium-133 atom gravimeter uses Raman beams at $\lambda = 852$ nm in the counter-propagating geometry, with pulse spacing $T = 85$ ms. Take $g = 9.81$ m/s². Find (a) $k_\mathrm{eff}$; (b) the scale factor $k_\mathrm{eff}T^2$ and the total phase $\Phi$; (c) the phase change caused by a 50 µGal drop in gravity; (d) the chirp rate that nulls the phase; (e) what you would get with the "$\tau = 2T$" convention.

**Hint:** $k = 2\pi/\lambda$ and the counter-propagating pair doubles it. 1 µGal = 10⁻⁸ m/s². The chirp null is where $2\pi\alpha = k_\mathrm{eff}g$.

**Solution sketch:**
1. *Restate.* Given $\lambda = 852$ nm, $T = 0.085$ s, $g = 9.81$ m/s², $\Delta g = 5\times10^{-7}$ m/s². Want $k_\mathrm{eff}$, $k_\mathrm{eff}T^2$, $\Phi$, $\Delta\Phi$, $\alpha$.
2. *Write state.* Three pulses $\pi/2$-$\pi$-$\pi/2$ at $0, T, 2T$; $\Phi = k_\mathrm{eff}gT^2$.
3. *Name move.* M7 (recoil, $k_\mathrm{eff}\approx2k$, $\Phi = k_\mathrm{eff}gT^2$, chirp null), M1 (units).
4. *Algebra.*
   - (a) $k = 2\pi/852\times10^{-9} = 7.37\times10^6$ m⁻¹, so $k_\mathrm{eff} = 1.47\times10^7$ m⁻¹.
   - (b) $T^2 = 7.225\times10^{-3}$ s². $k_\mathrm{eff}T^2 = 1.07\times10^5$ rad per m/s². $\Phi = 1.07\times10^5\times9.81 = 1.05\times10^6$ rad.
   - (c) $\Delta\Phi = 1.07\times10^5\times5\times10^{-7} = 0.053$ rad, about 53 mrad.
   - (d) $\alpha = k_\mathrm{eff}g/2\pi = 1.47\times10^7\times9.81/2\pi = 2.30\times10^7$ Hz/s, about 23 MHz/s.
   - (e) With $\tau = 2T$: $4\times1.05\times10^6 = 4.18\times10^6$ rad, four times too large.
5. *Check.* Units: m⁻¹ × m/s² × s² = rad. Order: Cs is heavier and its wavelength longer than the textbook Rb case, and $T$ is about half, so $\Phi$ should be roughly four times smaller than a Rb, 160 ms instrument; it is. 53 mrad is a measurable fringe shift for a phase noise of a few mrad.
6. *Answer.* $k_\mathrm{eff} = 1.47\times10^7$ m⁻¹; scale factor $1.07\times10^5$ rad/(m/s²); $\Phi = 1.05\times10^6$ rad; a 50 µGal anomaly shifts the phase by 53 mrad; chirp null at 23 MHz/s.

The habit to keep: compute the scale factor $k_\mathrm{eff}T^2$ first, because every sensitivity question is that number times a $\Delta g$.

### Exercise C3.2 (quantitative)

The caesium instrument of C3.1 detects $N = 4\times10^5$ atoms per shot and runs one shot every 0.5 s. (a) Find its shot-noise-limited resolution per shot and its noise density in µGal/√Hz. (b) In the field it is vibration-limited at 40 µGal/√Hz. A classical relative spring meter on the same site has 6 µGal/√Hz noise and drifts by 15 µGal per day. How long does each instrument need to average down to 5 µGal, and after how many hours does the spring meter's drift alone reach 5 µGal?

**Hint:** $\delta\Phi = 1/\sqrt{N}$; divide by the scale factor; multiply by $\sqrt{T_c}$ for the density. Time to reach a resolution $R$ from density $S$ is $(S/R)^2$. Drift adds linearly and does not average away.

**Solution sketch:**
1. *Restate.* Given $N = 4\times10^5$, $T_c = 0.5$ s, scale factor $1.07\times10^5$ rad/(m/s²) from C3.1, field density 40 µGal/√Hz, spring 6 µGal/√Hz and 15 µGal/day. Want shot-noise floor, two averaging times, a drift time.
2. *Write state.* $\delta g_\mathrm{shot} = (1/\sqrt{N})/(k_\mathrm{eff}T^2)$; $S = \delta g_\mathrm{shot}\sqrt{T_c}$; $t_R = (S/R)^2$; drift time $= R/(\text{drift rate})$.
3. *Name move.* M3 (shot noise), M2 (density and $1/\sqrt{t}$), M7 (scale factor).
4. *Algebra.*
   - (a) $\delta\Phi = 1/\sqrt{4\times10^5} = 1.58\times10^{-3}$ rad. $\delta g_\mathrm{shot} = 1.58\times10^{-3}/1.07\times10^5 = 1.48\times10^{-8}$ m/s² $= 1.48$ µGal. $S = 1.48\times\sqrt{0.5} = 1.05$ µGal/√Hz.
   - (b) Atom, field: $(40/5)^2 = 64$ s. Spring: $(6/5)^2 = 1.44$ s. Spring drift: $15/24 = 0.625$ µGal per hour, so it reaches 5 µGal after $5/0.625 = 8$ hours.
5. *Check.* The field figure (40) is about 38 times the shot-noise floor (1.05), so the atoms are not the limit; vibration is. The spring meter is quieter in the short term, as real spring meters are.
6. *Answer.* Shot-noise floor 1.5 µGal per shot, 1.05 µGal/√Hz. In the field the atom meter needs about a minute per 5 µGal reading; the spring meter needs seconds but its drift exceeds 5 µGal after 8 hours, so a long survey must keep returning to a base station.

The comparison that matters is never "noise density versus noise density": it is short-term noise against long-term drift, over the length of the job.

### Exercise C3.3 (quantitative)

A caesium beam gyroscope (atoms, 852 nm Raman light) is compared with a fibre-optic gyroscope. (a) Compute the ideal Sagnac ratio $m\lambda c/h$. (b) The atom loop encloses $5\times10^{-5}$ m², the fibre coil 200 m². What is the ratio after the area penalty? (c) The atom beam delivers $10^8$ atoms/s; the light $10^{18}$ photons/s. Include the shot-noise flux penalty and state the verdict.

**Hint:** $h/m$ for caesium uses $m = 133$ u (1 u $= 1.66\times10^{-27}$ kg). Area enters the phase linearly; count rate enters the phase noise as a square root.

**Solution sketch:**
1. *Restate.* Given $\lambda = 852$ nm, Cs mass, areas $5\times10^{-5}$ and 200 m², rates $10^8$ and $10^{18}$ per second. Want the ideal ratio and two corrected ratios.
2. *Write state.* $\Phi_\mathrm{atom}/\Phi_\mathrm{light} = m\lambda c/h$ at equal area; multiply by $A_\mathrm{atom}/A_\mathrm{light}$; divide by $\sqrt{R_\mathrm{light}/R_\mathrm{atom}}$.
3. *Name move.* M7 (Sagnac ratio), M3 (shot noise $1/\sqrt{N}$).
4. *Algebra.*
   - (a) $m = 2.21\times10^{-25}$ kg, $h/m = 3.00\times10^{-9}$ m²/s. $\lambda c = 852\times10^{-9}\times3.00\times10^8 = 255$ m²/s. Ratio $= 255/3.00\times10^{-9} = 8.5\times10^{10}$.
   - (b) Area ratio $200/5\times10^{-5} = 4\times10^6$. $8.5\times10^{10}/4\times10^6 = 2.1\times10^4$.
   - (c) Flux penalty $\sqrt{10^{18}/10^8} = 10^5$. $2.1\times10^4/10^5 = 0.21$.
5. *Check.* Heavier atom than Rb, so $h/m$ smaller and the ideal ratio larger ($8.5\times10^{10}$ versus about $5\times10^{10}$): consistent. Each correction is dimensionless.
6. *Answer.* Ideal ratio $8.5\times10^{10}$; about $2\times10^4$ after area; about 0.2 on a pure shot-noise budget, on these assumed numbers. That is not a verdict: the real outcome depends on the flux and area actually achieved (a thermal beam can deliver far more atoms per second, L110), so for a real comparison cite a measured figure, such as the thermal-beam atom gyroscope's $6\times10^{-10}$ rad/s/√Hz (L151), against a fibre gyroscope measured the same way (judgement).

So "10¹⁰" is a response factor at equal area and equal flux, not a delivered gain. Neither is ever equal, and you should say so whenever you quote it.

### Exercise C3.4 (writing)

Harrowmere Water & Power (fictional) must survey the 150 stations (fictional) on its Greystock reservoir embankment, where it suspects a void with a signal of about 5 µGal (fictional), and repeat the survey every month. The options are its installed relative spring meter (8 µGal/√Hz, drift 30 µGal/day, 14 kg; fictional) and a portable atom gravimeter (absolute, 30 µGal/√Hz, negligible drift, 110 kg, needs vibration isolation; fictional). Assume (fictional, for this exercise only) a 7 h working day, 15 min to move and level the atom gravimeter with its vibration isolation at each station, and 5 min per station for the spring meter. Each station needs 2 µGal resolution. Write a 150-200 word F1 gain argument: how many stations per day can each instrument do, and what does that mean for a monthly repeat?

**Hint:** Work out three numbers before writing: averaging time per station for each instrument to reach 2 µGal, $t = (S/2)^2$; stations per day including set-up; and the spring meter's drift over a 2-hour base-station loop and over a month. Then fill the six F1 slots. The honest caveat is throughput and robustness.

**Model paragraph:** Harrowmere must resolve 2 µGal per station on a roughly 5 µGal void signal across 150 stations each month (fictional figures). The installed spring meter is quiet: at 8 µGal/√Hz it needs only 16 s per station, so about 79 stations a day and the grid in two days. But it is relative and drifts 30 µGal a day: a 2-hour base-station loop already carries 2.5 µGal, more than the 2 µGal target, so loops must close within about 1.6 hours, and a month of drift is 900 µGal that must be removed before one month can be compared with the next. An atom gravimeter is absolute: three light pulses time free-falling atoms, so $\Phi = k_\mathrm{eff}gT^2$ ties each reading to a laser wavelength and a clock, with negligible drift. The figure of merit is absolute repeatability month to month. The cost is throughput: at 30 µGal/√Hz it needs 225 s per station, and with 15 min of set-up for a 110 kg instrument that is about 22 stations a day, roughly 7 days per survey. Verdict: use the atom meter on the stations over the suspected void as an absolute monthly reference and the spring meter for the full grid; the caveat is that site vibration may make 30 µGal/√Hz optimistic.

**What a weak answer misses:** It quotes "10¹⁰ times more sensitive" (a response factor at equal area, irrelevant here). It compares noise densities without converting to time per station and stations per day. It ignores drift, which is the real classical limitation over a monthly repeat. It omits the 110 kg and vibration-isolation logistics. It forgets to label the invented figures as fictional.

## 6. Cold attempt

Attempt this on paper before opening the sketch. Same type as §5, fresh numbers.

### Exercise C3.5 (quantitative)

A potassium-39 atom gravimeter uses 767 nm Raman light. On the ground in a fountain it runs at $T = 0.2$ s. A proposed microgravity version would run at $T = 4$ s. (a) Find $k_\mathrm{eff}$ and the scale factor $k_\mathrm{eff}T^2$ for both. (b) What is the gain in phase per unit $g$? (c) How tall would a ground fountain need to be to reach $T = 4$ s? (d) What phase does a change of $10^{-9}g$ produce in each case? (e) Give one reason the per-√Hz gain will be smaller than (b).

**Hint:** Use $k_\mathrm{eff} \approx 2\cdot2\pi/\lambda$. Gain is $(T_2/T_1)^2$. A fountain of duration $2T$ rises to $\tfrac12gT^2$. $10^{-9}g = 9.81\times10^{-9}$ m/s².

**Do not open the sketch until you have a written attempt.**

**Solution sketch:**
1. *Restate.* Given $\lambda = 767$ nm, $T_1 = 0.2$ s, $T_2 = 4$ s, $\Delta g = 9.81\times10^{-9}$ m/s². Want two scale factors, their ratio, a height, two phases, a caveat.
2. *Write state.* $\Phi = k_\mathrm{eff}gT^2$; scale factor $k_\mathrm{eff}T^2$; apex height $h = \tfrac12gT^2$.
3. *Name move.* M7 ($T^2$ scaling, ground versus space), M1 (units).
4. *Algebra.*
   - (a) $k = 2\pi/767\times10^{-9} = 8.19\times10^6$ m⁻¹, $k_\mathrm{eff} = 1.64\times10^7$ m⁻¹. Ground: $1.64\times10^7\times0.04 = 6.55\times10^5$ rad/(m/s²). Microgravity: $1.64\times10^7\times16 = 2.62\times10^8$ rad/(m/s²).
   - (b) $(4/0.2)^2 = 400$.
   - (c) $\tfrac12\times9.81\times4^2 = 78.5$ m.
   - (d) Ground: $6.55\times10^5\times9.81\times10^{-9} = 6.4\times10^{-3}$ rad. Microgravity: $2.62\times10^8\times9.81\times10^{-9} = 2.57$ rad.
   - (e) The cycle is about 20 times longer, so there are fewer shots per second to average; the cloud expands for longer, so fewer atoms are detected and $\delta\Phi = 1/\sqrt{N}$ grows.
5. *Check.* Ratio of the two phases in (d): $2.57/6.4\times10^{-3} = 400$, matching (b). A phase above $\pi$ for $10^{-9}g$ means the space instrument must track which fringe it is on.
6. *Answer.* Scale factors $6.6\times10^5$ and $2.6\times10^8$ rad/(m/s²); gain 400; a ground fountain would need about 79 m; a $10^{-9}g$ change gives 6.4 mrad on the ground and 2.6 rad in microgravity; the real per-√Hz gain is smaller because of the slower cycle and atom loss.

If you got (b) right but (c) wrong, revisit the fountain picture in Fig 3.6: the atoms rise for $T$ and fall for $T$.

## 7. Confusion log prompts

Answer each in writing (two or three sentences) after your pass through the lecture. Log the answer in your confusion log with the date.

1. In your own words, why does $z(0)-2z(T)+z(2T)$ remove the launch velocity and the recoil kick but keep $g$? What would happen to the phase if the atoms also had a constant sideways velocity?
2. The lecture's Eq 3.1 and its L114 formula use different meanings of the time. Which one would you cite in the portfolio, and how will you state the convention so a reader cannot misread it by a factor of 4?
3. You are told an instrument has "20 µGal/√Hz". Write down, without notes, how long it needs to reach 2 µGal, and one reason a classical meter with a smaller number might still lose over a week-long survey.
4. (Optional) Which of L99 and L139 would you trust for a corner cube meter's noise, and what would you need to know before quoting either?

## 8. Figures

One note per figure: what to look at, what it shows, the lecture line, and the trap.

**Fig 3.1 (Mach-Zehnder interferometer, L26-L32).** Look at the red block in the lower arm labelled $\Delta\varphi = \Delta n\cdot kL$ and at the **two** detectors. The block adds an extra phase to one arm; the recombiner sends light to one detector or the other depending on that phase ($\cos^2(\varphi/2)$ to one, $\sin^2(\varphi/2)$ to the other, 4A). Trap: the lecture's formula describes one port only, and mirror phase shifts are ignored. Nothing is lost; light moves between the two outputs.

**Fig 3.2 (light-pulse atom interferometer, L40-L46).** Look at the state labels: $\lvert a,p_0\rangle$ in, then $\lvert a,p_0\rangle$ and $\lvert b,p_0+\Delta p\rangle$ after the splitter, swapped by the mirror, overlapped at the recombiner. Internal state and momentum are locked together: being in b means having the extra kick. Trap: the light gratings are drawn as stationary columns in space, so the horizontal axis here is distance along the beam (a space-domain picture), unlike Fig 3.6, where it is time. Also, the outputs are two arrows; the interference shows up as how many atoms leave in each.

**Fig 3.3 (Raman transition, L52-L60).** (a) Two laser arrows $\omega_1$ up and $\omega_2$ down via a dashed virtual level a distance $\Delta$ below e. (b) The same thing as one effective transition $\omega_\mathrm{eff}$. (c) Rabi oscillations: solid line a, dotted line b, crossing at 0.5. Trap: the horizontal axis is labelled "t[1/Ω_R]", but the tick labels $\pi/2$, $\pi$, $2\pi$ are the pulse area $\Omega_Rt$. Read the $\pi/2$ tick as "50:50, splitter" and the $\pi$ tick as "complete swap, mirror". The unlabelled tick between $\pi$ and $2\pi$ is $3\pi/2$. Also, the $\Omega_R$ here is not the rotation $\Omega$ of Eq 3.1.

**Fig 3.4 (momentum transfer, L64, L68-L72).** Look at the arrows and the final momentum $p = \hbar(k_1-k_2) = \hbar k_\mathrm{eff}$. The atom ends in $\lvert b\rangle$ moving right. Trap: the formula is a vector difference. The beams point in opposite directions, so the magnitudes add, $\lvert k_\mathrm{eff}\rvert \approx 2k$ (4C). Read "$k_1-k_2$" as a scalar difference and you would conclude the kick is almost zero.

**Fig 3.5 (Kapitza-Dirac versus Bragg, L74-L79).** Left: a thin grating (short pulse) fans the beam into many orders. Right: a thick grating (long pulse) at the right angle gives only the 0th and 1st order, which is what a clean two-path interferometer needs. Trap: "Mirror" labels the retro-reflecting optic that makes the standing wave of light, not the atom-optics "mirror" ($\pi$ pulse) of Figs 3.2 and 3.6. The arrow $\hat{x}$ marks the grating direction.

**Fig 3.6 (gravimeter space-time diagram, L83-L91).** Look at the axes first: horizontal is time $t$ (pulses at 0, $T$, $2T$), vertical is height $z$. The diamond is not a shape in space; it is two height-versus-time histories. The straight lines are the trajectories without gravity and the curved lines those with gravity (L83), bent downward by $\tfrac12gt^2$. The labels $\phi_1^A$, $\phi_2^A$, $\phi_2^B$, $\phi_3^A$ are the laser-phase stamps that combine into $\Phi = \phi_1-2\phi_2+\phi_3$ (4E). The question marks at the outputs say: which port each atom leaves by depends on that phase. Trap: the diagram's enclosed "area" is in the $z$-$t$ plane, so there is no Sagnac area (4G). And the time between pulses is $T$, not $2T$; the whole sequence lasts $2T$ (L95).

**Fig 3.7 (classical gravimeters, L125-L139).** Three panels. Left: a zero-length spring meter, $g = yk/m$: a relative meter reading a length. Middle: a superconducting sphere levitated over a coil in liquid helium, $g$ read from the coil voltage: relative, very stable, not portable. Right: a falling corner cube in one arm of a laser interferometer; the fringe signal chirps (the zero crossings $T_1$, $T_2$, $T_3$ get closer) as the cube speeds up, and the chirp rate gives $g$ absolutely. Trap: the right panel is the classical twin of the atom chirp in 4D; both measure $g$ from a chirp, one with a falling mirror, one with falling atoms. Also, the $k$ and $L$ in the spring panel are a spring constant and a spring length, not a wavenumber and a grating separation. The "t = t_{final}" label is a typesetting slip for $t = t_\mathrm{final}$.
