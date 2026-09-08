---
id: ct850-2016-incline-err-during-incline-action
title: INCLINE ERR raised because the reading does not change while the incline runs
kind: troubleshooting
question: What does INCLINE ERR mean when I press the incline keys on a Spirit CT850-2016
  treadmill?
asked_as:
- incline err when i press incline up
- incline does not move and shows an error
- spirit treadmill incline error while running
keywords:
- incline err
- vr value
- up down keys
- relay
- incline motor
- 12 pin cable
- inverter
- no change
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-vr-out-of-range
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-test-procedure
- ct850-2020-incline-err
- ct850-2016-error-code-items-list
- ct850-2016-incline-motor-replacement
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Error Message: INCLINE ERR, pages 44-46 (printed 43-45). Page 44 is a
    flattened image and was read from raw/page-44.png'
  extracted_at: '2026-09-08'
---

**This manual defines `INCLINE ERR` twice, with two different meanings, and never says so.** This
card holds the second definition; `ct850-2016-incline-err-vr-out-of-range` holds the first. Read
both before condemning a part.

This one is the reading not *changing*, and it appears **while the incline is being driven**:

> During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Cause, from the facing page:

> Press the incline UP/DOWN key. The incline doesn't operate. INCLINE ERR appears on the display.
> Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline
> operates, moving the VR, which changes the VR value. The display board CPU reads the incline VR
> value. If there is no VR value change, to the CPU, the incline is not operating when it should be.
> INCLINE ERR appears on the display.

| Part | Troubleshooting |
|---|---|
| Inverter | 1. Press incline UP key. If not as above, inspect the cable and connections. 2. Press incline UP or DOWN key again, making the incline motor return to its position. 3. If ERR still appears, re-calibrate the incline set. |
| 12-pin cable | 1. Inspect whether the 12-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

The CT850 2020 manual keeps this definition under the name `INCLINE ERR` and moves the other one to
the code `E3`: see `ct850-2020-incline-err`.

If the motor is stuck, its gears are cracked or its circuit is broken, the replacement procedure is
on `ct850-2016-incline-motor-replacement`.
