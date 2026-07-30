# Assignment 1 Solution — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a complete, submittable `assignment_1.tex` (all 10 questions with full workings) and a companion `assignment_1_study_guide.md` for future review.

**Architecture:** Single LaTeX file compiled with `pdflatex`. All 10 answers have been pre-verified mathematically. Study guide is plain Markdown, one section per question.

**Tech Stack:** LaTeX (braket, amsmath, amssymb, geometry packages), Markdown

---

## Files

| Action | Path |
|--------|------|
| Create | `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex` |
| Create | `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md` |

---

## Task 1: LaTeX skeleton + Questions 1–3

**Files:**
- Create: `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex`

- [ ] **Step 1: Create the file with preamble, cover block, and Q1–Q3**

```latex
\documentclass[12pt,a4paper]{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{braket}
\usepackage[margin=2.5cm]{geometry}

\title{\textbf{Foundations of Quantum Computing}\\[0.5em]
       \large Assignment 1}
\author{Duc Hung Le}
\date{\today}

\begin{document}
\maketitle
\thispagestyle{empty}

% ---------------------------------------------------------------
\section*{Question 1}

Consider the single-qubit unitary transformations $Z$, $H$, and $\mathrm{CX}$ as defined
in the question. We compute $Z_1\,Z_2\,\mathrm{CX}_{2,1}\,\mathrm{CX}_{2,3}\,H_2\ket{0,0,0}$
by applying gates right-to-left.

\medskip
\textbf{Step 1 — Apply $H_2$:}
\begin{align*}
H_2\ket{0,0,0}
  &= \ket{0}_1 \otimes H\ket{0}_2 \otimes \ket{0}_3 \\
  &= \ket{0} \otimes \frac{1}{\sqrt{2}}\!\left(\ket{0}+\ket{1}\right) \otimes \ket{0} \\
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{0,1,0}\right)
\end{align*}

\textbf{Step 2 — Apply $\mathrm{CX}_{2,3}$ (control = qubit 2, target = qubit 3):}

$\mathrm{CX}_{2,3}\ket{q_1,q_2,q_3}=\ket{q_1,q_2,q_2\oplus q_3}$

\begin{align*}
\mathrm{CX}_{2,3}\cdot\frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{0,1,0}\right)
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0\oplus 0}+\ket{0,1,1\oplus 0}\right) \\
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{0,1,1}\right)
\end{align*}

\textbf{Step 3 — Apply $\mathrm{CX}_{2,1}$ (control = qubit 2, target = qubit 1):}

$\mathrm{CX}_{2,1}\ket{q_1,q_2,q_3}=\ket{q_2\oplus q_1,\,q_2,\,q_3}$

\begin{align*}
\mathrm{CX}_{2,1}\cdot\frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{0,1,1}\right)
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0\oplus 0,0,0}+\ket{1\oplus 0,1,1}\right) \\
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{1,1,1}\right)
\end{align*}

\textbf{Step 4 — Apply $Z_2$:}

$Z\ket{0}=\ket{0}$, $Z\ket{1}=-\ket{1}$, so $Z_2$ negates any term where qubit 2 is $\ket{1}$:
\begin{align*}
Z_2\cdot\frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{1,1,1}\right)
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}-\ket{1,1,1}\right)
\end{align*}

\textbf{Step 5 — Apply $Z_1$:}

$Z_1$ negates any term where qubit 1 is $\ket{1}$:
\begin{align*}
Z_1\cdot\frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}-\ket{1,1,1}\right)
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}-(-1)\ket{1,1,1}\right) \\
  &= \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{1,1,1}\right)
\end{align*}

\[
  \boxed{Z_1\,Z_2\,\mathrm{CX}_{2,1}\,\mathrm{CX}_{2,3}\,H_2\ket{0,0,0}
         = \frac{1}{\sqrt{2}}\!\left(\ket{0,0,0}+\ket{1,1,1}\right)}
\]

% ---------------------------------------------------------------
\section*{Question 2}

We compute $H_2\!\left(\tfrac{1}{2}\ket{\Phi^+}+\tfrac{1}{2}\ket{\Phi^-}
+\tfrac{1}{2}\ket{\Psi^+}+\tfrac{1}{2}\ket{\Psi^-}\right)$.

\medskip
\textbf{Step 1 — Expand the Bell-state mixture into the computational basis:}
\begin{align*}
&\tfrac{1}{2}\ket{\Phi^+}+\tfrac{1}{2}\ket{\Phi^-}+\tfrac{1}{2}\ket{\Psi^+}+\tfrac{1}{2}\ket{\Psi^-} \\
&= \frac{1}{2\sqrt{2}}\Bigl[
   \bigl(\ket{00}+\ket{11}\bigr)
  +\bigl(\ket{00}-\ket{11}\bigr)
  +\bigl(\ket{01}+\ket{10}\bigr)
  +\bigl(\ket{01}-\ket{10}\bigr)\Bigr] \\
&= \frac{1}{2\sqrt{2}}\Bigl[2\ket{00}+2\ket{01}\Bigr]
 = \frac{1}{\sqrt{2}}\bigl(\ket{0,0}+\ket{0,1}\bigr) \\
&= \ket{0}_1 \otimes \underbrace{\frac{1}{\sqrt{2}}\bigl(\ket{0}+\ket{1}\bigr)}_{=\,\ket{+}}
 = \ket{0}\otimes\ket{+}
\end{align*}

\textbf{Step 2 — Apply $H_2$:}

\begin{align*}
H_2\bigl(\ket{0}\otimes\ket{+}\bigr)
  &= \ket{0}\otimes H\ket{+} \\
  &= \ket{0}\otimes H\!\left(\frac{\ket{0}+\ket{1}}{\sqrt{2}}\right) \\
  &= \ket{0}\otimes\frac{1}{\sqrt{2}}\!\left(H\ket{0}+H\ket{1}\right) \\
  &= \ket{0}\otimes\frac{1}{\sqrt{2}}\!\left(\frac{\ket{0}+\ket{1}}{\sqrt{2}}+\frac{\ket{0}-\ket{1}}{\sqrt{2}}\right) \\
  &= \ket{0}\otimes\ket{0}
\end{align*}

\[
  \boxed{H_2\!\left(\tfrac{1}{2}\ket{\Phi^+}+\tfrac{1}{2}\ket{\Phi^-}
         +\tfrac{1}{2}\ket{\Psi^+}+\tfrac{1}{2}\ket{\Psi^-}\right) = \ket{0,0}}
\]

% ---------------------------------------------------------------
\section*{Question 3}

Consider $\ket{\Psi^-}=\dfrac{1}{\sqrt{2}}\ket{0,1}-\dfrac{1}{\sqrt{2}}\ket{1,0}$.
We measure the first qubit in the $\{\ket{0},\ket{1}\}$ basis and obtain $\ket{0}$.

\medskip
Only the terms where the first qubit is $\ket{0}$ survive the measurement.
From the expansion, the sole surviving term is $\dfrac{1}{\sqrt{2}}\ket{0}_1\ket{1}_2$.

The probability of this outcome is $\left|\dfrac{1}{\sqrt{2}}\right|^{\!2}=\dfrac{1}{2}$.

After normalising (dividing by $\dfrac{1}{\sqrt{2}}$), the joint state collapses to
$\ket{0}_1\otimes\ket{1}_2$, so the state of the second qubit is:

\[
  \boxed{\ket{1}}
\]

\end{document}
```

- [ ] **Step 2: Verify the file compiles**

```bash
cd module_1_foundation_of_quantum_computing/assignment_1
pdflatex assignment_1.tex
```

Expected: `assignment_1.pdf` produced with no errors. Open and confirm Q1–Q3 render correctly (fractions, kets, boxes).

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex
git commit -m "feat: add assignment 1 LaTeX skeleton with Q1-Q3 solutions"
```

---

## Task 2: Questions 4–7

**Files:**
- Modify: `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex`

Replace `\end{document}` at the bottom with the following content, then re-add `\end{document}` after it.

- [ ] **Step 1: Add Q4–Q7 before `\end{document}`**

```latex
% ---------------------------------------------------------------
\section*{Question 4}

Consider $\ket{\Psi^-}=\dfrac{1}{\sqrt{2}}\ket{0,1}-\dfrac{1}{\sqrt{2}}\ket{1,0}$.
We measure the first qubit in the $\{\ket{+},\ket{-}\}$ basis and obtain $\ket{-}$.

\medskip
We compute the (unnormalised) state of qubit 2 by projecting onto $\ket{-}$ via the
inner product ${}_{1}\!\bra{-}\ket{\Psi^-}$. Using
$\braket{-|0}=\tfrac{1}{\sqrt{2}}$ and $\braket{-|1}=-\tfrac{1}{\sqrt{2}}$:

\begin{align*}
{}_{1}\!\bra{-}\ket{\Psi^-}
  &= \frac{1}{\sqrt{2}}\braket{-|0}_1\ket{1}_2
   - \frac{1}{\sqrt{2}}\braket{-|1}_1\ket{0}_2 \\
  &= \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}\,\ket{1}_2
   - \frac{1}{\sqrt{2}}\cdot\!\left(-\frac{1}{\sqrt{2}}\right)\ket{0}_2 \\
  &= \frac{1}{2}\ket{1}_2 + \frac{1}{2}\ket{0}_2
   = \frac{1}{2}\bigl(\ket{0}+\ket{1}\bigr)_2
\end{align*}

The norm of this unnormalised state is
$\sqrt{(1/2)^2+(1/2)^2}=\dfrac{1}{\sqrt{2}}$.
Normalising:

\[
  \frac{\tfrac{1}{2}\bigl(\ket{0}+\ket{1}\bigr)}{\tfrac{1}{\sqrt{2}}}
  = \frac{1}{\sqrt{2}}\bigl(\ket{0}+\ket{1}\bigr)
  = \ket{+}
\]

\[
  \boxed{\ket{+}}
\]

% ---------------------------------------------------------------
\section*{Question 5}

Consider the same state $\ket{\Psi^-}$. We now measure the first qubit in the
$\{\ket{+i},\ket{-i}\}$ basis and obtain $\ket{+i}$, where
$\ket{+i}=\tfrac{1}{\sqrt{2}}(\ket{0}+i\ket{1})$.

\medskip
The corresponding bra is $\bra{+i}=\tfrac{1}{\sqrt{2}}(\bra{0}-i\bra{1})$ (conjugate).

Using $\braket{+i|0}=\tfrac{1}{\sqrt{2}}$ and $\braket{+i|1}=-\tfrac{i}{\sqrt{2}}$:

\begin{align*}
{}_{1}\!\bra{+i}\ket{\Psi^-}
  &= \frac{1}{\sqrt{2}}\braket{+i|0}_1\ket{1}_2
   - \frac{1}{\sqrt{2}}\braket{+i|1}_1\ket{0}_2 \\
  &= \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}\,\ket{1}_2
   - \frac{1}{\sqrt{2}}\cdot\!\left(-\frac{i}{\sqrt{2}}\right)\ket{0}_2 \\
  &= \frac{1}{2}\ket{1}_2 + \frac{i}{2}\ket{0}_2
   = \frac{1}{2}\bigl(i\ket{0}+\ket{1}\bigr)_2
\end{align*}

The norm is $\sqrt{|i/2|^2+|1/2|^2}=\sqrt{1/4+1/4}=\dfrac{1}{\sqrt{2}}$.
Normalising:

\[
  \frac{\tfrac{1}{2}(i\ket{0}+\ket{1})}{\tfrac{1}{\sqrt{2}}}
  = \frac{1}{\sqrt{2}}(i\ket{0}+\ket{1})
  = i\cdot\frac{1}{\sqrt{2}}(\ket{0}-i\ket{1})
  = i\ket{-i}
\]

Since the global phase factor $i$ has no physical effect, the state of the second qubit is:

\[
  \boxed{\ket{-i}}
\]

% ---------------------------------------------------------------
\section*{Question 6}

We compute the $2\times2$ matrix for
$U(\theta,\phi)=R_z(-\phi)\,R_y(\theta)\,R_z(\phi)$, where

\[
  R_y(\theta)=e^{i\theta/2}
  \begin{pmatrix}\cos\tfrac{\theta}{2}&-\sin\tfrac{\theta}{2}\\
                  \sin\tfrac{\theta}{2}& \cos\tfrac{\theta}{2}\end{pmatrix},
  \qquad
  R_z(\phi)=\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix}
\]

Let $c=\cos(\theta/2)$ and $s=\sin(\theta/2)$.

\medskip
\textbf{Step 1 — Compute $R_y(\theta)\,R_z(\phi)$:}
\begin{align*}
R_y(\theta)\,R_z(\phi)
  &= e^{i\theta/2}\begin{pmatrix}c&-s\\s&c\end{pmatrix}
     \begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix}
   = e^{i\theta/2}\begin{pmatrix}c & -se^{i\phi}\\s & ce^{i\phi}\end{pmatrix}
\end{align*}

\textbf{Step 2 — Pre-multiply by $R_z(-\phi)$:}
\begin{align*}
U(\theta,\phi)
  &= \begin{pmatrix}1&0\\0&e^{-i\phi}\end{pmatrix}
     \cdot e^{i\theta/2}\begin{pmatrix}c & -se^{i\phi}\\s & ce^{i\phi}\end{pmatrix} \\[6pt]
  &= e^{i\theta/2}
     \begin{pmatrix}c & -se^{i\phi}\\se^{-i\phi} & c\end{pmatrix}
\end{align*}

\[
  \boxed{U(\theta,\phi)=e^{i\theta/2}
    \begin{pmatrix}
      \cos\tfrac{\theta}{2} & -e^{i\phi}\sin\tfrac{\theta}{2}\\[4pt]
      e^{-i\phi}\sin\tfrac{\theta}{2} & \cos\tfrac{\theta}{2}
    \end{pmatrix}}
\]

% ---------------------------------------------------------------
\section*{Question 7}

Let $V=U(1,1)$. From Question 6:
\[
  V = e^{i/2}
      \begin{pmatrix}
        \cos\tfrac{1}{2} & -e^{i}\sin\tfrac{1}{2}\\[4pt]
        e^{-i}\sin\tfrac{1}{2} & \cos\tfrac{1}{2}
      \end{pmatrix}
\]

The controlled-$V$ gate acts as $\ket{0}\!\bra{0}\otimes I+\ket{1}\!\bra{1}\otimes V$.
As a $4\times4$ matrix (control qubit in the first register):

\[
  \boxed{CV =
  \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & e^{i/2}\cos\tfrac{1}{2}  & -e^{3i/2}\sin\tfrac{1}{2} \\
    0 & 0 & e^{-i/2}\sin\tfrac{1}{2} &  e^{i/2}\cos\tfrac{1}{2}
  \end{pmatrix}}
\]
```

- [ ] **Step 2: Verify the file compiles**

```bash
cd module_1_foundation_of_quantum_computing/assignment_1
pdflatex assignment_1.tex
```

Expected: no errors. Open PDF and confirm Q4–Q7 render correctly.

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex
git commit -m "feat: add Q4-Q7 solutions to assignment 1"
```

---

## Task 3: Questions 8–10

**Files:**
- Modify: `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex`

Replace `\end{document}` with the following, then re-add `\end{document}` after it.

- [ ] **Step 1: Add Q8–Q10 before `\end{document}`**

```latex
% ---------------------------------------------------------------
\section*{Question 8}

The four Bell states form an orthonormal basis. We compute the probability of each
outcome when measuring $\ket{+i,+i}$ in the Bell basis.

\medskip
\textbf{Step 1 — Expand $\ket{+i,+i}$:}
\begin{align*}
\ket{+i,+i}
  &= \frac{1}{\sqrt{2}}\bigl(\ket{0}+i\ket{1}\bigr)
     \otimes
     \frac{1}{\sqrt{2}}\bigl(\ket{0}+i\ket{1}\bigr) \\
  &= \frac{1}{2}\bigl(\ket{00}+i\ket{01}+i\ket{10}+i^2\ket{11}\bigr) \\
  &= \frac{1}{2}\bigl(\ket{00}+i\ket{01}+i\ket{10}-\ket{11}\bigr)
\end{align*}

\textbf{Step 2 — Compute $P(B_k)=|\braket{B_k|+i,+i}|^2$ for each Bell state:}

\begin{align*}
\braket{\Phi^+|+i,+i}
  &= \frac{1}{\sqrt{2}}(\bra{00}+\bra{11})
     \cdot\frac{1}{2}(\ket{00}+i\ket{01}+i\ket{10}-\ket{11}) \\
  &= \frac{1}{2\sqrt{2}}(1+(-1)) = 0
\end{align*}

\begin{align*}
\braket{\Phi^-|+i,+i}
  &= \frac{1}{\sqrt{2}}(\bra{00}-\bra{11})
     \cdot\frac{1}{2}(\ket{00}+i\ket{01}+i\ket{10}-\ket{11}) \\
  &= \frac{1}{2\sqrt{2}}(1-(-1)) = \frac{1}{\sqrt{2}}
\end{align*}

\begin{align*}
\braket{\Psi^+|+i,+i}
  &= \frac{1}{\sqrt{2}}(\bra{01}+\bra{10})
     \cdot\frac{1}{2}(\ket{00}+i\ket{01}+i\ket{10}-\ket{11}) \\
  &= \frac{1}{2\sqrt{2}}(i+i) = \frac{i}{\sqrt{2}}
\end{align*}

\begin{align*}
\braket{\Psi^-|+i,+i}
  &= \frac{1}{\sqrt{2}}(\bra{01}-\bra{10})
     \cdot\frac{1}{2}(\ket{00}+i\ket{01}+i\ket{10}-\ket{11}) \\
  &= \frac{1}{2\sqrt{2}}(i-i) = 0
\end{align*}

\textbf{Step 3 — Probability distribution:}

\[
  \boxed{
    P(\ket{\Phi^+})=0,\quad
    P(\ket{\Phi^-})=\tfrac{1}{2},\quad
    P(\ket{\Psi^+})=\tfrac{1}{2},\quad
    P(\ket{\Psi^-})=0
  }
\]

Check: $0+\tfrac{1}{2}+\tfrac{1}{2}+0=1$ \checkmark

% ---------------------------------------------------------------
\section*{Question 9}

The CCX (Toffoli) gate flips the third qubit only when both the first and second
qubits are $\ket{1}$: $\mathrm{CCX}\ket{a,b,t}=\ket{a,b,\,t\oplus(a\wedge b)}$.

\medskip
\textbf{Step 1 — Expand $\ket{+,+,0}$:}
\begin{align*}
\ket{+,+,0}
  &= \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\otimes\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\otimes\ket{0} \\
  &= \frac{1}{2}(\ket{000}+\ket{010}+\ket{100}+\ket{110})
\end{align*}

\textbf{Step 2 — Apply CCX term by term:}
\begin{align*}
\mathrm{CCX}\ket{000}&=\ket{000}, &
\mathrm{CCX}\ket{010}&=\ket{010}, \\
\mathrm{CCX}\ket{100}&=\ket{100}, &
\mathrm{CCX}\ket{110}&=\ket{111}
\end{align*}
\[
  \ket{\psi_0}=\mathrm{CCX}\ket{+,+,0}
  =\frac{1}{2}\bigl(\ket{000}+\ket{010}+\ket{100}+\ket{111}\bigr)
\]

\textbf{Step 3 — Measure the third qubit; find $P(\ket{0})$:}

The terms with third qubit $=\ket{0}$ are $\ket{000}$, $\ket{010}$, $\ket{100}$,
each with amplitude $\tfrac{1}{2}$:
\[
  P(\text{third qubit}=\ket{0})
  = \left|\tfrac{1}{2}\right|^2+\left|\tfrac{1}{2}\right|^2+\left|\tfrac{1}{2}\right|^2
  = \frac{3}{4}
\]

\[
  \boxed{P(\text{third qubit}=\ket{0})=\frac{3}{4}}
\]

% ---------------------------------------------------------------
\section*{Question 10}

We use the same state $\ket{\psi_0}=\tfrac{1}{2}(\ket{000}+\ket{010}+\ket{100}+\ket{111})$
from Question 9, with $P(\text{qubit 3}=\ket{0})=\tfrac{3}{4}$.

\medskip
\textbf{Step 1 — Post-measurement state conditioned on qubit 3 $=\ket{0}$:}

Retaining only the terms $\ket{000}$, $\ket{010}$, $\ket{100}$ and normalising
(dividing by $\sqrt{3/4}=\tfrac{\sqrt{3}}{2}$):
\[
  \ket{\psi\,|\,\text{qubit 3}=0}
  = \frac{1}{\sqrt{3}}\bigl(\ket{000}+\ket{010}+\ket{100}\bigr)
\]

\textbf{Step 2 — Measure the first two qubits; find $P(\ket{10})$:}

The amplitude of $\ket{10}\otimes\ket{0}$ in the normalised state is $\tfrac{1}{\sqrt{3}}$, so:
\[
  P(\ket{10})=\left|\frac{1}{\sqrt{3}}\right|^2=\frac{1}{3}
\]

\emph{Equivalently, using conditional probability directly:}
\[
  P(\ket{10}\,|\,\text{qubit 3}=\ket{0})
  =\frac{P(\ket{10,0})}{P(\text{qubit 3}=\ket{0})}
  =\frac{1/4}{3/4}=\frac{1}{3}
\]

\[
  \boxed{P(\text{first two qubits}=\ket{10}\mid\text{qubit 3}=\ket{0})=\frac{1}{3}}
\]
```

- [ ] **Step 2: Verify the complete document compiles**

```bash
cd module_1_foundation_of_quantum_computing/assignment_1
pdflatex assignment_1.tex
```

Expected: no errors. Open PDF and confirm all 10 questions are present with correct typesetting and boxed answers.

- [ ] **Step 3: Commit**

```bash
git add module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex
git commit -m "feat: complete assignment 1 LaTeX with all 10 solutions"
```

---

## Task 4: Study guide

**Files:**
- Create: `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md`

- [ ] **Step 1: Create the study guide**

```markdown
# Assignment 1 — Study Guide

A plain-English companion to the solutions. Read this after submission to consolidate
what each question was really testing.

---

## Q1 — Gate Composition on 3 Qubits

**What it tests:** Ability to apply a sequence of quantum gates step by step.

**Recipe:**
1. Read the expression right-to-left — the rightmost gate applies first.
2. For each gate, apply it only to the qubit(s) it acts on; leave the rest unchanged.
3. Use tensor product notation: if gate G acts on qubit k, write the state as
   a sum of terms and apply G to the k-th factor in each term.
4. For Z: Z|0⟩ = |0⟩, Z|1⟩ = −|1⟩ — it just changes the sign of |1⟩.
5. For H: H|0⟩ = (|0⟩+|1⟩)/√2, H|1⟩ = (|0⟩−|1⟩)/√2.
6. For CX (control c, target t): flip the target iff the control is |1⟩.

**Why it works:** Every quantum gate is linear — you can apply it term by term
to a superposition, then collect results.

**Common mistakes:**
- Applying gates left-to-right instead of right-to-left.
- Forgetting to leave uninvolved qubits unchanged.
- Missing the sign flip from Z on |1⟩.

---

## Q2 — Hadamard on an Entangled Superposition

**What it tests:** Simplifying a mixture of Bell states before applying a gate.

**Recipe:**
1. Expand every Bell state into the computational basis using its definition.
2. Collect like terms — many will cancel or double.
3. Identify the simplified result as a product state if possible.
4. Apply H to the target qubit of the product state using H|+⟩ = |0⟩, H|−⟩ = |1⟩.

**Why it works:** The equal superposition of all four Bell states is not entangled
— it simplifies to |0⟩⊗|+⟩, which is a product state. H then undoes the |+⟩.

**Common mistakes:**
- Trying to apply H directly to each Bell state without simplifying first (more work).
- Forgetting that H is its own inverse: H² = I, so H|+⟩ = |0⟩.

---

## Q3 — Partial Measurement (Computational Basis)

**What it tests:** How measurement collapses part of a multi-qubit state.

**Recipe:**
1. Write the state as a sum: Σ aₖ |outcome_on_qubit1, state_of_qubit2⟩.
2. Keep only the terms where qubit 1 matches the measurement outcome.
3. The remaining second-qubit state (after stripping out the first qubit ket) is the
   unnormalised post-measurement state.
4. Normalise by dividing by the norm (= √(probability of that outcome)).

**Why it works:** Measurement "projects" the state onto the subspace consistent
with the outcome. The Born rule says the probability is the sum of |amplitude|²
for all terms matching the outcome.

**Common mistakes:**
- Forgetting to normalise after projecting.
- Confusing which qubit is being measured.

---

## Q4 — Partial Measurement (Hadamard / {+,−} Basis)

**What it tests:** Measuring in a non-computational basis.

**Recipe:**
1. Compute the inner product ⟨outcome|ψ⟩ for the measured qubit.
   For |−⟩: ⟨−|0⟩ = 1/√2, ⟨−|1⟩ = −1/√2.
2. Apply this to the full 2-qubit state by acting only on the first qubit's factor.
3. The result is the unnormalised second-qubit state. Normalise.

**Why it works:** Projecting onto |−⟩ in the first register is the same as
computing how much of the state "points along" |−⟩. The formula is:
post-measurement state of qubit 2 ∝ ₁⟨−|ψ₁₂⟩.

**Common mistakes:**
- Using the ket instead of the bra (⟨−| not |−⟩) when projecting.
- Forgetting to conjugate when computing ⟨−| from |−⟩.

---

## Q5 — Partial Measurement (Y Basis / {+i,−i})

**What it tests:** Measurement with complex-valued basis states.

**Recipe:**
1. Write the bra: |+i⟩ = (|0⟩ + i|1⟩)/√2, so ⟨+i| = (⟨0| − i⟨1|)/√2.
   Note the conjugation: i → −i.
2. Compute ⟨+i|0⟩ = 1/√2 and ⟨+i|1⟩ = −i/√2.
3. Apply these inner products term by term to extract the second qubit state.
4. Normalise. If the normalised state equals e^{iφ}|known⟩, identify it as |known⟩
   (global phase has no physical effect).

**Why it works:** The Y-basis states are eigenstates of the Pauli Y gate. The algebra
is the same as Q4 but with complex coefficients — the key new step is correctly
conjugating i → −i when converting ket to bra.

**Common mistakes:**
- Forgetting to conjugate i when writing the bra.
- Not recognising the global phase: i|−i⟩ is physically equivalent to |−i⟩.

---

## Q6 — Rotation Gate Composition

**What it tests:** 2×2 matrix multiplication with complex entries.

**Recipe:**
1. Substitute the matrix definitions of Ry(θ) and Rz(φ).
2. Multiply Ry(θ)·Rz(φ) first (right-to-left): column of Rz multiplied by rows of Ry.
3. Then pre-multiply by Rz(−φ).
4. Carry any global scalar (like e^{iθ/2}) through — it factors outside the matrix.

**Why it works:** Any single-qubit unitary U(θ,φ) = Rz(−φ)Ry(θ)Rz(φ) is a
"sandwich" that rotates around an axis tilted by φ from the z-axis. This
decomposition is used in real quantum hardware to implement arbitrary single-qubit
gates using only two native rotation types.

**Common mistakes:**
- Multiplying in the wrong order (left-to-right instead of right-to-left).
- Dropping the global phase e^{iθ/2} — it matters for controlled gates (Q7).

---

## Q7 — Controlled Gates

**What it tests:** How a single-qubit gate becomes a 2-qubit controlled gate.

**Recipe:**
1. A controlled-V gate has the block structure:
   CV = [[I, 0], [0, V]]  (as a 2×2 block matrix over 2×2 blocks)
   i.e., the top-left 2×2 is the identity, the bottom-right 2×2 is V.
2. Substitute V = U(1,1) from Q6 (with θ=1, φ=1 — leave trig unevaluated as instructed).
3. The (3,3), (3,4), (4,3), (4,4) entries of the 4×4 matrix are exactly V's entries.

**Why it works:** If the control qubit is |0⟩, nothing happens (identity on target).
If the control is |1⟩, V is applied to the target. Written as a projection:
CV = |0⟩⟨0|⊗I + |1⟩⟨1|⊗V.

**Common mistakes:**
- Placing V in the top-left block instead of bottom-right.
- Evaluating the trig numerically when the question says not to.

---

## Q8 — Bell Basis Measurement and Probability Distribution

**What it tests:** Computing measurement probabilities in a non-standard basis.

**Recipe:**
1. Expand the state being measured into the computational basis.
2. For each Bell state |Bₖ⟩, compute the inner product ⟨Bₖ|ψ⟩.
3. P(Bₖ) = |⟨Bₖ|ψ⟩|². Note |i|² = 1 and |0|² = 0.
4. Check your answers sum to 1.

**Why it works:** The Bell states form an orthonormal basis. The Born rule applies
in any orthonormal basis: probability of each outcome = squared modulus of the
component of the state along that basis vector.

**Common mistakes:**
- Forgetting to take the modulus squared (|·|²) — for complex inner products,
  |i/√2|² = 1/2, not i/2.
- Arithmetic errors when expanding the tensor product.

---

## Q9 — Toffoli Gate and Measurement Probability

**What it tests:** Multi-qubit gate application (CCX) followed by a single measurement.

**Recipe:**
1. Expand the input state term by term into computational basis states.
2. Apply CCX to each term: only flip the third qubit if BOTH the first and second are |1⟩.
3. Sum the |amplitude|² of all terms where the measured qubit matches the outcome.

**Why it works:** CCX is the quantum version of the classical AND gate — it is reversible
(Toffoli gate). The probability of a measurement outcome is the total weight of the
part of the superposition consistent with that outcome.

**Common mistakes:**
- Flipping the third qubit when only one of the control qubits is |1⟩.
- Summing amplitudes instead of |amplitudes|² (interference vs. probability).

---

## Q10 — Sequential Conditional Measurement

**What it tests:** Conditional probability after a first measurement collapses the state.

**Recipe (two equivalent methods):**

Method A — Conditional probability formula:
  P(A|B) = P(A and B) / P(B)
  Here: P(first two = |10⟩ | third = |0⟩) = P(|10,0⟩) / P(third = |0⟩)

Method B — Post-measurement state:
1. After measuring the third qubit = |0⟩, keep only terms with third qubit = |0⟩.
2. Normalise by dividing by √(probability of that outcome).
3. The probability of the second measurement is |amplitude of target term|² in the
   normalised state.

**Why it works:** Sequential measurements are described by conditional probability.
Each measurement updates (collapses) the state; subsequent probabilities are
computed from the collapsed state.

**Common mistakes:**
- Computing P(|10,0⟩) and reporting it as the answer without conditioning on P(third=|0⟩).
- Normalising incorrectly after the first measurement.
```

- [ ] **Step 2: Commit**

```bash
git add module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md
git commit -m "docs: add assignment 1 study guide with recipes for all 10 questions"
```

---

## Task 5: Final compile and CONTINUATION.md update

**Files:**
- Modify: `CONTINUATION.md`

- [ ] **Step 1: Final compile check**

```bash
cd module_1_foundation_of_quantum_computing/assignment_1
pdflatex assignment_1.tex
pdflatex assignment_1.tex
```

Run twice — LaTeX sometimes needs two passes to resolve references. Expected: zero errors, `assignment_1.pdf` opens correctly showing all 10 questions with boxed answers.

- [ ] **Step 2: Add .gitignore for LaTeX build artifacts**

Create `module_1_foundation_of_quantum_computing/assignment_1/.gitignore`:

```
*.aux
*.log
*.out
*.synctex.gz
*.fls
*.fdb_latexmk
```

- [ ] **Step 3: Update CONTINUATION.md "What Has Been Built" table**

Add these rows to the table:

```markdown
| `module_1_foundation_of_quantum_computing/assignment_1/assignment_1.tex` | ✅ Done | Full LaTeX solution for all 10 questions |
| `module_1_foundation_of_quantum_computing/assignment_1/assignment_1_study_guide.md` | ✅ Done | Study guide with recipes for all 10 questions |
```

- [ ] **Step 4: Final commit**

```bash
git add module_1_foundation_of_quantum_computing/assignment_1/.gitignore CONTINUATION.md
git commit -m "chore: add LaTeX gitignore and update CONTINUATION.md for assignment 1"
```

---

## Submission Checklist

- [ ] Open `assignment_1.pdf` and verify all 10 answers have boxed final results
- [ ] Confirm your name appears on the cover block
- [ ] Upload `assignment_1.pdf` to the Canvas submission point
- [ ] Declaration confirmed: the PDF contains your own work (you have reviewed and understood every solution)
