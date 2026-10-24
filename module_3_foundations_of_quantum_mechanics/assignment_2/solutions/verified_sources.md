# Verified sources: Stern–Gerlach essay (Module 3, Assignment 2)

Compiled 24 Oct 2026. Every bibliographic record below (authors, title, journal, volume, issue, pages or article number, year) was checked against the Crossref API (`https://api.crossref.org/works/<DOI>`). Claims come from the abstract or full text, opened through arXiv, Crossref, Semantic Scholar, PubMed or the publisher. The numbers here are working labels. In the essay, renumber the sources in order of first citation (APS numerical style).

Already in hand and not re-verified: Gerlach & Stern, Z. Phys. 9, 349 (1922); Bauer's translation, arXiv:2301.11343; Schmidt-Böcking et al., Eur. Phys. J. H 41, 327 (2016); course lecture notes.

---

## A. History and foundations

**[1]** B. Friedrich and D. Herschbach, Stern and Gerlach: How a bad cigar helped reorient atomic physics, Phys. Today **56**(12), 53 (2003). DOI: 10.1063/1.1650229
- *Verified:* Crossref (pp. 53–59, Dec 2003). Full text read from the PDF at courses.physics.ucsd.edu/2013/Fall/physics130b/stern_gerlach.pdf.
- Apparatus numbers: silver oven at 1000 °C, collimating slits 0.03 mm wide, magnet 3.5 cm long, field about 0.1 T, gradient about 10 T/cm. The beam split by "only 0.2 mm", so a misalignment of more than 0.01 mm could spoil a run. The deposit was roughly a monolayer (~10^16 atoms/cm^2) and was invisible until sulfur from the cigar smoke turned it into jet-black silver sulfide.
- "Descendants" of the experiment and its idea of "sorting quantum states via space quantization" include the prototypes for NMR, optical pumping, the laser and atomic clocks, as well as the Lamb shift and the electron's anomalous magnetic moment.
- Historical subtlety: the agreement with Bohr's theory was a "lucky coincidence". Silver's orbital angular momentum is zero and the splitting comes from spin, but nobody attributed it to spin until Fraser in 1927.

**[2]** J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge University Press, Cambridge, 2020). DOI: 10.1017/9781108587280
- *Verified:* Crossref record, plus the CUP front-matter PDF (assets.cambridge.org/97811084/73224/frontmatter/9781108473224_frontmatter.pdf), contents page.
- Chapter 1 ("Fundamental Concepts") opens with §1.1 "The Stern–Gerlach Experiment", which contains §1.1.2 "Sequential Stern–Gerlach Experiments" and §1.1.3 "Analogy with Polarization of Light". You can cite this as the textbook paradigm of measurement and as the source for the SG ↔ polarising-beam-splitter analogy used in the communication section.

## B. Spin qubits and quantum computing

**[3]** D. Loss and D. P. DiVincenzo, Quantum computation with quantum dots, Phys. Rev. A **57**, 120 (1998). DOI: 10.1103/PhysRevA.57.120
- *Verified:* Crossref (pp. 120–126); abstract from arXiv:cond-mat/9701055.
- Proposes a universal set of one- and two-qubit gates "using the spin states of coupled single-electron quantum dots", with gates controlled by tuning the tunnelling barrier between neighbouring dots.
- Gate quality is computed from a spin master equation that includes decoherence from a magnetic environment.

**[4]** G. Burkard, T. D. Ladd, A. Pan, J. M. Nichol, and J. R. Petta, Semiconductor spin qubits, Rev. Mod. Phys. **95**, 025003 (2023). DOI: 10.1103/RevModPhys.95.025003
- *Verified:* Crossref; abstract from arXiv:2112.08863.
- The spin is "a natural two-level system that is insensitive to electric fields, leading to long quantum coherence times".
- Reviews progress from GaAs dots to Si and Ge qubits, "scaling to larger system sizes", the present fidelity limits, and the effect of noise analysed with the filter-function formalism (useful for the noise section).

**[5]** J. M. Elzerman, R. Hanson, L. H. Willems van Beveren, B. Witkamp, L. M. K. Vandersypen, and L. P. Kouwenhoven, Single-shot read-out of an individual electron spin in a quantum dot, Nature **430**, 431 (2004). DOI: 10.1038/nature02693
- *Verified:* Crossref (pp. 431–435); abstract from arXiv:cond-mat/0411232 and Semantic Scholar.
- A spin measured along the field "can have only two outcomes: parallel or anti-parallel". This is the SG two-outcome result, achieved here electrically.
- Uses spin-to-charge conversion read out by a quantum point contact. Spin-measurement visibility is **~65%**, and T1 is **up to ~0.85 ms at 8 T**.

**[6]** C. D. Bruzewicz, J. Chiaverini, R. McConnell, and J. M. Sage, Trapped-ion quantum computing: Progress and challenges, Appl. Phys. Rev. **6**, 021314 (2019). DOI: 10.1063/1.5088164
- *Verified:* Crossref (the abstract is in the record) and arXiv:1904.04178.
- "The basic requirements for universal QC have all been demonstrated with ions." Reviews ions' "strengths and limitations as qubits" and what is needed "to increase the scale … while mitigating decoherence and control errors".

**[7]** A. H. Myerson, D. J. Szwer, S. C. Webster, D. T. C. Allcock, M. J. Curtis, G. Imreh, J. A. Sherman, D. N. Stacey, A. M. Steane, and D. M. Lucas, High-fidelity readout of trapped-ion qubits, Phys. Rev. Lett. **100**, 200502 (2008). DOI: 10.1103/PhysRevLett.100.200502
- *Verified:* Crossref (all 10 authors match). Abstract from arXiv:0802.1684.
- Single-shot readout of 40Ca+ by state-dependent fluorescence reaches **99.991(1)%** average fidelity over one million trials. Adaptive detection reaches 99.99% in **145 µs**. The 43Ca+ hyperfine qubit reaches 99.77(3)%.
- Fidelity is "sufficient for fault-tolerant quantum computation".

**[8]** X. Xue, M. Russ, N. Samkharadze, B. Undseth, A. Sammak, G. Scappucci, and L. M. K. Vandersypen, Quantum logic with spin qubits crossing the surface code threshold, Nature **601**, 343 (2022). DOI: 10.1038/s41586-021-04273-w
- *Verified:* Crossref (7 authors; the abstract is in the record).
- A silicon spin processor with single- and two-qubit gate fidelities **all above 99.5%** (gate-set tomography), above the **~1% surface-code error threshold**. A variational quantum eigensolver was run on it.
- Spin qubits "can leverage advanced semiconductor technology" for scaling.

**[9]** S. G. J. Philips *et al.*, Universal control of a six-qubit quantum processor in silicon, Nature **609**, 919 (2022). DOI: 10.1038/s41586-022-05117-x
- *Verified:* Crossref (15 authors, pp. 919–924; the abstract is in the record) and arXiv:2202.09252.
- "The requirements of having a large qubit count and operating with high fidelity are typically conflicting." Earlier demonstrations used 1–4 qubits, and this one uses **six**.
- State preparation uses initialisation by measurement with real-time feedback and quantum-non-demolition measurement, which is SG-type projective readout used as a resource.

## C. Quantum sensing

**[10]** C. L. Degen, F. Reinhard, and P. Cappellaro, Quantum sensing, Rev. Mod. Phys. **89**, 035002 (2017). DOI: 10.1103/RevModPhys.89.035002
- *Verified:* Crossref; abstract from arXiv:1611.02427.
- Defines quantum sensing as "the use of a quantum system, quantum properties or quantum phenomena to perform a measurement of a physical quantity". The most common platforms are "spin qubits, trapped ions and flux qubits".

**[11]** L. Rondin, J.-P. Tetienne, T. Hingant, J.-F. Roch, P. Maletinsky, and V. Jacques, Magnetometry with nitrogen-vacancy defects in diamond, Rep. Prog. Phys. **77**, 056503 (2014). DOI: 10.1088/0034-4885/77/5/056503
- *Verified:* Crossref; abstract from arXiv:1311.5214.
- The NV electron spin enables "magnetic imaging with nanometric resolution and field detection capabilities in the nanotesla range", thanks to its atomic size and "exceptionally long spin-coherence times". Applications are in nanomagnetism, mesoscopic physics and the life sciences.

**[12]** J. F. Barry, J. M. Schloss, E. Bauch, M. J. Turner, C. A. Hart, L. M. Pham, and R. L. Walsworth, Sensitivity optimization for NV-diamond magnetometry, Rev. Mod. Phys. **92**, 015004 (2020). DOI: 10.1103/RevModPhys.92.015004
- *Verified:* Crossref; abstract from arXiv:1903.08176 and Semantic Scholar.
- Limitation: present NV-ensemble devices "exhibit sensitivities orders of magnitude away from theoretical limits".
- The most promising routes to improvement are the spin dephasing time, the readout fidelity and the properties of the host diamond.

**[13]** G. Balasubramanian *et al.*, Ultralong spin coherence time in isotopically engineered diamond, Nat. Mater. **8**, 383 (2009). DOI: 10.1038/nmat2420
- *Verified:* Crossref (14 authors, pp. 383–387); abstract from PubMed (PMID 19349970).
- In 13C-depleted (0.3%) CVD diamond, single NV electron spins show **T2 = 1.8 ms at room temperature**, "the longest room-temperature spin dephasing times ever observed in solid-state systems".
- Magnetic-field sensitivity reaches **4 nT Hz^-1/2** with sub-nanometre spatial resolution. Lesson: materials engineering (removing the nuclear-spin bath) is how noise is controlled.

**[14]** Y. Margalit, O. Dobkowski, Z. Zhou, O. Amit, Y. Japha, S. Moukouri, D. Rohrlich, A. Mazumdar, S. Bose, C. Henkel, and R. Folman, Realization of a complete Stern-Gerlach interferometer: Toward a test of quantum gravity, Sci. Adv. **7**, eabg2879 (2021). DOI: 10.1126/sciadv.abg2879
- *Verified:* Crossref (all 11 authors match). Abstract from arXiv:1801.02708.
- Until this work there was "little evidence" that SG with free atoms and macroscopic magnets is a fully coherent process, and numerous theoretical studies called a full-loop interferometer "a near impossible endeavor".
- They demonstrate a high-visibility spatial SG interference pattern and a full-loop SG interferometer, using precise magnetic fields from an **atom chip**. They also observe "the gradual emergence of time-irreversibility as the splitting is increased".
- Proposed applications: large-momentum-transfer beam splitting for atom-interferometric metrology, probing electron transport down to shot noise, NMR, and tests of quantum gravity.

**[15]** O. Amit, Y. Margalit, O. Dobkowski, Z. Zhou, Y. Japha, M. Zimmermann, M. A. Efremov, F. A. Narducci, E. M. Rasel, W. P. Schleich, and R. Folman, T^3 Stern-Gerlach matter-wave interferometer, Phys. Rev. Lett. **123**, 083601 (2019). DOI: 10.1103/PhysRevLett.123.083601
- *Verified:* Crossref (all 11 authors match). Abstract from arXiv:1908.03879.
- The interferometer phase scales with the **cube of the interrogation time (T^3)**, and four magnetic-gradient pulses create the state-dependent force.
- It uses "no light", so it "can therefore serve as a high-precision surface probe at very close distances".

**[16]** S. Bose, A. Mazumdar, G. W. Morley, H. Ulbricht, M. Toroš, M. Paternostro, A. A. Geraci, P. F. Barker, M. S. Kim, and G. Milburn, Spin entanglement witness for quantum gravity, Phys. Rev. Lett. **119**, 240401 (2017). DOI: 10.1103/PhysRevLett.119.240401
- *Verified:* Crossref (all 10 authors match). Abstract from arXiv:1707.06050.
- Two **micron-size** test masses, each with an embedded spin, are placed in adjacent matter-wave (SG) interferometers. Gravity-induced phase evolution could entangle them "even when they are placed far apart enough to keep Casimir–Polder forces at bay". Spin-correlation measurements would then witness gravity as a quantum coherent mediator. This is a future-advancement example.

## D. Quantum communication

**[17]** B. Hensen *et al.*, Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres, Nature **526**, 682 (2015). DOI: 10.1038/nature15759
- *Verified:* Crossref (19 authors, pp. 682–686); abstract from arXiv:1508.05949.
- Event-ready entanglement of NV electron spins **1.3 km** apart. Efficient spin readout closes the detection loophole.
- **245 trials** gave **S = 2.42 ± 0.20** (the CHSH bound is 2), with **p = 0.039**. The result supports device-independent quantum-secure communication and randomness certification.
- Critical point: the trial count is small (245), which shows how slow remote entanglement generation is.

**[18]** M. Pompili, S. L. N. Hermans, S. Baier, H. K. C. Beukers, P. C. Humphreys, R. N. Schouten, R. F. L. Vermeulen, M. J. Tiggelman, L. dos Santos Martins, B. Dirkse, S. Wehner, and R. Hanson, Realization of a multinode quantum network of remote solid-state qubits, Science **372**, 259 (2021). DOI: 10.1126/science.abg1919
- *Verified:* Crossref (all 12 authors match, pp. 259–264). Editor's summary in Crossref; abstract from arXiv:2102.04471.
- A **three-node** network of NV-centre spin qubits connected by photons. Each node has a memory qubit. It demonstrated multipartite entanglement distribution and entanglement swapping through an intermediate node, without post-selection.

**[19]** S. Wehner, D. Elkouss, and R. Hanson, Quantum internet: A vision for the road ahead, Science **362**, eaam9288 (2018). DOI: 10.1126/science.aam9288
- *Verified:* Crossref (editor's summary in the record).
- Proposes "stages of development that each correspond to increasingly powerful applications". A full quantum internet "is still some ways away", but "the first long-range quantum networks are already being planned".

## E. Noise, coherence and fundamental limits

**[20]** B.-G. Englert, J. Schwinger, and M. O. Scully, Is spin coherence like Humpty-Dumpty? I. Simplified treatment, Found. Phys. **18**, 1045 (1988). DOI: 10.1007/BF01909939
- *Verified:* Crossref (issue 10, pp. 1045–1056); abstract read on link.springer.com.
- Recombining the two partial SG beams to recover the original spin state is the Humpty-Dumpty problem. A substantial loss of spin coherence "always occurs" unless the field inhomogeneity is controlled to about **one part in 10^5**. This is the key limitation that [14] eventually overcame with atom-chip fields.

**[21]** B. M. Garraway and S. Stenholm, Does a flying electron spin?, Contemp. Phys. **43**, 147 (2002). DOI: 10.1080/00107510110102119
- *Verified:* Crossref (issue 3, pp. 147–160); abstract from Semantic Scholar. **Note:** the title is "Does a flying electron spin?", not "Is the Stern-Gerlach experiment with electrons possible?".
- In the late 1920s Bohr argued that the magnetic moment of a free electron could not be observed, and that quantum effects would wash out the separated classical trajectories in an SG-type experiment. The review concludes that quantum effects "do not overwhelm the magnetic effects of spin", and that "no principle seems to prevent the observation of the magnetic moment of the free electron". The electron g-factor has instead been measured precisely in traps.

**[22]** H. Batelaan, T. J. Gay, and J. J. Schwendiman, Stern-Gerlach effect for electron beams, Phys. Rev. Lett. **79**, 4517 (1997). DOI: 10.1103/PhysRevLett.79.4517
- *Verified:* Crossref (issue 23, pp. 4517–4521); abstract read on journals.aps.org.
- Contrary to the Bohr–Pauli analysis, a modified SG-type device using classical trajectories could still produce strong spin separation of an electron beam. The required fields are within reach of a tabletop electron spin filter.

## F. Optional extra (verified)

**[23]** M. Keil, O. Amit, S. Zhou, D. Groswasser, Y. Japha, and R. Folman, Fifteen years of cold matter on the atom chip: promise, realizations, and prospects, J. Mod. Opt. **63**, 1840 (2016). DOI: 10.1080/09500340.2016.1178820
- *Verified:* Crossref (issue 18, pp. 1840–1885); abstract from arXiv:1605.04939.
- Atom chips produce "BECs at a rate of several per second" and enable matter-wave interferometry and "novel probing of surfaces and new forces". Technological applications are "intensively pursued". This supports the claim that atom chips offer a scalable, chip-based platform for SG interferometry.

---

## Online resource: only partly verified (check in a browser before citing)

- The Nobel Prize, *The Nobel Prize in Physics 1943*, https://www.nobelprize.org/prizes/physics/1943/summary/. Every nobelprize.org URL returned HTTP 403 to my fetches, so I could not open the page. The search engine's index of nobelprize.org gives the motivation: Otto Stern "for his contribution to the development of the molecular ray method and his discovery of the magnetic moment of the proton". The prize was reserved and awarded in 1944. Open the page yourself, then add it as an online source with "(accessed <date>)".
- Fallback online source that is verified: [1] is freely readable at the UCSD course URL above, and Physics Today is a magazine (physicstoday.aip.org), so it can serve as the "online resource" if needed.

## Not included / could not verify
- Intel/Diraq qubit-count press claims (e.g. 12-qubit "Tunnel Falls"): not checked, so do not cite. Use [9] (six qubits, peer-reviewed) as the scalability example.
- A dedicated research paper on SG ↔ polarising-beam-splitter analogy: not searched further. [2] §1.1.3 covers the analogy.

---

## Critical-analysis seeds

1. **Strength: projective two-outcome readout is the workhorse of every spin technology.** The 1922 two-spot result [1] reappears as electrical single-shot spin readout (~65% visibility in 2004) [5], ion fluorescence readout at 99.991% [7], and measurement-based initialisation in a six-qubit silicon processor [9]. *Limitation:* readout fidelity depends strongly on the platform (65% vs 99.99%), so "SG-type measurement" is not one solved technology.
2. **Limitation: recombining SG beams coherently is extremely demanding.** Coherence is lost unless field inhomogeneity is controlled to ~1 part in 10^5 [20]. Only atom-chip fields achieved a full-loop SG interferometer [14], and coherence still degrades as the splitting grows (time-irreversibility). *Opportunity:* T^3 phase scaling [15] and light-free operation for surface probing.
3. **Strength vs scalability (computing).** Silicon spin qubits now exceed 99.5% fidelity, above the ~1% surface-code threshold [8], and can use CMOS fabrication [4,8]. *Limitation:* qubit count and fidelity "are typically conflicting" [9]. Peer-reviewed devices are still only a handful of qubits, while ions show all the ingredients but face scale-up and control-error challenges [6].
4. **Sensing: excellent coherence, but noise-limited in practice.** Isotopic purification gives T2 = 1.8 ms and 4 nT Hz^-1/2 at room temperature [13], with nanoscale imaging [11]. *Limitation:* ensemble NV magnetometers remain "orders of magnitude" from theoretical limits [12]. Dephasing time and readout fidelity are the bottlenecks, which links back to seed 1.
5. **Communication: landmark but slow.** NV spins 1.3 km apart violated the Bell inequality loophole-free (S = 2.42 ± 0.20) [17], and a three-node network now distributes and swaps entanglement [18]. *Limitation:* only 245 trials [17] and three nodes [18], against the multi-stage roadmap in [19]. Rates and node count are the scalability problem.
6. **Fundamental scope: which particles can be "SG-ed"?** Bohr and Pauli argued that free electrons cannot show SG splitting. Later analyses [21,22] find no principle forbidding it, but in practice electron spin is read indirectly (spin-to-charge conversion [5], Penning traps [21]). This illustrates the move from literal SG deflection to SG-*equivalent* state-dependent measurement. Future frontier: SG interferometry with micron-scale masses to test quantum gravity [16].
