---
id: spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
title: 'The 14-pin console-to-driver cable: motor, 5 V, MPOS, two RPM lines, 12 V,
  and INC+, INC- and IPOS for the actuator'
kind: spec
question: What are the fourteen pins of the console-to-driver-board cable on a Spirit
  CE850-2016, XE395-2016 or XE895 elliptical?
asked_as:
- ce850 14 pin cable pinout
- xe395 console cable pin definition
- which pin is ipos on the xe895 system cable
- 14 pin computer cable wiring elliptical
keywords:
- 14-pin
- console cable
- system cable
- computer cable
- pin define
- pinout
- mtr+
- mpos
- rpm1 rpm2
- inc+ inc- ipos
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe395-2016
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v
- spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used
- e35-2016-console-to-driver-board-pinout
see_also:
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: Console to Driver board wire pin define, PDF p. 47 (printed
    47), text.md lines 766-796. XE895-2016: PDF p. 48, lines 762-797. XE395-2016:
    PDF p. 48, lines 755-789. All three print the same fourteen rows'
  extracted_at: '2026-09-11'
---

Three books print the same table for the cable between the display board's SYSTEM CABLE socket
and the driver board's J8:

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **MTR-** | 8 | **RPM2** |
| 2 | **MTR+** | 9 | **GND** |
| 3 | **+5V** | 10 | **+12V** |
| 4 | **MPOS** (tension motor position) | 11 | **GND** |
| 5 | **GND** | 12 | **INC+** |
| 6 | **RPM1** | 13 | **INC-** |
| 7 | **GND** | 14 | **IPOS** (actuator position) |

Pins 1-4 are the tension (gear) motor's drive and feedback, passed through the driver board to its
5-pin plug (`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`). Pins 12-14 carry
the actuator: **INC+ / INC-** command the AC motor's up and down relays and **IPOS** returns the
0-5 V of its position sensor - on the CE850 and XE895 that actuator is the stride motor, on the
XE395 the incline motor. Two RPM lines serve the two speed sensors.

**The XE195, XE295 and XG400 print the same table with pins 8 and 11-14 marked N/A** - no driver
board, no actuator (`spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used`).
**The CE850-2020 renumbers three pins** - RPM on 6, NC on 8, 5V on 9 - for its 2-pin RPM sensor
(`ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v`). Sole's E35 prints a
14-pin table of its own (`e35-2016-console-to-driver-board-pinout`), and the 2016 XB bikes another
(`spirit-xb-2016-specs-console-to-driver-board-14-pin-definition`).

