---
id: spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
title: 'Tension motor voltage test at the elliptical drive board: blue and green wires,
  plus and minus 5.5 to 6.0 VDC, and a caption that names other wires'
kind: procedure
question: How do I voltage test the tension motor on a Spirit XE195-2016, XE295-2016,
  XE395-2016 or XG400-2016 elliptical?
asked_as:
- how to test the tension motor on a spirit xe elliptical
- xe395 resistance motor voltage
- elliptical drive board 5.5 volts
- xg400 tension motor test
keywords:
- tension motor
- voltage test
- multimeter
- drive board
- blue wire
- green wire
- 5.5 vdc
- fuse
- power led
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xg400-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
- xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc
see_also:
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
- e25-2016-tension-motor-voltage-test
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: XE195 2016 (XE509S-SE021-01) service manual Tension Motor Voltage Test
    Procedure and the photo caption, PDF p. 37-38, text.md lines 545-587; XE295 2016
    (XE519S-SE020-01) service manual Tension Motor Voltage Test Procedure and the
    photo caption, PDF p. 37-38, text.md lines 549-588; XE395 2016 (XE539S-SE019-01)
    service manual Tension Motor Voltage Test Procedure and the photo caption, PDF
    p. 43-44, text.md lines 681-720; XG400 2016 (SE551-SE023-01) service manual Tension
    Motor Voltage Test Procedure and the photo caption, PDF p. 35-36, text.md lines
    486-528
  extracted_at: '2026-09-11'
---

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+5.5~6.0VDC**. Motor operates. Resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5.5~6.0VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, inspect power socket the holder **FUSE**. If broke replace it.
6. Inspect the drive board **POWER LED** whether lit. If no lit the drive board is bad. Replace it.

This is the test the `--` section ends on (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`). The XE195 2016, XE295 2016, XE395 2016 and XG400 2016 print the six steps in the same words, and **the floor of the normal reading is 5.5 V** on all four.

**All four books contradict themselves on the wire colours.** Step 1 says blue and green. The caption under the photo on the very next page says *Place probes on the motor control wire (Red probe in palm wire, Black probe in black wire) on the drive board*. The step is the instruction and the caption is a leftover; go by the drive board's motor connector rather than by either colour.

**The CE850 2016, CE850 (2020) and XE895 2016 print the same six steps with a 5 V floor** (`spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc`), and the XE395ENT 2021 a 5 V floor on brown and black wires (`xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc`). The Spirit XBR25, XBR55 and XBU55 2016 bikes print exactly this page - blue and green, 5.5 V - for their own tension motor (`spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires`). Sole's E25 2016 uses brown and black and a 5 V floor (`e25-2016-tension-motor-voltage-test`).
