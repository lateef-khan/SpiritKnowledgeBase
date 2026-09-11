---
id: ct900-errors-incline-e33-no-vr-change-during-incline-action
title: INCLINE E33 raised because the reading does not change while the incline runs,
  checked at the relays, the console cable and the motor
kind: troubleshooting
question: What does INCLINE E33 mean when I press the incline keys on a Spirit ct900
  treadmill, and what does the service manual say to check?
asked_as:
- e33 when i press incline up on my spirit treadmill
- incline does not move and shows e33
- incline err e33 relay check
keywords:
- e33
- incline err
- incline e33
- vr value
- up down keys
- up relay
- down relay
- console cable
- driver board
- incline motor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e33
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e33-incline-err
- ct900-e3-igbt-over-temp
- ct850-2020-incline-err
- spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter
see_also:
- ct900-e33-incline-err
- ct850-2020-incline-err
- ct900-error-code-table
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: 'CT900 service manual Error Message: INCLINE E33, PDF p. 35-37, text.md
    lines 475-537'
  extracted_at: '2026-09-11'
---

**The CT900 service manual defines E33 twice, and this is the second definition.** The first - the VR reading out of range at power on - is on `ct900-e33-incline-err` under *Service manual remedy*. This one is the reading not *changing* while the incline is driven, under the heading `Error Message: INCLINE E33`.

Definition: *During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.*

Cause of INCLINE ERR: *Press the incline UP/DOWN key. The incline doesn't operate. INCLINE ERR appears on the display.* Explanation: *Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which changes the VR value. The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it should be. INCLINE Err appears on the display.* The heading says E33; the text under it says INCLINE ERR throughout, and the matrix row for this machine prints the message as `INCLINE E33`.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP RELAY action. 2. Press incline DOWN key. The driver board DOWN RELAY action. 3. If not as above, inspect the cable and connections. |
| console cable | 1. Inspect whether the console cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN RELAY is action. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If ERR still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

This is the CT850 2020's `INCLINE ERR` table under the CT900's number (`ct850-2020-incline-err`), which explains why that CT850 book's flow chart ends in a pasted `E33` box. The owner's manual's one-line remedy - replace the incline motor or inverter if the first calibration fails - is on `ct900-e33-incline-err`; the matrix row is carded under maintenance for this machine (`ct900-incline-position-mismatch-e33`).
