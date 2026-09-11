---
id: spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
title: Incline motor is an AC actuator printed at 120 V in the 2016 book and 115 V
  in the ENT book, with red up, black down, white common and green ground wires and
  a 3-pin position sensor
kind: spec
question: What are the electrical specifications of the incline motor on a Spirit
  XE395 or XE395ENT elliptical?
asked_as:
- xe395 incline motor voltage
- which wire is up on the xe395 incline motor
- xe395ent incline motor wires
- incline motor position sensor xe395
keywords:
- incline motor
- actuator
- 120 v ac
- 115 v ac
- red up
- black down
- white common
- green ground
- position sensor
- tension motor 4.5-7.5v
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe395-2016
  - xe395ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor
- e35-2016-incline-motor-spec
see_also:
- spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
- spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
- spirit-xe-specs-which-machines-have-a-power-incline
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: 'XE395-2016: section 3 Electrical Configurations, INCLINE MOTOR, PDF p.
    12 (printed 12), text.md lines 219-241. XE395ENT-2021: section 3, PDF p. 9, lines
    70-105, the same entry printed 115 volt AC'
  extracted_at: '2026-09-11'
---

Both books describe the incline motor as an AC motor "using variable elevation" - the linear
actuator under the rear rail - with the same four wires:

| Wire | Function |
|---|---|
| Red | **UP** |
| Black | **DOWN** |
| White | **COM** (neutral for both directions) |
| Green | **ground** |

plus a **3-pin position sensor** on its own lead
(`spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v`).

**The printed supply differs by five volts between the two editions**: **120 volt AC** in the
XE395-2016 book, **115 volt AC** in the XE395ENT-2021 book. Both are the North American mains
nominal; the meter tests in the error chapters use the same two figures
(`xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`,
`xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`).

Both books also name the tension motor on the same page at **DC 4.5 ~ 7.5 V**
(`spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v`). **No current, stroke or
duty figure is printed** for the actuator. The CE850's stride motor is the same four-wire class
of part doing a different job (`spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor`);
Sole's E35 incline motor is another brand's twin (`e35-2016-incline-motor-spec`).

