import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ASSIGN_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('OUTDIR', ASSIGN_DIR)
sys.path.insert(0, HERE)
import sys
from docx import Document

path = sys.argv[1]
doc = Document(path)
for i, p in enumerate(doc.paragraphs):
    print(f"{i}\t[{p.style.name}]\t{p.text!r}")
