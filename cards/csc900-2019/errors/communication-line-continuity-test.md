---
id: csc900-2019-errors-communication-line-continuity-test
title: 'Buzzing out the communication line: each same-colour conductor end to end,
  near zero ohms is good'
kind: procedure
question: How do I test the communication line between the console and the controller
  on a Spirit csc900-2019 stair climber?
asked_as:
- how to test the climbmill console cable
- csc900 control wire continuity check
- multimeter test for the stair climber communication wire
keywords:
- communication line
- continuity
- multimeter
- buzzer
- control wire
- same colour
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
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with: []
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2019-errors-er12-console-not-receiving-controller-data
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 7. Determination of defective accessories, Communication line continuity
    measurement, PDF p. 10; text.md lines 374-399
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** This is the test the ER11, ER12 and no-power rows rely on, printed once on its own page.

> Use the multi-meter's two test leads to contact the upper and lower terminals of the control line, measure the same color line, and set the buzzer position. The multi-meter has a beeping sound and the resistance value is close to 0 ohms, then the line is normally conducting. If there is no resistance value, the line is disconnected. Generally it is pinch off or the terminal is not in good contact. You can replace the control wire for troubleshooting.

The two probe positions the page draws: the **red** lead on the upper control line, inside the fuselage cover behind the console; the **black** lead on the lower control line, inside the controller. *Test whether the lines with the same serial number are connected at both ends.*

**Match colour to colour, one conductor at a time.** The line is a multi-way cable, and the test is a continuity buzz on each conductor between its two ends - a beep and something close to 0 ohms passes, an open circuit fails. The book gives no resistance ceiling beyond "close to 0 ohms".

**What an open usually is.** The book says a failed line is generally pinched ("pinch off") or a terminal that is not seated - which is why the code rows say to replace the wire rather than repair it, and why "extruded" appears in the ER12 row: the mast crushes it.
