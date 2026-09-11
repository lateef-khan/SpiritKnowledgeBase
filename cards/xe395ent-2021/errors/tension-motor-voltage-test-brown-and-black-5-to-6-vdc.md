---
id: xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc
title: 'Tension motor voltage test at the drive board: brown and black wires, plus
  and minus 5 to 6.0 VDC, with the caption agreeing'
kind: procedure
question: How do I voltage test the tension motor on a Spirit xe395ent-2021 elliptical?
asked_as:
- how to test the tension motor on the xe395ent
- e2 voltage test elliptical
- brown and black wire test on the drive board
- ent elliptical resistance motor volts
keywords:
- tension motor
- voltage test
- multimeter
- drive board
- brown wire
- black wire
- 5 vdc
- fuse
- power led
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
see_also:
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires
- e25-2016-tension-motor-voltage-test
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: XE395ENT 2021 (XE539S-SE025-01) service manual Tension Motor Voltage Test
    Procedure and the photo caption, PDF p. 28-29, text.md lines 340-380
  extracted_at: '2026-09-11'
---

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in brown wire, Black probe in black wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+5~6.0VDC**. Motor operates. Resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5~6.0VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, inspect power socket the holder **FUSE**. If broke replace it.
6. Inspect the drive board **POWER LED** whether lit. If no lit the drive board is bad. Replace it.

This is the test the `E2` section ends on (`xe395ent-2021-errors-e2-tension-motor-does-not-move`). **The floor of the normal reading is 5 V**, and the wires are brown and black.

**On this book the caption agrees with the step**: *Place probes on the motor control wire (Red probe in brown wire, Black probe in black wire) on the drive board* is printed under the photo in the same words. The 2016 books say blue and green in the step and *palm* and black in the caption.

The 2016 residential ellipticals test on blue and green wires with a 5.5 V floor (`spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`) and the CE850 books with a 5 V floor (`spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc`). The XBR55ENT and XBU55ENT 2021 bikes print this brown-and-black, 5 V page for their own motor (`spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires`), as does Sole's E25 2016 (`e25-2016-tension-motor-voltage-test`).
