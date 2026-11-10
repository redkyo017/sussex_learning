# Week 04 Companion - Quantum communication

**Built on:** Day 06 (M8 crypto in one page, M9 BB84 by hand and no-cloning, M10 CHSH, fibre loss and repeaters)
**Feeds:** Portfolio (Assessment 2) through the Week 4 Consolidate piece. Nothing here is aimed at Assessment 1.

Line numbers `L..` refer to `week_4/week_4_lecture.md`. Figure numbers refer to `week_4/figures/fig4_N.png`; the two BB84 tables are `fig4_table1.png` and `fig4_table2.png`. Read this alongside the lecture, not instead of it.

## 1. Read these first (Pass 0)

Before you read the lecture, know what the week asks you to do with it. Types only, no solutions.

1. **Explore quiz (4 MCQ):** where encryption is needed; what is true about quantum communication; what a qubit is; what quantum cryptography is. Answers: see the inventory key (`docs/problem_inventory.md`, Week 4 rows). Q4 is flagged there as loose: QKD distributes a key, the encryption itself is classical.
2. **Apply (forum, 200-300 words):** pick one application area of quantum communication and argue how it matters there. Type: F1 gain argument, short form.
3. **Consolidate (portfolio, 300 words):** how a quantum-based solution gives more security than classical communication, with the gain **and** the downsides, quantified (bit rates, required fidelities) and with practical aspects. Type: F1 gain argument with numbers from M8, M9 and M10.
4. **Checkpoint quiz:** the same four questions as Explore with the options shuffled. See the inventory key.
5. **Optional interactive:** QuVis BB84 simulation (controls, eavesdrop button, challenges page). Walkthrough in §9.

The quantitative side the week expects of you is small: run BB84 by hand, explain why intercept-resend gives a 25% error rate on the sifted key and why the chance of missing Eve falls as $(3/4)^n$, compute the CHSH values 2 and $2\sqrt2$, and turn a fibre length into a transmission. Sections 4-6 drill exactly that.

## 2. What the lecture is doing, in one picture

Two people want to share a secret random key; once they have one, a classical cipher (a one-time pad, or AES) does the encrypting. Classically the key exchange rests on a maths problem being hard, which a quantum computer may break. The quantum idea is different: send the key bits on single photons in one of two incompatible polarisation bases. Anyone who looks at a photon must pick a basis, and picking the wrong one disturbs it, so an eavesdropper leaves errors that Alice and Bob can count. No-cloning (L45-L61) is the reason she cannot copy first and look later. BB84 (L65-L102) is the prepare-and-measure version, B92 (L104-L121) a two-state variant, and E91 (L123-L142) the entanglement version, which checks for Eve with a Bell (CHSH) test. The second half (L146-L219) is engineering: photons are lost in fibre exponentially with distance, quantum signals cannot be amplified, so long links today use trusted nodes or satellites, and true quantum repeaters are still in the lab.

The lecture states the security idea well but skips most of the numbers, gets the repeater physics backwards at L152, and mis-states one B92 figure (L121). Section 4 fixes these.

Free reading if you want more than the lecture: Pirandola et al., *Advances in quantum cryptography*, https://arxiv.org/abs/1906.01645 (§1, the BB84 section, and the practical and satellite sections); the NCSC white paper, *Quantum security technologies*, https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies (all; the official UK view of QKD versus post-quantum cryptography); Chapman & Peters, https://physics.aps.org/articles/v15/172 (satellite QKD, short).

## 3. Notation and unit decoder

Several symbols in this lecture have two meanings, and other sources use a different convention. The "clash" column is the reason this table exists.

| Symbol as written | Read it as | Unit | Where (lecture line) | Clash / trap | Move |
|---|---|---|---|---|---|
| $\lvert0\rangle$, $\lvert1\rangle$ | the two computational basis states of a qubit | none | L51-L55 | for a photon, $\lvert0\rangle = \lvert H\rangle$, $\lvert1\rangle = \lvert V\rangle$ in the R basis | M9 |
| $\alpha$, $\beta$ | complex amplitudes, $\lvert\alpha\rvert^2+\lvert\beta\rvert^2 = 1$ | none | L51 | L53 writes $\alpha^2$; read it as $\alpha\cdot\alpha$ from the product, not a probability | M9 |
| $U_\mathrm{cl}$ | a hypothetical cloning unitary acting on (input, blank) | none | L51-L57 | L55 writes "$U_\mathrm{cl}\alpha\lvert00\rangle$"; read it as $\alpha\,U_\mathrm{cl}\lvert00\rangle$ | M9 |
| $\lvert\phi\rangle\lvert0\rangle$ | two-qubit product state: unknown input, blank target | none | L53 | the same as $\lvert\phi\rangle\otimes\lvert0\rangle$ | M9 |
| R | rectilinear basis: H and V | none | Fig 4.3, Tables 4.1-4.3 | many sources (Pirandola, many simulators) write this basis as "+" | M9 |
| D | diagonal basis: +45° and −45° | none | Fig 4.3, Tables 4.1-4.3 | many sources write this basis as "×" | M9 |
| H, V | horizontal (bit 0), vertical (bit 1) polarisation | none | Fig 4.3, L106 | | M9 |
| "+", "−" in the tables | the **states** +45° (bit 0) and −45° (bit 1) | none | Fig 4.3, Tables 4.1-4.2 | in the lecture "+" is a state; in "+/×" notation it is a basis. Check which before reading any table | M9 |
| $\lvert\pm\rangle$ | $(\lvert H\rangle\pm\lvert V\rangle)/\sqrt2$, the ±45° states | none | not in lecture | the lecture's "+" and "−" rows are these kets | M9 |
| $\lvert D\rangle$, $\lvert A\rangle$ (Day 06) | the +45° and −45° states: Day 06's $\lvert D\rangle \equiv$ the lecture's "+" (bit 0), $\lvert A\rangle \equiv$ the lecture's "−" (bit 1) | none | Day 06 M9.1 | Day 06 uses D both for the diagonal **basis** and for the +45° **state**; context decides | M9 |
| QBER | quantum bit error rate: fraction of **sifted** bits where Bob ≠ Alice | fraction or % | implicit at L93, L102 | measured on sifted bits only, never on the raw string | M9 |
| $\langle ab\rangle$ | expectation (correlation) of Alice's ±1 result at setting $a$ with Bob's at $b$ | none, in $[-1, 1]$ | L137-L142 | lower-case and capital letters are **different settings**, not different people | M10 |
| $S$ (CHSH) | $\lvert\langle ab\rangle+\langle AB\rangle+\langle aB\rangle-\langle Ab\rangle\rvert$ | none | Eq 4.3, L137 | local (classical) bound 2; quantum maximum $2\sqrt2 \approx 2.83$ | M10 |
| DV-QKD, CV-QKD | discrete-variable (photon counting) versus continuous-variable (field quadrature) QKD | none | L144 | CV is not "more advanced BB84"; it is a different detection method | M10 |
| kb/s, Gb/s | kilobits and gigabits per second ($10^3$ and $10^9$) | bit/s | L177 | L177 compares a **classical** fibre data rate (Gb/s) with a satellite **key** rate (kb/s); see 4K | M10 |
| dB, dB/km | loss in decibels: $T = 10^{-\text{dB}/10}$ | dB, dB/km | not in lecture | typical telecom fibre at 1550 nm loses about **0.2 dB/km** (typical value, not stated in the lecture) | M10 |
| $T$ (here), $\eta$ (Day 06) | channel transmission, the fraction of photons that arrive: Day 06's $\eta \equiv$ this companion's $T$ | none | not in lecture | in C4.2 below, $\eta_d$ is **detector efficiency**, not transmission; do not mix it with Day 06's $\eta$ | M10 |
| km | link length | km | L167, L172, L203-L209 | always ask "lab spool or deployed fibre?" and "with or without trusted nodes?" | M10 |
| QRNG | quantum random number generator | bit/s | L199 | a component, not QKD | M8 |
| TRL-like words: "lab", "demonstrated", "rolled out" | maturity statements | none | L167, L183, L191 | not the same as a TRL; see Day 10 (F2) | F2 |

**Conversions you will use every time.** Loss in dB to transmission: $T = 10^{-\alpha L/10}$ with $\alpha$ in dB/km and $L$ in km. Every 10 dB is a factor 10. At 0.2 dB/km (typical, labelled), 50 km is 10 dB, 100 km is 20 dB ($T = 0.01$), 600 km is 120 dB ($T = 10^{-12}$).

## 4. Skipped steps, expanded

Each item gives the lecture line, the gap, the missing lines and the move. Items B, C, D and G are the reason this companion exists.

### 4A. L51-L57: no-cloning, with the missing definition (M9)

The lecture applies $U_\mathrm{cl}$ to a superposition and "gets" $\alpha\lvert00\rangle+\beta\lvert11\rangle$ without saying why. The missing line is what $U_\mathrm{cl}$ must do to basis states.

1. **Definition (skipped).** A cloner must copy every state, in particular the basis states: $U_\mathrm{cl}\lvert0\rangle\lvert0\rangle = \lvert00\rangle$ and $U_\mathrm{cl}\lvert1\rangle\lvert0\rangle = \lvert11\rangle$.
2. **Linearity.** $U_\mathrm{cl}(\alpha\lvert0\rangle+\beta\lvert1\rangle)\lvert0\rangle = \alpha\,U_\mathrm{cl}\lvert00\rangle+\beta\,U_\mathrm{cl}\lvert10\rangle = \alpha\lvert00\rangle+\beta\lvert11\rangle$. This is Eq 4.2; it uses step 1.
3. **What cloning demands.** $\lvert\phi\rangle\lvert\phi\rangle = \alpha^2\lvert00\rangle+\alpha\beta\lvert01\rangle+\alpha\beta\lvert10\rangle+\beta^2\lvert11\rangle$ (Eq 4.1).
4. **Compare.** The $\lvert01\rangle$ coefficient must be 0 and $\alpha\beta$ at once, so $\alpha\beta = 0$: only $\lvert0\rangle$ or $\lvert1\rangle$ themselves can be copied. Matching $\lvert00\rangle$ also needs $\alpha = \alpha^2$. No single unitary clones an unknown superposition. That is the whole proof, in four lines.
5. **Why it matters for BB84.** Eve can copy H and V perfectly with a machine built for the R basis, but the same machine wrecks the ±45° states. Since she does not know the basis, she cannot copy without disturbing.
6. **L61's "analogy explanation" is not a proof.** It says "changing one quantum state into another correctly every time fundamentally does not exist", which is false as stated (any unitary changes states correctly every time). The real content is lines 1-4. Use those.

### 4B. Table 4.1 (`fig4_table1.png`, L77-L85): BB84 without Eve, decoded (M9)

Encoding (Fig 4.3): R basis H = 0, V = 1; D basis +45° ("+") = 0, −45° ("−") = 1.

| Position | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Alice bit, basis, sends | 1, D, − | 0, R, H | 1, R, V | 0, R, H | 0, D, + | 1, D, − |
| Bob basis | D | D | D | R | D | R |
| Bases match? | yes | no | no | yes | yes | no |
| Bob's bit | 1 | 1 (random) | 1 (random) | 0 | 0 | 0 (random) |

1. **Sifting.** Bob announces his bases (never his results). Matches at positions 1, 4, 5 (the checked cells in the "Compare bases" row). Sifted key: 1, 0, 0, which equals Alice's bits there. The striped positions 2, 3, 6 are discarded.
2. **Sifted fraction** $= 3/6 = 0.5$, which is the expected value: Bob's basis matches Alice's with probability ½.
3. **The yellow cells** are the random outcomes from mismatched bases. Their bits are fine as random results.
4. **Two symbol slips in the figure.** Position 3: Bob measured in D but the table says "V". A D-basis measurement can only give + or −; result 1 should be written "−". Position 6: Bob measured in R but the table says "+"; result 0 should be written "H". The bits and the key are unaffected.

### 4C. Table 4.2 (`fig4_table2.png`, L93-L99): why Eve's errors show, and the confusing "Secret key" row (M9)

| Position | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Alice sends (bit, basis) | + (0, D) | V (1, R) | − (1, D) | H (0, R) | V (1, R) | V (1, R) |
| Eve basis, result | D, + | D, − | R, V | D, − | R, V | D, + |
| Eve right basis? | yes | no | no | no | yes | no |
| Bob basis, result | D, + → 0 | R, H → 0 | R, V → 1 | D, − → 1 | D, + → 0 | R, H → 0 |
| Alice-Bob bases match? | yes | yes | no | no | no | yes |

1. **Eve resends what she measured.** At positions 2 and 6 she guessed wrong (D instead of R) and resent a diagonal photon. Bob, now in the right basis (R), gets H or V at random: a 50% chance of error each time. Here both came out wrong (H, bit 0, instead of V, bit 1). Those are the two "!" marks.
2. **Position 1:** Eve guessed right, resent the true state, no error. Positions 3, 4, 5 are discarded at sifting, so whatever Eve did there is invisible.
3. **Sifted key:** positions 1, 2, 6. Alice 0, 1, 1; Bob 0, 0, 0. Errors in 2 of 3 sifted bits, QBER $= 2/3 \approx 67\%$ in this tiny sample; the long-run value is 25% (4D).
4. **The confusing row.** The row labelled "Secret key" (0, 0, 1, 1, 0, 0) is just a copy of Bob's raw bits, including positions 3, 4, 5, which the striped background marks for discard. Read it as "Bob's raw bits, shaded by whether the bases matched". The real sifted key is three bits, and two of them disagree, which is how Eve is caught.
5. **L93's test step.** Alice and Bob publicly compare a **random sample** of sifted bits (and then discard them). Any error rate above what the channel alone explains means "abort". L93 says "Bob tells Alice a result from the key"; one result is not enough (4D).

### 4D. L93, L102: the 25% QBER and $1-(3/4)^n$, which the lecture never computes (M9)

1. Full intercept-resend: Eve measures every photon in a random basis and resends her result.
2. Consider only sifted bits (Alice and Bob in the same basis). Eve picks the wrong basis with probability ½. If she does, she resends a state of the other basis, and Bob's measurement in the correct basis gives the wrong bit with probability ½. If she picks right, no error.
3. QBER $= \tfrac12\times\tfrac12 = \tfrac14 = 25\%$.
4. Each tested sifted bit passes with probability $3/4$. After $n$ independent test bits, Eve stays hidden with probability $(3/4)^n$, so detection probability is $1-(3/4)^n$.
5. Numbers: $n = 6$: $1-0.178 = 0.82$. $n = 20$: $(3/4)^{20} = 0.0032$, detection 0.997. Testing a few dozen bits makes a full intercept-resend attack essentially certain to be seen.
6. L102's "small probability that Eve guesses all the bases correctly" is the right idea in the wrong form. Eve does not have to guess every basis; she is missed whenever her wrong guesses happen not to cause errors in the tested bits. The correct statement is $(3/4)^n$ per tested bit.
7. **What real systems do (Pirandola §BB84):** they estimate the QBER, then run error correction and privacy amplification, which shrink the key to remove Eve's partial information. Below about 11% QBER, one-way BB84 can still distil a secure key; above it, they abort. A channel with errors does not make Eve undetectable (L102); it means every error is charged to Eve.

### 4E. L106-L121: B92, and the "75%" claim checked (M9)

1. **Encoding.** 0 = H, 1 = +45°. These two states are not orthogonal; that is the point of B92.
2. **Bob's conclusive results.** Bob measures in R or D at random. If he gets V (R basis), the photon cannot have been H, so Alice sent +45°: bit 1. If he gets −45° (D basis), it cannot have been +45°, so Alice sent H: bit 0. All other outcomes are inconclusive and discarded (L118, L120). Table 4.3 lists the cases; "V or H" means 50:50.
3. **Conclusive fraction without Eve:** Bob's basis is the "opposite" one with probability ½, and the informative outcome then occurs with probability ½: $\tfrac12\times\tfrac12 = 0.25$ of photons.
4. **Intercept-resend on B92 (Eve measures in R or D at random and resends what she sees).** Working through the cases (Alice's 2 states × Eve's 4 outcomes × Bob's 2 bases): the conclusive fraction rises from 1/4 to 3/8 (0.375) of photons, and 1/8 (0.125) of photons give a conclusive but **wrong** bit. Error rate on kept bits $= 0.125/0.375 = 1/3$.
5. **Verdict on L121 (B92): the 75% does not hold.** Under intercept-resend (Eve measures in R or D at random and resends what she sees), Bob's conclusive fraction rises from 1/4 to 3/8 of photons and 1/3 of his kept bits are wrong; each checked kept bit exposes Eve with probability 1/3, so she survives $n$ checks with probability $(2/3)^n$. The lecture's 3/4 is BB84's per-bit survival probability, not a B92 detection probability. (Judgement on the origin of the slip; the arithmetic is above. Day 06 M9.5 carries the same note.) Also, B92 is weaker than BB84 on lossy links, because Eve can use an attack that discards photons she cannot identify (Pirandola, practical section).

### 4F. L125: "the information will be instantly known" (no-signalling)

1. Measuring one half of an entangled pair fixes the **correlation**, not a message. Alice's own results are 50:50 random whatever Bob does.
2. Alice and Bob can only see the correlation by comparing results over the classical channel, which is limited by the speed of light. So no information travels faster than light (the no-signalling principle).
3. This is why quiz Q2's option "a way to transfer messages instantaneously" is false (see the inventory key). Read L125 as "the outcomes are correlated however far apart they are".

### 4G. L135-L142: CHSH with the numbers (M10)

1. Each measurement gives ±1. For a polarisation-entangled pair in $\lvert\Phi^+\rangle = (\lvert HH\rangle+\lvert VV\rangle)/\sqrt2$ and polariser angles $\theta_a$, $\theta_b$, the correlation is $E(\theta_a,\theta_b) = \cos2(\theta_a-\theta_b)$ (standard result; take it on trust, the full CHSH derivation is skipped in this sprint).
2. Settings that fit the lecture's sign pattern ($+ab+AB+aB-Ab$), the same set Day 06 M10.1 uses: $a = 22.5^\circ$, $A = 67.5^\circ$, $b = 0^\circ$, $B = 45^\circ$.
   - $\langle ab\rangle$: $\Delta\theta = 22.5^\circ$, $\cos(45^\circ) = 0.707$
   - $\langle AB\rangle$: $\Delta\theta = 22.5^\circ$, $\cos(45^\circ) = 0.707$
   - $\langle aB\rangle$: $\Delta\theta = -22.5^\circ$, $\cos(-45^\circ) = 0.707$
   - $\langle Ab\rangle$: $\Delta\theta = 67.5^\circ$, $\cos(135^\circ) = -0.707$
3. $S = 0.707+0.707+0.707-(-0.707) = 4\times0.707 = 2\sqrt2 \approx 2.83$.
4. **Local bound 2.** If each result were fixed in advance (±1 values for $a$, $A$, $b$, $B$), then $ab+aB+AB-Ab = a(b+B)+A(B-b)$; one bracket is 0 and the other ±2, so the sum is ±2. Averages cannot exceed 2. Only angle differences matter: rotating all four settings by the same angle (for example to $a = 0^\circ$, $A = 45^\circ$, $b = -22.5^\circ$, $B = 22.5^\circ$) leaves every $\Delta\theta$, and so $S$, unchanged.
5. **L142 "measure less than 2 if Eve has measured".** Read: "at most 2". Eve's measurement turns the pair into a classical mixture of product states, which obeys the local bound. Real noise also lowers $S$: with visibility $V$, $S = 2\sqrt2V$, so $V$ must exceed $1/\sqrt2 = 0.71$ for any violation.
6. **L135 "they don't have to sacrifice key results".** True in E91: the Bell test uses the rounds with non-matching settings, which BB84-style sifting would throw away anyway.

### 4H. L152 (erratum) and L219: repeaters do not amplify (M10)

1. **L152 says** "the aim of a quantum repeater is to amplify the signal". **This is wrong.** An amplifier that outputs more copies of an unknown quantum state is a cloner, forbidden by 4A. L152's own previous sentence and L219 ("no method of amplifying the signal without measuring") say so.
2. **What a quantum repeater does.** Split the link into short segments. Create an entangled pair across each segment and store each half in a **quantum memory** until its neighbour succeeds. Then do a Bell measurement at the middle node (**entanglement swapping**): the two short pairs become one longer pair, end to end, without any qubit crossing the whole distance. **Entanglement purification** (distillation; L152 mentions it) consumes several noisy pairs to make fewer, better ones.
3. Why memories matter: without them, all segments must succeed at once, and the success probability multiplies down just like direct transmission.
4. **L219 "quantum repeaters are outside of the current scope of physics".** Read: outside current **engineering**. The physics is known and parts have been demonstrated (L213, L219 cite lab progress); reliable, fast memories are the bottleneck.
5. L152's cache analogy and "speed up communication" are loose. A memory in a repeater is there to wait for heralded success, not to speed anything up.

### 4I. L201-L209: trusted node versus true quantum network (M10)

1. **Trusted node.** Run separate QKD on A→N and N→B. Node N holds both keys in the clear, decrypts and re-encrypts (or XORs them). Security now depends on N being physically secure. It works today over any distance, but the "quantum" guarantee stops at each node.
2. **True quantum network.** End-to-end entanglement via repeaters (4H), or a satellite that sends entangled photons to both ends. No intermediate point ever holds the key.
3. The lecture says this correctly at L201 ("these are not true quantum networks"). Apply it to every long-distance figure you quote: L209's 2000 km and 4600 km network uses trusted nodes.
4. Why trusted nodes are unavoidable today: at 0.2 dB/km (typical), 2000 km of fibre is 400 dB, a transmission of $10^{-40}$. No photon arrives. The 45 km link at L203 is 9 dB ($T = 0.126$), fine without nodes.

### 4J. L167-L177: fibre versus free space versus satellite, with numbers (M10)

1. **Fibre loss (typical value, not in the lecture): 0.2 dB/km** at 1550 nm. At 100 km: 20 dB, $T = 0.01$. At 600 km (L167): 120 dB, $T = 10^{-12}$.
2. **Why 600 km needed a trick.** L167 says "phase stabilisation, which is the main loss": read instead "phase stabilisation, which is the main **technical difficulty**"; the main loss is still absorption. Twin-field QKD sends light from both ends to a middle station, so the key rate scales roughly as $\sqrt{T}$ instead of $T$: $\sqrt{10^{-12}} = 10^{-6}$ (Pirandola, practical section). The middle station is untrusted, which is why it is "repeater-like" but not a repeater.
3. **The repeaterless limit (Pirandola).** For a point-to-point link the key per channel use cannot exceed $-\log_2(1-T)\approx1.44\,T$. Rates fall exponentially with distance; no protocol escapes that without repeaters (or the twin-field middle station).
4. **Free space (L172).** Loss is mostly beam spreading (geometric) plus turbulence and scattering, and it grows much more slowly than fibre's exponential. At 70 km, fibre is 14 dB ($T = 0.04$); beyond a few tens of km free space can win, so L172's "smaller losses for distances larger than 70 km" is the right order (judgement). Daylight background noise is the price.
5. **Satellite (L177).** Most of the path is vacuum, so the loss is mostly diffraction and the last ~10 km of atmosphere. L177's "optical fibres can transfer gigabits per second and satellites kilobits per second" compares **unlike quantities**: Gb/s is a classical data rate; QKD key rates over metro fibre are typically kb/s to Mb/s and fall steeply with distance (Pirandola; Chapman & Peters). Compare key rate with key rate.

### 4K. Questionable claims at L29 and L35 (M8)

1. **L29: "transfer more information with fewer qubits".** Holevo's bound (Nielsen & Chuang, lecture ref 1): $n$ qubits carry at most $n$ bits of classical information you can read out. Superdense coding sends 2 bits per qubit only by consuming a pre-shared entangled pair. The advantage of qubits in this week is **security**, not capacity.
2. **L35: "inherently more secure ... because of its randomness and the key is only known to Alice and Bob".** The security comes from measurement disturbance and no-cloning (4A), not randomness alone. And it holds only if (i) the classical channel is **authenticated**, otherwise Eve simply impersonates Bob (Fig 4.2 shows Eve on the classical channel: she may read it, she must not be able to change it); (ii) the devices behave as modelled, since real systems have been attacked through detector side channels; (iii) the nodes are trusted. The NCSC white paper makes exactly these points and recommends post-quantum cryptography over QKD for most uses. That is your "downsides" paragraph.
3. **L35 / L187 implied: harvest now, decrypt later.** Data recorded today can be decrypted once a large quantum computer exists. Mosca's rule (M8): if $x$ (years the data must stay secret) + $y$ (years to migrate) $> z$ (years until such a computer), act now.
4. **Quiz Q4 link.** QKD distributes a key; it does not encrypt. The inventory key flags the loose option.

### 4L. Reference mismatches and smaller decodes

- **L203 cites [26]** (May et al., correlation filters for infrared imagery). That paper is not about QKD. The Tokyo trusted-node network is unsourced in the lecture; do not cite [26] for it.
- **L209 cites [29]** (Gibney 2016, Nature news on the Micius launch). It does not report the 2017 Beijing-Shanghai fibre backbone. Ref [19] (Chen et al. 2021, the 4600 km network) is the right source for the integrated network.
- **L217 cites [32]**, a Canadian announcement about a satellite **emissions-detection** system; it does not support the quantum-satellite claim. Flag it.
- **L205 / ref [27]:** the Delft experiment (Hensen et al. 2015) was a loophole-free **Bell test** over 1.3 km, not a QKD network for "an online game". Cite it only as a Bell test.
- **L67:** "it doesn't matter if the photons are originally polarised or unpolarised" is true only because the filter prepares the state; real systems use attenuated lasers, whose occasional multi-photon pulses need decoy states (Pirandola).
- **L21:** the "grey" picture (Fig 4.1) suggests a mixture; a superposition has a definite phase between $\lvert0\rangle$ and $\lvert1\rangle$, which is what makes the diagonal basis possible.
- **L135:** "E91 is built on BB84" is loose history: E91 (1991) is an independent idea; BBM92 later showed the entanglement version reduces to BB84 (judgement).
- **L144:** "superdense coding" is not a key-distribution protocol.

## 5. Clones

These have the same type as the week's quantitative content and its Consolidate task, with fresh bit strings, distances and a fictional case. Do them after the lecture, before the cold attempt in §6.

### Exercise C4.1 (quantitative)

An 8-photon BB84 run, no eavesdropper. Encoding: R basis H = 0, V = 1; D basis +45° = 0, −45° = 1.

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Alice bit | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Alice basis | D | D | R | R | D | R | R | D |
| Bob basis | D | R | R | D | R | R | D | D |
| Bob's outcome where bases differ | | H | | +45° | V | | −45° | |

(a) Write what Alice sends and Bob's bit at every position. (b) Find the sifted key and the sifted fraction, and compare it with the expected value. (c) They publicly test positions 3 and 8; what key is left? (d) If Eve had intercept-resent every photon, how many errors would you expect in the 4 sifted bits, and what is the chance the 2 test bits show none? (e) How many test bits would give 99% detection of a full intercept-resend attack?

**Hint:** Sifting keeps positions where the bases agree, whatever Bob got elsewhere. QBER for full intercept-resend is ¼ per sifted bit. Solve $(3/4)^n \le 0.01$ with logarithms.

**Solution sketch:**
1. *Restate.* 8 photons, bases and bits given, no Eve. Want sent states, Bob's bits, sifted key, fraction, remaining key, expected errors under attack, a pass probability and a test size.
2. *Write state.* Sent state = basis + bit (R: H/V, D: +/−). Sift on matching bases. Under attack, per sifted bit $P(\text{error}) = 1/4$; $P(\text{no error in } n) = (3/4)^n$.
3. *Name move.* M9 (BB84 by hand, QBER, $(3/4)^n$).
4. *Algebra.*
   - (a) Alice sends −, +, V, V, −, V, H, +. Bob's bits: 1, 0 (H), 1, 0 (+45°), 1 (V), 1, 1 (−45°), 0.
   - (b) Matches at 1, 3, 6, 8. Sifted key 1, 1, 1, 0. Fraction $4/8 = 0.5$, exactly the expected value this time.
   - (c) Positions 3 and 8 are sacrificed (both agree); the key left is 1, 1 (positions 1 and 6).
   - (d) Expected errors $4\times0.25 = 1$. $P(\text{no error in 2 tests}) = 0.75^2 = 0.5625$: with two test bits Eve escapes more often than not.
   - (e) $n \ge \ln0.01/\ln0.75 = 16.0$, so $n = 17$ test bits.
5. *Check.* Bob's outcomes at 2, 4, 5 and 7 do not matter for the key, as they should not; at those positions his bit happens to match Alice's at 2 and 5 and not at 4 and 7, which is why unsifted agreement means nothing. $0.75^{17} = 0.0075 < 0.01$, and $0.75^{16} = 0.010$, just above.
6. *Answer.* Sifted key 1110 (50% kept); after testing, 11. A full attack would cause about 1 error in 4 sifted bits, but two test bits catch it only 44% of the time; 17 test bits give 99%.

The habit to keep: errors are always counted on the sifted bits, and the number of bits you test sets your confidence.

### Exercise C4.2 (quantitative)

A QKD link runs over deployed fibre at 0.2 dB/km (typical telecom fibre, labelled). The source sends $10^9$ single photons per second (idealised), and Bob's detectors have 25% efficiency. (a) Find the transmission and the sifted key rate at 150 km. (b) Repeat at 300 km. (c) The 300 km route is split by two trusted nodes into three 100 km segments; find the sifted rate per segment. (d) Compare (a) with the repeaterless bound $-\log_2(1-T)$ bits per channel use, using the channel transmission only.

**Hint:** $T = 10^{-\alpha L/10}$. Detected rate = source rate × $T$ × efficiency; sifting keeps half. The bound is per channel use, so multiply by $10^9$.

**Solution sketch:**
1. *Restate.* $\alpha = 0.2$ dB/km, rate $10^9$/s, $\eta_d = 0.25$, distances 150, 300 and 100 km. Want $T$, sifted rates and a bound.
2. *Write state.* $T = 10^{-0.02L}$; $R_\mathrm{sift} = \tfrac12\times10^9\times T\times0.25$; $R_\mathrm{max} = -\log_2(1-T)\times10^9$.
3. *Name move.* M10 (dB to transmission, key rate falls with distance, trusted node).
4. *Algebra.*
   - (a) 150 km: 30 dB, $T = 10^{-3}$. $R_\mathrm{sift} = 0.5\times10^9\times10^{-3}\times0.25 = 1.25\times10^5$ bit/s, about 125 kb/s.
   - (b) 300 km: 60 dB, $T = 10^{-6}$. $R_\mathrm{sift} = 125$ bit/s.
   - (c) 100 km: 20 dB, $T = 0.01$. $R_\mathrm{sift} = 1.25\times10^6$ bit/s per segment; the end-to-end key rate is that of the slowest segment, about 1.25 Mb/s.
   - (d) $-\log_2(1-10^{-3}) = 1.44\times10^{-3}$ bits per use, so at most $1.44\times10^6$ bit/s at 150 km. The sifted figure in (a) sits below the bound, as it must.
5. *Check.* Doubling the distance from 150 to 300 km multiplied the loss in dB by 2 and divided the rate by 1000, not by 2: loss is exponential in distance. Sifted rates are before error correction and privacy amplification, so the final key is smaller still.
6. *Answer.* 125 kb/s at 150 km, 125 bit/s at 300 km, about 1.25 Mb/s with two trusted nodes, at the price of trusting both nodes.

So the trusted node buys back a factor of $10^4$ in rate, and that is exactly why it is used, and exactly why it is a security caveat.

### Exercise C4.3 (quantitative)

An entanglement-based link tests CHSH with $E(\theta_a,\theta_b) = \cos2(\theta_a-\theta_b)$ and the lecture's sign pattern $S = \lvert\langle ab\rangle+\langle AB\rangle+\langle aB\rangle-\langle Ab\rangle\rvert$. The optimal set (4G) is $a = 22.5^\circ$, $A = 67.5^\circ$, $b = 0^\circ$, $B = 45^\circ$. A misaligned set-up keeps $b = 0^\circ$ but uses $a = 15^\circ$, $A = 45^\circ$, $B = 30^\circ$. (a) Compute $S$. (b) Does it violate the local bound, and how far is it below $2\sqrt2$? (c) With the optimal angles but a source of visibility $V = 0.8$, what is $S$? (d) With the misaligned angles of (a), what is the minimum visibility for any violation, and how does it compare with the optimal set's $1/\sqrt2$?

**Hint:** Only angle differences matter. Each term is $\cos$ of twice the difference. With visibility $V$ every correlation is multiplied by $V$.

**Solution sketch:**
1. *Restate.* Four angles, $E = \cos2\Delta\theta$. Want $S$ for these angles, $S$ for $V = 0.8$, and the threshold $V$ for the misaligned set.
2. *Write state.* $S = E(a,b)+E(A,B)+E(a,B)-E(A,b)$; with visibility, $S \to VS$.
3. *Name move.* M10 (CHSH arithmetic).
4. *Algebra.*
   - (a) Differences 15°, 15°, −15°, 45°. $\langle ab\rangle = \cos30^\circ = 0.866$; $\langle AB\rangle = 0.866$; $\langle aB\rangle = \cos(-30^\circ) = 0.866$; $\langle Ab\rangle = \cos90^\circ = 0$. $S = 3\times0.866 = 2.60$.
   - (b) $2.60 > 2$: violation, but $2.83 - 2.60 = 0.23$ below $2\sqrt2$.
   - (c) $2.83\times0.8 = 2.26$.
   - (d) $2.60\,V > 2 \Rightarrow V > 0.770$, against 0.707 for the optimal set.
5. *Check.* Each correlation is in $[-1, 1]$; $S$ is below the quantum maximum, as it must be. Misalignment raises the visibility the source must reach.
6. *Answer.* $S = 2.60$, a violation 0.23 short of $2\sqrt2$; $V = 0.8$ gives 2.26 with the optimal angles; the misaligned set needs $V > 0.77$ instead of 0.71.

The point for a write-up: "a Bell violation" is not a yes/no badge; how far above 2 you are sets how much key you can safely extract, and alignment and source quality both eat into that margin.

### Exercise C4.4 (writing)

Harrowmere Water & Power (fictional; shared fact sheet in `STRATEGY.md`) reaches its 160 km site over its own dark fibre. The site's AES-256 key is refreshed every 60 s, and the telemetry must stay confidential for 15 years (fictional). The route is too long for one QKD link, so any QKD design needs a trusted node. Hypothetical design for this exercise only: the node sits in an unstaffed pumping depot 70 km along the route, leaving a 90 km second hop; each QKD box pair costs £110k installed; securing the depot (cage, alarms, tamper-evident racks) costs £40k plus £25k a year for monitoring and vetted maintenance staff; a hybrid post-quantum key exchange on this one route costs £10k (all hypothetical). Write a 150-200-word risk note on the trusted node: what must be trusted and where, what an insider at the node could do, and what the route costs over 10 years against PQC. End with a verdict for this route.

**Hint:** Draw the chain: control centre, 70 km, depot, 90 km, site. Mark where the key exists in the clear (M10.3: the node holds both hop keys and announces their XOR). Ask whether an insider's misuse would raise the QBER. Cost both box pairs, the depot works and 10 years of upkeep, against the PQC figure for the same route. State the 0.2 dB/km assumption for the hop losses.

**Model paragraph:**
On Harrowmere's 160 km route (fictional), QKD's guarantee stops at the relay. With a trusted node in a pumping depot 70 km out (hypothetical), each hop runs its own QKD link, losing 14 dB and 18 dB at an assumed 0.2 dB/km, and the node holds both hop keys in the clear to build the end-to-end key. What must be trusted is therefore a building, not physics: the depot's locks and alarms, the node's hardware and firmware, and everyone with access. An insider there could copy every key that passes, one a minute, and decrypt recorded telemetry throughout the 15 years it must stay secret (fictional), or hand out substitute keys. None of this raises the error rate, because the node is a legitimate end of both links, so the QBER check is blind to it. The route costs £260k for two box pairs and the depot works, plus £25k a year, about £510k over 10 years (hypothetical), against £10k for a hybrid post-quantum exchange that holds no key in the middle. Verdict: use PQC on this route; the node reintroduces exactly the insider risk QKD was meant to remove, at about fifty times the cost.

**What a weak answer misses:** It calls the trusted-node chain "end-to-end quantum-secure", or calls the node a repeater that amplifies (L152). It assumes an insider at the node would show up as errors, when the node is a legitimate endpoint and leaves no QBER trace. It costs only the boxes and forgets the depot and its yearly upkeep, or compares this one route with a whole-network PQC price. It gives no location for the node, no hop losses, and no link to Harrowmere's 15-year confidentiality, so it could be pasted onto any company. It does not label the depot and the prices as hypothetical.

## 6. Cold attempt

Attempt this on paper before opening the sketch. Same type as §5, fresh numbers.

### Exercise C4.5 (quantitative)

A 65 km BB84 link over fibre at 0.2 dB/km (typical) uses the hypothetical box of Day 06 Exercise 6.7, so assume the same intrinsic QBER of 2.5% from imperfect optics (hypothetical trial figure). An eavesdropper intercept-resends a fraction $f = 0.3$ of the photons. (a) Find the channel transmission. (b) What QBER does Eve add, and roughly what total QBER do Alice and Bob see? (c) If they abort above 11%, do they abort? (d) Compute the secret fraction $r = 1 - 2h(Q)$ at the total QBER. (e) How many test bits do they need to see at least one Eve-caused error with 99.9% probability? (f) In one or two sentences: has Eve got away with it?

**Hint:** Eve adds $f\times\tfrac14$. For (d), $h(Q) = -Q\log_2Q-(1-Q)\log_2(1-Q)$ (Pirandola et al. 2020). For (e), each tested bit shows an Eve error with probability equal to the added QBER; solve $(1-q)^n \le 0.001$.

**Do not open the sketch until you have a written attempt.**

**Solution sketch:**
1. *Restate.* $L = 65$ km, $\alpha = 0.2$ dB/km, intrinsic 2.5% (hypothetical), $f = 0.3$, threshold 11%, confidence 99.9%. Want $T$, QBER, the abort decision, $r$, $n$ and what the threshold means.
2. *Write state.* $T = 10^{-\alpha L/10}$; $q_\mathrm{Eve} = f/4$; total ≈ intrinsic + $q_\mathrm{Eve}$ (small rates add approximately; the exact combination $0.025\times0.925+0.075\times0.975 = 0.096$ is slightly lower, so adding errs on the safe side); $r = 1-2h(Q)$; $n \ge \ln0.001/\ln(1-q_\mathrm{Eve})$.
3. *Name move.* M10 (fibre loss), M9 (QBER, secret fraction, detection probability).
4. *Algebra.*
   - (a) 13 dB, $T = 10^{-1.3} = 0.050$.
   - (b) $q_\mathrm{Eve} = 0.3\times0.25 = 0.075$. Total ≈ $0.025+0.075 = 0.10$, that is 10%.
   - (c) $10\% < 11\%$: they do **not** abort.
   - (d) $h(0.10) = 0.469$, $r = 1 - 0.938 = 0.062$: about 6% of the sifted bits survive as secret key, about a tenth of what the same box keeps with no Eve (Day 06 Exercise 6.7).
   - (e) $n \ge \ln0.001/\ln0.925 = 88.6$, so 89 test bits.
5. *Check.* With $f = 1$ the added QBER would be 25%, matching 4D, and the link would abort. At $Q = 11\%$, $r$ reaches 0, so 10% sitting just below the line gives a small positive $r$, as found.
6. *Answer.* $T = 0.050$; Eve adds 7.5%, total about 10%; below 11%, so no abort; $r \approx 0.06$; 89 test bits give 99.9% confidence of seeing one of Eve's errors. (f) No. The 11% threshold is not an alarm that Eve slipped under: Alice and Bob charge **all** 10% of the errors to Eve, and privacy amplification shrinks the key to 6% of the sifted bits, which removes what she could know. Below the threshold an attack costs key rate, not secrecy; above it no key can be made, so they abort.

If you got (b) wrong, go back to 4D: the ¼ is per sifted bit **that Eve touched**, so scale it by $f$. If you thought "no abort" meant "Eve wins", reread M9.4's paragraph on what real systems do.

## 7. Confusion log prompts

Answer each in writing (two or three sentences) after your pass through the lecture. Log the answer in your confusion log with the date.

1. Without notes: why does Eve's wrong-basis guess cause an error only half the time, and why is the QBER computed on sifted bits only?
2. L152 says repeaters amplify; L219 says nothing can amplify. In your own words, what does a quantum repeater actually do, and why does it need a memory?
3. Your portfolio piece will quote a QKD distance. What two questions (about nodes, and about lab versus field) must you answer next to the number so a reader cannot be misled?
4. (Optional) Re-derive the B92 error rate under intercept-resend (1/3) for one of Alice's two states, and say in one sentence why L121's 75% is not right.

## 8. Figures

One note per figure: what to look at, what it shows, the lecture line, and the trap.

**Fig 4.1 (bit versus qubit, L21-L29).** Left: a classical bit is either the white 0 box or the dark 1 box. Right: a strip from 0 to 1 with a teal middle labelled "0 and 1, superposition state". Trap: the strip suggests a continuous dial or a grey mixture. A qubit state needs **two** real numbers (a weight and a relative phase), and the phase is what lets the diagonal basis exist (4L). Measurement still gives only 0 or 1 (4K, Holevo).

**Fig 4.2 (two channels, L35-L43).** Look at the arrows: the quantum channel is one-way (Alice → Bob), the classical channel two-way. Eve sits between both. Trap: the figure lets Eve touch the classical channel without saying how. She may **listen** to it (basis announcements are public by design), but it must be **authenticated** so she cannot alter it; otherwise she plays Bob to Alice and Alice to Bob, and QKD gives no protection (4K).

**Fig 4.3 (polarisation bases, L67-L75).** Top: the R basis (horizontal/vertical arrows) and the D basis (diagonal arrows); top right, the bit assignment H = 0, V = 1, +45° = 0, −45° = 1. Bottom left: an H photon passes an R filter unchanged. Bottom right: a −45° photon meets the R filter and comes out H or V, 50:50. This is the whole BB84 mechanism in one picture: same basis, certain result; wrong basis, coin toss. Trap: the lecture's long description calls the bottom-right photon "diagonally ... at a 45-degree angle" and repeats the "bottom left" sentence; the drawn photon is −45°. And "+" here labels a **state**, while many sources use "+" for the R **basis** (§3).

**Fig 4.4 (BB84 configuration, L87-L91).** Same layout as Fig 4.2 with the four states (H, V, −45°, +45°) drawn inside the quantum channel. Look at it as "four states, two bases, each photon carries one". Trap: Eve is drawn off the quantum channel, but in BB84 she attacks the photons themselves; the classical channel carries only bases, never bit values (except the sacrificed test bits).

**Table 4.1 (`fig4_table1.png`, L77-L85).** Read row by row: Alice's bits and bases, what she sends, Bob's bases, what he measures, his bits, "Compare bases" (checked = match, striped = mismatch) and the sifted key 1, 0, 0. The yellow cells are random outcomes from wrong bases. Trap: positions 3 and 6 show symbols Bob's basis cannot produce (V in D, + in R); the bits are right, the symbols should be − and H (4B).

**Table 4.2 (`fig4_table2.png`, L93-L99).** Two extra rows for Eve's basis and result. Follow positions 2 and 6: Eve uses D on an R photon, resends a diagonal state, and Bob (in R) gets the wrong bit; the "!" marks those errors. Trap: the row labelled "Secret key" is Bob's raw string with shading, not a key; only the checked positions 1, 2, 6 survive sifting, and two of the three disagree (4C).

**Fig 4.5 (E91 configuration, L125-L131).** The quantum channel is now two-way: a source in the middle sends one particle of each entangled pair to each side (the dots). Trap: the source can be anywhere, even controlled by Eve; E91's security does not depend on trusting it, because the CHSH value (4G) certifies the correlations. The figure does not show the Bell-test step, which is where the security comes from.

**Fig 4.6 (simple network, L154-L160).** Two end-nodes joined through a box labelled "Node repeater or switch", with the channel labelled "optical fibre, seawater, atmosphere" and "... and more nodes". Trap: the one box hides three very different things. A **trusted node** (holds the key in the clear, used today), a **quantum repeater** (entanglement swapping plus memories, lab only) and an optical **switch** (routes photons, adds loss, no extension of range). When you cite a network, say which box it uses (4H, 4I).

## 9. Course interactive walkthrough

**QuVis BB84 photons (University of St Andrews):** https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/BB84_photons/BB84_photons.html. The course's own instructions are in `week_4/week_4_content.md` L107-L128. Control names below follow that task text; the simulation's on-screen labels may differ slightly. About 30 minutes. This is where the Week 4 QuVis run happens: Day 06 only points here.

**Steps.**
1. **Intro page.** Read it once. Note which symbols the simulation uses for the two bases and the four states, and map them to the lecture's R/D and H/V/+/− (§3). Write the mapping down before you start.
2. **Open the controls** ('controls', near the top right). Display all of them.
3. **Run without Eve.** Send photons one at a time for the first ten or so and predict each of Bob's results before it appears: same basis, certain; different basis, 50:50. Then let it run. Record: number sent, number sifted, and errors in the sifted key. Expect a sifted fraction near 50% and 0% errors.
4. **Switch eavesdropping on.** Before running, **predict** the error rate on the sifted bits (it should be 25%, from 4D). Run, then compare.
5. **Fast forward** to build up statistics (a few hundred photons). Watch the sifted fraction settle near 50% and the error rate near 25%. Note how noisy it is for small numbers: that is the $(3/4)^n$ story.
6. **Challenges page.** Answer the questions; note which ones you got wrong and why.

**What to record** (one line each, in your notes): photons sent; sifted bits; sifted fraction; errors without Eve; errors with Eve; error rate with Eve; one sentence on what surprised you.

**How it maps to M9.** Step 3 is sifting (4B). Step 4 is the intercept-resend QBER, $\tfrac12\times\tfrac12$ (4D). Step 5 is detection probability: with $n$ checked bits, Eve hides with probability $(3/4)^n$. Real systems add error correction and privacy amplification after this point; the simulation stops at detection.

### Check questions

1. You send 200 photons with no eavesdropper and an ideal channel. About how many sifted bits do you expect, and how many errors?
   *Answer:* about 100 sifted bits (half), and 0 errors.
2. Eve intercept-resends every photon and you keep 20 sifted bits. How many errors do you expect, and what is the chance that none of the 20 shows an error?
   *Answer:* $20\times0.25 = 5$ errors expected. $P(\text{none}) = 0.75^{20} = 0.0032$, about 0.3%.
3. Eve intercepts only half of the photons. What error rate on the sifted bits do you expect, and what changes in how many bits you must check?
   *Answer:* $0.5\times0.25 = 12.5\%$. Each checked bit now reveals Eve with probability 0.125 instead of 0.25, so you need roughly twice as many checked bits for the same confidence.
