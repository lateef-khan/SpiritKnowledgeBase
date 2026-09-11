---
id: xe395ent-2021-errors-e2-tension-motor-does-not-move
title: 'E2: the tension motor does not move when Level Up or Down is pressed, and
  the drive board output is checked at plus and minus 5 VDC'
kind: troubleshooting
question: What does E2 mean on a Spirit xe395ent-2021 elliptical, and how is the tension
  motor diagnosed?
asked_as:
- xe395ent shows e2
- e2 on my spirit ent elliptical
- resistance wont change e2
- tension motor error e2 elliptical
keywords:
- e2
- tension motor
- resistance motor
- level up
- drive board
- 5vdc
- error message
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- spirit-ce850-2016-errors-e2-table-label-tension-motor
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- ce850-2024-errors-err-tension-motor-failure
see_also:
- xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
- e25-2023-e2-gear-motor-failure
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: 'XE395ENT 2021 (XE539S-SE025-01) service manual Error code items, Error
    Message: E2 and Tension Motor Operation / Troubleshooting, PDF p. 26-28, text.md
    lines 308-375'
  extracted_at: '2026-09-11'
---

**This is the XE395ENT 2021's `E2`, its tension motor. It is not `E3`, the incline VR fault that is the only other row on its table, and it is not the CE850 2016's `E2`, which that book prints as a table label and never shows.** There is no `EEPROM ERR` row on this machine.

| Error Message | Explain |
|---|---|
| E2 | Tension motor is failure |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

Definition, as printed: *When you press the Level Up or Down key, the motor does not move. "E2" appears on the display.*

How the parts are meant to work (*Tension Motor Operation*):

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive Board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

How to find the fault (*Tension Motor Troubleshooting*):

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive Board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor, but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered multi-meter test - **brown and black wires, 5 to 6.0 VDC** - is `xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc`. On this book the caption under the photo names the same wires as the step, unlike the 2016 books.

The 2016 residential ellipticals print this section under the message `--` and test on blue and green wires (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`); the CE850 (2020) prints it under `Err`. The XBR55ENT and XBU55ENT 2021 bikes of the same year print `E2` with the same brown-and-black test (`spirit-xb-errors-e2-motor-does-not-move-on-level-key`), and Sole's E25 2023 calls it `E2` too (`e25-2023-e2-gear-motor-failure`). Different product line and different brand; separate cards.
