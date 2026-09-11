---
id: spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
title: 'Two dashes on the display: the tension motor does not move when Level Up or
  Down is pressed, and the drive board output is checked at plus and minus 5 VDC'
kind: troubleshooting
question: What do the two dashes "--" mean on a Spirit CE850-2016, XE895-2016, XE195-2016,
  XE295-2016, XE395-2016 or XG400-2016 elliptical, and how is the tension motor diagnosed?
asked_as:
- my spirit elliptical shows two dashes
- resistance wont change and the display shows --
- elliptical level shows dashes
- tension motor error on a spirit xe elliptical
keywords:
- dashes
- --
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
  model: '*'
  applies_to:
  - ce850-2016
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe895-2016
  - xg400-2016
  section: errors
  code: dashes
authority: 3
not_to_be_confused_with:
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
- spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- ce850-2024-errors-err-tension-motor-failure
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
see_also:
- spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- spirit-ce850-2016-errors-e2-table-label-tension-motor
- spirit-xb-2016-errors-dashes-tension-motor-failure
- e25-2016-e2-tension-motor-failure
- xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: 'CE850 2016 (XE898-SE011) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 41-42, text.md lines
    680-720; XE895 2016 (XE895-SE022) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 42-43, text.md lines
    680-723; XE195 2016 (XE509S-SE021-01) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 36-37, text.md lines
    537-581; XE295 2016 (XE519S-SE020-01) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 36-37, text.md lines
    541-585; XE395 2016 (XE539S-SE019-01) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 42-43, text.md lines
    673-716; XG400 2016 (SE551-SE023-01) service manual Error code items, Error Message:
    -- and Tension Motor Operation / Troubleshooting, PDF p. 34-35, text.md lines
    478-522'
  extracted_at: '2026-09-11'
---

**This is the `--` tension motor fault of the 2016 elliptical books. It is not `EEPROM ERR` / `E1`, the first row on the same table, and it is not the `Err` or `E3` stride and incline faults some of the same books print.** The CE850 (2020) prints the same fault as `Err` and the XE395ENT 2021 as `E2`.

| Error Message | Explain |
|---|---|
| -- | Tension motor is failure |

Definition, as printed: *When you press the Level Up or Down key, the motor does not move. "--" appears on the display.* The configuration drawing on the same page shows the level keys feeding the display board, the display board sending a level signal to the tension motor, and the motor's VR (position) signal returning to the display board.

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

The numbered multi-meter test follows on the next page, and the figure it expects differs between the books: **blue and green wires and 5 to 6.0 VDC** on the CE850 2016 and XE895 2016 (`spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc`), **blue and green wires and 5.5 to 6.0 VDC** on the XE195, XE295, XE395 and XG400 2016 (`spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`).

**Six service manuals print this section in the same words.** The XE195 2016, XE295 2016, XE395 2016 and XG400 2016 list the row as `--` in their error tables. **The CE850 2016 and XE895 2016 list the same row as `E2 | Tension motor is failure`** and then head the section `Error Message: --` - the chapter never shows an `E2` on the display, and its `8-2 Error Message: E2` heading two pages on describes the stride VR fault whose message is `E3` (`spirit-ce850-2016-errors-e2-table-label-tension-motor`). The XE795 2016 and CE900 of the same generation have no tension motor and no such row; the XE795 2016 watches a driver-board output instead (`xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`).

**The XG400 2016 also prints a second, unrelated page about the same motor** - `Troubleshooting for Motor Error`, where the message is `Err` and the causes run from a chipped gear to weak batteries: `xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback`.

The Spirit residential bikes of 2016 print this page word for word about their own tension motor (`spirit-xb-2016-errors-dashes-tension-motor-failure`), and Sole calls the same fault `E2` on its E25, E35, E55 and E95S 2016 ellipticals (`e25-2016-e2-tension-motor-failure`). Different product line and different brand; separate cards.
