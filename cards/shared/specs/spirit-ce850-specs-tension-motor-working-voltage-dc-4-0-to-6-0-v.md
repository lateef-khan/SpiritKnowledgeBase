---
id: spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v
title: Tension motor working voltage is DC 4.0 to 6.0 V on the adjustable-stride elliptical,
  and the electrical configuration names four parts
kind: spec
question: What voltage does the tension motor run on in a Spirit CE850 elliptical,
  and what electrical parts does the service manual name?
asked_as:
- ce850 tension motor voltage
- what is the working voltage of the ce850 gear motor
- ce850 electrical configuration
- what does the main controller do on the ce850
keywords:
- tension motor
- gear motor
- working voltage
- dc 4.0-6.0v
- electrical configuration
- main controller
- stride motor
- console
- lcd
- led
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
see_also:
- spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
- spirit-ce850-specs-parts-electronic-parts-named
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: section 3 Electrical Configurations, PDF pp. 12-13 (printed
    12-13), text.md lines 214-260. CE850-2020: section 3, PDF pp. 11-12, lines 198-243,
    the same four entries with the tension motor headed TENSION MOTOR (GEAR MOTOR)
    and the console entry reading LED'
  extracted_at: '2026-09-11'
---

Section 3 of both books names four electrical parts:

- **CONSOLE** - the interface that controls all functions; key controls and a display (an **LCD**
  in the 2016 book, **LED** windows in the 2020 book).
- **MAIN CONTROLLER** - "the DC power supply for console, stride driver and tension motor driver";
  it includes the power supply and the driver control circuit.
- **TENSION MOTOR** (the 2020 book adds *GEAR MOTOR* in the heading) - **Work voltage: DC 4.0 ~
  6.0 V**. It winds a steel cable that moves the magnet bracket.
- **STRIDE MOTOR** - an AC actuator; its figures are on
  `spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor`.

**4.0 to 6.0 V is the CE850 figure.** Every XE-family book of the same years - including the
XE895, which is otherwise this same manual - prints **DC 4.5 ~ 7.5 V** for the same 5-wire gear
motor (`spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v`). The troubleshooting
test in the CE850 books expects **5 to 6 VDC** across the motor leads while a level changes, which
sits inside both ranges. The plug pinout is
`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`.

