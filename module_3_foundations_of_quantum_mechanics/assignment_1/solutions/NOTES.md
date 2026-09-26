# Working notes — Assessment 1 (PRB)

Things to check before you submit, and the reasoning behind two choices I made for you.

---

## 1. The Canvas markdown export lost its `\sqrt` commands

`assignment_1/Assessment_1_Problem_Set.md` and your professor's LaTeX template disagree about two states. Every difference is exactly one missing `\sqrt`, which is the signature of a lossy markdown export rather than two genuinely different problems.

| | Canvas `.md` says | Template `.tex` says |
| :--- | :--- | :--- |
| Q10 state | $\frac{1}{3}\|\phi_1\rangle - \frac{2}{3}\|\phi_2\rangle + \frac{i}{3}\|\phi_3\rangle$ | $\frac{1}{\sqrt{3}}\|\phi_1\rangle - \frac{\sqrt{2}}{\sqrt{3}}\|\phi_2\rangle + \frac{i}{\sqrt{3}}\|\phi_3\rangle$ |
| Q11 state | $\frac{1}{7}[2\|\phi_1\rangle + 3\|\phi_2\rangle + \|\phi_3\rangle + \|\phi_4\rangle]$ | $\frac{1}{\sqrt{7}}[\sqrt{2}\|\phi_1\rangle + \sqrt{3}\|\phi_2\rangle + \|\phi_3\rangle + \|\phi_4\rangle]$ |

**The template is authoritative**, for two reasons:

1. The template's Q11 state is *exactly normalised*: $\frac{2+3+1+1}{7} = 1$. The Canvas version gives $\frac{4+9+1+1}{49} = \frac{15}{49}$, which is not 1 and is not a tidy number either. A problem author choosing coefficients deliberately picks the normalised set.
2. A markdown converter that drops `\sqrt` but keeps its argument turns `\frac{1}{\sqrt{7}}` into `\frac{1}{7}` and `\sqrt{2}` into `2` — which is precisely the pattern observed, in both questions.

### What changes if the Canvas version were taken literally

**Q10.** The template state has norm $4/3$, giving $P(a_3) = \frac{1/3}{4/3} = \boxed{1/4}$.

There is a second plausible reading of what the stripped Canvas text was hiding, namely $\frac{1}{3}, -\frac{\sqrt{2}}{3}, \frac{i}{3}$ (i.e. `\frac{\sqrt{2}}{3}` losing its `\sqrt`). That state has norm $\frac{1+2+1}{9} = \frac{4}{9}$ and gives $P(a_3) = \frac{1/9}{4/9} = 1/4$ — **the same answer**. Only the literal Canvas reading $\frac13, -\frac23, \frac{i}3$ differs, giving norm $2/3$ and $P(a_3) = \frac{1/9}{2/3} = 1/6$.

So $1/4$ is the robust answer: two of the three readings give it, including the one written explicitly in your professor's own file.

**Q11 and Q12.** Template: probabilities $\frac27, \frac37, \frac17, \frac17$. Canvas literal: the state is un-normalised with $\langle\psi_0|\psi_0\rangle = \frac{15}{49}$, so the probabilities become $\frac{4}{15}, \frac{9}{15}, \frac{1}{15}, \frac{1}{15}$. The energies and the $A$ values are unaffected either way.

**Q13 is unaffected.** The collapse argument gives $3a_0$ regardless of the coefficients, since it depends only on $n=2$.

### What to do about it

Open the actual Canvas quiz and read the *rendered* Q10 and Q11 — the browser will show the square roots if they are there. Thirty seconds settles it. If the rendering matches the template, change nothing.

If it turns out Canvas really does show no square roots, the method in every solution is unchanged: check the norm, divide by it, apply the Born rule. Only the arithmetic in the last line of Q10, Q11 and Q12 needs swapping for the values above. The method marks, which is where most of the credit sits, are safe either way.

---

## 2. Why Q10 needs a normalisation step at all

Worth being ready to defend this in case a marker expects the naive answer. The Born rule as stated in the Week 3 lecture applies to a **normalised** state: $P(\lambda_n) = |\langle\phi_n|\psi\rangle|^2$, derived on the assumption $\sum_n |\alpha_n|^2 = 1$. The Q10 state does not satisfy that, so taking $|i/\sqrt{3}|^2 = 1/3$ directly would be wrong — the three outcomes would then sum to $4/3$, which is not a probability distribution.

The lecture gives the un-normalised form explicitly for expectation values, $\langle\hat{A}\rangle_\psi = \frac{\langle\psi|\hat{A}|\psi\rangle}{\langle\psi|\psi\rangle}$, and the probability version used in the solution is the same idea applied to a single outcome. The solution shows both routes — divide by the norm, or normalise the state first — and they agree, which is the cleanest way to demonstrate the point.

---

## 3. The compiled PDF

`QT01_PRB_solutions.pdf` is built and checked in: **20 pages**, zero overfull boxes, all cross-references resolved, Figure 1 placed inside Question 2 and referenced from parts (a), (c) and (d). Every page has been inspected visually.

**Canvas numbering is carried throughout.** Your professor's template groups the 13 Canvas questions into 5 problems (8 + 37 + 22 + 8 + 25 = 100, matching the Canvas points exactly). Because that grouping is not obvious to someone reading down the Canvas list, the PDF states it in two places: a Canvas range in each section heading ("Question 2 (Canvas questions 2--5)") and a `(Canvas Qn)` tag on every sub-part heading. Nothing is omitted — all 13 parts are answered. Marks are shown once, in your professor's grey question boxes; the duplicates that had appeared in the solution headings were removed.

It was built with **Tectonic** (`brew install tectonic`), a single self-contained binary that downloads the LaTeX packages it needs on first use — about 20 MB installed, against roughly 4 GB for MacTeX. It handled your professor's preamble unchanged; no package substitutions were needed.

To rebuild after editing the `.tex`:

```
cd assignment_1/solutions
tectonic -X compile QT01_PRB_solutions.tex
```

Tectonic reruns TeX automatically until references settle, so there is no need to invoke it twice, and it cleans up `.aux`/`.log`/`.xdv` afterwards. Add `--keep-logs` if you want the log to inspect warnings.

Overleaf remains a fine fallback: upload the `.tex`, put the PNG in a `figures/` folder, compile with pdfLaTeX, and run it twice so `\ref{fig:psi_proba}` resolves.

The title page carries candidate number **672128**.

## 4. Before you submit

- [x] Candidate number on the title page set to 672128.
- [ ] Q10 and Q11 states checked against the *rendered* Canvas quiz (section 1 above).
- [x] PDF compiled (20 pages); Figure 1 appears and resolves as "Fig. (1)". Rebuild only if you edit the `.tex`.
- [ ] Solutions read through and re-voiced in your own words where the phrasing does not sound like you — the brief requires the workings to be your own, and you should be able to reproduce every step unaided.
- [ ] Every derivation checked once by you independently. The results to confirm: $B = 2\sqrt{\beta/3}$; $\langle x\rangle = -1/(4\beta)$; mode at $x=0$; $[\hat{x},\hat{p}] = i\hbar$; $P(a_3) = 1/4$; energies $E_0, 4E_0, 9E_0, 16E_0$ with $\frac27, \frac37, \frac17, \frac17$; $A$ values $2a_0 \dots 5a_0$ with the same probabilities; final answer $3a_0$.
- [ ] Pointer lines typed into Canvas Q1–Q13 (see `CANVAS_ANSWERS.md`, Part A), in one browser tab only.
- [ ] PDF uploaded at Q14, then **Submit** pressed.

Deadline: **1 October, 23:00** (Canvas), with the module page also quoting 17:00 UK on the Thursday of Week 4 and a 24-hour lateness period. The two stated times disagree — treat 17:00 as the real deadline and do not rely on the later one.

---

## 5. Regenerating the figure

`make_figure.py` needs `matplotlib` and `numpy`, which are not in your system Python. From this directory:

```
python3 -m venv .venv && ./.venv/bin/pip install matplotlib numpy
./.venv/bin/python make_figure.py
```

It writes `figures/psi_probability_density.png`. All quantities are plotted in dimensionless units ($\beta x$ horizontally, $|\psi|^2/\beta$ vertically), so the figure is correct for any $\beta > 0$ and needs no regeneration unless you want to restyle it.
