## Week 4: Quantum communication: Study

## 4: Quantum communication

## Introduction

This Study section will guide you through the key concepts of this week’s topics. You may leave and return to it as you see fit. You are encouraged to take notes as you work through, pulling out key ideas, questions or challenges you have.

With ever increasing volumes of stored, processed and transmitted information, secure communication is of paramount interest across many sectors of business and public life. Consequently, a lot of effort has always been made to encrypt sensitive messages in ways that mean intercepting messages is difficult. Quantum physics enables a step change in the technology to do this, in that it provides tools that prevent unnoticed eavesdropping on a communication line on fundamental grounds.

 The Study topics this week are: 

-   [4.1 Encoding in quantum communication](#sect1)
-   [4.2 Quantum communication protocols](#sect2)
-   [4.3 Overview of technology implementation](#sect3)
-   [4.4 Key sectors](#sect4)
-   [4.5 Timeline of quantum communication](#sect5)

## 4.1 Encoding in quantum communication

Quantum communication is rooted in the same core ideas as classical communication. Classical information is encoded in the form of bits, where a bit can be in state 0, or state 1. Quantum communication differs in the fundamental unit of information by using a quantum bit, or qubit [\[1\]](#sect6). The qubit can be 0 or 1, but can also be in state 0 and state 1 at the same time. If white is 0 and black is 1, then there is a grey state that the qubit can be in (as depicted in Figure [4.1](#fig4.1)). 

Figure 4.1: Classical bit compared to a quantum bit.

Long description

A representation of a standard (classical) bit on the left hand side of the image. There are two boxes representing the two possible states of the bit. One is a white box with a ‘0’ in it, the other a **dark blue** box with a ‘1’ in it. On the right hand side, the same two boxes are shown, but now a larger **green** area links the two with the label ‘0 and 1’, illustrating the possibility of a quantum superposition state of a qubit.

Being in two states at the same time is called a superposition. The Schrödinger cat state hypothesis is where a cat is simultaneously alive and dead until the box is opened [\[2\]](#sect7). The superposition property is very important for quantum communication. The qubit is therefore considered better than the bit used in classical communication because of the added possibilities that a single qubit can have and the ability to transfer more information with fewer qubits than the classical analogue.

The qubit comes in many forms, just like a classical bit can be a punch (or no punch) in a card, or a dent in the surface of a CD [\[1\]](#sect6). Some of the physical forms qubits take will be discussed later in this study section, and in later weeks of this course.

**Quantum key distribution (QKD)**

Consider the situation where there is an encoder of the quantum bits, called Alice, and a receiver of the quantum bits, Bob. They are connected by a quantum channel, and have a classical communication channel to discuss results. If you want to keep a message secret in a classical communication channel, you may use a secret code but this can be cracked. In recent years, cyber attacks have increased in frequency with more sophisticated computers and cracking algorithms, and the development of quantum computers that could crack the codes quicker [\[3\]](#sect8). In quantum communication, a key is also needed to have secure information and the cryptography protocol of making this key is called quantum key distribution (QKD). Properties of quantum mechanics mean quantum mechanics is inherently more secure than the classical method because of its randomness and the key is only known to Alice and Bob.

An eavesdropper that has access to both communication channels, called Eve, is considered in the cryptography protocols (depicted in Figure [4.2](#fig4.2)). Due to quantum mechanics theorems, the listener has restrictions on how they can intercept the qubits.

Figure 4.2: Alice and Bob are connected by two channels, a quantum channel communicating with qubits and a classical channel communicating with bits. Eve can eavesdrop on both channels.![Diagram representation of Alice and Bob connected by a quantum and a classical channel. Long description follows.](https://canvas.sussex.ac.uk/courses/42093/files/6842104/preview)

Long description

Alice and Bob are represented by different coloured rectangles on the left-hand and right-hand side of the image, respectively. A broad arrow labelled ‘quantum channel’ points from Alice to Bob, a thinner bidirectional arrow labelled ‘classical channel’ also links Alice and Bob. A central oval represents Eve in the centre of the schematic, sandwiched in between the two arrows.

**No-cloning theorem**

The no-cloning theorem states that it is impossible to make an exact copy of an unknown quantum state [\[4\]](#sect9).

**Quantum mechanics explanation**

Suppose there is an unknown quantum state $| \phi \rangle = \alpha |0 \rangle + \beta |1 \rangle$ and a unitary operator $U_{\textrm{cl}}$ that can clone the state. Due to linearity, the unitary operator should give the same result for the following operations,

$$U_{\textrm{cl}}(| \phi \rangle |0 \rangle ) = | \phi \rangle | \phi \rangle  = (\alpha |0 \rangle + \beta | 1 \rangle)(\alpha |0 \rangle + \beta | 1 \rangle) = \alpha^2| 00 \rangle + \alpha \beta |01 \rangle + \beta \alpha |10 \rangle + \beta^2 |11 \rangle$$

$$U_{\textrm{cl}}(| \phi \rangle |0 \rangle ) = U_{\textrm{cl}} (\alpha |0 \rangle + \beta | 1 \rangle)|0 \rangle = U_{\textrm{cl}}\alpha| 00 \rangle + U_{\textrm{cl}}\beta |10 \rangle = \alpha |00 \rangle + \beta |11 \rangle$$

The results in Eq. [4.1](#uni1)  and [4.2](#uni2)  are incompatible, the second calculation does not have any cross terms, therefore there is no unitary operator that can clone a quantum state.

**Analogy explanation**

In the classical world, if you want to make a copy of a picture or a document, you can use a photocopier and print out an exact copy of the information. To think of this process in more detail, the copying machine turns the paper and ink in the printer into a copy of the picture. This applies in the quantum world too; you have to change a quantum state into the unknown information. In fact the process of changing one quantum state into another correctly every time fundamentally does not exist in quantum mechanics, therefore this is a proof of the no-cloning theorem [\[4\]](#sect9). The no-cloning theorem has implications for the listener Eve, because they cannot copy the information. Instead, they have to intercept the qubit and send a fake one. Or the qubit has to be measured then sent on to Bob. This allows Alice and Bob to perform a check on the qubits and find out if the information was compromised.

## 4.2 Quantum communication protocols

**BB84**

The first cryptography protocol written for quantum communication was in 1984 by Charles Bennett and Gilles Brassard called BB84 [\[5](#sect10), [6\]](#sect11). This protocol uses a photon as the qubit, and four states that are given by the polarisation of the photon. Photons from a source (it doesn’t matter if the photons are originally polarised or unpolarised) are passed through a polarising filter. There are two orthogonal bases that are used in BB84, as shown in Figure [4.3](#bb84filter). 

Figure 4.3: Photon polarisation before and after being passed through a rectilinear filter.

Long description

At the top of this diagram, there are two sets of two orthogonal double-headed arrows, one parallel/orthogonal to the page, the other rotated by 45 degrees. Also shown are two corresponding coordinate system choices in Horizontal/Vertical and ±45◦ basis, respectively. At the bottom of this diagram to the left, a horizontally polarised photon is depicted as a horizontal double-headed arrow that passes in horizontal/vertical direction. At the bottom of this diagram to the right, a horizontally polarised photon is depicted as a horizontal double-headed arrow that passes in horizontal/vertical direction. At the bottom of this diagram to the left, a diagonally linearly polarised photon is depicted as double-headed arrow at a 45-degree angle that passes through the same filter (depicted in the same way as before). In this case the output is a horizontally or vertically polarised photon with equal probability and is depicted as two double-headed arrows next to each other, one oriented in horizontal, the other in vertical orientation.

 A classical bit is assigned to the two directions in each basis, and both Alice and Bob know the conversion. This protocol is implemented as follows:

1.   Alice chooses a random string of bits and random bases to apply to the bits. The qubits are sent over the quantum channel and Bob detects them. Bob also chooses random bases to apply to the detected photons and records his answer. If Bob guesses the same basis as Alice then the bit will be correct, highlighted in Table [4.1](https://canvas.sussex.ac.uk/courses/42093/pages/week-4-quantum-communication-study#fig:table_BB84_principle) with the background checked pattern. If the basis was wrong, highlighted in Table with the background vertical striped pattern, then Bob will get a random bit as his answer. The random bits are highlighted in Table with the background solid colour.  
    
    Table 4.1: Table illustrating a possible bit sequence in the BB84 protocol 1 and basis choices with the resulting secure key generation. Adapted from Bennett and Brassard, p. 178 [\[7\]](#sect12).
    
    Long description
    
    This table has seven columns. The first column has the heading of ‘Quantum transmission’ and the remaining six columns to the right of the first column have the heading of ‘Resulting secure key generation’. The first-row cell in the ‘Quantum transmission’ column has the title ‘Alice bits’. In the six respective cells to the right of the ‘Alice bits’ cell, they contain the numbers of 1, 0, 1, 0, 0 and 1. The second-row cell in the ‘Quantum transmission’ column has the title ‘Alice basis’. In the six respective cells to the right of the ‘Alice basis’ cell, they contain the letters of D, R, R, R, D and D. The third-row cell in the ‘Quantum transmission’ column has the title ‘Alice sends’. In the six respective cells to the right of the ‘Alice sends’ cell, they contain the symbols and numbers of -, H, V, H, + and -. The fourth-row cell in the ‘Quantum transmission’ column has the title ‘Bob basis’. In the six respective cells to the right of the ‘Bob basis’ cell, they contain the letters of D, D, D, R, D and R. The fifth-row cell in the ‘Quantum transmission’ column has the title ‘Bob measures’. In the six respective cells to the right of the ‘Bob measures’ cell, they contain the symbols of -, -, V, H, + and +. In this row, the 2nd, 3rd and 6th cells (containing the symbols of -, V and + respectively) have a solid coloured background. The sixth-row cell in the ‘Quantum transmission’ column has the title ‘Bob receives’. In the six respective cells to the right of the ‘Bob receives’ cell, they contain the numbers of 1, 1, 1, 0, 0, 0. In this row, the 2nd, 3rd and 6th cells (containing the numbers of 1, 1 and 0) have a solid coloured background. The seventh-row cell in the ‘Quantum transmission’ column has the title ‘Compare bases’. In the six respective cells to the right of the ‘Compare bases’ cell, there are no numbers or symbols within each cell (they are all blank). In this row, the 1st, 4th and 5th cells have a checked pattern background, the 2nd, 3rd and 6th cells have a vertical striped background. The eighth-row cell in the ‘Quantum transmission’ column has the title ‘Secret Key’. In the six respective cells to the right of the ‘Secret key’ cell, there are no numbers or symbols within the 2nd , 3rd and 6th cells (they are blank). In this row, the 1st cell has the number 1, the 4th and 5th cells have the number 0.
    
 2.   Over the classical channel, Bob tells Alice the basis that was used for each qubit. Alice tells Bob which ones were the same, and they both mark down those bit results, ignoring the wrong basis bits. The results are the key, and Alice and Bob have the exact same list.  
    
    Figure 4.4: BB84 channel configuration.![Depiction of a BB84 channel configuration with Alice and Bob. Long description follows current section.](https://canvas.sussex.ac.uk/courses/42093/files/6842106/preview)
    
    Long description
    
    Alice and Bob are shown as two rectangular blocks in different colours. They are connected through a classical communication channel depicted at the bottom of the image as a double-headed arrow and another arrow from Alice to Bob, depicting a quantum channel. A set of four double-headed arrows in horizontal, vertical and the two diagonal orientations are shown inside the quantum channel arrow, illustrating the possible photon states. Eve as possible eavesdropper is shown as an oval in the centre of the image in between Alice and Bob and in between the two arrows representing the communication channels.
    
 3.  To check for a listener Eve, Bob tells Alice a result from the key, sacrificing the security of that information. Eve cannot make a copy due to the no-cloning theorem so has to take the photon, send it through their random basis, and then send it to Bob. This will change the photon polarisation if Eve guesses wrong, so Bob will not get the same key bit as Alice. Any wrong key results alert them to a listener in the channels and they stop communication. This is shown with a few examples in Table [4.2](#fig:table_BB84_listener).  
    
    Table 4.2: Possible consequences of an eavesdropper ‛Eve’ intercepting a key sent from Alice to Bob, thereby necessarily altering some bits, which will reveal their interception.![Secure key generation for ‘Eve’ intercepting a key sent from Alice to Bob. Long description follows current section.](https://canvas.sussex.ac.uk/courses/42093/files/6842115/preview)
    
    Long description
    
    This table has seven columns. The first column has the heading of ‘Quantum transmission’ and the remaining six columns to the right of the first column has the heading of ‘Resulting secure key generation’. The first-row cell in the ‘Quantum transmission’ column has the title ‘Alice bits’. In the six respective cells to the right of the ‘Alice bits’ cell, they contain the numbers of 0, 1, 1, 0, 1 and 1. The second-row cell in the ‘Quantum transmission’ column has the title ‘Alice basis’. In the six respective cells to the right of the ‘Alice basis’ cell, they contain the letters of D, R, D, R, R and R. The third-row cell in the ‘Quantum transmission’ column has the title ‘Alice sends’. In the six respective cells to the right of the ‘Alice sends’ cell, they contain the symbols of +, V, -, H, V and V. The fourth-row cell in the ‘Quantum transmission’ column has the title ‘Eve basis’. In the six respective cells to the right of the ‘Eve basis’ cell, they contain the letters of D, D, R, D, R and D. The fifth-row cell in the ‘Quantum transmission’ column has the title ‘Eve receives’. In the six respective cells to the right of the ‘Eve receives’ cell, they contain the symbols of +, -, V, -, V and +. The sixth-row cell in the ‘Quantum transmission’ column has the title ‘Bob basis’. In the six respective cells to the right of the ‘Bob basis’ cell, they contain the letters of D, R, R, D, D and R. The seventh-row cell in the ‘Quantum transmission’ column has the title ‘Bob measures’. In the six respective cells to the right of the ‘Bob measures’ cell, they contain the symbols of +, H, V, -, + and H. The eighth-row cell in the ‘Quantum transmission’ column has the title ‘Bob receives’. In the six respective cells to the right of the 'Bob receives’ cell, they contain the numbers of 0, 0, 1, 1, 0 and 0. The ninth-row cell in the ‘Quantum transmission’ column has the title ‘Secret key’. In the six respective cells to the right of the ‘Secret key’ cell, they contain the numbers of 0, 0, 1, 1, 0 and 0. In this row, the 1st, 2nd and 6th cells have a checked pattern background, the 3rd, 4th and 5th cells have a vertical striped background. The final row in ‘Quantum transmission’ column has no title and all the cells in this row are blank, except for the 2nd and 6th cell that contains the symbol of !.
    

This protocol relies on probability, so there is a small probability that Eve guesses all the bases correctly and Alice and Bob cannot detect their presence in the channels. The protocol relies on a perfect channel for the qubits; error in the channel causes the results to not be the same and makes it harder to detect a listener.

**B92**

Bennett went on to write another protocol in 1992 called B92 that uses two polarisations of light only [\[8\]](#sect13). This is simpler, with bit 0 being horizontal polarisation, and bit 1 being +45° polarisation.

1.  Alice sends photons with random bases; if linear is used then it has to be 0, and diagonal is 1. Bob also uses a random basis and measures the polarisation. Bob can therefore work out the bit that was sent for certain cases, and discards ambiguous results. This is depicted in Table [4.3](#e91_table).  
    
    Table 4.3: B92 protocol [\[8\]](https://canvas.sussex.ac.uk/#sect13): All possible basis combinations between Alice and Bob with the corresponding resulting measurement results on Bob's receiving end. Only for equal basis choices are these results unique. Adapted from Bennett p. 3121 .
    | Alice basis | Bob basis | Bob polarisation |
    | --- | --- | --- |
    | R | R | H |
    | D | R | V or H |
    | R | D |  \+ or - |
    | D | D | + |
    
    There are two possible combinations to get horizontal polarisation but only choosing opposite bases gives the vertical polarisation. Similarly for measuring -45°. 
    
2.   Bob tells Alice which photons they measured the results V or - and they discard the other results.
 3.   To check for a listener they share a few of the bits they recorded to check they agree, the same as BB84. If a listener was interrupting the quantum channel then Eve has a 75% chance for each measurement that they are detected.

**E91**

Written by Artur Ekert in 1991, this protocol was the first to consider entangled particles and the violation of Bell’s inequality to confirm a listener Eve in the quantum channel [\[9\]](#sect14). Entanglement is a phenomenon in the quantum world that does not exist in the classical world. If two particles are entangled, measuring a property of one of the particles instantly determines a property of the other particle. It doesn’t matter about the distance of the particles, the information will be instantly known once a measurement has been made. In Ekert’s paper, he uses two entangled particles where one is sent to Alice and one to Bob. This is illustrated in Figure [4.5](#e91) .

Figure 4.5: E91 channel configuration.

Long description

Alice and Bob are depicted as different coloured rectangular boxes on the left and right hand side of the image, respectively. They are connected through a classical channel depicted as black double-headed arrow and a quantum channel depicted as orange double-headed arrow with entangled particles added as dots inside the arrow. A potential eavesdropper Eve is shown as red oval in the centre of the image between Alice and Bob and between the two arrows.

 

E91 is built on BB84 as well, so Alice and Bob choose random bases to make their measurements, for example, choosing linear or diagonal polarisation filter. Afterwards they discuss which ones they used and the ones that were the same are used in the key. The source is in a public quantum channel, so Eve could intercept the particle, measure it and send it on, or send in a different particle. However, how they check the channel is secure is based on the probabilities of the results they measured. They don’t have to sacrifice some of their key results outright to the public channel. Instead, Alice and Bob test one of Bell’s inequalities. The CHSH inequality, in Eq. 4.3, is the addition of expectation values from their measurements on the particles,

$$
|\langle ab \rangle + \langle AB \rangle + \langle aB \rangle - \langle Ab \rangle | \leq 2
$$
(4.3)

where Alice could make measurement A or a, and Bob B or b. Alice and Bob expect their measurements to violate the inequality and give greater than 2, $2\sqrt2$ if the entanglement is perfect [\[10](#sect15), [11](#sect16), [12\]](#sect17). They will measure less than 2 if Eve has measured the particle before sending on. Eve could give entangled particles, but they will gain no information from doing this.

Here we have discussed three of the more well-known protocols, and these are the base for many other protocols that have been published and used, such as SARG04, BBM92, and superdense coding [\[13\]](#sect18). These are all discrete-variable quantum key distribution DV-QKD, for example, where the measurement gives defined results of horizontal or vertical polarisation. There are many protocols that apply the BB84 and E91 protocols to continuous-variable quantum key distribution CV-QKD, which measures the quadrature of the electric field instead. The CV-QKD can be integrated with classical communication channels, which makes them more attractive to scientists [\[14\]](#sect19).

## 4.3 Overview of technology implementation

Now let’s look at how and where quantum communication is being used and developed today.

**Quantum hardware**

The protocols of how secure quantum communication can be carried out have been developed, but in order for quantum communication to be used in everyday life, there needs to be a quantum network. Direct communication between the end-nodes, Alice and Bob, is the simplest quantum network but this has limited uses and separation distance. Classical communication uses amplifiers to reduce the loss of information, but these cannot be used for entangled states and quantum bits [\[1\]](#sect6). The development of quantum repeaters is therefore an important step in having a more complex quantum network. The aim of a quantum repeater is to amplify the signal and contain quantum memory, where the state of the qubits is stored. The classical equivalent of quantum memory would be the cache memory; the quantum memory would be used to speed up communication between multiple end-nodes. Amplifying the signal might include quantum purification, a process of making a more highly entangled state so the state lasts longer and reaches the end-node. Due to losses in the quantum line, just like classical communication, if Alice sends a horizontally polarised photon, it might not be completely horizontal when it reaches Bob and this error will be detected when the measurement is done. There are many proposed ways of purifying the signal but the challenge is having the repeater work 100% of the time.

Figure 4.6: Simple schematic of a quantum network.!

Long description

Two end-nodes (Alice and Bob) are depicted as different coloured rectangles, connected through a central repeater (indicated as a white box containing the text 'Node repeated or switch') by arrows.

The arrow pointing from end-node (Alice) to the central repeater is labelled Optical fibre, seawater, atmosphere.  The arrow pointing from the central repeater to end-node (Bob) have the '...and more nodes' written above it.

Related to the quantum network but not mentioned in Figure [4.6](#network) is the interfacing with quantum computers, sensors and even interfacing with the current classical systems. This is an important part of how the user will be part of the quantum network, and is called the quantum internet [\[15\]](#sect20). Depending on the quantum channel, there is a finite distance that the qubits can be transported before a repeater is needed. Some of the possible quantum channels are:

  

-   **Optical fibre systems**  
    Optical fibres are preferred in classical communication because of the large bandwidth and can transfer light over longer distances than electrical signals. They are also faster, lighter and more secure than other cables, such as copper. There are multiple papers that discuss the use of classical and quantum cores in the same optical fibre, which can take advantage of current infrastructure. Optical fibres for the transport of photons have been shown to work in the laboratory. In 2021, scientists at the University of Cambridge working with Toshiba demonstrated quantum communication over 600 km in the laboratory [\[16\]](#sect21). They implemented a repeater-like part to improve the phase stabilisation, which is the main loss in optical fibres, where Alice sends the information to Charlie, and Charlie then sends it to Bob. The losses were still high but the method they used of using two reference signals (Twin-Field QKD) was shown to be tolerable with the losses, and extend the distance the qubits can be distributed before they are undetectable. This is the furthest so far with optical fibres but far from what is needed to connect the world.

  

-   **Free space system**  
    For mobile devices, fixed position fibre optics systems are not ideal, so quantum communication through free space, for example through the atmosphere, has been investigated. Free space channels have some advantages over optical fibres, being cheaper, less fragile, and having smaller losses for distances larger than 70km. However, the added complexity of propagation through a fluid, such as turbulence, thermal fluctuations and scattering, means there are many limitations to overcome [\[17\]](#sect22). There is also an amount of background noise that will need to be accounted for that is not present in optical fibres. Free space can include the atmosphere but also could be seawater: an obvious choice covering 70% of the Earth's surface. It has been demonstrated that entangled photons can be transferred in seawater and well enough for quantum communication purposes [\[18\]](#sect23).

  

-   **Satellite-based system**  
    This is an example of free space quantum communication using satellites and stations on Earth to create the quantum channel. In the vacuum of space above the Earth’s atmosphere, the losses due to attenuation reduce to nearly zero. Alice and Bob are on Earth and communicate through Charlie on a satellite. In a real-life satellite network, there might be inter-satellite communication with more satellites in orbit, and there can be a large network of optical fibre channels on Earth. Such a quantum network will span thousands of kilometres [\[19\]](#sect24). Satellite quantum networks come at a price to the bandwidth that can be achieved; optical fibres can transfer gigabits per second and satellites are currently transferring kilobits per second. However, the distances satellites cover are practically impossible with an optical fibre without a relay or repeater-like part, so this is a significant improvement. Scientists predict that it will take more than 10 years before satellites can reach Gb/s, but specialist satellites for quantum communication have already been launched, such as Micius in 2016, and there are many plans across the world for satellite-based quantum communication networks [\[20\]](#sect25).

## 4.4 Key sectors

**Financial transactions**

The financial sector has a keen interest in quantum communication because of the layers of security that the quantum key distribution (QKD) presents. The transfer of card numbers and client data can be performed securely with the quantum channel. Also, many one-time passwords can be created by the QKD and dispensed to customers. This technology is being developed and it is hoped that it will be rolled out commercially in the next 10 years, whereas the distribution of the QKD wirelessly and over fibre networks has been implemented on the small scale. There are numerous projects ongoing for quantum communication in the finance sector, such as the OPENQKD project bringing together many banks, quantum communication companies and university research groups. In 2022, researchers from Denmark's Technical University in collaboration with Danske Bank successfully performed a bank transfer with a continuous variable quantum key distribution over the classical current fibre optic network [\[21\]](#sect26). This was an important result from the ongoing project, supported by Innovation Fund Denmark, between DTU and other organisations in Denmark, and Danske Bank. This was performed out of the lab between two Danske Bank computers, but was closely controlled by scientists from DTU. The clear next step would be autonomous CVQKD for bank transfers.

**Health records**

In the last decade there have been many cases of high profile data breaches from cyber attacks in the healthcare sector. For example, in 2015, 80 million records from the US company Anthem were stolen [\[22\]](#sect27), and 239 incidents were reported in the NHS between June and October 2016 [\[23\]](#sect28). With fewer paper-based health records and so many healthcare professionals needing to access records, creating more weak points, the need for protection is becoming more critical. Medical records also need to be transferred between locations securely for better healthcare for individuals. The main focus for the health sector is to use quantum technology to protect from cyber attacks now, and in the future with the development of quantum computers that have the potential to break current classical encryption. Integration into the current communication channels could include using random number generators for the QKD or local quantum channels in a medical facility. A larger quantum network that connects between locations is a longer term goal.

**Protecting infrastructure**

Similarly, cyber attacks have been focused on infrastructure in the last decade, such as on the power grids, oil refineries and water filtration systems. Data needs to be transferred for infrastructure to work efficiently, and random number generation can provide better encryption for the data. In 2019, research by Oak Ridge and Los Alamos national laboratories on the EPB Chattanooga power facility in Tennessee demonstrated using QKD to test for a listener. Researchers indicated that this shows the quantum communication works on the current infrastructure but is many years away from being implemented as the sole communication [\[24\]](#sect29). The more secure communication that quantum communication provides is also important for e-government, or electronic government, which is the use of technology for public services. Government services that are being digitised, such as tax forms, license applications and documents, need protection from cyber attacks.

**E-commerce**

The buying and selling of goods and services would benefit from the added protection that quantum communication provides, as it involves the transfer of money and private information. QKD protocols have been applied to e-commerce specifically, such as what happens if the order is cancelled, and preparing multiple sets of qubits for an order and shipping information.

## 4.5 Timeline of quantum communication

What has been achieved up to today and what will be developed in the next 10 years in quantum communication will be explored in the following sections. Quantum random number generators (QRNG) have been commercially available since 2010 and there are numerous companies creating quantum random number generators [\[25\]](#sect30). They are used to enhance security in classical systems and provide more security than the pseudorandom sequences from classical methods. QRNGs available today are trusted devices and are based off models of quantum processes, but they do contain noise, which means they do not meet the requirements for some quantum communication networks and protocols. Some are self-testing QRNG, which test Bell’s inequalities, making the generator typically slower and more expensive. No commercially available generators are based on quantum entanglement (as of 2023), which can be attributed to cost, slow speeds, and difficulty of implementing entanglement effectively. In the future, the technology will allow for faster bit rates and make the QRNG based on quantum entanglement more affordable. Miniaturisation is also a key area of research from QRNG so that they can be applied to chip-based quantum communication.

Demonstrations of quantum communication with a trusted classical repeater. These are not true quantum networks:

-   In 2010, a secure TV conference was held using a trusted QKD in Japan, between Koganei and Otemachi, 45 km away [\[26\]](#sect31).

-   In 2015, an entanglement QKD was demonstrated across buildings at the Delft University of Technology; the distances were 1280 m, 463 m and 816 m. They carried out some of the simpler tasks such as communicating strategies to win an online game [\[27\]](#sect32).

-   In 2016, the first satellite Micius demonstrated QKD in free space [\[28\]](#sect33). In the five years since this, communication over thousands of km has been shown with entanglement, and more satellites with the sole use of quantum communication have been built and launched. They have been used to communicate with collaborators in Austria too.

-   In 2017, Beijing and Shanghai were connected with over 2000 km of optical fibre [\[29\]](#sect34). In the years since, it has been optimised and more nodes added, and today it covers 4600 km across China, serves banks and power grids, and is used for e-government websites.

-   In 2018, the first UK quantum network was launched in Cambridge [\[30\]](#sect35). Since then there have been more quantum networks launched in Manchester and Bristol.

Research into developing truly quantum networks is the focus for governments and funding bodies currently. The technology is not available for a quantum repeater and while aspects have been shown in the laboratory, the implementation into a large-scale network needs typically 4 years to develop. There are a number of plans to make a true quantum network in the next 10 years that are hinged on research and teaching new scientists:

-   EuroQCI is an EU-wide network that will be comprised of optical fibre networks and satellite segments, in collaboration with ESA and industry. The ground base network began work in 2023 and the satellites are to be launched in late 2024, with the aim of being operational in 2027 [\[31\]](#sect36).

-   Collaborations between countries are being established to form a quantum network, such as the UK and Canada. Canada opened new funding opportunities in 2021 to develop satellite-based communication networks [\[32\]](#sect37).

One of the main challenges that quantum communication currently faces is that quantum repeaters are outside of the current scope of physics. There is no method of amplifying the signal without measuring the quantum state and destroying the entanglement of the qubits. There has been progress in the last 5 years on quantum repeaters but nothing is near being outside of the laboratory yet [\[33\]](#sect38). Beyond the technical challenges, the cost to create a quantum network is large, and it has to gain trust from the public to become an effective line of communication [\[34\]](#sect39).

## Summary

Well done! You have now reached the end of this week’s Study – Week 4: Quantum communication.

## References

1.  [\[1\]](#sect1) Nielsen M. A. and Chuang, I. L. Quantum Computation and Quantum Information: 10th Anniversary Edition, 10th edn. Cambridge University Press, 2010.
2.  [\[2\]](#sect1) Schrödinger, E. Die gegenw artige Situation in der Quantenmechanik. Naturwissenschaften, 1935. \[Online\], 23 (48), pp. 807–812. Available at: http://hermes.ffn.ub.es/luisnavarro/nuevo\_maletin/Schrodinger\_1935\_cat.pdf \[accessed 24 May 2023\].
3.  [\[3\]](#sect1) National Institute of Standards and Technology (NIST). Computer Security Division Annual Report 2015. U.S. Department of Commerce, 2016. \[Online\]. Available: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-182.pdf \[accessed 24 May 2023\].
4.  [\[4\]](#sect1) Wootters W. K. and Zurek, W. H. A single quantum cannot be cloned. Nature, 1982, 299 (5886), pp. 802–803.
5.  [\[5\]](#sect2) Bennett C. H. and Brassard, G. Quantum cryptography: Public key distribution and coin tossing. Theoretical Computer Science, 2014. \[Online\], 560 (1), pp. 7–11. Available at:  
    https://arxiv.org/abs/2003.06557 \[accessed 24 May 2023\].
6.  [\[6\]](#sect2) Scarani, V., Bechmann-Pasquinucci, H., Cerf, N. J., Dušek, M., Lütkenhaus, N. and Peev, M. The security of practical quantum key distribution. Reviews of Modern Physics, 2009. \[Online\], 81 (3), pp. 1301–1308. Available at: https://link.aps.org/doi/10.1103/RevModPhys.81.1301 \[accessed 24 May 2023\].
7.  [\[7\]](#sect2) Bennett C. H. and Brassard, G. Quantum cryptography: Public key distribution and coin tossing. Theoretical Computer Science, 2014. \[Online\] 560. Available at: https://www-sciencedirect-com.sussex.idm.oclc.org/science/article/pii/S0304397514004241 5
8.  [\[8\]](#sect2) Bennett, C. H. Quantum cryptography using any two nonorthogonal states. Physical Review Letters, 1992. \[Online\], 68 (21), pp. 3121–3124. Available at: doi: 10.1103/PhysRevLett.68.3121 \[accessed 24 May 2023\].
9.  [\[9\]](#sect2) Ekert, A. K. Quantum cryptography based on bell’s theorem. Physical Review Letters, 1991. \[Online\], 67 (6), pp. 661–663. Available at: https://link.aps.org/doi/10.1103/PhysRevLett.67.661 \[accessed 24 May 2023\].
10.  [\[10\]](#sect2) Palacios-Laloy, A., Mallet, F., Nguyen, F., Bertet, P., Vion, D., Esteve, D. and Korotkov, A. N. Experimental violation of a bell’s inequality in time with weak measurement. Nature Physics, 2010. \[Online\], 6 (6), pp. 442–447. Available at: http://www.nature.com/articles/nphys1641 \[accessed 24 May 2023\].
11.  [\[11\]](#sect2) Rarity J. G. and Tapster, P. R. Experimental violation of bell’s inequality based on phase and momentum. Physical Review Letters, 1990. \[Online\], 64 (21), pp. 2495–2498. Available at: https://link.aps.org/doi/10.1103/PhysRevLett.64.2495 \[accessed 24 May 2023\].
12.  [\[12\]](#sect2) Ansmann, M., Wang, H., Bialczak, R. C., Hofheinz, M., Lucero, E., Neeley, M., O’Connell, A. D., Sank, D., Weides, M., Wenner, J., Cleland, A. N. and Martinis, J. M. Violation of Bell’s inequality in Josephson phase qubits. Nature, 2009. \[Online\], 461 (7263), pp. 504–506. Available at: https://pubmed.ncbi.nlm.nih.gov/19779447/ \[accessed 24 May 2023\].
13.  [\[13\]](#sect2) Lopes, M. and Sarwade, N. Cryptography from quantum mechanical viewpoint. International Journal on Cryptography and Information Security, 2014. \[Online\], 4 (2). Available at: https://arxiv.org/abs/1407.2357 \[accessed 24 May 2023\].
14.  [\[14\]](#sect2) Gehring, T., Händchen, V., Duhme, J., Furrer, F., Franz, T., Pacher, C., Werner, R. F. and Schnabel, R. Implementation of continuous-variable quantum key distribution with composable and one-sided-device-independent security against coherent attacks. Nature Communications, 2015. \[Online\], 6 (1), p. 8795. Available at: https://www.nature.com/articles/ncomms9795 \[accessed 24 May 2023\].
15.  [\[15\]](#sect3) Zhukov, A. A.,  Kiktenko, E. O., Elistratov, A. A. W., Pogosov, V. and Lozovik, Y. E. Quantum communication protocols as a benchmark for quantum computers. Quantum Information Processing, 2019. \[Online\], 18, p. 31. Available at: https://arxiv.org/abs/1812.00587 \[accessed 24 May 2023\].
16.  [\[16\]](#sect3) Pittaluga, M., Minder, M., Lucamarini, M., Sanzaro, M., Woodward, R. I., Li, M.-J., Yuan, Z. and Shields, A. J. 600-km repeater-like quantum communications with dual-band stabilization. Nature Photonics, 2021. \[Online\], 15 (7), pp. 530–535. Available at: http://www.nature.com/articles/s41566-021-00811-0 \[accessed 24 May 2023\].
17.  [\[17\]](#sect3) Pirandola, S. Limits and security of free-space quantum communications. Physical Review Research, 2021. \[Online\], 3 (1), p. 13279. Available at: https://link.aps.org/doi/10.1103/PhysRevResearch.3.013279 \[accessed 24 May 2023\].
18.  [\[18\]](#sect3) Ji, L., Gao, J,. Yang, A.-L., Feng, Z., Lin, X.-F., Li, H.-G. and Jin, X.-M. Towards quantum communication in free-space seawater. Quantum Physics, 2016. \[Online\]. Available at: https://arxiv.org/abs/1602.05047 \[accessed 24 May 2023\].
19.  [\[19\]](#sect3) Chen,Y .-A., Zhang, Q., Chen, T.-Y., Cai, W.-Q., Liao, S.-K., Zhang, J., Chen, K., Yin, J., Ren, J.-G., Chen, Z., Han, S.-L., Yu, Q., Liang, K., Zhou, F., Yuan, X., Zhao, M.-S., Wang, T.-Y., Jiang, X., Zhang, L., Liu, W.-Y., Li, Y., Shen, Q., Cao, Y., Lu, C.-Y., Shu, R., Wang, J.-Y., Li, L., Liu, N.-L., Xu, F., Wang, X.-B., Peng, C.-Z. and Pan, J.-W. An integrated space-to-ground quantum communication network over 4,600 kilometres. Nature, 2021. \[Online\], 589 (7841), pp. 214–219. Available at: http://www.nature.com/articles/s41586-020-03093-8 \[accessed 24 May 2023\].
20.  [\[20\]](#sect3) Lu, C.-Y., Cao, Y., Peng, C.-Z. and Pan, J.-W. Micius quantum experiments in space. Reviews of Modern Physics, 2022. \[Online\], 94 (3), p. 35001. Available at: doi: 10.201103/RevModPhys.94.035001 \[accessed 24 May 2023\].
21.  [\[21\]](#sect4) KPMG, Quantum-safe data transfer performed at danske bank, n.d. \[Online\]. https://kpmg.com/dk/en/home/media/press-releases/2022/02/quantum-safe-data-transfer-performed-at-danske-bank.html \[accessed 23 May 2023\].
22.  [\[22\]](#sect4) Money CNN. Anthem hack: What you need to know. CNN Money, February 2015, \[Online\]. Available at: https://money.cnn.com/2015/02/04/technology/anthem-insurance-hack-data-security \[accessed 24 May 2023\].
23.  [\[23\]](#sect4) NHS England. Lessons learned review of the wannacry ransomware cyber attack. NHS, 2018. \[Online\]. Available at: www.england.nhs.uk/wp-content/uploads/2018/02/lessons-learned-review-wannacry-ransomware-cyber-attack-cio-review.pdf \[accessed 24 May 2023\].
24.  [\[24\]](#sect4) Puketza, P., Chiang, P. and Jackson, K. Quantum-safe cryptography for the grid: Cybersecurity for distributed energy resources. US Department of Energy Office of Scientific and Technical Information, 2019. \[Online\]. Available at: https://www.osti.gov/biblio/1607136 \[24 May 2023\].
25.  [\[25\]](#sect5) Jacak, M. M., Józwiak, P., Niemczuk, J. and Jacak, J. E. Quantum generators of random numbers. Scientific Reports, 2021. \[Online\], 11 (1), p. 16108. Available at: https://www.nature.com/articles/s41598-021-95388-7 \[accessed 24 May 2023\].
26.  [\[26\]](#sect5) May, R. A., Duncan, B. D. and Prather, D. W. Comparing performance of quantum and classical correlation filters for target detection in infrared imagery. Optics Express, 2011, 19 (11), pp. 10 387–10 409.
27.  [\[27\]](#sect5) Hensen, B., Bernien, H., Dréau, A., Reiserer, A., Kalb, N., Blok, M., Ruitenberg, J., Vermeulen, R., Schouten, R. and Abellán, C. Loophole-free bell inequality violation using electron spins separated by 1.3 kilometres. Nature, 2015, 526 (7575), pp. 682–686.
28.  [\[28\]](#sect5) Liao, S.-K., Cai, W.-Q., Liu, W.-Q., Zhang, L., Li, J., Ren, J.-G., Yin, J., Shen, Q., Cao, Y., Li, Y.-H. Satellite-to-ground quantum key distribution. Nature, 2017, 549 (7670), pp. 43–47.
29.  [\[29\]](#sect5) Gibney, E. Chinese satellite is one giant step for the quantum internet. Nature, 2016. \[Online\], 535 (7613), pp. 478–479. Available at: https://www.doi.org/10.1038/535478a \[accessed 24 May 2023\].
30.  [\[30\]](#sect5) University of Cambridge. Cambridge launches uk’s first quantum network, 2020. \[Online\]. Available at: https://www.cam.ac.uk/research/news/cambridge-launches-uks-first-quantum-network \[accessed 24 May 2023\].
31.  [\[31\]](#sect5) Quantum Strategist. New secure quantum communication infrastructure initiative (EuroQCI), 2022. \[Online\]. Available at: https://quantumzeitgeist.com/new-secure-quantum-communication-infrastructure-initiative-euroqci/ \[accessed 24 May 2023\].
32.  [\[32\]](#sect5) Canadian government. Government of Canada supports world-leading Canadian satellite-based emissions detection system, 2021. \[Online\]. Available at: https://www.canada.ca/en/innovation-science-economic-development/news/2021/11/government-of-canada-supports-world-leading-canadian-satellite-based-emissions-detection-system.html \[accessed 24 May 2023\].
33.  [\[33\]](#sect5) Ruihong Q. and Ying, M. Research progress of quantum repeaters. Journal of Physics, 2019. \[Online\], 1237 (5), p. 52032. Available at: https://iopscience.iop.org/article/10.1088/1742-6596/1237/5/052032 \[accessed 24 May 2023\].
34.  [\[34\]](#sect5) Diamanti, E., Lo, H.-K., Qi, B. and Yuan, Z. Practical challenges in quantum key distribution. npg Quantum Information, 2016. \[Online\], 2 (1), p. 16025. Available at: https://www.nature.com/articles/npjqi201625 \[accessed 24 May 2023\].