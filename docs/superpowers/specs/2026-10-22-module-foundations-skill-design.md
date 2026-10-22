# Module Foundations Skill + Standard Prompts — Design

**Date:** 2026-10-22
**Status:** Approved in chat; implementation via `superpowers:writing-skills` (test-first)

## Problem

Three modules, three different content layouts. The generic engine
(`~/git_clone/learning_path/skill.md`, `building-learning-path`) does not know Sussex syllabus
exports, assessment deadlines, or the clone-integrity rule that bit Module 3. Assignment solving
already has a tested skill (`solving-sussex-assignments`); foundation content does not.

## Deliverables

1. `.claude/skills/building-module-foundations/` — repo-scoped, Sussex-specific layer over the
   external engine (referenced by path, existence-checked, never vendored).
2. `PROMPTS.md` at repo root — two slotted templates in the learner's v2 style:
   build-foundations, solve-assignment. Thin: the skills carry the process.
3. Standard module layout = **Module 3's, as the learner's latest standard**:

```
module_N_<slug>/
├── module_N_intro.md, module_N_resources.md    syllabus exports (untouched)
├── week_K/                                      week_K_content.md, week_K_lecture.md,
│                                                week_K_problems_hint.md, week_K_problems_model_answer.md
├── internal_resources/                          exporter skill notes, prompt log
├── exteral_resources/                           PDFs, readings            (sic — existing name)
├── latex_tutorial/                              instructor templates, if supplied
├── foundations_sprint/                          README, STRATEGY, content/{GLOSSARY, dayNN, companions/, physics/}
│   └── docs/superpowers/{specs,plans}
├── assignment_K/                                brief exports + solutions/   (assignment skill)
└── prompt.md                                    per-module prompt log (superseded by root PROMPTS.md)
```

## Skill phases

0 Ingest the export contract; extract weeks, outcomes, every task/portfolio/quiz problem,
  assessments with deadlines **diffed across sources**.
1 Classify: quantitative (moves, clones, verify scripts) / qualitative (readings digest,
  frameworks, task prep, source vault) / hybrid (ask about simulations).
2 Mine problem-first: assessed skills → moves/frameworks → order by deadline, then dependency.
3 Build via the external engine: Spec → Plan → Content, model gates, scratch branch,
  hints + sketches, done-when, spaced review.
Standing: clone integrity checked mechanically; week companions; glossary; deadline map;
  simple version first; hand-off to `solving-sussex-assignments` when `assignment_*/` appears.

## Test plan (spec-level only)

Fixtures: Module 3 exports with `foundations_sprint/` removed (quantitative); Module 2 exports
(qualitative). Baseline agents design the foundations content without the skill; scored on a
rubric written first. Then the same with the skill. No day files authored in tests.
