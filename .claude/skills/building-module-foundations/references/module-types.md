# Module types

Baseline agents classified correctly on their own (a physics module as "moves", an innovation
module as "frameworks, no equations"). State the classification in one line of the spec and
adapt the *form*; the layout stays the same.

| | Quantitative (maths, physics, CS) | Qualitative (business, policy, innovation) | Hybrid (quantum computing) |
|---|---|---|---|
| Unit of teaching | Named **move**, 10 min, drilled cold | Named **framework**: inputs, outputs, failure mode, example | Both; ask whether runnable sims are wanted |
| Day cadence (Module 3 default) | 20 retrieval · 60 moves · 90 drills · 40 companion apply · 10 log (3.5 h) | 20 retrieval · 50 frameworks · 60 apply to running case · 40 reading triage · 10 log (3 h) | As quantitative |
| Exercise | Problem -> hint -> sketch -> closing sentence | Application prompt -> hint -> model paragraph -> what a weak answer misses | Both |
| Companion §3 | Notation decoder | Framework decoder | Notation decoder |
| Second strand | `content/physics/` background | `content/background/` (e.g. economics primers) | optional `code/` only if asked |
| Verify | Numeric check script beside the content; `check_clones.py` on course problems | Claims cite file:line in the exports; outside material labelled; `check_clones.py --entities` against `docs/clone_forbidden_entities.txt` | Both |
| Reading triage | Lecture is primary | `sources/` is mixed: official pages first, AI-generated reports secondary, misfiled papers ignored - say which | — |

Standing preferences from the learner profile: text-only unless asked, simple version first then
extend, link good online resources inside the content, British English.
