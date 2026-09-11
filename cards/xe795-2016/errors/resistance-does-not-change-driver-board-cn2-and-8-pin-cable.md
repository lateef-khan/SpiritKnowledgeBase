---
id: xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
title: 'Resistance does not change on the generator-brake elliptical: the driver board
  CN2 output must rise with UP and fall with DOWN, then swap the 8-pin cable'
kind: troubleshooting
question: Why does the resistance not change on a Spirit xe795-2016 elliptical, and
  what does the service manual say to check?
asked_as:
- xe795 resistance wont change
- no resistance on my 2016 spirit xe795
- elliptical driver board cn2
- generator brake elliptical no tension
keywords:
- no resistance
- cn2
- driver board
- 8-pin cable
- generator brake
- hybrid generator
- display board
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2016
  applies_to:
  - xe795-2016
  section: errors
  code: no-code
  model_number:
  - '795015'
authority: 3
not_to_be_confused_with:
- spirit-xe-errors-no-resistance-check-console-then-replace-the-gear-motor-cable
- ce800ent-no-resistance
see_also:
- xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: XE795 2016 (XE815-SE024-01) service manual Test configuration pin tables
    and Troubleshooting (Display board / 8-pin cable), PDF p. 39-41, text.md lines
    550-609
  extracted_at: '2026-09-11'
---

**This elliptical prints no code for a resistance fault.** Its error table holds one row, `EEPROM ERR` (`spirit-elliptical-errors-eeprom-err-replace-upper-controller`); the `--` tension-motor fault of its sister books does not exist here because the XE795 2016 brakes with a hybrid generator (work voltage DC 0.4~14V) and has no tension motor. What it prints instead is a two-part `Troubleshooting` table after the pin definitions:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press UP key. The driver board CN2 OUTPUT higher output voltage than the previous level. 2. Press DOWN key. The driver board CN2 OUTPUT lower output voltage than the previous level. 3. If not as above, inspect the cable and connections. |
| 8-pin cable | 1. Inspect whether the 8-PIN cable is connected well. 2. Test by replacing the cable with a good one. |

**Unlike the XBR95 2016 bike's printing of this table, this one gives the direction**: the CN2 output must be *higher than the previous level* on UP and *lower* on DOWN. No figure is printed for it. If it does not move with the key, the cable and its connections come before the board.

The two pin tables on the pages before it give what the connectors carry. Console to driver board, six pins: `1. 12 VDC, 2. GND, 3. +6 VDC, 4. NC, 5. RES, 6. RPM`. Driver board control, six pins: `1. 12 VDC, 2. GND, 3. +5 VDC, 4. NC, 5. PWM, 6. SPD`, beside the generator brake output and generator input connectors. **The two tables give pin 3 as +6 VDC and as +5 VDC**, and the display-board drawing calls the system cable 6 pins while this table calls it 8-pin; the book does not reconcile either.

The XBR95 2016 recumbent bike prints the same two-part table, pin-3 mismatch included, without the up/down direction (`xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`). The tension-motor ellipticals answer the same symptom with a console check and a new gear-motor cable (`spirit-xe-errors-no-resistance-check-console-then-replace-the-gear-motor-cable`), and the generator-brake CE800 with a control board (`ce800ent-no-resistance`).
