# Module 4 Foundations Sprint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Module 4 foundations sprint: 10 day files, 6 week companions, STRATEGY, README and GLOSSARY. Every exercise ships a hint and a sketch, every number is machine-checked, and nothing collides with a course case.

**Architecture:**
- Markdown content in Module 3's layout.
- Each day and each companion is written by one subagent from the spec, the inventory and the lecture.
- Each content file has a sibling Python check file listing its numeric answers. Two stdlib scripts gate every task: `verify_numbers.py` recomputes the numbers and `check_structure.py` enforces the skeletons.

**Tech Stack:** Markdown with `$...$` maths; Python 3 stdlib only (checks); `.claude/skills/building-module-foundations/assets/check_clones.py`.

**Spec:** `../specs/2026-11-10-module4-foundations-design.md` (read it in full before any task).

## Global Constraints

Paths are relative to `module_4_applications_of_quantum_technology/` (abbreviated `M4/`).

| Area | Rule |
|---|---|
| Writes | Only inside `M4/foundations_sprint/`. Never edit `week_*/`, `module_4_*.md` or figures. |
| Git | No git commands in any subagent. The controller commits on `authoring/module4`, staging only `M4/foundations_sprint/`. |
| Language | British English. Plain, direct prose. Maths in `$...$` / `$$...$$` as in Module 3. |
| Exercise format | `### Exercise N.k (quantitative)` or `### Exercise N.k (writing)`. Quantitative: `**Hint:**` then `**Solution sketch:**` (six-steps form: Restate, Write state, Name move, Algebra, Check, Answer). Writing: `**Hint:**`, `**Model paragraph:**`, `**What a weak answer misses:**`. Everything inline, never in a separate file. |
| Writing exercises | Use only the fictional running case **"Harrowmere Water & Power"**. Its invented figures are labelled "(fictional)". Never use the learner's own field, a lecture named case (`docs/clone_forbidden_entities.txt`) or a real company as the case. |
| Numbers | Every numeric answer in a sketch has an entry in that file's check module (Task 1 interface). |
| Accuracy | A physics claim beyond the lecture cites a source from the spec's Target Sources table, or is labelled "(judgement)". Lecture errors are corrected as listed in `docs/problem_inventory.md` ("Lecture errors"), naming the lecture line. |
| Links | Only links from the spec's Target Sources, plus lecture reference URLs. |
| Moves and frameworks | Use the IDs M1-M14 and F1-F3 exactly as the spec defines them. |
| Assessment | No content aimed at Assessment 1. No Portfolio drafting. |

## Review Focus

1. **Wrong physics stated confidently,** especially Φ = k_eff g T² conventions, T/√Hz arithmetic, QBER and Shor arithmetic. The reviewer recomputes every sketch, and `verify_numbers.py` must pass.
2. **A lecture error copied instead of corrected.** The reviewer checks each erratum row for that week against the companion's §4.
3. **A model paragraph that reads like a usable portfolio answer for a generic case.** It must be anchored on Harrowmere's fictional figures and must not use a lecture case. The entity check must pass.
4. **Exercises missing a hint or sketch, or a day missing Done when or Spaced review.** `check_structure.py` must pass.
5. **A day that runs well past 3 h.** Each day states its timings in the cadence (15/55/50/45/15). Heavy days mark stretch exercises `(stretch)`.

---

### Task 1: Check scripts (controller writes these)

**Files:**
- Create: `M4/foundations_sprint/docs/verify_numbers.py`
- Create: `M4/foundations_sprint/docs/check_structure.py`
- Create: `M4/foundations_sprint/docs/checks/__init__.py` (empty)

**Interfaces:**
- **Produces:** each content task creates `docs/checks/check_<stem>.py`, where `<stem>` is `day01` … `day10` or `week02` … `week07`. The module defines `CHECKS: list[tuple[str, float, float, float]]`. Each tuple is `(label, computed, stated, rel_tol)`:
  - `computed` is calculated in Python from the inputs.
  - `stated` is the number as written in the markdown.
  - `rel_tol` is typically 0.05 for 2-significant-figure answers.
- `verify_numbers.py [stem ...]` imports every `docs/checks/check_*.py` (or only the named stems) and prints `MISMATCH label computed stated` for each failure. It ends with `N checks, M mismatches` and exits 1 if M > 0 or if a content file exists without its check module.
- `check_structure.py [file ...]` checks the content files:
  - Day files must have the sections `## Why this matters`, `## Core concepts`, `## Exercises`, `## Anti-patterns / Common mistakes`, `## Done when` and `## Read next`. Days 02-10 also need `## Spaced review`.
  - Companions must have the sections `## 1.` to `## 7.`.
  - Every `### Exercise` block must contain `**Hint:**` and either `**Solution sketch:**` or both `**Model paragraph:**` and `**What a weak answer misses:**`.
  - It prints `FAIL file: reason` lines and exits 1 on any failure.

- [ ] Step 1: Write both scripts, then add a planted bad file in scratch to confirm each fails. Expected outputs: `MISMATCH` and `FAIL ... missing **Hint:**`.
- [ ] Step 2: Run both on the empty content tree. Expected: `0 checks, 0 mismatches` and no FAIL lines.
- [ ] Step 3: Commit `WIP: task 1 check scripts`.

### Task 2: STRATEGY.md and README skeleton

**Files:** Create `M4/foundations_sprint/STRATEGY.md` and `M4/foundations_sprint/README.md`.

**STRATEGY.md** follows Module 3's STRATEGY section order, adapted:
1. The strategy: argument-first plus moves; the four principles.
2. Kept fundamentals and skipped topics: the spec lists, verbatim in substance.
3. The 7 mistakes that waste most beginners' time in this module, each as mistake → how you notice → fix. They must include:
   - quoting a gain without units, conditions or a source
   - comparing a lab record with a fielded classical product
   - believing the "parallel computation" myth
   - treating QKD as unbreakable
   - TRL inflation
   - copying lecture numbers without checking them
   - reading for coverage instead of writing
4. The Five-Pass Lecture Protocol, with a worked example on the Week 2 lecture.
5. The six-steps write-up (quantitative), with a trivial example that is not a course case.
6. F1 gain argument template, with an annotated 300-word example on Harrowmere.
7. Confusion-log template.
8. "Where's the evidence" for the method, cited as in the spec.

**README.md** at this stage holds:
- quickstart
- the deadline table from the spec, with its time-zone note
- the day map and timetable from the spec curriculum (dates, A1 window, the 25-29 Nov slot for the learner's Weeks 1-3 pieces)
- the companion map
- the figures note

The inventory row map is added in Task 19.

- [ ] Step 1: Write both files. Expected: the README timetable dates match the spec exactly.
- [ ] Step 2: Check: `grep -c "Harrowmere" STRATEGY.md` ≥ 1; `grep -n "Thu 19 Nov" README.md` matches.
- [ ] Step 3: Commit `WIP: task 2 strategy and readme`.

### Tasks 3-7 (Batch 1, days) and 8-9 (Batch 1, companions)

Each task creates exactly two files: the content file, and its check module `docs/checks/check_<stem>.py`.

**Inputs every writer reads:**
- the spec (whole)
- `docs/problem_inventory.md`
- `docs/clone_forbidden_entities.txt`
- `.claude/skills/building-module-foundations/references/companion-skeleton.md` (companions only)
- the listed lecture file(s), in full
- the listed figures (companions only; read the PNGs)
- for style, Module 3's `foundations_sprint/content/day02.md` and `content/companions/week03_companion.md`

**Day contract:**
- Follow the spec's Content Day Skeleton and cadence.
- 6-10 exercises, with at least 2 writing and at least 3 quantitative.
- Each Move is taught as idea → one worked clone → "you've got it when…".
- `## Done when` gives a no-notes pass mark.
- `## Read next` gives 1-2 Target Sources links with the sections to read.

**Companion contract:**
- §1-§7 as in the skeleton.
- §3 is a notation **and unit** decoder citing lecture line numbers.
- §4 covers every skipped step the mining found plus every erratum row for that week, each with the lecture line.
- §5 has 2-4 clones using numbers and cases not in the lecture.
- §6 is the cold attempt.
- §7 gives confusion-log prompts.
- A final `## 8. Figures` section has one "reading the figure" note per figure file, saying what to look at and what it shows.
- Week 4 and Week 6 add `## 9. Course interactive walkthrough`.
- Companions include the week's quiz items by reference to the inventory key ("see inventory"), not by copying the key.

| Task | File | Moves / scope | Lecture & figures | Rows |
|---|---|---|---|---|
| 3 | `content/day01.md` | F1, F3, M1; the four QT types and their figures of merit; Week 1 lecture decoded inside the day, with errata L52/L70 | `week_1/week_1_lecture.md` | W1 all |
| 4 | `content/day02.md` | M2, M3 | `week_2` §2.1-2.2 | W2 Consolidate |
| 5 | `content/day03.md` | M4, M5; clock and magnetometer comparison table (sensitivity, bandwidth, standoff, SWaP-C) | `week_2` §2.3-2.15 | W2 Apply/Consolidate |
| 6 | `content/day04.md` | M6, M7; derive Φ = k_eff g T² (π/2-π-π/2, T = pulse spacing); ground vs space T² gain; Sagnac ratio (h/m ≈ 5×10⁻⁹ m²/s for ⁸⁷Rb) and why the real gain is smaller; classical gravimeter table | `week_3` | W3 rows |
| 7 | `content/day05.md` | Checkpoint: 12 no-notes items over M1-M7 (fresh numbers) + one timed F1 piece on Harrowmere (gravity survey for voids); marking guide | Days 01-04 files | W1-W3 |
| 8 | `content/companions/week02_companion.md` | Decode Week 2 | `week_2/week_2_lecture.md`, `week_2/figures/fig2_1..3.png` | W2 |
| 9 | `content/companions/week03_companion.md` | Decode Week 3; §4 must build Eq 3.1 from Φ = k_eff g T² and reconcile τ = 2T | `week_3/week_3_lecture.md`, `week_3/figures/fig3_1..7.png` | W3 |

**Steps for each of Tasks 3-9:**
- [ ] Step 1: Write the content file and its check module.
- [ ] Step 2: Run `python3 docs/verify_numbers.py <stem>` and `python3 docs/check_structure.py content/<file>`. Expected: `0 mismatches`, no FAIL.
- [ ] Step 3: Run the entity check:
  - days: `python3 ../../.claude/skills/building-module-foundations/assets/check_clones.py --entities docs/clone_forbidden_entities.txt content/<file>`
  - companions: extract §5-§6 to the scratch dir and run the same check on that extract
  - Expected: `0 flag(s)`.
- [ ] Step 4: The controller commits after the batch's writers finish (not during).

Day 05 (Task 7) runs after Tasks 3-6 are committed. Tasks 3-6 and 8-9 run in parallel.

### Batch 1 gate

- [ ] Run `verify_numbers.py` (all), `check_structure.py` (all), the entity checks, and `check_clones.py M4/week_*/ M4/foundations_sprint/content/`. Expected: all zero.
- [ ] One physics-accuracy reviewer (fresh subagent) per batch. It recomputes every sketch, checks errata handling, checks the Review Focus items, and reports issues with file:line. Fix the issues, re-run the gate, then commit `WIP: batch 1`.

### Tasks 10-14 (Batch 2, days) and 15-18 (Batch 2, companions)

Same contracts and steps as Batch 1.

| Task | File | Moves / scope | Lecture & figures | Rows |
|---|---|---|---|---|
| 10 | `content/day06.md` | M8, M9, M10. BB84 by hand on a fresh 10-bit run (not Table 4.1's bits). No-cloning in four lines. CHSH at 0°/22.5°/45°/67.5°. Fibre at 0.2 dB/km (typical telecom fibre, labelled). Mosca x+y>z. QuVis walkthrough pointer to the Week 4 companion | `week_4` | W4 all |
| 11 | `content/day07.md` | M11; corrected Table 5.2; analogue vs digital; J vs U; ion spin models | `week_5` | W5 all, W6 Explore |
| 12 | `content/day08.md` | M12; Bell circuit; Deutsch-Jozsa n=2 as amplitude sum with a stated balanced f; Quirk walkthrough (Week 1 interactive stand-in) | `week_6` §6.1-6.2 | W1 interactive, W6 Apply |
| 13 | `content/day09.md` | M13. Shor classical arithmetic on **N = 21** (a = 2, r = 6), not 15. Grover iterations for N = 10⁶. Depth from F = 0.995 per gate. Threshold theorem stated correctly. Annealing vs gate model | `week_6` §6.3-6.8 | W6 Consolidate |
| 14 | `content/day10.md` | F2, M14. TRL with evidence. Five barriers. Market figures only from the McKinsey 2026 monitor with date. Harrowmere fact sheet + benefit/risk paragraph. "Map your own background" exercise (prompts and a decision table only, no prose for the learner's case). Cumulative 10-item capstone | `week_7` | W7 all |
| 15 | `content/companions/week04_companion.md` | Decode Week 4, incl. Tables 4.1/4.2 from the figure PNGs; §9 QuVis BB84 walkthrough | `week_4/...`, `week_4/figures/*` | W4 |
| 16 | `content/companions/week05_companion.md` | Decode Week 5 | `week_5/...`, `week_5/figures/fig5_1..9.png` | W5 |
| 17 | `content/companions/week06_companion.md` | Decode Week 6; §9 The Qubit Factory walkthrough (medium-high confidence identification, say so) | `week_6/week_6_lecture.md` | W6 |
| 18 | `content/companions/week07_companion.md` | Framework decoder for Week 7 (TRL table, the five barriers, the advantage test); no figures | `week_7/week_7_lecture.md` | W7 |

Day 10 (Task 14) runs after Tasks 10-13. All the others run in parallel.

### Batch 2 gate

Same as the Batch 1 gate. Commit `WIP: batch 2`.

### Task 19: GLOSSARY and README completion

**Files:**
- Create: `content/GLOSSARY.md`
- Modify: `README.md` (add the inventory row → file map and the Read-next index)

The glossary is notation- and unit-first, grouped by day, with an A-Z index. Each entry is one line: symbol or term | meaning | unit | Day/§.

- [ ] Step 1: Write both.
- [ ] Step 2: Check that every inventory row appears in the README map: a script compares the row count in `problem_inventory.md` with the row count in the map. Expected: equal.
- [ ] Step 3: Full gate (as for the batches) plus `git status --short` showing changes only under `foundations_sprint/` and the learner's own `week_*/figures/`. Commit `WIP: task 19`.

### Task 20: Handoff teardown (controller)

- [ ] Run, in order: `git reset --soft master` → `git switch master` → `git reset` → `git branch -D authoring/module4` → `git status`.
- [ ] Expected: `foundations_sprint/` is untracked on `master`, the figures are still untracked, and nothing was pushed.
