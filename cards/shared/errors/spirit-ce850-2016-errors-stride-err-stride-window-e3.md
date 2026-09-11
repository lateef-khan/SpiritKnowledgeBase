---
id: spirit-ce850-2016-errors-stride-err-stride-window-e3
title: STRIDE ERR with E3 in the stride window comes from a wrong position sensor
  value, and the fix is a power cycle then a calibration
kind: troubleshooting
question: What do I do when a Spirit CE850-2016 or XE895-2016 elliptical shows STRIDE
  ERR?
asked_as:
- elliptical says stride err
- stride window shows e3
- stride length wont change on my spirit elliptical
- stride error on the console
keywords:
- stride err
- e3
- stride motor
- position sensor
- calibrate
- power cycle
- ac switch
- stride length
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
  code: stride-err
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-stride-err-position-sensor-wrong
- xe395-2016-errors-incline-err-incline-window-err
- xe395ent-2021-errors-incline-err-incline-window-e3
- ct850-2016-incline-err-shown-in-incline-window
see_also:
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- ce850-2024-errors-stride-err-position-sensor-wrong
- ce850-2024-errors-stride-adjustment-buttons-not-working
- e95s-2016-stride-position-mismatch
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual 8-7 Troubleshooting procedure matrix,
    the stride rows; 8.5 CALIBRATION PROCEDURE, PDF p. 54, PDF p. 56, text.md lines
    973-1012; XE895 2016 (XE895-SE022) service manual 8-7 Troubleshooting procedure
    matrix, the stride rows; CALIBRATION PROCEDURE, PDF p. 55, PDF p. 57, text.md
    lines 973-1012
  extracted_at: '2026-09-11'
---

**This is the matrix's `STRIDE ERR`, and on these two books the stride window shows `E3` - not the three dashes the CE850 (2020) and CE850 2024 print for the same row.**

The manual prints two conditions together, and answers them separately.

| Condition | Reason | Solve |
|---|---|---|
| The stride position doesn't match console | Console is not calibrated | Calibrate the console |
| STRIDE ERR, STRIDE window displays "E3" | Position sensor value of stride motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

**Only the second row is an error.** The first is a number that reads wrong; the second is the machine refusing to show a number at all.

**The power cycle comes before the calibration.** The stride calibration on these books is a five-second hold on the **Stride key and the Start key** together; it starts and runs automatically, and the book says to contact the service department if the problem persists.

**The other half of this fact is the E3 chapter earlier in the book**, which names the parts and prints the nine-step test: `spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read` and `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`. Nothing in the book connects the two.

The CE850 (2020) and CE850 2024 print this pair with `---` in the window (`ce850-2024-errors-stride-err-position-sensor-wrong`); the XE395 2016 prints it about its incline with `Err` (`xe395-2016-errors-incline-err-incline-window-err`) and the XE395ENT 2021 with `E3` (`xe395ent-2021-errors-incline-err-incline-window-e3`). Sole's E95S 2016 prints the same stride rows (`e95s-2016-stride-position-mismatch`). Different machines; separate cards.
