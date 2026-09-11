---
id: xe395-2016-errors-incline-err-incline-window-err
title: INCLINE ERR with Err in the incline window comes from a wrong position sensor
  value, and the fix is a power cycle then a calibration
kind: troubleshooting
question: What do I do when a Spirit xe395-2016 elliptical shows INCLINE ERR?
asked_as:
- xe395 says incline err
- incline window shows err
- incline wont change on my spirit elliptical
- incline error on the console
keywords:
- incline err
- err
- incline motor
- position sensor
- calibrate
- power cycle
- ac switch
- incline
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395-2016
  applies_to:
  - xe395-2016
  section: errors
  code: incline-err
  model_number:
  - '395015'
authority: 3
not_to_be_confused_with:
- xe395ent-2021-errors-incline-err-incline-window-e3
- spirit-ce850-2016-errors-stride-err-stride-window-e3
- ct850-2016-incline-err-shown-in-incline-window
see_also:
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395-2018-errors-incline-calibration-three-key-hold
- spirit-xe395-errors-incline-adjustment-buttons-not-working
- e25-2016-incline-position-mismatch
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: XE395 2016 (XE539S-SE019-01) service manual Troubleshooting procedure matrix,
    the incline rows; CALIBRATION PROCEDURE, PDF p. 55, PDF p. 57, text.md lines 966-1008
  extracted_at: '2026-09-11'
---

**This is the matrix's `INCLINE ERR`, and on this book the incline window shows `Err` - not the `E3` the XE395ENT 2021 prints for the same row, and not a treadmill's INCLINE ERR.**

The manual prints two conditions together, and answers them separately.

| Condition | Reason | Solve |
|---|---|---|
| The incline position doesn't match console | Console is not calibrated | Calibrate the console |
| INCLINE ERR, INCLINE window displays "Err" | Position sensor value of incline motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

**Only the second row is an error.** The first is a number that reads wrong; the second is the machine refusing to show a number at all.

**The power cycle comes before the calibration.** The incline calibration on this book is a five-second hold on the **Stop key, Level key and Start key** together; it starts and runs automatically, and the book says to contact the service department if the problem persists (`xe395-2018-errors-incline-calibration-three-key-hold`).

**The other half of this fact is the Err chapter earlier in the book**, which names the parts and prints the nine-step test: `xe395-2016-errors-err-incline-vr-out-of-range-or-not-read` and `xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`.

The XE395ENT 2021 prints this pair with `E3` in the window (`xe395ent-2021-errors-incline-err-incline-window-e3`); the stride machines print it as `STRIDE ERR` (`spirit-ce850-2016-errors-stride-err-stride-window-e3`, `ce850-2024-errors-stride-err-position-sensor-wrong`); Spirit treadmills print the same pair about their own incline (`ct850-2016-incline-err-shown-in-incline-window`), and Sole's E25 family prints it too (`e25-2016-incline-position-mismatch`). Different machines; separate cards.
