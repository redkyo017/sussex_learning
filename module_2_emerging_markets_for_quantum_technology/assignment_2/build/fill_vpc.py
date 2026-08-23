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
        "The survey or HSE manager at a UK utility asset owner, or at the tier-1 contractor digging for them, who signs off pre-excavation risk. They are the buyer; the site crew is the user; the asset owner's insurer is a third party whose interests we can borrow."),
    'Jobs': T(
        'Interaction: commissioned per site as a second pass beside a PAS 128 contract; they receive a map, not an instrument. Context: always to know what is under the ground before breaking it; on a verge a compliance step, beside a gas main a safety sign-off that must be defensible afterwards. Current tools: record drawings, electromagnetic location, radar and trial holes, returned into NUAR.'),
    'Gains': T(
        'Measured by strike rate per thousand excavations, PAS 128 quality level achieved, and days lost to stoppages. Time is the saving valued most: an emergency reinstatement closes a street for longer than the survey took. Socially they want fewer injured workers, fewer disrupted streets, and data that stays useful through NUAR. They would pay most for a strike-rate improvement they can show an insurer and a board.'),
    'Pains': T(
        'Barriers: records are often wrong, with around 4 million km of buried pipes and cables and a hole dug every seven seconds (Geospatial Commission, 2024); trial holes sample points only, at a cost in money and closures. Challenges: radar loses signal in wet, clay-rich ground and at depth; electromagnetic location cannot see plastic. Underperformance: surveys come back qualified as B3 or B4 (British Standards Institution, 2022), handing the risk back to the manager. The worst outcome is not the invoice; it is the injury.'),
    'Value Proposition': T(
        'We tell contractors what lies under the ground on the sites where radar gives up. Stated honestly: we are slower per metre and coarser than radar in good conditions, so we are the second pass on hard ground, not a replacement for the first. Claiming more would put crews at risk, which is where responsible innovation becomes a design constraint (Stilgoe, Owen and Macnaghten, 2013).'),
    'Products and Features': T(
        'A survey service, not an instrument sale: a trolley or vehicle-mounted quantum gravity gradiometer run by our own crews. One specific job, the risk sign-off on difficult ground, not a variety. The features are both tangible and digital: the field service, and a depth-resolved density map with stated uncertainty, issued in GIS and BIM formats and cross-referenced to PAS 128 quality levels.'),
    'Pain Relievers': T(
        'Frustrations: the sensor responds to density contrast, so wet clay and plastic pipes stop being the problem they are for radar and electromagnetic location. Improvement: voids, culverts and abandoned shafts become visible, and each survey removes several trial holes. Risk: the output carries explicit uncertainty (Stray et al., 2022), so the manager prices residual risk instead of discovering it with a digger. It mitigates rather than eliminates: PAS 128 does not yet recognise gravity methods.'),
    'Gain Creators': T(
        'Savings: priced by the day against the true cost of one strike, 29 times its repair bill (Utility Strike Avoidance Group, 2023), it is arithmetic a buyer can run themselves. Expectations: on the ground it is built for it exceeds them, because current methods return a caveat there; in good conditions it only meets them, and we say so. Outperformance: outcomes are reported against the national baseline, so the claim can be checked, and data is returned NUAR-ready, turning a survey cost into an asset the owner keeps.'),
}

fill_notes(SRC, OUT, BOXES)
