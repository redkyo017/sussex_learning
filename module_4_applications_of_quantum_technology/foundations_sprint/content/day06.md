# Day 06: Quantum Communication: Keys, BB84, CHSH and Channels

**Time:** ~3 h · **Feeds:** Week 4 lecture (§4.1 to §4.5), inventory rows W4 Apply, W4 Consolidate, W4 quiz Q1 to Q4, W4 interactive (QuVis BB84: pointer only, run in the companion session); errata W1 L52 and W4 L152 · **Companion:** week04_companion.md §3 (notation and units), §4 (errata), §9 (QuVis walkthrough)

**Cadence (180 min):** 15 min retrieval (start with **Spaced review** at the bottom) · 55 min moves M8, M9 and M10 below · 50 min quantitative drills (Exercises 6.1 to 6.7; skip everything marked *(stretch)* if you are past time) · 45 min writing on the running case (Exercises 6.8 to 6.10) · 15 min companion pointer and confusion log (the QuVis run belongs to the companion session, not today).

This is the second heavy day of the sprint (with Day 04): three moves instead of two. The core is Moves M8.1 to M10.4 and Exercises 6.1 to 6.6, 6.8 and 6.9, minus the parts labelled (stretch): 6.3(c-e), 6.5(d-e) and all of 6.7. Exercise 6.10 is a short 10-minute piece. If you run long, move the stretch parts to the Week 4 Consolidate session; the QuVis simulation is done in the companion session.

## Why this matters

You already run cryptography for a living: you terminate TLS, rotate keys and manage certificates. Week 4 asks a narrower question than "is quantum communication secure?". It asks **what problem in that stack quantum physics solves, at what key rate and distance, and against which alternative.** The lecture describes BB84, B92 and E91, but it never says what QKD protects against (a future quantum computer breaking today's key exchange), what it does not do (encrypt anything, or authenticate anyone), or what the competing fix is (post-quantum cryptography). It also gives no channel numbers: no loss per kilometre, no key rate, no error rate.

Today fills those gaps with three moves. **M8** puts QKD in the crypto stack you know. **M9** is the protocol by hand: polarisation encodings, no-cloning in four lines, a BB84 run, and the 25% error an eavesdropper leaves. **M10** is the physics of the channel: the CHSH number $2\sqrt2$ that E91 relies on, fibre loss in dB/km, why key rate falls exponentially with distance, and why a quantum repeater is not an amplifier. With these in hand, the Week 4 Consolidate task ("bit rates or required fidelities") becomes a calculation, not a slogan.

## Core concepts

### Move M8.1: Symmetric keys, AES and the one-time pad

**Idea.** Bulk data is always encrypted with a **symmetric** cipher: both ends hold the same secret key. Two kinds matter here.
- **AES** (128 or 256-bit key). One short key encrypts gigabytes. Its security is *computational*: no known attack beats trying keys, and $2^{256}$ tries is out of reach. A quantum computer running Grover's search (Day 09) only square-roots the work, to about $2^{128}$ for AES-256, which is still out of reach (standard result; judgement on how much to say before Day 09).
- **One-time pad (OTP).** XOR the message with a truly random key **as long as the message**, used once. This is *information-theoretically* secure: the ciphertext carries no information about the message whatever computer the attacker has (Shannon's result; standard). The price is key volume: one key bit per message bit, for ever.

QKD's promise is a key that no computer can ever recover, so in principle it can feed an OTP. In practice its key rate is far too low for most links, so real deployments feed AES with frequently refreshed keys (Pirandola et al. 2020, introduction; NCSC white paper). Keep both numbers in mind: the **OTP key rate equals the data rate**, while the **AES rekey rate** is 256 bits per rekey interval.

*Worked clone (a generic remote weather-station link, 9.6 kbit/s).*
- OTP: 9.6 kbit/s of key, which is $9600\times86\,400/8 = 1.04\times10^{8}$ bytes, about 104 MB, per day.
- AES-256 rekeyed every 5 minutes: $256/300 = 0.85$ bit/s of key.

That is a factor of about $10^{4}$ between the two. Which one you assume decides whether any QKD link is "fast enough".

*You've got it when* you can say why an OTP is unbreakable and what it costs, and convert a data rate and rekey interval into a key rate in bit/s.

### Move M8.2: Public-key exchange, the Shor threat and Mosca's inequality

**Idea.** Symmetric keys must first be agreed. On the internet that is done with **public-key** cryptography: RSA (security rests on factoring) or elliptic-curve Diffie-Hellman, ECDH (security rests on the discrete logarithm). Shor's algorithm on a large, fault-tolerant quantum computer solves both problems efficiently (Day 09). AES itself is not broken by Shor; **the key exchange is** (NCSC white paper). This is what the lecture's L35 means by "quantum computers that could crack the codes quicker".

**Harvest now, decrypt later.** An adversary can record encrypted traffic today, including the public-key handshake, and decrypt it once a capable quantum computer exists. So data with a long confidentiality life is already at risk, even though no such machine exists yet.

**Mosca's inequality** turns this into a planning rule. Let
- $x$ = how long the data must stay secret (years),
- $y$ = how long it takes to migrate the system to quantum-safe cryptography,
- $z$ = how long until a cryptographically relevant quantum computer exists.

If $x + y > z$, data protected today will be exposed while it still matters. The overlap $x + y - z$ is the exposure window. Nobody knows $z$, so use a range and test the inequality at the pessimistic end (judgement; this is how the rule is normally applied).

*Worked clone (a generic land registry archive).* $x = 10$, $y = 4$, $z = 12$ years. Then $x + y = 14 > 12$: records sent in the next two years would still be secret-worthy when $z$ arrives, so migration should have started already.

*You've got it when* you can explain in one sentence why the threat is to the key exchange, not to AES, and apply $x + y > z$ to a case with numbers.

### Move M8.3: Two answers, PQC and QKD, and what QKD does not do

**Post-quantum cryptography (PQC)** replaces RSA and ECDH with new public-key schemes based on mathematical problems with no known quantum shortcut. NIST published the first three standards in August 2024: **FIPS 203** (ML-KEM, key encapsulation), **FIPS 204** (ML-DSA, signatures) and **FIPS 205** (SLH-DSA, hash-based signatures) (standard fact; not one of the Target Sources). PQC is software: it runs on existing hardware and networks. Its costs are bigger handshakes (an ML-KEM-768 public key is 1184 bytes against 32 bytes for X25519, from the FIPS 203 parameter tables) and the fact that its security is still a *computational assumption*, only newer.

**Quantum key distribution (QKD)** derives a shared key from single photons, and physics guarantees that eavesdropping leaves errors (M9). Its security does not rest on a hard problem. But read the small print, which the NCSC white paper sets out plainly:
1. **QKD distributes keys; it does not encrypt.** The data is still encrypted classically, with an OTP or AES. This is why the inventory flags W4 quiz Q4 ("quantum cryptography … encrypts data") as loose.
2. **QKD needs an authenticated classical channel.** Without authentication, Eve can sit in the middle and run one QKD session with Alice and another with Bob. Authentication uses either a pre-shared key (so QKD "grows" a small secret into a large one) or classical signatures, which today means PQC anyway. One useful asymmetry: authentication only has to hold *during* the session, so breaking it later does not expose old keys (NCSC white paper; judgement on emphasis).
3. **QKD needs special hardware and dedicated links**, has limited range (M10), and relies on **trusted nodes** for long distances (M10.3).
4. **Real devices leak** through side channels the protocol proof does not cover (Pirandola et al. 2020, practical-security sections).

The NCSC's position is that PQC is the main defence and QKD is, at most, a niche addition (NCSC white paper). For you, the engineer's analogy is useful: PQC is a cipher-suite upgrade; QKD is new physical infrastructure that replaces only the key-agreement step.

*Worked clone.* A link already running AES-256 wants quantum-safe keys. Option P: enable a hybrid ECDH + ML-KEM key exchange in software (a configuration and firmware change). Option Q: install a QKD transmitter and receiver at the two ends, dedicated fibre between them, and a pre-shared authentication key. Both remove the harvest-now risk *for the key exchange*. Only Q removes reliance on a computational assumption, and only P works over a radio link (judgement).

*You've got it when* you can list the four small-print items without notes, and say which threat PQC and QKD each remove.

### Move M9.1: Qubits in polarisation, two bases

**Idea.** A photon's polarisation is a qubit. BB84 uses two bases (lecture L67, Fig 4.3):

| Basis | Lecture letter | State for bit 0 | State for bit 1 |
|---|---|---|---|
| Rectilinear (+) | R | $\lvert H\rangle$ (horizontal, 0°) | $\lvert V\rangle$ (vertical, 90°) |
| Diagonal (×) | D | $\lvert D\rangle$ (+45°, the lecture's "+") | $\lvert A\rangle$ (−45°, the lecture's "−") |

In the $H/V$ basis, $\lvert D\rangle = (\lvert H\rangle + \lvert V\rangle)/\sqrt2$ and $\lvert A\rangle = (\lvert H\rangle - \lvert V\rangle)/\sqrt2$. This is Module 3's $\lvert\pm\rangle$ in optical clothing. The bit assignments match the lecture's Table 4.1 (R: H = 0, V = 1; D: + = 0, − = 1).

The measurement rule is **Malus's law**: a photon polarised at angle $\theta$ to the analyser's axis passes with probability $\cos^2\theta$. So:
- Measured in its own basis, a BB84 state gives the right bit with certainty.
- Measured in the *other* basis, the angle is 45° and each outcome has probability $\cos^2 45° = \tfrac12$: a coin toss, and the photon leaves in the new basis (lecture L73: "horizontal or vertical with equal probability").

*Worked clone.* A photon at 10° is measured in R: $P(H) = \cos^2 10° = 0.97$. Measured in D: $P(D) = \cos^2(45°-10°) = \cos^2 35° = 0.67$.

*An erratum to note.* L29 says a qubit can "transfer more information with fewer qubits than the classical analogue". One qubit, measured, yields at most one classical bit (Holevo's bound, standard; the "superdense coding" the lecture names at L144 gets two bits only by consuming a pre-shared entangled pair). The quantum gain in communication is *detectability of eavesdropping*, not capacity (judgement; not in the inventory errata).

*You've got it when* you can write $\lvert D\rangle$ and $\lvert A\rangle$ in the $H/V$ basis and give the outcome probabilities for any state in either basis.

### Move M9.2: No-cloning in four lines (the step the lecture omits)

The lecture's proof (L51-57) uses a cloner $U_\text{cl}$ but never says what it does to basis states, and then silently uses $U_\text{cl}\lvert 10\rangle = \lvert 11\rangle$ in Eq 4.2. Here is the complete argument, with that definition stated.

1. **Define the cloner on the basis states** (the missing line): $U\lvert0\rangle\lvert0\rangle = \lvert0\rangle\lvert0\rangle$ and $U\lvert1\rangle\lvert0\rangle = \lvert1\rangle\lvert1\rangle$.
2. **Apply it to a superposition, using linearity:** $U(\alpha\lvert0\rangle+\beta\lvert1\rangle)\lvert0\rangle = \alpha\lvert00\rangle + \beta\lvert11\rangle$.
3. **Write what a clone would be:** $(\alpha\lvert0\rangle+\beta\lvert1\rangle)(\alpha\lvert0\rangle+\beta\lvert1\rangle) = \alpha^2\lvert00\rangle + \alpha\beta\lvert01\rangle + \alpha\beta\lvert10\rangle + \beta^2\lvert11\rangle$.
4. **Compare:** the cross terms need $\alpha\beta = 0$, and then $\alpha^2 = \alpha$, $\beta^2 = \beta$ as well. So the cloner works only for $\lvert0\rangle$ or $\lvert1\rangle$, never for a superposition of them. No linear (unitary) machine copies an unknown state.

**Why it matters for BB84.** A machine that clones $\lvert H\rangle$ and $\lvert V\rangle$ will fail on $\lvert D\rangle$ and $\lvert A\rangle$, which are superpositions of $H$ and $V$. Since Eve does not know which basis Alice used, she cannot keep a perfect copy and forward the original. She has to measure, and measuring in the wrong basis disturbs the photon (M9.4). **It also forbids an amplifier**, which would be a cloner; that is the erratum at L152 (M10.3).

*You've got it when* you can write lines 1-4 from memory and say where the lecture's version needed line 1.

### Move M9.3: BB84 by hand, and sifting

**Idea (lecture L77-93).** Alice picks a random bit and a random basis for each photon. Bob picks a random basis to measure each one. Over the classical channel they announce **bases only**, never bits, and keep the positions where the bases match (**sifting**). With random bases the match rate is $\tfrac12$, so about half the detected photons survive. Then they sacrifice a random sample of the sifted bits to estimate the error rate (lecture L93), and stop if it is too high.

*Worked clone (a fresh 10-photon run; not Table 4.1's bits).*

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Alice bit | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| Alice basis | R | D | D | R | R | D | R | D | R | D |
| Alice sends | H | A | A | H | V | D | H | A | V | D |
| Bob basis | R | R | D | D | R | D | D | D | R | R |
| Bases match? | yes | no | yes | no | yes | yes | no | yes | yes | no |
| Bob measures | H | V (random) | A | D (random) | V | D | A (random) | A | V | H (random) |
| Bob bit | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| Sifted key | 0 | – | 1 | – | 1 | 0 | – | 1 | 1 | – |

Six of ten positions match (60%, against an expected 50%; with ten photons, exactly six matches has probability $\binom{10}{6}/2^{10} = 0.21$). The sifted key is **011011**. To test for Eve they reveal, say, positions 3 and 8 (both agree), and keep **0101** from positions 1, 5, 6 and 9. In a real system the run is millions of photons long, the test sample is a few per cent, and the surviving key is then corrected for errors and shortened by **privacy amplification** to remove whatever Eve might know (Pirandola et al. 2020, BB84 section; judgement on the level of detail).

*You've got it when* you can fill in a blank BB84 table for any bits and bases, sift it, and say exactly what is announced in public.

### Move M9.4: Intercept-resend, the 25% error and $(3/4)^n$ detection

**Idea.** The simplest attack: Eve measures every photon in a random basis and sends Bob a fresh photon in the state she found. Look only at the sifted positions (Alice and Bob used the same basis):
- With probability $\tfrac12$, Eve chose the right basis. She learns the bit and resends the right state: **no error**.
- With probability $\tfrac12$, she chose the wrong basis. She resends a state in the wrong basis, and Bob's measurement in Alice's basis is a coin toss: **error with probability $\tfrac12$**.

So the **quantum bit error rate** (QBER) on the sifted key is

$$\text{QBER} = \tfrac12\times\tfrac12 = \tfrac14 = 25\%.$$

If Eve intercepts only a fraction $f$ of the photons, $\text{QBER} = f/4$.

**Detection.** Each checked sifted bit reveals a full intercept-resend Eve with probability $\tfrac14$, so she survives $n$ checked bits with probability $(3/4)^n$, and

$$P_\text{detect} = 1 - (3/4)^n .$$

*Worked clone.* $n = 10$: $P_\text{detect} = 1 - 0.75^{10} = 0.944$. To push Eve's survival below $10^{-6}$, $n > \ln(10^{-6})/\ln(0.75) = 48.0$, so 49 checked bits.

**What real systems do.** Real channels have a few per cent QBER from noise, so Alice and Bob cannot blame every error on Eve. They assume the worst (all errors are Eve's), then remove her possible knowledge by privacy amplification. For BB84 with one-way processing a secret key is possible only while the QBER stays below about **11%** (Pirandola et al. 2020, BB84 section; Shor-Preskill bound). Full intercept-resend at 25% is far beyond it. The asymptotic secret fraction per sifted bit is $r = 1 - 2h(Q)$, with $h$ the binary entropy (same source; used in Exercise 6.7).

*A lecture note (judgement; not in the inventory errata).* L102 says there is "a small probability that Eve guesses all the bases correctly": that is the $(3/4)^n$ survival above (strictly, she survives a bit even with a wrong basis half the time).

*You've got it when* you can derive 25% in two lines, compute $1-(3/4)^n$ for any $n$, and invert it for the $n$ that reaches a target.

### Move M9.5: B92 and E91 in brief

**B92 (lecture L104-121).** Two non-orthogonal states only: $\lvert H\rangle$ for 0 and $\lvert D\rangle$ (+45°) for 1. Bob measures in R or D at random. He gets a *conclusive* result only when his outcome is impossible for one of Alice's states: $V$ rules out $H$, so Alice sent $D$ (bit 1); $A$ (−45°) rules out $D$, so Alice sent $H$ (bit 0). That happens with probability $\tfrac12\times\tfrac12 = \tfrac14$ per photon (the lecture's step 2: keep only "V or −"). Simpler hardware, lower yield.

*A lecture note (judgement on the origin of the slip; the arithmetic is enumerated in the check module and in `week04_companion.md` 4E).* L121 (B92): the 75% does not hold. Under intercept-resend (Eve measures in R or D at random and resends what she sees), Bob's conclusive fraction rises from 1/4 to 3/8 of photons and 1/3 of his kept bits are wrong; each checked kept bit exposes Eve with probability 1/3, so she survives $n$ checks with probability $(2/3)^n$. The lecture's 3/4 is BB84's per-bit survival probability, not a B92 detection probability.

**E91 (lecture L123-142).** A source sends one photon of an entangled pair to each of Alice and Bob. Matching measurement bases give correlated bits for the key; the other basis combinations go into the CHSH test (M10.1). If the CHSH value is near $2\sqrt2$, the pairs are still entangled and Eve has no information about them. Two corrections:
- **Erratum W1 L52.** Week 1 says QKD "uses entangled particles". BB84 and B92 use none: single photons from Alice. Entanglement-based QKD (E91) is a separate family.
- **L125, "the information will be instantly known".** Measuring one particle fixes the *correlation*, but no message travels: Bob's own results look random until Alice tells him her bases over the classical channel. That is the no-signalling principle and the reason W4 quiz Q2 rejects "transfer messages instantaneously" (judgement wording; inventory W4 Q2).

*You've got it when* you can say in one line each how B92 and E91 differ from BB84, and correct L52 and L125.

### Move M10.1: CHSH, $2$ versus $2\sqrt2$ (arithmetic only)

**Idea.** Alice measures with analyser angle $a$ or $A$, Bob with $b$ or $B$; each result is $\pm1$. The lecture's Eq 4.3 (L137) combines four correlations:

$$S = \langle ab\rangle + \langle AB\rangle + \langle aB\rangle - \langle Ab\rangle .$$

**Why classical gives at most 2.** If each photon carries pre-set answers $a, A, b, B \in\{\pm1\}$, then $S = a(b+B) + A(B-b)$ for each pair. One bracket is 0 and the other is $\pm2$, so every pair gives $\pm2$ and the average satisfies $\lvert S\rvert\le2$. (This two-line bound is all we need; the full Bell derivation is skipped, per the spec.)

**Quantum value.** For the polarisation-entangled state $(\lvert HH\rangle+\lvert VV\rangle)/\sqrt2$ the correlation between analysers at angles $\theta_1$ and $\theta_2$ is

$$E(\theta_1,\theta_2) = \cos 2(\theta_1 - \theta_2)$$

(standard result; Pirandola et al. 2020, entanglement-based QKD section). Choose angles from $\{0°, 22.5°, 45°, 67.5°\}$: Alice $a = 22.5°$, $A = 67.5°$; Bob $b = 0°$, $B = 45°$. Then

| Term | Angle difference | $\cos 2(\Delta\theta)$ |
|---|---|---|
| $\langle ab\rangle$ | 22.5° | $\cos45° = 0.707$ |
| $\langle AB\rangle$ | 22.5° | $0.707$ |
| $\langle aB\rangle$ | −22.5° | $0.707$ |
| $\langle Ab\rangle$ | 67.5° | $\cos135° = -0.707$ |

$$S = 0.707 + 0.707 + 0.707 - (-0.707) = 4\times0.707 = 2\sqrt2 \approx 2.83 > 2.$$

**Noise.** If the pairs are mixed with noise so that the correlations shrink by a visibility $V$, then $S = 2\sqrt2\,V$, which beats 2 only when $V > 1/\sqrt2 = 0.707$. *Worked clone:* $V = 0.9$ gives $S = 2.55$.

The lecture's L142 says Alice and Bob "will measure less than 2" if Eve has measured the particles. More exactly: if Eve measures every photon, the pairs are no longer entangled and $S \le 2$; for the angle set above, measuring in $H/V$ gives $S = \sqrt2$ (Exercise 6.5).

*You've got it when* you can compute $S$ for the 0°/22.5°/45°/67.5° set from $\cos 2\Delta\theta$, and say what $S = 2.4$ or $S = 1.9$ tells Alice and Bob.

### Move M10.2: Fibre loss in dB/km, transmission and key rate

**Idea.** Telecom fibre at 1550 nm loses about $\alpha = 0.2$ dB/km (typical value for standard fibre; Pirandola et al. 2020 use it). Decibels add, so a link of length $L$ loses $\alpha L$ dB, and the fraction of photons that arrive is

$$\eta = 10^{-\alpha L/10}.$$

At 0.2 dB/km: every 15 km halves the photons (3 dB), every 50 km divides them by 10.

*Worked clone.*
- 50 km: 10 dB, $\eta = 0.1$. 100 km: 20 dB, $\eta = 0.01$.
- 1000 km: 200 dB, $\eta = 10^{-20}$. A source emitting $10^{9}$ photons per second would deliver one photon every $10^{11}$ s, about 3200 years.

**Key rate.** Classical links fix loss with optical amplifiers. Quantum links cannot (no-cloning, M9.2), so each lost photon is simply gone, and at long distance the **key rate is proportional to $\eta$**: it falls exponentially with distance. There is a hard ceiling for any point-to-point protocol without a repeater: at most $-\log_2(1-\eta)$ secret bits per channel use, which is about $1.44\,\eta$ when $\eta$ is small (the repeaterless or "PLOB" bound; Pirandola et al. 2020, section on limits of point-to-point QKD). *Worked clone:* at 100 km, $-\log_2(0.99) = 0.0145$ bits per use; at $10^9$ uses per second that is at most 14.5 Mbit/s. Real systems sit well below the ceiling (detector efficiency, dark counts, error correction), and beyond a few hundred kilometres the detector noise floor stops them entirely (judgement; Pirandola et al. 2020 practical sections). Twin-field QKD, the 600 km laboratory result in L167, beats the ceiling's scaling ($\propto\sqrt\eta$) by using a middle station, but it is still a lab result.

*You've got it when* you can turn km into dB into $\eta$ in your head at 0.2 dB/km, and explain why key rate falls exponentially while a classical link's does not.

### Move M10.3: Trusted nodes versus quantum repeaters (erratum L152)

**Trusted node.** Chain QKD links: Alice to node, node to Bob. The node shares key $K_1$ with Alice and key $K_2$ with Bob. It announces $K_1\oplus K_2$ publicly; Bob XORs it with $K_2$ and recovers $K_1$, which becomes the Alice-Bob key. In short, the node **decrypts and re-encrypts**, and it knows $K_1$. You know this pattern: it is a TLS-terminating proxy. It works today (lecture L201-211 calls these demonstrations "not true quantum networks"), but **every node sees the key** and must be physically secured and trusted.

**Quantum repeater.** Never measures the data. It
1. makes entangled pairs over short segments (Alice to node, node to Bob),
2. stores them in a **quantum memory** until both segments succeed,
3. performs **entanglement swapping**: a joint (Bell) measurement on the node's two photons leaves Alice's and Bob's photons entangled with each other, though they never met,
4. optionally **purifies** (distils) several noisy pairs into fewer, better ones.

Alice and Bob then run E91-style QKD end to end. The node learns nothing about the key, and the rate can beat the repeaterless ceiling.

**Erratum L152.** The lecture says "the aim of a quantum repeater is to amplify the signal". Amplifying an unknown quantum state would be cloning it, which M9.2 forbids. Repeaters work by **entanglement swapping plus memories** (with purification). The lecture's own L152 opening sentence and L219 ("no method of amplifying the signal without measuring the quantum state") say the right thing; the middle of L152 contradicts them. Repeaters are not yet out of the laboratory (L219). But L219's own opening, that repeaters are "outside of the current scope of physics", is itself wrong: read it as outside current **engineering**. The physics (swapping, memories, purification) is known and parts have been demonstrated in the lab (L219 itself cites the progress); reliable, fast quantum memories are the bottleneck (judgement; matches `week04_companion.md` 4H.4).

*You've got it when* you can draw a trusted-node chain and a repeater chain side by side and mark where the key is visible in each.

### Move M10.4: Satellite versus fibre, in one paragraph

In fibre, loss grows **exponentially** with length (M10.2). In free space, a beam mostly spreads by diffraction, so the received fraction falls roughly as $1/L^2$: doubling the distance costs a factor 4 (6 dB), not hundreds of dB. For a satellite, most of the absorbing atmosphere is in the bottom few tens of kilometres of the path, so a ground-to-space link of hundreds of kilometres can lose less than a 1000 km fibre's 200 dB by many orders of magnitude (L177; Chapman & Peters 2022, <https://physics.aps.org/articles/v15/172>). The costs are just as real: a satellite is visible only for minutes per pass, works best at night and in clear weather, delivers kbit/s rather than the Gbit/s of fibre (L177), and today acts as a **trusted node** in the sky, since it holds the keys it relays (Chapman & Peters 2022). Fibre suits metro and regional links; satellites suit continental and intercontinental key exchange.

*You've got it when* you can explain in two sentences why satellites win at 1000 km and lose at 40 km.

### Week 4 quiz and a QuVis pointer

**Quiz (inventory rows W4 Q1-Q4).** Do it cold, then check against the key in `docs/problem_inventory.md` (Quizzes table, Week 4). Today's physics covers Q2 (eavesdropping is detectable, not preventable, and nothing is instantaneous; M9.4, M9.5) and Q4 (flagged loose: QKD distributes a key, M8.3).

**QuVis BB84 (inventory row W4 interactive).** Not run today: do it in the Week 4 companion session, following `week04_companion.md` §9 (about 30 minutes).

## Exercises

Cold attempt first; open the hint only after a real try. Solution sketches use the six steps: Restate, Write state, Name move, Algebra, Check, Answer. All Harrowmere Water & Power figures come from the shared fact sheet at the end of `STRATEGY.md` and are invented for practice, marked (fictional). The ones used today: the control centre is linked to **four sites over dark fibre at 12, 38, 95 and 160 km**; each site's **AES-256 key is refreshed every 60 s**; telemetry must stay confidential for **15 years** ($x$); a full cryptographic migration takes **5 years** ($y$). Anything else (a QKD box's rate, a price) belongs to a clearly **hypothetical** candidate device or quote and is labelled so.

**Assumptions used in every channel calculation (state them in your own answers too, F3).** Harrowmere's dark fibre is taken to lose the typical 0.2 dB/km at 1550 nm, with no extra splice or connector loss; the hypothetical QKD box's key rate is taken to scale as $\eta$ from its quoted reference point. Both are optimistic, and both are the first things a real survey would measure.

### Exercise 6.1 (quantitative)

(a) Each Harrowmere site refreshes an AES-256 key every 60 s (fictional). What key rate does one site need, in bit/s, and how many key bits per day? What do all four sites need together? (b) A hypothetical QKD box delivers 10 kbit/s of secure key on a link. If Harrowmere instead used that key as a one-time pad, what is the most telemetry it could encrypt, and how many times over does the same key cover the AES need of one site? (c) Apply Mosca's inequality with $x = 15$ and $y = 5$ years (fictional) for a range of $z$ from 10 to 25 years (judgement: published expert estimates of $z$ vary widely). For which $z$ is Harrowmere exposed, and what is the exposure window at the pessimistic end? (d) What $z$ would make Harrowmere just safe?

**Hint:** AES key rate = 256 bits / rekey interval; OTP key rate = data rate (Move M8.1). Mosca: compare $x + y$ with $z$ (Move M8.2).

**Solution sketch:**
- *Restate:* the AES key requirement, the OTP ceiling set by a key rate, and a Mosca test over a range.
- *Write state:* rekey 60 s; 4 sites; QKD key 10 kbit/s (hypothetical); $x = 15$, $y = 5$, $z\in[10, 25]$.
- *Name move:* M8.1 and M8.2.
- *Algebra:* (a) $256/60 = 4.3$ bit/s per site; per day $256\times1440 = 368\,640$ bits (about 46 kB); four sites $4\times4.27 = 17$ bit/s. (b) At most 10 kbit/s of telemetry under an OTP; $10\,000/4.27 = 2.3\times10^{3}$ times the AES need. (c) $x + y = 20$; exposed whenever $z < 20$; at $z = 10$ the window is $20 - 10 = 10$ years. (d) $z = 20$ years.
- *Check:* both sides of every comparison are key rates in bit/s for the same site, so the ratio in (b) is like-for-like (F3).
- *Answer:* 4.3 bit/s per site (368 640 bits a day), 17 bit/s for all four. The same 10 kbit/s could pad at most 10 kbit/s of telemetry, or cover AES rekeying about 2300 times over. Harrowmere is exposed for any $z$ below 20 years, by up to 10 years at the pessimistic end, so the key exchange should be made quantum-safe now.

### Exercise 6.2 (quantitative)

(a) Write $\lvert D\rangle$ and $\lvert A\rangle$ in the $H/V$ basis and show $\langle D\vert A\rangle = 0$ and $\lvert\langle H\vert D\rangle\rvert^2 = \tfrac12$. (b) A photon polarised at 30° is measured in R and in D. Give $P(H)$, $P(V)$, $P(D)$, $P(A)$. (c) Alice sends $\lvert A\rangle$ and Bob measures in R. What is the chance Bob's bit equals Alice's bit, and why does this position get discarded?

**Hint:** Malus: $P = \cos^2(\text{angle to the analyser axis})$. D is at 45°, A at −45° (Move M9.1).

**Solution sketch:**
- *Restate:* basis algebra, Malus probabilities, and the wrong-basis case.
- *Write state:* $\lvert D\rangle = (\lvert H\rangle+\lvert V\rangle)/\sqrt2$, $\lvert A\rangle = (\lvert H\rangle-\lvert V\rangle)/\sqrt2$; $\theta = 30°$.
- *Name move:* M9.1.
- *Algebra:* (a) $\langle D\vert A\rangle = \tfrac12(1\cdot1 + 1\cdot(-1)) = 0$; $\langle H\vert D\rangle = 1/\sqrt2$, squared $\tfrac12$. (b) $P(H) = \cos^2 30° = 0.75$, $P(V) = 0.25$; $P(D) = \cos^2(45°-30°) = \cos^2 15° = 0.93$, $P(A) = 0.07$. (c) $\lvert A\rangle$ in R gives $H$ or $V$ with probability $\tfrac12$ each, so Bob's bit matches with probability 0.5; the bases differ, so the position is discarded in sifting.
- *Check:* each pair of probabilities sums to 1; at 45° both bases would give 0.5/0.5 or 1/0, as expected.
- *Answer:* (a) shown; (b) 0.75, 0.25, 0.93, 0.07; (c) 0.5, a coin toss, so it carries no shared information and is dropped.

### Exercise 6.3 (quantitative)

A fresh BB84 run (different from Move M9.3 and from the lecture's Table 4.1):

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Alice bit | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| Alice basis | D | R | R | D | D | R | D | R | D | R |
| Bob basis | R | D | R | R | D | R | D | D | D | D |
| Bob's random outcome where bases differ | H | D | – | V | – | – | – | A | – | D |

(a) Fill in "Alice sends" and Bob's bit at every position. (b) Sift: which positions survive, and what is the sifted key? What fraction is that? (c) (stretch) Compare Alice's and Bob's *raw* (unsifted) strings: how many of the 10 agree, and why is that useless? (d) (stretch) What exactly is said over the public channel? (e) (stretch) If Bob detects $2\times10^{6}$ photons, roughly how long is the sifted key? If 5% of it is sacrificed for testing, how many bits remain?

**Hint:** R: H = 0, V = 1. D: D(+45°) = 0, A(−45°) = 1. Same basis → Bob gets Alice's bit; different basis → use the given random outcome (Move M9.3).

**Solution sketch:**
- *Restate:* complete the table, sift, compare, and scale up.
- *Write state:* Alice sends A, V, H, D, A, H, A, V, D, V.
- *Name move:* M9.1 and M9.3.
- *Algebra:* (a) Bob's bits: 0 (H), 0 (D), 0 (H), 1 (V), 1 (A), 0 (H), 1 (A), 1 (A), 0 (D), 0 (D). (b) Bases match at 3, 5, 6, 7, 9: five of ten, 50%. Sifted key **01010**. (c) Raw strings: Alice 1100101101, Bob 0001101100; they agree at 6 of 10 (positions 3, 5, 6, 7, 8, 9), but position 8 agrees only by chance, and nobody can tell which wrong-basis positions agreed. (d) Bob announces his ten bases; Alice says which match; then they reveal the values at a few sifted test positions. Never the other bits. (e) $2\times10^{6}\times0.5 = 10^{6}$ sifted bits; after 5% testing, $9.5\times10^{5}$.
- *Check:* every matched position has Bob's bit equal to Alice's, as it must without Eve or noise.
- *Answer:* sifted key 01010 (50%); raw agreement 6/10 is meaningless off the matched positions; about $10^{6}$ sifted bits and $9.5\times10^{5}$ after testing, before error correction and privacy amplification.

### Exercise 6.4 (quantitative)

(a) Alice sends $\lvert D\rangle$ (bit 0). Eve measures in R, gets $H$, and resends $\lvert H\rangle$. Bob measures in D. What is the probability that Bob's bit is wrong? (b) Use (a) to derive the QBER for full intercept-resend. (c) Eve intercepts only 40% of the photons. What QBER does she cause? (d) With full intercept-resend, what is the detection probability if Alice and Bob check 20 sifted bits? (e) How many checked bits give 99.9% detection with full intercept-resend, and how many with Eve at 40%?

**Hint:** QBER $= f/4$. Per checked bit, Eve is caught with probability QBER, so survival after $n$ bits is $(1-\text{QBER})^n$ (Move M9.4). Solve $(1-\text{QBER})^n < 10^{-3}$ with logarithms and round up.

**Solution sketch:**
- *Restate:* single-photon error, QBER for full and partial attack, detection probabilities.
- *Write state:* $f = 1$ and $f = 0.4$; $n = 20$; target $10^{-3}$ survival.
- *Name move:* M9.4.
- *Algebra:* (a) $\lvert H\rangle$ measured in D gives D or A with probability $\tfrac12$ each: error 0.5. (b) Eve's basis is wrong half the time; then the error is $\tfrac12$: QBER $= \tfrac12\times\tfrac12 = 0.25$. (c) $0.4/4 = 0.10$. (d) $1 - 0.75^{20} = 0.997$. (e) $n > \ln(10^{-3})/\ln(0.75) = 24.0$, so 25 bits (check: $0.75^{24} = 0.0010$, just above the target); at $f = 0.4$, $n > \ln(10^{-3})/\ln(0.9) = 65.6$, so 66 bits.
- *Check:* a gentler Eve is harder to catch per bit but still causes a 10% QBER, which is close to BB84's 11% limit for a usable key, so she cannot hide in a large sample.
- *Answer:* (a) 0.5; (b) 25%; (c) 10%; (d) 99.7%; (e) 25 checked bits for a full attack, 66 for a 40% attack. Real systems check thousands of bits.

### Exercise 6.5 (quantitative)

Use $E(\theta_1,\theta_2) = \cos 2(\theta_1-\theta_2)$ and the lecture's $S = \langle ab\rangle + \langle AB\rangle + \langle aB\rangle - \langle Ab\rangle$. (a) With $a = 22.5°$, $A = 67.5°$, $b = 0°$, $B = 45°$, compute all four terms and $S$. (b) The source has visibility $V = 0.85$. What is $S$, and does it violate the classical bound? (c) What is the smallest visibility that still violates it? (d) (stretch) Alice and Bob carelessly use $a = b = 0°$ and $A = B = 45°$. What is $S$? (e) (stretch) Eve measures every photon in $H/V$ before forwarding it, so each pair becomes $HH$ or $VV$ at random, with correlation $E = \cos2\theta_1\cos2\theta_2$. What is $S$ for the angles in (a)?

**Hint:** Work in a table of angle differences (Move M10.1). For (e), $\cos 2\theta$ at 0°, 22.5°, 45°, 67.5° is 1, 0.707, 0, −0.707.

**Solution sketch:**
- *Restate:* CHSH value for ideal, noisy, badly chosen and attacked cases.
- *Write state:* angle differences in (a): 22.5°, 22.5°, −22.5°, 67.5°.
- *Name move:* M10.1.
- *Algebra:* (a) $0.707 + 0.707 + 0.707 - (-0.707) = 2.83 = 2\sqrt2$. (b) $2.83\times0.85 = 2.40 > 2$: violated. (c) $V = 1/\sqrt2 = 0.707$. (d) $\langle ab\rangle = \cos0 = 1$, $\langle AB\rangle = 1$, $\langle aB\rangle = \cos 90° = 0$, $\langle Ab\rangle = 0$: $S = 2$, no violation. (e) $\langle ab\rangle = 0.707\times1$, $\langle AB\rangle = (-0.707)\times0 = 0$, $\langle aB\rangle = 0.707\times0 = 0$, $\langle Ab\rangle = (-0.707)\times1$; $S = 0.707 + 0 + 0 + 0.707 = 1.41 = \sqrt2$.
- *Check:* (e) sits below 2, as any classically correlated source must (Move M10.1's two-line bound).
- *Answer:* (a) $2\sqrt2\approx2.83$; (b) 2.40, violated; (c) $V > 0.707$; (d) 2, so the angle choice matters; (e) $\sqrt2\approx1.41$: Eve's measurement destroys the violation, which is how E91 detects her.

### Exercise 6.6 (quantitative)

Harrowmere's four sites sit at 12, 38, 95 and 160 km of dark fibre (fictional). A hypothetical candidate QKD box is quoted at 10 kbit/s of secure key over 40 km of standard fibre in the vendor's own test (hypothetical datasheet), with a maximum range of 120 km (hypothetical). Use the two assumptions stated above. (a) Find the loss in dB and $\eta$ for each site. (b) Estimate the key rate at each site. (c) The 160 km site is beyond range. With one trusted node halfway, what is the key rate per hop? (d) Compare each rate with the 4.3 bit/s per site that Harrowmere's AES rekeying needs (Exercise 6.1). (e) At $10^{9}$ pulses per second, what is the repeaterless ceiling at the 95 km site?

**Hint:** $\eta = 10^{-\alpha L/10}$; the rate scales by $10^{-\alpha(L-40)/10}$ from the 40 km reference (Move M10.2). Ceiling: $-\log_2(1-\eta)$ bits per pulse.

**Solution sketch:**
- *Restate:* loss, transmission, scaled key rates, a trusted-node split, a like-for-like comparison with the need, and the PLOB ceiling.
- *Write state:* $\alpha = 0.2$ dB/km (assumed); $L = 12, 38, 95, 160$ km; reference 10 kbit/s at 40 km (hypothetical box).
- *Name move:* M10.2 and M10.3.
- *Algebra:* (a) 12 km: 2.4 dB, $\eta = 0.58$; 38 km: 7.6 dB, $\eta = 0.17$; 95 km: 19 dB, $\eta = 0.013$; 160 km: 32 dB, $\eta = 6.3\times10^{-4}$. (b) 12 km: $10\times10^{0.56} = 36$ kbit/s; 38 km: $10\times10^{0.04} = 11$ kbit/s; 95 km: $10\times10^{-1.1} = 0.79$ kbit/s; 160 km: $10\times10^{-2.4} = 0.040$ kbit/s = 40 bit/s on paper, but beyond range, so zero in practice. (c) Two 80 km hops of 16 dB each: $10\times10^{-0.8} = 1.6$ kbit/s per hop. (d) Every reachable site clears 4.3 bit/s by a factor of about 180 (the 95 km site) or more. (e) $-\log_2(1-0.0126) = 0.018$ bits per pulse, at most 18 Mbit/s.
- *Check:* every extra 50 km divides the rate by 10 (95 km is 55 km past the reference: $10^{-1.1}$). The 12 km figure is an extrapolation *upwards* from the reference, where detector saturation may cap it, so treat 36 kbit/s as an upper estimate (judgement).
- *Answer:* 12 km: 2.4 dB, about 36 kbit/s (upper estimate); 38 km: 7.6 dB, about 11 kbit/s; 95 km: 19 dB, about 0.79 kbit/s; 160 km: 32 dB, out of range, about 1.6 kbit/s per hop with a trusted node. All exceed the 4.3 bit/s AES need, so key rate is not the binding constraint for Harrowmere; range, the trusted node and cost are. Ceiling at 95 km: about 18 Mbit/s.

### Exercise 6.7 (quantitative) (stretch)

The asymptotic BB84 secret fraction per sifted bit is $r = 1 - 2h(Q)$, with $h(Q) = -Q\log_2Q - (1-Q)\log_2(1-Q)$ (Pirandola et al. 2020). (a) Compute $r$ at $Q = 1\%$, $4\%$ and $11\%$. (b) On the 38 km site, the hypothetical box's receiver detects 40 kbit/s of raw bits with QBER 2.5% (hypothetical trial figures). Find the sifted rate, $h(Q)$, $r$ and the secure key rate.

**Hint:** Sift first (×0.5), then multiply by $r$ (Moves M9.3 and M9.4).

**Solution sketch:**
- *Restate:* secret fraction at three error rates, then a secure-rate budget.
- *Write state:* $Q = 0.01, 0.04, 0.11$; raw 40 kbit/s, $Q = 0.025$.
- *Name move:* M9.4 with M9.3.
- *Algebra:* (a) $h(0.01) = 0.081$, $r = 0.84$; $h(0.04) = 0.242$, $r = 0.52$; $h(0.11) = 0.500$, $r\approx0$. (b) Sifted $40\times0.5 = 20$ kbit/s; $h(0.025) = 0.169$; $r = 1 - 0.337 = 0.66$; secure $20\times0.66 = 13$ kbit/s.
- *Check:* $r$ falls to zero at 11%, the BB84 threshold quoted in Move M9.4, so the formula and the threshold agree.
- *Answer:* $r = 0.84$, 0.52 and about 0 at 1%, 4% and 11%. At 38 km: 20 kbit/s sifted, $r = 0.66$, about 13 kbit/s secure, the same order as Exercise 6.6's 11 kbit/s estimate. The "required fidelity" in the Consolidate task is this: keep the QBER well under 11%.

### Exercise 6.8 (writing)

*Inventory row W4 Apply.* Write a 200-300-word post on how quantum communication matters for one application area: securing **Harrowmere Water & Power**'s control-network telemetry. Use the Mosca test from Exercise 6.1 and the 38 km site from Exercise 6.6.

**Hint:** Start from Harrowmere's own threat (15-year confidentiality, 5-year migration), then the mechanism (eavesdropping leaves a 25% error), then what QKD would deliver at one named site against that site's actual key need (like for like: bit/s of key against bit/s of key). Say plainly that QKD feeds a classical cipher and needs authentication. Do not claim "unbreakable".

**Model paragraph:**
Harrowmere Water & Power's control centre talks to four sites over its own dark fibre, and the telemetry it sends (fictional) must stay confidential for 15 years. Each site's AES-256 key is refreshed every minute by a public-key exchange, and that exchange, not AES, is what Shor's algorithm would break. A full migration to new cryptography would take Harrowmere 5 years (fictional), so by Mosca's rule it is already exposed if a code-breaking quantum computer arrives within 20 years; at the pessimistic end of expert guesses (10 years) traffic recorded today would be readable for a decade while it still matters. Quantum key distribution replaces the vulnerable exchange with physics. The control centre sends single photons in one of two polarisation bases; an eavesdropper cannot copy them (no-cloning) and must measure, which corrupts about a quarter of the bits Harrowmere checks, so interception shows up in the error rate. The fit is good on rate: at the 38 km site, a candidate box quoted at 10 kbit/s over 40 km (hypothetical) would give about 11 kbit/s if the fibre meets the typical 0.2 dB/km, against the 4.3 bit/s the one-minute rekey actually uses. The limits are Harrowmere-specific. QKD only delivers keys; AES still encrypts. Its classical channel must be authenticated, with a pre-shared key or post-quantum signatures. The 160 km site is beyond the box's range and would need a trusted relay that sees every key. And the 38 substations are not on the dark-fibre list, so QKD would reach four sites at most. For Harrowmere, quantum communication matters for the four fibre-linked sites, not the whole network.

**What a weak answer misses:** It says QKD "cannot be intercepted" (W4 quiz Q2 says otherwise: interception is detectable, not impossible). It never says what is under threat (the key exchange, not AES) or why it matters now (Harrowmere's $x + y = 20$ years). It compares a vendor rate with nothing, or with a generic need, instead of Harrowmere's 4.3 bit/s per site. It forgets authentication, and it ignores the sites and substations QKD cannot serve.

### Exercise 6.9 (writing)

*Inventory row W4 Consolidate.* In 300 words, using all six parts of F1, argue how much more security QKD gives Harrowmere than classical options, and what the downsides are. Include bit rates and the required error rate, and compare with post-quantum cryptography. Hypothetical quotes for this exercise: a QKD box pair costs £120k installed; a trusted node also needs a secured building; a PQC upgrade of the whole control network (hybrid key exchange in firmware) costs £60k.

**Hint:** Use Exercise 6.6 for rates and 6.7 for the 11% QBER limit, and state the 0.2 dB/km assumption. Count the hardware from Harrowmere's own map: the 12, 38 and 95 km sites need one pair each; the 160 km site needs two pairs and a node. The figure of merit is secure key rate at a distance *and* what the security rests on; since every rate clears 4.3 bit/s, the decision turns on the second half.

**Model paragraph:**
(1) *Classical limit.* Harrowmere refreshes each site's AES-256 key every minute by elliptic-curve exchange, which Shor's algorithm would break; with telemetry that must stay secret 15 years and a 5-year migration (fictional), Mosca's rule leaves it exposed unless a code-breaking machine is more than 20 years away. (2) *Mechanism.* BB84 QKD encodes key bits in photon polarisation; no-cloning forces an eavesdropper to measure, which raises the error rate to 25% on intercepted bits. (3) *Figure of merit.* Secure key rate at each site's distance, the error rate tolerated, and what the security rests on. (4) *Gain.* Assuming the typical 0.2 dB/km on Harrowmere's dark fibre, a candidate box quoted at 10 kbit/s over 40 km (hypothetical) gives about 11 kbit/s at 38 km and 0.79 kbit/s at 95 km, and about 1.6 kbit/s per hop to the 160 km site via a halfway node. Each exceeds the 4.3 bit/s that one-minute rekeying needs, provided the error rate stays well below BB84's 11% limit (Pirandola et al. 2020). So rate is not Harrowmere's constraint; the gain is that keys stop resting on any mathematical assumption. PQC (NIST FIPS 203, 2024) also removes the Shor threat, but on newer computational assumptions. (5) *Maturity and practicality.* QKD needs five box pairs, about £600k on the hypothetical quote, against £60k for PQC on every link; it still needs authentication; the 160 km node sees every key on that route; and the 38 substations are off the dark fibre. (6) *Verdict.* For Harrowmere, migrate the whole control network to PQC first, as the NCSC advises, because only that fits inside the 20-year Mosca window everywhere; QKD is worth a trial on the 12 km and 38 km sites only. The caveat: an unsurveyed fibre with extra splice loss could cut the 95 km rate tenfold.

**What a weak answer misses:** It treats QKD and PQC as the same kind of fix. It quotes a key rate without a distance or without Harrowmere's 4.3 bit/s need beside it, or it compares a vendor lab figure with an assumed field loss without saying so. It forgets that a trusted node holds the key, or calls it a repeater, or says repeaters "amplify" (erratum L152). Its verdict could be pasted onto any company because it never uses Harrowmere's four distances, its 15 + 5 years, or its substations.

### Exercise 6.10 (writing)

*Errata in practice (about 10 minutes).* A Harrowmere board slide (fictional) says: "Our QKD supplier will add quantum repeaters that amplify the photons, so our entangled-photon QKD will encrypt telemetry instantly to all our sites, including the 160 km one." Write a 100-150-word correction for the board.

**Hint:** There are at least four errors: "amplify" (L152), "entangled-photon" (W1 L52), "encrypt" (W4 Q4 flag), and "instantly … all our sites" (L125, M10.2, and the dark-fibre map). Give the correct statement for each in plain words, with one Harrowmere number.

**Model paragraph:**
The slide needs four corrections. First, nothing can amplify a quantum signal: an amplifier would copy an unknown photon state, which the no-cloning theorem forbids. Quantum repeaters work differently, by entanglement swapping between stored photons, and none is yet in commercial service; for our 160 km site the realistic option is a trusted relay halfway, which sees every key and must be secured like a control room. Second, the QKD we are considering (BB84) uses single photons, not entangled ones. Third, QKD does not encrypt anything; it delivers keys, and AES still encrypts the telemetry. Fourth, it is neither instant nor universal: keys build up at kbit/s rates that fall about tenfold every 50 km of fibre, and only our four dark-fibre sites could be connected, not the 38 substations.

**What a weak answer misses:** It fixes "amplify" but does not say what repeaters do instead. It misses that the 160 km route would in practice use a trusted node, which changes the security argument. It lets "encrypt" stand, and gives no number for how distance limits the rate.

## Anti-patterns / Common mistakes

- **Saying QKD encrypts data.** How you'd notice: no classical cipher appears in your description. Instead: QKD distributes a key; an OTP or AES encrypts (M8.3, W4 Q4).
- **Forgetting authentication.** How you'd notice: your QKD design has no pre-shared key or signature. Instead: an unauthenticated QKD link is open to a man in the middle; state how the classical channel is authenticated.
- **"Quantum computers break AES."** How you'd notice: you claim Shor breaks symmetric ciphers. Instead: Shor breaks the public-key exchange; Grover only halves AES's key length in bits (M8.1, M8.2).
- **Using the OTP key need when the system runs AES (or the reverse).** How you'd notice: your verdict flips between "QKD is far too slow" and "QKD is far more than enough". Instead: state which cipher the key feeds, then compute (Exercise 6.1).
- **Calling a repeater an amplifier.** How you'd notice: the word "amplify" next to "quantum signal". Instead: no-cloning forbids it; repeaters use entanglement swapping plus memories (L152 erratum).
- **Calling a trusted node "end-to-end secure".** How you'd notice: a chain of QKD links with no mention of who can read the key in the middle. Instead: every trusted node holds the key, like a TLS-terminating proxy.
- **Saying "BB84 uses entanglement".** How you'd notice: you are repeating Week 1 L52. Instead: BB84 uses single photons; E91 uses entangled pairs.
- **Quoting the 25% error as Eve's chance of detection per photon sent.** How you'd notice: you forgot sifting. Instead: 25% is the error rate on the *sifted* bits under full intercept-resend; detection over $n$ checked bits is $1-(3/4)^n$.
- **Linear thinking about fibre distance.** How you'd notice: you halve the key rate for double the distance. Instead: dB add, so rate falls exponentially: ×0.1 per 50 km at 0.2 dB/km.

## Done when

Without notes, in 40 minutes, you can do all of the following. Pass mark: 8 of 10.

1. Explain the difference between a one-time pad and AES, and convert a data rate and rekey interval into a key rate.
2. State Mosca's inequality, define $x$, $y$ and $z$, and apply it to a case.
3. List the four limits of QKD from M8.3 and name the three NIST PQC standards.
4. Write $\lvert D\rangle$ and $\lvert A\rangle$ in the $H/V$ basis and give wrong-basis outcome probabilities.
5. Prove no-cloning in four lines, including the basis-state definition the lecture omits.
6. Run and sift a 10-photon BB84 table, and say what is announced publicly.
7. Derive the 25% intercept-resend QBER and compute $1-(3/4)^n$ for a given $n$.
8. Compute $S = 2\sqrt2$ for the 0°/22.5°/45°/67.5° angle set and state the classical bound.
9. Convert a fibre length to dB and $\eta$ at 0.2 dB/km, and explain why key rate falls exponentially.
10. Contrast a trusted node and a quantum repeater, and correct L152.

## Companion pointer and confusion log

Open `content/companions/week04_companion.md` (§3 notation and units, §4 errata, §9 QuVis walkthrough). Read lecture L65-102 (BB84 and Tables 4.1-4.2) with Moves M9.3 and M9.4 beside you, then L146-177 (hardware and channels) with M10.2 to M10.4. Log every symbol or statement you had to check twice (R/D, "+"/"−", $\langle ab\rangle$, "amplify", "trusted") with its lecture line.

| Symbol or line | What confused me | Resolution |
|---|---|---|
| | | |
| | | |

## Spaced review

Do this first, closed book, 15 minutes. Answers follow.

**From Day 05 (sensing checkpoint, M1-M7 and F1).**
1. A gravimeter has $40\ \mu\text{Gal}/\sqrt{\text{Hz}}$. What is its noise after averaging 400 s?
2. Compute $\Phi = k_\text{eff}gT^2$ for $k_\text{eff} = 1.6\times10^{7}\ \text{m}^{-1}$, $g = 9.81\ \text{m/s}^2$ and $T = 0.05$ s.
3. In which part of F1 do TRL and SWaP-C belong?

**From Day 03 (clocks and magnetometers).**
4. An optical transition at $5\times10^{14}$ Hz has a 0.5 Hz linewidth. What is $Q$?
5. A 1 mm² loop sits in a 1 nT field. How many flux quanta $\Phi_0 = h/2e$ thread it?

**From Day 01 (F1, F3 and M1).**
6. A clock has fractional error $10^{-14}$. What time error builds up in one day, and what distance is that at the speed of light?
7. State the F3 source hierarchy, top to bottom.

*Answers.* 1. $40/\sqrt{400} = 2\ \mu\text{Gal}$. 2. $1.6\times10^{7}\times9.81\times0.0025 = 3.9\times10^{5}$ rad. 3. Part 5, maturity and practicality. 4. $5\times10^{14}/0.5 = 10^{15}$. 5. $10^{-9}\times10^{-6} = 10^{-15}$ Wb, which is $10^{-15}/2.07\times10^{-15} = 0.48\,\Phi_0$. 6. $10^{-14}\times86\,400 = 8.6\times10^{-10}$ s, which is about 0.26 m. 7. Peer-reviewed paper or metrology institute > review > vendor datasheet > press release > market report.

## Read next

- Pirandola et al., *Advances in quantum cryptography* (2020), <https://arxiv.org/abs/1906.01645>. Read the introduction, the BB84 and discrete-variable protocol sections (sifting, QBER, the 11% threshold), the section on the limits of point-to-point QKD (the repeaterless bound), and the free-space and satellite sections.
- NCSC white paper, *Quantum security technologies*, <https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies>. Read all of it (short): it is the source for the QKD limits in M8.3 and the "PQC first" verdict.
