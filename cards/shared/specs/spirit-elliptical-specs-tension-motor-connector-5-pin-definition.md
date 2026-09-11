---
id: spirit-elliptical-specs-tension-motor-connector-5-pin-definition
title: 'The tension motor plug has five pins: 1 M+, 2 M-, 3 +5V, 4 VR, 5 GND, with
  a steel rope off the motor'
kind: spec
question: What are the five pins of the tension motor connector on a Spirit gear-motor
  elliptical?
asked_as:
- tension motor connector pins on the xe295
- what are the 5 pins on the ce850 gear motor plug
- xe395 resistance motor wiring m+ m-
- gear motor plug pinout spirit elliptical
keywords:
- tension motor
- gear motor
- connector
- pinout
- 5-pin
- m+
- m-
- +5v
- vr
- steel rope
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- e25-2016-tension-motor-connector-pinout
- sole-bike-tension-motor-connector-pinout
see_also:
- spirit-xb-specs-gear-motor-connector-5-pin-definition
- spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
- spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
- spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used
- xe395ent-2021-specs-driver-board-cs51005-connections
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: Tension Motor connector definition function, PDF p. 35 (printed
    35), text.md lines 578-600. CE850-2020: PDF p. 28, lines 472-499. XE195-2016:
    PDF p. 30, lines 434-458. XE295-2016: PDF p. 30, lines 442-466. XE395-2016: PDF
    p. 36, lines 573-595. XE395ENT-2021: PDF p. 24, lines 279-301. XE895-2016: PDF
    p. 36, lines 579-601. XG400-2016: PDF p. 28, lines 380-404. Every book prints
    the same drawing'
  extracted_at: '2026-09-11'
---

Eight books print one drawing: the gear motor with its **STEEL ROPE** leaving one end and a plug
labelled **MAIN CONTROL** at the other, the plug numbered 5 down to 1.

| Pin | Signal |
|---|---|
| 1 | **M+** |
| 2 | **M-** |
| 3 | **+5V** |
| 4 | **VR** |
| 5 | **GND** |

M+ and M- are the motor windings; +5V, VR and GND are the position potentiometer that tells the
console how far the steel rope has wound. **No wire colours are printed** on the drawing, and no
resistance for the potentiometer.

Where the other end lands depends on the machine. On the XE195, XE295 and XG400 the plug's five
lines run straight up the console loom as MTR-, MTR+, +5V, MPOS and GND
(`spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used`); on the driver-board
machines they go to the board's motor socket (J7 on the CS62004, J9 on the CS51007, J6 *ECB MTR* on
the CS51005), whose own pin list on the XE395ENT reads MTR-, MTR+, VREF, MPOS, GND
(`xe395ent-2021-specs-driver-board-cs51005-connections`).

The motor's working voltage is DC 4.5-7.5 V in the XE books and DC 4.0-6.0 V in the CE850 books.
The XB bikes use the same plug (`spirit-xb-specs-gear-motor-connector-5-pin-definition`); Sole's
E25/E35/E55 ellipticals print the same five pins on another brand
(`e25-2016-tension-motor-connector-pinout`).

