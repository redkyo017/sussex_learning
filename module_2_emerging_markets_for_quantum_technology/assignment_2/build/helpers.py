import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
import copy
import random
import re
from docx.oxml.ns import qn


def fix_typography(text, apostrophes=True, currency=True):
    """Apply GBP->£ and straight apostrophe -> typographic apostrophe fixes."""
    if currency:
        text = text.replace("GBP ", "£")
    if apostrophes:
        text = text.replace("'", "’")
    return text


def fix_reference_dashes(text):
    """Convert page-range hyphens (e.g. 109-123) to en dashes in reference text.
    Applied only to reference list text. Does not touch hyphenated words."""
    return re.sub(r'(\bpp?\.\s*\d+)-(\d+\b)', r'\1–\2', text)


def set_checkbox(sdt_el, checked: bool):
    """Given a w:sdt element that is a checkbox content control, set its
    checked state and the displayed glyph consistently."""
    sdtPr = sdt_el.find(qn('w:sdtPr'))
    cb = sdtPr.find(qn('w14:checkbox'))
    checked_el = cb.find(qn('w14:checked'))
    checked_state = cb.find(qn('w14:checkedState'))
    unchecked_state = cb.find(qn('w14:uncheckedState'))
    checked_el.set(qn('w14:val'), '1' if checked else '0')
    state = checked_state if checked else unchecked_state
    code = int(state.get(qn('w14:val')), 16)
    glyph = chr(code)
    sdtContent = sdt_el.find(qn('w:sdtContent'))
    r = sdtContent.find(qn('w:r'))
    t = r.find(qn('w:t'))
    t.text = glyph


def find_checkbox_in_paragraph(p_el):
    """Return the w:sdt checkbox element that is a direct child of paragraph p_el,
    or None."""
    for sdt in p_el.findall(qn('w:sdt')):
        sdtPr = sdt.find(qn('w:sdtPr'))
        if sdtPr is not None and sdtPr.find(qn('w14:checkbox')) is not None:
            return sdt
    return None


def paragraph_label_text(p_el):
    """Concatenate direct-child run text of a paragraph element (ignoring sdt content)."""
    texts = []
    for r in p_el.findall(qn('w:r')):
        for t in r.findall(qn('w:t')):
            texts.append(t.text or '')
    return ''.join(texts)


def regen_ids(el):
    """Assign fresh random ids to any w14:paraId attributes and w:sdt id elements
    within el, to avoid duplicate-id artifacts after deepcopy."""
    if el.get(qn('w14:paraId')) is not None:
        el.set(qn('w14:paraId'), '%08X' % random.randint(0, 0xFFFFFFFF))
    if el.get(qn('w14:textId')) is not None:
        el.set(qn('w14:textId'), '%08X' % random.randint(0, 0xFFFFFFFF))
    for sdt in el.iter(qn('w:sdt')):
        sdtPr = sdt.find(qn('w:sdtPr'))
        if sdtPr is not None:
            idel = sdtPr.find(qn('w:id'))
            if idel is not None:
                idel.set(qn('w:val'), str(random.randint(10000000, 999999999)))
    for p in ([el] + list(el.iter(qn('w:p')))):
        if p.get(qn('w14:paraId')) is not None:
            p.set(qn('w14:paraId'), '%08X' % random.randint(0, 0xFFFFFFFF))
        if p.get(qn('w14:textId')) is not None:
            p.set(qn('w14:textId'), '%08X' % random.randint(0, 0xFFFFFFFF))


def clone_block(p_elements):
    """Deep-copy a list of paragraph elements, regenerate ids, return new list
    (not yet inserted into tree)."""
    new_els = []
    for p_el in p_elements:
        new_el = copy.deepcopy(p_el)
        regen_ids(new_el)
        new_els.append(new_el)
    return new_els


def insert_block_after(anchor_el, new_els):
    """Insert new_els (in order) immediately after anchor_el."""
    prev = anchor_el
    for el in new_els:
        prev.addnext(el)
        prev = el
    return new_els[-1]  # new last element, for chaining


def add_run_after_label(p_el, text):
    """Add a new w:r/w:t run to the end of a plain paragraph (no sdt), containing
    ' ' + text, matching sibling run formatting (no explicit rPr => inherits style)."""
    from docx.oxml import OxmlElement
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = ' ' + text
    r.append(t)
    p_el.append(r)
    return r


def new_paragraph(style_name, text=None):
    from docx.oxml import OxmlElement
    p = OxmlElement('w:p')
    if style_name:
        pPr = OxmlElement('w:pPr')
        pStyle = OxmlElement('w:pStyle')
        pStyle.set(qn('w:val'), style_name)
        pPr.append(pStyle)
        p.append(pPr)
    if text is not None:
        r = OxmlElement('w:r')
        t = OxmlElement('w:t')
        t.set(qn('xml:space'), 'preserve')
        t.text = text
        r.append(t)
        p.append(r)
    return p
