---
id: ct900-pger-pg-feedback-loss-warning
title: Inverter warning PGEr - PG feedback loss warning
kind: troubleshooting
question: What does inverter warning PGEr mean on a CT900 and how do I fix it?
asked_as:
- what does pger mean on the inverter display
- pg feedback loss warning
keywords:
- pger
- pg feedback loss warning
- encoder warning
- kpc-cc01
- inverter warning
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: pger
authority: 3
not_to_be_confused_with:
- ct900-e26-encoder-err
see_also:
- ct900-e26-encoder-err
source:
  ref: ct900-om
  locator: p. 48
  extracted_at: '2026-08-24'
---

**This is the inverter's PGEr warning code (warning #21), not the console's [E26 ENCODER ERR](e26-encoder-err.md) error code** - a related but separate encoder/feedback fault in the inverter's own namespace. Press RESET to clear any Warning Code.

**Corrective actions**:
1. Verify if the Encoder works properly.
2. Verify the wiring of PG card.
3. Verify if the motor's speed is over the PG terminal's detection range.
4. Verify the setting of Pr02-31 ~Pr02-39.
