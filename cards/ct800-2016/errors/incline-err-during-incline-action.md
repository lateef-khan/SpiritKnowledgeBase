---
id: ct800-2016-errors-incline-err-during-incline-action
title: INCLINE ERR raised because the reading does not change while the incline runs,
  checked at the driver board LEDs
kind: troubleshooting
question: What does INCLINE ERR mean when I press the incline keys on a Spirit ct800-2016
  treadmill?
asked_as:
- incline err when i press incline up
- incline does not move and shows an error
- spirit treadmill incline error while running
keywords:
- incline err
- vr value
- up down keys
- up led
- down led
- incline motor
- 12 pin cable
- driver board
- no change
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: errors
  code: incline-err
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-during-incline-action
- ct850-2020-incline-err
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
- ct800-2016-errors-controller-led-debugging-90-to-110-v
- ct850-2016-incline-err-shown-in-incline-window
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: 'CT800 2016 service manual Error Message: INCLINE ERR (second definition),
    Cause of INCLINE show Err, Troubleshooting, PDF p. 48-50 (printed 47-49), text.md
    lines 900-950'
  extracted_at: '2026-09-11'
---

**The CT800 2016 service manual defines `INCLINE ERR` twice, and this is the second definition.** The first, the reading out of range at power on, is on `ct850-2016-incline-err-vr-out-of-range`, which the CT800 2016 prints word for word. This one is the reading not changing while the incline is driven.

Definition: *During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.*

Cause: *Press the incline UP/DOWN key. The incline doesn't operate. INCLINE ERR appears on the display. Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which changes the VR value. The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it should be. INCLINE E2 appears on the display.*

That last sentence says `INCLINE E2`; nothing else in the book uses E2 and the heading says INCLINE ERR.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP LED lights. 2. Press incline DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 12-pin cable | 1. Inspect whether the 12-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If ERR still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

**The CT850 2016 prints this definition against an inverter, not a driver board** - its table has three rows, Inverter, 12-pin cable and Incline motor, and no LED steps (`ct850-2016-incline-err-during-incline-action`). The CT800 2016 has a DC controller with `INC_UP` and `INC_DW` LEDs on it (`ct800-2016-errors-controller-led-debugging-90-to-110-v`), and the table watches those. The CT850 2020's `INCLINE ERR` table is this one with *RELAY action* in place of *LED lights* (`ct850-2020-incline-err`).
