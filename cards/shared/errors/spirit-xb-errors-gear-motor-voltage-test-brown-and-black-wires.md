---
id: spirit-xb-errors-gear-motor-voltage-test-brown-and-black-wires
title: 'Gear motor voltage test at the drive board: brown and black wires, plus and
  minus 5 to 6.0 VDC'
kind: procedure
question: How do I voltage test the resistance motor on a Spirit XBR55-2023, XBU55-2023,
  XBR55ENT-2021 or XBU55ENT-2021 bike?
asked_as:
- how to test the resistance motor on my spirit bike
- what voltage should the gear motor read on an xbr55
- multimeter test for the bike tension motor
- drive board power led not lit on spirit bike
keywords:
- voltage test
- gear motor
- tension motor
- multi-meter
- 20vdc
- brown wire
- drive board
- fuse
- power led
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
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
see_also:
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
- b94-2023-gear-motor-voltage-test
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: XBR55 2023 service manual 8.2 Gear Motor Voltage Test Procedure and the
    probe caption, PDF p. 13-14, text.md lines 242-294; XBU55 2023 service manual
    8.2 Gear Motor Voltage Test Procedure and the probe caption, PDF p. 13-14, text.md
    lines 225-293; XBR55ENT 2021 service manual Tension Motor Voltage Test Procedure
    and the probe caption, PDF p. 25-26, text.md lines 275-316; XBU55ENT 2021 service
    manual Tension Motor Voltage Test Procedure and the probe caption, PDF p. 25-26,
    text.md lines 272-313
  extracted_at: '2026-09-11'
---

This is the test the E2 section ends on (`spirit-xb-errors-e2-motor-does-not-move-on-level-key`).

1. Put the multi-meter on the **20VDC** setting and place the probes on the motor control wire (**red probe in brown wire, black probe in black wire**) on the drive board.
2. Turn on the unit power. The display will light up.
3. Press **LEVEL UP**. The normal reading should be **+5~6.0 VDC**, and the motor should operate with resistance increasing.
4. Press **LEVEL DOWN**. The normal reading should be **-5~6.0 VDC**, and the motor should operate with resistance decreasing.
5. If there is no voltage, inspect the power socket and the holder **FUSE**. If it is broken, replace it.
6. Inspect the drive board **POWER LED** to see if it is lit. If it is not lit, the drive board is bad and needs to be replaced.

The caption under the photo on the next page repeats the probe placement in the same words - brown and black - so the wire colours are stated twice and agree in all four books.

**The 2016 residential books put the probes on different wires and expect a different reading**: blue and green, 5.5 to 6.0 VDC, and their own caption contradicts them - `spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires`. Check which book you are holding before you clip a probe.

Sole's 2023 bikes print this procedure word for word: `b94-2023-gear-motor-voltage-test`. Different brand, separate card.
