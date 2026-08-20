import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
from helpers import fix_typography
from fill_notes_doc import fill_notes

T = lambda s: fix_typography(s)

SRC = f"{ASSIGN_DIR}/Business Model Canvas_Blank.docx"
OUT = f"{OUT_DIR}/BMC_filled.docx"

BOXES = {
    'Key Partners': T(
        ('A university physics group for the licence and continued absorptive '
            'capacity; laser, vacuum and shielding suppliers whose lead times become '
            'ours; a survey firm as channel; the Geospatial Commission through NUAR; '
            'Innovate UK and the National Quantum Technologies Programme. This is the'
            ' triple helix in practice rather than in theory (Etzkowitz and '
            'Leydesdorff, 2000): the venture exists only where university, industry '
            'and state overlap. Engaging the HSE and unions early costs little and '
            'shapes the product while it is still shapeable.')),
    'Key Activities': T(
        "Paid field trials with lead users, on their worst sites rather than our best "
        "ones (von Hippel, 1986). Inversion software. Standards work with BSI so that "
        "gravity methods become specifiable under PAS 128. Recruiting and keeping the "
        "ten or so people who can do this. We also settle the dual-use question early: "
        "the instrument that finds a culvert finds a tunnel, so export-control "
        "classification happens before the first defence conversation, not after."),
    'Value Proposition': T(
        "Depth-resolved subsurface maps, with stated uncertainty, on the ground where "
        "existing methods fail. Sold as risk reduction per site, not as quantum "
        "technology, because nobody buys physics."),
    'Relationships': T(
        "Repeat rather than one-off, because difficult sites recur. A named crew per "
        "account, a data licence that renews, and a joint review after each survey, "
        "which is also our post-project review: the learning routine Tidd and Bessant "
        "(2021) treat as a dynamic complementary asset in its own right."),
    'Customer Segments': T(
        "Primary: UK utility asset owners and tier-1 contractors working high-risk "
        "urban sites. Secondary: highway, rail and local authorities commissioning "
        "ground investigation. The user is the site crew, the payer is the capital "
        "projects or survey budget, and the beneficiary who never appears on the "
        "invoice is the public whose street stays open."),
    'Key Resources': T(
        "The licensed interferometry IP matters less than the tacit build-and-align "
        "knowledge held by staff, which is the part a competitor cannot buy. The "
        "crews. The accumulating dataset of subsurface signatures, which improves the "
        "inversion with every job. The dataset is also a liability: a map of what lies "
        "beneath critical infrastructure is worth stealing, so access control is "
        "designed in from the first survey."),
    'Channels': T(
        ('Direct technical selling into a handful of asset owners for the first '
            'paid trials, then framework agreements. Alongside that, a partnership '
            'with an established PAS 128 survey firm that already holds the '
            'accreditation, the customer relationships and the field logistics we '
            'lack. Teece (1986) explains why: the channel is the complementary asset,'
            ' and building one from nothing would cost more than the sensor did.')),
    'Cost Structure': T(
        "People first: physicists and field engineers are the largest, least "
        "compressible and scarcest cost. Then the instrument, its lasers, vacuum and "
        "shielding, and the vehicle carrying it. Field operations and traffic "
        "management. Standards, certification and export-control compliance are small "
        "lines, easy to underestimate and awkward to retrofit."),
    'Revenue Streams': T(
        "Day rates for surveys, which is how this industry already buys. A licence for "
        "the processed dataset, plus re-surveys. Grant income from Innovate UK and the "
        "quantum missions as early revenue that costs no equity. Instrument leasing "
        "only later, once the crews' know-how is no longer the product."),
}

fill_notes(SRC, OUT, BOXES)
