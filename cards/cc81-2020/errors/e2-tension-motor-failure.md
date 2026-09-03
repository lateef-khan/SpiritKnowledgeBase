---
id: cc81-2020-e2-tension-motor-failure
title: "Tension motor failure error on the climber console"
kind: troubleshooting
question: "What does E2 mean on a Sole CC81-2020 climber, and how do I fix it?"
asked_as:
- "my sole climber shows e2"
- "resistance wont change on my climber and it shows an error"
- "e2 error on the cc81"
keywords:
- "e2"
- "tension motor"
- "resistance"
- "control cable"
- "error code"
- "level up"
- "level down"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2020
  applies_to:
  - cc81-2020
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- cc81-2020-e1-eeprom-failure
- sole-bike-tension-motor-error
- sole-e2-error
see_also:
- cc81-2020-tension-motor-console-output-check
- cc81-2020-tension-motor-voltage-test
- cc81-2020-tension-motor-spec
- cc81-2020-no-resistance-or-flywheel-noise
source:
  ref: sole-climber-cc81-2020-service-manual
  locator: "Sections 7-1 Error Codes and 7-4 Error Message: E2"
  extracted_at: '2026-09-03'
---

**This is the climber E2, not the climber E1 (EEPROM), and not the treadmill E2 or the bike E2.**

| Field | Value |
|---|---|
| Code | E2 |
| Cause, as printed | Tension motor is failure |
| Definition | The tension motor operates abnormal, or the console can't receive the signal from tension motor. |

**Fix, in the manual's order**

1. Check the control cable and re-plug it.
2. Check the tension motor.

Step 2 is worked through in two more places: check what the console puts out (card `cc81-2020-tension-motor-console-output-check`), then measure it at the drive board (card `cc81-2020-tension-motor-voltage-test`).
