---
id: erg700-2022-errors-light-sensor-problem-receiving-board-dust-cable-replace
title: 'A light sensor problem is checked four ways: the receiving board position,
  dust between the light point and the receiving point, the cable, then a new sensor'
kind: troubleshooting
question: What are the checks for a light sensor problem on an Xterra erg700-2022
  rower?
asked_as:
- xterra rower light sensor fault
- erg rower not counting strokes optical sensor
- rowing machine sensor dusty
- xterra rower stroke rate wrong
keywords:
- light sensor
- optical sensor
- photo sensor
- receiving board
- dust
- obstruction
- cable
- stroke count
- rower
facets:
  brand:
  - xterra
  product_line: rower
  model: erg700-2022
  applies_to:
  - erg700-2022
  section: errors
  code: '*'
  model_number:
  - '170918'
authority: 3
not_to_be_confused_with:
- xterra-rower-errors-no-count-or-distance-sensor-wire-then-monitor
see_also:
- crw800-2024-errors-light-sensor-problem
- sr500-2016-light-sensor-problem
- erg700-2022-errors-e2-cable-communication-abnormal-8-pin-cable-and-tension-motor
source:
  ref: xterra-rower-erg700-2022-owners-manual
  locator: ERG700 OM Troubleshooting table, PDF p. 26 (printed 23), text.md lines
    794-856 (also in the OCR supplement for that page)
  extracted_at: '2026-09-11'
---

**This rower reads its stroke optically, so its sensor row is a light-sensor row, not the reed-switch-and-magnet row of the other Xterra rowers** (`xterra-rower-errors-no-count-or-distance-sensor-wire-then-monitor`).

The condition is printed as *Light sensor problem*, and its Cause column is empty; the book prints only the solutions:

| Solution |
|---|
| Check that the receiving board is in the correct position |
| Check the light point and the receiving point for dust obstruction |
| Check the cable |
| Replace the light sensor |

**The second check costs nothing.** Dust between the emitter and the receiver stops the count without breaking anything, so clean before condemning the sensor. The book never says which readings fail when this sensor does - it prints no row for a stroke rate, distance or speed that reads zero - so this heading is all there is to work from.

The Spirit CRW800 and XRW600 (`crw800-2024-errors-light-sensor-problem`) and the Sole SR500 (`sr500-2016-light-sensor-problem`) print the same four steps for their own rowers; the Spirit books also print an RF handheld-board row above it that this book does not have.
