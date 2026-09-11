---
id: csc900-2019-errors-incorrect-pedal-position-when-stopping-stopper
title: The pedals stop in the wrong position, and the stopper is re-plugged or replaced
kind: troubleshooting
question: Why do the pedals on a Spirit csc900-2019 stair climber stop in the wrong
  position?
asked_as:
- climbmill steps stop in a weird spot
- csc900 pedals not level when it stops
- stair climber stops with one step up
keywords:
- pedal position
- stopping
- stopper
- proximity switch
- loose wire
- climbmill
- stair climber
- step parking
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: no-code
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with: []
see_also:
- csc900-2019-errors-error-code-table
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 10, PDF p. 9; text.md
    lines 353-355
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **Issue:** Incorrect pedal position when stopping.

| Analysis | Method |
|---|---|
| Defective stopper or loose wire. | Re-plug or replace the stopper. |

**"Stopper" is the part that tells the controller where the steps are** so that they park in the right place; elsewhere in the same book the wiring diagram and the replacement pages call it the **proximity switch**, and the part label in the render reads `TL-N20ME PROXIMITY SWITCH`. Its cable is one of the three the controller-replacement page has you unplug (power-off brake, motor, proximity switch), which is where to find the plug to reseat.

**Re-plug before you replace.** The row lists a loose wire as a cause equal to a defective part, and the remedy starts with the plug.

No test is printed for the stopper - unlike the brake, the magnetic switch and the resistor, which all get a multimeter procedure later in the book.
