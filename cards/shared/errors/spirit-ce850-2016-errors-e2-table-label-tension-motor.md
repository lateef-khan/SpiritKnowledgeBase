---
id: spirit-ce850-2016-errors-e2-table-label-tension-motor
title: E2 is printed in the error table as the tension motor failure, but the chapter
  shows the fault as two dashes and heads its E2 section with the stride VR fault
kind: troubleshooting
question: What does E2 mean on a Spirit CE850-2016 or XE895-2016 elliptical?
asked_as:
- e2 on my spirit ce850
- what is error 2 on the elliptical
- elliptical manual says e2 tension motor
- e2 versus dashes on a spirit elliptical
keywords:
- e2
- tension motor
- error table
- dashes
- e3
- ramp error
- misprint
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe895-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- e25-2016-e2-tension-motor-failure
see_also:
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- ce850-2024-errors-err-tension-motor-failure
- e95s-2016-e3-stride-error
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850 2016 (XE898-SE011) service manual Error code items, Error Message:
    -- and 8-2 Error Message: E2, PDF p. 39-44, text.md lines 647-739; XE895 2016
    (XE895-SE022) service manual Error code items, Error Message: -- and 8-2 Error
    Message: E2, PDF p. 40-45, text.md lines 648-735'
  extracted_at: '2026-09-11'
---

**This is E2 as the CE850 2016 and XE895 2016 books print it, and the books never agree with themselves about it. It is not E1 (EEPROM) and not E3 (stride VR).**

The error table:

| Error Message | Explain |
|---|---|
| E1 | EEPROM failure |
| E2 | Tension motor is failure |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

Three things then go wrong in the same chapter.

1. **The tension-motor section is headed `Error Message: --`**, and its definition says *"--" appears on the display* - not `E2`. That section, with its operation and troubleshooting tables and the voltage test, is `spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`.
2. **The section headed `8-2 Error Message: E2` is about the stride VR**, not the tension motor: its definition is the E3 line of the table, word for word, and ends *"E3" appears on the display*; the page after it is headed `Case of RAMP ERROR` and says `E3` throughout. That fault is `spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`.
3. **No page in either book shows an `E2` on the display.**

So a caller who reads `E2` on the screen has a tension-motor fault by the table, and the tests to run are the `--` section's; a caller whose *manual* says `8-2 Error Message: E2` is reading the stride chapter. The same table with the same three rows, and the same `RAMP ERROR` heading on the stride pages, is in Sole's E95S 2016 book (`e95s-2016-e3-stride-error`) - the Dyaco template these books were built from. The later CE850 (2020) resolves it by renaming the rows `EEPROM ERROR`, `ERR` and `---` (`ce850-2024-errors-err-tension-motor-failure`).
