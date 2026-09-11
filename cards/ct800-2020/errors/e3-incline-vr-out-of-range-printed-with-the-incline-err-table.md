---
id: ct800-2020-errors-e3-incline-vr-out-of-range-printed-with-the-incline-err-table
title: 'E3: the incline VR voltage out of range, in a section that prints the INCLINE
  ERR relay checks under it'
kind: troubleshooting
question: What does section 8-3 say E3 means on a Spirit ct800-2020 treadmill, and
  why is its check table the INCLINE ERR one?
asked_as:
- what does e3 mean on my spirit treadmill
- treadmill showing e3 incline
- e3 relay check on the driver board
keywords:
- e3
- incline
- vr voltage
- out of range
- relay
- up relay
- down relay
- console cable
- driver board
- incline motor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2020
  applies_to:
  - ct800-2020
  section: errors
  code: e3
  model_number:
  - '800840'
authority: 3
not_to_be_confused_with:
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-incline-err
- spirit-2024-errors-e3-incline-motor-wires-then-calibration
see_also:
- spirit-2024-errors-e3-incline-motor-wires-then-calibration
- ct850-2020-incline-err
- ct850-2016-incline-err-shown-in-incline-window
source:
  ref: spirit-treadmill-ct800-2020-service-manual
  locator: 'CT800 2020 service manual 8-3 Error Message: E3; pages 38 and 39 are pictures
    read from the render, PDF p. 37-40 (printed 36-39), text.md lines 498-556'
  extracted_at: '2026-09-11'
---

**This is the CT800 2020 service manual's E3 section, and its check table is not an E3 table.** The 8-1 row for E3 - *The incline motor can't work normally / 1. Check and plug all the wires of the incline motor to the controller board. 2. Doing the calibration procedure.* - is on `spirit-2024-errors-e3-incline-motor-wires-then-calibration`, which the 2024 owner's manual inherited from this book.

Section 8-3 defines E3 the usual way:

> The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. "E3" appears on the display.

and the cause page, headed *CAUSE OF INCLINE E3*: *Incline VR value exceeds the range. INCLINE E3 appears on the display. Incline motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so INCLINE E3 appears.* The configuration drawing shows the driver board with an `INCLINE DOWN RELAY` and an `INCLINE UP RELAY`, and the action flow chart - a picture read from the render - runs INCLINE VR -> DRIVER BOARD -> DISPLAY BOARD, ending at *display operates normally* or *ERR appears on the display*.

Then, under the heading *INCLINE ERR Troubleshooting*, the section prints the table that belongs to the next section:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP RELAY action. 2. Press incline DOWN key. The driver board DOWN RELAY action. 3. If not as above, inspect the cable and connections. |
| console cable | 1. Inspect whether the console cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN RELAY is action. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If ERR still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

Section 8-4, INCLINE ERR, then prints the same table again with its step numbers running on - 4, 5, 6 / 3, 4 / 3, 4 / 5, 6, 7, 8 - which is a paste that kept counting. The CT850 2020 prints a different E3 table, four rows starting at the incline VR (`ct850-2020-e3-incline-motor-cannot-work`); this book never prints that one. **No VR voltage test is printed anywhere in the CT800 2020 service manual** - the nine-step potentiometer procedure of the CT800 2016 and the XT books is absent.

The INCLINE ERR section that follows is on `ct850-2020-incline-err`, which this book prints word for word, `E33` flow-chart box included.
