---
id: mt200-2022-errors-step-sensors-no-response-10-to-12-v-dc
title: 'A step sensor gives no response: 10 to 12 V DC at the sensor connector means
  the sensor, at the board means the cable, none means the board'
kind: troubleshooting
question: What do I check when the step sensor test shows no response on one or both
  sides of a Spirit mt200-2022 treadmill?
asked_as:
- step sensor not working on my 7.0t
- symmetry display shows nothing on one side
- step sensor voltage check
keywords:
- step sensor
- symmetry
- sensor test
- maintenance mode
- 10-12v dc
- pin 1 pin 2
- low control board
- left right
- replace sensor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: mt200-2022
  applies_to:
  - mt200-2022
  section: errors
  code: no-code
  model_number:
  - '720080'
  - '720087'
authority: 3
not_to_be_confused_with: []
see_also:
- mt200-2022-errors-no-power-console-does-not-light-five-steps
source:
  ref: spirit-treadmill-mt200-2022-service-manual
  locator: 7.0T (MT200 2022) service manual 5. Troubleshooting and Problem solving,
    item 4 Step sensors, PDF p. 22, text.md lines 433-448
  extracted_at: '2026-09-11'
---

Section 5, item 4 of the 7.0T service manual. Start with the step-sensor test in maintenance mode (a console fact); if one side or both show no response on the display:

1. Disconnect the cable at the step sensor and measure the DC voltage on the connector coming from the lower control board, **between pin 1 and pin 2. 10 to 12 V DC there means the sensor is at fault - replace the sensor.** No voltage: next step.
2. Measure the same output, pin 1 to pin 2, at the **red control board** - **LEFT for the left sensor, RIGHT for the right**. 10 to 12 V DC here but not at the sensor means the cable - replace it. No voltage here means the low control board - change it.

The sensors themselves are calibrated by moving their magnets until the maintenance-mode reading matches a target of 65 (a console procedure), and their mechanical adjustment is in the parts chapter. This card is only the electrical fault-finding.
