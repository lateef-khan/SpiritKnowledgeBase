---
id: cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
title: E2 on the 2016 stepper means the tension motor did not move when the level
  key was pressed, and the drive is 5 volts either way through a 10-pin cable
kind: troubleshooting
question: What does E2 mean on a Spirit cs800-2016 stepper?
asked_as:
- my stepper says e2 when i change the level
- cs800 e2 tension motor
- what does e2 mean on a spirit stepper
keywords:
- e2
- tension motor failure
- level up
- level down
- 5vdc
- 10-pin cable
- drive board
- stepper
- error code
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: errors
  code: e2
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- cs800-2016-errors-e1-eeprom-failure-replace-the-upper-controller
- cvc800-e-2-tension-motor-error
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
- crw800-2024-errors-e2-cable-tension-communication-error
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
see_also:
- cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- sc200-2016-e2-tension-motor-failure
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 8. Error Messages / Troubleshooting, Error code items table, PDF p. 32,
    text.md lines 454-459; 8-2 Error Message E2 with the Tension Motor Operation and
    Troubleshooting tables, the Part / Troubleshooting table and the connector pin
    list, PDF p. 34-38, text.md lines 484-568
  extracted_at: '2026-09-11'
---

**This is the CS800 of the 2016 `XS200-SS003` book.** The 2020-book and 2024 CS800 print this fault as `Err` in the LEVEL window (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`); this machine prints `E2`.

| Error Message | Explain |
|---|---|
| E2 | Tension motor is failure |

**8-2 Error Message: E2.** Definition: When you press the Level Up or Down key, the motor does not move. "E2" appears on the display. The configuration drawing: the display board takes the LEVEL UP/DOWN keys, sends a *level up/down signal* to the tension motor and receives a *level count signal* back.

**Tension Motor Operation**

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Tension Motor | Tension Motor receives the signal and responds by putting out power to the motor. Level UP: **+5VDC**; Level DOWN: **-5VDC** |

**Tension Motor Troubleshooting**

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Tension Motor | Inspect Display board output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor, but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

| Part | Troubleshooting |
|---|---|
| Display board | Inspect the 10-pin cable connections. |
| 10-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension Motor | Inspect the display board 10-pin connections. |

**The cable is ten pins on this machine, and the book prints its map:** 1 VCC +5V, 2 GND, 3 UP, 4 SIGNAL, 5 DOWN, 6 SPEED SENSOR, 7 SPEED GND, 8 VCC +12V, 9 NA, 10 GND. The 2020-book CS800 and the CRS800S use a 14-pin and a 9-pin cable respectively; do not read their pin numbers here.

**Two voltages for the same drive.** These tables say 5 V; the voltage test procedure on the next page says 4.0 to 6.0 V and adds a drive-board LED to look at (`cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led`). Measure against the band.

Sole prints this page for the SC200 2016: `sc200-2016-e2-tension-motor-failure`.
