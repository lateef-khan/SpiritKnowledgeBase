---
id: ct900-osp-over-speed-warning
title: Inverter warning oSP - Over Speed Warning
kind: troubleshooting
question: What does inverter warning oSP mean on a CT900 and how do I fix it?
asked_as:
- what does osp mean on the inverter display
- over speed warning
keywords:
- osp
- over speed warning
- kpc-cc01
- inverter warning
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: osp
authority: 3
not_to_be_confused_with:
- ct900-e24-over-speed
- ct900-osl-over-slip-warning
see_also:
- ct900-e24-over-speed
- ct900-osl-over-slip-warning
source:
  ref: ct900-om
  locator: p. 47
  extracted_at: '2026-08-24'
---

**This is the inverter's oSP warning code (warning #13, Over Speed), not oSL (warning #12, Over Slip), and not the console's [E24 OVER SPEED](e24-over-speed.md) error code.** Press RESET to clear any Warning Code.

**Corrective actions**:
1. Verify if the frequency command is bigger than the maximum of main communication frequency.
2. Verify the settings of Pr03-12 and Pr03-14.
