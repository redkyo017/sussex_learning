import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
import re
from helpers import fix_typography, fix_reference_dashes

def _curly(s):
    """Straight quote delimiters -> typographic, matching the Assignment 1 house style."""
    s = re.sub(r"'([^']*)'", lambda m: '\u2018' + m.group(1) + '\u2019', s)
    s = re.sub(r'"([^"]*)"', lambda m: '\u201c' + m.group(1) + '\u201d', s)
    return s


R = lambda s: _curly(fix_reference_dashes(fix_typography(s, apostrophes=False, currency=True)))

# Asterisks (*...*) mark italicised titles, preserved verbatim from portfolio_content.md
# so that merge.py can render them as italic runs.
REFERENCES = [
    R("British Standards Institution (2022) *PAS 128:2022 Underground utility "
      "detection, verification and location*. London: BSI."),
    R("Etzkowitz, H. and Leydesdorff, L. (2000) 'The dynamics of innovation: from "
      "National Systems and \"Mode 2\" to a Triple Helix of "
      "university-industry-government relations', *Research Policy*, 29(2), pp. "
      "109-123."),
    R("Geospatial Commission (2024) *National Underground Asset Register*. London: "
      "Department for Science, Innovation and Technology. Available at: "
      "https://www.nuar.uk (Accessed: 20 August 2026)."),
    R("Gruber, M. and Tal, S. (2017) *Where to play: 3 steps for discovering your "
      "most valuable market opportunities*. Harlow: Pearson."),
    R("HM Government (2023) *National quantum strategy*. London: Department for "
      "Science, Innovation and Technology."),
    R("Osterwalder, A. and Pigneur, Y. (2010) *Business model generation*. Hoboken, "
      "NJ: Wiley."),
    R("Osterwalder, A., Pigneur, Y., Bernarda, G. and Smith, A. (2014) *Value "
      "proposition design*. Hoboken, NJ: Wiley."),
    R("Rumelt, R. (2011) *Good strategy/bad strategy: the difference and why it "
      "matters*. London: Profile Books."),
    R("Stilgoe, J., Owen, R. and Macnaghten, P. (2013) 'Developing a framework for "
      "responsible innovation', *Research Policy*, 42(9), pp. 1568-1580."),
    R("Stray, B., Lamb, A., Kaushik, A., Vovrosh, J., Rodgers, A., Winch, J., "
      "Hayati, F., Boddice, D., Stabrawa, A., Niggebaum, A., Langlois, M., Lien, "
      "Y.-H., Lellouch, S., Roshanmanesh, S., Ridley, K., de Villiers, G., Brown, "
      "G., Cross, T., Tuckwell, G., Faramarzi, A., Metje, N., Bongs, K. and "
      "Holynski, M. (2022) 'Quantum sensing for gravity cartography', *Nature*, 602, "
      "pp. 590-594."),
    R("Teece, D.J. (1986) 'Profiting from technological innovation: implications "
      "for integration, collaboration, licensing and public policy', *Research "
      "Policy*, 15(6), pp. 285-305."),
    R("Tidd, J. and Bessant, J. (2021) *Managing innovation: integrating "
      "technological, market and organizational change*. 7th edn. Chichester: "
      "Wiley."),
    R("University of Birmingham (2025) *Delta.g secures GBP 4.6 million in "
      "oversubscribed seed round to advance quantum sensing*. Available at: "
      "https://www.birmingham.ac.uk/news/2025/delta.g-secures-4.6-million-in-"
      "oversubscribed-seed-round-to-advance-quantum-sensing "
      "(Accessed: 23 August 2026)."),
    R("Utility Strike Avoidance Group (2023) *Utility strike damage report*. "
      "Coventry: USAG."),
    R("von Hippel, E. (1986) 'Lead users: a source of novel product concepts', "
      "*Management Science*, 32(7), pp. 791-805."),
]


def parse_italic_segments(text):
    """Split text on '*' delimiters into (segment, is_italic) tuples."""
    parts = text.split('*')
    segments = []
    for i, part in enumerate(parts):
        if part == '':
            continue
        segments.append((part, i % 2 == 1))
    return segments


if __name__ == '__main__':
    for r in REFERENCES:
        print(r)
        print()
