# Essays

Prose submissions with a word limit and Harvard citations, usually delivered as .docx.
Example: Module 2 Assignment 1, "Essay (1500 Words)".

## Structure that worked

Keep the content in a markdown source of truth (`essay_draft.md` -> `essay_final.md`) and generate
the .docx from it. Editing prose directly in Word loses the ability to diff, and the diff is what
makes a word-count squeeze tractable.

Keep `references.md` and `verified_sources.md` as separate files: one is the reference list, the
other records what was actually checked and how.

## Verify every factual claim before it ships

Market figures, company claims, funding numbers and dates are the highest-risk content in a
business-facing essay, and a fact-check pass has caught a real citation error before submission.

- Every in-text citation must appear in the reference list, and vice versa. Automate this check.
- Prefer primary sources; record the URL and access date in `verified_sources.md`.
- If a number cannot be verified, either attribute it explicitly to its claimant or cut it.

## Word limits

Confirm what counts before compressing: titles, headings, in-text citations, reference lists and
appendices are often excluded, and the answer changes the strategy completely.

If over, compress by phrasing rather than by cutting substance, and stop when phrasing passes are
exhausted - going further starts removing marks. Going modestly over can be a deliberate trade
when the extra words answer a printed prompt or add a citation, but it should be a decision that is
recorded, not an accident.

## Turnitin

See `integrity.md`. Essays should score lower than worksheet submissions because less of the text
is supplied. Prose matching another student paper or a publication is the only kind that matters.
