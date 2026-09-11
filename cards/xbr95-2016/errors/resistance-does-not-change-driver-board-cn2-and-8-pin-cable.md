---
id: xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
title: 'Resistance does not change on the generator-brake bike: watch the driver board
  CN2 output, then swap the 8-pin cable'
kind: troubleshooting
question: Why does the resistance not change on a Spirit xbr95-2016 recumbent bike,
  and what does the service manual say to check?
asked_as:
- resistance wont change on my xbr95
- level up does nothing on the spirit recumbent
- xbr95 brake not responding
- no resistance on spirit xbr95 2016
keywords:
- resistance
- generator brake
- driver board
- cn2
- display board
- 8-pin cable
- level up
- level down
- recumbent
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2016
  applies_to:
  - xbr95-2016
  section: errors
  code: no-code
  model_number:
  - '951115'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-errors-dashes-tension-motor-failure
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
see_also:
- spirit-bike-errors-eeprom-err-replace-upper-controller
- sole-bike-ems-brake-resistance-not-changing
- spirit-xb-2016-errors-dashes-tension-motor-failure
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: XBR95 2016 service manual Troubleshooting table (Display board / 8-pin
    cable), PDF p. 41, text.md lines 572-585; XBR95 2016 service manual Test configuration
    pin tables, PDF p. 39-40, text.md lines 528-572
  extracted_at: '2026-09-11'
---

**This bike prints no code for a resistance fault.** Its error table holds one row, `EEPROM ERR` (`spirit-bike-errors-eeprom-err-replace-upper-controller`); the `--` and `E2` motor faults of its sister books do not exist here because the XBR95 2016 brakes with a hybrid generator and has no tension motor. What it prints instead is a two-part `Troubleshooting` table, reproduced in full:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press UP key. The driver board CN2 OUTPUT. 2. Press DOWN key. The driver board CN2 OUTPUT. 3. If not as above, inspect the cable and connections. |
| 8-pin cable | 1. Inspect whether the 8-PIN cable is connected well. 2. Test by replacing the cable with a good one. |

**Steps 1 and 2 print no direction** - the book says the CN2 output should change when UP or DOWN is pressed and does not say which way. Read it as: the output must move with the key, and if it does not, the cable and its connections come before the board.

The two pin tables on the pages before it give what CN2 carries. Console to driver board, six pins: `1. 12 VDC, 2. GND, 3. +6 VDC, 4. NC, 5. RES, 6. RPM`. Driver board control, six pins: `1. 12 VDC, 2. GND, 3. +5 VDC, 4. NC, 5. PWM, 6. SPD`, beside the generator brake output and generator input connectors. **The two tables give pin 3 as +6 VDC and as +5 VDC** - one of them is wrong and the book does not say which; do not quote either as a pass/fail figure without the other.

Sole's LCB 2016, LCB 2019 and LCR 2016 print the same two-part table about their EMS brake, with the driver board connector named CN3 and a 7-pin or 6-pin cable: `sole-bike-ems-brake-resistance-not-changing`. Different brand and different connector names; a separate card.
