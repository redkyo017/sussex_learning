"""Essay checks: citation order (APS numbering by first use), every cite has an entry and
vice versa, and the body word count (prose between the ESSAY-BODY markers, excluding the
table float, LaTeX commands and citation keys; headings counted separately)."""
import re
from pathlib import Path

src = Path(__file__).with_name("parts").joinpath("essay.tex").read_text()
body = src.split("% ESSAY-BODY-BEGIN")[1].split("% ESSAY-BODY-END")[0]
bib = re.findall(r"\\bibitem\{([^}]+)\}", src)

cites = []
for group in re.findall(r"\\cite\{([^}]+)\}", body):
    for key in group.split(","):
        if key.strip() not in cites:
            cites.append(key.strip())
print("cited in order of first use matches bibliography order:", cites == bib)
print("cited but missing from bibliography:", sorted(set(cites) - set(bib)) or "none")
print("in bibliography but never cited:", sorted(set(bib) - set(cites)) or "none")

def words(tex):
    tex = re.sub(r"~?\\cite\{[^}]*\}", "", tex)
    tex = re.sub(r"\\label\{[^}]*\}|\\ref\{[^}]*\}", "X", tex)
    tex = re.sub(r"\$[^$]*\$", " X ", tex)                 # inline maths = one token
    tex = re.sub(r"\\(textbf|emph|subsection)\{([^}]*)\}", r" \2 ", tex)
    tex = re.sub(r"\\[a-zA-Z]+\*?", " ", tex)
    tex = re.sub(r"[{}]", " ", tex)
    return len([w for w in re.split(r"\s+", tex) if re.search(r"[A-Za-z0-9]", w)])

table = re.search(r"\\begin\{table\}.*?\\end\{table\}", body, re.S).group(0)
prose = body.replace(table, "")
heads = re.findall(r"\\subsection\{([^}]*)\}", prose)
prose_no_heads = re.sub(r"\\subsection\{[^}]*\}", "", prose)
print(f"body prose words (excl. headings, table, references): {words(prose_no_heads)}")
print(f"  + subsection headings: {sum(len(h.split()) for h in heads)}")
print(f"  + table incl. caption: {words(table)}")
