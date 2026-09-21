# Week 6 Companion — The Stern-Gerlach Experiment (concept and portfolio-essay method)

**Built on:** [Day 3](../day03.md) (operators, Pauli matrices: Moves 3.1 and 3.4) and the measurement idea from Day 5 ([Move 5.1](../day05.md), probabilities $|c_n|^2$). Method habits are in [STRATEGY](../../STRATEGY.md). Day 7 (Bell states, [Move 7.5](../day07.md)) is where the lecture's passing mention of entanglement pays off.

**What this week is, and is not.** There is almost no new maths. Week 6 asks for a *conceptual* understanding and feeds the Stern-Gerlach discussion in the Assessment 2 Portfolio essay. The only calculations are tiny spin-½ probability checks. The week's Apply task is to research and decide which results and implications of the experiment you consider most important. That judgement has to be yours, so this companion gives you a **method and a planning structure**, never essay text.

## What this week is really saying

Fire a beam of silver atoms through a magnet whose field is *not uniform*. Classically, each atom is a tiny bar magnet pointing in a random direction, so the atoms should be pushed by all sorts of different amounts and smear into a continuous band on a screen. What is actually seen is **two separate spots**, one deflected up and one deflected down.

Plain-English consequences, in the order the lecture builds them:

1. **Spin is quantised.** The component of the atom's magnetic moment along the field can take only two values, not a continuum. Spin is a genuinely quantum property with no classical picture that survives scrutiny (the lecture warns the "little arrow" picture will "deceive you sooner or later").
2. **Repeat the same measurement, get the same answer** (lecture 6.2). Send the upper beam of a $z$-magnet into a second $z$-magnet: it emerges upper again, every time. So the magnet both *prepares* and *measures*.
3. **Change the measurement direction and the earlier result is undone** (lecture 6.3). Send the upper $z$-beam into an $x$-magnet: you get up and down with probability 1/2 each. A definite $S_z$ means a completely undecided $S_x$. Put a third magnet (along $z$ again) after that and the $S_z$ value you thought you had "fixed" is 50/50 again. The second measurement can erase the first.
4. **Interference** (lecture 6.4). If you split a beam by $S_x$ and recombine it without looking at which path each atom took, the final $S_z$ result is as if nothing had happened. If you *do* look, it is 50/50. That is the double-slit story in spin language.

In state language: the beams are the eigenstates of the measured spin component. Measuring collapses the state onto one of them ([Move 5.3](../day05.md)). The eigenstates of $\hat{S}_x$ are *superpositions* of the eigenstates of $\hat{S}_z$, which is exactly why "definite $S_z$" implies "50/50 $S_x$".

## Notation decoder

| Symbol | Say it as | Means | Tiny example |
|---|---|---|---|
| $\hat{S}_z$, $\hat{S}_x$ | "S-z hat", "S-x hat" | The spin component along $z$ or $x$, and also the name of the Stern-Gerlach box whose field gradient points that way | A box labelled $\hat{S}_z$ in the lecture figures |
| $S_z = +$, $S_z = -$ | "S-z plus/minus" | The two outcomes (beams) of the $\hat{S}_z$ box | Upper beam is $S_z = +$ |
| $\hbar/2$ | "h-bar over two" | The size of the spin-½ eigenvalues. **Convention, not in the lecture:** the lecture only writes $+$ and $-$. The standard convention is $S_z = \pm\hbar/2$; $\hbar$ is Planck's constant divided by $2\pi$ | $\hat{S}_z$ returns $+\hbar/2$ or $-\hbar/2$ |
| $\lvert{\uparrow}\rangle,\ \lvert{\downarrow}\rangle$ | "ket up", "ket down" | The $\hat{S}_z$ eigenstates, written $\lvert u\rangle,\lvert d\rangle$ in Week 3 and $\lvert\psi_z^{\pm}\rangle$ in this week's lecture. All three notations name the same states | $\lvert{\uparrow}\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ |
| $\lvert\psi_x^{\pm}\rangle$ | "psi x plus/minus" | The $\hat{S}_x$ eigenstates. In the column basis above (a standard convention) $\lvert\psi_x^{\pm}\rangle = (\lvert{\uparrow}\rangle \pm \lvert{\downarrow}\rangle)/\sqrt{2}$ | Overlap with $\lvert{\uparrow}\rangle$ is $1/\sqrt{2}$, matching Eq. 6.2 |
| $\sigma_x,\sigma_y,\sigma_z$ | "sigma x, y, z" | Pauli matrices (Day 3, [Move 3.4](../day03.md)). Convention: $\hat{S}_i = \tfrac{\hbar}{2}\sigma_i$ | $\sigma_x\lvert{\uparrow}\rangle = \lvert{\downarrow}\rangle$, so $\hat{S}_x\lvert{\uparrow}\rangle = \tfrac{\hbar}{2}\lvert{\downarrow}\rangle$: not an eigenstate |
| $\langle b\mid a\rangle$ | "bra b, ket a" | The *amplitude* for a particle in state $a$ to come out in state $b$ | $\langle\psi_x^+\mid\psi_z^+\rangle = 1/\sqrt{2}$ |
| $P(b\mid a)=\lvert\langle b\mid a\rangle\rvert^2$ | "probability of b given a" | Probability = amplitude modulus squared (Eq. 6.1 to 6.4). Note this is a probability, not the amplitude | $P = \lvert 1/\sqrt2\rvert^2 = 1/2$ |
| inhomogeneous field | "in-homo-JEE-neous" | A magnetic field whose strength changes with position ($\mathrm{d}B_z/\mathrm{d}z \neq 0$) | Magnet poles shaped so the field is stronger near one pole |
| magnetic moment $\boldsymbol{\mu}$ | "mu" | How strongly the atom acts as a tiny bar magnet, and in which direction | $\boldsymbol{\mu} = \frac{gq}{2m}\mathbf{S}$ (lecture): proportional to spin |
| $F = \langle\mu_z\rangle\,\mathrm{d}B_z/\mathrm{d}z$ | "force equals mu-z times the field gradient" | The net force on the atom. Deflection is set by $\mu_z$ | Zero gradient means zero force |
| $g$, $q$, $m$ | "g-factor, charge, mass" | Constants relating spin to magnetic moment; for silver the 47th electron carries the effect | Only the ratio matters for the deflection size |
| $\mathbf{m}\cdot\mathbf{n}$ | "m dot n" | Dot product of two unit vectors giving the angle between the two magnet directions (Day 2, [Move 2.1](../day02.md)) | Perpendicular directions: $\mathbf{m}\cdot\mathbf{n} = 0$ |
| $\hat{S}_z\hat{S}_x\hat{S}_z\lvert\psi\rangle$ | "S-z, S-x, S-z on psi" | A three-magnet sequence. **Read right to left**: the right-most operator is the *first* apparatus (lecture 6.2) | Right-most $\hat{S}_z$ acts first |
| collapse | "collapse" | After a measurement the state is the eigenstate for the result seen ([Move 5.3](../day05.md)) | After $S_z = +$ the state is $\lvert{\uparrow}\rangle$ |

## Skipped steps, expanded

### Why the field must be inhomogeneous

The force on a magnetic moment is $F = \langle\mu_z\rangle\,\mathrm{d}B_z/\mathrm{d}z$ (lecture, 6.1). The force depends on the **gradient** of the field, not on its strength. In a uniform field $\mathrm{d}B_z/\mathrm{d}z = 0$, so there is no net push. (A tiny magnet in a uniform field feels a twisting effect but no net sideways force, so the beam would not split.) Only a field that changes with position pulls the "north end" of the atom's magnet differently from its "south end", producing a net force. That is why Question 2 of the quiz is about *inhomogeneous* fields.

The lecture also says: if $\boldsymbol{\mu}$ is perpendicular to $\mathbf{B}$ there is no deflection; if aligned or anti-aligned the deflection is maximal. Since deflection tracks $\mu_z$, the pattern on the screen is a direct map of the allowed $\mu_z$ values.

### What "two beams, not a smear" implies

- Classically the atoms' magnets point in all directions, so $\mu_z$ would run continuously from $-\mu$ to $+\mu$ and the screen would show a filled band.
- Two spots means $\mu_z$ takes exactly two values. Since $\boldsymbol{\mu}\propto\mathbf{S}$, so does $S_z$: it is quantised (compare the discrete energy levels of the oscillator in Week 5).
- For a single atom the result is *one* of the two beams, not both at once. The lecture says a particle "can subsequently emerge in either (but not simultaneously both)" of the trajectories. The sum over many atoms fills both spots.
- The silver detail (47 electrons, 46 forming a spherically symmetric cloud, the 47th in a $5s$ orbital) is there only to justify treating a silver atom as "a heavy electron" for spin purposes. It is context, not something you compute with.

### The sequential-measurement paradox in spin-state language (Moves 3.4, 5.1)

Write the $\hat{S}_z$ eigenstates as $\lvert{\uparrow}\rangle,\lvert{\downarrow}\rangle$ and the $\hat{S}_x$ eigenstates as $\lvert\psi_x^{\pm}\rangle = (\lvert{\uparrow}\rangle \pm \lvert{\downarrow}\rangle)/\sqrt{2}$ (standard convention).

1. **Same-type repeat.** After an $S_z=+$ result the state is $\lvert{\uparrow}\rangle$. Expanding in the $z$-eigenbasis: $\lvert{\uparrow}\rangle = 1\cdot\lvert{\uparrow}\rangle + 0\cdot\lvert{\downarrow}\rangle$. [Move 5.1](../day05.md) gives probability $1^2 = 1$ for $+$ and $0^2 = 0$ for $-$. That is Eq. 6.1: certainty, and the identity-like table in the lecture just lists these probabilities. (That table is a table of amplitude sizes, **not** the spin operator: the operator $\hat{S}_z$ has eigenvalues $\pm\hbar/2$, so it is $\tfrac{\hbar}{2}\sigma_z$, not the identity.)
2. **Different-type step.** Re-expand $\lvert{\uparrow}\rangle$ in the $x$-eigenbasis. Because $\lvert{\uparrow}\rangle = (\lvert\psi_x^+\rangle + \lvert\psi_x^-\rangle)/\sqrt{2}$, the coefficients are $1/\sqrt{2}$ each, so $P(x{+}) = P(x{-}) = 1/2$. That is Eq. 6.2.
3. **The "paradox".** After the $\hat{S}_x$ box the state is $\lvert\psi_x^{\pm}\rangle$, which is itself an equal superposition in the $z$ basis. So a final $\hat{S}_z$ box gives $+$ or $-$ with probability 1/2 each, even though the very first box had fixed $S_z=+$. Nothing is "disturbed" mysteriously: the state after each measurement is simply the eigenstate for the *latest* result, and eigenstates of different spin components are different states.
4. **No simultaneous definite values.** $\lvert{\uparrow}\rangle$ is not an eigenstate of $\hat{S}_x$ (see $\sigma_x\lvert{\uparrow}\rangle = \lvert{\downarrow}\rangle$ in the decoder), so "$S_z=+$ and $S_x=+$ together" has no meaning. The lecture puts it as: a definite $S_z$ makes sense only when the only later operations are $\hat{S}_z$ measurements.
5. **General angle** (Eq. 6.3). For two magnet directions at angle $\theta$, $P(n{+}\mid m{+}) = (1+\cos\theta)/2$. Check: $\theta = 0$ gives 1 (same magnet), $\theta = 90^\circ$ gives $1/2$ (the $z$ then $x$ case), $\theta = 180^\circ$ gives 0.

### Interference (lecture 6.4), in one paragraph of logic

Path A is "went via $S_x = +$", path B is "went via $S_x = -$". If the two paths are recombined and nobody records which was taken, you **add amplitudes** for the final outcome before squaring ([Move 5.1](../day05.md), amplitude version); if the path is recorded, you **add probabilities**. Exercise 3 below does this sum for a simple case.

## Moves used this week

- **[Move 3.1](../day03.md)** — operators as matrices acting on kets: [Day 3](../day03.md). Used for $\hat{S}_x\lvert{\uparrow}\rangle$.
- **[Move 3.4](../day03.md)** — Pauli matrices, spin-up/down and the $\pm x$ states: [Day 3](../day03.md).
- **[Move 5.1](../day05.md)** — expansion in an eigenbasis, probabilities $|c_n|^2$ summing to 1: Day 5.
- **[Move 2.1](../day02.md)** — dot product (for $\mathbf{m}\cdot\mathbf{n}$ in Eq. 6.3): Day 2.
- **[Move 7.5](../day07.md)** — what entanglement does and does not imply (the lecture only mentions entanglement in its introduction): [Day 7](../day07.md).

## Worked clones

Three short spin-½ exercises. Convention used: $\hat{S}_i = \tfrac{\hbar}{2}\sigma_i$; $\lvert\psi_x^{\pm}\rangle = (\lvert{\uparrow}\rangle \pm \lvert{\downarrow}\rangle)/\sqrt{2}$. A beam of unpolarised atoms means each atom passes the first $\hat{S}_z$ box in either beam with probability 1/2. None of these reproduce a course problem (Week 6 has no portfolio calculation; these are practice for the lecture's Eqs. 6.1 to 6.4).

1. A beam is prepared in $S_z = +$. It then enters a Stern-Gerlach box whose field points along a direction $\mathbf{n}$ lying in the $xz$-plane at $60^\circ$ to the $z$-axis. Find the probabilities of $S_n = +$ and $S_n = -$. Then take only the atoms that emerged $S_n = -$ and send them into an $\hat{S}_z$ box: what is the probability of $S_z = +$? — **Hint:** Use Eq. 6.3 for the first part, with $\mathbf{m}$ along $z$. For the second part the "prepared" state is now $\lvert\psi_n^-\rangle$, so use Eq. 6.4 with the roles of the two directions swapped. Only the angle matters, and $\cos 60^\circ = 1/2$. — **Solution sketch:** $\mathbf{m}\cdot\mathbf{n} = \cos 60^\circ = 1/2$. Eq. 6.3: $P(n{+}) = (1+\tfrac12)/2 = 3/4$ and $P(n{-}) = (1-\tfrac12)/2 = 1/4$; they sum to 1. For the second part the prepared state is $\lvert\psi_n^-\rangle$ and the new box points along $z$, with $\mathbf{n}\cdot\mathbf{z} = 1/2$ again. Eq. 6.4 gives $P(z{+}) = (1 - \tfrac12)/2 = 1/4$. Sanity check: an $n{-}$ atom is "mostly $z{-}$" because $n{+}$ was "mostly $z{+}$" (3/4), so $z{+}$ being the minority (1/4) is plausible.

2. Three boxes in series, $\hat{S}_z\to\hat{S}_x\to\hat{S}_z$ (the lecture's Figure 6.4 layout, a beam of unpolarised atoms in). Only the $S_z=+$ beam leaves the first box, only the $S_x=+$ beam leaves the second, and the third box gives $S_z=+$ or $S_z=-$. (a) What fraction of the atoms entering the first box leave the final box in the $S_z = -$ beam? (b) Remove the middle box and repeat: what is the fraction now? (c) Write the whole sequence as an operator product acting on $\lvert\psi\rangle$ and say which operator acts first. — **Hint:** Multiply probabilities along the path, one factor per box: 1/2 for the unpolarised first box, then the Eq. 6.2 value, then the Eq. 6.2 value again. For (b) use Eq. 6.1. — **Solution sketch:** (a) $\tfrac12\cdot\tfrac12\cdot\tfrac12 = 1/8$: first box passes $z{+}$ with probability 1/2; $x{+}$ from $z{+}$ has probability 1/2; $z{-}$ from $x{+}$ has probability $\lvert\langle\psi_z^-\mid\psi_x^+\rangle\rvert^2 = \lvert 1/\sqrt2\rvert^2 = 1/2$. (b) With no middle box the atom is in $\lvert{\uparrow}\rangle$ and Eq. 6.1 gives $P(z{-}) = 0$, so the fraction is $\tfrac12\cdot 0 = 0$. Inserting the $x$-box makes an "impossible" outcome happen 1/8 of the time. (c) $\hat{S}_z\hat{S}_x\hat{S}_z\lvert\psi\rangle$: the right-most $\hat{S}_z$ acts first, as the lecture stresses.

3. Interference check. Atoms prepared in $S_z=+$ go through an $\hat{S}_x$ splitter and a recombiner (Figure 6.7), then a final $\hat{S}_z$ box. (a) If the path is not observed, add the two path amplitudes for the outcome $S_z=-$ and square: what is $P(z{-})$? (b) If the path is observed, what is $P(z{-})$? Use $\langle\psi_z^-\mid\psi_x^{\pm}\rangle = \pm 1/\sqrt{2}$ and $\langle\psi_x^{\pm}\mid\psi_z^+\rangle = 1/\sqrt{2}$. — **Hint:** The amplitude via path $\pm$ is the product $\langle\psi_z^-\mid\psi_x^{\pm}\rangle\langle\psi_x^{\pm}\mid\psi_z^+\rangle$. Unobserved: add the two amplitudes, then take the modulus squared. Observed: square each path's amplitude first, then add. — **Solution sketch:** Path amplitudes: via $x{+}$: $(1/\sqrt2)(1/\sqrt2) = 1/2$; via $x{-}$: $(-1/\sqrt2)(1/\sqrt2) = -1/2$. (a) Sum $= 0$, so $P(z{-}) = 0$: the same as with no splitter at all (lecture 6.4, Eq. 6.1). (b) $\lvert 1/2\rvert^2 + \lvert -1/2\rvert^2 = 1/4 + 1/4 = 1/2$, the value in Eq. 6.2. The cross-term that cancelled in (a) is the interference.

   *Note on the sign convention.* Eq. 6.2 lists $1/\sqrt2$ for these overlaps: it is a table of magnitudes. The sign (phase) is a convention, and I use the standard one, $\lvert\psi_x^{\pm}\rangle=(\lvert{\uparrow}\rangle\pm\lvert{\downarrow}\rangle)/\sqrt2$, which gives $\langle\psi_z^-\mid\psi_x^-\rangle=-1/\sqrt2$. The interference result depends on the *relative* sign of the two path amplitudes. With an all-plus table the amplitudes would be $+\tfrac12$ via $x{+}$ and $+\tfrac12$ via $x{-}$; the unobserved sum would be $1$ and $P(z{-})=1$, rather than cancelling to 0. That contradicts Eq. 6.1 (no splitter gives $P(z{-})=0$) and shows the all-plus table is not a consistent set of orthonormal states ($\lvert\psi_x^+\rangle$ and $\lvert\psi_x^-\rangle$ must be orthogonal). The observed case is unaffected: $\tfrac14+\tfrac14=\tfrac12$ under either convention, because squaring removes the sign.

## Portfolio essay guide (method only)

**This is a structure, not text to submit.** It contains no paragraphs of the essay and no argument you can lift. It is a planning frame. The Apply task asks *you* to identify what you consider the most important results and implications; your ranking and reasons are the assessed content. Your own words and your own judgement are what earn marks, and the university's assessment rules apply. Nothing here has been checked against the portfolio brief, which is not in the local exports: follow the official brief for the required structure, weighting, word limit and referencing style, and if it differs from this companion, the brief wins.

### The prompt, taken apart (from the Week 6 Apply task)

The task names three things to consider: the discovery of **quantised spin states**, the **violation of classical physics principles**, and the **development of quantum mechanics**. It then asks you to **identify what you consider most important**. So the essay is not a summary of the experiment: it must *choose and justify*.

### Questions your plan must answer (you write the answers)

1. What was expected classically, what was observed, and what is the single feature of the data that rules the classical picture out?
2. What exactly is quantised, and how do you know it is a property of the atom and not of the apparatus?
3. Which classical principles are violated, or assumed and found wanting (for example, that a property has a definite value regardless of what else is measured; lecture 6.3 speaks to this)?
4. What do the sequential experiments add beyond the first observation (preparation and measurement in one device; incompatible measurements; interference)?
5. Which result or implication matters *most*, by what criterion (conceptual, historical, technological), and what would you rank below it?
6. How did the experiment feed later quantum mechanics and technology (the lecture's introduction lists spin, entanglement and quantum information technologies)? What evidence supports each link?

### Evidence types to gather

| Type | What it can support | Where to look |
|---|---|---|
| Original result | What was observed and when | The Stern-Gerlach source cited in the lecture (Bauer, arXiv 2301.11343, listed in the introduction references of the Week 6 content file, not in the Explore task) |
| Theory / derivation | Force law, $\boldsymbol{\mu}\propto\mathbf{S}$, probabilities, Eqs. 6.1 to 6.4 | Week 6 lecture (this is course material: cite it as such) |
| Conceptual discussion | The interpretation of spin, why the "little arrow" is misleading | The Explore videos named in the Week 6 content file; the Susskind and Collins files in `exteral_resources/`, which **this companion has not summarised**: read them yourself before using them |
| Later applications | Development of quantum mechanics and technology | Sources you have read and can cite precisely |
| Your own reasoning | Ranking and justification | Your notes from Exercises 1 to 3 (a probability calculation can serve as a short piece of evidence, in your own working) |

### Paragraph-by-paragraph outline with word budgets

This assumes the Stern-Gerlach discussion is one part of the 2100-word portfolio and takes about 450 words. If the brief allots a different amount, scale every line proportionally.

| Block | Purpose (a question to answer, not a sentence to copy) | Suggested words |
|---|---|---|
| 1. Framing | State the question and the ranking criterion you will use | 50 |
| 2. The observation | Expected versus observed; what "two beams" establishes | 120 |
| 3. Classical principles challenged | Which assumptions fail, with a specific piece of evidence | 100 |
| 4. Sequential and interference results | What repeated and mixed measurements show; link to the double slit | 100 |
| 5. Implications and ranking | Downstream impact; your most important result and why the others rank below it | 60 |
| 6. Close | One-sentence position; check that it answers the task as worded | 20 |
| **Total** | | **450** |

Adjust the split to your argument (for example, a case built on interference needs more in block 4 and less in block 2). Keep an eye on total length across the whole portfolio; the 2100 limit is the university's, so confirm what counts toward it in the brief.

### Citation and integrity checklist

- [ ] Every source you cite is one you have **read** (not merely seen listed).
- [ ] Each factual claim (date, apparatus, implication) has a source, using the referencing style required by the brief.
- [ ] Course lecture material is cited as course material, and the lecture's own cited sources (Bauer; Cresser lecture notes) are not cited *as if read* unless you read them.
- [ ] Quotations are in quote marks with page or section; otherwise paraphrase in your own words.
- [ ] Your ranking of "most important" is your own and is argued, not asserted.
- [ ] Any equations or numbers you use are checked (probabilities within [0, 1], sums to 1).
- [ ] You have followed the module's rules on collaboration and on generative-AI use. This companion is a study aid, not a source for the essay.
- [ ] Similarity-check expectations: supplied notation and figure captions may raise a matching score harmlessly; copied prose will not.
- [ ] Word count includes/excludes what the brief says it does.

## Retrieval questions

Answer closed-book first. Each names the misconception it traps. The themes follow the eight Week 6 quiz questions; the wording here is my own, so use these for practice and check them against the lecture.

1. What did the Stern-Gerlach experiment show about the values a spin component can take? (Trap: "spin can take any value between up and down", the classical continuous picture.) — **Hint:** Compare the classical expected screen pattern with the observed one (lecture 6.1). — **Solution sketch:** Two discrete spots, not a continuous band, so the spin component takes only specific discrete values (two for silver atoms).

2. What kind of magnetic field does the experiment need, and why does a uniform field not work? (Trap: thinking any strong field will split the beam.) — **Hint:** Look at the force law $F = \langle\mu_z\rangle\,\mathrm{d}B_z/\mathrm{d}z$. — **Solution sketch:** An inhomogeneous field. The force is proportional to the field *gradient*, which is zero in a uniform field, so no net deflection and no splitting.

3. Which property of the particle is being probed, and how does it connect to the magnetic dipole? (Trap: assuming it measures mass, charge or velocity.) — **Hint:** See $\boldsymbol{\mu} = \frac{gq}{2m}\mathbf{S}$. — **Solution sketch:** Spin (intrinsic angular momentum). The magnetic moment is proportional to spin, so measuring the deflection measures the spin component along the field.

4. For a single silver atom, can it emerge in both beams at once? What do you see after many atoms? (Trap: "deflection either up or down or both" read as one atom being in two places; check the wording of the lecture.) — **Hint:** The lecture says "either (but not simultaneously both)"; note that in the lecture that sentence is about a single atom after the $\hat S_x$ box (section 6.3), not about the basic experiment. — **Solution sketch:** No: each atom is detected in one beam. Many atoms build up both spots. Note that the Week 6 quiz's keyed answer for the deflection question reads "up, down or both", which looks at odds with this sentence of the lecture if "both" means "both for one atom". Follow the lecture in your own work, and raise it with your tutor if you want it clarified.

5. What is the meaning of "spin values are limited to discrete values" for the possible results of $\hat{S}_z$? (Trap: "any arbitrary integer" or "any positive value".) — **Hint:** Think of the eigenvalues of $\hat{S}_z = \tfrac{\hbar}{2}\sigma_z$ (Day 3). — **Solution sketch:** A measurement can only return an eigenvalue of the operator; for $\hat{S}_z$ on a spin-½ particle these are $+\hbar/2$ and $-\hbar/2$. Not a range, not arbitrary, and not only positive.

6. Two $\hat{S}_z$ boxes in a row, upper beam of the first into the second: what emerges, and how does this depend on the initial state? (Trap: expecting the second box to re-randomise the result, or expecting the answer to depend on the initial state.) — **Hint:** Eq. 6.1 and the collapse rule ([Move 5.3](../day05.md)). — **Solution sketch:** The same outcome, with certainty, whatever the initial state. After the first measurement the state is $\lvert{\uparrow}\rangle$, and measuring $S_z$ again gives $+$ with probability $|\langle{\uparrow}\mid{\uparrow}\rangle|^2 = 1$.

7. Name the areas the lecture introduction says the experiment's insights reach. (Trap: treating the experiment as only a historical curiosity.) — **Hint:** Reread the Introduction of the lecture. — **Solution sketch:** Electron spin, the behaviour of atoms and subatomic particles, quantum entanglement, and quantum information technologies. In your portfolio, support any such link with sources you have read, not the lecture's general statement alone. Note that the quiz key for the matching question lists "Optics and photonics", which the lecture does not support; ask your tutor about it rather than relying on it.

8. After an $\hat{S}_z$ box gives $+$, an $\hat{S}_x$ box gives $+$, and a final $\hat{S}_z$ box is applied: what are the probabilities, and which phenomenon does an unobserved split-and-recombine version illustrate? (Trap: believing the first $S_z$ result is preserved, or that measuring never changes anything.) — **Hint:** Use Eq. 6.2 for the last box; for the phenomenon, see lecture 6.4. — **Solution sketch:** Final box gives $S_z = +$ or $S_z = -$ with probability 1/2 each, because the state after the $x$ box is the $\lvert\psi_x^+\rangle$ superposition of $\lvert{\uparrow}\rangle$ and $\lvert{\downarrow}\rangle$. The unobserved split-and-recombine version is described in the lecture in terms of interference; the state is a superposition of the two $x$ paths. Observing the path removes the interference. (The quiz's answer options name "interference" and "superposition" separately: be ready to explain how the two ideas connect.)

## Six-steps write-up template

The course's own "six steps" page is not in the local exports; this uses the stand-in in [STRATEGY](../../STRATEGY.md). Applied to a sequential-measurement probability question:

1. **Restate:** what probability is asked for, and what is given (which boxes, which beams selected, what the initial beam is).
2. **State in notation:** draw the boxes left to right and label each beam; write the prepared state as $\lvert{\uparrow}\rangle$ or $\lvert\psi_m^{\pm}\rangle$.
3. **Name the principle:** collapse after each measurement ([Move 5.3](../day05.md)); probability $=\lvert\text{amplitude}\rvert^2$ ([Move 5.1](../day05.md)); Eqs. 6.1 to 6.4 for the values.
4. **Do the algebra:** one probability per box, multiplied along the path; or add amplitudes if the path is unobserved.
5. **Check:** every probability in [0, 1]; the probabilities at each box sum to 1; the limits ($\theta = 0$ gives 1, $\theta = 90^\circ$ gives 1/2, $\theta = 180^\circ$ gives 0).
6. **State the answer** in a full sentence, including which beams were selected.

*For the portfolio essay, the six steps do not apply as written. Use the planning skeleton above and the brief's own structure.*
