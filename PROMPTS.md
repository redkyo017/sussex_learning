# Standard prompts

Two templates, one per phase of every module. Fill the `[BRACKETS]`, delete lines you don't need.
They are deliberately thin: the process lives in the skills, which load automatically.

- `.claude/skills/building-module-foundations/` - foundation content from a syllabus export
- `.claude/skills/solving-sussex-assignments/` - assessed work, problem set or portfolio

Both follow the v2 style in `~/git_clone/learning_path/basic_prompt.md`. The engine behind the
first one is `~/git_clone/learning_path/skill.md`; it must be cloned on the machine.

---

## 1. Build the foundations for a module

Use after exporting the syllabus into `module_N_<slug>/` (module intro, each week's content and
lecture or head-up/tasks/consolidate, hints, model answers, resources) and before or during the
first weeks.

```
I want to master the foundation knowledge needed to follow and comprehend [MODULE N: TITLE]
for my Sussex MSc as fast as humanly possible - fast, but real: by the end I must be able to
[follow every lecture step and solve the weekly task and portfolio problems on a blank page
in the six-steps write-up | read every core source and apply its frameworks to a named case
in assessment-ready prose].

Module folder: [/Users/hunghd/git_clone/sussex_learning/module_N_<slug>]. The syllabus is
exported there. I have just finished Week [K]. Assessments: [Assessment 1, type, due week;
Assessment 2, type, due week] - check the exports, the dates have disagreed before.
Time: [H] h/day for about [D] days, or recommend a number.

About me: see ~/git_clone/learning_path/LEARNER_PROFILE.md, plus for this module:
[what I remember / what I never learned]. [Text-only, no simulations | I want runnable checks.]

Skip the traditional learning path wherever it doesn't pay off, but keep the load-bearing
fundamentals and tell me which they are. Give me the strategy expert practitioners use, the
mistakes that waste most beginners' time and how I'd notice them, and an aggressive day-by-day
plan where every day ends with something done and self-checked, with spaced review.

Rules for you:
- Use the building-module-foundations skill. Module 3's layout is my standard.
- Problem-first: inventory every task, portfolio and quiz item before choosing what to teach.
- Every exercise ships a hint and a solution sketch. Clones never reuse course problem numbers.
- Simple version first; we extend later. Link good online resources inside the content.
- Accurate over impressive: evidence or label it as judgment. Push back if the time doesn't fit.

Ask me questions before answering: one round, at most 7, only ones whose answers would change
the plan, each with a default I can accept by replying "defaults". Then proceed.
```

---

## 2. Solve an assessment

Use once the brief is exported into `module_N_<slug>/assignment_K/`. Works for the mid-module
problem set or essay and for the final portfolio alike; the skill adapts by type.

```
In [MODULE N: TITLE] at [/Users/hunghd/git_clone/sussex_learning/module_N_<slug>] I have
[Assessment 1 - problem set | essay, mid-module after Week K | Assessment 2 - portfolio,
final], described in [assignment_K/]. Help me solve it precisely and comprehensively.

Instructor material: [hints and model answers in week_K/ | a LaTeX template in latex_tutorial/
| worksheet templates in assignment_K/ | none]. [Anything else: word limit, format, what I've
already drafted.]

Rules for you:
- Use the solving-sussex-assignments skill.
- Diff every copy of the questions; instructor-authored files beat Canvas markdown exports.
  Compute every reading of any discrepancy - never judge by inspection.
- Candidate number 672128, never my name. Every answer ends with a closing sentence.
- Verify every result by a method that is not the same algebra, and read every rendered page.
- [PDF upload with pointer lines | answer in the Canvas boxes] unless you argue otherwise.
- Tell me plainly what only I can do before submitting.

Ask me only what would change the deliverable: one round, with defaults. Then proceed.
```

---

## Earlier prompts, for the record

Module 3's foundations request (21 Sep 2026) and Assessment 1 request (26 Sep 2026) are kept in
`module_3_foundations_of_quantum_mechanics/internal_resources/prompt.md` and
`module_3_foundations_of_quantum_mechanics/prompt.md`. Both are superseded by the templates above.


In [MODULE 3] at [/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics] I have
[Assessment 2 - portfolio, final], described in [/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics/assignment_2]. Help me solve it precisely and comprehensively.

Instructor material: [hints and model answers from week 1 to week 7 | the assignment
description in: '/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics/assignment_2/description.md' | worksheet templates in '/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics/assignment_2/QT01_POF_student_template.pdf' or you can refer to my exported version in '/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics/assignment_2/Assessment_2_Portfolio.md'| all material for the essay of week 6 is in '/Users/hunghd/git_clone/sussex_learning/module_3_foundations_of_quantum_mechanics/week_6']. [Anything else: word limit, format, what I've
already drafted.]

Rules for you:
- Use the solving-sussex-assignments skill.
- Diff every copy of the questions; instructor-authored files beat Canvas markdown exports.
  Compute every reading of any discrepancy - never judge by inspection.
- Candidate number 672128, never my name. Every answer ends with a closing sentence.
- Verify every result by a method that is not the same algebra, and read every rendered page.
- [PDF upload with pointer lines | answer in the Canvas boxes] unless you argue otherwise.
- Tell me plainly what only I can do before submitting.
Last time, our assigment 1 got 100/100, good job, keep the pace.
Ask me only what would change the deliverable: one round, with defaults. Then proceed.

- "13–14" to "12–14" in W4 P1.
- Check the W5 P2 labelling, then verify or soften items 1–8 above.
- check any "numerically confirmed" claims you didn't run, if there's any, consider remove it
check the Scientific accuracy of the following
- Week 3: Correct the statement that normalisability alone guarantees the wavefunction vanishes at infinity. Specify the operator domain and boundary conditions.
- Essay – Reference [10]: Identify the 99.991% result as optical-qubit readout in calcium-40 ions
- Essay – Reference [11]: Clarify that exceeding a gate-fidelity threshold is not equivalent to demonstrating a fully fault-tolerant quantum computer
- Essay – historical background: Correct the electron-spin historical timeline.