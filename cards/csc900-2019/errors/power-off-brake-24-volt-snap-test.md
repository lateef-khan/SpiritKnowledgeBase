---
id: csc900-2019-errors-power-off-brake-24-volt-snap-test
title: 'Feeding the power-off brake 24 volts directly: a snap means the brake is good,
  silence means it is bad'
kind: procedure
question: How do I test the power-off brake on a Spirit csc900-2019 stair climber?
asked_as:
- how to test the climbmill brake
- csc900 brake bench test 24v
- does the stair climber brake click when powered
keywords:
- power-off brake
- power failure brake
- 24v
- snap
- click
- power adapter
- bench test
- climbmill
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
- csc900-2019-errors-countdown-normal-no-code-and-no-motion-power-failure-brake
- csc900-2024-errors-brake-does-not-turn-on
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 7. Determination of defective accessories, Measurement of power-off brake,
    PDF p. 10-11; text.md lines 400-413
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** > Use the power adapter to draw a DC 24V voltage, and connect it directly to the two ends of the brake power line. If the brake makes a "snap" sound, the brake is normal. If there is no sound, the brake can be judged to be bad.

**The sound is the whole pass condition.** No coil resistance, no current and no dwell time is printed - a brake that snaps when 24 V is put across its two leads is good, one that stays silent is replaced. The photograph on the page shows the brake beside the machine's own power adapter, which is what supplies the 24 V.

**Why this test exists.** The brake is held open by power, and the console cannot see it; a dead brake shows as a normal countdown with no motion and no code (`csc900-2019-errors-countdown-normal-no-code-and-no-motion-power-failure-brake`). Feeding it directly takes the controller and the cable out of the question - if it snaps here and not in the machine, the fault is the supply line, not the brake.

The 2022 magnetic-system CSC900 book prints the same 24 V snap test and adds a second measurement at the controller's brake socket (`csc900-2024-errors-brake-does-not-turn-on`). This book has no controller-side figure.
