---
id: spirit-xb-errors-e2-motor-does-not-move-on-level-key
title: 'E2: the resistance motor does not move when Level Up or Down is pressed'
kind: troubleshooting
question: What does E2 mean on a Spirit XBR55-2023, XBU55-2023, XBR55ENT-2021 or XBU55ENT-2021
  residential bike, and how is it diagnosed?
asked_as:
- e2 on my spirit bike
- resistance wont change and the bike shows e2
- level up does nothing on my xbu55
- spirit recumbent e2 error
keywords:
- e2
- gear motor
- tension motor
- resistance
- level up
- level down
- drive board
- residential bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbr55ent-2021
  - xbu55-2023
  - xbu55ent-2021
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- spirit-xb-2023-errors-eeprom-err-replace-display-board
- spirit-xb-2016-errors-dashes-tension-motor-failure
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
see_also:
- spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires
- spirit-xb-2023-errors-eeprom-err-replace-display-board
- b94-2023-e2-gear-motor-failure
- sole-bike-tension-motor-error
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55 2023 service manual 8. Error Code List (E2 = Gear Motor is defective)
    and 8.2 Error Message: E2, PDF p. 13-14, text.md lines 242-294; XBU55 2023 service
    manual 8. Error Code List and 8.2 Error Message: E2, PDF p. 13-14, text.md lines
    225-293; XBR55ENT 2021 service manual Error code items (E2 = Tension motor is
    failure), Error Message: E2 and Tension Motor Operation / Troubleshooting, PDF
    p. 23-26, text.md lines 246-316; XBU55ENT 2021 service manual Error code items
    (E2 = Tension motor is failure), Error Message: E2 and Tension Motor Operation
    / Troubleshooting, PDF p. 23-26, text.md lines 243-313'
  extracted_at: '2026-09-11'
---

**This is the bike E2, the resistance motor. It is not the EEPROM message on the same tables (`EEPROM ERR`, listed as `E1` on two of them), and it is not a Spirit treadmill E2, which is an over-current fault with a different fix.**

Definition, as printed: *When you press the Level Up or Down key, the motor does not move. "E2" appears on the display.* The 2023 code tables call the cause `Gear Motor is defective`; the two ENT books call the same part the tension motor - `Tension motor is failure`. Same motor, same steps.

How the parts are meant to work:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive Board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

How to find the fault:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive Board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered multi-meter test that confirms it - **red probe on the brown wire, black on the black wire, +5 to 6.0 VDC** - is `spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires`. A multi-meter is the only tool the four books ask for.

**Four service manuals print this section in the same words**: the XBR55 2023 and XBU55 2023 (as section 8.2) and the XBR55ENT 2021 and XBU55ENT 2021 (as `Error Message: E2`). On the two ENT books it is the **only** message in the error table - they print no `EEPROM ERR` at all - and their code table calls the cause `Tension motor is failure`, the wording the 2016 residential books use for their `--` row. The XBR95 2023 and XBR95 2016 have no E2 because they have no motor: a generator brake sets their resistance.

**The 2016 residential books print the same motor fault under a different label.** The XBR25 2016, XBR55 2016 and XBU55 2016 show `--` on the display, test on blue and green wires and expect 5.5 to 6.0 VDC: `spirit-xb-2016-errors-dashes-tension-motor-failure`. Do not quote those wire colours here.

Sole's 2023 bikes print this section word for word under the same code - `b94-2023-e2-gear-motor-failure` - and its 2016-2019 bikes as `sole-bike-tension-motor-error`. Both are Sole machines and separate cards.
