"""Count the assessed prose in the portfolio.

The submission contains a lot of text the student did not write: the templates'
own prompt questions, field labels and checkbox options. This script counts only
the words that were INSERTED, by diffing each paragraph of the built document
against the blank templates' paragraphs.

Rules:
  - a paragraph identical to a template paragraph counts 0 (including the copies
    produced by duplicating the MON's Part 2 / Part 3 blocks, and checkbox
    options, whose tick is normalised away before comparison)
  - a paragraph of the form "<template label>: <our text>" counts only our text
  - a paragraph with no template counterpart counts in full (rationales, notes,
    title block)
  - the References section and the title block are excluded, per normal academic
    convention (title pages and reference lists do not count toward a word limit)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)

from docx import Document

BLANKS = ["Market Opportunity Navigator_Blank.docx",
          "Value Proposition Canvas_Blank.docx",
          "Business Model Canvas_Blank.docx"]
BUILT = f"{OUT_DIR}/Assessment2_Quantum_Portfolio.docx"
ALLOWANCE = 1500


def paragraphs(path):
    # normalise ticked boxes back to blank so a ticked option still matches its
    # template counterpart and counts as zero words
    return [p.text.strip().replace('\u2612', '\u2610')
            for p in Document(path).paragraphs if p.text.strip()]


def main():
    template = set()
    for b in BLANKS:
        template.update(paragraphs(f"{ASSIGN_DIR}/{b}"))

    section, counts, samples = "Item 1 (MON)", {}, {}
    total = 0
    for i, para in enumerate(paragraphs(BUILT)):
        if i < 2:
            continue                       # title + subtitle: not assessed prose
        if para == "Value Proposition Canvas":
            section = "Item 2 (VPC)"
        elif para == "Business Model Canvas":
            section = "Item 3 (BMC)"
        elif para == "References":
            break

        if para in template:
            continue                       # pure template boilerplate
        ours = para
        for t in template:                 # strip a template label prefix
            if t and para.startswith(t) and len(t) < len(para):
                candidate = para[len(t):].strip()
                if len(candidate) < len(ours):
                    ours = candidate
        n = len(ours.split())
        counts[section] = counts.get(section, 0) + n
        samples.setdefault(section, []).append((n, ours[:60]))
        total += n

    for s in ["Item 1 (MON)", "Item 2 (VPC)", "Item 3 (BMC)"]:
        print(f"{s:16s} {counts.get(s, 0):5d} words")
    print(f"{'TOTAL':16s} {total:5d} words   (allowance {ALLOWANCE}, "
          f"{total / ALLOWANCE - 1:+.0%})")
    if total > ALLOWANCE * 1.1:
        print("\nWARNING: more than 10% over. Trim the MON Part 2 rationales first.")
    return total


if __name__ == '__main__':
    main()
