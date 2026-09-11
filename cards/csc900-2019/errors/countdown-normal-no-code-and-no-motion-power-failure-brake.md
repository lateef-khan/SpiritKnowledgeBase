---
id: csc900-2019-errors-countdown-normal-no-code-and-no-motion-power-failure-brake
title: A normal countdown with no motion and no fault code is the power failure brake
  or its supply cable
kind: troubleshooting
question: Why does a Spirit csc900-2019 stair climber count down and then not run,
  with no error code shown?
asked_as:
- climbmill counts down but nothing moves and no error
- csc900 brake wont release
- stair climber steps locked after start
keywords:
- power failure brake
- power-off brake
- countdown
- no code
- brake cable
- steps do not move
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
  code: no-code
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2024-errors-brake-does-not-turn-on
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-power-off-brake-24-volt-snap-test
- csc900-2024-errors-brake-does-not-turn-on
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 9, PDF p. 9; text.md
    lines 346-352
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **The absence of a code is the diagnosis.** A normal countdown followed by no motion *with* a code is ER11 or ER12; the same thing with a blank code field is this row.

**Issue:** After pressing Start, the countdown is normal, the machine does not run, and the console does not display the fault code.

| Analysis | Method |
|---|---|
| The power failure brake is not working. Bad reasons: 1. The power supply line of the power failure brake is bad. 2. The power failure brake is bad. | 1. Check if the power failure brake connection cable is normal. 2. Replace the power failure brake. |

**A power failure brake is a brake held *open* by power.** When the supply drops it clamps the steps, which is what makes the machine safe in a power cut - and what locks the steps when its cable or coil fails while everything else is healthy. The console has no way to see it, so it prints nothing.

**The brake can be proved on the bench with 24 V** - it should snap audibly - before it is condemned: `csc900-2019-errors-power-off-brake-24-volt-snap-test`. That test is the same one the 2022 magnetic-system book prints against its own brake row (`csc900-2024-errors-brake-does-not-turn-on`); that book adds a controller-side measurement this one does not.
