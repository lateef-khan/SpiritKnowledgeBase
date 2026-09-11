---
id: spirit-xs895-errors-incline-position-does-not-match-the-console-calibrate
title: The incline position does not match what the console shows, and the one cause
  printed is a console that has not been calibrated
kind: troubleshooting
question: Why does the incline on a Spirit XS895 stepper not match the level the console
  shows?
asked_as:
- xs895 incline reads wrong
- stepper incline number doesnt match the actual angle
- my spirit incline stepper needs calibrating
keywords:
- incline position
- does not match
- calibrate
- calibration
- console
- incline level
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
see_also:
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
- spirit-xs895-errors-incline-buttons-do-not-work-cable-connectors-and-the-switch
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-8 Troubleshooting procedure matrix, "The incline position doesn't match
    console" row, PDF p. 36 (printed 35); text.md lines 557-558
  extracted_at: '2026-09-11'
---

| Condition | Reason | Solve |
|---|---|---|
| The incline position doesn't match console | 1. Console is not calibrated. | 1. Calibrate the console. |

**One cause and one remedy, and the remedy is a console procedure.** The console learns the incline motor's travel by running it end to end and reading the potentiometer at each end; a console that has never done that - or did it before a motor or a board was changed - shows a level that is not where the steps are. The calibration routine itself lives in the engineering menu and is carded under `section: console`.

**No code, and that is what separates it from `E3`.** The same potentiometer reading missing or out of range puts `STEP ERROR` on the display and is the code row (`spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr`), whose first response is also a power cycle and a calibration. A mismatch *with* a reading is this row.

The incline motor's own length is set at replacement - 245 mm between the bolt holes with the motor at zero, on the same book's incline motor page - and a motor fitted at the wrong length will not calibrate to the console's range.
