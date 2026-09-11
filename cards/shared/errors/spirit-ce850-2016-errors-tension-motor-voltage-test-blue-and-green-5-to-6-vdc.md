---
id: spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
title: 'Tension motor voltage test at the drive board: blue and green wires, plus
  and minus 5 to 6.0 VDC, and a caption that names other wires'
kind: procedure
question: How do I voltage test the tension motor on a Spirit CE850-2016, CE850-2020
  or XE895-2016 elliptical?
asked_as:
- how to test the tension motor on a spirit elliptical
- voltage at the resistance motor wires
- elliptical resistance motor multimeter test
- ce850 tension motor test
keywords:
- tension motor
- voltage test
- multimeter
- drive board
- blue wire
- green wire
- 5 vdc
- fuse
- power led
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe895-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc
see_also:
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- ce850-2024-errors-err-tension-motor-failure
- e25-2016-tension-motor-voltage-test
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual Tension Motor Voltage Test Procedure
    and the photo caption, PDF p. 42-43, text.md lines 688-731; CE850 (2020) service
    manual Tension Motor Voltage Test Procedure and the photo caption, PDF p. 35-36,
    text.md lines 585-624; XE895 2016 (XE895-SE022) service manual Tension Motor Voltage
    Test Procedure and the photo caption, PDF p. 43-44, text.md lines 688-727
  extracted_at: '2026-09-11'
---

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+5~6.0VDC**. Motor operates. Resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5~6.0VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, inspect power socket the holder **FUSE**. If broke replace it.
6. Inspect the drive board **POWER LED** whether lit. If no lit the drive board is bad. Replace it.

This is the test the tension-motor section ends on: the `--` section of the CE850 2016 and XE895 2016 (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`) and the `Err` section of the CE850 (2020) (`ce850-2024-errors-err-tension-motor-failure`). All three print the six steps in the same words, and **the floor of the normal reading is 5 V** on all three.

**All three books contradict themselves on the wire colours.** Step 1 says blue and green. The caption under the photo on the very next page says *Place probes on the motor control wire (Red probe in palm wire, Black probe in black wire)*. The step is the instruction and the caption is a leftover; go by the drive board's motor connector rather than by either colour.

**The XE195, XE295, XE395 and XG400 2016 print the same six steps with a 5.5 V floor** (`spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`), and the XE395ENT 2021 with a 5 V floor on brown and black wires (`xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc`). Sole's E25, E35 and E55 2016 print it with brown and black wires and a 5 V floor (`e25-2016-tension-motor-voltage-test`), and the Spirit XB 2016 bikes with blue and green and 5.5 V (`spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires`). Quote the figure that belongs to the book in front of you.
