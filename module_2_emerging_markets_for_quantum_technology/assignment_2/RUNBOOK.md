# Runbook: Module 2 Assignment 2 portfolio

Operational steps for working on this assignment from any machine. Lives beside the work
it operates. For *why* the portfolio says what it says, read the design spec first:
`docs/superpowers/specs/2026-08-20-module2-assignment2-portfolio-design.md` (repo root).

**What is submitted:** one file — `Assessment2_Quantum_Portfolio.docx`, in this directory.
Canvas takes a single upload, doc/docx/pdf, up to 40MB. Nothing else is uploaded.

---

## 0. Before leaving the machine you are on

Two things do NOT travel with the repo. Do these or the rest of this runbook cannot start.

1. **Push the branch.** A local branch is invisible to every other machine.

       git push -u origin feat/module2-assignment2-portfolio

   No network / no remote? Make a bundle and carry it:

       git bundle create ~/assignment2.bundle feat/module2-assignment2-portfolio
       # elsewhere: git clone ~/assignment2.bundle -b feat/module2-assignment2-portfolio repo

2. **Claude Code's memory is machine-local** (`~/.claude/projects/.../memory/`). It is not in
   the repo and will not be on the new machine. This runbook and the spec are the
   replacement — see step 3 for what to paste.

---

## 1. Prerequisites on the new machine

- git, python3 (3.9+), pip
- Word or LibreOffice, only if you want to eyeball the layout or export PDF

Nothing else. No LaTeX, no pandoc.

---

## 2. Get the work and confirm it is intact

    git clone <repo> && cd sussex_learning
    git checkout feat/module2-assignment2-portfolio
    cd module_2_emerging_markets_for_quantum_technology/assignment_2

    python3 -m venv build/venv
    ./build/venv/bin/pip install python-docx docxcompose

    ./build/venv/bin/python build/verify.py      # expect: OVERALL: ALL CHECKS PASS
    ./build/venv/bin/python build/wordcount.py   # expect: 1723 words total (+15%)

If `verify.py` passes, the document is complete: every box filled, exactly one tick per
criterion group, references present. If it fails, do not edit the .docx by hand — rebuild
(step 4A) and re-verify.

---

## 3. Getting Claude Code up to speed in one paste

Start a session in the repo root and give it this:

> Read `module_2_emerging_markets_for_quantum_technology/assignment_2/RUNBOOK.md` and
> `docs/superpowers/specs/2026-08-20-module2-assignment2-portfolio-design.md`, then
> `module_2_emerging_markets_for_quantum_technology/assignment_2/build/README.md`.
> and `module_2_emerging_markets_for_quantum_technology/assignment_2/CHANGES-2026-08-23.md`.
> I'm continuing Module 2 Assignment 2. <what you want to change>

Reading order matters: the spec carries the decisions and the rejected alternatives, so it
stops a fresh session from re-litigating the venture choice or quietly deleting the
deliberate critical-thinking hooks listed in §Invariants below.

---

## 4. Task recipes

### A. Rebuild the .docx from source

    cd module_2_emerging_markets_for_quantum_technology/assignment_2
    ./build/venv/bin/python build/fill_mon.py
    ./build/venv/bin/python build/fill_vpc.py
    ./build/venv/bin/python build/fill_bmc.py
    ./build/venv/bin/python build/merge.py
    ./build/venv/bin/python build/verify.py

Last rebuilt in place 2026-08-23 (MON Part 2 notes per score; VPC/BMC answer every prompt).

### B. Change the wording

The prose lives in **two** places and both must change:

1. `portfolio_content.md` — the readable source of truth
2. the matching build script — `fill_mon.py` (core abilities, applications, Part 2 scores
   and per-score notes, Part 3 notes), `verify.py` (`required_snippets` if a box's opening words change), `fill_vpc.py` / `fill_bmc.py` (each box's `Notes:`),
   `references.py` (reference list), `merge.py` (`TITLE` / `SUBTITLE`)

Then build to a scratch directory first, so a mistake cannot damage the file you may
already have submitted:

    OUTDIR=/tmp/rebuild ./build/venv/bin/python build/fill_mon.py     # and the others
    OUTDIR=/tmp/rebuild ./build/venv/bin/python build/merge.py
    OUTDIR=/tmp/rebuild ./build/venv/bin/python build/verify.py
    OUTDIR=/tmp/rebuild ./build/venv/bin/python build/wordcount.py

Read the diff against the current file, then rebuild in place (step 4A) once happy.

### C. Check the word count

    ./build/venv/bin/python build/wordcount.py

Counts only inserted prose: template prompts, field labels, checkbox options and the
reference list are excluded. Allowance is 1500 (500 per item); current build is 1723 (+15%), a deliberate
trade recorded in the spec's Word budget section. Do not trim further without re-reading it —
what is left is direct answers to printed prompts and the critical-thinking hooks.

### D. Export a PDF

Open in Word → Save As → PDF. This machine has no LibreOffice and pandoc's PDF route needs
LaTeX, so there is no scripted path. Both .docx and .pdf are accepted; .docx is fine.

### E. Submit

- Deadline: **Monday 25 Aug 2026**. The brief says both "16:00" and "10:00 UK time" —
  work to 10:00. A 24-hour lateness period exists but carries a penalty.
- Upload `Assessment2_Quantum_Portfolio.docx` only. Never upload `MON_filled.docx`,
  `VPC_filled.docx` or `BMC_filled.docx` — they are per-canvas reference copies with no
  title block and no references.
- You may resubmit until the deadline; the last submission before it is the one marked.
  So submit early, read the Turnitin report, and fix with time in hand.

### F. After the Turnitin similarity report

Expect a low score. Matches should be template boilerplate ("What problem are you
solving?"), the reference list, and fixed terms (PAS 128, National Underground Asset
Register) — the same notation-and-formula pattern seen on the maths portfolio, which
scored 6% and was safe. If a *prose* passage is flagged, paraphrase it in
`portfolio_content.md` and the matching script, rebuild (4A/4B), resubmit.

### G. After the mark and feedback

Feedback lands within 15 working days. Record it in the spec under a new "## Feedback"
heading, the way Assignment 1's lessons were carried forward, so the next assignment
inherits it. Then update the memory file if you are on the machine that holds it.

---

## 5. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `ModuleNotFoundError: No module named 'docx'` | Wrong interpreter. Use `./build/venv/bin/python`, not bare `python3`. The package is `python-docx`; `import docx`. |
| `merge.py` says "fallback body-concat" | `docxcompose` missing. Harmless — output is equivalent — but `pip install docxcompose` for a cleaner merge. |
| `verify.py` reports a group with 0 or 2+ ticks | An edit to `fill_mon.py` changed a score without changing its checkbox. Fix the score dict, rebuild. |
| Document opens with odd pagination | Each MON opportunity sits on its own page. Expected: the template's last checkbox paragraph carries a page break which is duplicated with the block. Cosmetic. |
| Edited `portfolio_content.md` but the .docx is unchanged | The scripts hardcode their own copy. See recipe B — edit both. |
| Word count jumped after an edit | Rationales grow easily. Re-run `wordcount.py` before every rebuild in place. |

---

## 6. Invariants — do not break these without a reason

1. **One file is submitted.** The merged document, not the intermediates.
2. **49 tick groups, exactly one tick each.** `verify.py` enforces it.
3. **The five critical-thinking hooks** listed in the spec: Delta.g named as a funded
   competitor; Potential Market Volume scored MEDIUM not HIGH; the back-up hedging market
   but not technical risk; the VPC conceding it is slower and coarser than radar; the BMC
   treating channel, crews and dataset as the co-specialised assets. These are where the
   Critical Thinking and Application marks come from. A tidy-up that deletes them costs
   marks.
4. **References stay alphabetical**: Teece, The Quantum Insider, Tidd.
5. **No fabricated figures.** Every number traces to a source named in the spec.
