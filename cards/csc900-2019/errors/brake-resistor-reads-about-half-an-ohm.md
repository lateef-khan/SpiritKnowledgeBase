---
id: csc900-2019-errors-brake-resistor-reads-about-half-an-ohm
title: The brake resistor measures close to half an ohm across its two ends, and open
  or too high means it is bad
kind: procedure
question: How do I test the power resistor on a Spirit csc900-2019 stair climber?
asked_as:
- how to test the climbmill resistor
- csc900 brake resistor reading
- what should the stair climber power resistor measure
keywords:
- power resistor
- brake resistor
- 0.5 ohm
- resistance
- multimeter
- alternator load
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
- csc900-2019-errors-er22-speed-out-of-control-alternator
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 7. Determination of defective accessories, Resistor measurement, PDF p.
    11; text.md lines 423-434
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** > The multi-meter scale is adjusted to the resistance level, and the two red and black test leads respectively contact the two ends of the resistance. The multi-meter shows that the value is close to 0.5 ohms is normal. If there is no resistance value or the resistance value is too large, it can be judged that the resistance is bad.

**Close to 0.5 ohms is the pass figure**, measured across the resistor's two terminals with the meter on ohms. An open circuit or a reading well above that condemns it. No tolerance band is printed beyond "close to".

**This is the load the alternator works against**, and it is why the resistor sits in the ER22 row (`csc900-2019-errors-er22-speed-out-of-control-alternator`): with the resistor open the alternator has nothing to push into and the steps run away. Measure it before replacing it - it is step 3 of that row, and the alternator is step 4.

Half an ohm is a small figure, and a meter's own lead resistance is a fair part of it; touch the leads together first and subtract what the meter shows.
