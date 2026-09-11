---
id: xe395ent-2021-specs-driver-board-cs51005-connections
title: 'Six call-outs on the CS51005 driver board of the incline ENT elliptical: AC
  in on two sockets, DOWN black, COM white and UP red spades, console, INC VR, RPM
  sensor and ECB MTR'
kind: spec
question: What connects where on the CS51005 driver board of a Spirit xe395ent-2021
  elliptical?
asked_as:
- xe395ent driver board connections
- cs51005 board
- which plug is the tension motor on the xe395 ent controller
- xe395ent lower board ecb mtr
keywords:
- driver board
- controller
- cs51005
- rev 1.2
- up com down
- console j5
- inc vr j10
- rpm sensor j8
- ecb mtr j6
- ac power
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
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
see_also:
- xe395ent-2021-specs-console-to-driver-board-6-pin-definition
- xe395ent-2021-specs-circuit-diagram-xe539s-se025
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-elliptical-specs-motor-controller-fuse-5-a
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: Driver Board PCB Component Locations, PDF p. 21 (printed 21), text.md lines
    231-237, and Driver Board function, PDF p. 23, lines 243-279; photographs read
    from 300 dpi renders (OCR supplement lines 1435-1462)
  extracted_at: '2026-09-11'
---

The board silkscreen reads **CS51005 Rev 1.2**. Call-outs on the function page, with the
silkscreen name in brackets:

| Socket | Lead |
|---|---|
| **J4** and **J9** | AC power - from the power switch and the fuse |
| spades | **DOWN - black**, **COM - white**, **UP - red** to the incline motor |
| **J5** | **SYSTEM CABLE** (*Console*) - the 6-pin serial cable |
| **J10** | **INCLINE MOTOR VR SET** (*INC VR*) - 3-pin position sensor |
| **J8** | **RPM SENSOR** - 4-pin |
| **J6** | **TENSION MOTOR** (*ECB MTR*) - 5-pin |

**No transformer sockets** are called out: unlike the CS62004 of the 2016 XE395, this board takes
mains straight in on J4/J9 and makes its own low voltages. The 6-pin console cable carries only
power and serial data (`xe395ent-2021-specs-console-to-driver-board-6-pin-definition`), so the
tension motor, the position sensor and the RPM sensor all terminate here rather than passing up to
the console.

The tension-motor pins at the board are 1 MTR-, 2 MTR+, 3 VREF, 4 MPOS, 5 GND; the motor's own plug
reads M+, M-, +5V, VR, GND (`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`).
The circuit diagram draws the board as *Controller* with the incline motor on the right and the
tension motor on the left (`xe395ent-2021-specs-circuit-diagram-xe539s-se025`).

