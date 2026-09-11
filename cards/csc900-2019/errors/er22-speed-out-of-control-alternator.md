---
id: csc900-2019-errors-er22-speed-out-of-control-alternator
title: ER22 with the speed out of control is the alternator, its wire, or the brake
  resistor
kind: troubleshooting
question: What does ER22 mean on a Spirit csc900-2019 stair climber?
asked_as:
- climbmill speed runs away and shows er22
- csc900 er22
- what does er22 mean on a spirit stair climber
keywords:
- er22
- alternator
- generator
- resistor
- speed out of control
- resistor wire
- climbmill
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: er22
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2019-errors-er07-safety-switch-connector
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2019-errors-er12-console-not-receiving-controller-data
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-brake-resistor-reads-about-half-an-ohm
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 3, PDF p. 9; text.md
    lines 309-318
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **This is ER22, and it exists only on the alternator-drive machine.** Neither the 2022 magnetic-system CSC900 book nor the CSC880 book prints an `ER22`; their over-current codes are `ER05` and `ER04`, and their magnet-wheel code is `ER02`. None of those is this.

**Issue:** When you press start, the speed is out of control, display message will show "ER22".

| Analysis | Method |
|---|---|
| Abnormal alternator. Explain: 1. Alternator wire off or not in good contact. 2. Brake resistor wire off or bad contact. 3. Alternator damage or resistor damage. | 1. Check alternator wire. 2. Check resistor wire. 3. Replace resistor. 4. Replace alternator. |

**Why an alternator controls the speed.** On this machine the steps drive an alternator through a transmission belt, and the electrical load on that alternator - a power resistor switched by the controller - is what holds the step speed. Lose the alternator wire or the resistor wire and there is no load, so the steps run away. That is why the code reads as a *speed* fault and the fix is wiring and a resistor.

**Two wires before two parts.** The method checks the alternator wire and the resistor wire first, then replaces the resistor, and only then the alternator - the cheapest thing last.

The resistor has a pass figure printed later in the book: **close to 0.5 ohms** across its two ends (`csc900-2019-errors-brake-resistor-reads-about-half-an-ohm`). No figure is printed for the alternator itself.
