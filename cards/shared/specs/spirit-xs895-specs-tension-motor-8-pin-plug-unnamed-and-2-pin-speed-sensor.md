---
id: spirit-xs895-specs-tension-motor-8-pin-plug-unnamed-and-2-pin-speed-sensor
title: The tension motor plug is numbered 1 to 8 with no signal names, and its 2-pin
  speed sensor plug is GND and SPEED
kind: spec
question: What are the pins of the tension motor connectors on a Spirit XS895 incline
  stepper?
asked_as:
- xs895 tension motor connector pins
- 8 pin gear motor plug on the spirit incline stepper
- speed sensor plug on the xs895 motor
- does the xs895 manual name the motor pins
keywords:
- tension motor
- gear motor
- connector
- 8-pin
- speed sensor
- gnd
- speed
- steel rope
- pinout
- unnamed
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
see_also:
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
- spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 6-1-6 TENSION MOTOR CONNECTOR DEFINITION FUNCTION, PDF p. 24 (printed 23),
    text.md lines 326-353 (the numbers 1-8, 1-2 and the SPEED SENSOR list are native;
    the photographs read from a 110 dpi render, OCR supplement 1315-1326)
  extracted_at: '2026-09-11'
---

Two photographs of a black gear motor: the front, with a **STEEL ROPE** callout on the white drum,
and the side, which has a white eight-way socket at the top numbered **1 to 8** and a white two-way
below it numbered 1 to 2.

| Plug | Pins printed |
|---|---|
| Eight-way | **1, 2, 3, 4, 5, 6, 7, 8** - numbers only, no names |
| Two-way | **SPEED SENSOR: 1 GND, 2 SPEED** |

**The book never says what the eight pins carry.** The XRW600 rower's motor is the same two-socket
type and its book does name them - VIN, MT+, MT-, COUNT, ZERO, VCC, GND, SPEED
(`xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor`) - and the XS895's own
11-pin console cable carries SPEED, GND, VCC+5V, ZERO, COUNT, MOTOR-, MOTOR+ and VIN
(`spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins`), which are the
same eight signals. That is the likely content of the plug, but it is inferred from two other
pages, not printed on this one; meter before you rely on it.

The circuit diagram calls the lead an **8 pin Motor W/cable** into the controller
(`spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor`). The E2 test
still says "blue wire" and "green wire" for the motor pair, copied from the five-pin books.

