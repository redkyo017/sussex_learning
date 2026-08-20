# Assignment 2 Portfolio — content plan and full draft

**Venture:** Substrata Quantum Ltd — a proposed UK spin-out commercialising cold-atom
gravity gradiometry for subsurface survey.

**Chain of argument:** MON Part 3 selects pre-excavation utility survey as the primary
opportunity -> VPC drills into one segment inside it -> BMC answers the value-capture
question the MON raised (sell surveys and data, not instruments).

**Word budget:** MON ~520, VPC ~490, BMC ~490 = ~1500. Template prompt text and the
reference list are not counted.

---

# ITEM 1 — MARKET OPPORTUNITY NAVIGATOR

## Part 1 — Market Opportunity Set

### Core Ability 1 — Differential cold-atom interferometry
Description: Measures the difference in gravitational acceleration between two clouds of
laser-cooled atoms falling in one apparatus. It reads density contrast, so it needs no line
of sight, no contact and no excavation.

### Core Ability 2 — Rejection of real-world noise
Description: Vibration is common to both atom clouds and cancels in the differential
measurement; accelerometers and shielding handle the rest. This is what took the instrument
off the optical bench and onto a street (Stray et al., 2022).

### Core Ability 3 — Inference under uncertainty
Description: Bayesian inversion turns sparse gradient readings into a three-dimensional
density estimate, and reports its confidence in position and depth rather than drawing one
certain line.

### Core Ability 4 — Field engineering of a laboratory instrument
Description: Packaging lasers, vacuum and shielding into equipment a trained surveyor can
run through a working day. Most of it is tacit knowledge held by people, which matters later
for value capture.

### Opportunity 1
Application: Targeted pre-excavation survey of high-risk urban sites, finding buried assets,
voids and abandoned structures that electromagnetic location and radar miss.
Customer Group: UK water, gas, power and telecoms asset owners, the tier-1 contractors
digging on their behalf, and highway and rail authorities.

### Opportunity 2
Application: Density targeting for mineral exploration and geothermal assessment, narrowing
down where to drill before anyone drills.
Customer Group: Exploration companies, geothermal developers, and the geophysical survey
contractors who serve them.

### Opportunity 3
Application: Drift-free inertial navigation where satellite signals are jammed, spoofed or
unavailable.
Customer Group: The Ministry of Defence and defence primes first, maritime and aviation
operators later.

## Part 2 — Market Attractiveness

### Opportunity 1: Pre-excavation subsurface survey
Impact — Problem Severity: HIGH. Pertinent Solution: HIGH. Impact Reach: HIGH.
Overall Impact: HIGH.
Potential — Compelling Reasons to Buy: HIGH. Potential Market Volume: MEDIUM.
Economic Viability: HIGH. Overall Potential: HIGH.
Challenge — Implementation Obstacles: MEDIUM. Time to Revenue: MEDIUM.
External Risks: HIGH. Overall Challenge: MEDIUM.
Impact and potential: One hole in every 65 hits something: about 60,000 strikes a year,
GBP 2.4bn of economic cost, and a true cost 29 times the repair bill (Utility Strike
Avoidance Group, 2023). Workers are hurt. Contractors already buy PAS 128 surveys, so a
budget line and a standard exist to sell against (British Standards Institution, 2022), and
strike rates are reported nationally, so improvement can be shown rather than claimed.
Challenge: The physics already works outdoors, so this is productisation, not discovery.
Two risks bite: PAS 128 recognises radar and electromagnetic location, not gravity; and
Delta.g, a Birmingham spin-out holding GBP 4.6m of seed funding, is ahead of us on the same
road (The Quantum Insider, 2025).
Opportunity Category: GOLD MINE — the highest potential and lowest challenge of the three,
judged against each other rather than in the abstract.

### Opportunity 2: Mineral and geothermal exploration
Impact — Problem Severity: MEDIUM. Pertinent Solution: MEDIUM. Impact Reach: MEDIUM.
Overall Impact: MEDIUM.
Potential — Compelling Reasons to Buy: HIGH. Potential Market Volume: HIGH.
Economic Viability: MEDIUM. Overall Potential: HIGH.
Challenge — Implementation Obstacles: HIGH. Time to Revenue: HIGH. External Risks: MEDIUM.
Overall Challenge: HIGH.
Impact and potential: Better targeting means fewer speculative boreholes, though the harm
avoided is diffuse next to a gas main struck in a city street. Global exploration budgets
dwarf UK survey spend, and drilling costs enough that a better target is worth paying for.
Challenge: Remote sites, power and calibration in harsh conditions sit beyond our packaging.
Campaigns are seasonal, procurement slow, and airborne gradiometry already serves this
market.
Opportunity Category: MOON SHOT.

### Opportunity 3: GPS-denied navigation
Impact — Problem Severity: HIGH. Pertinent Solution: MEDIUM. Impact Reach: MEDIUM.
Overall Impact: MEDIUM.
Potential — Compelling Reasons to Buy: HIGH. Potential Market Volume: MEDIUM.
Economic Viability: MEDIUM. Overall Potential: HIGH.
Challenge — Implementation Obstacles: VERY HIGH. Time to Revenue: VERY HIGH.
External Risks: HIGH. Overall Challenge: VERY HIGH.
Impact and potential: Satellite navigation is jammed and spoofed routinely, with
consequences running from delayed shipping to lost life. The national mission targets quantum
navigation on aircraft by 2030 (HM Government, 2023), so the state agrees the problem is
severe even where no commercial market exists. Defence buyers pay well, but are few and slow.
Challenge: A survey instrument may stand still; a navigator must work while moving, at a
fraction of the size, weight and power. Export control applies, and the dual-use question
becomes ours to answer rather than postpone.
Opportunity Category: MOON SHOT.

## Part 3 — Agile Focus Strategy

Primary Opportunity: Opportunity 1, pre-excavation subsurface survey.
Other Opportunities: Opportunity 2, mineral and geothermal exploration; Opportunity 3,
GPS-denied navigation.
Opportunity 1 — Agile Strategy: PURSUE NOW.
Opportunity 2 — Product Relatedness: HIGH. Market Relatedness: LOW.
Back-Up Option: YES. Growth Option: NO. Agile Strategy: KEEP OPEN.
Opportunity 3 — Product Relatedness: MEDIUM. Market Relatedness: LOW.
Back-Up Option: NO. Growth Option: YES. Agile Strategy: KEEP OPEN.

Notes: The kernel is Rumelt's (2011). Our diagnosis is a laboratory-grade sensor with no
route to a customer; the guiding policy is to earn revenue surveying the ground everyone
else struggles with, so the instrument matures on a client's site rather than in our
laboratory. Exploration is a genuine back-up, because its buyers and drivers are unrelated
to UK construction: a stall in contractor adoption would not stop it. It is not a hedge
against technical failure, since all three options need the same sensor to work, and
pretending otherwise is the comfortable fiction this tool exists to prevent (Gruber and Tal,
2017). Keeping both open costs design headroom and one data-sharing agreement, but no
engineers.

---

# ITEM 2 — VALUE PROPOSITION CANVAS

## Customer Segment
Notes: The survey or HSE manager at a UK utility asset owner, or at the tier-1 contractor
digging on their behalf, who signs off pre-excavation risk on live streetworks. They are
the buyer; the user is the crew on site; and the asset owner's insurer is a third party
whose interests we can borrow.

### Jobs
Know what is under the ground before breaking it, to a standard that can be defended
afterwards. Specify and commission PAS 128 surveys, hold the programme to its dates, keep
the crew safe, and return accurate records into the National Underground Asset Register.
Today that is done with statutory record drawings, electromagnetic location, radar and
trial holes.

### Pains
Records are often wrong: there are around 4 million km of buried pipes and cables, and a
hole is dug every seven seconds (Geospatial Commission, 2024). Radar loses signal in wet,
clay-rich ground and at depth, and electromagnetic location cannot see plastic, so surveys
come back qualified as B3 or B4 (British Standards Institution, 2022) — which transfers risk
back to the manager instead of removing it. Trial holes sample points only, and each costs
time, traffic management and money. The worst outcome is not the invoice; it is the injury.

### Gains
An answer rather than a caveat. Fewer stoppages, fewer emergency reinstatements, fewer
conversations with the HSE. A strike-rate improvement that can be shown to an insurer and
a board. Data that stays useful after the job, through NUAR.

## Value Proposition
Notes: We tell contractors what lies under the ground on the sites where radar gives up.
Stated honestly: we are slower per metre and coarser in resolution than radar in good
conditions, so we are the second pass on hard ground, not a replacement for the first.
Claiming more would put crews at risk, which is the point at which responsible innovation
stops being a seminar topic and starts being a design constraint (Stilgoe, Owen and
Macnaghten, 2013).

### Products and Features
A survey service rather than an instrument sale: a trolley or vehicle-mounted quantum
gravity gradiometer, run by our own crews as a targeted second pass on the sites the manager
already worries about. The deliverable is a depth-resolved density map with stated
uncertainty on position and depth, issued in GIS and BIM formats and cross-referenced to
PAS 128 quality levels.

### Pain Relievers
The sensor responds to density contrast, so wet clay and plastic pipes stop being the
problem they are for radar and electromagnetic location, and voids, culverts and abandoned
shafts become visible for the first time. Each survey removes several trial holes and the
traffic management around them. Because the output carries explicit uncertainty (Stray et
al., 2022), the manager prices residual risk instead of discovering it with a digger.

### Gain Creators
Priced by the day against the 29-times multiplier on a single strike, the arithmetic is
one a buyer can run themselves. We report outcomes on surveyed sites against the published
national baseline, so the claim can be checked rather than believed, and data is returned
NUAR-ready, which turns a survey cost into an asset the owner keeps.

---

# ITEM 3 — BUSINESS MODEL CANVAS

### Customer Segments
Primary: UK utility asset owners and tier-1 contractors working high-risk urban sites.
Secondary: highway, rail and local authorities commissioning ground investigation. The user
is the site crew, the payer is the capital projects or survey budget, and the beneficiary
who never appears on the invoice is the public whose street stays open.

### Value Proposition
Depth-resolved subsurface maps, with stated uncertainty, on the ground where existing
methods fail. Sold as risk reduction per site, not as quantum technology, because nobody
buys physics.

### Channels
Direct technical selling into a handful of asset owners for the first paid trials, then
framework agreements. Alongside that, a partnership with an established PAS 128 survey firm
that already holds the accreditation, the customer relationships and the field logistics we
lack. Teece (1986) explains why: the channel is the complementary asset, and building one
from nothing would cost more than building the sensor did.

### Customer Relationships
Repeat rather than one-off, because difficult sites recur. A named crew per account, a data
licence that renews, and a joint review after each survey, which is also our post-project
review: the learning routine Tidd and Bessant (2021) treat as a dynamic complementary asset
in its own right.

### Revenue Streams
Day rates for surveys, which is how this industry already buys. A licence for the processed
dataset, plus re-surveys. Grant income from Innovate UK and the quantum missions as early
revenue that costs no equity. Instrument leasing only later, once the crews' know-how is no
longer the product.

### Key Activities
Paid field trials with lead users, on their worst sites rather than our best ones (von
Hippel, 1986). Inversion software. Standards work with BSI so that gravity methods become
specifiable under PAS 128. Recruiting and keeping the ten or so people who can do this. We
also settle the dual-use question early: the instrument that finds a culvert finds a tunnel,
so export-control classification happens before the first defence conversation, not after.

### Key Resources
The licensed interferometry IP matters less than the tacit build-and-align knowledge held by
staff, which is the part a competitor cannot buy. The crews. The accumulating dataset of
subsurface signatures, which improves the inversion with every job. The dataset is also a
liability: a map of what lies beneath critical infrastructure is worth stealing, so access
control is designed in from the first survey.

### Key Partners
A university physics group for the licence and continued absorptive capacity; laser, vacuum
and shielding suppliers whose lead times become ours; a survey firm as channel; the
Geospatial Commission through NUAR; Innovate UK and the National Quantum Technologies
Programme. This is the triple helix in practice rather than in theory (Etzkowitz and
Leydesdorff, 2000): the venture exists only where university, industry and state overlap.
Engaging the HSE and the unions early costs little and shapes the product while it is still
shapeable.

### Cost Structure
People first: physicists and field engineers are the largest, least compressible and
scarcest cost. Then the instrument, its lasers, vacuum and shielding, and the vehicle
carrying it. Field operations and traffic management. Standards, certification and
export-control compliance are small lines, easy to underestimate and awkward to retrofit.

---

# REFERENCES

British Standards Institution (2022) *PAS 128:2022 Underground utility detection,
verification and location*. London: BSI.

Etzkowitz, H. and Leydesdorff, L. (2000) 'The dynamics of innovation: from National Systems
and "Mode 2" to a Triple Helix of university-industry-government relations', *Research
Policy*, 29(2), pp. 109-123.

Geospatial Commission (2024) *National Underground Asset Register*. London: Department for
Science, Innovation and Technology. Available at: https://www.nuar.uk (Accessed: 20 August
2026).

Gruber, M. and Tal, S. (2017) *Where to play: 3 steps for discovering your most valuable
market opportunities*. Harlow: Pearson.

HM Government (2023) *National quantum strategy*. London: Department for Science,
Innovation and Technology.

Osterwalder, A. and Pigneur, Y. (2010) *Business model generation*. Hoboken, NJ: Wiley.

Osterwalder, A., Pigneur, Y., Bernarda, G. and Smith, A. (2014) *Value proposition design*.
Hoboken, NJ: Wiley.

Rumelt, R. (2011) *Good strategy/bad strategy: the difference and why it matters*. London:
Profile Books.

Stilgoe, J., Owen, R. and Macnaghten, P. (2013) 'Developing a framework for responsible
innovation', *Research Policy*, 42(9), pp. 1568-1580.

Stray, B., Lamb, A., Kaushik, A., Vovrosh, J., Rodgers, A., Winch, J., Hayati, F., Boddice,
D., Stabrawa, A., Niggebaum, A., Langlois, M., Lien, Y.-H., Lellouch, S., Roshanmanesh, S.,
Ridley, K., de Villiers, G., Brown, G., Cross, T., Tuckwell, G., Faramarzi, A., Metje, N.,
Bongs, K. and Holynski, M. (2022) 'Quantum sensing for gravity cartography', *Nature*, 602,
pp. 590-594.

Teece, D.J. (1986) 'Profiting from technological innovation: implications for integration,
collaboration, licensing and public policy', *Research Policy*, 15(6), pp. 285-305.

The Quantum Insider (2025) *University of Birmingham spin-out Delta.g raises GBP 4.6 million
in oversubscribed seed round*. Available at: https://thequantuminsider.com (Accessed: 20
August 2026).

Tidd, J. and Bessant, J. (2021) *Managing innovation: integrating technological, market and
organizational change*. 7th edn. Chichester: Wiley.

Utility Strike Avoidance Group (2023) *Utility strike damage report*. Coventry: USAG.

von Hippel, E. (1986) 'Lead users: a source of novel product concepts', *Management
Science*, 32(7), pp. 791-805.
