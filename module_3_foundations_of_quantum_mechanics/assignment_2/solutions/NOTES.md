# Working notes: Assessment 2 (POF), Module 3

The deliverable is `QT01_POF_solutions.pdf`: 25 pages and one upload. It holds the 9 portfolio problems (pp. 1–20), followed by the Week 6 essay and its references (pp. 21–25). Candidate 672128 is on the title page and in every footer.

---

## 1. Deadline and admin

| Item | Value | Source |
|---|---|---|
| Due | **Mon 26 Oct 2026, 10:00 UK = 17:00 Vietnam** | `description.md`, which states both times. UK clocks go back on Sun 25 Oct, so 10:00 GMT is 17:00 ICT and the two agree. The module intro also says "Monday of Week 8 at 10:00 UK". |
| Late window | 24 h, with a flat 5 percentage-point penalty | `description.md`, `module_3_intro.md` |
| Weight | 70% of the module: problems 50%, essay 50% | `description.md` |
| Files | **one file only** (PDF/DOC/DOCX) | `description.md`, plus every week's "condense into a single document" |
| Anonymity | candidate number only | your rule; no name appears in the .tex or the PDF metadata (checked) |
| Essay format | numerical referencing, pages numbered sequentially | `description.md` (footer gives "Page n of 25") |

## 2. Source diff (every copy of each question)

I compared four copies: the instructor `.tex` template (authoritative), its PDF, your Canvas export `Assessment_2_Portfolio.md`, and the weekly `week_N_content.md` pages.

| Problem | Difference | Every reading, computed |
|---|---|---|
| W2 P1(d) | template / week page: "limiting cases $b=a$ and $b=2a$"; export: "$b\to2a$ and $b\to a$" | Both readings give $P(x<a)=1/2$ at $b=2a$ and $P\to1$ as $b\to a$. Literally, $b=a$ is $0/0$ in the 2nd branch, so the solution treats it as $b\to a^+$ and says so. |
| W2 P1(d) | "left of $a$" vs "left of $x=a$" | same quantity |
| W5 P2 | the labels $\lvert\psi_1\rangle,\lvert\psi_2\rangle$ are identical in all copies but **ambiguous**: they could mean $n=1,2$ or "first and second states" $n=0,1$ | $n=1,2$ (Week 5 lecture convention, $\lvert\psi_0\rangle$ = ground): $\langle p\rangle=-\sqrt{m\hbar\omega}$. **$n=0,1$: $\langle p\rangle=-\sqrt{m\hbar\omega/2}$.** **Confirmed $n=1,2$:** the Week 5 lecture defines number states by $\hat N\lvert\psi_n\rangle=n\lvert\psi_n\rangle$ with $\lvert\psi_0\rangle$ the ground state (Eqs. 5.14–5.15), and the question says "two number states". The solution cites this in "Given". Both values are checked in `verify.py`. |
| W7 P1 | $\sigma,\tau$ as Pauli ($\pm1$) or spin ($\pm\hbar/2$) operators | Every answer is 0 under either reading (stated in the solution). |
| All others | no substantive difference; no dropped `\sqrt` this time (W4: $\sqrt3/3,\,2/3,\,\sqrt2/3$ in every copy, norm exactly 1; W5: $5,4,3$ over $\sqrt{50}$ in every copy, norm exactly 1) | n/a |

Template marks: 16+6+12+8+5+17+20+6+10 = **100**, which matches "100 points possible".

**Word count.** The module intro says "2100 words" for the whole assessment, and the brief says the essay is 1,200 words. I read 2100 as the total equivalent (problems + 1200 essay), so the binding limit is the essay's 1,200. Essay counts (from `essay_check.py`):

| Reading | Words |
|---|---|
| body prose only (agreed rule) | 1119 |
| + headings | 1132 |
| + table and caption (strictest) | 1198 |

The body is a little under the 1150 aim. I chose that so that **no reading of the rule exceeds 1200**. There's essentially no room left under the strictest count (2 words), so keep re-voicing word-neutral.

## 3. Verification (none of it re-runs the write-up's algebra)

`verify.py`: 83/83 PASS (`verify_output.txt`). Each problem was checked a different way:
- W2 P1: quadrature at 3 values of (a,b), plus the numerical limits.
- W2 P2: 1000 random complex vectors.
- W3 P1 and W4 P2(d): finite-difference derivatives with grid quadrature on complex test functions. There's also a control showing that a complex $V$ breaks Hermiticity.
- W3 P2: radial normalisation plus a real 1 pm cube average. The ratio comes out at 7.26, 1.8% below e², which is quoted in the solution as the size of the approximation.
- W4 P1: Monte Carlo of 20,000 ensembles.
- W4 P2: random Hermitian matrices.
- W5: 40-level ladder matrices with `expm` time evolution, plus independent position-space Hermite functions. Ehrenfest consistency was also checked.
- W7: Kronecker products, the full $\langle\sigma_i\tau_j\rangle=-\delta_{ij}$ matrix, and a "Bob first" projective simulation.

The document: 0 overfull boxes and 0 undefined references. All 25 rendered pages were read. Fixes made after reading: six over-wide equations split, a broken identity glyph (`\mathbb 1`) replaced with $\mathbb I$, cramped answer fractions, and table spacing.

## 4. Essay sources

Details are in `verified_sources.md`. 27 references, numbered in order of first citation (checked by `essay_check.py`). Every cite has an entry and vice versa. All 25 DOIs resolve on Crossref with matching title, volume, pages and year. The arXiv translation [2] matches its title and author on the arXiv API. I re-checked all of these myself, separately from the research agent. The 27th is the course notes.

- **Left out:** the Nobel 1943 page could not be opened (HTTP 403). If you want a web-page source, open https://www.nobelprize.org/prizes/physics/1943/summary/ yourself, then add it with an access date.
- Industry qubit-count press claims (Intel/Diraq) were not verifiable, so they are not used.
- The essay mixes textbook [6], course notes [5], an original paper and its translation [1,2], reviews [4,8,13,21,23,24] and research papers. The brief asks for that range.

## 5. Rebuild

```bash
python3 build.py && tectonic -X compile --keep-logs QT01_POF_solutions.tex
python verify.py          # needs numpy + scipy
python3 essay_check.py    # citation order + word counts
```
`build.py` copies the problem statements byte-for-byte from the instructor template and stops with an error if any placeholder or `123456` survives.

## 6. Review pass (24 Oct 2026)

- W4 P1: the spread is $\sqrt{NP(1-P)}=13.4,\ 14.1,\ 11.8$, so the text now says 12–14. The Monte Carlo now checks the spreads as well as the means.
- W5 P2: phase variants (+i gives +√(mħω); a real coefficient gives 0) are now actually computed in `verify.py`. Every remaining "checked numerically" claim maps to a PASS line.
- W3 P1 / W4 P2(d): replaced "normalisable ⇒ vanishes at ∞", which is false. The operator domains are now stated (ψ, ψ′ ∈ L² for p̂; ψ, ψ′, ψ″ ∈ L² for Ĥ), with a proof that the boundary terms vanish on them.
- Essay: [10] is now identified as the ⁴⁰Ca⁺ optical-qubit result. [11] says that passing the threshold is necessary for fault tolerance but is not a fault-tolerant computer. The timeline now reads: spin postulated in 1925, splitting first attributed to spin in 1927 (Fraser), per [3].
