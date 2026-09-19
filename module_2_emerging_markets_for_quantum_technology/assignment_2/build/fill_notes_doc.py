"""Generic filler for VPC/BMC-style docs: append verbatim text to each box's
'Notes:' paragraph, matched by nearest preceding heading text."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from helpers import fix_typography


def make_run(text):
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = ' ' + text
    r.append(t)
    return r


def fill_notes(src, out, box_text_map):
    """box_text_map: dict heading_text -> verbatim text (already typography-fixed)."""
    doc = Document(src)
    current_heading = None
    filled = set()
    for p in doc.paragraphs:
        style = p.style.style_id
        if style in ('Heading1', 'Heading2', 'Heading3'):
            current_heading = p.text.strip()
            continue
        txt = p.text.strip()
        if txt == 'Notes:' or txt.startswith('Notes:'):
            if current_heading in box_text_map:
                # find the run whose text is exactly 'Notes:'
                target_run_el = None
                for r in p._p.findall(qn('w:r')):
                    tt = r.find(qn('w:t'))
                    if tt is not None and tt.text == 'Notes:':
                        target_run_el = r
                        break
                if target_run_el is None:
                    raise RuntimeError(f"Could not find 'Notes:' run under heading "
                                        f"{current_heading!r}")
                new_run = make_run(box_text_map[current_heading])
                target_run_el.addnext(new_run)
                filled.add(current_heading)
    missing = set(box_text_map) - filled
    if missing:
        raise RuntimeError(f"Boxes not filled: {missing}")
    doc.save(out)
    print(f"Saved {out}; filled boxes: {sorted(filled)}")
