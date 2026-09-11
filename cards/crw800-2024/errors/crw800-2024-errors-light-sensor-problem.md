---
id: crw800-2024-errors-light-sensor-problem
title: The light sensor row lists four checks, starting with dust between the light
  point and the receiving point
kind: troubleshooting
question: What are the checks for a light sensor problem on a Spirit CRW800 or XRW600
  rower?
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
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - xrw600-2019
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-speed-abnormal-then-data-resets
see_also:
- crw800-2024-errors-rf-handheld-board-problem
- csc900-2024-errors-speed-abnormal-then-data-resets
- spirit-crw800-errors-count-not-shown-or-no-display-check-board-34-and-the-three-cables
- sr500-2016-light-sensor-problem
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, Happening / Caused / Processing
    Step table on printed pages 32 and 33. Both pages are flat pictures with no text
    layer and were read from the rendered page; CRW800 2016 (CW800-YR001) service
    manual 8.5 Troubleshooting Quick Lookup Table, PDF p. 38-39, text.md lines 487-519;
    XRW600 (DW400-YR002) service manual 8.5 Troubleshooting Quick Lookup Table, PDF
    p. 38-39, text.md lines 478-505; CRW800 2021 (800940) service manual 7-5 Troubleshooting
    Quick Lookup Table, PDF p. 37 (printed 36), text.md lines 536-561; CRW800 2016
    8.8 Light sensor problem, PDF p. 40, text.md lines 543-547; XRW600 8.8 Photo coupler
    sensor problem (RPM sensor device), PDF p. 39-40, text.md lines 526-533; CRW800
    2021 7-7-3, PDF p. 39 (printed 38), text.md lines 595-600
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

## The three rower service manuals print this row word for word, and the XRW600 names what the sensor does

The CRW800 2016 (`CW800-YR001`), CRW800 2021 (`800940`) and XRW600 (`DW400-YR002`) service manuals all print the four steps above, and each repeats them as a lettered list on the next page. **The XRW600's heading for that list is `Photo coupler sensor problem (RPM sensor device)`** - which answers the question the owner's manual leaves open: this sensor is the stroke counter, and the readings that depend on it are the stroke rate and everything derived from it. The Q&A chapter of all three books calls the same part *optical coupler Board (34)* and sends a console that does not count to it (`spirit-crw800-errors-count-not-shown-or-no-display-check-board-34-and-the-three-cables`). Sole's SR500 2016 prints this row (`sr500-2016-light-sensor-problem`).
