---
id: spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor
title: Stride motor is a 115 V AC actuator with red up, black down, white common and
  green ground wires and a 3-pin position sensor
kind: spec
question: What are the electrical specifications of the stride motor on a Spirit CE850
  or XE895 elliptical?
asked_as:
- ce850 stride motor voltage
- which wire is up on the xe895 stride motor
- does the ce850 stride motor run on 220 volts
- stride motor position sensor wires ce850
keywords:
- stride motor
- actuator
- 115 v ac
- 220 volt
- red up
- black down
- white common
- green ground
- position sensor
- 3-pin
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
- e95s-2016-stride-motor-spec
see_also:
- spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-ce850-specs-stride-length-18-to-24-inches
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: section 3 Electrical Configurations, STRIDE MOTOR, PDF p.
    13 (printed 13), text.md lines 238-260. XE895-2016: PDF p. 13, lines 239-261,
    the same entry. CE850-2020: PDF p. 12, lines 224-243, the same entry with the
    voltage printed 115 volt (or 220 volt)'
  extracted_at: '2026-09-11'
---

The stride motor is "an AC motor, using variable elevation" - the linear actuator that moves the
moving-range adjusting assembly to change stride length.

| | |
|---|---|
| Supply | **115 V AC** (the CE850-2020 book prints *115 volt (or 220 volt)*, the export machine's mains) |
| Red wire | **UP** |
| Black wire | **DOWN** |
| White wire | **COM** - the neutral, shared by up and down |
| Green wire | **ground** |
| Position feedback | a **3-pin position sensor** plug on its own lead |

The four motor wires land on the driver board's UP / COM / DOWN spade terminals and the ground
stud; the sensor lead lands on the board's VR socket. Pin colours of the sensor and the 0-5 V it
returns are on `spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v`.

**No current, stroke or duty figure is printed** for the actuator in any of the three books; the
zeroing distance the assembly chapter sets is a mechanical figure, not an electrical one. The
XE395's incline motor is the same class of part with the same four colours but a different job
and a different printed voltage
(`spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor`). Sole's E95S
stride motor is the same four colours and voltage on another brand (`e95s-2016-stride-motor-spec`).

