---
id: csc900-2024-errors-speed-abnormal-then-data-resets
title: The speed reads wrong and the data resets three seconds after stopping, and the light sensor is the cause
kind: troubleshooting
question: Why does a Spirit CSC900-2024 stairclimber show an abnormal speed and then
  reset the display?
asked_as:
- my stairclimber speed reading is wrong
- csc900 display resets a few seconds after i stop
- speed jumps around on my spirit stair climber
keywords:
- light sensor
- speed abnormal
- data reset
- grating
- sensor distance
- optical sensor
- stairclimber
- no code
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-rpm-shows-zero
see_also:
- csc900-2024-errors-error-code-table
- ces880-2025-errors-rpm-shows-zero
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING, Problem / Reason / Method table on printed page 34. That
    page is a flat picture with no text layer and was read from the rendered page at 500
    dpi.
  extracted_at: '2026-09-10'
---

**Condition:** Press "START" to start, the machine speed is abnormal, 3 seconds after the stop,
display data reset.

| Reason | Method |
|---|---|
| Light sensor failure | 1. Check whether the light sensor line is off or damaged. 2. Check whether the distance between the light sensor and the grating can be sensed. 3. Replace the light sensor. |

**This machine reads its speed optically**, from a light sensor and a slotted grating, rather than
from a magnet and a reed or hall sensor as Spirit's treadmills and bikes do. The second check is a
**gap** check - whether the sensor can see the grating at its present distance - and the manual
gives no figure for it.

**No code is printed for this fault.** It is a symptom row, and the console shows nothing but the
wrong number.

The five codes this machine does print are on `csc900-2024-errors-error-code-table`.
