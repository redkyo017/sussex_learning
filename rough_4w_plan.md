Course Content Map (Weeks 1–4)

  ┌──────┬────────────────────────────────────────────────────────────────────────────┬──────────────────────────────────────────┐
  │ Week │                                Core Topics                                 │           Prerequisites Needed           │
  ├──────┼────────────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────┤
  │ 1    │ Boolean logic, Reversible computation, Randomised computation              │ Probability basics, combinatorics        │
  ├──────┼────────────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────┤
  │ 2    │ 2D algebra, Complex numbers, Eigenvectors/eigenvalues, Single-qubit states │ Linear algebra, complex numbers, trig    │
  ├──────┼────────────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────┤
  │ 3    │ Single-qubit unitaries, Bloch sphere, Multi-qubit states                   │ Linear algebra (matrices, unitary), trig │
  ├──────┼────────────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────┤
  │ 4    │ Quantum teleportation, Bell states, Hadamard, Phase estimation             │ Everything from weeks 1–3                │
  └──────┴────────────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────┘

  ---
  Phase 0 — Emergency Prerequisites Sprint (Before / Alongside Week 1–2)
  
  Do this in parallel with course study, not before. Each crash course is deliberately short.

  1. Linear Algebra (HIGHEST PRIORITY — affects weeks 2, 3, 4 and everything after)

  Why: Weeks 2–4 are built entirely on vectors, matrices, inner products, eigenvalues, and unitary transformations. Without this, you'll be memorising symbols without understanding what they mean.

  Crash course: 3Blue1Brown — "Essence of Linear Algebra" (YouTube, free)
  - 16 videos, ~10 min each ≈ 2.5 hrs total
  - Chapters you must not skip: vectors, linear transformations, matrix multiplication, dot products, change of basis, eigenvalues/eigenvectors
  - Search: 3Blue1Brown essence of linear algebra

  Supplementary (optional, for exercises): Khan Academy → "Linear Algebra" section — good for drilling computation by hand.

  Estimated time: 3–4 days (1 hr/day) to feel comfortable

  ---
  2. Complex Numbers (HIGH PRIORITY — starts week 2, never goes away)

  Why: Every quantum state vector has complex-number amplitudes. Week 2 introduces ket notation with complex entries, and from week 3 onward the math is entirely complex-valued.

  Crash course (pick one):
  - Khan Academy → "Complex numbers" section (under Algebra 2 or Precalculus) — 1–2 hrs
  - 3Blue1Brown — "Euler's formula with introductory group theory" (1 video, 24 min) — for the geometric intuition which is exactly what the course uses

  Must understand before Week 2:
  - Complex arithmetic: (a+bi)(c+di), conjugates a+bi → a-bi
  - Polar form: re^{iθ} = r(cosθ + i sinθ) — Euler's formula
  - Modulus: |a+bi| = √(a²+b²)

  Estimated time: 1–2 days

  ---
  3. Probability Theory (MEDIUM PRIORITY — needed from week 1 randomised computation)
  
  Why: Week 1's randomised computation section uses probability vectors (stochastic vectors) and matrix–vector products where matrices are row-stochastic. Week 2 connects this to quantum amplitudes.

  Crash course:
  - Khan Academy → "Statistics & Probability" — specifically: Basic probability, conditional probability, probability distributions
  - Seeing Theory (seeing-theory.brown.edu) — browser-based visual intro, excellent for building intuition in 1–2 hrs 

  Must understand:
  - Probability distributions over finite sets (like bit strings)
  - Expected value
  - What a "stochastic matrix" / "transition matrix" is

  Estimated time: 1–2 days

  ---
  4. Trigonometry Refresher (LIGHT — needed for angles/unit circle in week 2)
  
  The course uses cos(θ), sin(θ) for unit vectors and the Bloch sphere. You don't need deep trig — just:
  - Unit circle, radians vs degrees
  - sin/cos definitions from a right triangle
  - sin²(θ) + cos²(θ) = 1

  Khan Academy → "Trigonometry" → "Unit circle" — 30–45 min is enough.

  ---
  Prerequisite Study Schedule (Days 1–10, Pre-Midterm Sprint)

  Day 1–2:   Linear Algebra — 3B1B videos 1–8 (vectors → dot product)
  Day 3–4:   Linear Algebra — 3B1B videos 9–16 (change of basis → eigenvalues)
  Day 5:     Complex Numbers — Khan Academy + Euler's formula
  Day 6:     Trig refresher (unit circle, radians) — 45 min
             Probability Theory — Khan Academy distributions
  Day 7:     Probability Theory — stochastic matrices, transition matrices
  Day 8–10:  Apply: re-read Week 1 + Week 2 study materials with new eyes

  ---
  8-Week Module Roadmap

  Week 1 — Boolean Logic, Reversible & Randomised Computation

  Course topics: Boolean logic, binary encoding, logic gates (NOT/AND/OR/XOR), reversible circuits (CNOT, Toffoli), stochastic/probability vectors

  What to do:
  - Read the Week 1 PDF fully — this is closest to your CS background (binary, logic gates = familiar)
  - Focus extra time on section 1.3 (Randomised computation) — probability vectors in ket notation are the hardest part here and directly bridge to quantum

  Practice exercises:

  import numpy as np

  # Exercise 1: Binary encoding
  def to_binary(n, bits=4):
      return format(n, f'0{bits}b')

  for i in range(16):
      print(f"{i:2d} → {to_binary(i)}")

  # Exercise 2: Truth tables for all 4 operators
  def boolean_ops(a, b):
      return {
          'AND': a & b,
          'OR':  a | b,
          'XOR': a ^ b,
          'NOT_a': 1 - a
      }

  for a in [0, 1]:
      for b in [0, 1]:
          print(f"a={a}, b={b} → {boolean_ops(a,b)}")

  # Exercise 3: Stochastic matrix (randomised computation)
  # A coin flip represented as a probability vector + transition matrix
  heads_tails = np.array([0.5, 0.5])  # fair coin: [P(heads), P(tails)]
  fair_flip = np.array([[0.5, 0.5],    # stochastic matrix for fair coin flip
                        [0.5, 0.5]])

  result = fair_flip @ heads_tails
  print(f"After one flip: {result}")  # should still be [0.5, 0.5]

  Key concept to nail: Why reversible computation matters — every quantum gate is reversible (unitary), so you need to understand why standard Boolean gates (like AND) are NOT reversible (you can't recover inputs from output), and how
  CNOT/Toffoli fix this.

  ---
  Week 2 — 2D Geometry, Complex Numbers, Eigenvalues, Single Qubits
  
  Course topics: Ket notation, inner products, norms, complex numbers, eigenvectors/eigenvalues, Bloch sphere basics, qubit states, Born rule measurements

  This is the hardest week — do NOT skip the prerequisites first.

  Practice exercises:

  import numpy as np

  # Exercise 4: Inner products and norms (ket notation)
  ket_0 = np.array([1, 0], dtype=complex)  # |0⟩
  ket_1 = np.array([0, 1], dtype=complex)  # |1⟩
  ket_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)  # |+⟩

  def inner_product(u, v):
      return np.conj(u) @ v  # ⟨u|v⟩ = u†·v

  def norm(v):
      return np.sqrt(np.real(inner_product(v, v)))

  print(f"⟨0|0⟩ = {inner_product(ket_0, ket_0)}")  # 1
  print(f"⟨0|1⟩ = {inner_product(ket_0, ket_1)}")  # 0 (orthogonal)
  print(f"‖|+⟩‖ = {norm(ket_plus):.4f}")            # 1 (unit vector)

  # Exercise 5: Complex number arithmetic
  z1 = 1 + 2j
  z2 = 3 - 1j
  print(f"z1 * z2 = {z1 * z2}")
  print(f"|z1| = {abs(z1):.4f}")
  print(f"z1† (conjugate) = {z1.conjugate()}")
  print(f"Euler: e^(iπ/4) = {np.exp(1j * np.pi/4):.4f}")  # = (1+i)/√2

  # Exercise 6: Eigenvalues and eigenvectors of a 2x2 matrix
  Z = np.array([[1, 0], [0, -1]])   # Pauli Z gate
  X = np.array([[0, 1], [1,  0]])   # Pauli X gate

  eigenvalues_Z, eigenvectors_Z = np.linalg.eig(Z)
  print(f"Z eigenvalues: {eigenvalues_Z}")
  print(f"Z eigenvectors:\n{eigenvectors_Z}")

  # Exercise 7: Verify single-qubit state is on Bloch sphere
  # |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
  def bloch_state(theta, phi):
      return np.array([np.cos(theta/2),
                       np.exp(1j * phi) * np.sin(theta/2)])

  psi = bloch_state(np.pi/3, np.pi/4)
  print(f"|ψ⟩ = {psi}")
  print(f"Norm = {norm(psi):.4f}")  # Must be 1

  ---
  Week 3 — Single-Qubit Gates, Bloch Sphere, Multi-Qubit Systems

  Course topics: Rotation operators (Rx, Ry, Rz), standard gates (X/Y/Z/H/S/T), tensor products for multi-qubit states, CNOT gate, separable vs entangled states

  Practice exercises:

  import numpy as np

  # Standard single-qubit gates
  I = np.eye(2, dtype=complex)
  X = np.array([[0, 1], [1,  0]], dtype=complex)   # Pauli X (NOT gate)
  Y = np.array([[0,-1j],[1j, 0]], dtype=complex)   # Pauli Y
  Z = np.array([[1, 0], [0, -1]], dtype=complex)   # Pauli Z
  H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)  # Hadamard

  # Exercise 8: Verify gates are unitary (U†U = I)
  def is_unitary(U, tol=1e-10):
      return np.allclose(U.conj().T @ U, np.eye(len(U)), atol=tol)

  for name, gate in [('X',X),('Y',Y),('Z',Z),('H',H)]:
      print(f"{name} unitary: {is_unitary(gate)}")

  # Exercise 9: Tensor product (2-qubit system)
  def tensor(A, B):
      return np.kron(A, B)

  ket_0 = np.array([1, 0], dtype=complex)
  ket_1 = np.array([0, 1], dtype=complex)

  ket_00 = np.kron(ket_0, ket_0)  # |00⟩
  ket_11 = np.kron(ket_1, ket_1)  # |11⟩
  bell_state = (ket_00 + ket_11) / np.sqrt(2)  # |Φ+⟩
  print(f"|Φ+⟩ = {bell_state}")

  # Exercise 10: CNOT gate and entanglement
  CNOT = np.array([[1,0,0,0],
                   [0,1,0,0],
                   [0,0,0,1],
                   [0,0,1,0]], dtype=complex)

  # Apply Hadamard to qubit 0, then CNOT → creates Bell state
  H_I = np.kron(H, I)   # H on first qubit, identity on second
  state = H_I @ ket_00
  state = CNOT @ state
  print(f"After H⊗I then CNOT: {np.round(state, 4)}")
  # Should be |Φ+⟩ = [1/√2, 0, 0, 1/√2]

  ---
  Week 4 — Teleportation, Phase Estimation (Pre-Midterm)
  
  Course topics: Bell basis measurement, quantum teleportation protocol, Hadamard transform on n qubits, phase kickback, intuition for Grover's/Shor's

  Practice exercises:

  import numpy as np

  # Exercise 11: Bell basis measurement
  # Prepare |Φ+⟩ and verify the four Bell states
  def bell_state(x, z):
      """Returns Bell state |Φ+⟩ modified by Z^z X^x on second qubit"""
      CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)
      H = np.array([[1,1],[1,-1]], dtype=complex)/np.sqrt(2)
      X = np.array([[0,1],[1,0]], dtype=complex)
      Z = np.array([[1,0],[0,-1]], dtype=complex)
      ket_00 = np.array([1,0,0,0], dtype=complex)
      state = CNOT @ np.kron(H, np.eye(2)) @ ket_00
      if x: state = np.kron(np.eye(2), X) @ state
      if z: state = np.kron(np.eye(2), Z) @ state
      return state

  for x in [0,1]:
      for z in [0,1]:
          b = bell_state(x, z)
          print(f"x={x}, z={z}: {np.round(b, 3)}")

  # Exercise 12: Verify teleportation math
  # Show that measuring qubit a in Bell basis "teleports" state to Bob
  # This is the algebraic proof — follow the algebra from the Week 4 PDF
  alpha, beta = 0.6+0.8j, 0  # some valid qubit state (|α|²+|β|²=1... let's use normalized)
  alpha, beta = 1/np.sqrt(2), 1/np.sqrt(2)
  print(f"Teleporting state α={alpha:.3f}, β={beta:.3f}")
  print(f"Norm check: {abs(alpha)**2 + abs(beta)**2:.4f}")

  ---
  Weeks 5–8 Preview (Once Materials Arrive)
  
  Based on the progression so far, the likely topics will be:
  - Week 5: Quantum algorithms intro (Deutsch-Jozsa, Bernstein-Vazirani)
  - Week 6: Quantum Fourier Transform
  - Week 7: Grover's search algorithm
  - Week 8: Shor's algorithm overview / error correction intro

  Resources to pre-study once you're done with weeks 1–4:
  - IBM Qiskit Textbook (free, at learning.qiskit.org) — chapters on Deutsch-Jozsa, Grover, QFT directly parallel this course structure
  - Quantum Country (quantumcountry.com) — spaced-repetition quantum computing textbook by Andy Matuschak, excellent for retention

  ---
  Midterm Assignment Preparation (End of Week 4)
  
  Based on the topics, your midterm will likely test:

  ┌────────────────────────┬─────────────────────────────────────────────────────────────────────────────┐
  │         Topic          │                            What to be able to do                            │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Boolean logic          │ Write truth tables, prove universality with AND/OR/NOT                      │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Reversible gates       │ Show a Toffoli/CNOT circuit, explain why reversibility matters              │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Randomised computation │ Multiply a stochastic matrix by a probability vector                        │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Linear algebra         │ Inner products, matrix multiplication, show U is unitary (U†U = I)          │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Complex numbers        │ Polar form, conjugates, Euler's formula                                     │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Eigenvectors           │ Find eigenvalues/vectors of a 2×2 matrix                                    │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Qubit states           │ Represent a qubit on the Bloch sphere, compute Born-rule probabilities      │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Multi-qubit            │ Write a 2-qubit state as tensor product, construct Bell state via H+CNOT    │
  ├────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ Teleportation          │ Explain the protocol steps (no need to rederive, just understand each step) │
  └────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘

  Midterm prep drill (last 3 days before assignment):
  1. Do all the Python exercises above by hand on paper first, then check with code
  2. Re-read the Week 1–4 PDFs and do any embedded exercises
  3. Verify you can: (a) construct a Bell state from scratch, (b) compute U†U = I for the Hadamard gate, (c) multiply a stochastic matrix by a prob vector

  ---
  Tools to Install Now

  pip install numpy scipy matplotlib qiskit

  For a quantum circuit simulator directly in Python, Qiskit is the industry standard and directly mirrors the QAAL notation your course uses. It lets you run circuits on a simulated quantum computer locally.

  ---
  Summary Priority Stack

  WEEK 0 (now):  3Blue1Brown Linear Algebra → Complex Numbers → Probability basics
  WEEK 1 study:  Boolean/reversible/randomised — lean on CS background, focus on prob vectors
  WEEK 2 study:  Hardest week — go slow, re-read 3B1B after each section
  WEEK 3 study:  Gates, Bloch sphere — do the Python exercises above
  WEEK 4 study:  Teleportation — follow the algebra step by step, don't try to memorise
  MIDTERM PREP:  3 days, work problems by hand

  The biggest risk for you is linear algebra deficiency hitting you hard in week 2 — those 3Blue1Brown videos are the single highest-ROI thing you can do this week.