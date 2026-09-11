---
id: spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
title: 'Tension motor voltage test at the drive board: blue and green wires, plus
  and minus 5.5 to 6.0 VDC, and a caption that names other wires'
kind: procedure
question: How do I voltage test the tension motor on a Spirit XBR25-2016, XBR55-2016
  or XBU55-2016 bike?
asked_as:
- how to test the resistance motor on my 2016 spirit bike
- what voltage should the tension motor read on an xbr25
- multimeter test bike tension motor blue wire
- which wires do i probe on the spirit bike drive board
keywords:
- voltage test
- tension motor
- multi-meter
- 20vdc
- blue wire
- green wire
- drive board
- fuse
- power led
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
- spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires
see_also:
- spirit-xb-2016-errors-dashes-tension-motor-failure
- spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires
- sole-bike-tension-motor-voltage-test
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: XBR25 2016 service manual Tension Motor Voltage Test Procedure and the
    probe caption on the next page, PDF p. 36-37, text.md lines 503-543; XBR55 2016
    service manual Tension Motor Voltage Test Procedure and the probe caption on the
    next page, PDF p. 38-39, text.md lines 525-564; XBU55 2016 service manual Tension
    Motor Voltage Test Procedure and the probe caption on the next page, PDF p. 36-37,
    text.md lines 504-543
  extracted_at: '2026-09-11'
---

This is the test the `--` section ends on (`spirit-xb-2016-errors-dashes-tension-motor-failure`).

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+5.5~6.0VDC**. Motor operates. Resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5.5~6.0VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, inspect power socket the holder **FUSE**. If broke replace it.
6. Inspect the drive board **POWER LED** whether lit. If no lit the drive board is bad. Replace it.

**The book contradicts itself on the wire colours.** Step 1 says blue and green. The caption under the photo on the very next page says *Red probe in palm wire, Black probe in black wire*. All three books carry both sentences. The step is the instruction and the caption is a leftover; go by the drive board's motor connector rather than by either colour name if the harness in front of you does not match, and expect the reading, not the colour, to decide the fault.

**The floor of the normal reading is 5.5 V here**, against the 5 V floor the 2023 and ENT books print for the same test on brown and black wires: `spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires`.

Sole's B94 and R92 of 2016-2019 print the procedure with brown and black wires and a 5 V floor: `sole-bike-tension-motor-voltage-test`. Different brand, separate card.
