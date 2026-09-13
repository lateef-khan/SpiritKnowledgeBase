---
id: tt9-2018-errors-e1-motor-not-responsive
title: 'E1 with no belt movement after Start: calibrate or contact service'
kind: troubleshooting
question: What does E1 mean when the motor is not responsive after Start on a Sole
  TT9-2018?
asked_as:
- tt9 shows e1 and stops
- press start belt never moves e1
- what is e1 on my sole tt9
keywords:
- e1
- motor not responsive
- belt stops
- run calibration
- contact service
- tt9
- low speed
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt9-2018
  applies_to:
  - tt9-2018
  section: errors
  code: e1
  model_number:
  - '599818'
authority: 3
not_to_be_confused_with:
- f65-2023-e1-no-rpm-signal
- f63-2026-e01-error-code
- xt-2023-errors-e1-motor-not-responsive
- f80-2016-motor-not-responsive-after-start
see_also:
- sole-inverter-error-code-list
source:
  ref: sole-tm-tt9-2018-owners-manual
  locator: SERVICE CHECKLIST table, PDF p. 41, text.md lines 1241-1290
  extracted_at: '2026-09-12'
---

**This is the TT9's E1, not the DC-controller E1 (no RPM signal), not a 2026 E01 (overload), and not Spirit's E1.** The TT9 uses a Rhymebus AC inverter whose own code set is `sole-inverter-error-code-list` — this bare E1 sits outside that set, in the owner's troubleshooting table.

> Motor is not responsive after pressing Start — 1. If the belt moves, but stops after a short time and the display shows "E1", run calibration. 2. If you press Start and the belt never moves, then the display shows "E1", contact service.

Same two branches as the LS rows in the DC-controller books, with the code printed as E1. Never carry the DC E1 sensor/controller/motor remedies onto this machine, and never carry this run-calibration answer onto a DC E1.

Gap in this book: it says "run calibration" but prints no calibration procedure — "factory settings", "engineering mode", "maintenance menu", "wheel size" and "calibration procedure" all return zero hits, and "calibration" appears exactly once, in this row.
