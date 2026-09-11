---
id: spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used
title: 'The 14-pin console cable on the ellipticals without a driver board: motor,
  5 V, MPOS, RPM and 12 V on pins 1 to 10, pins 11 to 14 N/A'
kind: spec
question: What are the pins of the 14-pin console cable on a Spirit XE195, XE295 or
  XG400 elliptical?
asked_as:
- xe295 14 pin cable pinout
- xe195 console cable pin definition
- which pins are used on the xg400 system cable
- why are pins 11 to 14 n/a on the xe295 cable
keywords:
- 14-pin
- console cable
- system cable
- pin define
- pinout
- mtr+
- mpos
- rpm1 rpm2
- n/a
- 12v
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
see_also:
- spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
- spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor
source:
  ref: spirit-elliptical-xe295-2016-service-manual
  locator: 'XE295-2016: Console to Driver board wire pin define, PDF p. 39 (printed
    39), text.md lines 588-621. XG400-2016: PDF p. 37, lines 528-562. XE195-2016:
    PDF p. 39, lines 587-620, the same table with pin 8 also N/A'
  extracted_at: '2026-09-11'
---

The page keeps its *Console to Driver board* heading even though these machines have no driver
board: the cable runs from the console board's J2 down the mast to the gear motor and speed
sensor plugs.

| Pin | XE295 / XG400 | XE195 | Pin | All three |
|---|---|---|---|---|
| 1 | MTR- | MTR- | 8 | **RPM2** on XE295/XG400, **N/A** on XE195 |
| 2 | MTR+ | MTR+ | 9 | GND |
| 3 | +5V | +5V | 10 | +12V |
| 4 | MPOS | MPOS | 11 | **N/A** |
| 5 | GND | GND | 12 | **N/A** |
| 6 | RPM1 | **RPM** | 13 | **N/A** |
| 7 | GND | GND | 14 | **N/A** |

Pins 12-14 are the INC+, INC- and IPOS lines of the XE395/XE895 cable, absent here because there
is no actuator (`spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins`).
The XE295 and XG400 circuit diagrams draw **SPEED SENSOR1 and SPEED SENSOR2**, the XE195's a
single **SPEED SENSOR** - hence the second RPM pin on two of the three
(`spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor`). The XE195 page also calls its
console socket *J2 SYSTEM CABLE (10 PINS)* while tabling fourteen positions; ten is the count of
pins in use.

Pins 1-4 pass to the gear motor's 5-pin plug (`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`).

