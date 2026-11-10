# Day 07: Quantum Simulation

**Time:** ~3 h · **Feeds:** Week 5 lecture (§5.1 to §5.5), inventory rows W5 Apply, W5 Consolidate, W5 quiz Q1 to Q4, W6 Explore · **Companion:** week05_companion.md §3 (notation and units), §4 (erratum L55, skipped step in Eq 5.2), §5 (clones)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min move M11 below (M11.1 to M11.8) · 50 min quantitative drills (Exercises 7.1 to 7.7; skip the two marked *stretch* if you are past time) · 45 min writing on the running case (Exercises 7.8 to 7.10) · 15 min companion pointer and confusion log.

The core is Moves M11.1 to M11.8 and Exercises 7.1, 7.2, 7.4, 7.6, 7.7 and two of the three writing exercises (7.9 and 7.10). Exercises 7.3 and 7.5 are stretch work; Exercise 7.8 (the Week 6 Explore piece) can move to Day 08's writing slot if today runs long.

## Why this matters

Week 5 has only two equations (Eq 5.1 and Eq 5.2, L23-33), and the whole argument of the week rests on one table: Table 5.2 (L55), which says how much RAM you need to store the state of $N$ spins. Two of its six rows are wrong by a factor of 10. You think in bytes for a living, so this is the week where you can out-check the lecture in five minutes. After that, the rest of the week is a short list of stories that each have one number in them: why a classical computer runs out of memory at about 50 spins, what a quantum simulator actually hands back (averages from repeated shots, not a state vector), the difference between building a copy of the Hamiltonian (analogue) and compiling it into gates (digital), why an atom can stand in for an electron, and what "superfluid to Mott insulator" means when you look at the camera image.

The engineering view, in one line: a state vector of $N$ spins is an array of $2^N$ complex numbers, and **every extra spin doubles the array**. A quantum simulator does not store that array anywhere you can read; it *is* the array, and you query it by sampling.

## Core concepts

### Move M11.1: $2^N$ amplitudes and $8\cdot2^N$ bytes (with the corrected Table 5.2)

**Idea.** One spin has two basis states, $|\uparrow\rangle$ and $|\downarrow\rangle$. By the tensor-product rule you already know from Module 3, $N$ spins have $2^N$ basis states, and a general state needs one complex amplitude for each (Table 5.1, L39-49, lists the 8 states for $N = 3$). The lecture stores each amplitude in single precision: 32 bits for the real part, 32 for the imaginary part, so 8 bytes (L53). Memory for the state:

$$\text{bytes} = 8\cdot 2^N \quad\text{(single precision)},\qquad 16\cdot 2^N \quad\text{(double precision, what most scientific codes use)}.$$

Recompute Table 5.2 yourself before reading on. Decimal prefixes (1 kB = $10^3$ B):

| $N$ | $2^N$ | $8\cdot2^N$ bytes | Lecture (L55) | Verdict |
|---|---|---|---|---|
| 3 | 8 | 64 B | 64 bytes | correct |
| 10 | 1024 | 8.2 kB | 8.2 kilobytes | correct |
| 20 | $1.05\times10^{6}$ | **8.4 MB** | 840 kilobytes | **wrong, 10× too small** |
| 30 | $1.07\times10^{9}$ | 8.6 GB | 8.6 gigabytes | correct |
| 40 | $1.10\times10^{12}$ | **8.8 TB** | 880 gigabytes | **wrong, 10× too small** |
| 50 | $1.13\times10^{15}$ | 9.0 PB (9000 TB) | 9000 terabytes | correct |

The quick check that catches the error: ten more spins multiply memory by $2^{10} = 1024\approx10^3$, so each row must be about 1000× the one above. 8.2 kB → 840 kB is only ×100, and 8.6 GB → 880 GB is only ×100. (Erratum L55, verified; see `docs/problem_inventory.md`.) The lecture's L59 also calls the 50-spin figure "disk space"; it is RAM, because a time-evolution code has to touch every amplitude at every step.

*Worked clone.* $N = 25$ spins: $2^{25} = 3.36\times10^{7}$ amplitudes, $8\times3.36\times10^{7} = 2.7\times10^{8}$ B $= 268$ MB in single precision, 537 MB in double. A laptop holds that easily. $N = 45$: $8\cdot2^{45} = 2.8\times10^{14}$ B $= 281$ TB, which is a large supercomputer's entire memory.

*You've got it when* you can rebuild Table 5.2 from "$\times1024$ per 10 spins" in your head, find both wrong rows, and say what double precision does (one more factor of 2, i.e. one spin fewer).

### Move M11.2: Evolution is a matrix, and Eq 5.2 hides a diagonalisation

**Idea.** Storing the state is the cheap part (the lecture says so at L57). Eq 5.2, $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$, needs the exponential of a $2^N\times2^N$ matrix. The step the lecture skips is how you exponentiate a matrix: go to the eigenbasis of $H$. If $H|n\rangle = E_n|n\rangle$, then $e^{-iHt/\hbar}|n\rangle = e^{-iE_nt/\hbar}|n\rangle$, so

$$|\psi(t)\rangle = \sum_n c_n\,e^{-iE_nt/\hbar}\,|n\rangle,\qquad c_n = \langle n|\psi(0)\rangle .$$

That is three steps: diagonalise $H$, project $|\psi(0)\rangle$ onto the eigenvectors, attach a phase to each. It is exactly the 2×2 eigenproblem you did in Module 3, made exponentially bigger.

*Worked clone (one spin, so you can see every line).* $H = \tfrac{\hbar\Omega}{2}\sigma_x$. Eigenvectors $|\pm\rangle = (|\uparrow\rangle\pm|\downarrow\rangle)/\sqrt2$ with $E_\pm = \pm\hbar\Omega/2$. Start in $|\uparrow\rangle = (|+\rangle + |-\rangle)/\sqrt2$. Then

$$|\psi(t)\rangle = \tfrac{1}{\sqrt2}\big(e^{-i\Omega t/2}|+\rangle + e^{+i\Omega t/2}|-\rangle\big) = \cos\tfrac{\Omega t}{2}|\uparrow\rangle - i\sin\tfrac{\Omega t}{2}|\downarrow\rangle,$$

so $P_\downarrow(t) = \sin^2(\Omega t/2)$: Day 03's Rabi formula, recovered by diagonalisation. With $\Omega = 2\pi\times1$ kHz and $t = 0.125$ ms, $\Omega t/2 = \pi/8$ and $P_\downarrow = 0.146$.

**Cost, in your units.** A dense $2^N\times2^N$ complex matrix in **double** precision (16 bytes per entry) takes $16\cdot4^N$ bytes, which is $2^N$ times the double-precision state itself. (Companion 4A quotes the single-precision figure, $8\cdot4^N$, half of this.) Dense diagonalisation costs of order $(2^N)^3 = 8^N$ operations (standard linear algebra; judgement on the constant). Real codes avoid the dense matrix: a Hamiltonian with only nearest-neighbour terms has about $N+1$ non-zero entries per row, so they store it sparsely and step the state forward with repeated matrix-vector products. That turns the bottleneck back into the state vector of M11.1, which is why $8\cdot2^N$ is the number everyone quotes.

*You've got it when* you can write the three-step recipe for $e^{-iHt/\hbar}$, redo the one-spin example, and say why the dense matrix is $2^N$ times worse than the state.

### Move M11.3: What a simulator outputs, and where classical methods still win

**Idea.** The lecture says the goal is "to find the full quantum state" (L61). No device can hand you that. Each run of a quantum simulator ends with a measurement that returns one bit string ($N$ bits: which spins are up), and the state is destroyed. You repeat the run $M$ times and average. What you get is **observables**: magnetisation, correlations between site $i$ and site $j$, the fraction of doubly occupied lattice sites, a camera image of the momentum distribution. The precision of any average of $\pm1$ outcomes is at best $1/\sqrt{M}$: this is Day 02's shot-noise law (M3), applied to runs instead of atoms. Reading out all $2^N$ amplitudes would need exponentially many runs, so it is never done.

That changes the comparison with classical computing. The relevant question is not "can I store $2^N$ amplitudes?" but "can I compute *this observable* to *this precision* some other way?" Often you can (judgement, in line with Georgescu et al. §I-II, see Read next):

- **Low entanglement (ground states of 1D chains, short times):** tensor networks (matrix product states) store the state as $N$ small matrices of size $\chi\times\chi$ ("bond dimension" $\chi$). Memory is about $2\chi^2N$ complex numbers, polynomial in $N$.
- **Bosons and unfrustrated magnets in equilibrium:** quantum Monte Carlo samples configurations and works well.
- **Where they break:** many interacting fermions (the "sign problem" spoils Monte Carlo), frustrated magnets, and dynamics after a sudden change, where entanglement grows and $\chi$ must grow exponentially with time. These are exactly the regimes quantum simulators target.

*Worked clone.* A 60-spin chain held as a matrix product state with $\chi = 128$: $2\times128^2\times60 = 1.97\times10^{6}$ complex numbers, about 16 MB in single precision. The full state would need $8\cdot2^{60} = 9.2\times10^{18}$ B, about 9.2 EB.

*You've got it when* you can say what one run returns, how the precision of an average scales with the number of runs, and name one regime where classical methods are fine and one where they are not.

### Move M11.4: Analogue versus digital simulation (Trotter in one paragraph)

**Idea.** The lecture describes simulators that "engineer the Hamiltonian" (L61) and never contrasts the two ways of doing it.

- **Analogue:** build a physical system whose own Hamiltonian *is* the model. Atoms in an optical lattice obey the Bose-Hubbard model; ions with laser-induced couplings obey a spin model. You turn knobs (laser power, magnetic field) and watch. Strengths: large $N$ today (hundreds to hundreds of thousands of particles), no gate overhead. Weaknesses: one family of models per machine, and no error correction, so you trust the answer only as far as you trust the calibration (judgement; Georgescu et al. §II).
- **Digital:** compile $e^{-iHt/\hbar}$ into gates on a general quantum computer. The standard trick is the **Trotter split**. If $H = A + B$ and you can do $e^{-iAt}$ and $e^{-iBt}$ separately but $A$ and $B$ do not commute, chop time into $n$ slices:

$$e^{-i(A+B)t} \approx \big(e^{-iAt/n}\,e^{-iBt/n}\big)^n,$$

with an error bounded by about $\tfrac{t^2}{2n}\big\|[A,B]\big\|$ (units with $\hbar = 1$; standard first-order bound, Georgescu et al. §II). More slices give a better answer and cost more gates. Strengths: any model, and in principle error-correctable. Weakness: gate counts are huge, and today's gates are noisy (Day 09 makes this quantitative).

*Worked clone.* Commutator norm 2, $t = 5$, target error 0.01: $n = t^2\|[A,B]\|/(2\varepsilon) = 25\times2/0.02 = 2500$ slices.

*You've got it when* you can state one strength and one weakness of each, write the Trotter formula from memory, and say which way the error moves as $n$ grows.

### Move M11.5: Bosons, fermions and the composite-particle rule

**Idea.** Electrons are fermions: no two in the same state. To simulate electrons in a solid with whole atoms you need atoms that are themselves fermions (L69). The rule: a composite particle is a **fermion if it contains an odd number of fermions** (protons, neutrons, electrons), and a boson if the number is even. A neutral atom has $Z$ protons, $Z$ electrons and $N_n$ neutrons, so the total is $2Z + N_n$ and **only the neutron number decides**: odd $N_n$ → fermion.

*Worked clone.* Helium-3: $Z = 2$, $N_n = 1$; total $2+2+1 = 5$, odd, fermion. Helium-4: $N_n = 2$; total 6, even, boson. Same element, opposite statistics. The lecture's lithium-6 (L69): $3+3+3 = 9$, fermion.

*You've got it when* you can classify any neutral isotope from its mass number $A$ and atomic number $Z$ in ten seconds ($N_n = A - Z$, then parity).

### Move M11.6: Bose-Einstein condensation, $\lambda_\text{th}$ versus spacing

**Idea.** The lecture's criterion (L81) is that BEC happens when the de Broglie wavelength becomes comparable to the spacing between particles. Make it a number. For a gas at temperature $T$ the relevant wavelength is the **thermal de Broglie wavelength**

$$\lambda_\text{th} = \frac{h}{\sqrt{2\pi m k_B T}},$$

and the spacing is $d = n^{-1/3}$ for number density $n$. The precise condition for an ideal uniform Bose gas is $n\lambda_\text{th}^3 \ge 2.612$, i.e. $\lambda_\text{th}\gtrsim1.38\,d$ (standard statistical physics; judgement, not in the lecture). Rearranged, the critical temperature is $T_c = \frac{2\pi\hbar^2}{mk_B}\big(\frac{n}{2.612}\big)^{2/3}$. Low density keeps the gas from forming a solid (L81), so $T_c$ ends up in the nanokelvin to microkelvin range.

*Worked clone (sodium-23, $m = 3.82\times10^{-26}$ kg, $n = 10^{20}\ \text{m}^{-3}$, $T = 1\ \mu$K).* $\lambda_\text{th} = 6.626\times10^{-34}/\sqrt{2\pi\times3.82\times10^{-26}\times1.381\times10^{-23}\times10^{-6}} = 3.6\times10^{-7}$ m. Spacing $d = (10^{20})^{-1/3} = 2.2\times10^{-7}$ m. $n\lambda_\text{th}^3 = 4.8 > 2.612$: condensed. $T_c = 1.5\ \mu$K. At room temperature the same atoms have $\lambda_\text{th} = 2.1\times10^{-11}$ m, ten thousand times smaller than the spacing.

*You've got it when* you can compute $\lambda_\text{th}$, $d$ and $n\lambda_\text{th}^3$ and say which side of 2.612 you are on.

### Move M11.7: Optical lattices and the Bose-Hubbard story ($J$ versus $U$)

**Idea.** Two counter-propagating laser beams of wavelength $\lambda$ form a standing wave whose intensity repeats every $\lambda/2$. Atoms are pulled to the bright (or dark) spots, so the lattice spacing is $d = \lambda/2$ (L71, L103). Three pairs of beams give a cubic crystal of light with no defects, and the laser power sets the well depth.

Two numbers run the physics (story level; the maths is skipped per the spec):

- **$J$, tunnelling:** how fast an atom hops to a neighbouring site. It falls *exponentially* as the wells get deeper.
- **$U$, on-site repulsion:** the energy cost of putting two atoms on the same site. It rises *slowly* with depth.

The Bose-Hubbard model is $H = -J\sum_{\langle i,j\rangle}b_i^\dagger b_j + \tfrac{U}{2}\sum_i n_i(n_i-1)$: a hopping term and a crowding penalty. Read the ratio $U/J$:

- **$U/J$ small → superfluid.** Atoms hop freely, each one is spread over many sites, and all sites share one phase. The number on any one site fluctuates.
- **$U/J$ large → Mott insulator.** Hopping is too slow to pay the crowding cost, so each site holds a fixed whole number of atoms, number fluctuations vanish, and the phase between sites becomes random.
- For one atom per site in a 3D cubic lattice there are two estimates of the switch: $U/J\approx29.3$ from quantum Monte Carlo (judgement; Capogrosso-Sansone et al. 2007, not a Target Source), and $5.83z\approx35$ from mean-field theory with $z = 6$ neighbours (mean field ignores fluctuations and overestimates it). This sprint takes **29** as the working value; no answer in Exercise 7.7 (or companion C5.3) changes if you use 35.

**What the interference peaks mean.** Switch the lattice off and let the cloud fly for a time $t_\text{TOF}$, then photograph it. In the superfluid every site emits a matter wave with the *same* phase, so they interfere like light through a diffraction grating: sharp peaks separated in velocity by $h/(md)$, i.e. in position by $\Delta x = h\,t_\text{TOF}/(md)$. In the Mott insulator the phases are random, the waves do not add coherently, and you see one broad blob (L103). Sharp peaks = phase coherence across the lattice; no peaks = localised atoms. That is the whole reading of the lecture's Fig 5.4.

*Worked clone.* Lattice lasers at 852 nm: $d = 426$ nm. Sodium-23 released for 10 ms: $h/(md) = 6.626\times10^{-34}/(3.82\times10^{-26}\times4.26\times10^{-7}) = 4.1\times10^{-2}$ m/s, so the peaks sit 0.41 mm apart.

*You've got it when* you can say what $J$ and $U$ each measure, which way each moves as the lattice deepens, and what sharp peaks versus a blob tell you.

### Move M11.8: Trapped-ion spin models, and why the transition is "sharper with $N$"

**Idea.** In a linear ion trap (L141, Fig 5.7) each ion is a spin: two internal levels play $|\uparrow\rangle$ and $|\downarrow\rangle$. The ions repel each other, so they share collective vibrations (phonons), like beads on a spring. A laser applies a force that depends on the spin; that force shakes the chain, and the shaking is felt by every other ion. The net effect is an effective spin-spin coupling (L153): an **Ising model** in words, "each pair of spins prefers to point the same way (or opposite ways), with a strength set by the lasers", plus a "transverse field" that tries to tip every spin sideways. Laser intensity and detuning set the coupling strength and how fast it falls off with distance.

Ramp the coupling up relative to the field and the ground state moves from paramagnetic (spins follow the field) to ferromagnetic (spins all aligned with each other) (L157). With 2 ions the change is a smooth crossover. A true phase transition is a sharp, non-analytic change that exists only for infinitely many particles; with more ions the crossover narrows towards it (L169: 2 to 9 ions). That is "sharper with $N$" (finite-size effect; judgement).

**Honest scale check.** Nine ions are $2^9 = 512$ amplitudes, 4 kB; sixteen ions are $8\cdot2^{16} = 524$ kB. Every ion experiment in the lecture can be checked on a laptop. That is a strength for validation, not an advantage claim: the advantage case needs regimes (large $N$, long-time dynamics, frustration) where the M11.3 shortcuts fail.

*You've got it when* you can explain phonon-mediated coupling in two sentences and say why a 2-ion "phase transition" is not yet a phase transition.

### Week 5 quiz pointers

The four quiz items and their flags are in the inventory key ("Quizzes" table, Week 5). Today's moves cover their reasoning: Q2 is M11.4's "special-purpose versus universal"; Q3's superposition option is the parallelism myth (one outcome per run, M11.3); Q4 is badly posed. Answer from the inventory key, not from memory of options.

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. Constants: $h = 6.626\times10^{-34}$ J s, $k_B = 1.381\times10^{-23}$ J/K, rubidium-87 mass $m_\text{Rb} = 1.443\times10^{-25}$ kg. Decimal prefixes throughout (1 TB $= 10^{12}$ B).

### Exercise 7.1 (quantitative)

(a) Without looking at Move M11.1, compute $8\cdot2^N$ bytes for $N = 20$ and $N = 40$ and compare with the lecture's Table 5.2 (L55). (b) Redo $N = 30$ and $N = 50$ in double precision. (c) A colleague's code stores amplitudes as two 64-bit floats and keeps three copies of the state (current, next, workspace). How much RAM for $N = 34$?

**Hint:** Ten more spins means $\times1024$. Double precision means 16 bytes per amplitude. Three copies means $\times3$.

**Solution sketch:**
- *Restate:* single-precision memory at two sizes, double-precision memory at two sizes, then a realistic code footprint.
- *Write state:* 8 B (single) or 16 B (double) per amplitude; $2^N$ amplitudes.
- *Name move:* M11.1.
- *Algebra:* (a) $8\times2^{20} = 8.39\times10^{6}$ B $= 8.4$ MB; $8\times2^{40} = 8.80\times10^{12}$ B $= 8.8$ TB. (b) $16\times2^{30} = 1.7\times10^{10}$ B $= 17$ GB; $16\times2^{50} = 1.8\times10^{16}$ B $= 18$ PB. (c) $3\times16\times2^{34} = 8.2\times10^{11}$ B $= 820$ GB.
- *Check:* 8.4 MB to 8.6 GB is ×1024 over ten spins, as it must be. The lecture's 840 kB and 880 GB fail this test.
- *Answer:* (a) 8.4 MB and 8.8 TB (lecture: 840 kB and 880 GB, both 10× too small; erratum L55). (b) 17 GB and 18 PB. (c) about 820 GB, so 34 spins already need a big-memory server.

### Exercise 7.2 (quantitative)

A (fictional) university cluster has 2 TB of RAM per node and 10 PB in total. Using double precision and one copy of the state: (a) what is the largest $N$ that fits on one node? (b) on the whole machine (ignore communication)? (c) The whole machine has 5000 times the memory of one node. How many extra spins does that buy, and what does that tell you about "just buy a bigger computer"?

**Hint:** Solve $16\cdot2^N\le$ memory, i.e. $N\le\log_2(\text{memory}/16)$, and round down.

**Solution sketch:**
- *Restate:* largest $N$ for two memory budgets, then the marginal return.
- *Write state:* $2\times10^{12}$ B and $10^{16}$ B; 16 B per amplitude.
- *Name move:* M11.1.
- *Algebra:* (a) $\log_2(2\times10^{12}/16) = \log_2(1.25\times10^{11}) = 36.9$, so $N = 36$ ($16\times2^{36} = 1.1\times10^{12}$ B; $N = 37$ needs $2.2\times10^{12}$ B). (b) $\log_2(10^{16}/16) = 49.2$, so $N = 49$ ($16\times2^{49} = 9.0\times10^{15}$ B). (c) $49 - 36 = 13$ spins; $\log_2 5000 = 12.3$.
- *Check:* multiplying memory by $2^{k}$ adds $k$ spins, and $2^{12.3}\approx5000$. Consistent.
- *Answer:* 36 spins per node, 49 on the whole machine. Five thousand times the hardware buys 13 spins. Memory grows linearly with money; the problem grows exponentially with $N$. This is the quantitative core of the W5 Consolidate and W6 Explore arguments.

### Exercise 7.3 (quantitative) (stretch)

(a) For $N = 16$ and $N = 20$ spins, how much memory does the dense $2^N\times2^N$ Hamiltonian need in double precision, and roughly how many operations does dense diagonalisation take? (b) One spin with $H = \tfrac{\hbar\Omega}{2}\sigma_x$, $\Omega = 2\pi\times250$ Hz, starts in $|\uparrow\rangle$. Use the eigenbasis method to find $P_\downarrow$ at $t = 1$ ms, and the first time the spin is fully flipped.

**Hint:** (a) $16\cdot4^N$ bytes and about $8^N$ operations (Move M11.2). (b) The worked clone gives $P_\downarrow = \sin^2(\Omega t/2)$; full flip when $\Omega t/2 = \pi/2$.

**Solution sketch:**
- *Restate:* dense-matrix memory and cost at two sizes; one-spin evolution by diagonalisation.
- *Write state:* (a) $N = 16, 20$. (b) $\Omega = 2\pi\times250\ \text{s}^{-1} = 1571\ \text{s}^{-1}$, $t = 10^{-3}$ s.
- *Name move:* M11.2.
- *Algebra:* (a) $N = 16$: $16\times4^{16} = 6.9\times10^{10}$ B $= 69$ GB; $8^{16} = 2.8\times10^{14}$ operations. $N = 20$: $16\times4^{20} = 1.8\times10^{13}$ B $= 18$ TB; $8^{20} = 1.2\times10^{18}$ operations. Compare the state itself at $N = 20$: 8.4 MB. (b) $\Omega t/2 = 2\pi\times250\times10^{-3}/2 = \pi/4$; $P_\downarrow = \sin^2(\pi/4) = 0.50$. Full flip: $t = \pi/\Omega = 1/(2\times250) = 2$ ms.
- *Check:* the dense matrix at $N = 20$ is $2^{20}\approx10^6$ times the double-precision state (16.8 MB), as M11.2 predicts.
- *Answer:* (a) 69 GB and $\sim3\times10^{14}$ operations at 16 spins; 18 TB and $\sim10^{18}$ operations at 20 spins, against 8.4 MB for the state. That is why real codes never form the dense matrix. (b) $P_\downarrow = 0.50$ at 1 ms; full flip at 2 ms.

### Exercise 7.4 (quantitative)

(a) A 100-spin chain in a weakly entangled state is stored as a matrix product state with bond dimension $\chi = 256$, single precision. Memory, against the full state vector? (b) A quantum simulator measures a single-spin observable with outcomes $\pm1$. How many runs $M$ give a standard error of 0.005? (c) How long does that take at 20 s per run (typical of a cold-atom machine, judgement) and at 10 ms per run (an ion trap, judgement)?

**Hint:** (a) $2\chi^2N$ complex numbers at 8 B each (Move M11.3). (b) Error $\le1/\sqrt{M}$, so $M = 1/\varepsilon^2$. (c) Multiply.

**Solution sketch:**
- *Restate:* compressed versus full memory; runs for a target precision; wall-clock time.
- *Write state:* $N = 100$, $\chi = 256$; $\varepsilon = 0.005$; 20 s and 0.01 s per run.
- *Name move:* M11.3 with M3 (shot noise).
- *Algebra:* (a) $2\times256^2\times100\times8 = 1.05\times10^{8}$ B $\approx105$ MB; full state $8\times2^{100} = 1.0\times10^{31}$ B. (b) $M = 1/0.005^2 = 4.0\times10^{4}$ runs. (c) $4\times10^{4}\times20 = 8.0\times10^{5}$ s $= 222$ h $\approx9.3$ days; $4\times10^{4}\times0.01 = 400$ s, about 6.7 min.
- *Check:* halving $\varepsilon$ quadruples $M$, the same $1/\sqrt{\ }$ law as Day 02.
- *Answer:* (a) about 105 MB versus $10^{31}$ B: when entanglement is low, the classical shortcut wins outright. (b) 40,000 runs. (c) about 9 days on a slow cold-atom cycle, under 7 minutes on an ion trap. Repetition rate is a real practicality term in any simulator argument.

### Exercise 7.5 (quantitative) (stretch)

A digital simulation of a 50-spin chain uses $H = A + B$ ($A$: 49 nearest-neighbour couplings; $B$: 50 single-spin field terms). For this (fictional) model $\|[A,B]\| = 4$ in units with $\hbar = 1$, the target time is $t = 10$, and the target Trotter error is 0.01. (a) How many Trotter slices $n$? (b) Each slice uses one gate per term. Total gates? (c) With gate fidelity 0.999, after how many gates has the overall success probability fallen to one half (treat it as $0.999^{g}$)? Conclusion?

**Hint:** (a) $n = t^2\|[A,B]\|/(2\varepsilon)$ (Move M11.4). (b) Gates per slice $= 49 + 50$. (c) Solve $0.999^g = 0.5$ with logs.

**Solution sketch:**
- *Restate:* Trotter slices, total gate count, and the gate budget allowed by noise.
- *Write state:* $t = 10$, $\|[A,B]\| = 4$, $\varepsilon = 0.01$; 99 terms; $F = 0.999$.
- *Name move:* M11.4 (with a preview of Day 09's depth-from-fidelity, M13).
- *Algebra:* (a) $n = 100\times4/0.02 = 2.0\times10^{4}$. (b) $2.0\times10^{4}\times99 = 1.98\times10^{6}$ gates. (c) $g = \ln0.5/\ln0.999 = 693$ gates.
- *Check:* the noise budget (about 700 gates) is about 2900 times smaller than the requirement ($1.98\times10^6/693$).
- *Answer:* $2\times10^{4}$ slices, about $2\times10^{6}$ gates, against a budget of about 693 gates at 99.9% fidelity. Uncorrected digital simulation of this problem is hopeless; it needs error correction (Day 09) or a smarter split. Analogue machines dodge the gate count, which is why they lead today.

### Exercise 7.6 (quantitative)

(a) Classify as boson or fermion, showing the count: lithium-7 ($Z = 3$), potassium-40 ($Z = 19$), rubidium-87 ($Z = 37$), sodium-23 ($Z = 11$), strontium-87 ($Z = 38$). Which of these could stand in for electrons? (b) Rubidium-87 gas at density $n = 10^{20}\ \text{m}^{-3}$: find the spacing $d$, and $\lambda_\text{th}$ and $n\lambda_\text{th}^3$ at $T = 2\ \mu$K and $T = 200$ nK. Which is condensed? (c) Find $T_c$ at this density.

**Hint:** (a) $N_n = A - Z$; odd neutron number → fermion for a neutral atom (Move M11.5). (b) $d = n^{-1/3}$, $\lambda_\text{th} = h/\sqrt{2\pi mk_BT}$, condensed if $n\lambda_\text{th}^3\ge2.612$ (Move M11.6). (c) $T_c = \frac{2\pi\hbar^2}{mk_B}(n/2.612)^{2/3}$, or scale from (b): $n\lambda_\text{th}^3\propto T^{-3/2}$.

**Solution sketch:**
- *Restate:* five parity counts; spacing, thermal wavelength and phase-space density at two temperatures; critical temperature.
- *Write state:* (a) $N_n$ = 4, 21, 50, 12, 49. (b) $m = 1.443\times10^{-25}$ kg, $n = 10^{20}\ \text{m}^{-3}$.
- *Name move:* M11.5, M11.6.
- *Algebra:* (a) Li-7: $3+3+4 = 10$, boson. K-40: $19+19+21 = 59$, fermion. Rb-87: $37+37+50 = 124$, boson. Na-23: $11+11+12 = 34$, boson. Sr-87: $38+38+49 = 125$, fermion. (b) $d = 10^{-20/3} = 2.15\times10^{-7}$ m. At 2 µK: $\lambda_\text{th} = 6.626\times10^{-34}/\sqrt{2\pi\times1.443\times10^{-25}\times1.381\times10^{-23}\times2\times10^{-6}} = 1.32\times10^{-7}$ m; $n\lambda_\text{th}^3 = 0.23$. At 200 nK: $\lambda_\text{th} = 4.19\times10^{-7}$ m; $n\lambda_\text{th}^3 = 7.3$. (c) $T_c = 2\ \mu\text{K}\times(0.23/2.612)^{2/3} = 0.40\ \mu$K, about 400 nK.
- *Check:* cooling by 10× raises $n\lambda_\text{th}^3$ by $10^{3/2} = 31.6$, and $7.3/0.23 = 31.6$. Consistent. Heavier rubidium needs a lower $T_c$ than sodium's 1.5 µK at the same density (M11.6 clone), as $T_c\propto1/m$ predicts.
- *Answer:* (a) fermions: K-40 and Sr-87 (odd neutron number), so these can stand in for electrons; Li-7, Rb-87 and Na-23 are bosons. (b) $d = 215$ nm; at 2 µK, $\lambda_\text{th} = 132$ nm and $n\lambda_\text{th}^3 = 0.23$ (not condensed); at 200 nK, $\lambda_\text{th} = 419$ nm and $n\lambda_\text{th}^3 = 7.3$ (condensed). (c) $T_c\approx400$ nK.

### Exercise 7.7 (quantitative)

A cubic optical lattice is made from 1064 nm lasers and loaded with rubidium-87. (a) Lattice spacing? (b) The atoms fill a cube 25 µm on a side; how many sites, and what is the mean filling for $1.2\times10^{5}$ atoms? (c) For four lattice depths (in units of the recoil energy $E_r$), standard deep-lattice approximations give (judgement, rounded): depth 5: $J/h = 175$ Hz, $U/h = 340$ Hz; depth 10: 46 Hz, 570 Hz; depth 15: 15 Hz, 770 Hz; depth 20: 5.6 Hz, 960 Hz. Compute $U/J$ for each and say which are superfluid and which are Mott insulators (take the switch at $U/J\approx29$; would the mean-field 35 change any verdict?). (d) In the superfluid, after 15 ms of free flight, how far apart are the interference peaks? What do you expect to see at depth 20?

**Hint:** (a) $d = \lambda/2$. (b) Sites $= (L/d)^3$. (c) Divide; compare with 29 (Move M11.7). (d) $\Delta x = h\,t_\text{TOF}/(md)$.

**Solution sketch:**
- *Restate:* spacing, site count and filling, phase at four depths, peak spacing.
- *Write state:* $\lambda = 1064$ nm; $L = 25\ \mu$m; $1.2\times10^{5}$ atoms; the $J$, $U$ table; $t_\text{TOF} = 0.015$ s.
- *Name move:* M11.7.
- *Algebra:* (a) $d = 532$ nm. (b) $25/0.532 = 47.0$ sites per side; $47.0^3 = 1.04\times10^{5}$ sites; filling $1.2\times10^{5}/1.04\times10^{5} = 1.16$. (c) $340/175 = 1.9$; $570/46 = 12.4$; $770/15 = 51$; $960/5.6 = 171$. No ratio lies between 29 and 35, so the mean-field boundary gives the same verdicts. (d) $h/(md) = 6.626\times10^{-34}/(1.443\times10^{-25}\times5.32\times10^{-7}) = 8.6\times10^{-3}$ m/s; $\times0.015$ s $= 1.3\times10^{-4}$ m $= 129\ \mu$m.
- *Check:* deepening the lattice cuts $J$ by about 30× (175 → 5.6 Hz) while $U$ less than triples, so the ratio moves almost entirely through $J$, as M11.7 says.
- *Answer:* (a) 532 nm. (b) about $1.04\times10^{5}$ sites, about 1.2 atoms per site. (c) $U/J$ = 1.9, 12.4, 51, 171: depths 5 and 10 are superfluid, 15 and 20 are Mott insulators, with 29 or 35 alike; the switch lies between 10 and 15. (d) peaks about 129 µm apart; at depth 20 the peaks are gone and you see one broad cloud, because each site has a fixed atom number and an undefined phase.

### Exercise 7.8 (writing)

*Inventory row W6 Explore.* In 200 words, summarise the limits of conventional computing for a reader on **Harrowmere Water & Power**'s (fictional) technology board, and say where Harrowmere already relies on high-end computing. Use at least one number you computed today.

**Hint:** Separate the two limits: general slowdown of hardware improvement (judgement, keep it short) and the specific exponential wall for quantum systems (Exercise 7.2). Then name where Harrowmere uses HPC today and say which of those uses hit the wall (most do not).

**Model paragraph:**
Harrowmere Water & Power (fictional) already relies on high-end computing for three jobs: hydraulic models of its 2,400 km of water mains, rainfall and reservoir-inflow forecasts, and materials calculations bought from suppliers to understand the corrosion of its ductile-iron mains, which drives £40 million a year of replacement (fictional figures). The first two are classical physics: their cost grows roughly in proportion to the size of the network or the weather grid, so more hardware buys proportionally more detail. Their limit is money and energy, not principle (judgement). The third job is different. Corrosion and catalysis are decided by electrons, and an exact description of $N$ interacting quantum particles needs $2^N$ complex numbers. In double precision, 36 spins fill a 2 TB node and 49 fill a whole 10 PB machine; 5,000 times the hardware buys 13 more particles. A rust layer has far more than 49 relevant electrons, so exact simulation is impossible at any budget, and Harrowmere's suppliers use approximate methods that work well for some materials and fail for strongly interacting ones. That exponential wall, not general hardware slowdown, is the opening quantum simulators aim at. Caveat: the wall applies to *exact* methods; most of Harrowmere's computing never meets it.

**What a weak answer misses:** It says "classical computers are too slow" with no number and no distinction between polynomial jobs (hydraulics) and exponential ones (many-electron quantum systems). It quotes the lecture's Table 5.2 uncorrected (840 kB, 880 GB). It forgets that approximate classical methods exist, so it implies every chemistry problem is out of reach. It names a real supercomputer or vendor instead of keeping figures sourced or labelled fictional.

### Exercise 7.9 (writing)

*Inventory row W5 Apply.* Select a type of quantum simulation and write 200-300 words on how the quantum approach could matter for **Harrowmere Water & Power**'s (fictional) problem: the iron-oxide layers that form inside its ductile-iron mains, whose electronic behaviour controls how fast corrosion proceeds. Corrosion drives £40 million a year of mains replacement across 2,400 km of mains (fictional).

**Hint:** Pick one: analogue cold-atom lattice (fermionic atoms for electrons), analogue trapped-ion spin model, or digital. Say what model it would simulate (not "the pipe"), why the model is classically hard, what observable would come out, and how that feeds back to Harrowmere. Use M11.5 to justify the atom choice.

**Model paragraph:**
I would choose an analogue cold-atom simulator of the Fermi-Hubbard model, the textbook model for electrons that hop between lattice sites and repel each other when they share one. Iron oxides of the kind that grow inside Harrowmere's ductile-iron mains, whose corrosion drives £40 million a year of replacement (fictional), are strongly interacting electron systems, and the cheap approximations used in materials codes treat that repulsion with an adjustable correction whose value changes the predicted electronic behaviour (judgement). The simulator replaces electrons with fermionic atoms. Potassium-40 qualifies because it has 21 neutrons, an odd total of 59 fermions, so it obeys the same exclusion rule as an electron. Atoms in an optical lattice made from 1064 nm light sit 532 nm apart, and the laser power tunes the ratio of repulsion $U$ to tunnelling $J$ continuously, something no real oxide allows. The output is observables averaged over many runs: how many sites are doubly occupied, and whether neighbouring spins line up, for each $U/J$. Those curves become benchmarks: if a classical method reproduces the simulator across the range of $U/J$, Harrowmere's suppliers can trust it for oxide calculations. The value is indirect. The simulator does not model a pipe, contain water or chloride, or deliver a corrosion rate. It tests the models that do. Maturity is research-lab only (lecture L179), and the hardest regime, cold enough to show long-range magnetic order, is still a frontier (judgement). So for Harrowmere the simulator cannot touch this year's replacement bill; it is a watch-and-partner item for the suppliers' modelling, not a purchase.

**What a weak answer misses:** It says the simulator will "simulate the pipe" or "predict corrosion", skipping the model-mapping step (real material → lattice model → atoms). It picks a bosonic atom (rubidium-87) to stand in for electrons. It promises output of "the full quantum state" rather than averaged observables. It has no maturity statement, or it borrows a lecture case (the Mott or ion experiments) as its own example.

### Exercise 7.10 (writing)

*Inventory row W5 Consolidate.* In 300 words, using all six parts of F1, advise Harrowmere's (fictional) materials team on one decision. Corrosion of its ductile-iron mains drives £40 million a year of replacement (fictional). The team has a hypothetical budget of £180,000 for one year to study how a candidate corrosion-inhibitor molecule binds to the iron-oxide layer, and must choose between classical HPC time and access to a quantum simulator. The team's chemists (hypothetical) say an exact treatment of the binding site needs 60 spin-orbitals holding 30 electrons.

**Hint:** Size the exact problem with the counting that respects electron number: $\binom{60}{30}$ configurations rather than $2^{60}$, at 8 B each, and compare it with a memory figure of the same kind (Exercise 7.2's whole machine, single precision). For the digital route, use Exercise 7.5 only as a lower bound and say why. Compare the budget with the replacement bill in the same units (pounds per year). The verdict must turn on Harrowmere's constraint: the study is worth doing only if it can change what inhibitor Harrowmere specifies.

**Model paragraph:**
(1) *Classical limit.* An exact treatment of the inhibitor's binding site (hypothetical: 60 spin-orbitals, 30 electrons) has $\binom{60}{30} = 1.2\times10^{17}$ electron configurations. At 8 bytes each, one state needs about 940 PB, roughly 94 times the 10 PB total memory of the cluster in Exercise 7.2, before any workspace. Exact classical simulation is out of reach. (2) *Mechanism.* A quantum simulator would hold that state in about 60 qubits, one per spin-orbital, and evolve it under a compiled Hamiltonian. (3) *Figure of merit.* Whether the binding-energy ranking of candidate inhibitors is accurate enough to change what Harrowmere specifies, per pound spent. (4) *Quantified gain.* Memory falls from $10^{17}$ numbers to about 60 qubits. Run time does not follow: Exercise 7.5's 50-spin chain, with only 99 terms, already needed about $2\times10^{6}$ gates against a budget of about 700 at 99.9% gate fidelity, and a 60-orbital chemistry Hamiltonian has far more terms (judgement), so the gap only widens. The analogue machines that do run at scale simulate lattice models, not this molecule on this oxide. (5) *Maturity and practicality.* The lecture places quantum simulators in the research phase (L179). Access would buy benchmark runs, not an inhibitor ranking. HPC running approximate methods on a reduced active space produces a ranking this year. (6) *Verdict.* Spend the £180,000 on HPC. That is 0.45% of one year's £40 million replacement bill (fictional), so it is justified if the ranking shifts the inhibitor choice even slightly; quantum access cannot shift it within the year. The caveat: the 60-orbital figure is the chemists' estimate. If approximate methods disagree with each other on the binding site, that disagreement is the signal to revisit quantum routes, on the timescale of error-corrected machines.

**What a weak answer misses:** It uses $2^{60}$ without noting that fixed electron number reduces the count, or it copies the lecture's 880 GB-style figures. It compares a memory figure with a machine of a different kind (single-precision state against a node, or bytes against operations). It quotes "exponential speed-up" with no gate count and no fidelity budget. It recommends quantum access as if a research-phase simulator could rank inhibitors. Its verdict would read the same for any company, because it never ties the spend to Harrowmere's £40 million a year or to the inhibitor decision.

## Anti-patterns / Common mistakes

- **Copying Table 5.2.** How you'd notice: consecutive rows differ by ×100 instead of ×1024. Instead: recompute $8\cdot2^N$ and flag L55 (20 spins: 8.4 MB; 40 spins: 8.8 TB).
- **Mixing binary and decimal prefixes silently.** How you'd notice: your 8.8 TB comes out as 8.0. Instead: state "decimal prefixes" (as here) or use TiB, and stick to one.
- **"The simulator gives us the full quantum state."** How you'd notice: no mention of runs or averages. Instead: one bit string per run; observables to $1/\sqrt{M}$ precision (M11.3, correcting the wording of L61).
- **Treating $2^N$ as the end of the classical story.** How you'd notice: your argument has no regime where classical methods win. Instead: name tensor networks and Monte Carlo, and say why your problem escapes them (fermions, frustration, dynamics).
- **Conflating analogue and digital.** How you'd notice: you quote gate counts for a cold-atom lattice, or "any problem" for an analogue machine. Instead: analogue = one model family, large $N$, no error correction; digital = any model, huge gate counts.
- **Counting only protons and electrons.** How you'd notice: every neutral atom comes out a boson. Instead: count neutrons; for a neutral atom, odd $N_n$ means fermion.
- **Using $\lambda_\text{dB} = h/(mv)$ with a guessed speed for BEC.** How you'd notice: answers depend on what $v$ you picked. Instead: use $\lambda_\text{th} = h/\sqrt{2\pi mk_BT}$ and compare $n\lambda_\text{th}^3$ with 2.612.
- **Reading the Mott transition as "atoms freeze".** How you'd notice: you cannot say what the peaks mean. Instead: Mott = fixed number per site, random phase, no peaks; it is driven by $U/J$, not by temperature.
- **Calling a 2-ion experiment a phase transition or a quantum advantage.** How you'd notice: 2 to 16 spins fit in kilobytes. Instead: a demonstration of building blocks, valuable for validation.

## Done when

Without notes, in 40 minutes, you can do all of the following. Pass mark: 7 of 9.

1. Rebuild the corrected Table 5.2 for $N = 3$ to 50 and name the two wrong lecture rows.
2. Find the largest $N$ that fits in a given RAM budget, in single or double precision.
3. Write $|\psi(t)\rangle = \sum_n c_ne^{-iE_nt/\hbar}|n\rangle$ and explain why the dense Hamiltonian is $2^N$ times bigger than the state.
4. Say what a simulator run returns and how many runs a target precision needs; name one regime where classical approximations work and one where they fail.
5. Contrast analogue and digital simulation, and write the Trotter formula with the direction of its error.
6. Classify any neutral isotope as boson or fermion from $A$ and $Z$.
7. Compute $\lambda_\text{th}$, $d$ and $n\lambda_\text{th}^3$ and decide whether a gas is condensed.
8. Explain $J$ versus $U$, the superfluid and Mott phases, and what the interference peaks show, including the peak spacing $h\,t_\text{TOF}/(md)$.
9. Explain phonon-mediated spin coupling in trapped ions and why the transition sharpens with $N$.

## Companion pointer and confusion log

Open `content/companions/week05_companion.md` (§3 notation and units, §4 erratum L55 and the skipped diagonalisation in Eq 5.2). Read lecture L35-61 with Moves M11.1 to M11.3 beside you, then L99-103 with M11.7 and L141-169 with M11.8. Log every term you had to look up twice (Hamiltonian, unitary, Feshbach, Mott, phonon, paramagnetic) with its lecture line.

| Term or line | What confused me | Resolution |
|---|---|---|
| | | |
| | | |

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 06 (crypto and QKD: M8 to M10).**
1. Eve intercepts and resends every BB84 photon in a random basis. What QBER does she cause on the sifted key?
2. Alice and Bob compare 20 sifted bits. What is the chance Eve's intercept-resend goes unnoticed?
3. A link runs 50 km over fibre with 0.2 dB/km loss (typical telecom fibre). What fraction of photons arrives?
4. State the classical bound and the quantum maximum for the CHSH quantity.
5. Mosca's rule: data must stay secret for 10 years, migration takes 5 years, and a cryptographically relevant quantum computer is 12 years away. Act now or wait?

**From Day 04 (interferometry: M6 and M7).**
6. Rubidium-87 on its 780 nm line, $T = 0.1$ s: what is $k_\text{eff}$ and $\Phi = k_\text{eff}gT^2$?

**From Day 02 (sensor figures of merit: M2 and M3).**
7. A magnetometer has $2\ \text{fT}/\sqrt{\text{Hz}}$. What is its noise in a 100 Hz bandwidth?
8. With $N = 10^{6}$ particles, what are the shot-noise and Heisenberg phase limits?

*Answers.* 1. 25%. 2. $(3/4)^{20} = 3.2\times10^{-3}$. 3. 10 dB loss, so $10^{-1} = 0.10$. 4. 2 and $2\sqrt2\approx2.83$. 5. $x + y = 15 > z = 12$: act now. 6. $k_\text{eff} = 4\pi/780\ \text{nm} = 1.61\times10^{7}\ \text{m}^{-1}$; $\Phi = 1.61\times10^{7}\times9.81\times0.01 = 1.58\times10^{6}$ rad. 7. $2\times\sqrt{100} = 20$ fT. 8. $1/\sqrt N = 10^{-3}$ rad and $1/N = 10^{-6}$ rad.

## Read next

- Georgescu, Ashhab and Nori, *Quantum simulation*, Rev. Mod. Phys. 86, 153 (2014), <https://arxiv.org/abs/1308.6253>. Read §I (why classical simulation fails, and the classical methods that sometimes succeed), §II (analogue versus digital simulation, including the Trotter decomposition) and §III (the platforms: cold atoms, trapped ions and others).
- Aspuru-Guzik and Walther, *Photonic quantum simulators*, Nat. Phys. 8, 285 (2012), author copy (draft title "Photonic Quantum Orreries"), <https://dash.harvard.edu/bitstream/handle/1/11881655/aspuru-guzik-photonic-quantum-simulators.pdf?sequence=1>. Read the introduction for a second, short statement of the analogue-versus-digital distinction and of what a simulator is for.
