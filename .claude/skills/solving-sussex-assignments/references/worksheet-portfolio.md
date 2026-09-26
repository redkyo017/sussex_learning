# Worksheet and canvas portfolios

Submissions built from supplied templates - Market Opportunity Navigator, Value Proposition Canvas,
Business Model Canvas - filled in and assembled into one document.
Example: Module 2 Assignment 2 (40% of module, submitted at 1748 words, Turnitin 16%).

## Read the word-count phrasing exactly

The brief said: *"Item 1 - Market Opportunity Navigator (4 worksheets, equivalent to 500 words)"*.

That means **the completed canvases ARE the word count**. No separate essay is required, and adding
one would have roughly doubled the assessed length. Rubrics may still refer to an "essay" - that is
usually boilerplate. Resolve the contradiction from the item-by-item breakdown, not the boilerplate.

## Marks are earned inside the worksheet, not around it

Knowledge, critical thinking and reading marks have to be earned in each worksheet's `Notes:`
field, as prose with Harvard citations. A canvas filled with bare bullet points scores poorly no
matter how good the underlying idea is.

## Build pipeline traps - both of these have bitten

**1. Prose lives in two places.** The text exists in both the markdown source of truth and the
`fill_*.py` scripts that write the .docx, where string literals wrap across lines. A search and
replace that matches the markdown silently misses the script. Keep a `check_docs_match.py` that
compares the two, and run it after every prose edit.

**2. Identity lives in code, not in the document.** The student name sat in `merge.py` as a
constant. A name typed into the .docx is discarded by the next rebuild. Check where identity fields
actually come from before editing the document.

More generally: when a document is generated, never hand-edit the generated artefact. Edit the
source and rebuild, or the next build silently reverts the fix.

## Keep a decisions log

`CHANGES-<date>.md` recording why the submission is as it is - why three opportunities rather than
two, which fields deliberately stay blank, which punctuation must not be "corrected". Without it,
a later editing pass helpfully undoes deliberate choices.
