---
name: solving-sussex-assignments
description: Use when working on assessed Sussex MSc Quantum Technology coursework - reading an assignment brief, producing worked solutions, checking answers, or preparing a submission for a problem set, portfolio, essay or worksheet assignment.
---

# Solving Sussex Assignments

## Overview

Across five completed assignments, marks were never lost on the physics. They were lost on
presentation, and near-misses came from administrative traps in the assignment materials.
This skill exists to close those two gaps.

**Core principle: the working mode is fixed and stated up front.** You produce full derivations;
the student verifies and re-voices them before submitting. Not a refusal, not a silent hand-off
of answers. See `references/integrity.md` — read it first, it is short.

## When to Use

- Any file under a `assignment_*/` or `assessment_*/` directory is in play
- The user mentions a problem set, portfolio, essay, PRB, POF, or a Canvas submission
- A brief, rubric or question sheet needs turning into a deliverable

Not for: weekly study notes, lecture companions, or practice problems that are not assessed.

## Phases

| # | Phase | Detail |
|---|---|---|
| 0 | Triage the brief | Collect every source file. Extract weight, word count *and what counts*, deadline, submission mechanics, anonymity. |
| 1 | Diff the sources | `references/checks.md` - mechanical, takes seconds |
| 2 | Choose the deliverable, get sign-off | Route decision + explicit approval before writing |
| 3 | Solve | `references/marking-rules.md` - **the closing sentence is mandatory** |
| 4 | Verify independently | `references/checks.md` - never re-run the same algebra |
| 5 | Package | Instructor template if supplied; `assets/solution_template.tex` otherwise |
| 6 | Hand off | `NOTES.md` + an explicit list of what only the student can do |

Load the reference for the assignment type at phase 0:

| Type | Reference |
|---|---|
| Problem set (PRB) | `references/problem-set.md` |
| Problem portfolio (POF) | `references/problem-portfolio.md` |
| Essay | `references/essay.md` |
| Worksheet/canvas portfolio | `references/worksheet-portfolio.md` |

## The Two Tested Failures

Both were observed in subagent baseline runs on a fixture built from real traps.

**1. Inconsistent working mode.** Given the same assignment, one agent refused outright; another
delivered a compiled PDF. Read `references/integrity.md` before deciding what to produce, so the
answer does not depend on which session the student happens to get.

**2. A boxed answer with no sentence.** The agent that did produce solutions ended every question
with `\boxed{...}` and nothing else. This is the exact thing the Module 1 tutor asked for on four
separate questions, and the only question that lost marks was flagged "could do with some more
exposition". Every solution ends with a sentence. No exceptions.

## Red Flags

- About to write a final answer as a bare formula or a lone `\boxed{}` → add the sentence
- Trusting a Canvas markdown export without diffing it against an instructor file
- Claiming a result is verified when the check re-used the same algebra
- Reporting "done" while a placeholder candidate number remains
- Presenting a deadline without checking whether another file states a different one
