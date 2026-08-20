# Portfolio build pipeline

Rebuilds `Assessment2_Quantum_Portfolio.docx` by filling the three blank worksheet
templates issued with the assignment. Verified on 2026-08-21 to reproduce the submitted
document's text exactly (473 paragraphs, identical).

## Requirements

    python3 -m venv venv && ./venv/bin/pip install python-docx docxcompose

`docxcompose` is used for the merge; `merge.py` falls back to manual body concatenation
if it is unavailable.

## Run (from this directory)

    python fill_mon.py      # -> ../MON_filled.docx
    python fill_vpc.py      # -> ../VPC_filled.docx
    python fill_bmc.py      # -> ../BMC_filled.docx
    python merge.py         # -> ../Assessment2_Quantum_Portfolio.docx  (adds title block + references)
    python verify.py        # checks every box filled and exactly one tick per criterion group
    python wordcount.py     # counts only inserted prose, excluding template text and references

Set `OUTDIR` to build somewhere else without touching the submitted file — useful for
checking a change before overwriting:

    OUTDIR=/tmp/rebuild python fill_mon.py && OUTDIR=/tmp/rebuild python merge.py

## IMPORTANT: where the words live

`../portfolio_content.md` is the readable source of truth for the prose, **but the fill
scripts hardcode their own copy of it**. Editing the markdown alone changes nothing in the
.docx. To change wording you must edit both:

- `fill_mon.py` — core ability descriptions, opportunity applications/customer groups,
  Part 2 scores and rationales, Part 3 notes
- `fill_vpc.py` / `fill_bmc.py` — the `Notes:` body of each box
- `references.py` — the reference list (alphabetical: Teece, The Quantum Insider, Tidd)
- `merge.py` — `TITLE` / `SUBTITLE` constants

Then re-run the pipeline and `verify.py`.

## What the scripts do that is not obvious

- The MON template ships with **one** Part 2 block; `fill_mon.py` deep-copies it so all
  three opportunities are scored. The template's last checkbox paragraph carries a page
  break, so each opportunity lands on its own page. Cosmetic, not an error.
- Part 3's Opportunity Assessment block is likewise duplicated for Opportunities 2 and 3.
  Opportunity 1 gets a plain "Agile Strategy: Pursue Now" line, since relatedness is
  measured relative to the primary opportunity and would be meaningless for it.
- The MON template has no `Notes:` field in Part 3; one is added to match the VPC/BMC
  convention.
- Typography: `GBP ` -> `£`, straight apostrophes -> typographic, page-range hyphens ->
  en dashes in references only, `*asterisks*` -> real italic runs.
