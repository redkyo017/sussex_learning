import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
from helpers import fix_typography
from fill_notes_doc import fill_notes

T = lambda s: fix_typography(s)

SRC = f"{ASSIGN_DIR}/Value Proposition Canvas_Blank.docx"
OUT = f"{OUT_DIR}/VPC_filled.docx"

BOXES = {
    'Customer Segment': T(
        "The survey or HSE manager at a UK utility asset owner, or at the tier-1 "
        "contractor digging on their behalf, who signs off pre-excavation risk on live "
        "streetworks. They are the buyer; the user is the crew on site; and the asset "
        "owner's insurer is a third party whose interests we can borrow."),
    'Jobs': T(
        "Know what is under the ground before breaking it, to a standard that can be "
        "defended afterwards. Specify and commission PAS 128 surveys, hold the "
        "programme to its dates, keep the crew safe, and return accurate records into "
        "the National Underground Asset Register. Today that is done with statutory "
        "record drawings, electromagnetic location, radar and trial holes."),
    'Gains': T(
        "An answer rather than a caveat. Fewer stoppages, fewer emergency "
        "reinstatements, fewer conversations with the HSE. A strike-rate improvement "
        "that can be shown to an insurer and a board. Data that stays useful after the "
        "job, through NUAR."),
    'Pains': T(
        "Records are often wrong: there are around 4 million km of buried pipes and "
        "cables, and a hole is dug every seven seconds (Geospatial Commission, 2024). "
        "Radar loses signal in wet, clay-rich ground and at depth, and electromagnetic "
        "location cannot see plastic, so surveys come back qualified as B3 or B4 "
        "(British Standards Institution, 2022) — which transfers risk back to the "
        "manager instead of removing it. Trial holes sample points only, and each costs "
        "time, traffic management and money. The worst outcome is not the invoice; it "
        "is the injury."),
    'Value Proposition': T(
        ('We tell contractors what lies under the ground on the sites where radar '
            'gives up. Stated honestly: we are slower per metre and coarser in '
            'resolution than radar in good conditions, so we are the second pass on '
            'hard ground, not a replacement for the first. Claiming more would put '
            'crews at risk, which is where responsible innovation stops being a '
            'seminar topic and becomes a design constraint (Stilgoe, Owen and '
            'Macnaghten, 2013).')),
    'Products and Features': T(
        'A survey service rather than an instrument sale: a trolley or vehicle-mounted quantum gravity gradiometer, run by our own crews as a targeted second pass on the sites the manager already fears. The deliverable is a depth-resolved density map with stated uncertainty on position and depth, issued in GIS and BIM formats and cross-referenced to PAS 128 quality levels.'),
    'Pain Relievers': T(
        "The sensor responds to density contrast, so wet clay and plastic pipes stop "
        "being the problem they are for radar and electromagnetic location, and voids, "
        "culverts and abandoned shafts become visible for the first time. Each survey "
        "removes several trial holes and the traffic management around them. Because "
        "the output carries explicit uncertainty (Stray et al., 2022), the manager "
        "prices residual risk instead of discovering it with a digger."),
    'Gain Creators': T(
        (('Priced by the day against the true cost of one strike, 29 times its '
             'repair bill (Utility Strike Avoidance Group, 2023), it is arithmetic a '
             'buyer can run themselves. We report outcomes on surveyed sites against '
             'the published national baseline, so the claim can be checked rather than'
             ' believed, and data is returned NUAR-ready, which turns a survey cost '
             'into an asset the owner keeps.'))),
}

fill_notes(SRC, OUT, BOXES)
