import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
import re
from docx import Document
from docx.oxml.ns import qn
from helpers import find_checkbox_in_paragraph, paragraph_label_text
from references import REFERENCES

PATH = f"{OUT_DIR}/Assessment2_Quantum_Portfolio.docx"

doc = Document(PATH)
paras = doc.paragraphs
full_text = '\n'.join(p.text for p in paras)

results = []

def check(name, ok, detail=''):
    results.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" -- {detail}" if detail and not ok else ''))


# ---------- Check 1: required verbatim strings present ----------
required_snippets = [
    'Measures the gravitational difference between two',
    'Vibration is common to both clouds and',
    "Bayesian inversion turns sparse gradient readings",
    "Packaging lasers, vacuum and shielding",
    "Targeted pre-excavation survey of high-risk urban sites",
    'UK water, gas, power and telecoms asset owners,',
    "Density targeting for mineral exploration",
    "Exploration companies, geothermal developers",
    "Drift-free inertial navigation",
    "The Ministry of Defence and defence primes first",
    'One hole in every 65 hits something:',
    'The physics already works outdoors,',
    'Better targeting means fewer speculative boreholes,',
    "Remote sites, power and calibration in harsh conditions",
    'Satellite navigation is jammed and spoofed routinely,',
    'A survey instrument may stand still;',
    "The kernel is Rumelt’s (2011):",
    "The survey or HSE manager at a UK utility asset owner",
    "Interaction: commissioned per site",
    "Barriers: records are often wrong",
    "Measured by strike rate per thousand excavations",
    "We tell contractors what lies under the ground",
    "A survey service, not an instrument sale:",
    "Frustrations: the sensor reads density contrast",
    "Savings: priced by the day against the true cost of one strike",
    "Suppliers: a university physics group for the licence",
    "Value proposition: paid field trials with lead users",
    "Need: depth-resolved subsurface maps with stated uncertainty",
    "Repeat rather than one-off, because difficult sites recur",
    "Value is created for UK utility asset owners and tier-1 contractors",
    "Value proposition: the licensed IP matters less",
    "Reach: direct technical selling into a handful of asset owners",
    "Most expensive resources: physicists and field engineers",
    "Willing to pay: a day rate set against the cost of one strike",
]
missing = [s for s in required_snippets if s not in full_text]
check("All core-ability/Application/CustomerGroup/rationale/Notes body text present",
      len(missing) == 0, f"missing: {missing}")

missing_refs = []
for ref in REFERENCES:
    # references were inserted with '*' markers converted into italic runs, so
    # strip the literal asterisks before searching the flattened plain text
    plain_ref = ref.replace('*', '')
    probe = plain_ref[:60]
    if probe not in full_text:
        missing_refs.append(ref)
check("All reference strings present", len(missing_refs) == 0,
      f"missing: {missing_refs}")

# ---------- Check 2: no bare unfilled labels ----------
bare_labels = {'Notes:', 'Description:', 'Application:', 'Customer Group:'}
bad_paras = [p.text for p in paras if p.text.strip() in bare_labels]
check("No paragraph left as a bare label (Notes:/Description:/Application:/Customer Group:)",
      len(bad_paras) == 0, f"bad paragraphs: {bad_paras}")

# ---------- Check 3: exactly three non-empty 'Opportunity Name:' paragraphs ----------
opp_name_paras = [p.text for p in paras if p.text.strip().startswith('Opportunity Name:')]
non_empty = [t for t in opp_name_paras
             if t.strip() != 'Opportunity Name:' and len(t.strip()) > len('Opportunity Name:')]
check("Exactly three non-empty 'Opportunity Name:' paragraphs",
      len(opp_name_paras) == 3 and len(non_empty) == 3,
      f"found {len(opp_name_paras)}: {opp_name_paras}")

# ---------- Check 4: tick counts ----------
def get_style_id(p_el):
    pPr = p_el.find(qn('w:pPr'))
    if pPr is None:
        return None
    pStyle = pPr.find(qn('w:pStyle'))
    if pStyle is None:
        return None
    return pStyle.get(qn('w:val'))


def paragraph_glyph(cb):
    sdtContent = cb.find(qn('w:sdtContent'))
    t = sdtContent.find(qn('w:r')).find(qn('w:t'))
    return t.text


def is_checked(cb):
    checked_el = cb.find(qn('w:sdtPr')).find(qn('w14:checkbox')).find(qn('w14:checked'))
    return checked_el.get(qn('w14:val')) == '1'


all_p = list(doc.element.body.iter(qn('w:p')))
groups = []  # (heading_label, [ (opt_text, checked_bool) ])
current_group = None
for p_el in all_p:
    style = get_style_id(p_el)
    if style in ('Heading1', 'Heading2', 'Heading3'):
        if current_group and current_group[1]:
            groups.append(current_group)
        current_group = (paragraph_label_text(p_el).strip().rstrip(':').strip(), [])
    cb = find_checkbox_in_paragraph(p_el)
    if cb is not None and current_group is not None:
        current_group[1].append((paragraph_label_text(p_el).strip(), is_checked(cb)))
if current_group and current_group[1]:
    groups.append(current_group)

total_ticks = sum(1 for _, opts in groups for _, checked in opts if checked)
print(f"\nTotal checkbox groups found: {len(groups)}")
print(f"Total ticked (☒) checkboxes across document: {total_ticks}")

bad_groups = []
for idx, (label, opts) in enumerate(groups):
    n_checked = sum(1 for _, c in opts if c)
    marker = 'X' if n_checked == 1 else ('!!' if n_checked != 1 else '')
    print(f"  [{idx:2d}] {label!r:30s} options={len(opts)} checked={n_checked} {marker}")
    if n_checked != 1:
        bad_groups.append((idx, label, n_checked))

check("Total ticks == 49 (12 criteria x 3 opps x 4 groups(incl overall)=... see detail)",
      total_ticks == 49, f"actual total={total_ticks}")
check("Every criterion/category/assessment group has exactly one tick (no 0 or 2+)",
      len(bad_groups) == 0, f"bad groups: {bad_groups}")

# Part 2 specific: 3 opportunities x 13 groups (12 criteria + 1 category) = 39
part2_labels = {'Problem Severity', 'Pertinent Solution', 'Impact Reach', 'Overall Impact',
                 'Compelling Reasons to Buy', 'Potential Market Volume', 'Economic Viability',
                 'Overall Potential', 'Implementation Obstacles', 'Time to Revenue',
                 'External Risks', 'Overall Challenge', 'Opportunity Category'}
part2_ticks = sum(1 for label, opts in groups if label in part2_labels
                   for _, c in opts if c)
check("Part 2 ticks == 39 (3 opportunities x 13 groups)", part2_ticks == 39,
      f"actual={part2_ticks}")

part3_labels = {'Product Relatedness', 'Market Relatedness', 'Back-Up Option?',
                 'Growth Option?', 'Agile Strategy'}
part3_ticks = sum(1 for label, opts in groups if label in part3_labels
                   for _, c in opts if c)
check("Part 3 Opportunity Assessment ticks == 10 (2 opportunities x 5 groups)",
      part3_ticks == 10, f"actual={part3_ticks}")

# ---------- Check 5: word count excluding References ----------
ref_heading_idx = None
for i, p in enumerate(paras):
    if p.style.style_id == 'Heading1' and p.text.strip() == 'References':
        ref_heading_idx = i
        break

if ref_heading_idx is None:
    check("References heading found", False)
    body_word_count = None
else:
    check("References heading found", True)
    body_paras = paras[:ref_heading_idx]
    body_text = ' '.join(p.text for p in body_paras)
    words = re.findall(r"\S+", body_text)
    body_word_count = len(words)
    print(f"\nBody word count (excluding References section): {body_word_count}")

print("\n" + "=" * 60)
all_pass = all(ok for _, ok, _ in results)
print("OVERALL:", "ALL CHECKS PASS" if all_pass else "SOME CHECKS FAILED")
for name, ok, detail in results:
    if not ok:
        print(f"  FAILED: {name} -- {detail}")
