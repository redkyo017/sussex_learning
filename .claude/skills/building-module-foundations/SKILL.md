---
name: building-module-foundations
description: Use when a Sussex MSc module's syllabus has been exported into the repo (module intro, weekly content/lecture or head-up/tasks/consolidate files) and the learner wants foundation learning content built for it - a sprint, primers, week companions, or a "master this module fast" request.
---

# Building Module Foundations

## Overview

Sussex-specific layer over the generic learning-path engine. Baseline testing showed agents reason
about *what to teach* well on their own and then invent a fresh directory layout every time, ship
exercises without hints or sketches, and skip the lecture-decoder companions. This skill supplies
the **conventions**; the engine supplies the process.

**REQUIRED BACKGROUND:** `/Users/hunghd/git_clone/learning_path/skill.md` (`building-learning-path`)
for Spec -> Plan -> Content, model gates, scratch branch, standing constraints. First action:

```bash
test -f /Users/hunghd/git_clone/learning_path/skill.md || echo "MISSING: clone learning_path first"
```

If missing, stop and tell the learner. Do not substitute from memory.

## When to Use

- A `module_N_*/` folder holds exported syllabus files and no `foundations_sprint/` yet
- The learner asks to master, learn, or prepare for a module, or for primers/companions
- Not for assessed work: once an `assignment_*/` folder exists, that is `solving-sussex-assignments`

## Phases

| # | Phase | Produces |
|---|---|---|
| 0 | **Ingest** the export contract (`references/layout.md`) | `foundations_sprint/docs/problem_inventory.md` - **every** task, portfolio and quiz item, with week and the moves it needs. Exhaustive: a baseline agent read "only excerpts" and would have missed skills. |
| 1 | **Classify** quantitative / qualitative / hybrid (`references/module-types.md`) | One line in the spec stating the type and what form the days take |
| 2 | **Mine** problem-first: inventory -> moves/frameworks -> order by assessment deadline, then dependency | The curriculum table. Diff deadlines across every source and record conflicts. |
| 3 | **Build** via the engine's Spec -> Plan -> Content | The Module 3 layout, exactly (`references/layout.md`); companions from `references/companion-skeleton.md` |
| 4 | **Check** | `assets/check_clones.py` passes (maths instances, or `--entities` for qualitative modules); every exercise has hint + sketch; exports untouched |

## Non-negotiables (each was failed in baseline testing)

1. **Layout is Module 3's.** `foundations_sprint/{README.md, STRATEGY.md, content/{GLOSSARY.md, dayNN.md, companions/weekKK_companion.md}, docs/superpowers/{specs,plans}}`. Not `foundations/`, not `day_N_name/` folders, not `00_README`. The learner named this as their standard.
2. **Every exercise ships hint + solution sketch**, inline, in the engine's day format. "Answers in a separate file" is not that.
3. **One companion per lecture week**, shaped by `references/companion-skeleton.md`: notation decoder, skipped steps expanded, clone problems. A "what to know before week N" pre-read is not a companion.
4. **Clones never share numbers or functions with a course problem.** Run `assets/check_clones.py`. "Adapted" problems are exactly how Module 3's clones collided with real portfolio items.
5. **Syllabus exports are read-only.** The sprint is additive beside them.

## Red Flags

- Proposing a directory tree that is not the one in `references/layout.md`
- An exercise with an answer but no hint, or a hint but no sketch
- A clone whose numbers you chose by nudging a course problem
- Designing from the lecture headings without opening the task and portfolio problems
- A single deadline quoted when two files state different ones
