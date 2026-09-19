"""Guard against portfolio_content.md drifting out of sync with the built document.

The fill scripts hardcode their own copy of the prose, so an edit applied to the
markdown but not to the matching fill_*.py (or the reverse) silently ships a
document that does not say what the documentation says it says. This has happened
twice: the string literals in the fill scripts are wrapped across lines, so a
search-and-replace that matches the markdown can miss the script.

Checks every prose block between "# ITEM 1" and "# REFERENCES". Checkbox score
lines are skipped (they are ticks in the document, not text); references are
covered by verify.py. Run after every prose edit, alongside verify.py.
"""
import os, re, sys, unicodedata
import docx

HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
MD = f"{ASSIGN_DIR}/portfolio_content.md"
DOCX = f"{OUT_DIR}/Assessment2_Quantum_Portfolio.docx"

# the markdown holds pre-typography forms that fix_typography() converts at build time
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('GBP ', '£').replace("'", '’')
    s = re.sub(r'\*(.+?)\*', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()

VALUES = (r'(VERY\s+)?(LOW|MEDIUM|HIGH|YES|NO|GOLD MINE|MOON SHOT|QUICK WIN|'
          r'QUESTIONNABLE|PURSUE NOW|KEEP OPEN|PLACE IN STORAGE)')
SCORE_LINE = re.compile(rf':\s*{VALUES}\b')          # "Overall Impact: HIGH."

lines = open(MD, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('# ITEM 1'))
end = next(i for i, l in enumerate(lines) if l.startswith('# REFERENCES'))

blocks, cur = [], []
for line in lines[start:end]:
    skip = (not line.strip() or line.startswith(('#', '---', '**', '|', '>'))
            or SCORE_LINE.search(line))
    if skip:
        if cur: blocks.append(' '.join(cur)); cur = []
    else:
        cur.append(line)
if cur: blocks.append(' '.join(cur))
blocks = [b for b in blocks if len(b.split()) >= 5]

body = ' '.join(norm(p.text) for p in docx.Document(DOCX).paragraphs)
def present(b):
    if norm(b) in body:
        return True
    # some markdown lines carry an editorial annotation before the real text, e.g.
    # 'Lead sentence (added under ...): The scorecard below is completed once ...'
    if '): ' in b:
        return norm(b.split('): ', 1)[1]) in body
    return False

missing = [b for b in blocks if not present(b)]

print(f"prose blocks in portfolio_content.md: {len(blocks)}")
print(f"found in {os.path.basename(DOCX)}:       {len(blocks) - len(missing)}")
if missing:
    print(f"\nDRIFT -- {len(missing)} block(s) in the markdown are not in the built document:")
    for m in missing:
        print(f"  ! {norm(m)[:160]}")
    print("\nThe markdown and the fill_*.py scripts have diverged. Fix the script"
          "\n(its string literals wrap across lines, so match on a short fragment),"
          "\nrebuild, and re-run.")
    sys.exit(1)
print("\nOK: markdown and built document agree.")
