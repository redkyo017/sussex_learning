"""Assemble QT01_POF_solutions.tex from the instructor template.

The problem statements are taken byte-for-byte from ../QT01_POF_student_template.tex.
Only the candidate number, the nine placeholder solution blocks and the essay
(appended before \\end{document}) are substituted.

    python build.py && tectonic -X compile --keep-logs QT01_POF_solutions.tex
"""

import re
from pathlib import Path

HERE = Path(__file__).parent
template = (HERE.parent / "QT01_POF_student_template.tex").read_text()

PARTS = ["w2p1", "w2p2", "w3p1", "w3p2", "w4p1", "w4p2", "w5p1", "w5p2", "w7p1"]
PLACEHOLDER = re.compile(r"\\begin\{solutionbox\}.*?\\end\{insightbox\}", re.S)

blocks = PLACEHOLDER.findall(template)
assert len(blocks) == len(PARTS), f"expected {len(PARTS)} placeholder blocks, found {len(blocks)}"

it = iter(PARTS)
out = PLACEHOLDER.sub(lambda m: (HERE / "parts" / f"{next(it)}.tex").read_text().strip(), template)

assert out.count("Candidate number: 123456") == 1
out = out.replace("Candidate number: 123456  % Replace candidate number with yours",
                  "Candidate number: 672128")

out = out.replace(r"\graphicspath{{figures/}}",
                  "\\graphicspath{{figures/}}\n\\usepackage{fancyhdr}\n\\pagestyle{fancy}\\fancyhf{}"
                  "\n\\renewcommand{\\headrulewidth}{0pt}"
                  "\n\\fancyfoot[L]{\\footnotesize Candidate 672128}"
                  "\n\\fancyfoot[R]{\\footnotesize Page \\thepage\\ of \\pageref*{LastPage}}"
                  "\n\\usepackage{lastpage}\n\\usepackage{array}")

essay = (HERE / "parts" / "essay.tex")
assert essay.exists(), "parts/essay.tex missing"
out = out.replace(r"\end{document}", "\\newpage\n" + essay.read_text().strip() + "\n\n\\end{document}")

for leftover in ["Replace this placeholder", "State your final answer(s) clearly here",
                 "Add a short physical interpretation here", "123456"]:
    assert leftover not in out, f"template placeholder left in output: {leftover!r}"

(HERE / "QT01_POF_solutions.tex").write_text(out)
print("wrote QT01_POF_solutions.tex")
