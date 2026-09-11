---
id: xe395ent-2021-specs-console-to-driver-board-6-pin-definition
title: 'The 6-pin console-to-driver cable on the incline ENT elliptical: 12 V, GND,
  TXD, RXD, EUP and DMK'
kind: spec
question: What are the six pins of the console-to-driver-board cable on a Spirit xe395ent-2021
  elliptical?
asked_as:
- xe395ent console cable pinout
- 6 pin system cable xe395 ent
- what is eup on the xe395ent cable
- xe395ent txd rxd pins
keywords:
- 6-pin
- console cable
- system cable
- pin define
- pinout
- txd
- rxd
- eup
- dmk
- 12v
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xe795-2016-specs-console-to-driver-board-6-pin-definition
- e25-2019-console-to-driver-board-pinout
see_also:
- xe395ent-2021-specs-driver-board-cs51005-connections
- xe395ent-2021-specs-display-board-ata10001-and-interface-board-connections
- xe395ent-2021-specs-circuit-diagram-xe539s-se025
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: Console to Driver board wire pin define, PDF p. 33 (printed 33), text.md
    lines 414-433; Driver board to tension motor pin define and RPM pin define, PDF
    p. 34, lines 433-461
  extracted_at: '2026-09-11'
---

The ENT console talks to its CS51005 driver board over a **six-pin serial cable**, not the 14-pin
parallel loom of the 2016 XE395:

| Pin | Signal |
|---|---|
| 1 | **12V** |
| 2 | **GND** |
| 3 | **TXD** |
| 4 | **RXD** |
| 5 | **EUP** |
| 6 | **DMK** |

TXD/RXD are the serial pair; **EUP** and **DMK** are printed without expansion. The display board
socket is **J8 SYSTEM CABLE (6 PINS)**, the driver-board socket **J5**, captioned *Console*.

The same two pages define the plugs on the driver board's far side: **tension motor at the
board, 1 MTR-, 2 MTR+, 3 VREF, 4 MPOS, 5 GND** (the motor's own plug reads M+, M-, +5V, VR, GND -
`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`), the **4-pin RPM plug RPM1,
GND, RPM2, GND**, and the 3-pin position sensor. Because the motor and sensor no longer pass
through the console cable, none of their lines appears in the six pins above.

The XE795-2016's 6-pin cable carries different signals - 12 V, GND, +6 V, NC, RES, RPM
(`xe795-2016-specs-console-to-driver-board-6-pin-definition`); Sole's E25-2019 has its own 6-pin
table (`e25-2019-console-to-driver-board-pinout`).

