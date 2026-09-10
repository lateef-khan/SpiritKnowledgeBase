---
id: ct850-2020-incline-err
title: 'INCLINE ERR: the incline reading does not change while the incline runs'
kind: troubleshooting
question: What does INCLINE ERR mean on a Spirit CT850-2020 treadmill?
asked_as:
- incline err on my spirit treadmill
- treadmill display says incline error
- incline does not move and shows an error
keywords:
- incline err
- vr value
- up down keys
- relay
- incline motor
- console cable
- driver board
- recalibrate
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: errors
  code: incline-err
  model_number:
  - '850840'
authority: 3
not_to_be_confused_with:
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-e-52h-incline-motor-fails-during-calibration
- ct900-e33-incline-err
see_also:
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2016-incline-err-during-incline-action
- ct850-2020-inverter-error-code-list
- ct850-2020-incline-motor-replacement
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: 'Section 8-4 Error Message: INCLINE ERR, pages 42-44 (printed 41-43). Pages
    42 and 43 are flattened images and were read from raw/page-42.png and raw/page-43.png'
  extracted_at: '2026-09-08'
---

**This is the message INCLINE ERR, not the code E3 and not E-52H.** `INCLINE ERR` is not in the
error code table at 8-1 at all; it only has this section.

Definition:

> During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Cause:

> Press the incline UP/DOWN key. The incline doesn't operate. INCLINE ERR appears on the display.
> Incline motor isn't operation up or down, making the VR value exceed the range.
> Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline
> operates, moving the VR, which changes the VR value.
> The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the
> incline is not operating when it should be. INCLINE Err appears on the display.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP RELAY action. 2. Press incline DOWN key. The driver board DOWN RELAY action. 3. If not as above, inspect the cable and connections. |
| Console cable | 1. Inspect whether the console cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN REALY is action. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If ERR still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

**The action flow chart's end box does not say what the rest of the page says.** Re-rendered at 600
dpi, the box reads `SHOW INCLINE E33 MESSAGE`, and `E33` is set in a visibly different font from the
rest of the box, as though pasted in from another manual. `E33` appears **nowhere else in this
manual** - not in the 8-1 error code table, not on this page, not anywhere - while the section
heading and every other line here print `INCLINE ERR`. The message a technician will see on the
display is `INCLINE ERR`. Spirit's CT900 does use `E33` for its incline error, on a different
controller, which is the likeliest origin of the pasted box.

The code `E3`, which the 8-1 table does list, is the *reading out of range* rather than the reading
not changing: `ct850-2020-e3-incline-motor-cannot-work`. The CT850 2016 manual prints **both**
definitions under the single name `INCLINE ERR`.

The last part in the troubleshooting table is the incline motor, checked for a seizure, cracked
gears and a broken circuit; its replacement procedure is on
`ct850-2020-incline-motor-replacement`.
