# Standard module layout and the export contract

## The layout (Module 3 is the standard - the learner said so)

```
module_N_<slug>/
├── module_N_intro.md               syllabus export: outcomes, assessment overview, deadlines
├── module_N_resources.md           syllabus export (may be empty or generic)
├── week_K/                         syllabus exports - READ ONLY
├── internal_resources/             exporter skill notes, prompt log
├── exteral_resources/              PDFs and readings  (sic - keep the existing spelling)
├── latex_tutorial/                 instructor templates, when supplied
├── foundations_sprint/             <- everything this skill creates lives here
│   ├── README.md                   quickstart, day map, companion map, combined timetable
│   ├── STRATEGY.md                 strategy, kept fundamentals, mistakes, lecture protocol, six steps
│   ├── content/
│   │   ├── GLOSSARY.md             notation-first, grouped by day, A-Z index
│   │   ├── day01.md ... dayNN.md
│   │   ├── companions/
│   │   │   └── week02_companion.md ... weekKK_companion.md
│   │   └── physics/ | background/  optional second strand (P1.md ...)
│   └── docs/
│       ├── problem_inventory.md    phase 0 output
│       ├── clone_forbidden_entities.txt   qualitative modules: cases the course's tasks use
│       └── superpowers/
│           ├── specs/YYYY-MM-DD-<slug>-design.md
│           └── plans/YYYY-MM-DD-<slug>-plan.md
├── assignment_K/                   assessed work - the OTHER skill's territory
└── prompt.md                       per-module prompt log (root PROMPTS.md supersedes)
```

Zero-padded two-digit numbering: `day01.md`, `week02_companion.md`. Companions start at the
first week that has a lecture worth decoding (Week 1 is usually an overview; skip it).

## The export contract (what the page exporter produces)

Two variants exist. Detect by filename; accept both.

**STEM modules (Module 3 shape)**

| File | Holds |
|---|---|
| `week_K/week_K_content.md` | Intro, outcomes, Explore / Apply / Consolidate sections. **Task problems live under Apply; Portfolio problems under Consolidate.** Quiz questions may appear too. |
| `week_K/week_K_lecture.md` | The lecture, with numbered equations `\tag{K.n}` |
| `week_K/week_K_problems_hint.md` | Instructor hints (tone and depth calibration) |
| `week_K/week_K_problems_model_answer.md` | Instructor model answers - **style source for the six-steps write-up** |

Quirk: Week 1 may be `week1_content.md` with no underscore. Glob for `week*_content.md`.

**Business modules (Module 2 shape)**

| File | Holds |
|---|---|
| `week_K/week_K_head_up.md` | Outcomes for the week |
| `week_K/week_K_tasks.md` | The assessed or practised activity |
| `week_K/week_K_consolidate.md` | Independent study task - often feeds the assessment |
| `week_K/sources/` | Readings; some AI-generated reports, some misfiled - triage, do not trust blindly |

## Phase 0 output: the problem inventory

`foundations_sprint/docs/problem_inventory.md`, one row per item, no sampling:

| Week | Source section | Item | Type (task / portfolio / quiz / essay prompt) | Moves or frameworks needed | Feeds assessment |
|---|---|---|---|---|---|

The rule that follows from it: **a move appears in the curriculum only if a row cites it**, and
**every row must be covered by some day or companion**. Both directions. The inventory is also the
input to `assets/check_clones.py`.

## Deadlines

Read every file that states one: `module_N_intro.md`, any `assignment_*/description.md`, week
content. They have disagreed before (23:00 on a Canvas page, 17:00 UK in the module intro). Record
each, treat the earlier as real, and put the map in `README.md`.
