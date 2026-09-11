---
id: spirit-xb-2016-errors-dashes-tension-motor-failure
title: 'Two dashes on the display: the tension motor does not move when Level Up or
  Down is pressed'
kind: troubleshooting
question: What do the two dashes "--" mean on a Spirit XBR25-2016, XBR55-2016 or XBU55-2016
  residential bike, and how is the tension motor diagnosed?
asked_as:
- my spirit bike shows two dashes instead of a level
- resistance wont change and the display shows --
- dashes on the spirit xbr55 console
- tension motor failure on a 2016 spirit bike
keywords:
- dashes
- --
- tension motor
- gear motor
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
  - xbr25-2016
  - xbr55-2016
  - xbu55-2016
  section: errors
  code: dashes
authority: 3
not_to_be_confused_with:
- spirit-bike-errors-eeprom-err-replace-upper-controller
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
see_also:
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
- spirit-bike-errors-eeprom-err-replace-upper-controller
- xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
- sole-bike-tension-motor-error
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: 'XBR25 2016 service manual Error code items (-- = Tension motor is failure),
    Error Message: - -, Tension Motor Operation / Troubleshooting, PDF p. 33-36, text.md
    lines 465-539; XBR55 2016 service manual Error code items (-- = Tension motor
    is failure), Error Message: - -, Tension Motor Operation / Troubleshooting, PDF
    p. 35-38, text.md lines 487-561; XBU55 2016 service manual Error code items (--
    = Tension motor is failure), Error Message: - -, Tension Motor Operation / Troubleshooting,
    PDF p. 33-36, text.md lines 466-540'
  extracted_at: '2026-09-11'
---

**This is the `--` tension motor fault of the 2016 residential books. It is not `EEPROM ERR`, the other row on the same table, and it is not the `E2` the 2023 and ENT books print for the same motor.**

| Error Message | Explain |
|---|---|
| -- | Tension motor is failure |

Definition, as printed: *When you press the Level Up or Down key, the motor does not move. "--" appears on the display.* The configuration drawing on the same page shows the level keys feeding the display board, the display board sending a level signal to the tension motor, and the motor's VR (position) signal returning to the display board.

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

The numbered multi-meter test - **blue and green wires, 5.5 to 6.0 VDC** - is `spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires`.

**Three service manuals print this section in the same words**: the XBR25 2016, XBR55 2016 and XBU55 2016. The XBR95 2016 of the same generation has no tension motor and no such row; its resistance table is `xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`.

The 2023 and ENT residential books give the same motor fault the code `E2`, test on brown and black wires and expect 5 to 6.0 VDC: `spirit-xb-errors-e2-motor-does-not-move-on-level-key`. The Sole B94 and R92 of 2016-2019 call the same fault `E2` too - `sole-bike-tension-motor-error` - a different brand and a separate card.
