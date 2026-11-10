# Glossary — Module 4 Foundations Sprint

Notation and units in one place. Each row is: symbol or term | what it means, as the day files define it | unit ("—" for dimensionless or no unit) | where it is taught (Day and move or section, e.g. `04 M7.3`; `C4 §3` is the Week 4 companion's §3). A term sits under the day that defines it, in the order the days introduce them, so a term the module map names on Day 01 but Day 10 defines (TRL) is listed under Day 10. Values marked (judgement) or (typical) carry that label in the day file too. The A–Z index is at the end; the 20-minute retrieval sets at +7 and +21 days (README) are drawn from this page.

Conventions used throughout: $T$ in an atom interferometer is the **time between pulses** (the sequence lasts $2T$); noise densities are always **per** √Hz; $\Delta f$ is a bandwidth, so $B$ stays the magnetic field; decimal prefixes (1 kB = $10^3$ B).

## Frameworks and moves

| ID | Name | Day |
|---|---|---|
| F1 | Gain argument, six parts in order: classical limit with a number; quantum mechanism in one sentence; figure of merit named; quantified gain (like-for-like); maturity and practicality (TRL, SWaP-C, barriers); verdict with one honest caveat | 01 F1; STRATEGY §6 |
| F2 | Maturity lens: TRL 1-9 with evidence, the advantage test (L88), the five barriers, component TRL > system TRL | 10 F2.1-F2.3 |
| F3 | Credible numbers: source hierarchy; date, conditions, units; like-for-like ratios | 01 F3; 10 "F3 again" |
| M1 | Orders of magnitude, SI prefixes, module units (T, Gal, E, fractional); fractional error → time → distance via $c$ | 01 M1; 03 "M1 revisited" |
| M2 / M3 | Noise density, bandwidth, $1/\sqrt{t}$ averaging, Allan deviation / shot noise vs Heisenberg, SNR, distance gain | 02 |
| M4 / M5 | Two-level frequency reference ($E = h\nu$, $Q$, pulse area, lock loop) / magnetometers (Larmor, $\Phi_0$, NV) | 03 |
| M6 / M7 | Interference and matter waves / atom interferometry ($\hbar k$, $k_\text{eff}$, $\Phi = k_\text{eff} g T^2$, $T^2$, Sagnac) | 04 |
| M8 / M9 / M10 | Crypto in one page / BB84, QBER, no-cloning / CHSH, fibre loss, trusted node vs repeater | 06 |
| M11 | $2^N$ amplitudes and $8\cdot2^N$ bytes; analogue vs digital; $J$ vs $U$ | 07 |
| M12 | Gates and circuits, Bell state, phase kickback, Deutsch-Jozsa as an amplitude sum | 08 |
| M13 | Speed-up taxonomy, Grover, $F^g$ depth, error-correction overhead, threshold theorem | 09 |
| M14 | Benefit/risk: ranges, expected value, weakest assumption; fact-sheet anatomy | 10 |

## Day 01 — Module map, gain argument, credible numbers

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| four QT types; figure of merit | sensing, communication, simulation, computing (Week 7: maturity); the one number that defines "better" for each type (F1 part 3) | per type | 01 module map |
| Harrowmere Water & Power | the fictional utility used for all practice writing (shared fact sheet in STRATEGY) | — | 01 F1; STRATEGY |
| source hierarchy | peer-reviewed paper or national metrology institute > review > vendor datasheet > press release > market report | — | 01 F3 |
| like-for-like ratio | a gain whose two sides are measured the same way (lab vs lab, field vs field) | — | 01 F3 |
| SWaP-C | size, weight, power and cost: the practicality clause (F1 part 5) | kg, L, W, £ | 01 F1; 02 M2.2 |
| P, T, G, M, k / m, µ, n, p, f, a | SI prefixes $10^{15}$ … $10^{3}$ / $10^{-3}$ … $10^{-18}$; "T" is tera in "TB", tesla in "1 T" | — | 01 M1 |
| T (tesla) | magnetic field; Earth's field ≈ 50 µT (typical; 25-65 µT) | T | 01 M1 |
| Gal, mGal, µGal | 1 Gal = 1 cm/s² = $10^{-2}$ m/s²; 1 µGal = $10^{-8}$ m/s² ≈ $10^{-9}g$ | m/s² | 01 M1; 04 M7.8 |
| $g$ | local gravitational acceleration ≈ 9.81 m/s² ≈ 981 Gal; also used as a unit ("$10^{-9}g$") | m/s² | 01 M1 |
| E (Eötvös) | gravity gradient: 1 E = $10^{-9}$ s⁻² = $10^{-9}$ (m/s²) per m | s⁻² | 01 M1 |
| $y = \delta\nu/\nu$; $\delta g/g$ | fractional frequency error (offset) of a clock; fractional uncertainty of a clock or gravimeter | — | 01 M1 |
| $\delta t = y\,\tau$, $\delta x = c\,\delta t$ | clock chain: time error after running alone for $\tau$, then ranging error; $c$ = 299 792 458 m/s; 1 ns ↔ 0.30 m | s; m | 01 M1; 03 M1 rev. |
| parallelism myth | "a quantum computer does all calculations at once" (W1 L70); the gain is interference, then one measured outcome | — | 01 decode; 08 M12.4 |

## Day 02 — What makes a good sensor

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| precision | scatter of repeated readings (standard deviation); reduced only by averaging | unit of reading | 02 M2.1 |
| accuracy, bias | closeness of the mean to the true value; bias = mean − reference; removed by calibration | unit of reading | 02 M2.1 |
| resolution | (1) readout: smallest registrable change, e.g. one ADC LSB; (2) spatial: how close two sources can be told apart (the lecture's sense) | unit / m | 02 M2.1 |
| bandwidth, $f_c$, −3 dB point | signal frequency at which the response amplitude falls to $1/\sqrt2$ (half power); first-order model $\lvert H(f)\rvert = 1/\sqrt{1+(f/f_c)^2}$ (judgement) | Hz | 02 M2.2 |
| dynamic range; dB | full scale / noise floor; in amplitude dB, $20\log_{10}(\text{ratio})$ ($1/\sqrt2$ = −3.01 dB) | ratio or dB | 02 M2.2 |
| $S$ | amplitude noise spectral density (noise density) | unit/√Hz, e.g. T/√Hz | 02 M2.3 |
| $\Delta f$ | detection (noise) bandwidth you let through or average over; not the sensor's own −3 dB bandwidth | Hz | 02 M2.3; 05 warm-up |
| $\delta x = S\sqrt{\Delta f}$ | rms noise in bandwidth $\Delta f$ (white noise) | unit of reading | 02 M2.3 |
| $\delta x(\tau) \approx S/\sqrt{2\tau}$ | time form for averaging time $\tau$, with $\Delta f \approx 1/(2\tau)$ (convention; some drop the 2): noise $\propto 1/\sqrt\tau$ | unit of reading | 02 M2.3 |
| T/√Hz | tesla per root hertz; the lecture's "T√Hz" (L74) is a typo | T Hz⁻¹ᐟ² | 02 M2.3 |
| $\sigma_y(\tau)$ | Allan deviation: $\sigma_y^2 = \tfrac12\langle(\bar y_{k+1}-\bar y_k)^2\rangle$ over windows of length $\tau$ | — (fractional) | 02 M2.4 |
| Allan slopes | −1/2 white frequency noise (averaging helps); 0 flicker floor (stops helping); +1/2 or steeper random walk and drift (worse) | — | 02 M2.4 |
| $\delta\phi_\text{SQL} = 1/\sqrt N$ | standard quantum limit (shot or projection noise) for $N$ independent particles per shot; $n$ repeats give $1/\sqrt{Nn}$ | rad | 02 M3.1 |
| $\delta\phi_\text{HL} = 1/N$ | Heisenberg limit; needs entanglement; gain $\sqrt N$ over the SQL | rad | 02 M3.1 |
| SNR | signal amplitude / rms noise in the same bandwidth; $20\log_{10}$SNR in dB; detect at ≳3-5 (judgement) | — | 02 M3.2 |
| $(r_1/r_2)^n$ | distance gain moving from $r_1$ to $r_2$ for a $1/r^n$ source: $n$ = 1 line current, 2 current dipole (lecture Eq 2.1), 3 magnetic dipole | — | 02 M3.2 |

## Day 03 — Clocks and magnetometers

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| $E = h\nu$ | transition (photon) energy; $h = 6.626\times10^{-34}$ J s; Cs: $\nu$ = 9 192 631 770 Hz exactly | J, eV | 03 M4.1 |
| $Q = \nu/\Delta\nu$ | quality factor: transition frequency over linewidth (FWHM); at equal linewidth, higher $\nu$ → higher $Q$ (why optical beats microwave) | —; Hz | 03 M4.1 |
| $\Omega$ (Rabi) | Rabi frequency, set by drive strength; $H = \tfrac{\hbar\Omega}{2}\sigma_x$ on resonance | rad/s | 03 M4.2 |
| $\Omega t$, pulse area | $P_1(t) = \sin^2(\Omega t/2)$; π/2 pulse: $P_1 = 1/2$, beam splitter; π pulse: $P_1 = 1$, mirror | rad | 03 M4.2 |
| Ramsey, $T$, $\delta f$ | π/2 – free evolution for $T$ – π/2; linewidth $\Delta\nu \approx 1/(2T)$; $\delta f$ = detuning of drive from atom | s, Hz | 03 M4.2 |
| lock loop, $e$ | probe both sides of the line; error $e = P_1(-\Delta\nu/2) - P_1(+\Delta\nu/2)$; PI servo steers the oscillator | — | 03 M4.3 |
| holdover | the oscillator free-running with no atomic or satellite correction | — | 03 M4.3; 01 F1 |
| $f_n = n f_\text{rep} + f_\text{ceo}$ | frequency comb teeth; $\nu_\text{clock} = n f_\text{rep} + f_\text{ceo} + f_\text{beat}$ | Hz | 03 M4.4 |
| $f_L = \gamma B$ | Larmor frequency; $\gamma$ gyromagnetic ratio, ⁸⁷Rb ≈ 7 Hz/nT (7 GHz/T) | Hz | 03 M5.1 |
| OPM; SERF | optically pumped magnetometer: pump, precess at $f_L$, read with light (scalar OPM: total field). SERF: dense hot vapour near zero field; lowest noise, needs shielding, < 200 Hz bandwidth | — | 03 M5.1 |
| $\Phi_0 = h/2e$ | magnetic flux quantum ≈ $2.07\times10^{-15}$ Wb (lecture $\pi\hbar/q_e$); Eq 2.2 is $BS = n\Phi_0$ | Wb = T m² | 03 M5.2 |
| SQUID | superconducting loop whose voltage oscillates once per $\Phi_0$; needs cryogenics, costs standoff | — | 03 M5.2 |
| NV centre | diamond defect, spin-1 ($m_s = 0, \pm1$); $\pm1$ at 2.87 GHz; $\gamma_e \approx 28$ GHz/T (28 MHz/mT); dips at $2.87\ \text{GHz} \pm \gamma_e B$ | Hz | 03 M5.3 |
| fluxgate, BEC microscope | classical magnetometer (~100 pT/√Hz, L82); ultracold-atom field imager (~2 nT at ~100 nm, no per √Hz) | T/√Hz, T | 03 M5.4 |

## Day 04 — Interferometry to atom interferometry

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| $\varphi = \Delta n\,kL$; $k = 2\pi/\lambda$ | optical phase difference between Mach-Zehnder arms; wavenumber of one beam | rad; m⁻¹ | 04 M6.1 |
| $I \propto 2I_0\cos^2(\varphi/2)$ | Mach-Zehnder output; $\varphi = 0$ bright, $\pi$ dark; $I_0 = E_0^2$ | — (relative) | 04 M6.1 |
| $\lambda_\text{dB} = h/(mv)$ | de Broglie wavelength of an atom | m | 04 M6.2 |
| $\hbar k$, $v_\text{rec} = \hbar k/m$ | photon momentum; single-photon recoil velocity (Rb, 780 nm: 5.9 mm/s) | kg m/s; m/s | 04 M7.1 |
| $k_\text{eff} = \lvert\mathbf k_1 - \mathbf k_2\rvert \approx 2k = 4\pi/\lambda$ | effective wave vector of counter-propagating Raman beams; two-photon kick $\hbar k_\text{eff}/m = 2v_\text{rec}$ ($v_r$ in M7.3) | m⁻¹ | 04 M7.1, M7.3 |
| $\Omega_R$ | Rabi frequency of the Raman drive; $P_b = \sin^2(\Omega_R t/2)$; $\lvert a,p\rangle \leftrightarrow \lvert b, p+\hbar k_\text{eff}\rangle$ | rad/s | 04 M7.2 |
| $T$ | **time between pulses** (π/2 at 0, π at $T$, π/2 at $2T$) | s | 04 M7.2 |
| $\Phi = k_\text{eff} g T^2$ | atom-interferometer phase (magnitude); $P_b = \tfrac12(1-\cos\Phi)$ | rad | 04 M7.3 |
| $\alpha$, $\alpha_0$ | chirp rate of the Raman frequency difference; null at $\alpha_0 = k_\text{eff}g/2\pi$; $\Phi = (k_\text{eff}g - 2\pi\alpha)T^2$ | Hz/s | 04 M7.4 |
| $\delta g = \delta\varphi/(k_\text{eff}T^2)$ | acceleration noise from phase noise | m/s² | 04 M7.5 |
| µGal/√Hz | gravimeter noise density; after $t$ seconds, $S/\sqrt t$ | (m/s²)/√Hz | 04 M7.5, M7.8 |
| $T^2$ gain | sensitivity $\propto T^2$: ground $T$ ≈ few hundred ms, orbit ≈ 10 s; drop height $2gT^2$, fountain apex $\tfrac12 gT^2$ | — | 04 M7.6 |
| $\Omega$, $A$ (Sagnac) | rotation rate; enclosed area; $\Phi_\text{atom}/\Phi_\text{light} = m\lambda c/h$ (⁸⁷Rb: $h/m \approx 4.6\times10^{-9}$ m²/s, ratio $5.1\times10^{10}$) | rad/s; m² | 04 M7.7 |
| absolute / relative; drift | gravimeter that measures $g$ itself / only changes; drift (per month or year) adds linearly, does not average down | fraction/time | 04 M7.8; C3 §3 |
| $k\,\delta L = mg$; $\delta L = gT^2/4\pi^2$ | spring gravimeter ($k$ spring constant, $T$ its period); response rises as $T^2$ (erratum L135) | m | 04 M7.8 |

## Day 05 — Sensing checkpoint

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| blank-page law sheet | the ten Day 01-04 laws written from memory with units, before the items | — | 05 warm-up |
| item scoring; F1 rubric | 1 point: right number (±5%), unit and move named; ½: one slip; 0: wrong law or missing unit. F1 piece: six parts × 0-2 = 12, pass 8/12 with ≥ 1 in parts 1 and 4, 270-330 words | points | 05 scoring rules, rubric |

## Day 06 — Quantum communication

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| AES-128/256 | symmetric cipher, computational security; Grover only square-roots the work (AES-256 → ~$2^{128}$) | bit (key) | 06 M8.1 |
| OTP; rekey rate | one-time pad: random key as long as the message, used once; information-theoretic; key rate = data rate. AES rekey rate = 256 bits per interval | bit/s | 06 M8.1 |
| RSA, ECDH | public-key exchange (factoring; discrete log); both broken by Shor, AES is not | — | 06 M8.2 |
| harvest now, decrypt later | record traffic today, decrypt when a capable quantum computer exists | — | 06 M8.2 |
| $x + y > z$ | Mosca's inequality: secrecy life + migration time > time to a cryptographically relevant quantum computer; exposure $x+y-z$ | years | 06 M8.2 |
| PQC | post-quantum cryptography: FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA (Aug 2024); software, computational | — | 06 M8.3 |
| QKD | key distribution from single photons; distributes keys, does not encrypt; needs an authenticated classical channel | — | 06 M8.3 |
| R (+), D (×) | rectilinear basis (H = 0, V = 1); diagonal basis (+45° = 0, −45° = 1) | — | 06 M9.1; C4 §3 |
| $\lvert H\rangle$, $\lvert V\rangle$, $\lvert D\rangle$, $\lvert A\rangle$ | 0°, 90°, +45° (lecture "+"), −45° (lecture "−"); $\lvert D\rangle, \lvert A\rangle = (\lvert H\rangle \pm \lvert V\rangle)/\sqrt2$ | — | 06 M9.1 |
| Malus's law | pass probability $\cos^2\theta$ at angle $\theta$ to the analyser; wrong basis → ½ | — | 06 M9.1 |
| Holevo bound | one qubit yields at most one classical bit | bit | 06 M9.1 |
| no-cloning | no linear (unitary) machine copies an unknown state; also forbids amplifiers | — | 06 M9.2 |
| sifting; privacy amplification | keep positions where bases match (≈ ½), announcing bases only; then shorten the corrected key to remove Eve's knowledge | — | 06 M9.3 |
| QBER | quantum bit error rate on **sifted** bits; full intercept-resend gives 25%, fraction $f$ gives $f/4$ | % | 06 M9.4 |
| $P_\text{detect} = 1-(3/4)^n$ | chance $n$ checked sifted bits expose a full intercept-resend Eve | — | 06 M9.4 |
| 11%, $r = 1-2h(Q)$ | BB84 one-way QBER limit (Shor-Preskill); secret fraction, $h$ binary entropy | — | 06 M9.4 |
| B92 | two states ($\lvert H\rangle$ = 0, $\lvert D\rangle$ = 1); conclusive ¼ of photons; under intercept-resend survival $(2/3)^n$ | — | 06 M9.5 |
| E91, no-signalling | entanglement-based QKD with a CHSH check; measuring one particle sends no message | — | 06 M9.5 |
| $S$ (CHSH), $V$ | $\langle ab\rangle + \langle AB\rangle + \langle aB\rangle - \langle Ab\rangle$; local $\lvert S\rvert \le 2$, quantum $2\sqrt2 \approx 2.83$; $E(\theta_1,\theta_2) = \cos2(\theta_1-\theta_2)$; with visibility $V$, $S = 2\sqrt2V$ (> 2 needs $V > 0.707$) | — | 06 M10.1 |
| $\alpha$ (fibre) | fibre loss, ≈ 0.2 dB/km at 1550 nm (typical); link loss $\alpha L$ dB | dB/km | 06 M10.2 |
| $\eta = 10^{-\alpha L/10}$ | transmission: fraction of photons that arrive (companion writes $T$) | — | 06 M10.2; C4 §3 |
| PLOB bound | repeaterless ceiling $-\log_2(1-\eta) \approx 1.44\eta$ secret bits per channel use | bit/use | 06 M10.2 |
| trusted node | relay that holds $K_1$, $K_2$ and publishes $K_1 \oplus K_2$: decrypt and re-encrypt, sees the key | — | 06 M10.3 |
| quantum repeater | entanglement swapping + quantum memory (+ purification); never amplifies (erratum L152) | — | 06 M10.3 |
| free-space loss | spreads roughly as $1/L^2$ (×4 = 6 dB per doubling), not exponentially | — | 06 M10.4 |

## Day 07 — Quantum simulation

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| $2^N$ | amplitudes for $N$ spins (two states each; $d^N$ in general) | count | 07 M11.1; C5 §3 |
| $8\cdot2^N$, $16\cdot2^N$ | state memory, single / double precision (8 / 16 bytes per complex amplitude) | B | 07 M11.1 |
| $e^{-iHt/\hbar}$ | time evolution (Eq 5.2): diagonalise $H$, project $c_n = \langle n\vert\psi(0)\rangle$, attach $e^{-iE_nt/\hbar}$; dense double-precision $H$ takes $16\cdot4^N$ B, diagonalising it ~$8^N$ operations | — | 07 M11.2 |
| $M$ runs | repeated shots; precision of an average $\ge 1/\sqrt M$ | count | 07 M11.3 |
| MPS, $\chi$; sign problem | matrix product state, bond dimension $\chi$, memory ≈ $2\chi^2N$ complex numbers; the sign problem is why quantum Monte Carlo fails for many interacting fermions | — | 07 M11.3 |
| analogue / digital | hardware whose own $H$ is the model / evolution compiled into gates | — | 07 M11.4 |
| Trotter split | $e^{-i(A+B)t} \approx (e^{-iAt/n}e^{-iBt/n})^n$; error ≈ $\tfrac{t^2}{2n}\lVert[A,B]\rVert$ ($\hbar = 1$) | — | 07 M11.4 |
| boson / fermion rule | composite is a fermion if it holds an odd number of fermions; neutral atom: odd $N_n = A - Z$ → fermion | — | 07 M11.5 |
| $\lambda_\text{th} = h/\sqrt{2\pi mk_BT}$ | thermal de Broglie wavelength (companions once wrote $\lambda_T$) | m | 07 M11.6 |
| $n\lambda_\text{th}^3 \ge 2.612$; $d = n^{-1/3}$ | BEC condition (ideal uniform Bose gas), i.e. $\lambda_\text{th} \gtrsim 1.38d$, gives $T_c$; $d$ = spacing at number density $n$ (m⁻³) | —; m | 07 M11.6 |
| $d = \lambda/2$ | optical-lattice spacing | m | 07 M11.7 |
| $J$, $U$ | tunnelling (hopping) energy, falls exponentially with depth; on-site repulsion, rises slowly | J (or $J/h$ Hz) | 07 M11.7 |
| $U/J$ | small → superfluid (one shared phase, interference peaks); large → Mott insulator (fixed atoms per site, blob); switch ≈ 29 (working value; 35 mean field) | — | 07 M11.7 |
| $\Delta x = h\,t_\text{TOF}/(md)$ | time-of-flight peak spacing after release for $t_\text{TOF}$ | m | 07 M11.7 |
| Ising model (ions) | phonon-mediated spin-spin coupling plus transverse field; paramagnet → ferromagnet; "sharper with $N$" is a finite-size effect | — | 07 M11.8 |

## Day 08 — Quantum computing I

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| $\lvert\psi\rangle = \alpha\lvert0\rangle + \beta\lvert1\rangle$ | qubit, $\lvert\alpha\rvert^2+\lvert\beta\rvert^2 = 1$ | — | 08 M12.1 |
| $\theta$, $\varphi$ (Bloch) | $\cos\tfrac\theta2\lvert0\rangle + e^{i\varphi}\sin\tfrac\theta2\lvert1\rangle$; pure states on the surface, mixed inside (erratum L47); $P(0) = (1+z)/2$; equator $\lvert\pm\rangle = (\lvert0\rangle \pm \lvert1\rangle)/\sqrt2$ | rad | 08 M12.1 |
| $X$, $Z$, $Y = iXZ$, $H$ | bit flip; phase flip; bit and phase flip; Hadamard ($H^2 = I$, $HZH = X$, $HXH = Z$); $H^{\otimes n}\lvert0\cdots0\rangle$ is uniform, amplitude $2^{-n/2}$ | — | 08 M12.2 |
| CNOT, $\oplus$ | $\text{CNOT}\lvert x,y\rangle = \lvert x, y\oplus x\rangle$; $\oplus$ = XOR; control is the left bit | — | 08 M12.3 |
| right to left | circuit order in time is the reverse of matrix-product order: "$H$ then CNOT" = $\text{CNOT}(H\otimes I)$ | — | 08 M12.3 |
| $\lvert\Phi^+\rangle$ | Bell state $(\lvert00\rangle + \lvert11\rangle)/\sqrt2$; fails the product test (coef 00 × coef 11 ≠ coef 01 × coef 10) | — | 08 M12.3 |
| $P(\phi)$ | phase gate diag$(1, e^{i\phi})$; H-P-H gives $P(0) = \cos^2(\phi/2)$, the Mach-Zehnder fringe | — | 08 M12.4 |
| $U_f$, query | oracle $U_f\lvert x\rangle\lvert y\rangle = \lvert x\rangle\lvert y\oplus f(x)\rangle$; one use = one query | — | 08 M12.5 |
| phase kickback | ancilla in $\lvert-\rangle$: $U_f\lvert x\rangle\lvert-\rangle = (-1)^{f(x)}\lvert x\rangle\lvert-\rangle$ | — | 08 M12.5 |
| constant / balanced | $f$ same on all inputs / 1 on exactly half; Deutsch ($n = 1$) decides in one query | — | 08 M12.6 |
| amp$(0\cdots0)$ | Deutsch-Jozsa: $2^{-n}\sum_x(-1)^{f(x)}$, ±1 constant, 0 balanced; ancilla must start in $\lvert1\rangle$ (erratum L93) | — | 08 M12.7 |
| $2^{n-1}+1$; $2^{1-k}$ | deterministic classical worst-case queries; randomised error after $k$ queries | queries; — | 08 M12.7 |
| teleportation | one Bell pair + 2 classical bits $(m_1, m_2)$ per qubit; Bob applies $X^{m_2}$ then $Z^{m_1}$; not faster than light | — | 08 M12.8 |
| Quirk; The Qubit Factory | in-browser circuit simulator (Week 1 stand-in); Week 6 puzzle game (best identification) | — | 08 lab; C6 §9 |

## Day 09 — Quantum computing II

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| $n = \log_2 N$ | input size in bits of a number $N$ | bit | 09 M13.1 |
| speed-up classes; $O(\cdot)$ | exponential (Shor), simulation, quadratic (Grover), heuristic / unproven (annealing, VQE, QAOA, QML); $O$ = "grows no faster than" | — | 09 M13.1; C6 §3 |
| NFS | number field sieve, best classical factoring, $\exp(c\,n^{1/3}(\log n)^{2/3})$: **sub-exponential** | operations | 09 M13.1 |
| $a$, $r$ | random base; order (period): smallest $r > 0$ with $a^r \equiv 1 \pmod N$ | — | 09 M13.2 |
| Shor success; gcd; QFT | $r$ even **and** $a^{r/2} \not\equiv -1 \pmod N$, then $\gcd(a^{r/2}\pm1, N)$ (erratum L150); gcd is cheap (Euclid); the QFT period-finding is the only quantum step | — | 09 M13.2 |
| $k \approx (\pi/4)\sqrt N$ | Grover iterations; $\sin\theta = 1/\sqrt N$, $P_k = \sin^2((2k+1)\theta)$; overshoot past the optimum | iterations | 09 M13.3 |
| $F$, $g$, $F^g$, $g_{1/2}$ | two-qubit gate fidelity (error $1-F$); gate count; circuit success (crude); gates to 50%: $\ln0.5/\ln F \approx 0.693/(1-F)$ | —; gates | 09 M13.4 |
| $T_1$, $T_2$ | energy-relaxation time; dephasing time; $T_2 \le 2T_1$ | s | 09 M13.4 |
| QEC; $p$, $p_\text{th}$ | quantum error correction: one logical qubit in many physical ones, checked by syndrome measurements; physical error rate per operation; threshold (surface code ≈ $10^{-2}$) | — | 09 M13.5 |
| threshold theorem | if $p < p_\text{th}$ the logical error can be made arbitrarily small at polylog cost in $1/\varepsilon$ (erratum L184) | — | 09 M13.5 |
| $p_L$, $d$ | logical error per cycle ≈ $0.1(p/p_\text{th})^{(d+1)/2}$ (heuristic); $d$ odd code distance; ≈ $2d^2$ physical qubits per patch | —; count | 09 M13.5 |
| NISQ | noisy intermediate-scale quantum: ~50 to a few hundred physical qubits, no QEC | — | 09 M13.6 |
| VQE | classical optimiser tunes a short circuit to minimise measured energy; no proven speed-up | — | 09 M13.6 |
| ZNE, $\lambda$ | zero-noise extrapolation: noise ×$\lambda$ = 1, 2, …, extrapolate to 0, e.g. $E(0) = 2E(1)-E(2)$ | — | 09 M13.6 |
| annealing / gate model | analogue optimiser, special-purpose / universal digital machine; qubit counts not comparable | — | 09 M13.6 |

## Day 10 — Maturity, comparison, capstone

| Symbol / term | Meaning | Unit | Day/§ |
|---|---|---|---|
| TRL 1-9 | NASA technology readiness level, verbatim Table 7.1: 4 laboratory → 5 relevant environment → 6 system prototype → 7 operational → 8 qualified → 9 proven in operations | — | 10 F2.1; C7 §3 |
| component vs system TRL | score the system, never above its weakest essential component; a sale is not TRL 9 | — | 10 F2.1; C7 §4A |
| advantage test (L88) | relevant task; no known conventional technology; with reasonable effort; verdict shown / niche science only / not yet shown | — | 10 F2.2 |
| five barriers | technological developments → proof of relevance and practicality → use cases → validation of usability → scalable and robust production | — | 10 F2.3 |
| $C$, $B$, $p$; ranges | cost committed; benefit if it works; probability it works; each uncertain input carried as low, central, high | £; £; — | 10 M14.1 |
| $\mathrm{EV} = pB - C$; $p^* = C/B$ | expected value; break-even probability | £; — | 10 M14.1 |
| swing, weakest assumption | EV change as one input runs low → high ("tornado", judgement); the largest swing is the weakest assumption | £ | 10 M14.1 |
| $R = pB/C = p/p^*$ | benefit/risk ratio as defined in this sprint (expected benefit over cost); $R > 1$ ⇔ EV > 0 | — | 10 M14.2 |
| extraction card | seven fields for a market figure: figure, kind, year, segment, range, where, caveat | — | 10 "F3 again" |
| fact sheet | one A4 page (~400-450 words): header + six blocks (features, advantage table, how it helps, maturity, risks and $R$, sources) | words | 10 M14.3 |

## Lecture notation vs sprint notation

The companions' §3 decoders carry the full tables; these are the clashes that change a number.

| Lecture (or source) writes | Sprint reads | Where |
|---|---|---|
| "T√Hz" (W2 L74) | T/√Hz, a noise density | 02 M2.3; C2 §3 |
| $\delta x = S\sqrt{B}$ (the design spec) | $\delta x = S\sqrt{\Delta f}$; $B$ stays the field | 02 M2.3 |
| "100ρT", "κHz", "1019" (W2 L69, L119, L205) | 100 pT, kHz, $10^{19}$ | C2 §3, §4.10 |
| $\pi\hbar/q_e$ (W2 Eq 2.2) | $\Phi_0 = h/2e$ | 03 M5.2 |
| "amplitude increases by $r^2$" (W2 L94) | gain $(r_1/r_2)^2$ | 02 M3.2 |
| $\Phi = k_\text{eff}a\tau^2$, $\tau = 2T$ "total interrogation time" (W3 L105-110) | $\Phi = k_\text{eff}gT^2$, $T$ between pulses; the lecture's form is 4× larger | 04 M7.4; C3 §4E |
| "$\alpha = g$" (W3 L91) | $\alpha_0 = k_\text{eff}g/2\pi$ (Hz/s) | 04 M7.4; C3 §4D |
| $T$ for pendulum and spring periods (W3 L133, L135); $\Omega$ for rotation vs $\Omega_R$ for Rabi | context decides; $T$ in $\Phi$ is always pulse spacing | C3 §3 |
| E for electric field (W3 L26) and Eötvös (L153) | E = $10^{-9}$ s⁻² only when it follows a number | C3 §3 |
| R and D bases; "+" and "−" as **states** (W4 Fig 4.3) | R ≡ "+" basis, D ≡ "×" basis; lecture "+" ≡ $\lvert D\rangle$ (+45°, bit 0), "−" ≡ $\lvert A\rangle$ (−45°, bit 1) | 06 M9.1; C4 §3 |
| $T$ for transmission (C4) | Day 06's $\eta$; $\eta_d$ in C4.2 is detector efficiency | C4 §3 |
| "840 kB", "880 GB" (W5 Table 5.2, L55) | 8.4 MB, 8.8 TB ($8\cdot2^N$ B) | 07 M11.1; C5 §4C |
| $J$ (W5 Figs 5.8-5.9) | ion spin-spin coupling there; tunnelling in Bose-Hubbard | C5 §3 |
| $d$ (Day 07) vs $a$ in many texts | lattice spacing $d = \lambda/2$; $a_s$ is only the scattering length | C5 §3 |
| $H$ (W5 Hamiltonian) vs $H$ (W6 Hadamard) | context decides | C6 §3 |
| $N$ (Grover items, Shor number), $n$ (bits) | $N = 2^n$ in Grover; Shor's size is $\log_2 N$ bits | 09 M13.1; C6 §3 |
| "Deutsch-Josza" (W6) | Deutsch-Jozsa | 08 M12.7 |
| $T_2$ vs Week 3 $T$ | coherence time, not pulse spacing | C6 §3 |
| "SWAP-C" (W7 L108) | SWaP-C | C7 §4E |

## A–Z index

- **A–B:** absolute/relative gravimeter 04 · accuracy 02 · advantage test 10 · AES 06 · Allan deviation $\sigma_y(\tau)$ 02 · amp$(0\cdots0)$ 08 · analogue/digital simulation 07 · annealing 09 · $\alpha$ chirp 04 · $\alpha$ fibre loss 06 · B92 06 · bandwidth $f_c$ 02 · barriers (five) 10 · BB84 06 · BEC condition 07 · BEC microscope 03 · Bell state $\lvert\Phi^+\rangle$ 08 · bias 02 · blank-page law sheet 05 · Bloch sphere 08 · boson/fermion rule 07 · break-even $p^*$ 10
- **C–D:** $C$, $B$, $p$ 10 · CHSH $S$ 06 · CNOT 08 · coherence $T_1$, $T_2$ 09 · comb $f_\text{rep}$, $f_\text{ceo}$ 03 · component vs system TRL 10 · constant/balanced 08 · $d$ code distance 09 · $d$ lattice spacing 07 · $d = n^{-1/3}$ 07 · dB 02 · $\Delta f$ 02 · $\delta\phi_\text{SQL}$, $\delta\phi_\text{HL}$ 02 · $\delta t$, $\delta x$ (clock chain) 01 · $\delta x = S\sqrt{\Delta f}$ 02 · Deutsch, Deutsch-Jozsa 08 · distance gain $(r_1/r_2)^n$ 02 · drift 04 · dynamic range 02
- **E–F:** E (Eötvös) 01 · E91 06 · $E = h\nu$ 03 · ECDH 06 · $e^{-iHt/\hbar}$ 07 · EV 10 · extraction card 10 · F1, F2, F3 01, 10 · $F$, $F^g$, $g_{1/2}$ 09 · fact sheet 10 · figure of merit 01 · $f_L = \gamma B$ 03 · fluxgate 03 · free-space loss 06
- **G–K:** Gal, µGal 01 · $g$ 01 · gcd 09 · Grover $(\pi/4)\sqrt N$ 09 · $H$ Hadamard 08 · $H^{\otimes n}$ 08 · Harrowmere 01 · harvest now, decrypt later 06 · Holevo 06 · holdover 03 · $\lvert H\rangle\lvert V\rangle\lvert D\rangle\lvert A\rangle$ 06 · $I \propto \cos^2(\varphi/2)$ 04 · Ising (ions) 07 · $J$, $U$ 07 · $k$ 04 · $k_\text{eff}$ 04
- **L–N:** $\lambda_\text{dB}$ 04 · $\lambda_\text{th}$ 07 · Larmor 03 · like-for-like 01 · lock loop 03 · M1-M14 (moves table) · Malus 06 · Mosca $x+y>z$ 06 · Mott insulator 07 · MPS, $\chi$ 07 · $M$ runs 07 · $n = \log_2 N$ 09 · $N$ particles 02 · NFS 09 · NISQ 09 · no-cloning 06 · no-signalling 06 · NV centre 03
- **O–P:** $O(\cdot)$ 09 · OPM 03 · oracle $U_f$ 08 · OTP 06 · $P_1 = \sin^2(\Omega t/2)$ 03 · $P_\text{detect}$ 06 · $P(\phi)$ 08 · parallelism myth 01, 08 · $p$, $p_\text{th}$, $p_L$ 09 · phase kickback 08 · $\Phi = k_\text{eff}gT^2$ 04 · $\Phi_0$ 03 · PLOB bound 06 · PQC 06 · precision 02 · prefixes 01 · privacy amplification 06 · pulse area 03
- **Q–R:** QBER 06 · QEC 09 · QFT 09 · QKD 06 · $Q = \nu/\Delta\nu$ 03 · Quirk, Qubit Factory 08 · R, D bases 06 · $R = pB/C$ 10 · Rabi $\Omega$, $\Omega_R$ 03, 04 · Ramsey 03 · ranges 10 · recoil $v_\text{rec}$ 04 · rekey rate 06 · repeater 06 · resolution 02 · right-to-left 08 · RSA 06
- **S–T:** $S$ noise density 02 · Sagnac ratio 04 · SERF 03 · Shor, order $r$ 09 · sifting 06 · sign problem 07 · SNR 02 · source hierarchy 01 · speed-up classes 09 · spring $\delta L = gT^2/4\pi^2$ 04 · SQUID 03 · swing 10 · SWaP-C 01 · $T$ pulse spacing 04 · $T^2$ gain 04 · T (tesla), T/√Hz 01, 02 · teleportation 08 · threshold theorem 09 · Trotter 07 · TRL 10 · trusted node 06 · two-photon kick 04
- **U–Z:** $U/J$ 07 · $V$ visibility 06 · VQE 09 · $X$, $Y$, $Z$ 08 · $y = \delta\nu/\nu$ 01 · ZNE 09 · $2^N$, $8\cdot2^N$ 07 · $\eta$ transmission 06 · 11% QBER limit 06
