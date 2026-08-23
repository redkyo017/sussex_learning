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
        'Suppliers: a university physics group for the licence; laser, vacuum and shielding vendors. Resources: the interferometry IP and absorptive capacity; components whose lead times become ours. Activities: training the people we hire; calibration and repair. Who else: a PAS 128 survey firm as channel; the Geospatial Commission through NUAR. Stakeholders: Innovate UK, the National Quantum Technologies Programme, HSE and unions, engaged while the product is still shapeable: the triple helix in practice (Etzkowitz and Leydesdorff, 2000).'),
    'Key Activities': T(
        "Value proposition: paid field trials with lead users on their worst sites rather than our best (von Hippel, 1986); inversion software; standards work with BSI so gravity becomes specifiable under PAS 128. Channels: training the partner's surveyors, settling the dual-use question early, since the instrument that finds a culvert finds a tunnel: export-control classification comes first. Relationships: recruiting and keeping the ten or so people who can do this."),
    'Value Proposition': T(
        'Problem: excavation on ground where radar and electromagnetic location fail. Need: depth-resolved subsurface maps with stated uncertainty, defensible after the event. What only they want: risk reduction per site that an insurer will recognise, so it is sold as that, not as quantum technology: nobody buys physics.'),
    'Relationships': T(
        "Expected: technical and consultative, not transactional; the manager must understand the uncertainty figure before signing. Repeat rather than one-off, because difficult sites recur. Maintained by a named crew per account, a data licence that renews, and a joint review after each survey, doubling as our post-project review: the learning routine Tidd and Bessant (2021) treat as a dynamic capability."),
    'Customer Segments': T(
        'Value is created for UK utility asset owners and tier-1 contractors on high-risk urban sites, and secondarily for highway, rail and local authorities. Most important: the first asset owners to allow trials on live sites, because their strike data becomes our evidence. Who else benefits: the site crew, the insurer, and the public whose street stays open, who never appear on the invoice.'),
    'Key Resources': T(
        "Value proposition: the licensed IP matters less than the tacit build-and-align knowledge staff hold, the part a competitor cannot buy, and the dataset of subsurface signatures that improves the inversion with every job. Channels: the partner's PAS 128 accreditation and field logistics. Relationships: the crews, and access control designed in from the first survey, because a map of what lies beneath critical infrastructure is a liability worth stealing."),
    'Channels': T(
        'Reach: direct technical selling into a handful of asset owners for the first paid trials, then framework agreements. Channels they use: accredited PAS 128 survey firms under existing frameworks, so we partner with one already holding the accreditation, relationships and logistics we lack. Fit: direct sales prove the method; the partner scales it. The channel is the complementary asset (Teece, 1986); building one from nothing would cost more than the sensor did.'),
    'Cost Structure': T(
        "Essential: people, instrument, fieldwork, compliance. Most expensive resources: physicists and field engineers, the largest, least compressible and scarcest cost; then the instrument's lasers, vacuum and shielding, and its vehicle. Most expensive activities: field trials and traffic management. Standards, certification and export-control compliance are small lines, easy to underestimate and awkward to retrofit."),
    'Revenue Streams': T(
        'Willing to pay: a day rate set against the cost of one strike, as this industry already buys. Preferred: per-site day rates under a framework, with a renewing licence for the processed dataset. Contribution, as a planning assumption rather than a forecast: surveys about two-thirds of early revenue, data licences and re-surveys a fifth, Innovate UK and quantum-mission grants the rest, costing no equity. Leasing only later, once know-how is no longer the product.'),
}

fill_notes(SRC, OUT, BOXES)
