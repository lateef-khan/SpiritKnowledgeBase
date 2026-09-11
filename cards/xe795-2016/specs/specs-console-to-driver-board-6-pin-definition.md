---
id: xe795-2016-specs-console-to-driver-board-6-pin-definition
title: 'The 6-pin console-to-driver cable of the 2016 generator elliptical: 12 V,
  GND, 6 V at the console and 5 V at the driver, NC, RES or PWM, and RPM or SPD'
kind: spec
question: What are the six pins of the console-to-driver-board cable on a Spirit xe795-2016
  elliptical?
asked_as:
- xe795 console cable pinout
- 6 pin system cable xe795
- which pin is pwm on the xe795 driver board
- xe795 pin 3 6 volt or 5 volt
keywords:
- 6-pin
- console cable
- system cable
- pin define
- pinout
- 12vdc
- res
- pwm
- rpm
- spd
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2016
  applies_to:
  - xe795-2016
  section: specs
  code: '*'
  model_number:
  - '795015'
authority: 3
not_to_be_confused_with:
- xe395ent-2021-specs-console-to-driver-board-6-pin-definition
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
see_also:
- xe795-2016-specs-display-amplifier-and-interface-board-connections
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xe795-2016-specs-circuit-diagram-xe815-se024
- xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: Console to Driver board wire pin define, PDF p. 39 (printed 39), text.md
    lines 550-570 (console end, photograph of the CS11020 board), and PDF p. 40, lines
    570-594 (driver end, photograph of the 031101B CN3 socket)
  extracted_at: '2026-09-11'
---

The book defines the cable twice, once at each end, and the two tables do not quite agree:

| Pin | At the console (p. 39) | At the driver board CN3 (p. 40) |
|---|---|---|
| 1 | 12 VDC | 12 VDC |
| 2 | GND | GND |
| 3 | **+6 VDC** | **+5 VDC** |
| 4 | NC | NC |
| 5 | **RES** | **PWM** |
| 6 | **RPM** | **SPD** |

Pins 5 and 6 are the same two signals under two names - the resistance command is a PWM level,
and the speed line is the RPM sensor's pulse, which enters at the console's J3 RPM IN and travels
**down** this cable to the controller. **Pin 3 is printed as 6 V at one end and 5 V at the
other**; the book does not resolve it. Sole's and Spirit's other 6-pin generator cables print
+6 V for this pin.

The troubleshooting chapter calls this an **8-PIN cable** in one step - a slip; every drawing and
both tables give six pins (`xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`).
The XE395ENT's six pins are serial data, not these
(`xe395ent-2021-specs-console-to-driver-board-6-pin-definition`); the 2016 XBR95 bike prints these
same two tables (`xbr95-2016-specs-console-to-driver-board-6-pin-definition`).

