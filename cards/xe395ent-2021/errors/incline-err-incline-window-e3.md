---
id: xe395ent-2021-errors-incline-err-incline-window-e3
title: INCLINE ERR with E3 in the incline window comes from a wrong position sensor
  value, and the fix is a power cycle then a calibration
kind: troubleshooting
question: What do I do when a Spirit xe395ent-2021 elliptical shows INCLINE ERR?
asked_as:
- xe395ent says incline err
- incline window shows e3
- incline wont change on my ent elliptical
- incline error on the touch console
keywords:
- incline err
- e3
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
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- xe395-2016-errors-incline-err-incline-window-err
- spirit-ce850-2016-errors-stride-err-stride-window-e3
- ct850-2016-incline-err-shown-in-incline-window
see_also:
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
- spirit-xe395-errors-incline-adjustment-buttons-not-working
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: XE395ENT 2021 (XE539S-SE025-01) service manual Troubleshooting procedure
    matrix, the incline rows; 4. Factory Setting, Incline Calibration, PDF p. 44,
    PDF p. 46, text.md lines 656-694
  extracted_at: '2026-09-11'
---

**This is the matrix's `INCLINE ERR`, and on this book the incline window shows `E3` - not the `Err` the XE395 2016 prints for the same row, and not a treadmill's INCLINE ERR.**

The manual prints two conditions together, and answers them separately.

| Condition | Reason | Solve |
|---|---|---|
| The incline position doesn't match console | Console is not calibrated | Calibrate the console |
| INCLINE ERR, INCLINE window displays "E3" | Position sensor value of incline motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

**Only the second row is an error.** The first is a number that reads wrong; the second is the machine refusing to show a number at all.

**The power cycle comes before the calibration.** On this touch console the calibration is the `Incline Calibration` entry of the engineer mode's Factory Setting page: press `start`, and the incline motor runs up until it stops for 3 to 6 seconds, then down until it stops for 3 to 6 seconds, and the calibration finishes. The engineer mode is reached by tapping `Settings` ten times on the Settings page.

**The other half of this fact is the E3 chapter earlier in the book**, which names the parts and prints the nine-step test: `xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read` and `xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`.

The XE395 2016 prints this pair with `Err` in the window (`xe395-2016-errors-incline-err-incline-window-err`); the stride machines print it as `STRIDE ERR` (`spirit-ce850-2016-errors-stride-err-stride-window-e3`); Spirit treadmills print the same pair about their own incline (`ct850-2016-incline-err-shown-in-incline-window`). Different machines; separate cards.
