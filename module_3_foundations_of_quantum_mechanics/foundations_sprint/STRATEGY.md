# Strategy: How to Get Fluent in Module 3 Fast

This file explains how the sprint works, which traps to avoid, how to read a lecture so it actually sticks, and how to write up solutions. Read it once now, then come back to the reading protocol at the start of each week.

## The Strategy

The design is **problem-first reverse engineering**. We looked at what Weeks 2 to 7 actually ask you to do, listed the exact maths "moves" those problems use, and teach only those moves, in the shortest workable form. Four principles hold it together.

### 1. Learn moves, not subjects

**Why it works.** A subject ("linear algebra") is huge. A move ("find the eigenvalues of a 2x2 matrix") is small, testable and reusable. Module 3 problems are built from a short list of moves, so mastering the list beats surveying the field.

**Do this.** Each day file names its moves (for example Move 3.2). When you finish a day, you should be able to say each move's name and perform it on a blank page. If a move is shaky, redo its exercise before moving on.

### 2. Problems before theory

**Why it works.** Attempting a problem cold and failing makes your brain ask a precise question. The explanation that follows then lands on a prepared gap instead of washing past you. Reading a clean derivation first feels smooth, but the smoothness is an illusion of understanding.

**Do this.** Before reading a day's moves, spend five to ten minutes on the first exercise with no help. Write down where you got stuck. Then read the move. Also do this with the lecture: read the quiz and task problems before the lecture text (Pass 0 below).

### 3. Retrieval over rereading

**Why it works.** Pulling an idea out of memory strengthens it far more than looking at it again. Rereading gives familiarity, not recall, and exam or assessment conditions test recall.

**Do this.** Every day opens with five closed-book questions from earlier days. Answer them on paper before checking. Wrong answers are useful: mark them and put the underlying move on tomorrow's list.

### 4. Six-steps write-up from day 1

**Why it works.** A fixed structure removes decisions about how to present, leaving all your attention for the physics and algebra. It also makes errors easy to find, because each step has a job, and it matches how marks are awarded for method.

**Do this.** Write every exercise solution in the six-step format (see the Six-Steps Write-Up section below), even the trivial ones. Speed comes from habit, so build the habit while the problems are easy.

Physics follows the same rule as the maths. Every physics idea is learned together with its quantum bridge (the classical version, then the quantum version, then what breaks), and the physical-reasoning kit at the end of P5 (units, order of magnitude, limiting case, symmetry) is the physics half of step 5, "Check", of the six-steps stand-in below.

### What we rejected and why

- **Weekly just-in-time primers.** Too gentle. If each tool is taught in the same week you must use it, a rusty learner meets new maths and new physics together, which is exactly what makes the lectures hard now.
- **Compressed bottom-up prerequisites.** This is the traditional path in a smaller box. Around 80% of the time goes on material the module never touches, and you already have longer courses on linear algebra and physics fundamentals for that depth.

## Mistakes That Waste 80% of Beginners' Time

1. **Rebuilding all of calculus and linear algebra "properly" first.**
   *Fix:* learn only the named moves in the sprint; look up anything else at the moment a problem demands it.
2. **Watching and rereading instead of solving.**
   *Fix:* pen on paper within five minutes of starting any session; the ratio should be at least two parts solving to one part reading.
3. **Skipping the boring algebra, then failing at the same step repeatedly.**
   *Fix:* write every algebra line; when the same step fails twice, isolate it as a mini-exercise and drill it (Day 1 exists for this).
4. **Treating the wave function as a wave picture only and missing that the maths is linear algebra.**
   *Fix:* whenever a lecture shows a state, ask "what is the vector, what is the basis, what are the coefficients?"; Day 2 makes this reflex.
5. **Memorising formulas without checking normalisation, units and limiting cases.**
   *Fix:* step 5 of the six steps is mandatory: check that probabilities are in [0, 1] and sum to 1, that units match, and that a limit you know behaves.
6. **Confusing a bra with its ket, or forgetting complex conjugation in inner products.**
   *Fix:* say it aloud each time: "bra means transpose and conjugate"; in any inner product, conjugate the left-hand object first, then multiply.
7. **Reading solutions before a real attempt.**
   *Fix:* a real attempt is at least ten minutes and a full page of written work; only then open the hint, and only after that the solution sketch.

## Five-Pass Lecture Protocol

Use this for every weekly lecture from Week 2 on. Total is roughly two hours plus problem practice.

| Pass | Time | What you do |
|---|---|---|
| 0 | 10 min | Read the quiz and task problems first. Do not solve them; just see what the week is aiming at. |
| 1 | 20 min | Read the Week Companion summary and picture. Skim the lecture for structure only: headings, boxed results, equation numbers. |
| 2 | 45 min | Read the lecture properly, with the companion's notation decoder open beside it. Keep a confusion log (template below): one row for each symbol, step or concept you could not follow. |
| 3 | closed book | Re-derive the week's key result from memory. Where you fail is exactly the gap to fix; go back and repair only that. |
| 4 | as needed | Clone a worked problem from the companion, then solve a fresh variant, then explain the idea aloud in three sentences (the Feynman check: if you cannot say it simply, you have not got it yet). |

### Worked example: Week 2, Postulate 1

**Pass 0 (10 min).** Open the Week 2 quiz and task list. Notice which questions involve bras, kets and inner products. Just note "Postulate 1 is about states living in a space where inner products exist" and move on. You are only collecting targets.

**Pass 1 (20 min).** Read the Week 2 companion's plain-English summary of Postulate 1: a system's state is a vector in a complex vector space with an inner product. Skim the lecture's Postulate 1 section for its headings, boxed statements and equation numbers. Do not try to understand every line yet.

**Pass 2 (45 min).** Read the lecture's Postulate 1 section slowly with the notation decoder open. Typical rows to put in your confusion log:

| Where (lecture § / eq.) | Symbol or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| Postulate 1, first equation | $\lvert\psi\rangle$ | some kind of wave | a vector; the bar-and-angle is just a name tag for it | yes |
| Postulate 1, inner product line | $\langle\phi\lvert\psi\rangle$ | multiply two vectors | conjugate-transpose the left, then dot: gives one complex number | yes |
| Postulate 1, normalisation remark | $\langle\psi\lvert\psi\rangle = 1$ | a coincidence | the length of the state vector is 1, so probabilities can add to 1 | not yet |

Write the row the moment you get stuck, then keep reading; do not stop to fix things mid-flow.

**Pass 3 (closed book).** Close everything. On a blank page, from memory:

- state what Postulate 1 says in one sentence;
- write the definition of the inner product of two column vectors, including the conjugation;
- write down the two inner-product axioms (linearity in the ket; conjugate symmetry, $\langle B\lvert A\rangle = \langle A\lvert B\rangle^*$);
- re-derive the normalisation condition and explain why $\lvert\psi\rvert^2$ is a probability density.

Whatever you cannot reproduce goes back into the log as "not yet" and is the target for tomorrow's warm-up.

**Pass 4.** Take one worked clone from the companion, cover the solution, redo it. Then invent a variant with different numbers (change the vectors, keep the move). Finally say aloud, in three sentences: what a state is, what the inner product measures, and why normalisation matters.

## Six-Steps Write-Up (stand-in)

> **Note.** The university's own "Six steps to problem solving: How to gain marks" page is not in the local exports. This is a stand-in built on standard good practice. If you paste the real page into `module_3_resources.md`, replace this section.

The six steps:

1. **Restate** what is asked, and list the givens.
2. **Draw or write the state** in the right notation (sketch, column vector, ket, or graph).
3. **Name the principle or move** you will use, in words.
4. **Do the algebra**, with every step shown.
5. **Check**: units, normalisation, a limiting case, signs, and that any probability lies in [0, 1].
6. **State the answer** in a full sentence.

### Example on a trivial problem

Problem (a deliberately simple case, not a course problem): normalise $\psi(x) = C$ for $0 \le x \le L$ and $\psi(x) = 0$ elsewhere, with $C$ real and positive.

1. **Restate.** Find $C$ so that $\int_{-\infty}^{\infty}\lvert\psi\rvert^2\,\mathrm{d}x = 1$. Given: $\psi = C$ on $0 \le x \le L$, zero elsewhere, $C > 0$.
2. **Write the state.** $\lvert\psi\rvert^2 = C^2$ on $0 \le x \le L$ and $0$ elsewhere: a flat block of height $C^2$ and width $L$.
3. **Name the move.** Normalisation (Move 4.5): set the total probability to 1; the integrand vanishes outside $[0, L]$, so only that piece contributes.
4. **Algebra.** $1 = \int_0^{L} C^2\,\mathrm{d}x = C^2 L$, so $C^2 = 1/L$.
5. **Check.** $C = 1/\sqrt{L}$ gives a block of height $\lvert\psi\rvert^2 = 1/L$ and width $L$, whose area is $1$, as required. The integrand is positive, so the result is positive, as a probability must be.
6. **Answer.** The wave function is normalised when $C = 1/\sqrt{L}$ (units of inverse square root of length, since $\lvert\psi\rvert^2$ must have units of 1/length).

## Confusion Log Template

Copy this table into your notes for each lecture. Fill a row the moment you are stuck; resolve it at the end of the session or in the next warm-up.

| Where (lecture § / eq.) | Symbol or step | What I think it means | What it actually means | Resolved? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
