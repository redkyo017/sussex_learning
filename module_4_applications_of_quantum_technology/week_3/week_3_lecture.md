## Week 3: Quantum sensors part 2: Inertial forces: Study

## 3: Quantum sensors part 2: Inertial forces

## Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

Complementary to last week's topic, this week we will cover another class of quantum sensors: those based on atom interferometry. We will also look at their applications, including inertial sensing.

Since the first proof-of-principle experiments in 1991 [\[1\]](#sect5), atom interferometry has developed rapidly and matured to a versatile tool to measure inertial forces with ultra-high precision. It is used for fundamental research in particle physics, general relativity and cosmology. At the same time, it has also been applied in areas of metrology, geophysics, civil engineering, oil and minerals exploration, navigation, and space [\[2\]](#sect6).

 This Study section will guide you through atom interferometry from the key concepts to the most advanced applications. The Study topics this week are: 

-   [3.1 Concept of atom interferometry](#sect1)
-   [3.2 Advantage of using atoms for inertial sensing](#sect2)
-   [3.3 The future of atom interferometry](#sect3)
-   [3.4 Applications of atom interferometry](#sect4)

## 3.1 Concept of atom interferometry

It has been well known for centuries that light can produce interference phenomena [\[3\]](#sect7). Similarly, matter, such as atoms, exhibits wave-like properties. Matter waves, unlike light, are massive and bear gravitational signals in their interference patterns. To understand atom interferometry, and see how it can measure, for example, gravity, the best way is to first understand optical interferometry.

**Optical interferometry**

In optical interferometry, such as the widely used Mach-Zehnder interferometer [\[3\]](#sect7) (shown in Figure [3.1](#fig:opt-interferometry)), light waves are split, and recombined after propagating along separate paths. Depending on the difference in the phase accumulated along the two paths, the light may interfere constructively (appear bright) or destructively (appear dark) at the detector. In a simple description, the electromagnetic field $E_0 \sin(\omega t)$ in one arm of the interferometer gains a phase shift $\varphi=\Delta n kL$ as $E_0 \sin(\omega t + \varphi)$ and the two are superposed on the detector to give the measurable quantity of intensity as $I=|E_0 \sin(\omega t+\varphi)+E_0 \sin(\omega t)|^2 \approx 2I_0 \cos^2(\varphi/2)$. Additional phase shifts, for example on the mirror, are neglected and a time average is taken as detectors typically do not resolve temporal oscillations.

Figure 3.1: Scheme of optical interferometry. Adapted from Olivares p. 347 [\[4\]](#sect8).

Long description

Diagram showing the path of a laser beam starting from a laser, split into two by a beam splitter. Each beam is reflected by a mirror. One of the two beams passes through media experiencing an additional phase shift of Δn∙kL. The two beams are then recombined to produce interference and the two beams emerging from the recombiner are then measured by two detectors.

One of the optical interferometers widely used today for inertial sensing (as a gyroscope) is the Sagnac interferometer [\[3\]](#sect7). It has two counter-propagating beams enclosing the interferometer area, and can measure rotations to a very high accuracy by detecting the path length difference between the two beams as the position of the beam-splitting optics changes during the round trip of light in the interferometer.

**Light-pulse atom interferometry**

Many atom interferometers conceptually resemble the optical Mach–Zehnder interferometer. The first atom interferometry experiments were demonstrated using mechanical gratings [\[1\]](#sect5).

Today, most of them rely on light-pulse atom-optical elements, as this is easier to implement and gives more flexibility in manipulating the atoms. Additionally, it is often more robust. In the light- pulse atom interferometry scheme (see Figure [3.2](#fig:at-interferometry)), light takes the role of mirrors and beam splitters for the matter waves, effectively inverting the roles of light and matter in a traditional, optical interferometer [\[2](#sect6), [6\]](#sect10). Although there are many types of light-pulse atom interferometry approaches regarding the types of atom-light interactions, here, we are discussing only one of them for simplicity: Bragg diffraction with stimulated Raman transitions.

Figure 3.2: Scheme of light-pulse atom interferometry.

Long description

Diagram showing the trajectories of atoms in an atom interferometer. The atoms are initially in state ‘a’ and have momentum ‘_p_0’ shown as a horizontal arrow. The splitting of this atomic beam is done by a grating, for example, a standing wave of light pulse depicted as a periodic vertical pattern. Following the beam splitter, there are atoms in both state: ‘a’ with momentum ‘_p_0’ (horizontal line) and in state ‘b’ with momentum ‘_p_0 + Δ_p_’ (diagonal line). Both atomic beams are diverted by another grating called a ‘mirror’ which changes the state and momentum of the latter one into state ‘a’ and momentum ‘_p_0’ and the former one into state ‘b’ and momentum ‘_p_0 + Δ_p_’ shown with corresponding arrows. A third grating called ‘beam recombiner’ is placed at the intersection of the two atomic beams and is necessary for the atomic beams to interfere.

**Bragg diffraction with stimulated Raman transitions**

**The internal state of the atoms** 

If we consider atoms with multiple energy levels, stimulated Raman transitions between two levels, a and b, refer to a transition (see Figure [3.3a](#fig:AI-components)) stimulated by laser fields that excite the atoms in level a to a virtual level (dashed line). Consequently, they stimulate the transition from the virtual level to level b, and back via the same path. The two laser fields simultaneously present to interact with the atoms have energies $\hbar\omega_1$ and $\hbar\omega_2$.

Figure 3.3: Schematic of stimulated Raman transition (a), the equivalent two-level system (b) and Rabi oscillations between states a and b (c). Adapted from Brif et al. p. 3 [\[6\]](#sect10).

Long description

Diagram composed of three separate diagrams. The left panel shows the energy level scheme for stimulated Raman transition between levels ‘a’ and ‘b’ using laser fields via a virtual level near the excited state labelled ‘e’. Levels ‘a’, ‘b’ and ‘e’ are shown with horizontal lines, ‘a’ being the lowest and ‘e’ the highest level. The virtual level shown with a dashed line sits below level ‘e’ with a detuning of frequency ‘Δ’. The laser fields stimulating the Raman transition are of frequency ω1 and ω2 shown as arrows from level ‘a’ to the virtual level, and from the virtual level to level ‘b’, respectively. The middle panel depicts the equivalent two-level system, which consists of the lower level ‘a’ and higher level ‘b’ and the effective laser of frequency ωeff. In right diagram, the Rabi oscillations between state a and b are shown in a graph, with the x-axis labelled t\[1/ΩR\] (time normalised to the Rabi frequency) and the y-axis labelled N/N0. The relative population is expressed as the number of atoms in state a vs. the total atom number (solid line) and as the number of atoms in state b vs the total atom number (patterned line of small circles).

The virtual state needs to significantly differ from the nearest excited state e (lasers off resonant from level e by an energy gap $\hbar\Delta$), such that the atoms do not stay in level e. In this case the three-level energy scheme for the atom can be considered to be effectively a two-level scheme as shown in Figure [3.3b](#fig:AI-components), with the laser light being effectively resonant with the atomic transition $(\hbar\omega_\mathrm{eff})$ between levels a and b. The light interacts with the atoms  coherently: it drives the populations between the levels a and b in an oscillatory manner. These oscillations are called Rabi oscillations (Figure [3.3c](#fig:AI-components)) [\[5\]](#sect9). Starting with the atoms in level $\mathsf{a}, a \pi/2$ phase evolution of the Rabi oscillation brings the atoms into a superposition state with equal probability of the atoms being in level a and level b.  A $\pi$ phase evolution will excite the atoms from level a to level b, or if they start in level b then it will bring them to level a. The phase evolution for the light fields at fixed intensity only depends on the pulse duration that the light field is applied for. Therefore, the laser pulses driving these situations are called $\pi/2$ or $\pi$ pulses, and they act as a 50:50 beam splitter or a mirror, respectively, for the atomic states.

**The momentum state of the atoms**

During the interaction of atoms with light, both the momentum and energy need to be conserved. The momentum transfer from the light field to a single atom is shown in Figure [3.4](#fig:AI-components2a), where a photon from each of the counter-propagating Raman beams (as explained in Figure [3.3a](#fig:AI-components)) is absorbed by the atom, and consecutively two photons of the energy and momentum of one of the incoming photons are emitted, as the stimulated emission process dictates. The photon momenta are of the form $\hbar \mathbf{k}$, where k is the wave vector. The momentum of the atom in this process changes by $\Theta = \Delta p / p_\mathrm{beam} = n \lambda_\mathrm{dB}/d.$. This elementary process takes place in a light pulse beam splitter as described in the previous section.

The beam splitters used in atom interferometry are often based on diffraction. Diffraction occurs when a wave interacts with any object that locally shifts its phase or amplitude, and involves the coherent superposition and interference of the wave with itself after propagating through the diffracting region via different paths. A diffraction grating is a spatially periodic object that splits an incident wave into multiple momentum orders. The $n^\textrm{th}$ order momentum transferred to the wave is $\Delta p = n h/d,$, where n is an integer, h is Planck’s constant and d is the grating period. Since the de Broglie wavelength depends on the initial momentum of the atomic beam $p_\mathrm{beam}$ as $\lambda_\mathrm{dB}=h/p_\mathrm{beam},$, the resulting diffraction angles are $\Delta \mathbf{p}=\hbar \mathbf{k}_\mathrm{eff}=\hbar (\mathbf{k}_1 -\mathbf{k}_2)$. To observe the interference, the transverse momentum distribution of the incident atomic wave must be small enough to resolve the diffraction orders.

Figure 3.4: Momentum transfer from two counter-propagating light fields to the atoms when a photon from each field is absorbed and two photons are emitted by stimulated emission. Adapted from Peters et al p. 25 [\[7\]](#sect11).

Long description

At the top of this diagram, the initial state of an atom is shown, where the atom, depicted as a circle is in energy state |a ⟩ and has a momentum p = 0. To the left of this atom is a zig-zagged arrow pointing to it representing the photon momentum of hk1. To the right of the atom is another zig-zagged arrow pointing to representing the photon momentum of hk2. Following the momentum transfer process the final state is shown at the bottom of this diagram. The atom in this case is in energy state |b ⟩ and has a momentum p = h (k1 — k2) = hkeff shown with the circle and an arrow pointing to the right. To the left of this atom are two zig-zagged lines with arrows pointing left representing the photons of total momentum 2hk2.

Standing waves of light can make a phase (or amplitude) grating for a particular species of atoms in a specific state. The non-dissipative gratings (ones that do not alter the amplitude of the incoming beam at the grating) are called Kapitza-Dirac or Bragg gratings [\[2\]](#sect6), which correspond to the two regimes shown in Figure [3.5](#fig:AI-components2b). The Kapitza-Dirac gratings are thin, or consist of very short pulses of light, and produce multiple diffraction orders around the central transmitted beam ($0\mathrm{th}$ order). Bragg gratings correspond to thick or longer pulses of light and when the incidence angle to the grating is optimal, only one diffraction order appears beside the transmitted ($0\mathrm{th}$) beam.

Figure 3.5: Two examples of atomic beam diffraction on light pulses. Adapted from Cronin et al p. 1060 [\[2\]](#sect6).
Long description

To the left of this diagram, the thin grating Kapitza-Dirac diffraction is depicted. In this depiction, an arrow with the label ‘Atom Beam’ is pointing to a thin horizontal line with the label of ‘Mirror’. From this ‘Mirror’, five arrows are pointing away that are in a ‘fanned out’ formation. To the right of this diagram, the thick grating Bragg diffraction is depicted. In this depiction, an arrow with the label ‘Atom Beam’ is pointing to a thick horizontal line with the label of ‘Mirror’. From this ‘Mirror’ there are two arrows pointing from it; one labelled ‘0th order’ and the other labelled ‘1st order’.

**An atomic gravimeter**

In the interferometer scheme we have discussed, the first diffraction grating (pulsed standing wave of light from the Raman beams) creates a superposition of internal as well as of momentum states (see labelling in Figure [3.3](#fig:AI-components)b). The excited part of the superposition, which has gained energy from the photons $(\hbar\omega_\mathrm{eff})$ and acquired photon momentum $(\hbar \mathbf{k}_\mathrm{eff})$, will move away from the part left in the ground state, allowing the atoms to simultaneously travel along different trajectories. When these paths differ in height, the resulting interference phase will depend on the gravitational potential difference between the trajectories, and the interferometer becomes a very sensitive gravity sensor. One of the first atom interferometers following the $\pi/2 - \pi - \pi/2$ light pulse scheme (demonstrated in 1991 by Kasevich and Chu [\[1\]](#sect5)) was developed into a high-precision gravimeter (Peters et al [\[7\]](#sect11)). The space-time diagram of this atom interferometer (Figure [3.6](#fig:Chu-gravimeter1)) shows the effect of gravity on the trajectories of the atoms starting from the space-time point $(t=0)$ when the initial wave packet is split into two by the first interferometer pulse. The straight lines are the trajectories without gravity, and the curved lines are the trajectories in the presence of gravity.

Figure 3.6: Atomic gravimeter scheme based on the $\pi/2 - \pi - \pi/2$ pulse sequence involving Bragg diffraction with stimulated Raman transitions. Adapted from Peters et al. p. 26 [\[7\]](#sect11).

Long description

Graph of the atomic gravimeter scheme based on the π/2 − π − π/2 pulse sequence with the x-axis labelled ‘t’ for time and the y-axis labelled ‘z’ for position. This graph has three key points: π/2 pulse (beam splitter) at 0 of the time-axis, π pulse (mirror) at T of the time-axis and π/2 pulse (beam splitter) at 2T of the time-axis.

When the interferometry sequence is optimised, one needs to take care of the phase of the Raman beams and ensure that the positions of the nodes/antinodes in the standing wave align with the position of the atoms as they are falling. The former one can be adjusted by adding a time dependent relative frequency shift (chirp) between the counter-propagating beams [\[2\]](#sect6). If there is a significant mismatch between the chirp rate $\alpha$ and the free-fall rate g (showing up on the curved trajectories intersecting the pulse at $t=T$ in Figure [3.6](#fig:Chu-gravimeter1) at a different phase of the pulse as for $t=0$), a reduction in excitation efficiency – and consequently in interference contrast – due to a non-compensated Doppler shift [\[2\]](#sect6) appears. Therefore, finding the optimal chirp rate $\alpha=g$ experimentally (which can be precisely controlled with high-spec waveform generators) is equivalent to finding the value for the atoms' acceleration or g. A measurement of the atomic population in state $\mid{b}\rangle$ at the interferometer output versus the phase of the grating extracted from $\alpha$ (for a pulse spacing of $T=160~ms$ ms) is shown in Figure 19 of Peters et al [\[7\]](#sect11). Performing a least squares fit to this data determines local gravity to $10^{-9} g$ accuracy.

The coherence and narrow momentum distribution of atoms necessary for interferometry are ensured by cooling the atoms to a millionths of a degree above absolute zero (sub-microkelvin temperature). The atomic clouds contain tens of thousands to millions of atoms to get better statistics on the measurement of populations, and the measurement sequence is repeated many times to reduce the error.

An overview of the experimental setup showing the elements of laser cooling/trapping and preparation of atoms in the initial state for interferometry, the Raman beams, detection beams and suppression of environmental effects using vibration isolation and magnetic shielding can be seen in Figure 5 of Peters et al [\[7\]](#sect11). The atoms in this configuration have been prepared in the lower part of the experiment, launched upwards, and detected after falling back to the launch site. This way, the interferometer time 2T can be considerably enlarged to achieve better sensitivity to gravity. In Figure 23 of Peters et al [\[7\]](#sect11), gravity data is plotted over a period of several days. The data points are $\sim 1$ minute apart and each corresponds to one of the interferometer fringes shown in Figure 19. The gravity data clearly shows the complex variations of g caused by tidal effects. The solid line comes from a theoretical model of gravity tides at the measurement site.

To determine the accuracy of the atomic gravimeter, a comparison to an absolute gravimeter needs to be done. Figure 25 of Peters et al [\[7\]](#sect11) shows such gravity measurements taken at nearby locations simultaneously, as the measurements are sensitive to changes in the local environment. The offset between the data sets is mainly due to environmental effects. The classical gravimeter here is the FG5, one of the most advanced absolute gravimeters, which measures gravity by monitoring the motion of a free falling corner cube acting as a retro-reflector in one arm of a Michelson interferometer [\[2\]](#sect6).

In addition to the accuracy, the measurement noise is another important property of an instrument. The FG5 has a drop rate of 4/minute, and for ideal conditions (seismologically quiet site, far from civilisation related noise and using the maximum achievable drop rate of  60/minute) it is specified to have a resolution of $5\, \mu\mathrm{Gal}/\sqrt{\mathrm{Hz}} (1\, \mathrm{Gal}= 0.01\, \mathrm{m/s}^2$ after Galileo). The atom interferometer has a drop rate of 40/minute and the resolution is measured to be $20\, \mu\mathrm{Gal}/\sqrt{\mathrm{Hz}}$. From the data in Figure 25 of Peters et al [\[7\]](#sect11), where each data point represents 1 minute of tide corrected gravity data, the comparison indicates that under noisy environmental conditions, the atom interferometer noise is smaller by a factor of 3 for equivalent measurement times. The noise per drop is comparable for the two instruments.

## 3.2 Advantage of using atoms for inertial sensing

Inertial sensors based on atom interferometers already perform better or comparably to the best available sensors based on any technology [\[8\]](#sect12). The achievable performance of atom interferometers depends on which quantity we aim to measure and the type of interferometer such as gravimeters, gyroscopes or gravity gradiometers. For example, thermal atom beams for rotation, freely falling atoms for acceleration, and two clouds of falling atoms with a common laser beam for the gradiometer have given the best results to date. To explore the precision, resolution, accuracy, and stability, we begin by looking at the response factor. For a three-grating interferometer, acceleration $a$ and rotation $\Omega$ cause a phase shift of 

$$
    \Phi = (k_\mathrm{eff} a)\tau^2 + 2k_\mathrm{eff} (\Omega\times v)\tau^2,
$$ 
(3.1)

where $\tau=2T$ is the total interferometer (interrogation) time and v is the velocity of the atoms between the gratings. The presence of velocity v in the second term means that in a space-domain interferometer, the acceleration phase depends on $\tau^2$ while the rotation phase depends on $\tau$. Therefore, slow (cold) atoms are particularly advantageous for sensing acceleration, but fast atomic beams offer competitive sensitivity for gyroscopes. However, the phase shift is not the only factor that matters for the performance. Part of the trade-off is that fast atomic beams offer more atoms per second than cold atom sources. Larger interferometers will improve sensitivity and slow atom interferometers can make compact sensors. In each case, to judge the overall performance one must also look at systematic errors.

**Comparison of atomic to optical interferometry**

Taking rotation as an example, a space-domain atom interferometer obtains a phase shift of $\Phi_\mathrm{atom} = 2\Omega k_\mathrm{eff}LT = 4\pi\Omega mA/h,$, where L is the separation between gratings, T is the time of flight between gratings, and A is the area enclosed by the interferometer paths. To relate this quantity to the de Broglie wavelength we can use $\lambda_\mathrm{dB}=h/p$ and $p=mv$.  For an optical interferometer, the phase shift is $\Phi_\mathrm{light} = 2\Omega k_\mathrm{eff}L^2/c = 4\pi\Omega A/\lambda_\mathrm{ph}c,$, with c being the speed of light. The ratio of phase shifts for a given rotation rate $\Omega$, assuming equivalent interferometer areas A, gives an estimate of how the performance of the two interferometers compare:

$$
\frac{\Phi_\mathrm{atom}}{\Phi_\mathrm{light}}= \frac{ m}{h} \cdot \frac{1}{1/\lambda_\mathrm{ph}c } = \frac{\lambda_\mathrm{ph}c }{\lambda_\mathrm{dB}v} \approx 10^{10}
$$
(3.2)

This ratio shows that atom interferometers have a large Sagnac response factor compared to optical interferometers. (For acceleration $\frac {\Phi_\mathrm{atom}}{\Phi_\mathrm{light}} \propto (\frac{c}{v})^2$) This is mainly due to the fact that atoms travel along the interferometer much slower than the photons, thereby sensing the inertial effect for an increased duration. However, to really gain this large increase in resolution both the enclosed area and the count rate of the two types of interferometers must be equal. But a fibre optic ring gyroscope can easily have an enclosed area of $A=10^3$ m2 (see fibre optic gyroscopes or LIGO) and still have a much better bandwidth compared with the largest atom interferometers that have $A=10^{-4}$ m2$. So the response factor is only a few orders larger for today’s atom interferometers. Furthermore, while the photon count rate for a watt of laser power is on the order of $10^{19}$ photons/s, typical atom interferometers offer only $10^7$ atoms/s.

Instrument **resolution** is given by the response factor times the precision with which the phase shift can be measured. Since the noise-limited phase precision increases with the square root of time, the resolution is typically given in units of $1/\sqrt{\mathrm{Hz}}$. Instrument **bandwidth** is limited by the resolution and also simply by the interferometer time. Many applications in geophysics are currently served with gravity sensors that have $5\times 10^{-9}g$ $(5\,\mu\mathrm{Gal})$ precision after averaging for 15 minutes. The light pulse atomic gravimeter attains this precision in less than 1 minute (Peters et al. [\[7\]](#sect11)).

Figure 3.7: Competing methods for precision gravity measurements. Adapted from de Angelis et al p. 8 [\[9\]](#sect13).

Long description

In the panel to the left, a schematic of the spring gravimeter method is shown. Here, a spring with a ball weight (with force ‘mg’) attached at the end is shown. The length of the spring is ‘L’. The vertical component of the ball position is ‘y’. The gravitational acceleration in the spring gravimeter can be expressed as g = y k/m, where k is the spring constant. In the middle panel, a schematic of the superconducting gravimeter method is shown. Here, a coil is shown with a voltage ‘V’ applied to it, levitating the Nb atom. The setup is placed in liquid helium. In the superconducting gravimeter, g is related to the coil voltage. In the panel to the right, the free-falling corner cube gravimeter method is shown. Here, a horizontal laser beam is partially reflected by a beam splitter, retroreflected from a corner cube, which is the test object shown at various heights above the beam splitter, using solid and dashed lines, marking the vertical positions as D1T1, D2T2 and D3T3. The retroreflected beams in each case cross the beam splitter and get retroreflected by another corner cube below, to finally overlap the horizontal laser beam upon reflection. The superposition of the two horizontal beams is detected on a fringe detector. A small inset shows the shape of the signal, which is a frequency modulated (i.e. chirped) sinusoidal wave, that has the zero crossings T1, T2 and T3 at reducing intervals. In this free falling corner cube gravimeter, g is related to the fringe chirping.

**Competing methods for gravimetry**

To measure gravitational acceleration, there are two types of gravimeters: absolute meters, where g can be directly determined by measuring a length and/or a time, and relative meters, which only detect variations of g over time. The earliest instrument, used for the first gravimetric survey mapping in the 1930s, was a pendulum in which the period T, the length L and g are related by the simple relationship $T = 2\pi \sqrt{L/g}$. The accuracy achieved with these measurements was $\Delta g/g\approx10^{-4}$. Nowadays, for gravimetric survey, relative spring gravimeters are used, while superconducting and freely falling corner cube gravimeters are used at fixed sites (see Figure [3.7](#ffig:gravimeters)).

Spring gravimeters [\[10\]](#sect14) consist of a mass on an almost mass-less spring with elastic constant k and total length L. The equilibrium position for a spring elongation $\delta L$ is $k\delta L = mg$ and the oscillation period is $T = 2\pi \sqrt{m/k}$. This instrument allows us to measure changes in g by measuring changes in $\delta L$, working as a relative gravimeter. The sensitivity is proportional to $1/T^2$. Nowadays mass spring gravimeters are designed to have very large L and ‘zero length springs’, whereby one can measure changes in g by measuring changes in y. The main sources of uncertainty are the error in the measurement of y and the spring hysteresis, which causes temperature and random drifts. It enables only relative measurements and must be frequently re-calibrated. The advantages of these gravimeters are their size/weight/power $(0.04~\mathrm{m}^3/ 14~\mathrm{kg} /24~\mathrm{W})$ and the low noise of $\Delta g/g \approx 5\times 10^{-9} /\sqrt{\mathrm{Hz}}$. However, the drift can be as large as $\Delta g/g \approx 1.5\times 10^{-6} /$ month.

Superconducting gravimeters provide relative gravity measurements, too. The principle is to levitate a superconducting sphere in a magnetic field. Gravity changes are compensated by an electrostatic force applied to the sphere to keep it levelled. It is essentially an electromagnetic spring with a voltage readout signal. The instrument is not portable with its size/weight/power of  $1.5~\mathrm{m}^3/ 320~\mathrm{kg} /400~\mathrm{W}$, but is exceptionally stable in time $(\Delta g/g \approx 10^{-9} / year)$ and has very low noise of $\Delta g/g \approx 10^{-12} /\sqrt{\mathrm{Hz}}$.

Falling corner cube gravimeters provide absolute gravity measurements. The idea is to observe an object in free fall and determine its acceleration. The path length is measured by using an interferometric technique: a freely falling corner cube mirror is the end mirror of one of the arms of a Michelson interferometer. When the cube drops, a sensor reads the interference signal as a function of time. The detected signal is related to the number of half wavelengths of interferometer light covered during the fall by the mirror. For a drop of the mirror (of approximately 20 cm), the values of position and time are recorded and fitted to obtain g. The advantage of this instrument is that it is an absolute gravimeter with an accuracy of $\Delta g/g \approx 4\times 10^{-9}$ and noise level of $\Delta g/g \approx 5 \times 10^{-8} /\sqrt{\mathrm{Hz}}$. The disadvantage is that the most accurate instruments of this kind are not portable (size/weight/power of  $1.5~\mathrm{m}^3/130~\mathrm{kg} /350~\mathrm{W}$; however, there are portable versions such as the FG5 mentioned earlier.

## 3.3 The future of atom interferometry

**Types of atom interferometers**

There are four types of atom interferometers:

-   **Absolute atomic gravimeter:** The instrument described in the previous section has been further improved and systematic errors have been eliminated to find an agreement with the falling corner cube measurement of $\sim 10^{-8}$. The uncertainty has reached as low as $1.3 \times 10^{-9}$, representing the most accurate measurement of absolute acceleration of gravity, and it has been used to  test the local Lorentz invariance of post-Newtonian gravity by monitoring Earth gravity.

-   **Atomic accelerometer:** The concept for an atomic accelerometer is the same as for atomic gravimeters, with the axis of the counter-propagating 'interferometer' beams (i.e. Raman beams in our example) defining the direction of the acceleration to be measured. Accelerometers using atom-interferometry are mostly developed for applications to inertial navigation as a building block of a full inertial measurement unit (IMU). As a single-axis accelerometer only requires one (retro-reflected or one pair of) laser beam interacting with atoms at one given position, their implementation is simpler than for gyroscopes, which need to open a physical area to the interferometer. However, the first demonstration in a mobile vehicle (a plane) has shown the difficulties due to high frequency accelerations (vibrations) of the carrier and dead times between successive measurements, since the use of an isolation platform is not a solution for this type of operation. Different approaches to overcome these difficulties include the increasing of the repetition rate and bandwidth, the hybridisation with a classical accelerometer, multi-signal (for example multi-species) atom interferometers, and multi-axis measurements in a single shot.

-   **Atomic gyroscope:** A thermal atom gyroscope can be built using stimulated Raman transitions to coherently manipulate the atoms from counter-propagating thermal beams, forming two interferometers with opposite rotation phase shifts. This configuration allows rotation to be distinguished from acceleration. By electronically compensating the rotation-induced Doppler shifts of the Raman lasers, operation at an effective zero rotation rate can be achieved. An instrument rotation-rate sensitivity of $6\times 10^{-10}\,\mathrm{rad/s/}\sqrt{\mathrm{Hz}}$ has been achieved. Potential applications include inertial navigation, geophysical studies and tests of general relativity. 

-   **Atomic gravity gradiometer:** An atomic gradiometer is a gravimeter where two clouds of laser cooled atoms, separated by a distance D, are used for a simultaneous measurement of local gravity with respect to the common reference frame identified by the wavefronts of the Raman lasers. The instrument detects the differential acceleration $\Delta g$ and therefore the component of the gravity gradient along the direction of the Raman lasers is simply $\Delta g/D$. For each cloud interference fringes similar to those shown earlier are obtained. The accuracy of atomic gradiometers can be as low as $10~E (1~E = 10^{-9} \mathrm{s}^{-2}$ and the sensitivity $4 \times 10^{-9} g\mathrm{/m/}\sqrt{\mathrm{Hz}}$.

**Development directions**

It has been more than 30 years since the first demonstration of the Raman atom interferometer [\[2\]](#sect6). Many variants and technologies have been developed to improve the sensitivity of the devices and they are used in a wide range of applications. These applications require different performance of the atom interferometers, including sensitivity, accuracy, dynamic range, stability, compactness, portability and cost. Typically, applications in fundamental physics and metrology need atom interferometers with the highest sensitivity, while other applications have different criteria that need to be addressed during the development aimed at the specific application.

The sensitivity of atom interferometers can be improved by increasing the enclosed area of the interferometer by increasing the arm length L or the interrogation time T, but it can also be achieved by transferring large momentum to the atoms at the beam splitters. The former approach is limited by the spatial expansion of the atomic cloud during the sequence. To allow for long T or L the atoms can be cooled to ultra-low temperatures; however, this comes with a trade-off on atom number, and both lead to reduced bandwidth of the instrument.

**Large interferometer**

The Kasevich group (Stanford) built a $10~m$ tower for their atom interferometer [\[11\]](#sect15) to simultaneously measure the gravitational acceleration of two isotopes of rubidium to verify the equivalence principle in general relativity, and the sensitivity has reached $3 \times 10^{-11} g/\sqrt{\mathrm{Hz}}$.

**Large momentum transfer**

In the standard $\pi/2 - \pi - \pi/2$ sequence, the Raman pulses only transfer $2\hbar k_{\mathrm{eff}}$ momentum to the atoms. Methods to transfer tens or hundreds of $\hbar k_{\mathrm{eff}}$ momentum have been achieved by a sequence of Bragg pulses and by multi-photon processes, and further approaches include modified sequences where so-called Bloch oscillations are utilised or the Talbot-Lau interferometer scheme is realised.

**Portable devices**

Due to their competitive performance, atom interferometers have drawn lots of interest for applications such as inertial navigation, gravity detection and mineral surveys [\[8\]](#sect12). Therefore, a compact and portable system for field applications is desired. In the past decade, huge efforts have been devoted to developing portable systems. For instance, the size of an atomic gyroscope based on dual interferometers from the Kasevich group was smaller than $0.6 \times 0.6 \times 1\, \mathrm{m}^3$, and reached a sensitivity of $7 \times 10^{-6} \mathrm{rad/s/}\sqrt{\mathrm{Hz}}$. Their compact gravity gradiometer was smaller than $1\,\mathrm{m}^3$, and the sensitivity was $6 \times 10^{-9} g\mathrm{/m/}\sqrt{\mathrm{Hz}}$.

Compact and portable atomic gravimeters are already commercially available from companies like Muquans [\[12\]](#sect16) and AOSense and their performance is comparable to commercial falling corner cube instruments, like the FG5. The ultimate approach for miniaturisation might lie in using atom chip technology. Atom chips are micro-fabricated wires patterned on a substrate to trap and manipulate ultra-cold atoms. A free falling Bose-Einstein condensate from an atom chip has been used as an atomic gravimeter and an accuracy of $1.7 \times 10^{-7}g$ was obtained. To learn more, read Abend et al [\[13\]](#sect17). This technology will become more important for developing compact matter-wave interferometers for certain applications.

## 3.4 Applications of atom interferometry

Accurate gravity measurements find applications in many fields of physics: for example, in metrology for both the definition of SI units and a better knowledge of fundamental constants. Atom interferometry has also been proposed for laboratory tests of general relativity. These can be competitive with astrophysical tests and potentially superior to them in the long run. The main advantage in the short run is that there is limited control in astrophysical observations and often relativistic effects cannot be decoupled, while atom interferometry enables this.

**Applications in metrology and fundamental physics**

-   Measuring $h/m$, a component of the fine-structure constant, $\alpha$. This component is known to the least precision, therefore its measurement with higher precision will lead to more information about $\alpha$, which determines the strength of electromagnetic interactions, and plays a role in the theory about the expansion of the universe. The $h/m$ ratio is proportional to the photon recoil in an atomic accelerometer, which can be tested to high precision when other sources of acceleration are eliminated.

-   Testing Einstein's equivalence principle, in which one of the assumptions is the 'universality of free fall' (UFF). Finding a violation to the UFF will bring a unified theory of quantum gravity a step closer. The UFF can be tested by measuring the gravitational acceleration of two bodies, for example two atomic species simultaneously in an atom interferometer.

-   Newton’s gravitational constant, G, is the least accurately known fundamental constant. The 2005 CODATA value of G has a precision of $1.4\times 10^{-4}$. Atom interferometry involving two gravimeters may soon provide better precision $(10^{-5})$ to the CODATA value.

-   Gravitational wave detection [\[14\]](#sect18) has been a very recent major breakthrough that confirms Einstein's prediction of the existence of these waves. They provide valuable information about violent cosmic events and offer a new way to study them. This discovery also opens up a new era in astronomy and cosmology, and has the potential to transform our understanding of the universe.

**Applications in geodesy and geophysics**

Satellite missions are presently used to map the geoid. In these missions the geopotential second-order derivatives, i.e. the accelerations of proof masses, are measured along the orbit. The second-order derivatives are then used in an inverse problem to calculate the gravitational potential. The ESA gravity mission GOCE is based on a three-axis gravity gradiometer. The predicted accuracy of the gradiometer is, depending on the axis, $6 -100\,\mathrm{mE/}\sqrt{\mathrm{Hz}}$ between 5 and 100 $\,mHz$. A sensor for any GOCE follow-on mission will have to perform even better: sensitivity down to $0.1\,\mathrm{mE/}\sqrt{\mathrm{Hz}}$ between 0.1 and 100mHz. These figures cannot be obtained with presently available three-axis gravity gradiometer concepts. Atom interferometry represents a promising technology. The sensitivity of these instruments improves with the square of the interrogation time T and, although limited to a few hundreds of milliseconds on the ground because of gravity, in space T can be as large as 10s. In these conditions, a space gravity gradiometer could in principle achieve a sensitivity better than $1\,\mathrm{mE/}\sqrt{\mathrm{Hz}}$ at 0.1 Hz. However, a significant miniaturisation effort is required to satisfy the compactness needed for a space mission.

Interest in terrestrial gravity measurements [\[15\]](#sect19) can be summarised as follows: (1) high resolution prospecting for resource exploration; (2) monitoring of human-induced processes; (3) high resolution geoid mapping (or positioning); (4) investigation of subsurface mass redistribution at local (e.g. volcanoes and geothermal systems), regional (post-glacial rebound) and global scales (Earth’s mantle and core).

**Geophysics:** requiring transportable systems

-   monitoring magma flows
-   measuring groundwater
-   mapping of tectonic structure.

**Space:** requiring autonomous operation

-   fundamental physics
-   gravity-based Earth observation.

**Civil engineering:** requiring robust systems

-   reducing risk in construction
-   sinkhole and mineshaft detection.

**Oil and minerals:** requiring operation on mobile platforms

-   determining rock density
-   oil and minerals prospecting.

**Navigation:** requiring high bandwidth

-   inertial navigation.

## Summary

Well done! You have now reached the end of this week’s Study – Week 3: Quantum sensors part 2: Inertial forces.

In this section we explored quantum sensors based on atom interferometry and their applications. In recent decades, atom interferometry has developed rapidly and matured into a versatile tool to measure inertial forces with ultrahigh precision. It is used for fundamental research in particle physics, general relativity and cosmology. At the same time, it has also been applied in areas of metrology, geophysics, civil engineering, oil and minerals exploration, navigation and space.

## References

1.  [\[1\]](#sect1) Kasevich, M. and Chu, S. Atomic interferometry using stimulated raman transitions. Physical Review Letters, 1991, 67 (2), pp. 181–184.
2.  [\[2\]](#sect1) Cronin, A. Schmiedmayer, J. and Pritchard, D. Optics and interferometry with atoms and molecules. Reviews of Modern Physics, 2009, 81 (3), p. 1051.
3.  [\[3\]](#sect1) Hecht, E. Optics 5th edn. Pearson Education, 2017.
4.  [\[4\]](#sect1) Olivares, S. High-precision innovative sensing with continuous-variable optical states. La Rivista del Nuovo Cimento, 2018. \[Online\], 41. pp 314--382. Available at: https://arxiv.org/abs/1806.02292 \[accessed 24 May 2023\].
5.  [\[5\]](#sect1) Griffiths, D. J. Introduction to Quantum Mechanics. 2nd edn. Pearson, 2014.
6.  [\[6\]](#sect1) Brif, C. Ruzic, B. and Biedermann, G. Characterization of errors in interferometry with entangled atoms. PRX Quantum, 2020. \[Online\], 1, p. 010306. Available at: https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.1.010306 \[accessed 24 May 2023\].
7.  [\[7\]](#sect1) Peters, A., Chung, K. Y. and Chu, S. High-precision gravity measurements using atom interferometry. Metrologia. \[Online\], 38 (1). Available at: https://iopscience.iop.org/article/10.1088/0026-1394/38/1/4/pdf \[accessed 24 May 2023\].
8.  [\[8\]](#sect2) Fang, B., Gillot, P., Dutta, I., Savoie, D., Lautier, J., Cheng, B., Garrido, C. L., Alzar, C. L., Geiger, R., Merlet, S., Dos Santos, F. P. and Landragin, A. Metrology with atom interferometry: Inertial sensors from laboratory to field applications. Journal of Physics: Conference Series, 2016, 723 (1), p. 12049.
9.  [\[9\]](#sect2) de Angelis, M., Bertoldi, A., Cacciapuoti, L., Giorgini, A., Lamporesia, G., Prevedelli, M., Saccorotti, F. and Tino, G. M. Precision gravimetry with atomic sensors. Measurement Science and Technology, 2008. \[Online\], 20, p. 022001. Available at: https://iopscience.iop.org/article/10.1088/0957-0233/20/2/022001 \[accessed 24 May 2023\].
10.  [\[10\]](#sect2) Lacoste, L., Clarkson, N. and Hamilton, G. Lacoste and romberg stabilized platform shipboard gravity meter. Geophysics, 1967, 32 (1), pp. 49–58.
11.  [\[11\]](#sect3) Sugarbaker, A. Atom interferometry in a 10 m fountain. PhD diss. Stanford University, 2014.
12.  [\[12\]](#sect3) Muquans. Absolute quantum gravimeter, n.d. \[Online\]. Available at: https://www.muquans.com/product/absolute-quantum-gravimeter/ \[accessed 24 May 2023\].
13.  [\[13\]](#sect3) Abend, S., Gebbe, M., Gersemann, M., Ahlers, H., Müntinga, H., Giese, E., Gaaloul, N., Schubert, C., Lämmerzahl, C., Ertmer, W., Schleich, W. P. and Rasel, E. M. Atom-chip fountain gravimeter. Physical Review Letters, 2016.\[Online\], 117, p. 203003. Available at: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.117.203003 \[accessed 24 May 2023\].
14.  [\[14\]](#sect4) Weiss, R. Ligo and the discovery of gravitational waves, i. Nobel Lecture, Massachusetts Institute of Technology (MIT), 2017.
15.  [\[15\]](#sect4) Tino, G. M. Testing gravity with cold atom interferometry: results and prospects. Quantum Science and Technology, 2021, 6 (2), p. 24014.