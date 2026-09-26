# Problem sets (PRB)

Maths/physics questions with marks per part, submitted through a Canvas quiz that also offers a
PDF upload slot. Examples: Module 1 Assignment 1 (98/100), Module 3 Assignment 1.

## Choose the route first, and get sign-off

Canvas gives a text box per question plus a final upload slot. Decide on evidence:

**Choose the PDF upload when any of these hold** - they usually do:

- A sketch or figure is required. The Canvas editor cannot draw, and one figure often serves
  several questions. In Module 3 Assignment 1 three questions (27 marks) hung on a single sketch:
  one asked for it, two more said "mark it in your sketch".
- Derivations run to multiple aligned lines. The Canvas equation editor inserts one expression at
  a time; a 15-mark derivation becomes dozens of insertions, each a chance to mistype.
- The quiz warns about tabs and auto-save. Canvas's own instructions say multiple open instances
  can overwrite work, and a stale tab can auto-submit at the deadline and **overwrite previous
  attempts**. Minimise time spent inside the quiz.

**Then add pointer lines.** With a PDF-only submission, boxes 1..n sit empty and a marker may score
an empty box before finding the upload. Write one line per box:

> "Full solution and workings are in the uploaded PDF (Question 14), section 'Question 1'."

Explain what this is when telling the student to do it - the term means nothing on its own.

## Use the instructor's template if one exists

Leave the preamble byte-for-byte alone and fill the solution slots. It compiles as-is, matches what
the marker expects, and its structure (problem / solution / final answer / insight boxes) is already
the presentation the tutor wants. `assets/solution_template.tex` is only for when none is supplied.

Watch for a grouping mismatch: an instructor template may present 13 Canvas questions as 5 problems.
That is not missing work - verify by checking the marks sum - but cross-reference both numbering
schemes in the document.

## Build

`tectonic` is installed (`brew install tectonic`): one self-contained binary, ~20MB, fetches packages
on demand, reruns TeX until references settle, cleans up intermediates.

```bash
tectonic -X compile solutions.tex          # normal build
tectonic -X compile --keep-logs solutions.tex   # keep the log to inspect warnings
```

Overleaf as fallback: upload the `.tex`, put images in a folder named to match `\graphicspath`,
compile with pdfLaTeX **twice** so figure references resolve.

## Figures

Generate with matplotlib from a committed script, never by hand, so the figure can be regenerated
after any change. Plot in dimensionless units where possible (e.g. axes in `beta*x` and
`|psi|^2/beta`) so the figure is valid for all parameter values.

`matplotlib`/`numpy` are absent from system Python - use a venv.

Mark on the figure everything the questions ask to be marked, and reference it from each relevant
part so the marker is pointed at it.
