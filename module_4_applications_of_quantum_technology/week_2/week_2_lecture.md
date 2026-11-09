## Week 2: Quantum sensors part 1: Clocks and magnetometers: Study

## 2: Quantum sensors part 1: Clocks and magnetometers

## Introduction
This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

We introduced the various types of quantum technologies during the last week. This week and each of the coming weeks, we will learn more about each of the previously introduced technologies in more depth. We start this week by exploring clocks and magnetometers in the field of quantum sensors. These devices are superior to their classical counterparts in important ways. Before we go to the specifics of their operation, we will ask the question of what qualities actually matter for a good sensor. The previous notion that the improvements of a quantum sensor are ‘important’ depends on the needs of the applications, which we will therefore also explore in a little more depth.

 The Study topics this week are: 

-   [2.1 What makes a good sensor?](#sect1)
-   [2.2 Magnetic sensing](#sect2)
-   [2.3 Applications of magnetic sensing: Biomagnetism](#sect3)
-   [2.4 Applications of magnetic sensing: Navigation](#sect4)
-   [2.5 Applications of magnetic sensing: Material analysis](#sect5)
-   [2.6 Superconducting quantum interference devices (SQUIDs)](#sect6)
-   [2.7 Optically pumped magnetometers (OPMs)](#sect7)
-   [2.8 Nitrogen-vacancy centres](#sect8)
-   [2.9 Cold atom magnetometers](#sect9)
-   [2.10 Timing](#sect10)
-   [2.11 Why are atomic clocks useful?](#sect11)
-   [2.12 How does a clock work in general?](#sect12)
-   [2.13 How does an atomic clock work?](#sect13)
-   [2.14 Microwave and optical atomic clocks](#sect14)
-   [2.15 Future prospects for magnetometers and timing](#sect15)

## 2.1 What makes a good sensor?

From space-faring satellites monitoring weather systems, to stabilised drone cameras for blockbuster films, autonomous robots perceiving their environment or preventing the kitchen kettle from boiling over, sensors are ubiquitous in the modern world. Each of these scenarios has vastly different use case requirements and requires the sensing of different physical phenomena (for example, temperature, acceleration, magnetic fields or humidity). For two different sensors that measure the same physical phenomenon, which one should you choose?

Before further practical constraints are considered, the most important requirement is whether the sensor is able to measure the physical quantity that you are interested in.

Two important sensor performance measures (sometimes known as figures of merit) in metrology (the science of measurement) are accuracy and precision. While often used synonymously in the English language, in metrology, accuracy and precision are two distinct qualities that are not to be confused.

The precision of an instrument describes the degree of random variation in the sensor's output [\[1\]](https://canvas.sussex.ac.uk/courses/42093/pages/week-2-quantum-sensors-part-1-clocks-and-magnetometers-study#sect16). For example, an imprecise sensor would have a wide spread of output readings, whereas a precise sensor would have a narrow range of output readings. It is not possible to measure changes that are smaller than the random variation in the sensor without further processing of the signal. However, this processing would limit the response of the sensor to fast changes in the signal. On the other hand, the accuracy of a sensor describes how close the reading given by the sensor is to a hypothetical 'true' value . For example, a temperature sensor that reads $100.01^0$ when the 'true' temperature is $100.00^0$ would have high accuracy. A temperature sensor that reads $75^0$ when the actual temperature is $100^0$ would have low accuracy. If a temperature shut-off sensor in a kitchen kettle were to have such poor accuracy, it would continue heating the water even when it is boiling, regardless of the precision of the temperature measurement.

**Sensors could have:**

-   high precision and low accuracy 
-   low precision and high accuracy
-   low precision and low accuracy
-   high precision and high accuracy.

A sensor can be thought of as an archer shooting arrows at a target with a bullseye. If the central bullseye is the true value to be measured, the proximity of the archer's arrows to the bullseye is the archer's accuracy. The grouping of the arrows on the target is the archer's precision (see Figure [2.1](#fig2.1)).

After accuracy and precision, there are a number of other characteristics of sensors that one should consider, such as bandwidth and dynamic range. The bandwidth describes the sensor's ability to respond to fast-changing signals [\[1\]](#sect16). This is normally defined as the signal frequency at which the response of the sensor is reduced by a factor of $1/\sqrt{2}$. Due to this cut-off frequency, the bandwidth of the sensor of choice should be greater than the rate of change of the signal of interest. Dynamic range, on the other hand, determines the range of signal amplitude the sensor is able to record. If the signal of interest is greater than this range, the sensor has no meaningful output. Care must be taken to understand the range of signals that a sensor is able to observe, to ensure that its dynamic range is not exceeded. A more extensive discussion of sensor characteristics and measurement techniques can be found in Morris and Langari [\[2\]](#sect17).

Figure 2.1: Comparison of precision and accuracy. Adapted from Morris and Langari, p. 19 [\[2\]](#sect17).![Diagram of three dartboard-like sets to illustrate the difference between precision and accuracy.](https://canvas.sussex.ac.uk/courses/42093/files/6842113/preview)

Long description

Three dartboard-like sets of concentric circles illustrate the meaning of accuracy and precision. The first set shows a number of randomly distributed dots across the whole area of the circles, indicating a situation that lacks precision and accuracy altogether (labelled (a)). The second set displays a cluster of dots in one particular small, but not central, area of the rings, illustrating high precision but low accuracy (labelled (b)). The final set of circles shows a similar cluster of dots, but now inside the most central smallest circle ('bull's eye') to display a combination of high precision and high accuracy (labelled (c)).

Practical considerations must also be taken into account in order to implement a quantum sensor. The mass, volume and power consumption of the sensor are key issues for portable applications. Furthermore, reliability is of the utmost importance for space applications with no possibility of repairs. Depending on the number of sensors required and the value of the system into which they are to be incorporated, cost per sensor is a critical consideration. Fundamental research does not tend to require mass production of many sensors, so cost per sensor is not so crucial. If, on the other hand, one wants to incorporate a sensor into every smartphone, cost becomes key. 

Quantum sensing can interrogate fundamental physical quantities to achieve ultra-high precision and ultra-high accuracy measurements. While a basic understanding of this phenomenon has existed since the early 20th century, sensor volume, mass, power consumption and cost have limited their use to the study of fundamental physics [\[3\]](#sect18). However, recent developments in the miniaturisation and cost reduction of lasers, microelectromechanical systems (MEMS) fabrication and digital signal processing have enabled quantum sensors to be taken out of the lab and into application environments. Such is their sensitivity, and newfound portability, whole new application domains have been created that were once unreachable by conventional sensors. Two of the more mature quantum sensing domains of timing and magnetic sensing are described in the following sections.

## 2.2 Magnetic sensing

Magnetic fields are an elusive quantity to observe in everyday life unless they are very large, such as on a fridge magnet. Unlike temperature or acceleration, it is impossible for our bodies to perceive changes in magnetic fields. Magnetised minerals floating in water or oil were used to form our first compasses, and were the first magnetometers (magnetic field sensors). They allowed us to perceive the Earth's magnetic fields for navigation. For an understanding of size scales of magnetic fields, see Table [2.1](#tab2.1).

Table 2.1: Wide-ranging magnetic flux densities of different sources of magnetic fields.
|   Example | Approximate magnetic flux density (in tesla) |
| --- | --- |
|   MRI system magnet | $1.5 T$ |
|   Fridge magnet | $150\times 10^{-3}T(150mT)$ |
|   Earth's magnetic field | $50\times 10^{-6}T(50\mu T)$ |
|   Human heartbeat | $100\times 10^{-12}T(100\rho T)$ |
|   Human brain | $100\times 10^{-15}T(100fT)$ |

Since the development of the compass, a multitude of different technologies have been used for the detection of magnetic fields, including Hall probes, fluxgates and magnetoresistive devices. Conventional sensors have a large number of use cases, such as electronic compasses, orientation sensors, car traction control systems, and robotic arm positioning. Continued efforts to integrate them into electronic devices have enabled the embedding of such sensors in highly compact integrated circuits (ICs), albeit with a reduced accuracy and precision compared to their larger-scale cousins.

The precision of magnetic sensors is normally quantified with a figure of the sensor's noise or sensitivity. As this figure generally changes with frequency, it is often quoted as the spectral density over a frequency range with units of $T\sqrt{\text{Hz}}$. The lower this figure, the better the sensitivity and precision.

Regardless of the technology, it is often the case that the larger the magnetometer, the more superior the sensitivity. This can be seen in Figure [2.2](#fig2.2). The trade-off between sensitivity and sensor size has important consequences if one wants to build an array of sensors to form a magnetic image. The sensor size limits pixel-to-pixel distance, and therefore limits the resolution of the image.

Figure 2.2:  A comparison of the sensitivity of different magnetometer technologies in relation to their resolution.![Sensitivity of magnetometer technologies in relation to their resolution. Long description follows current section.](https://canvas.sussex.ac.uk/courses/42093/files/6842114/preview)

Long description

A graph of magnetic sensor sensitivity vs. spatial resolution in doubly logarithmic scaling. A variety of sensor types and their reported performance are displayed with different symbols. The general trend visible is that high sensitivity leads to lower resolution and conversely higher resolution leads to lesser sensitivity. On the graph a dashed trend line from the upper left to the lower right illustrates this trend. The line is drawn such that it divides classical sensors from their quantum counterparts. For a given resolution, the quantum sensors fall below this line (are more sensitive) and the classical sensors are above the line (less sensitive). The classical sensors displayed range from magnetic force microscopes (MFM) at around $10^{-4}~\mathrm{T}/\mathrm{Hz}^{1/2}$ sensitivity and $10^{-8}~\mathrm{m}$ resolution, via Hall probes and magnetoresistive sensors, to highly sensitive $(\sim 10^{-10}~\mathrm {T}/\mathrm{Hz}^{1/2})$ and lower resolution fluxgates $(\sim 10^{-2}~\mathrm {m})$. The quantum sensors displayed range from nitrogen vacancy (NV) centres at around $10^{-6}~\mathrm {T}/\mathrm{Hz}^{1/2}$ sensitivity and $10^{-8}~ \mathrm{m}$ resolution, via Bose-Einstein condensate microscopes (BEC-M), to highly sensitive $(\sim 10^{-15}~\mathrm {T}/\mathrm{Hz}^{1/2})$ and lower resolution superconducting quantum interference devices (SQUIDs) and optically pumped magnetometers (OPMs) $(\sim 10^{-3}~\mathrm {m})$ .

The sensitivity of some magnetometers can be exceeded by the ambient magnetic conditions. Nearby electronic devices, electric railways, power transmission cables, and vehicles create a noisy magnetic environment. The most precise magnetic measurements must, therefore, be conducted within magnetic shields made from materials with a high magnetic permeability, such as mu-metal (an alloy of nickel and iron), in order to achieve the desired sensitivity. These materials work by directing environmental magnetic fields around (rather than through) the sensor. For further information on different quantum and conventional types of magnetic sensors, read Grosz et al. [\[4\]](#sect19).

## 2.3 Applications of magnetic sensing: Biomagnetism

While there is a multitude of different applications for magnetic sensing, here we will concentrate on a few commercially interesting applications that require high precision or high accuracy.

Some living cells create magnetic fields whilst conducting their physiological functions. Of particular interest are cells that constitute part of the nervous system, called neurons. These cells are able to transmit neurological signals. When a neuron ‘activates’, a tiny electrical current is carried down the length of the cell, which the cell is then able to chemically transmit to other neurons [\[5\]](#sect20). The human brain is formed of a vast network of neurons. When a large number of neurons in a region are activated, small magnetic fields can be detected outside of the human or animal head. This non-invasive measurement of magnetic fields arising from the brain is called magnetoencephalography (MEG). Magnetic sensors may be arranged over a participant's head in order to create a map of the magnetic field distribution over time. This map can then be analysed to infer the positions of the electrical sources of those magnetic fields within the brain. Regions of activated neurons can be modelled as current dipoles (these can be thought of as a point-like section of wire). The field B at distance r away from the region of activity decays according to Eq. 2.1.

$$B\propto\frac{1}{r^2}.$$

The proximity of the magnetometers to the head is therefore of the utmost importance for increasing the amplitude of the field measured. As one moves closer to the source, the sensitivity of the magnetometer remains the same; however, the amplitude of the signal increases by $r^2$, thereby increasing the signal-to-noise ratio. Compared to its electric field cousin in the detection of neurological activity, electroencephalography (EEG), MEG is superior at distinguishing between separate nearby sources [\[6\]](#sect21). MEG has potential clinical applications including pre-surgical evaluation for epilepsy [\[7\]](#sect22) and early Parkinson's [\[8\]](#sect23)  and Alzheimer's [\[9\]](#sect24) disease diagnosis.

MEG has been widely used in research into the localisation and characterisation of processes within the brain. However, there are also developments in the monitoring of activity in the spinal cord (magnetospinography, MSG) and muscles (magnetomyography, MMG).

## 2.4 Applications of magnetic sensing: Navigation

Navigation with the use of satellite networks (global navigation satellite systems or GNSS) has become the status quo when travelling anywhere. However, there are a number of drawbacks to relying solely on satellites for navigation: 

-   lack of signal due to physical obstruction to the satellite networks
-   malicious jamming of the signals or spoofing by broadcasting fake GNSS signals to prevent somebody's location from being reliably established.

The monitoring of geomagnetic fields is one such solution for reliable global localisation. Magnetometers can be used to map magnetic anomalies in the Earth. By keeping on-board magnetic field maps, map-matching algorithms can be used to determine one's location without the need for external infrastructure [\[10\]](#sect25). The accuracy of localisation is therefore dependent on the quality of those magnetic maps, and the performance of the localisation algorithms, as well as the precision and accuracy of the magnetometer. For more details on magnetic navigation, read Lee and Canciani [\[11\]](#sect26).

## 2.5 Applications of magnetic sensing: Material analysis

Magnetic imaging can provide detailed structural and functional information on samples. Calculations similar to those used for MEG can be used to infer the location of magnetic sources. There is a multitude of magnetic sensing applications that require dense magnetic field maps to make observations of samples. One such example is the use of magnetometer arrays to monitor the distribution of currents within lithium-ion batteries for identification of defects and in order to grade battery performance [\[12\]](#sect27). Another example is the detection of structural defects in fatigued materials, which can be observed due to changes in their electromagnetic properties [\[13\]](#sect28). Furthermore, the quality of micro-fabricated structures can be interrogated. These industry-focused applications are rapidly developing alongside new quantum magnetometer technologies.

## 2.6 Superconducting quantum interference

Superconductors are materials that, once cooled below a critical temperature, allow electrons to flow without any resistance, and therefore without any losses. A superconducting quantum interference device (SQUID) consists of a loop of superconducting material interrupted in two places with a thin layer of insulating material [\[14\]](#sect29). These two gaps in the superconductor are called Josephson junctions, and the fact that they are electrically insulating inhibits the flow of electrons through them. Nevertheless, quantum mechanics dictates that there is a chance that these electrons will still pass to the other side of the gap through a process known as ‘tunnelling’. The presence of these gaps means that, if a current is passed through the loop, the voltage measured across the loop will oscillate whenever there is a changing magnetic field passing through the loop [\[15\]](#sect30). By measuring the current either side of the loop, one can monitor the number of oscillations n corresponding to the change in magnetic field, as calculated in Eq. 2.2.

$$\textbf{B}\cdot\textbf{S} =n\frac{\pi\hbar}{q_e}$$

Where B is magnetic flux density, S is the area of the loop, $\hbar$ is Planck's reduced constant and ${q_e}$ is the charge of an electron. This produces a very sensitive way of monitoring magnetic fields. Such is their sensitivity, they are able to measure biomagnetism, including fields arising from the brain. Thick insulation is required to insulate the participant from cryogenic temperatures, which limits their portability and the upkeep of cryogenic cooling increases costs. Watch this video by Cardiff University Psychology [\[16\]](#sect31) for an example of a SQUID system being used for MEG.

First used for MEG in the late 1960s [\[17\]](#sect32), SQUIDs are one of the more mature quantum magnetometer technologies. SQUIDs designed for MEG often achieve sensitivities of ${1}f T/\sqrt{\text{Hz}}$ and bandwidths of tens of $\kappa\text{Hz}$. Resolution is limited by the size of the pickup coils (approximately $1\text{cm}$ for MEG).

## 2.7  Optically pumped magnetometers (OPMs)

Optically pumped magnetometers (OPMs) utilise the evolution of atoms within a magnetic field to perform measurements. Typically, alkali atoms (such as caesium or rubidium) are held within a container, called a vapour cell, which is probed by laser beams to perform a measurement on the gaseous atoms. Alkali metals are solid at room temperature and therefore need to be heated in order to form a vapour. By absorbing light from a resonant laser beam, those alkali atoms can be pumped into the same quantum state [\[18\]](#sect33). Then, by monitoring the intensity or polarisation of light that is not absorbed, one can infer the state of those atoms.      

OPMs have been shown to achieve a similar, if not better, performance than SQUIDs [\[19\]](#sect34), and without the need for cryogenics, OPMs form compact and portable sensors. The added benefit of not requiring thick insulation for cryogenic cooling allows OPMs to take measurements much closer to sources of interest. This is pivotal for applications in MEG where, by moving closer to sources in the brain, one is able to better localise neural activity. An example of an OPM-MEG setup is shown in Fig. 2 of Brookes et al [\[20\]](#sect35) and can be seen in use in 'Designing a new brain scanner' [\[21\]](#sect36).

Although OPMs can offer reduced distances from sources compared to SQUIDs, the most sensitive OPM schemes (SERF or spin-exchange relaxation-free) have more limited bandwidths. While SQUIDs often achieve bandwidths of tens of $\kappa\text{Hz}$, SERF OPMs achieve bandwidths of less than $200\text{Hz}$. OPMs designed for MEG achieve sensitivities of approximately ${10}f T/\sqrt{\text{Hz}}$. Their spatial resolution is dependent on the size of the vapour cell (approximately $1\text{cm}$).

An introduction into the physics of OPMs for MEG is provided in Tierney et al [\[22\]](#sect37). For greater detail of the underlying physics of OPMs, as well as different OPM schemes, see Budker and Kimball [\[23\]](#sect38). This textbook can be used as a reference when specific schemes are of interest.

## 2.8 Nitrogen-vacancy centres

Nitrogen atoms can be introduced into diamond (carbon) lattices, causing an adjacent site in the lattice to become empty. The nitrogen atom with a neighbouring empty site is called a nitrogen-vacancy (NV) centre. In a similar way to that in which atoms are pumped into the same quantum state as was described with OPMs, so too can NV centres be pumped with the use of resonant lasers and microwave excitation. The magnetic field can then be inferred by fluorescence or by measuring the properties of the probing light.

As these magnetometers are fabricated from defects in diamond lattices, the sensitive region is extremely small in volume, and so very high resolution can be achieved. Magnetic imaging using NV centres can be performed either by creating an array of densely packed adjacent NV sensors or by attaching a single NV centre to a precisely controlled translation arm. Such a system can be seen within WebsEdge Science [\[24\]](#sect39). These techniques enable magnetic imaging with $<{10}\mathbb{nm}$ resolution.

Typically, the sensitivity that a single NV centre can achieve is approximately $100{\mathbb{n}{T}/\sqrt{\text\{Hz}}$. This can be improved at the expense of resolution by averaging over a large number of NV centres. High spatial resolution magnetic field images are pivotal for analysing the magnetic properties of nanomaterials and for understanding the operation of biological cells. For more insight into the operation of NV centre magnetometers, see Maze et al and Taylor et al [\[25](#sect40), [26\]](#sect41).

## 2.9 Cold atom magnetometers

Neutral atoms cooled to or below a millionth of a degree above absolute zero temperature can be used in many sensing applications. At such low temperatures, a gas of bosonic atoms undergoes a phase transition to become a Bose-Einstein condensate (BEC) where all the atoms occupy the same quantum state [\[27\]](#sect42). In the BEC state the atoms behave as a single quantum object rather than many thousands of distinct quantum objects. One of the quantum sensing applications of BECs is magnetic microscopy. This is implemented with alkali atoms such as rubidium within an ultra-high vacuum chamber. Viewports on the side of the chamber allow access to laser beams to cool and detect the atoms. By carefully controlling the current in tracks on an ‘atomic chip’, the shape and position of the BEC can be manipulated. Typically, a thin, elongated BEC (1D cloud) is created for this application. When placing the BEC near the surface of a sample, variations in the local magnetic field emerging from the sample cause variations in the shape of the BEC (as shown in Figure [2.3](#BEC-M)). By imaging the BEC cloud using a probing laser, one can infer the local magnetic field distribution. Furthermore, the 1D BEC can be scanned along the sample surface, producing a 2D image of the magnetic field parallel to the surface.

Figure 2.3: A schematic render of using ultra-cold atoms to magnetically map samples.![Schematic render of the use of ultra-cold atoms to magnetically map samples. Long description follows current section.](https://canvas.sussex.ac.uk/courses/42093/files/6842110/preview)

Long description

In this schematic three-dimensional render, a reflecting gold surface carrying a transparent sample with a random wire distribution is shown. A broad laser beam impacts upon the surface at a low angle and is reflected to a camera. A typical atom density image is shown next to the camera in false colour. A variable distribution of red blobs shows high atomic density in front of a low density (blue) background.

Such measurements have applications in the high-resolution magnetic field mapping of the nanostructure of small 2D samples. The rate at which one can capture magnetic images is therefore limited to the time required to create and move the BEC sausage. With this kind of cold atom magnetometer, resolution and sensitivity can be interchanged. As an example, for a resolution of approximately $100\mathbb{n}\mathbb{m}$, one would be able to resolve magnetic field changes of approximately $2\mathbb{n}{T}$. This therefore offers a slightly reduced spatial resolution compared with NV centres but superior sensitivity.

## 2.10 Timing

In addition to magnetometers, another relatively mature type of quantum sensor is atomic clocks. These are devices that take advantage of the discrete energy levels of electrons bound within atoms [\[28\]](#sect43). When an electron transitions between two energy levels, there is a well defined electromagnetic frequency proportional to the energy difference. This frequency can be utilised as the basis of creating a high performance clock. The parameters often used to describe the performance of a clock are stability and uncertainty.

Stability refers to the extent to which the frequency of the clock varies over an interval of time (how steadily the clock ‘ticks’). In a similar way to the precision of a sensor (a precise magnetometer gives many similar measurements with little random variation), so too does a stable atomic clock ‘tick’ at a frequency that does not vary much within a certain time-frame. Another way of putting this is to say that the noise associated with those ‘ticks’ is low. Since noise can often be reduced by taking an average of a number of different measurements, the stability of a clock is often given as a function of an averaging time [\[29\]](#sect44).

Uncertainty is the extent to which the frequency of an atomic clock may differ from the hypothetical ‘true’ frequency that is determined by the atomic transition that it uses. In this way, a clock with low uncertainty is highly accurate (similar to an accurate sensor). In other words, uncertainty is a measure of the effects of the physical processes other than this atomic transition that can influence the frequency of the clock; these processes are sometimes referred to as systematic effects. As a result, evaluating the uncertainty requires good knowledge of these systematic effects, which can include temperature-dependent effects and unwanted contributions from different atomic transitions [\[29\]](#sect44).

One example of an atomic clock can be found at the National Institute for Standards and Technology (NIST). This device, named NIST-F2, is a type of caesium clock, and would only lose roughly 1 second every 300 million years; in other words, roughly one part in $10^{16}$ [\[30\]](#sect45). In fact, this clock, and others like it, keep time so well that the Bureau International des Poids et Mesures (International Bureau of Weights and Measures) uses their principle of operation to define the duration of a second:

'The second, symbol s, is the SI unit of time. It is defined by taking the fixed numerical value of the frequency of caesium, $\Delta\nu_{\mathrm{Cs}}$, the frequency of the unperturbed ground-state hyperfine transition of the caesium 133 atom, to be 9 192 631 770 when expressed in the unit Hz, which is equal to $\mathrm{s}^{-1}.'$.′[\[31\]](#sect46) .

This definition was adopted across 1967–1968, when it first became technologically practical to use fundamental principles of nature in this way for timekeeping purposes. As such, atomic clocks based on caesium are among the oldest types of atomic clocks.

## 2.11 Why are atomic clocks useful?

Clocks based on conventional mechanical or electrical principles are employed in a huge range of devices, from wrist watches to computer systems. They are typically relatively simple and very reliable, and tend to have stabilities and uncertainties appropriate to their application. However, there are certain situations that are critically dependent on very accurate timekeeping beyond the capabilities of clocks based on classical physics. These situations include global navigation satellite systems, high-speed trading and global sensor networks, as well as tests of fundamental physics such as general relativity. Some of these applications require the measurement of time to a precision of tens of nanoseconds or less [\[32\]](#sect47).     

## 2.12 How does a clock work in general?

A clock may be thought of as requiring three key components:

-   something that oscillates in a periodic manner 
    
-   a means of counting those oscillations
    
-   a consensus on when that counting starts.

One example of an oscillator is a pendulum. When combined with an escapement mechanism in the form of a ratchet, the periodic motion of the pendulum can be translated into the rotation of a gear, allowing those periodic cycles to be easily counted on a clock face [\[33\]](#sect48). Another example is a quartz crystal oscillator. Quartz is a piezoelectric material, which means that, if it is mechanically deformed, it will generate a small voltage. Conversely, if a small voltage is applied across the material, it will oscillate at a particular frequency. It is this second property that makes it useful as the basis for many clocks. A quartz crystal clock [\[33\]](#sect48) is more stable than a pendulum clock and 'ticks' at a much higher rate, as the crystal can be engineered to oscillate at over 30,000 Hz.

## 2.13 How does an atomic clock work?

In the case of an atomic clock, the oscillations are provided by the discrete energy levels that electrons within an atom necessarily occupy, as described by quantum theory. Electrons can move up or down these energy levels if they absorb or emit photons, respectively. The energy of the photons matches the difference between those energy levels. More specifically, the difference in energy between two levels is given by the Planck relation, Eq. 2.3 [\[34\]](#sect49):

$$E = h\nu,$$

Where E is the energy of the atomic transition, ν is the corresponding frequency of a photon emitted or absorbed by the atom, and h is the Planck constant. If E is measured in joules, J, and ν in hertz, Hz, then $h \approx 6.63 \times 10^{-34}~\mathrm{J \cdot Hz^{-1}}$, so the change in energy is extremely small compared with the change in frequency. Crucially, this design means that the frequency of the oscillator in an atomic clock is determined directly by the laws of physics (in contrast to conventional clocks) and is therefore inherently extremely stable.

The oscillator atoms in an atomic clock are initially prepared in a particular energy state, using a magnetic field. Next, those atoms are exposed to microwave radiation at a particular frequency, which causes some of them to change energy state by absorbing energy from the microwaves, according to Eq. [(2.3)](#Planck). The closer the microwave frequency is to the resonance frequency of the atomic transition, the greater the fraction of atoms that will change their energy state in response to that radiation. By monitoring and maximising the fraction of atoms that have changed state, the microwave frequency can be tuned to be extremely close to the atomic resonance frequency. This microwave frequency can then be used as a reference to monitor, or indeed define, the passage of time. 

## 2.14 Microwave and optical atomic clocks

Not all atomic clocks use atoms of caesium as a frequency reference. Indeed, calcium, magnesium, ytterbium, or strontium may be used instead, for example [\[29\]](#sect44). Furthermore, not all atomic clocks use microwaves to change the state of their atomic oscillators. In fact, clocks based on certain atoms or ions instead use energy transitions corresponding to much higher frequencies, in the optical domain – 100s of terahertz $(\sim 100\times 10^{12} Hz)$, rather than roughly 9 gigahertz $(9\times 10^{9} Hz)$. Consequently, these optical atomic clocks ‘tick’ much faster than clocks based on microwaves and can be even more stable [\[29\]](#sect44). 

Unfortunately, the very fast ‘ticking’ of an optical atomic clock is also a disadvantage, since it is so fast that it cannot be counted directly, as modern electronic circuits cannot respond quickly enough for these frequencies to register. As a result, some kind of ‘clockwork’ is needed to convert from these optical frequencies to something slower that can be counted. The development of this clockwork presented a formidable challenge, but it was solved in the late 1990s and early 2000s by using extremely short and regular pulses of laser light to generate an evenly spaced ‘comb’ of optical frequencies [\[35\]](#sect50). The rate of pulsing can be in the microwave range, so this system features both optical and microwave frequencies. Furthermore, they are related in such a way that an unknown optical frequency (such as one generated by an optical atomic clock) can be ‘read off’ in the microwave domain. In this way, a frequency comb can function as a type of ‘ruler’, allowing the output from an optical atomic clock to be counted. This advance has allowed optical clocks to overtake the performance of the more technologically mature microwave clocks. As a result, optical clocks can now reach uncertainties of one part in $10^{18}$ – in other words, about 1 second every 30 billion years (longer than double the estimated age of the universe) [\[36\]](#sect51).

## 2.15 Future prospects for magnetometers and timing

With significant successes in the last 20 years, quantum magnetometry is a rapidly expanding field. The enhancement in sensitivity over conventional solutions and newly emerging applications has created significant commercial interest in this area of quantum technology, including biomedical MEG applications.

As with most sensor technologies, the pursuit of reduced size, weight, cost and power consumption, as well as improved performance characteristics, are key to enhancing the current application of quantum magnetometers and clocks, as well as finding new use cases. Tailoring quantum magnetometers to specific use cases is key to fully realising their advantages over their conventional counterparts.

In the context of timekeeping, given that optical atomic clocks can now significantly outperform their microwave counterparts, including those clocks that define the duration of a second, the future redefinition of the second with respect to those new optical clocks seems inevitable.

Even though the current performance of atomic clocks is astounding, it is interesting to ask whether it can be pushed still further. One (currently theoretical) device that may do this is the nuclear clock. Instead of deriving a frequency from the changing energy state of electrons in atoms, this type of clock would use a changing energy state in the nuclei of thorium atoms. The key advantage of this would come from the fact that the nucleus is much smaller than the atom as a whole, and so would be much less disturbed by interactions with its environment, such as background magnetic and electric fields, resulting in an even lower uncertainty: roughly one part in 1019 [\[37\]](#sect52).

## Summary

Well done! You have now reached the end of this week’s Study – Week 2: Quantum sensors part 1: Clocks and magnetometers.

## References

References

1.  [\[1\]](#sect1) Figliola, R. S. and Beasley, D. E. Theory and Design for Mechanical Measurements. 6th edn. Wiley, 2018.
2.  [\[2\]](#sect1) Morris, A. S. and Langari, R. Measurement and Instrumentation: Theory and Application. Academic Press, 2020.
3.  [\[3\]](#sect1) Degen, C. L., Reinhard, F. and Cappellaro, P. Quantum sensing. Reviews of Modern Physics, 2017, 89 (3), p. 35002.
4.  [\[4\]](#sect2) Grosz, A., Haji-Sheikh, M. J. and Mukhopadhyay, S. C. High Sensitivity Magnetometers. Springer, 2016.
5.  [\[5\]](#sect3) Kandel, E. R., Schwartz, J. H. and Jessell, T. M. Principles of Neural Science. 5th edn. McGraw-Hill Education, 2013.
6.  [\[6\]](#sect3) Lopes da Silva, F. EEG and MEG: Relevance to neuroscience. Neuron, 2013. \[Online\], 80 (5), pp. 1112–1128. Available at: www.sciencedirect.com/science/article/pii/S0896627313009203 \[accessed 25 May 2023\].
7.  [\[7\]](#sect3) Stufflebeam, S. M., Tanaka, N. and Ahlfors, S. P. Clinical applications of magnetoencephalography. Human Brain Mapping, 2009. \[Online\], 30 (6), pp. 1813–1823. Available at: www.ncbi.nlm.nih.gov/pmc/articles/PMC6870693/ \[accessed 24 May 2023\].
8.  [\[8\]](#sect3) Boon, L. I., Geraedts, V. J., Hillebrand, A. Tannemaat, M. R., Contarino, M. F., Stam, C. J. and Berendse, H. W. A systematic review of MEG-based studies in parkinson’s disease: The motor system and beyond. Human Brain Mapping, 2019, 40 (9), pp. 2827–2848.
9.  [\[9\]](#sect3) Maest, F., Cuesta, P., Hasan, O., Fernandéz, A., Funke, M. and Schulz, P. E. The importance of the validation of m/EEG with current biomarkers in alzheimer’s disease. Frontiers in Human Neuroscience, 2019, 13, p. 17.
10.  [\[10\]](#sect4) Reynolds, J. M. An Introduction to Applied and Environmental Geophysics. 2nd edn. Wiley, 2011.
11.  [\[11\]](#sect4) Lee, T. N. and Canciani, A. J. MagSLAM: Aerial simultaneous localization and mapping using earth Aˆos magnetic anomaly field. Journal of the Institute of Navigation, 2020. \[Online\], 67 (1), pp. 95–107. Available at: https://navi.ion.org/content/67/1/95 \[accessed 24 May 2005\].
12.  [\[12\]](#sect5) Bason, M. G., Coussens, T., Withers, M., Abel, C., Kendall, G. and Kroger, P. Non-invasive current density imaging of lithium-ion batteries. Journal of Power Sources, 2022. \[Online\], 533, p. 231312. Available at: www.sciencedirect.com/science/article/pii/S0378775322003251 \[accessed 24 May 2023\].
13.  [\[13\]](#sect5) Kosmas, K., Sargentis, C., Tsamakis, D. and Hristoforou, E. Non-destructive evaluation of magnetic metallic materials using hall sensors. Journal of Materials Processing Technology, 2005, 161 (1–2), pp. 359–362.
14.  [\[14\]](#sect6) Fagaly, R. Superconducting quantum interference device instruments and applications. Review of Scientific Instruments, 2006, 77 (10), p. 101101.
15.  [\[15\]](#sect6) Feynman, R., Leighton, R. B. and Sands, M. The Schrödinger equation in a classical context: A seminar on superconductivity. In: Feynman, R., Leighton, R. B., Sands, M. The Feynman Lectures on Physics, vol. III ch. 21. \[Online\]. Available at: www.feynmanlectures.caltech.edu/III 21.html \[accessed 24 May 2023\].
16.  [\[16\]](#sect6) Cardiff University Psychology. MEG scanner - Cardiff University Brain Research Imaging Centre, 2016. \[online video\]. Available at: www.youtube.com/watch?v=uwxR3wEeZnM \[accessed 24 May 2023\].
17.  [\[17\]](#sect6) Cohen, D. Magnetoencephalography: Evidence of magnetic fields produced by alpha-rhythm currents. Science, 1968. \[Online\], 161 (3843), pp. 784–786. Available at: www.science.org/doi/abs/10.1126/science.161.3843.784 \[accessed 24 May 2023\].
18.  [\[18\]](#sect7) Happer W. and Van Wijngaarden, W. A. An optical pumping primer. Hyperfine Interactions, 1987. \[Online\], 38 (1), pp. 435–470. doi:10.1007/BF02394855 \[accessed 24 May 2023\].
19.  [\[19\]](#sect7) Kominis, I. K., Kornack, T. W., Allred, J. C. and Romalis, M. V. A subfemtotesla multichannel atomic magnetometer. Nature, 2003. \[Online\], 422 (6932), p. 596. Available at: www.nature.com/articles/nature01484 \[accessed 24 May 2023\].
20.  [\[20\]](#sect7) Brookes, M. J., Leggett, J., Rea, M., Hill, R. M., Holmes, N., Boto, E. and Bowtell, R. Magnetoencephalography with optically pumped magnetometers (OPM-MEG): the next generation of functional neuroimaging. Trends in Neurosciences, 2022. \[Online\], 45 (8), pp. 621–634. Available at: www.cell.com/trends/neurosciences/abstract/S0166-2236(22)00102-3 \[accessed 24 May 2023\].
21.  [\[21\]](#sect7) Wellcome Trust. Designing a new brain scanner (MEG), 2018 \[online video\]. Available at: https://www.youtube.com/watch?v=Hx7\_SlvWmEs \[accessed 24 May 2023\].
22.  [\[22\]](#sect7) Tierney, T. M., Holmes, N., Mellor, S., López, J. D., Roberts, G., Hill, R. M., Boto, E., Leggett, J., Shah, V., Brookes, M. J., Bowtell, R. and Barnes, G. R. Optically pumped magnetometers: From quantum origins to multi-channel magnetoencephalography. Neurolmage, 2019. \[Online\], 199, pp. 598–608. Available at: www.sciencedirect.com/science/article/pii/S1053811919304550 \[accessed 24 May 2023\].
23.  [\[23\]](#sect7) Budker D. and Kimball, D. F. J. Optical Magnetometry. Cambridge University Press, 2013.
24.  [\[24\]](#sect8) WebsEdge Science. QZabre: Quantum Scanning Microscopy, 2021 \[online video\]. Available at: www.youtube.com/watch?v=wTntp4NEuiY \[accessed 24 May 2023\].
25.  [\[25\]](#sect8) Maze, J. R., Stanwix, P. L., Hodges, J. S., Hong, S., Taylor, J. M., Cappellaro, P., Jiang, L., Dutt, M. V. G., Togan, E., Zibrov, A. S., Yacoby, A., Walsworth, R. L. and Lukin, M. D. Nanoscale magnetic sensing with an individual electronic spin in diamond. Nature, 2008. \[Online\], 455, (7213), pp. 644–647. Available at: www.nature.com/articles/nature07279 \[accessed 24 May 2023\].
26.  [\[26\]](#sect8) Taylor, J. M., Cappellaro, P., Childress, L., Jiang, L., Budker, D., Hemmer, P. R., Yacoby, A., Walsworth, R. and Lukin, M. D. High-sensitivity diamond magnetometer with nanoscale resolution. Nature Physics, 2008. \[Online\], 4 (10), pp. 810–816. Available at: www.nature.com/articles/nphys1075 \[accessed 24 May 2023\].
27.  [\[27\]](#sect9)Pethick C. J. and Smith, H. Bose-Einstein Condensation in Dilute Gases. 2nd edn. Cambridge University Press, 2008.
28.  [\[28\]](#sect10)Major, F. G. The Quantum Beat: Principles and Applications of Atomic Clocks. Springer, 2007.
29.  [\[29\]](#sect10) Poli, N., Oates, C. W., Gill, P. and Tino, G. M. Optical atomic clocks. Atomic Physics, 2014. \[Online\], 36 (12), pp. 555–624. Available at: http://arxiv.org/abs/1401.2378 \[accessed 24 May 2023\].
30.  [\[30\]](#sect10) Heavner, T. P., Donley, E. A., Levi, F., Costanzo, G., Parker, T. E., Shirley, J. H., Ashby, N., Barlow, S. and Jefferts, S. R. First accuracy  
     evaluation of NIST-f2. Metrologia, 2014. \[Online\], 51 (3), pp. 174–182. Available at: https://iopscience.iop.org/article/10.1088/0026-1394/51/3/174 \[accessed 24 May 2023\].
31.  [\[31\]](#sect10) BIPM. The International System of Units (SI), n.d. \[Online\]. Available at: www.bipm.org/en/measurement-units \[accessed 24 May 2023\].
32.  [\[32\]](#sect11) Valat D. and Delporte, J. Absolute calibration of timing receiver chains at the nanosecond uncertainty level for GNSS time scales monitoring. Metrologia, 2020. \[Online\], 57 (2), p. 25019. Available at: https://iopscience.iop.org/article/10.1088/1681-7575/ab57f5 \[accessed 24 May 2023\].
33.  [\[33\]](#sect12) National Institute of Standards and Technology, Everyday time and atomic time, part 3, Taking Measure Just a Standard Blog. 14 April 2021. \[Online\]. Available at: www.nist.gov/blogs/taking-measure/everyday-time-and-atomic-time-part-3, 2015 \[accessed 24 April 2023\].
34.  [\[34\]](#sect13) Cohen-Tannoudji, C., Diu, B. and Laloë, F. Quantum Mechanics. Wiley, 1977.
35.  [\[35\]](#sect14) Udem, T., Reichert, J., Holzwarth, R. and Hänsch, T. W. Accurate measurement of large optical frequency differences with a mode-locked laser. Optics Letters, \[Online\], 24 (13), p. 881. Available at: https://opg.optica.org/abstract.cfm?URI=ol-24-13-881 \[accessed 24 May 2023\].
36.  [\[36\]](#sect14) Nemitz, N., Gotoh, T., Nakagawa, F., Ito, H., Hanado, Y., Ido, T., and Hachisu, H. Absolute frequency of 87Sr at 1.8 × 10−16 uncertainty by reference to remote primary frequency standards. Metrologia, \[Online\], 58 (2), 025006. Available at: https://iopscience.iop.org/article/10.1088/1681-7575/abc232#:~:text=Optical%20clocks%2C%20frequency%20standards%20that,constants%20%5B1%E2%80%936%5D \[accessed 24 May 2023\].
37.  [\[37\]](#sect15) Fan, H., Kumar, J. S., Kübler, H., Shaya K. and Shaffer, J. P. Atom based RF electric field sensing. Journal of Physics B: Atomic, Molecular and Optical Physics, \[Online\], 48 (20), 202001. Available at: https://iopscience.iop.org/article/10.1088/0953-4075/48/20/202001 \[accessed 24 May 2023\].

Image credits

EPSTOCK/Shutterstock (home page image)

Manuel/Unsplash Free to use under the Unsplash License. https://unsplash.com/photos/CANL3bzp6wU