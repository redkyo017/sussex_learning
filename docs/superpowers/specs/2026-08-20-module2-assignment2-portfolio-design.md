# Design: Module 2 Assignment 2 Portfolio — Substrata Quantum Ltd

**Date:** 2026-08-20
**Assignment:** Module 2 (Emerging Markets for Quantum Technology), Assessment 2 — portfolio, 1500 words, 40% of module grade, due Mon 25 Aug 2026, submitted via Canvas (doc/docx/pdf), single file upload. Note: the brief states both "Due Monday by 16:00" and "Due on Monday of Week 8 at 10:00 UK time" — work to 10:00. A 24-hour lateness period with penalty exists.
**Task:** Three items totalling 1500 words — Market Opportunity Navigator (4 worksheets), Value Proposition Canvas (1 worksheet), Business Model Canvas (1 worksheet), covering Weeks 5–7.

## Requirement interpretation (the load-bearing decision)

The brief reads "Item 1 – Market Opportunity Navigator (4 worksheets, **equivalent to 500 words**)". "Equivalent to" is the university's conversion of a filled worksheet into a word allowance: **the three completed canvases ARE the 1500 words. No separate essay is required**, and adding one would roughly double the assessed length. The rubric's references to "essay" are Sussex boilerplate shared across modules.

Consequence: marks for Knowledge, Critical thinking and Reading must be earned *inside* the worksheets, so every `Notes:` field carries analytical prose with Harvard citations rather than bullet fragments.

Second consequence: the MON supplied for this module is the **impact-oriented variant** (Part 2 leads with Problem Severity, Pertinent Solution "avoids secondary harm", Impact Reach). That block is where learning outcome 2 (responsible innovation) is assessed, so RI is woven through Impact scoring, the VPC's social gains and the BMC's stakeholders — not bolted on as a section.

## Approved decisions

- **Venture:** Substrata Quantum Ltd — a proposed UK spin-out selling cold-atom gravity gradiometry as a subsurface survey service.
- **Chain:** MON Part 3 selects the primary opportunity → VPC drills into one segment inside it → BMC answers the value-capture question the MON raised.
- **Voice:** same as Assignment 1 — plain UK academic English, concrete, varied sentence length, positions taken and limits conceded.
- **Referencing:** Harvard author-date, 15 sources, reference list excluded from word count.
- **Deliverable:** one .docx built by filling the supplied blank templates (not a rebuild in Markdown), so the marker sees the worksheets they issued.
- **Model split:** reasoning, content and fact-verification on the primary model; mechanical docx assembly delegated to Sonnet (user's instruction).

## Venture rationale, and what was rejected

Chosen because it is the module's own worked example (Week 5 notes list quantum sensing for "underground mapping (construction), oil/gas exploration, and GPS-free navigation" and place sensors "on the cusp of commercial launch"), because the customer pain is quantified and public, and because Teece bites properly: survey firms already own the distribution channel, so "sell instruments vs sell surveys and data" is a live strategic choice rather than a textbook recital.

Rejected alternatives:
- **Quantum-assured timing / PNT for critical infrastructure** — strong regulatory pull, but the customer pain is abstract and incumbent atomic-clock vendors crowd it.
- **Wearable OPM-MEG for healthcare** — compelling and matches the NHS mission, but medical-device regulation pushes every opportunity into "high challenge", flattening the MON comparison.
- **Quantum computing application layer (pharma/logistics)** — closest to the MSc subject matter, but every opportunity scores as a Moon Shot with no near-term revenue, and "we cannot yet beat a classical solver" is hard to write honestly in a VPC.

The decisive criterion was that the MON must produce a *genuine* spread of scores. An option set that scores identically makes Part 3 a formality and forfeits the Application marks.

## Content architecture

**MON Part 1 — four core abilities** stated as functions and properties, independent of product (as the tool requires): differential cold-atom interferometry; rejection of real-world noise; Bayesian inference under uncertainty; field engineering of a laboratory instrument.

**Three opportunities and their scored outcome:**

| # | Opportunity | Category | Agile strategy | Role |
|---|---|---|---|---|
| 1 | Pre-excavation utility/void survey | Gold Mine | Pursue now | Primary |
| 2 | Mineral and geothermal exploration | Moon Shot | Keep open | Back-up |
| 3 | GPS-denied navigation | Moon Shot | Keep open | Growth |

**Deliberate critical-thinking hooks** (these are where the marks are, so preserve them in any rewrite):
- Delta.g is named as a real, funded competitor already ahead on the same road — external risk scored HIGH for the primary opportunity, not hidden.
- Potential Market Volume for the primary opportunity is scored MEDIUM, not HIGH: it is a second pass on difficult ground, not every job.
- Part 3 states that the back-up hedges *market* risk but not *technical* risk, because all three options need the same sensor to work.
- The VPC states its own limitation: slower per metre and coarser than radar in good conditions, so a second pass rather than a replacement. Over-claiming would put crews at risk, which is where RI becomes a design constraint.
- BMC treats the channel partner, the crews and the accumulating dataset as the co-specialised complementary assets, since appropriability is weak — the same Teece spine as the Assignment 1 essay.

## Verified facts and their sources

Verified online on 2026-08-20 before drafting; do not re-cite these without the source attached.

- ~60,000 utility strikes/year in the UK, ~£2.4bn economic cost, one in every 65 holes dug, true cost of a strike = 29× the direct repair bill — Utility Strike Avoidance Group.
- ~4 million km of buried pipes and cables; a hole dug every seven seconds; NUAR live across England and Wales — Geospatial Commission. **The 4 million km is the size of the buried network, NOT the amount of it with faulty records** — do not let a compression pass merge the two clauses into "records are wrong across 4 million km" (that error was introduced and caught on 2026-08-23).
- First outdoor quantum gravity gradiometer survey: 2 m tunnel found at ~1.89 m depth, statistical uncertainty 20 E, SNR 8, Bayesian bounds — Stray et al. (2022), *Nature* 602, 590–594.
- PAS 128:2022 Survey Type B mandates electromagnetic location (EML) *and* GPR as a minimum, "plus other geophysical methods as appropriate"; gravity/gravimetry is named nowhere in the standard (0 hits in the CICES client specification guide). So gravity is not prohibited — it is simply not a named technique, and cannot on its own support a QL-B claim. B3 = detected by one technique with no reliable depth; B4 = expected from records but not detected, shown as an assumed route — BSI / CICES.
- Delta.g: University of Birmingham spin-out, £4.6m oversubscribed seed round announced 26 September 2025, led by Serendipity Capital with NSSIF and SCVC — University of Birmingham press release (cited; the primary source, replacing a Quantum Insider link that pointed only at the site root).
- Quantum navigation on aircraft by 2030 mission — HM Government National Quantum Strategy.

## Word budget

Allowance 1500 (500 per item). Measured by `build/wordcount.py`, which diffs the built document against the blank templates: **1748 words — MON 613, VPC 543, BMC 592 (+17%)**; the Part 2 orientation sentence and the bold "Opportunity n — <name>" card headings added 2026-08-23 keep the three scorecards reading as three cards rather than a copy-paste. Template prompt text, checkbox labels, the title block and the reference list are excluded.

History: 1691 (+13%) at first draft; phrasing trim to 1633 (+9%) on 2026-08-21. On 2026-08-23 a review found that the VPC/BMC notes left roughly a third of the printed prompts unanswered (e.g. "expected outcomes or exceed expectations?", "how much revenue will each stream contribute?"). Every box was rewritten so each prompt is answered in order, led by the prompt's keyword ("Interaction:", "Barriers:", "Suppliers:" …) so coverage is legible to the marker. That costs ~60–75 words per prompted box however tightly phrased; four compression passes brought the total from 1806 to 1723 without removing any answer, citation or critical-thinking hook (the fourth, on 2026-08-23, retouched all 17 VPC/BMC notes for phrasing only, -34 words). Phrasing alone bottoms out near 1723 (a later fact-check pass added 24 words back for accuracy and two framework citations, giving 1747); going to +10% would require deleting direct answers to printed prompts, which was judged the worse trade for a worksheet-based submission.

Also on 2026-08-23: the MON Part 2 rationales, previously two paragraphs parked at the foot of each scorecard ("Impact and potential:", "Challenge:") plus an unlabelled orphan sentence under Opportunity 1's category ticks, were split into one `Notes:` paragraph directly under each Overall Impact / Overall Potential / Overall Challenge score, with a labelled category note for Opportunity 1. The blank template has no Part 2 notes field; these are additions, placed beside the score they justify.

## Deliverable pipeline

Source of truth for every word: `module_2_emerging_markets_for_quantum_technology/assignment_2/portfolio_content.md`.
Build scripts: `assignment_2/build/` — see its README. Last rebuilt in place 2026-08-23; `portfolio_content.md` cross-checked line for line against the built document. Operational steps live in `assignment_2/RUNBOOK.md`.
Title block: "Assessment 2 Portfolio" + one-line subtitle naming the business; the venture name Substrata Quantum Ltd is a working label used in this spec only, not in the document (changed 2026-08-23).
Submission file: `assignment_2/Assessment2_Quantum_Portfolio.docx` (single upload; PDF export from Word is equally acceptable).

**Known duplication:** the fill scripts hardcode the prose rather than parsing `portfolio_content.md`. Editing the markdown alone does not change the .docx. See the build README.

## Out of scope

- No separate essay (see requirement interpretation above).
- No submission on the user's behalf; upload and any final personal edits are the user's.
- No fabricated figures: every number traces to a named source, verified before drafting.
