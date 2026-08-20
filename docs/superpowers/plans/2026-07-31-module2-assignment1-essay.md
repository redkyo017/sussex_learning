# Module 2 Assignment 1 Essay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a submission-ready 1500-word Harvard-referenced essay ("Capturing the Quantum Dividend") answering "How can policymakers and entrepreneurs develop the UK quantum industry? Propose at least three concrete actions", as a .docx file.

**Architecture:** Verify external sources first, then build the reference list, then draft the essay against the approved section/word budget, then run style and accuracy passes, then convert to docx. Each stage commits its output so the draft history is auditable.

**Tech Stack:** Markdown drafting; `wc`/`grep` for verification; pandoc for docx conversion; WebSearch/WebFetch for source verification.

## Global Constraints

- Essay body exactly ~1500 words (accept 1425–1575); reference list excluded from count.
- Thesis: UK creates quantum value but must act to capture it (Teece 1986); actions: (1) complementary assets, (2) skills, (3) demand + responsible innovation.
- Harvard author-date referencing; at most 1–2 short direct quotes; everything else paraphrased in original sentences.
- Style: UK academic English, third person, flowing prose, no bullets/headings mid-essay beyond plain paragraph flow; banned tells: "delve", "moreover/furthermore" chains, "it is important to note", adjective triads, em-dash overuse, template paragraphs.
- Every figure must trace to a named source; unverifiable figures are cut, never guessed.
- No fabricated sources, quotes, or page numbers.
- Working directory for outputs: `module_2_emerging_markets_for_quantum_technology/assignment_1/`.
- Spec: `docs/superpowers/specs/2026-07-31-module2-assignment1-essay-design.md`.

---

### Task 1: Verify external sources

**Files:**
- Create: `module_2_emerging_markets_for_quantum_technology/assignment_1/verified_sources.md`

**Interfaces:**
- Consumes: claims listed below (from spec "Extras to verify").
- Produces: `verified_sources.md` — one entry per claim with fields: Claim, Verdict (VERIFIED/CUT), Publisher, Year, Title, URL, Access date. Tasks 2, 3 and 5 rely on these fields verbatim.

- [ ] **Step 1: Verify each of these six claims via WebSearch/WebFetch**

1. DSIT announced five quantum missions in November 2023 (UK National Quantum Strategy Missions).
2. NIST published its first post-quantum cryptography standards in 2024 (FIPS 203/204/205).
3. The "$450–850bn global economic benefit over 15–30 years" estimate — find the primary source (the 2023 UK National Quantum Strategy cites it; identify who it attributes it to, likely BCG/McKinsey). If no primary attribution found, mark CUT and cite the figure as "HM Government (2023)" only.
4. South Korea's MSIT quantum strategy (27 June 2023; KRW 3 trillion to 2035).
5. Singapore National Quantum Strategy (30 May 2024; ~S$300m over five years).
6. Quantum talent shortage ratio (~3 vacancies per qualified candidate — likely McKinsey Quantum Technology Monitor). If not confirmed, mark CUT.

For each: record Claim / Verdict / Publisher / Year / Title / URL / Access date in `verified_sources.md`. Prefer gov.uk, nist.gov, msit.go.kr, nqo.sg, official publisher pages.

- [ ] **Step 2: Verify the file lists all six claims with verdicts**

Run: `grep -c "Verdict" module_2_emerging_markets_for_quantum_technology/assignment_1/verified_sources.md`
Expected: 6

- [ ] **Step 3: Commit**

```bash
git add module_2_emerging_markets_for_quantum_technology/assignment_1/verified_sources.md
git commit -m "Module 2 | assignment 1: verified external sources"
```

### Task 2: Build the Harvard reference list

**Files:**
- Create: `module_2_emerging_markets_for_quantum_technology/assignment_1/references.md`

**Interfaces:**
- Consumes: `verified_sources.md` (Task 1) for the extras' publisher/year/title/URL.
- Produces: `references.md` — a `## References` section with alphabetical Harvard entries. Task 3 cites only names/years present here; Task 6 appends this file to the essay.

- [ ] **Step 1: Write the core module-source entries**

```markdown
## References

EPSRC and Kantar Public (2018) *Quantum technologies public dialogue: full report*. Swindon: Engineering and Physical Sciences Research Council.

HM Government (2023) *National quantum strategy*. London: Department for Science, Innovation and Technology.

Kline, S.J. and Rosenberg, N. (1986) 'An overview of innovation', in Landau, R. and Rosenberg, N. (eds.) *The positive sum strategy: harnessing technology for economic growth*. Washington, DC: National Academy Press, pp. 275–305.

Pavitt, K. (1991) 'What makes basic research economically useful?', *Research Policy*, 20(2), pp. 109–119.

Quantum Technologies Strategic Advisory Board (2015) *National strategy for quantum technologies: a new era for the UK*. Swindon: EPSRC.

Rogers, E.M. (2003) *Diffusion of innovations*. 5th edn. New York: Free Press.

Rothwell, R., Freeman, C., Horlsey, A., Jervis, V.T.P., Robertson, A.B. and Townsend, J. (1974) 'SAPPHO updated: project SAPPHO phase II', *Research Policy*, 3(3), pp. 258–291.

Rotolo, D., Hicks, D. and Martin, B.R. (2015) 'What is an emerging technology?', *Research Policy*, 44(10), pp. 1827–1843.

Stilgoe, J., Owen, R. and Macnaghten, P. (2013) 'Developing a framework for responsible innovation', *Research Policy*, 42(9), pp. 1568–1580.

Teece, D.J. (1986) 'Profiting from technological innovation: implications for integration, collaboration, licensing and public policy', *Research Policy*, 15(6), pp. 285–305.
```

Then add one Harvard entry per VERIFIED item from `verified_sources.md`, e.g. (adjust to verified details):

```markdown
Department for Science, Innovation and Technology (2023) *National quantum strategy missions*. London: DSIT. Available at: <verified URL> (Accessed: <date>).

Ministry of Science and ICT (2023) *South Korea's quantum science and technology strategy*. Sejong: MSIT. Available at: <verified URL> (Accessed: <date>).

National Institute of Standards and Technology (2024) *NIST releases first three finalized post-quantum encryption standards*. Gaithersburg, MD: NIST. Available at: <verified URL> (Accessed: <date>).

National Quantum Office (2024) *Singapore national quantum strategy*. Singapore: NQO. Available at: <verified URL> (Accessed: <date>).
```

(The `<verified URL>`/`<date>` values MUST be replaced with the actual fields from `verified_sources.md`; if any remain, the step is incomplete. Drop entries for CUT items.)

- [ ] **Step 2: Verify alphabetical order and no placeholders**

Run: `grep -n "<verified\|<date" module_2_emerging_markets_for_quantum_technology/assignment_1/references.md`
Expected: no output. Then visually confirm alphabetical order.

- [ ] **Step 3: Commit**

```bash
git add module_2_emerging_markets_for_quantum_technology/assignment_1/references.md
git commit -m "Module 2 | assignment 1: Harvard reference list"
```

### Task 3: Draft the essay

**Files:**
- Create: `module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md`

**Interfaces:**
- Consumes: spec structure; `references.md` (cite only names/years listed there); `verified_sources.md` figures; module content summaries in conversation/spec.
- Produces: `essay_draft.md` — title line, then 6 sections of flowing prose (no internal headings in the final text; use HTML comments `<!-- intro -->` etc. as section markers so word counts per section can be checked, to be stripped in Task 6).

- [ ] **Step 1: Draft introduction (~180 w) and diagnosis (~200 w)**

Content contract — introduction: open on the paradox (first national quantum programme in the world, 2013, £270m — QT SAB 2015; top-three on quality of quantum science and second only to the US in quantum companies — HM Government 2023); pivot: invention does not guarantee profit; state thesis (Teece 1986: creating vs capturing value) and name the three actions; one scope sentence. Diagnosis: quantum is science-intensive but the linear model misleads (Kline and Rosenberg 1986); appropriability is weak because patents can be invented around and key knowledge is tacit (Teece 1986; Pavitt 1991); therefore complementary assets decide who profits; EMI CAT-scanner case in two sentences (invented it, lost the market within six years to firms holding manufacturing, distribution and service assets); risk statement: the UK as the world's quantum lab rather than its quantum industry.

- [ ] **Step 2: Check section word counts**

Run: `awk '/<!-- intro -->/,/<!-- diagnosis -->/' module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md | wc -w`
Expected: ~180 (±15%); repeat for diagnosis (~200).

- [ ] **Step 3: Draft Action 1 — complementary assets (~330 w)**

Content contract: policymakers sustain shared fabrication/packaging/testbeds (NQCC, hubs, missions programme funding lines from HM Government 2023 — use at most two figures, e.g. £2.5bn/ten years and the missions programme); entrepreneurs apply Teece's decision rule (weak appropriability + specialised assets → build or partner strategically, not licence away; the hollow-corporation risk); IBM's services pivot as value-capture exemplar; critical concession: infrastructure must be tied to missions/demand or it is supply-push (Kline and Rosenberg 1986).

- [ ] **Step 4: Draft Action 2 — skills (~330 w)**

Content contract: Pavitt (1991) — trained people, not papers, are the chief economic return on public science because technological knowledge is tacit and person-embodied; the 2023 Strategy's 1,000 additional postgraduate researchers target; talent scarcity (use the verified ratio if Task 1 verified it, else qualitative "vacancies outstrip qualified candidates"); competitive pressure from Korea (KRW 3tn, 2,500 core professionals by 2035 — MSIT 2023) and Singapore (scholarships — NQO 2024), figures only if verified; entrepreneurs: recruit via CDTs/placements to internalise tacit knowledge; critical concession: training without retention (visas, salaries, international mobility) leaks the return abroad.

- [ ] **Step 5: Draft Action 3 — demand and licence to operate (~330 w)**

Content contract: SAPPHO (Rothwell et al. 1974) — user-needs attention is the strongest success discriminator; only 25–33% of relevant UK businesses have begun preparing for quantum (HM Government 2023); policymakers act as intelligent lead customer (procurement commitments; post-quantum cryptography migration as concrete early demand — NIST 2024 if verified); Rogers (2003) — trialability and observability argue for demonstrators/testbeds; entrepreneurs sell solutions to user problems, not qubits; responsible innovation woven in, not bolted on: Collingridge dilemma via Stilgoe, Owen and Macnaghten (2013) AREA framework; EPSRC/Kantar (2018) dialogue found engagement increased support (health, security applications) — early engagement is market-building.

- [ ] **Step 6: Draft conclusion (~130 w)**

Content contract: restate thesis without repeating intro wording; the three actions are mutually reinforcing (assets capture value, people embody it, demand realises it); closing judgement: the choice is between repeating EMI at national scale and converting first-mover science into first-mover industry. No new citations needed.

- [ ] **Step 7: Full word count and citation check**

Run: `sed 's/<!--[^>]*-->//g' module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md | wc -w`
Expected: 1425–1575.
Then: every in-text citation (grep for `(19` and `(20`) has a matching entry in `references.md`, and every reference is cited at least once.

- [ ] **Step 8: Commit**

```bash
git add module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md
git commit -m "Module 2 | assignment 1: first full essay draft"
```

### Task 4: Humanising and style pass

**Files:**
- Modify: `module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md`

**Interfaces:**
- Consumes: Task 3 draft.
- Produces: same file, style-clean; Task 5 audits this text.

- [ ] **Step 1: Banned-tell scan**

Run: `grep -in "delve\|moreover\|furthermore\|it is important to note\|in today's\|landscape\|crucial\|pivotal\|holistic\|leverage" module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md`
Expected: no output (or deliberate, justified single uses — rewrite otherwise).

- [ ] **Step 2: Rhythm and template pass (manual edit)**

Check and fix: no two consecutive paragraphs open with the same syntactic shape; each section contains at least one short sentence (<10 words); em-dash count ≤ 3 across the essay (`grep -o "—" file | wc -l`); no sentence over ~45 words; contract at least one hedged judgement per action section ("this only works if…", "the harder problem is…").

- [ ] **Step 3: Re-run word count (must remain 1425–1575)**

Run: `sed 's/<!--[^>]*-->//g' module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md | wc -w`

- [ ] **Step 4: Commit**

```bash
git add module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md
git commit -m "Module 2 | assignment 1: style and humanising pass"
```

### Task 5: Accuracy and integrity audit

**Files:**
- Modify: `module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md` (fixes only)

**Interfaces:**
- Consumes: `essay_draft.md`, `verified_sources.md`, `references.md`, module source files under `module_2_emerging_markets_for_quantum_technology/week_*/sources/`.
- Produces: audited final text for Task 6.

- [ ] **Step 1: Figure-by-figure trace**

List every number in the essay (`grep -oE "£[0-9][^ ]*|\\$[0-9][^ ]*|[0-9]+%|[0-9],[0-9]{3}" file`). For each: confirm it appears in the cited source (module source file or verified_sources.md entry). Fix or cut any that fail. Specific known-risk figures: £270m (QT SAB 2015 — module file), £2.5bn (HM Government 2023 — module file), 25–33% (HM Government 2023 — module file), 1,000 postgrads (HM Government 2023), KRW 3tn (MSIT — Task 1), talent ratio (Task 1 verdict).

- [ ] **Step 2: Quote audit**

Run: `grep -c '"' module_2_emerging_markets_for_quantum_technology/assignment_1/essay_draft.md`
Expected: ≤ 4 double-quote characters (i.e. at most 2 quoted strings), each with author-date-page citation, each verified verbatim against the source file.

- [ ] **Step 3: Two-way citation-reference check (repeat of Task 3 Step 7 after edits)**

Every in-text (Author, Year) has a reference entry; every reference entry is cited. Fix mismatches.

- [ ] **Step 4: Commit**

```bash
git add -A module_2_emerging_markets_for_quantum_technology/assignment_1/
git commit -m "Module 2 | assignment 1: accuracy audit"
```

### Task 6: Produce the .docx deliverable

**Files:**
- Create: `module_2_emerging_markets_for_quantum_technology/assignment_1/Assessment1_Quantum_Essay.docx`
- Create (intermediate): `module_2_emerging_markets_for_quantum_technology/assignment_1/essay_final.md`

**Interfaces:**
- Consumes: `essay_draft.md` + `references.md`.
- Produces: the submission file the user edits and uploads.

- [ ] **Step 1: Assemble final markdown**

```bash
cd module_2_emerging_markets_for_quantum_technology/assignment_1
sed 's/<!--[^>]*-->//g' essay_draft.md > essay_final.md
printf '\n' >> essay_final.md
cat references.md >> essay_final.md
```

- [ ] **Step 2: Check pandoc availability and convert**

Run: `which pandoc || brew install pandoc`
Then: `pandoc essay_final.md -o Assessment1_Quantum_Essay.docx`
Fallback if pandoc unavailable and brew fails: `pandoc` via `npx` is not a thing — instead convert with `textutil`: `pandoc`-less path is `cat essay_final.md | sed ...` → write `essay_final.html` (wrap paragraphs in `<p>`) then `textutil -convert docx essay_final.html -output Assessment1_Quantum_Essay.docx`.

- [ ] **Step 3: Verify the docx opens and word count is right**

Run: `textutil -convert txt Assessment1_Quantum_Essay.docx -stdout | wc -w`
Expected: ~1500 body + ~250 references ≈ 1650–1850 total.

- [ ] **Step 4: Send the file to the user and commit**

Send `Assessment1_Quantum_Essay.docx` to the user (SendUserFile), reminding them: (a) do a light personal rewording pass, (b) confirm the Canvas deadline time (brief says both 10:00 and 16:00).

```bash
git add -A module_2_emerging_markets_for_quantum_technology/assignment_1/
git commit -m "Module 2 | assignment 1: final essay and docx deliverable"
```
