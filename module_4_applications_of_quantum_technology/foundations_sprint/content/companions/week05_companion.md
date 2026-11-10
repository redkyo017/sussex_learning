# Week 05 Companion - Quantum simulation

**Built on:** Day 07 (M11: $2^N$ amplitudes and $8\cdot2^N$ bytes, Hamiltonian evolution as a matrix, analogue versus digital simulation, J versus U), with Day 01 (M1 orders of magnitude), Day 02 (M3 shot noise $1/\sqrt{N}$, used for readout) and Day 04 (M6 de Broglie wavelength).
**Feeds:** Portfolio (Assessment 2) through the Week 5 Consolidate piece. Nothing here is aimed at Assessment 1.

Line numbers `L..` refer to `week_5/week_5_lecture.md`. Figure numbers refer to `week_5/figures/fig5_N.png`. Read this alongside the lecture, not instead of it.

## 1. Read these first (Pass 0)

Before you read the lecture, know what the week asks you to do with it. Types only, no solutions.

1. **Explore quiz (4 MCQ):** future applications; quantum computer versus quantum simulator; a "fundamental concept" of quantum computing; a "fundamental limitation". Answers: see the inventory key (`docs/problem_inventory.md`, Week 5 rows). **Q3 and Q4 are flagged there**: Q3 is ambiguous (the superposition option repeats the parallelism myth, Week 1 L70), and Q4 is badly posed (the intended answer is a capability, not a limitation). Q2 also has a contested distractor. If the course marks your choice wrong, try the other defensible option and note which one it wants.
2. **Apply (forum, 200-300 words):** pick one type of quantum simulation (cold atoms in lattices, trapped-ion spin models, molecules) and argue why the quantum approach matters and what applications could follow. Type: F1 gain argument, short form.
3. **Consolidate (portfolio, 300 words):** one or two advantages of quantum over classical numerical simulation, with quantitative and qualitative measures (speed, simulations not possible classically) and practical aspects. Type: F1 gain argument with M11 numbers.
4. **Checkpoint quiz:** the same four questions as Explore with the options shuffled. See the inventory key.

The quantitative side is small but must be exact: count the amplitudes ($d^N$), turn them into bytes, say what that costs for the Hamiltonian as well as the state, estimate a de Broglie wavelength against a spacing, and place an experiment on the J-versus-U axis. Sections 4-6 drill exactly that.

## 2. What the lecture is doing, in one picture

A classical computer stores a quantum state of $N$ two-state particles as $2^N$ complex numbers, so the memory doubles with every particle you add and runs out at a few tens of particles. Feynman's answer (L59) is to stop simulating the quantum system on classical hardware and instead build a **controllable** quantum system whose Hamiltonian copies the one you care about, let it evolve, and measure it. The lecture then shows three platforms. Ultracold neutral atoms in laser "egg-boxes" (optical lattices) play electrons in a crystal: lowering or raising the wells trades tunnelling J against interaction U and drives the superfluid-to-Mott-insulator transition. Two-dimensional atom clouds show the BKT transition through vortex pairing. Trapped ions play magnetic spins and show a paramagnet turning into a ferromagnet as an engineered spin-spin coupling is ramped up. All of these are **analogue** simulators, built for one model each; the lecture never contrasts them with digital (gate-based) simulation, and 4K does.

The lecture's one table (Table 5.2) is wrong in two of its six rows; 4C fixes it.

Free reading if you want more than the lecture: Georgescu, Ashhab, Nori, *Quantum simulation*, https://arxiv.org/abs/1308.6253 (§I-III), and the photonic-simulator review by Aspuru-Guzik & Walther, https://dash.harvard.edu/bitstream/handle/1/11881655/aspuru-guzik-photonic-quantum-simulators.pdf?sequence=1 (intro).

## 3. Notation and unit decoder

Two letters in this lecture mean two different things in two different sections. The "clash" column is the reason this table exists.

| Symbol as written | Read it as | Unit | Where (lecture line) | Clash / trap | Move |
|---|---|---|---|---|---|
| $H$ | Hamiltonian: the energy operator; for $N$ spins a $2^N\times2^N$ matrix | J (energy) | Eq 5.1, L28 | $H$ is not a number; "the Hamiltonian is a constant" (L28) means "does not change in time" | M11 |
| $\hbar$ | reduced Planck constant $h/2\pi = 1.055\times10^{-34}$ J·s | J·s | Eq 5.1 | $Ht/\hbar$ is dimensionless (an angle) | M11 |
| $\psi$, $\lvert\psi\rangle$ | the state: a column of complex amplitudes | dimensionless | Eq 5.1, L21 | L21 calls it "a probability amplitude"; it is a list of them, one per configuration | M11 |
| $\lvert\psi(0)\rangle$ | initial state the simulator is prepared in | - | Eq 5.2, L61 | | M11 |
| $e^{-iHt/\hbar}$ | time-evolution (unitary) operator: a matrix exponential | dimensionless | Eq 5.2, L35 | not $e$ to a number; see 4A | M11 |
| $\psi_1\dots\psi_8$ | the $2^3 = 8$ amplitudes of three spins | dimensionless | Table 5.1 | each is complex: two real numbers | M11 |
| $N$ | number of particles (spins, qubits, ions) | count | Table 5.2, L169, Fig 5.9 | in Fig 5.9 $N$ = number of ions; in M3 $N$ = number of shots or atoms detected | M11 |
| $2^N$, $d^N$ | number of amplitudes for $N$ particles with 2 (or $d$) states each | count | L53 (implicit) | the lecture never writes $2^N$; it lists 8 and tabulates the rest | M11 |
| bit, byte, kB, MB, GB, TB | 8 bits = 1 byte; decimal prefixes $10^3, 10^6, 10^9, 10^{12}$ | bytes | L53-L55 | $8\cdot2^{20}$ B is 8.4 MB (decimal) or exactly 8 MiB (binary); the lecture uses decimal | M1 |
| single precision | 32-bit real; a complex number is 2 × 32 bits = 8 bytes | bytes | L53 | double precision (usual in physics codes) is 16 bytes per complex number | M11 |
| qubit | a two-state quantum particle used to store information | - | L59 | L59's "all possible states stored naturally" is storage, not readable output; see 4D | M11 |
| fermion / boson | half-integer / integer total spin; fermions obey Pauli exclusion, bosons can share a state | - | L69 | count spin-½ constituents; see 4F | M11 |
| Li-6 | lithium-6: 3 p, 3 n, 3 e (a composite fermion) | - | L69, Fig 5.1B | Li-7 (one extra neutron) is a boson | M11 |
| nK, µK, mK | $10^{-9}$, $10^{-6}$, $10^{-3}$ kelvin | K | L81, L103 | "sub-millikelvin" (L81) is laser cooling; BEC needs hundreds of nK | M1 |
| µm | micrometre, $10^{-6}$ m | m | L141, L143 | ion spacing is µm; lattice spacing is a few hundred nm | M1 |
| °C | Celsius; K = °C + 273.15 | K | L181 | −196 °C = 77 K (liquid nitrogen) | M1 |
| MOT | magneto-optical trap: lasers plus a field gradient that cool and hold atoms | - | L81, Fig 5.2C | | M11 |
| BEC | Bose-Einstein condensate: a macroscopic number of bosons in one quantum state | - | L81 | requires bosons; see 4G for the criterion | M6, M11 |
| $\lambda_\mathrm{dB}$, $\lambda_\text{th}$ | de Broglie wavelength $h/mv$; thermal version $h/\sqrt{2\pi mk_BT}$ | m | L81, L103 (in words) | the lecture states the criterion in words only; earlier drafts of this companion (and many texts) write $\lambda_T$ for $\lambda_\text{th}$, the symbol Day 07 uses | M6 |
| Feshbach resonance | a magnetic-field setting where the atom-atom interaction strength can be tuned, even through zero | - | L83, L93 | it tunes $U$, not $J$ | M11 |
| BEC-BCS crossover | continuous change from tightly bound fermion pairs (molecules that condense) to loose Cooper-like pairs | - | L93 | | M11 |
| optical lattice | standing wave of laser light; atoms sit in the intensity wells | - | L71, Fig 5.1C | well spacing is $\lambda/2$; see 4H | M11 |
| $d$ | lattice spacing $\lambda/2$ (Day 07's symbol); in 4G and C5.2, $n^{-1/3}$ is the spacing between atoms in a gas | m | L71, L103 (in words) | many texts write $a$ for the lattice spacing; here $a_s$ is only the scattering length (C5.3) | M11 |
| lattice depth $V_0$ | height of the wells, often in units of the recoil energy $E_r = h^2/2m\lambda^2$ | J, or $E_r$ | L71, L103 | set by laser power | M11 |
| $J$ (Bose-Hubbard) | **tunnelling** energy between neighbouring wells | J, quoted as $J/h$ in Hz | L103 (in words) | in Figs 5.8-5.9 $J$ is the **spin-spin coupling** of the ions | M11 |
| $U$ | on-site interaction energy of two atoms in one well | J, or $U/h$ in Hz | L103 (in words) | | M11 |
| Mott insulator / superfluid | fixed atoms per site, no phase coherence / atoms delocalised, one shared phase | - | L99-L103, Fig 5.3 | the lecture calls the superfluid "a BEC" (L103) | M11 |
| Bose-Hubbard model | lattice model with only $J$ and $U$ | - | L93, L99 | story level only in this sprint | M11 |
| BKT, $T_c$ | Berezinskii-Kosterlitz-Thouless transition in 2D; its temperature | K | L121, Fig 5.5 | $T_c$ in Fig 5.5 is $T_\mathrm{BKT}$, not the 3D BEC $T_c$ | M11 |
| Tonks gas | 1D gas of strongly repelling bosons that behave like fermions | - | L95 | | M11 |
| Paul / Penning trap | ion trap using RF + DC electric fields / static electric + magnetic fields | - | L141, Fig 5.7 | | M11 |
| CCD | charge-coupled device camera | - | L141 | | - |
| spin ½, ↑ ↓ | two internal states of an ion, mapped to a magnetic spin | - | L153-L157 | the same two-level system as Module 3 | M11 |
| $\sigma^x_i$, $\sigma^z_i$ | Pauli operators on ion $i$ | - | Fig 5.8A | the field term uses $x$, the coupling $z$ | M11 |
| $B_x$, $B$ | effective transverse field (set by lasers or microwaves, not a real magnet) | energy units | Fig 5.8, Fig 5.9 | not the Week 2 magnetic field in tesla | M11 |
| $\lvert J/B_x\rvert$, $B/\lvert J\rvert$ | coupling-to-field ratio (Fig 5.8) and its inverse (Fig 5.9) | dimensionless | Fig 5.8B, Fig 5.9 | the two plots run in **opposite** directions | M11 |
| $m_x$ (written "ḿ$_x$") | ferromagnetic order parameter of the ion chain | dimensionless, 0 to 1 | Fig 5.9 | | M11 |
| Ising, XY, XYZ | spin models with $\sigma^z\sigma^z$ / $\sigma^x\sigma^x+\sigma^y\sigma^y$ / all three couplings | - | L153 | "Ising XY and XYZ" is three models, not one; see 4L | M11 |

**Conversions you will use every time.** Amplitudes $= d^N$. Bytes $= (\text{bytes per complex number})\times d^N$: 8 for single, 16 for double precision. Each extra two-state particle doubles the memory; ten extra multiply it by $2^{10} = 1024 \approx 10^3$, which is why the prefixes step k, M, G, T, P every ten particles.

## 4. Skipped steps, expanded

Each item gives the lecture line, the gap, the missing lines and the move. Items C, D and I are the reason this companion exists.

### 4A. Eq 5.1-5.2 (L21-L35): why $e^{-iHt/\hbar}$ solves the Schrödinger equation, and what it costs (M11)

1. **Check the solution.** Put $\lvert\psi(t)\rangle = e^{-iHt/\hbar}\lvert\psi(0)\rangle$ into Eq 5.1. If $H$ does not depend on time, the derivative of the exponential works as for numbers: $\frac{\mathrm{d}}{\mathrm{d}t}e^{-iHt/\hbar} = -\frac{i}{\hbar}H\,e^{-iHt/\hbar}$. Multiply by $i\hbar$: $i\hbar\,\frac{\mathrm{d}\psi}{\mathrm{d}t} = H\psi$. That is Eq 5.1, and at $t = 0$ the exponential is the identity, so the initial state is right.
2. **What "e to a matrix" means.** Diagonalise $H$ (Module 3's eigenproblem): $H = \sum_k E_k\lvert k\rangle\langle k\rvert$. Then $e^{-iHt/\hbar} = \sum_k e^{-iE_kt/\hbar}\lvert k\rangle\langle k\rvert$. In words: write the state in the energy eigenbasis, give each component the phase $e^{-iE_kt/\hbar}$, and rotate back. Nothing else happens. The phases differ between components, so populations in any other basis oscillate.
3. **Two-level example** (Module 3 objects). $H = \varepsilon\sigma_x$ has eigenvalues $\pm\varepsilon$. Since $\sigma_x^2 = I$, the series gives $e^{-i\varepsilon t\sigma_x/\hbar} = \cos(\varepsilon t/\hbar)\,I - i\sin(\varepsilon t/\hbar)\,\sigma_x$. Starting in $\lvert\uparrow\rangle$, $P_\downarrow(t) = \sin^2(\varepsilon t/\hbar)$: Rabi flopping.
4. **"Unitary" (L35)** means $U^\dagger U = I$: total probability stays 1. It holds because each $e^{-iE_kt/\hbar}$ has modulus 1.
5. **Why the matrix, not the vector, is the real cost.** For $N$ spins $H$ is $2^N\times2^N$. Stored densely in **single** precision (8 bytes per complex entry) it needs $8\cdot4^N$ bytes; Day 07 M11.2 quotes the double-precision figure, $16\cdot4^N$, so its numbers are twice these: for $N = 20$ that is $8.8\times10^{12}$ B (8.8 TB) against 8.4 MB for the state; for $N = 30$, $9.2\times10^{18}$ B. Diagonalising a $D\times D$ matrix takes about $D^3$ operations: $(2^{20})^3 = 1.2\times10^{18}$ for $N = 20$. Real codes avoid the dense matrix (sparse $H$, step-by-step evolution), but every step still touches all $2^N$ amplitudes (judgement; see Georgescu et al. §I). The lecture's "this is only to **store** the state" (L57) is this point.

### 4B. L37-L53: the implicit $2^N$ rule and $8\cdot2^N$ bytes (M11)

1. Table 5.1 lists every up/down pattern of three spins: $2\times2\times2 = 8$ rows. Each row needs its own complex amplitude because the quantum state is a superposition of all of them at once (L53). With $N$ spins: $2^N$ amplitudes. With $d$ states per particle: $d^N$.
2. One complex number in single precision = two 32-bit reals = 64 bits = 8 bytes (L53). So memory $= 8\cdot2^N$ bytes. Three spins: $8\times8 = 64$ B, as L53 says.
3. The lecture adds that real particles also have positions and momenta (L53). Each extra degree of freedom multiplies $d$, so the spin-only count is a **lower bound**.
4. Classical contrast (L53): a classical configuration of $N$ spins needs $N$ bits. The quantum one needs $2^N$ complex numbers. That gap, not "quantum is complicated", is the argument.

### 4C. L55, Table 5.2: two rows are wrong by a factor of 10 (erratum, verified)

Recompute every row with $8\cdot2^N$ bytes (decimal prefixes):

| $N$ | $2^N$ | $8\cdot2^N$ bytes | Correct | Lecture (L55) |
|---|---|---|---|---|
| 3 | 8 | 64 | 64 bytes | 64 bytes ✓ |
| 10 | 1,024 | 8,192 | 8.2 kB | 8.2 kilobytes ✓ |
| 20 | 1,048,576 | 8,388,608 | **8.4 MB** | 840 kilobytes ✗ |
| 30 | $1.07\times10^9$ | $8.59\times10^9$ | 8.6 GB | 8.6 gigabytes ✓ |
| 40 | $1.10\times10^{12}$ | $8.80\times10^{12}$ | **8.8 TB** | 880 gigabytes ✗ |
| 50 | $1.13\times10^{15}$ | $9.01\times10^{15}$ | 9000 TB (9.0 PB) | 9000 terabytes ✓ |

1. Pattern check: each row is ten particles on, so ×1024. The mantissas should run 8.2, 8.4, 8.6, 8.8, 9.0 with the prefix stepping k, M, G, T, P. The lecture breaks the pattern at $N = 20$ and $N = 40$ by exactly a factor of 10 (a slipped decimal), and its own neighbours (8.2 kB, 8.6 GB) expose the slip.
2. In double precision (16 bytes per amplitude) every row doubles: 50 spins need 18 PB.
3. The conclusion (L57, "a few tens of particles only") survives the correction; the correct numbers make it stronger at $N = 20$ and $N = 40$.

### 4D. L57-L59: "9000 TB versus 50 qubits", with the caveats the lecture leaves out (M11, M3)

The comparison is about **storage**. Four caveats belong next to it every time you quote it.

1. **Readout.** Measuring 50 qubits gives one 50-bit string per run, not $2^{50} = 1.13\times10^{15}$ amplitudes. You learn the state only through repeated runs. An expectation value with outcomes ±1 needs about $1/\varepsilon^2$ runs for an error $\varepsilon$ (M3): $\pm0.01$ needs $10^4$ runs. Reconstructing the whole state (Pauli tomography) needs $3^N$ measurement settings, $3^{50} = 7.2\times10^{23}$: hopeless. So a simulator answers **specific questions** (a magnetisation, a correlation, a phase boundary), not "give me $\psi$".
2. **Evolution cost.** L57 says it: storing is the easy part. A classical code must apply $e^{-iHt/\hbar}$ step after step, each step touching all $2^N$ amplitudes. The quantum simulator does this by physically evolving, which is where the real gain lies.
3. **Not every state needs $2^N$ numbers.** Weakly entangled states (for example many 1D ground states) compress well with classical tensor-network methods, so the classical frontier is not always "a few tens" (judgement; Georgescu et al. §I discusses classical methods and their limits).
4. **Errors and verification.** A 50-particle simulator has imperfect control and decoherence. If no classical computer can check it, how do you trust it? The usual answer: benchmark it where classical results exist (small $N$, special cases) and extrapolate. Fig 5.9's theory curves for $N = 2$ and $N = 9$ are exactly such a benchmark.

Also note the phrase "particles can be in multiple states simultaneously ... capable of storing all possible states" (L59). It is fine for storage, but read as "computes all answers at once" it becomes the parallelism myth (Week 1, L70 erratum).

### 4E. L61: the simulator recipe in three steps (M11)

1. **Prepare** a known $\lvert\psi(0)\rangle$ (for the ions: all spins along the field, L157).
2. **Evolve** under an engineered $H$ that copies the model (Eq 5.2, done by physics, not arithmetic).
3. **Measure** chosen observables, many times (4D), and compare with the real system.

The extra knob L61 mentions (spacing, geometry, dimensionality) is what makes a simulator more than a copy of the material: you can change parameters a real crystal does not let you change.

### 4F. L69: the boson/fermion counting rule for atoms (M11)

1. Protons, neutrons and electrons are all spin-½ fermions. An odd number of them adds to half-integer spin (composite **fermion**); an even number to integer spin (composite **boson**).
2. In a neutral atom electrons = protons, so protons + electrons is even. The neutron number alone decides, as L69 says: **odd neutrons → fermion**.
3. Li-6: $3 + 3 + 3 = 9$, odd → fermion (L69, Fig 5.1B). Li-7: $3 + 4 + 3 = 10$ → boson. Rb-87 (the Mott experiment, L103): $37 + 50 + 37 = 124$ → boson, which is why it can condense. Na-23: $11 + 12 + 11 = 34$ → boson. K-40: $19 + 21 + 19 = 59$ → fermion.
4. Why it matters: to simulate electrons (fermions) you need fermionic atoms (L69); to make a BEC you need bosons. Fermions reach a BEC only by first pairing into bosonic molecules (the BEC-BCS work, L93).

### 4G. L81: the BEC criterion as a formula (M6)

1. L81 says condensation happens when the de Broglie wavelength becomes "of the order of" the particle separation. The standard form (Pethick & Smith, lecture ref [15]) uses the **thermal** de Broglie wavelength $\lambda_\text{th} = h/\sqrt{2\pi mk_BT}$ and reads $n\lambda_\text{th}^3 \geq 2.612$ for an ideal uniform gas.
2. Rb-87 at 100 nK (L103's temperature; $m = 1.44\times10^{-25}$ kg): $\lambda_\text{th} = 5.9\times10^{-7}$ m $\approx 0.59$ µm. The critical density is $2.612/\lambda_\text{th}^3 = 1.3\times10^{19}$ m⁻³, where the spacing $n^{-1/3}$ is 0.43 µm. So at the threshold the wavelength (0.59 µm) is indeed comparable to the spacing (0.43 µm), as L81 says in words.
3. "A million times less dense than air" (L81): air at room temperature has $n = p/k_BT = 2.5\times10^{25}$ m⁻³, so the gas has about $2.5\times10^{19}$ m⁻³. Solving the criterion for $T$ at that density gives $T_c \approx 160$ nK: "hundreds of nanokelvin", matching L81.
4. Why so dilute: at liquid or solid densities the atoms would bind into a solid long before they condensed (L81, "metastable gaseous state").

### 4H. L71 and L103: the optical lattice, its spacing, and tunnelling versus depth (M11)

1. Two counter-propagating beams of wavelength $\lambda$ make a standing wave with intensity $\propto\cos^2(kx)$, $k = 2\pi/\lambda$. Neighbouring maxima (or minima) are $\pi/k = \lambda/2$ apart. So the lattice spacing is $d = \lambda/2$; for example 813 nm light gives $d = 406.5$ nm (example value, not from the lecture). Three such pairs make a 3D cubic lattice (Fig 5.1C shows two beams, so a 2D one).
2. The natural energy unit is the recoil energy $E_r = h^2/(2m\lambda^2)$. For Rb-87 in 813 nm light $E_r/h = 3.5$ kHz.
3. **Depth controls tunnelling exponentially.** Deeper wells mean a thicker barrier, and tunnelling falls roughly as $e^{-2\sqrt{V_0/E_r}}$. A standard deep-lattice approximation (take on trust, not examined) is $J/E_r \approx (4/\sqrt\pi)(V_0/E_r)^{3/4}e^{-2\sqrt{V_0/E_r}}$. Going from $5E_r$ to $20E_r$ cuts $J$ by a factor of about 31. The on-site interaction $U$ grows only slowly with depth (the atoms are squeezed into a smaller well). So raising the laser power drives $U/J$ up fast. That is the only knob in the Mott experiment (L103: "the lattice depth can be controlled with the power of the laser beams").

### 4I. L99-L117: the superfluid-to-Mott transition as J versus U (M11)

1. **Two competing energies.** Tunnelling $J$ lowers the energy when atoms spread over many sites with one common phase (superfluid). Interaction $U$ costs energy whenever two atoms share a well, so it favours a fixed, equal number per site (Mott insulator). The Bose-Hubbard model (L99) contains only these two terms.
2. **The boundary.** The transition sits at a fixed ratio. For one atom per site in a 3D cubic lattice there are two estimates: quantum Monte Carlo gives $(U/J)_c \approx 29.3$ (judgement; Capogrosso-Sansone et al. 2007, not a Target Source), and mean-field theory gives $5.83z$ with $z = 6$ neighbours, about 35 (standard result; take on trust). Mean field ignores fluctuations and so overestimates the boundary. This sprint, like Day 07, takes **29** as the working value; no answer in C5.3 (or Day 07 Exercise 7.7) changes if you use 35 instead, because no ratio there falls between the two. Below the boundary: superfluid. Above it: Mott insulator.
3. **Quantum, not thermal, fluctuations (L101).** At 100 nK thermal hopping is negligible. What drives the change is the number-phase trade-off: a state with a sharp phase across sites must have an uncertain number of atoms per site, and a state with a sharp number per site has no defined phase. Changing $U/J$ moves the ground state from one to the other at (nearly) zero temperature. That is what "quantum phase transition" means.
4. **Why interference peaks mean superfluid (Fig 5.4).** Switch the lattice off and let the cloud expand. Each site emits a small wavepacket. If all sites share one phase, the packets interfere like light through a diffraction grating, giving sharp peaks at momenta $0$ and $\pm2\hbar k$ (the reciprocal lattice). That is the central spot and four side spots in Fig 5.4b-e. If each site has a random phase (Mott), the packets add with no fixed phase relation and you see a featureless blob (Fig 5.4g-h). The image is a momentum picture, not a photograph of the lattice.
5. **"Around 2.5 on average" (L103).** A Mott state has an **integer** number per site. In a real trap the density varies, so there are shells of 1, 2, 3 atoms per site; 2.5 is an average over the dense centre, not a per-site count. "Equal number per well" holds within each shell.
6. **Fig 5.4 caption is misplaced (L111-L117).** It sits under the heading of the next example (BKT) but belongs to the Mott example; read it together with L103. The caption also has "Greiner etl al.".

### 4J. L119-L131: BKT at story level (M11)

1. L119 states a known theorem (Mermin-Wagner, not named): in 1D and 2D, fluctuations at any non-zero temperature destroy true long-range order.
2. BKT (L121): in 2D, vortices (whirls of the phase) appear spontaneously. Above $T_\mathrm{BKT}$ they roam freely and scramble the phase. Below it they bind into vortex-antivortex pairs whose phase twists cancel at long distance (Fig 5.5). The result is **quasi**-long-range order: correlations decay slowly (as a power law) rather than not at all. The lecture's "long-range order prevails" (L121) is loose: it is enough order to be superfluid, not true long-range order.
3. The 2006 cold-atom test (L129): two parallel 2D clouds are released and overlap. Straight fringes mean phase coherence; a sudden kink (dislocation) in a fringe marks a free vortex in one plane (Fig 5.6). Temperature is the knob.
4. Dates: L131 says the refined experiment was "in 2021"; ref [50] (Sunami et al.) is dated 2022 (the publication year; a 2021 preprint is the likely source of the slip, judgement). Also L129 "spectactular".

### 4K. L141-L169: trapped ions as a quantum magnet; analogue versus digital (M11)

1. **Spin mapping.** Two internal levels of each ion are the "spin up" and "spin down" of a magnetic atom (the Module 3 qubit). Laser beams apply a spin-dependent push; because the ions share their vibrations (L153: "collective vibrational modes"), a push on one is felt by the others. Net effect: an engineered spin-spin coupling $J_{ij}$.
2. **The model (Fig 5.8A).** A transverse-field Ising Hamiltonian, $H = J\sum_{i<j}\sigma^z_i\sigma^z_j - B_x\sum_i\sigma^x_i$. The field term wants every spin along $x$ (paramagnet). The coupling wants spins aligned with each other along $z$ (ferromagnet). The ratio $\lvert J/B_x\rvert$ decides, just as $U/J$ does for atoms. Ramp $J$ up slowly from zero (L157) and the state follows from paramagnet to ferromagnet.
3. **Reading the two-ion result.** Start: both spins along $x$, so each of the four $z$ patterns has probability $(1/\sqrt2)^4 = 0.25$. End: the ferromagnetic ground state is the superposition $(\lvert\uparrow\uparrow\rangle + \lvert\downarrow\downarrow\rangle)/\sqrt2$, so $P_{\uparrow\uparrow} = P_{\downarrow\downarrow} = 0.5$. That is Fig 5.8B, 0.25 rising to 0.50. Note the end state is entangled.
4. **Sharper with more ions (L169, Fig 5.9).** A true phase transition is a large-$N$ (thermodynamic-limit) idea. With 2 ions the change is smooth; with 9 it is sharper. That trend, not any single curve, is the evidence that the simulator is heading towards real many-body physics.
5. **Frustration (L169).** With antiferromagnetic coupling ($J > 0$, neighbours want to be opposite) on a triangle, no arrangement satisfies all three bonds. The energy $J(s_1s_2 + s_2s_3 + s_1s_3)$ is $+3J$ for the two all-aligned patterns and $-J$ for the other six, so the ground state is 6-fold degenerate and at best 2 of 3 bonds are satisfied. Degenerate, frustrated ground states are hard for classical methods and interesting for materials.
6. **"Analogue" (L157) without a contrast.** The lecture says "analogue quantum simulator" and never says what the other kind is. **Analogue:** build hardware whose own $H$ copies the model and let it evolve continuously; one machine, one family of models. **Digital:** run the evolution on a universal gate-based quantum computer by splitting $e^{-iHt/\hbar}$ into short steps, $e^{-i(H_1+H_2)t/\hbar} \approx \big(e^{-iH_1\Delta t/\hbar}e^{-iH_2\Delta t/\hbar}\big)^{t/\Delta t}$ (Trotter splitting), each step a few gates; any model, but the error shrinks only as the steps get shorter and the gate count grows (Georgescu et al. §III). Week 5 Quiz Q2's "computers can be universal, simulators address a specific set of problems" is this distinction.

### 4L. Smaller decodes and editorial glitches

- L153 "Porras and Zoller [51]": ref [51] is **Porras and Cirac**, PRL 92, 207901 (2004). Cite it as such.
- L153 "Ising XY and XYZ": three different models (Ising, XY, XYZ), see §3.
- L159 Fig 5.8 caption "Scheatz": ref [52] spells "Schatz"; the author is T. Schaetz. Cite from the journal record, not the caption.
- Ref [27] (Chin et al., *Feshbach resonances in ultracold gases*): listed as *Physical Review Letters*, but it is *Reviews of Modern Physics* 82, 1225 (2010), as the URL itself shows. Ref [42] (Balbinot et al.) likewise is *Physical Review A* 78, 021603, not PRL.
- L113 "Greiner etl al."; L129 "spectactular"; Fig 5.4 caption misplaced (4I).
- L181 temperatures: −269 °C = 4 K (liquid helium), −196 °C = 77 K (liquid nitrogen), −183 °C = 90 K. Flag (judgement): the Nobel-winning 1986 cuprate superconducted at about 35 K, and the first material above 77 K came a year later; the lecture merges the two. Check a source before quoting either temperature.
- L169 and ref [55]: "Islam et al ... 16 ions" (2013) is a different paper from Fig 5.9's ref [54] (2011, $N = 2$ to 9), though the first author is the same.

## 5. Clones

These have the same type as the week's quantitative content and its Consolidate task, but use different particles, atoms, lattices and a fictional case. Do them after the lecture, before the cold attempt in §6.

### Exercise C5.1 (quantitative)

A materials group models a chain of spin-1 particles (three states each: −1, 0, +1) and stores amplitudes in **double** precision. (a) How much memory does the state need for $N = 10$, 20 and 30? (b) With a 1 TB memory budget, what is the largest $N$ for spin-1, and for spin-½ in double precision? (c) How much memory would a dense Hamiltonian need for $N = 10$ spin-1 particles, also in double precision? (d) How many times larger is the $N = 20$ spin-1 double-precision state than the $N = 20$ spin-½ single-precision state?

**Hint:** Amplitudes $= 3^N$; double precision is 16 bytes per complex number. Solve $16\cdot d^N \le 10^{12}$ with logarithms. A dense Hamiltonian has $(3^N)^2$ entries.

**Solution sketch:**
1. *Restate.* Given $d = 3$, 16 bytes per amplitude, $N = 10, 20, 30$, budget $10^{12}$ B. Want state memory, largest $N$, matrix memory, a ratio.
2. *Write state.* Memory $= 16\cdot3^N$; matrix $= 16\cdot9^N$; spin-½ single $= 8\cdot2^N$.
3. *Name move.* M11 ($d^N$ amplitudes, bytes), M1 (prefixes, logarithms).
4. *Algebra.*
   - (a) $3^{10} = 59{,}049$; $16\times59{,}049 = 944{,}784$ B ≈ 0.94 MB. $3^{20} = 3.49\times10^9$; ×16 $= 5.6\times10^{10}$ B ≈ 56 GB. $3^{30} = 2.06\times10^{14}$; ×16 $= 3.3\times10^{15}$ B ≈ 3.3 PB.
   - (b) Spin-1: $3^N \le 6.25\times10^{10}$, $N \le \ln(6.25\times10^{10})/\ln3 = 22.6$, so $N = 22$. Spin-½: $N \le \ln(6.25\times10^{10})/\ln2 = 35.9$, so $N = 35$.
   - (c) $16\times59{,}049^2 = 5.6\times10^{10}$ B ≈ 56 GB: the matrix for 10 particles is as big as the state for 20.
   - (d) $5.58\times10^{10}/8.39\times10^6 \approx 6.7\times10^3$.
5. *Check.* Ten extra spin-1 particles multiply by $3^{10} \approx 5.9\times10^4$: 0.94 MB → 56 GB → 3.3 PB, consistent. Spin-1 reaches the 1 TB wall about 13 particles earlier than spin-½.
6. *Answer.* 0.94 MB, 56 GB, 3.3 PB; largest $N$ in 1 TB is 22 (spin-1) and 35 (spin-½, double); the dense $N = 10$ Hamiltonian already needs 56 GB; the spin-1 state is about 6,700 times the spin-½ state at $N = 20$.

The habit to keep: say the base ($d$), the precision and whether you mean the state or the operator before you quote any memory figure.

### Exercise C5.2 (quantitative)

A lab cools potassium-41 atoms ($m = 6.81\times10^{-26}$ kg) to 300 nK. (a) Is K-41 a boson or a fermion? What about K-40? (b) Find the thermal de Broglie wavelength and the critical density for condensation at 300 nK. (c) The cloud's peak density is $5\times10^{19}$ m⁻³. Is it condensed (ideal-gas estimate)? At what temperature would it condense at this density?

**Hint:** Potassium has 19 protons. $\lambda_\text{th} = h/\sqrt{2\pi mk_BT}$; criterion $n\lambda_\text{th}^3 \ge 2.612$. $T_c$ follows from setting $n\lambda_\text{th}^3 = 2.612$ and solving for $T$: $T_c = \frac{2\pi\hbar^2}{mk_B}\left(\frac{n}{2.612}\right)^{2/3}$.

**Solution sketch:**
1. *Restate.* Given $m$, $T = 3\times10^{-7}$ K, $n = 5\times10^{19}$ m⁻³. Want statistics, $\lambda_\text{th}$, $n_c$, $n\lambda_\text{th}^3$, $T_c$.
2. *Write state.* Counting rule; $\lambda_\text{th}$; $n\lambda_\text{th}^3$ against 2.612.
3. *Name move.* M11 (counting rule), M6 (de Broglie wavelength).
4. *Algebra.*
   - (a) K-41: $19 + 22 + 19 = 60$, even → boson. K-40: $19 + 21 + 19 = 59$ → fermion, which cannot condense on its own.
   - (b) $\lambda_\text{th} = 6.63\times10^{-34}/\sqrt{2\pi\times6.81\times10^{-26}\times1.38\times10^{-23}\times3\times10^{-7}} = 5.0\times10^{-7}$ m. $n_c = 2.612/\lambda_\text{th}^3 = 2.1\times10^{19}$ m⁻³.
   - (c) $n\lambda_\text{th}^3 = 5\times10^{19}\times(4.98\times10^{-7})^3 = 6.2 > 2.612$: condensed. $T_c = 5.3\times10^{-7}$ K ≈ 530 nK.
5. *Check.* The sample is denser than $n_c$, so $T_c$ must be above 300 nK; it is. Lighter than Rb, so a larger $\lambda_\text{th}$ at the same temperature: the scaling $\lambda_\text{th}\propto1/\sqrt{mT}$ holds.
6. *Answer.* K-41 boson, K-40 fermion; $\lambda_\text{th} \approx 0.50$ µm, $n_c \approx 2.1\times10^{19}$ m⁻³; the cloud is condensed ($n\lambda_\text{th}^3 \approx 6.2$) and would condense below about 530 nK.

Always check the statistics first: a fermion answer to (c) would be "no BEC, whatever the density".

### Exercise C5.3 (quantitative)

Potassium-39 atoms sit in a 3D cubic lattice made from 1550 nm light, with a Feshbach field (L83) setting their scattering length to $a_s = 5.0$ nm (fictional setting). The team (fictional readings, consistent with the deep-lattice approximation of 4H) measures at three depths:

| Depth $V_0/E_r$ | $J/h$ (Hz) | $U/h$ (Hz) |
|---|---|---|
| 6 | 137 | 264 |
| 14 | 19.6 | 499 |
| 20 | 5.9 | 652 |

(a) Is K-39 a boson or a fermion? Find the lattice spacing $d$ and the recoil energy $E_r/h$. (b) Compute $U/J$ at each depth and place each on the superfluid / Mott side of $(U/J)_c \approx 29$ (one atom per site; 4I). Would the mean-field value 35 change any verdict? (c) After 20 ms of free expansion, how far from the central peak are the first interference peaks? At which depth would you expect no peaks?

**Hint:** Potassium has 19 protons. Spacing $d = \lambda/2$; $E_r/h = h/(2m\lambda^2)$. The side peaks move at $h/(md)$ (the same as $2\hbar k/m$) relative to the centre, so they sit $h\,t/(md)$ away.

**Solution sketch:**
1. *Restate.* Given $\lambda = 1550$ nm, $m = 6.47\times10^{-26}$ kg, the table, $t = 0.020$ s. Want statistics, spacing, $E_r$, three ratios, a distance.
2. *Write state.* Counting rule; $d = \lambda/2$; $E_r = h^2/2m\lambda^2$; $U/J$; $\Delta x = h\,t/(md)$.
3. *Name move.* M11 (counting rule, J versus U), M6 (matter-wave momentum $h/\lambda$).
4. *Algebra.*
   - (a) K-39: $19 + 20 + 19 = 58$, even → boson. $d = 775$ nm. $E_r/h = 6.63\times10^{-34}/(2\times6.47\times10^{-26}\times(1.55\times10^{-6})^2) = 2.1\times10^3$ Hz.
   - (b) $264/137 = 1.9$ (superfluid); $499/19.6 = 25.5$ (superfluid, near the boundary); $652/5.9 = 110$ (Mott insulator). With 35 instead of 29 nothing moves: 25.5 is below both estimates and 110 above both.
   - (c) $h/(md) = 6.63\times10^{-34}/(6.47\times10^{-26}\times7.75\times10^{-7}) = 1.32\times10^{-2}$ m/s; $\Delta x = 0.0132\times0.020 = 2.6\times10^{-4}$ m ≈ 0.26 mm. Sharp peaks at depth 6, weaker ones at 14, none at 20.
5. *Check.* $J$ falls by about 23× from 6 to 20 $E_r$ while $U$ grows only about 2.5×, so the ratio moves mainly through $J$: the exponential tunnelling does the work, as in 4H.
6. *Answer.* K-39 is a boson; $d = 775$ nm, $E_r/h \approx 2.1$ kHz; $U/J \approx 1.9$, 25.5, 110: superfluid, superfluid near the edge, Mott (the same verdicts with 29 or 35); side peaks 0.26 mm from the centre after 20 ms, gone at the deepest setting.

Notice that nothing about the atom changed: only the laser power. That control is the simulator's selling point.

### Exercise C5.4 (writing)

Harrowmere Water & Power (fictional) spends £40 million a year (fictional) replacing corroded ductile-iron mains across its 2,400 km (fictional) network (shared fact sheet in `STRATEGY.md`). Its research board has £360,000 (hypothetical) for corrosion modelling and two proposals. (A) A three-year university partnership at £120,000 a year (hypothetical) to run cold-atom simulations of the Fermi-Hubbard model on an 8 × 8 lattice at half filling (64 sites, 128 spin-orbitals, 64 fermions), as a benchmark for the approximations its suppliers use for iron oxides. (B) £360,000 of classical HPC time this year for the suppliers' approximate oxide calculations. Write a 250-300 word F1 gain argument that decides **when** Harrowmere should put money into quantum simulation: now, through (A), or later.

**Hint:** Size the exact classical problem by counting configurations at fixed particle number, $\binom{128}{64}$, not $2^{128}$, and compare it with Day 07 Exercise 7.2's 10 PB machine. Then put both options on the same clock: when could each change the replacement bill, and what is 1% of that bill worth per year? Treat (A) as an option: what does Harrowmere lose by waiting, given that university results are published? Caveats: readout (averaged observables), analogue means one model (not the oxide), maturity (L179).

**Model paragraph:** (1) *Classical limit.* An exact state of the 8 × 8 Fermi-Hubbard lattice (64 fermions in 128 spin-orbitals) spans $\binom{128}{64} = 2.4\times10^{37}$ configurations; at 8 bytes each that is $1.9\times10^{38}$ B, about $2\times10^{22}$ times the 10 PB machine of Day 07 Exercise 7.2. Approximate classical methods are least trusted for strongly interacting fermions (judgement). (2) *Mechanism.* Fermionic atoms in an optical lattice obey this model directly, with $U/J$ set by laser power. (3) *Figure of merit.* Replacement spend avoided per pound of research, and how soon it arrives. (4) *Quantified gain.* The partnership returns double-occupancy and spin-correlation curves for a lattice model, each point averaged over thousands of runs, and they reach Harrowmere only through its suppliers' oxide models. A 1% cut in the £40 million bill (fictional) would be worth £0.4 million a year, but the partnership cannot influence an inhibitor choice before the end of year 3, plus supplier uptake (judgement). HPC time feeds this year's calculations. (5) *Maturity and practicality.* Analogue Fermi-Hubbard simulators are research instruments (L179); the partnership buys expertise and access, not a product. (6) *Verdict.* Spend the £360,000, 0.9% of one year's bill, on HPC now and defer the partnership. The option to fund quantum work is cheap to keep: university benchmarks are published, so waiting loses little knowledge, while money spent now buys answers inside the replacement cycle. Set a trigger to revisit: published cold-atom benchmarks showing that the suppliers' approximations mis-predict the model in the regime that matters for iron oxides. Caveat: if Harrowmere wants to steer which model is studied, a small co-funding stake is the hedge, not the full £360,000.

**What a weak answer misses:** It re-argues Day 07's inhibitor decision (HPC versus simulator access for one molecule) instead of the timing question. It sizes the problem with $2^{128}$ instead of counting configurations at fixed particle number. It claims the cold-atom lattice simulates the pipe, the oxide or the inhibitor. It treats "fund now" and "never" as the only choices, missing the value of waiting with a stated trigger. It ignores readout (averaged observables, not a state). It gives no verdict tied to the £40 million a year and the value of a 1% cut, or leaves invented figures unlabelled.

## 6. Cold attempt

Attempt this on paper before opening the sketch. Same type as §5, fresh numbers.

### Exercise C5.5 (quantitative)

A classical cluster tries to simulate 46 spin-½ particles. (a) How much memory does the state need in single and double precision? (b) The cluster can update $10^{11}$ amplitudes per second. How long does one sweep over the state take, and how long do 1,000 time steps take? (c) A 46-qubit analogue simulator measures the average magnetisation (outcomes ±1) to ±0.02 at 5 runs per second (fictional rate). How many runs and how long? (d) What does adding one more particle do to (a) and (b)?

**Hint:** $8\cdot2^N$ and $16\cdot2^N$ bytes. One sweep touches every amplitude once. Runs $\approx 1/\varepsilon^2$ (M3).

**Do not open the sketch until you have a written attempt.**

**Solution sketch:**
1. *Restate.* Given $N = 46$, $10^{11}$ amplitudes/s, 1,000 steps, $\varepsilon = 0.02$, 5 runs/s. Want two memories, two times, a run count and a time, a scaling.
2. *Write state.* Amplitudes $2^{46}$; memory $8\cdot2^{46}$ and $16\cdot2^{46}$; sweep time $2^{46}/10^{11}$; runs $1/\varepsilon^2$.
3. *Name move.* M11 (memory and evolution cost), M3 (shot-noise readout).
4. *Algebra.*
   - (a) $2^{46} = 7.04\times10^{13}$. Single: $5.6\times10^{14}$ B ≈ 563 TB. Double: $1.13\times10^{15}$ B ≈ 1,126 TB (1.1 PB).
   - (b) Sweep: $7.04\times10^{13}/10^{11} = 704$ s. 1,000 steps: $7.0\times10^5$ s ≈ 8.1 days.
   - (c) $1/0.02^2 = 2{,}500$ runs; $2{,}500/5 = 500$ s, about 8 minutes.
   - (d) $N = 47$ doubles both: 1.1 PB single, and about 16 days for 1,000 steps.
5. *Check.* $N = 46$ sits between the corrected Table 5.2 rows for 40 (8.8 TB) and 50 (9000 TB): $8.8\text{ TB}\times2^6 = 563$ TB, and $9000\text{ TB}/2^4 = 563$ TB. Consistent.
6. *Answer.* 563 TB (single) or 1.1 PB (double); 704 s per sweep, about 8 days for 1,000 steps; the simulator needs 2,500 runs (about 8 minutes) for one number to ±0.02; one more particle doubles the classical cost but adds one qubit.

If you got (c) wrong, revisit 4D: the simulator's cost is in repeated readout, and it buys you one observable, not the state.

## 7. Confusion log prompts

Answer each in writing (two or three sentences) after your pass through the lecture. Log the answer in your confusion log with the date.

1. Without notes, rebuild the corrected Table 5.2 from $8\cdot2^N$, and say in one sentence how you would spot the lecture's slip from the table alone.
2. "50 qubits replace 9000 TB." Write the two caveats you would attach to that sentence in a portfolio piece, and say which one limits a real simulator more.
3. Explain to a non-physicist why sharp interference peaks after release mean "superfluid" and a smooth blob means "Mott insulator", using the words phase, tunnelling and interaction.
4. (Optional) In one paragraph, say what makes the trapped-ion magnet an *analogue* simulator, and what a digital simulation of the same model would need instead.

## 8. Figures

One note per figure: what to look at, what it shows, the lecture line, and the trap.

**Fig 5.1 (simulating electrons using atoms, L65-L77).** Three panels. A: a metal crystal, positive ions on a grid with electrons between them: the system you want to understand. B: a lithium-6 atom, 3 p + 3 n in the nucleus and 3 e: the stand-in "electron" (a composite fermion, 4F). C: two crossed laser beams and a wavy egg-box surface with atoms in the dips: the optical lattice that replaces the ion grid. Read it left to right as "real thing → stand-in particle → stand-in crystal". Trap: in C the **atoms** play the electrons and the **light** plays the ions; the roles swap compared with A. Two beams give a 2D lattice; a 3D one needs three pairs (4H).

**Fig 5.2 (cold atoms, L81-L89).** A: an artist's view of a cloud held by six laser beams. B: a real photograph through a vacuum-chamber window of a MOT, the red glow being atoms scattering the cooling light. C: the optical table that does it: lasers, optics, electronics. What to take away: C is the SWaP-C reality behind every "atoms are easy to control" claim (L71). Trap: the glowing cloud in B is laser-cooled (sub-mK), not yet a BEC; condensation needs further cooling to hundreds of nK (4G).

**Fig 5.3 (superfluid versus Mott insulator, L103-L109).** A: one yellow sheet spread over many wells: a single delocalised wavefunction with one phase. B: one yellow ball per well: localised atoms with a fixed number per site. Trap: the picture shows one atom per site; the experiment's centre had 2-3 per site (4I), and what defines the Mott state is an integer number per site with no phase coherence, not "one atom each".

**Fig 5.4 (superfluid to Mott, time-of-flight images, caption at L113, misplaced under the BKT heading).** Eight absorption images a-h after releasing the atoms, with the lattice depth increasing downwards. Look at the central spot and the four side spots. In a the lattice is too shallow to diffract much; in b-e the side peaks at $\pm2\hbar k$ are sharp (phase coherence, superfluid); in f they fade; in g-h only a broad blob remains (Mott insulator). Trap: these are momentum distributions after expansion, not pictures of atoms in the lattice; peaks mean phase coherence (4I).

**Fig 5.5 (BKT mechanism, L121-L127).** Left, $T < T_c$: vortices (red hatched) and antivortices (blue open) sit in bound pairs, and the zoom shows opposite circulations that cancel at a distance. Right, $T > T_c$: free vortices everywhere: normal state. The double arrow is the transition at $T_\mathrm{BKT}$. Trap: $T_c$ here is the 2D BKT temperature, not the 3D BEC $T_c$ of 4G, and the ordered side has quasi-long-range order (4J).

**Fig 5.6 (BKT experiment with cold atoms, L129-L137).** a: a 1D lattice of light sheets slices the cloud into parallel 2D planes. b: an imaging beam passes through two released, overlapping planes onto a camera. Low temperature: straight, regular fringes (phase coherence). High temperature: wavy, irregular fringes. Insets with a 30 µm scale bar: a fringe pattern with a dislocation (a free vortex) and a washed-out one. Trap: the fringes come from interference **between two planes**, not from the lattice itself; a kink, not a missing fringe, is the vortex signature.

**Fig 5.7 (linear Paul trap, L141-L149).** A: four blade electrodes with two end-cap electrodes and a line of seven ions along the axis; a red laser beam crosses them. B: camera images of 1, 2, 3 and 9 ions, each a bright spot a few µm apart. What to take away: each spin is individually visible and addressable, which neutral atoms in a lattice only manage with special microscopes. Trap: the caption says "to the left / to the right" for panels labelled A and B.

**Fig 5.8 (two-ion quantum magnet, L157-L165).** A: the ramp. The hatched bar is the transverse field $B_x$, constant; the curve is the coupling $\lvert J(t)\rvert$ growing to $J_\mathrm{max}$; the dashed line marks $B_x = \lvert J\rvert$. Spins start along the field (paramagnet) and end in $\lvert\uparrow\uparrow\cdots\rangle + \lvert\downarrow\downarrow\cdots\rangle$, with the Hamiltonian terms written underneath (4K). B: the measured probabilities $P_{\uparrow\uparrow}$ (top) and $P_{\downarrow\downarrow}$ (bottom, axis inverted) against $\lvert J/B_x\rvert$ from 0 to about 5.5, each rising from 0.25 to 0.50. Trap: panel A draws three spins but the experiment used two ions; the lower axis is inverted, so the bars that shrink are probabilities that grow.

**Fig 5.9 (sharper transition with more ions, L169-L175).** Ferromagnetic order $m_x$ against $B/\lvert J\rvert$ on a log axis from 0.01 to 6, data for $N = 2$ (circles) and $N = 9$ (diamonds) with theory curves. Both fall from about 0.8 to near 0 as the field wins; the $N = 9$ drop is steeper. Trap: the horizontal axis is **field over coupling**, the inverse of Fig 5.8's, so ferromagnet is on the left here and on the right there. The plateau sits below 1 (judgement: imperfect state preparation and detection). The theory curves are the classical benchmark that makes the result trustworthy (4D).
