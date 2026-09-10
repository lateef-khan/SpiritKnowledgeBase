---
id: crw800-2024-errors-light-sensor-problem
title: The light sensor row lists four checks, starting with dust between the light point and the receiving point
kind: troubleshooting
question: What are the checks for a light sensor problem on a Spirit CRW800-2024 rower?
asked_as:
- no stroke count on my spirit rower
- light sensor fault on a crw800
- rower is not counting my strokes
keywords:
- light sensor
- optical sensor
- receiving board
- dust
- obstruction
- cable
- stroke count
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-speed-abnormal-then-data-resets
see_also:
- crw800-2024-errors-rf-handheld-board-problem
- csc900-2024-errors-speed-abnormal-then-data-resets
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, Happening / Caused /
    Processing Step table on printed pages 32 and 33. Both pages are flat pictures with
    no text layer and were read from the rendered page.
  extracted_at: '2026-09-10'
---

The condition is printed as `Light sensor problem`, and **the Caused column beside it is empty**, as
it is for the RF board row above it.

| Processing Step |
|---|
| 1. Check that the receiving board is in the correct position |
| 2. Check the light point and the receiving point for dust obstruction |
| 3. Check the cable |
| 4. Replace the light sensor |

**Step 2 is the one that costs nothing.** This machine reads its stroke rate optically, so dust
between the emitter and the receiver stops it counting without breaking anything - clean before you
condemn.

**The manual never says which readings depend on this sensor.** It prints no row for a stroke rate
or distance that reads zero or wrong, so this heading is all a technician has to work from.

The Spirit CSC900 2024 stairclimber uses the same kind of sensor and *does* print the symptom - an
abnormal speed that resets three seconds after stopping - together with a sensor-to-grating gap check
(`csc900-2024-errors-speed-abnormal-then-data-resets`). Different machine, but the same failure mode
described in full.
