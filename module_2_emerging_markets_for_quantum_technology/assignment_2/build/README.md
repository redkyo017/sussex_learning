# Portfolio build pipeline

Rebuilds `Assessment2_Quantum_Portfolio.docx` by filling the three blank worksheet
templates issued with the assignment. Last rebuilt in place on 2026-08-23; `portfolio_content.md` cross-checked line for line
against the built document.

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
    python check_docs_match.py  # portfolio_content.md must match the built document
    python wordcount.py     # counts only inserted prose, excluding template text and references

Set `OUTDIR` to build somewhere else without touching the submitted file — useful for
checking a change before overwriting:

    OUTDIR=/tmp/rebuild python fill_mon.py && OUTDIR=/tmp/rebuild python merge.py

## IMPORTANT: where the words live

`../portfolio_content.md` is the readable source of truth for the prose, **but the fill
scripts hardcode their own copy of it**. Editing the markdown alone changes nothing in the
.docx. To change wording you must edit both:

- `fill_mon.py` — core ability descriptions, opportunity applications/customer groups,
  Part 2 scores and per-score `notes`, Part 3 notes
- `fill_vpc.py` / `fill_bmc.py` — the `Notes:` body of each box
- `references.py` — the reference list (alphabetical: Teece, Tidd, University of Birmingham)
- `merge.py` — `NAME` (student name in the running head), `TITLE` / `SUBTITLE` constants

Then re-run the pipeline and `verify.py`.

## What the scripts do that is not obvious

- The MON template ships with **one** Part 2 block; `fill_mon.py` deep-copies it so all
  three opportunities are scored. The template's last checkbox paragraph carries a page
  break, so each opportunity lands on its own page. Cosmetic, not an error.
- Part 3's Opportunity Assessment block is likewise duplicated for Opportunities 2 and 3.
  Opportunity 1 gets a plain "Agile Strategy: Pursue Now" line, since relatedness is
  measured relative to the primary opportunity and would be meaningless for it.
- The MON template has no `Notes:` field in Part 2 or Part 3. `fill_mon.py` adds one under
  each Overall Impact / Potential / Challenge score (and under Opportunity 1's category) via
  the per-opportunity `notes={group_label: text}` map, anchored after the group's last
  checkbox; Part 3 gets one to match the VPC/BMC convention.
- Typography: `GBP ` -> `£`, straight apostrophes -> typographic, page-range hyphens ->
  en dashes in references only, `*asterisks*` -> real italic runs.

`verify.py` also checks a list of opening phrases from each box (`required_snippets`); if you
reword the start of a box, update that list too.

## The name in the header

`merge.py` puts `NAME` at the left of the template's running head, with the module title
right-aligned on the same line via a right tab stop. Change the name in `merge.py`, never by
hand in Word: a manual edit to the .docx is silently discarded by the next rebuild.

## Punctuation

12 semicolons remain, all separating list items that themselves contain commas (e.g.
"Opportunity 2, mineral and geothermal exploration; Opportunity 3, GPS-denied navigation").
**Do not bulk-replace them with commas** - that produces comma splices and, in Part 3, makes
two opportunities read as four. Clause-joining semicolons were converted to full stops on
2026-08-23; if the density still reads high, convert more to full stops, not commas.
