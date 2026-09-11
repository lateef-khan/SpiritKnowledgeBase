---
id: ce850-2024-errors-stride-err-position-sensor-wrong
title: STRIDE ERR and a stride window full of dashes come from a wrong position sensor
  value
kind: troubleshooting
question: What do I do when a Spirit CE850-2020 or CE850-2024 elliptical shows STRIDE
  ERR?
asked_as:
- elliptical says stride err
- stride length wont change on my spirit elliptical
- stride error on the console
keywords:
- stride err
- stride motor
- position sensor
- calibrate
- power cycle
- ac switch
- elliptical
- stride length
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2020
  - ce850-2024
  section: errors
  code: stride-err
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- ct850-2016-incline-err-shown-in-incline-window
- spirit-ce850-2016-errors-stride-err-stride-window-e3
see_also:
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- ce850-2024-errors-stride-adjustment-buttons-not-working
- ct850-2016-incline-err-shown-in-incline-window
- spirit-ce850-2016-errors-stride-err-stride-window-e3
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
source:
  ref: spirit-elliptical-ce850-2024-owners-manual
  locator: TROUBLESHOOTING, Condition / Reason / Solve matrix on printed page 38.
    That page is a flat picture with no text layer and was read from the rendered
    page; CE850 (2020) service manual 8-7 Troubleshooting procedure matrix, the stride
    rows, PDF p. 49, text.md lines 852-890
  extracted_at: '2026-09-10'
---

The manual prints two conditions together, and answers them separately.

| Condition | Reason | Solve |
|---|---|---|
| The stride position doesn't match console | Console is not calibrated | Calibrate the console |
| STRIDE ERR, STRIDE window displays `---` | Position sensor value of stride motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

**Only the second row is an error.** The first is a number that reads wrong; the second is the
machine refusing to show a number at all.

**The power cycle comes before the calibration**, and the manual gives no third step - it names no
part to replace and no measurement to take when both fail.

**The other half of this fact is in the error message table on the next page**, which names the
failed part: `--- | Stride motor is failure`
(`ce850-2024-errors-stride-window-dashes-stride-motor-failure`). Nothing in the manual connects the
two pages, so a reader who finds one half does not learn the other exists.

**This is the elliptical's stride equivalent of the treadmills' incline rows.** The CT850 and 2024
ENT treadmills print the same pair of rows about incline
(`ct850-2016-incline-position-does-not-match-console`,
`ct850-2016-incline-err-shown-in-incline-window`), with the same reason and the same two-step
remedy. Different axis, different machine; do not carry an incline part number here.

**The CE850 (2020) service manual prints both rows word for word** - the same `- - -`, the same wrong-position-sensor reason and the same power cycle then calibration - and, unlike the owner's manual, goes on to print the full `- - -` chapter and the nine-step motor test (`ce850-2024-errors-stride-window-dashes-stride-motor-failure`, `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`). Its stride calibration is a five-second hold on the STRIDE up key and START. The CE850 2016 prints the same pair of rows with `E3` in the window (`spirit-ce850-2016-errors-stride-err-stride-window-e3`).
