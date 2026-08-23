cd module_2_emerging_markets_for_quantum_technology/assignment_2
python3 -m venv build/venv && ./build/venv/bin/pip install python-docx docxcompose
./build/venv/bin/python build/verify.py      # ALL CHECKS PASS
./build/venv/bin/python build/wordcount.py   # 1738 words (+16%) — deliberate, see CHANGES-2026-08-23.md
Those two outputs tell you the document arrived intact. If they pass and you don't want changes, Assessment2_Quantum_Portfolio.docx is ready to upload as-is.

To change anything, the one rule: the prose lives in two places — portfolio_content.md and the matching build/fill_*.py. Edit both, then:
./build/venv/bin/python build/fill_mon.py    # and fill_vpc.py, fill_bmc.py
./build/venv/bin/python build/merge.py
./build/venv/bin/python build/verify.py && ./build/venv/bin/python build/wordcount.py

If you're picking it up with Claude, paste this and it will orient itself:

▎ Read module_2_emerging_markets_for_quantum_technology/assignment_2/RUNBOOK.md and docs/superpowers/specs/2026-08-20-module2-assignment2-portfolio-design.md, then assignment_2/build/README.md. I'm continuing Module 2 Assignment 2. <what you want>

That matters because your Claude memory doesn't travel with the repo — the runbook and spec are what replace it, including the five arguments that must survive any edit.

Everything else — recipes for PDF export, Turnitin response, post-feedback — is in RUNBOOK.md §4.