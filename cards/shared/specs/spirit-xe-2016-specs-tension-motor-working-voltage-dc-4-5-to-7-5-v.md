---
id: spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
title: Tension motor working voltage is DC 4.5 to 7.5 V on the gear-motor XE ellipticals,
  and the electrical configuration names the console and tension motor
kind: spec
question: What voltage does the tension motor run on in a Spirit XE195, XE295, XE395,
  XE395ENT, XE895 or XG400 elliptical?
asked_as:
- xe295 tension motor voltage
- what is the working voltage of the xe195 gear motor
- xg400 electrical configuration
- xe895 tension motor spec
keywords:
- tension motor
- gear motor
- working voltage
- dc 4.5-7.5v
- electrical configuration
- console
- main controller
- lcd
- steel cable
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
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
- spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v
- spirit-xb-specs-gear-motor-working-voltage-dc-4-5-to-7-5-v
see_also:
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- xe395ent-2021-errors-tension-motor-voltage-test-brown-and-black-5-to-6-vdc
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
source:
  ref: spirit-elliptical-xe195-2016-service-manual
  locator: 'XE195-2016: section 3 Electrical Configurations, PDF pp. 11-12 (printed
    11-12), text.md lines 176-203. XE295-2016: PDF pp. 11-12, lines 175-202. XG400-2016:
    PDF pp. 9-10, lines 111-138. XE395-2016: PDF p. 12, lines 219-241. XE395ENT-2021:
    PDF p. 9, lines 70-105. XE895-2016: PDF p. 13, lines 239-261'
  extracted_at: '2026-09-11'
---

Six books print the same tension-motor entry:

> **TENSION MOTOR** - Work voltage: **DC 4.5 ~ 7.5 V**

It is the gear motor that winds the steel cable and moves the magnet bracket against the
flywheel. Its 5-pin plug is defined on
`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`.

**What else the section names, by machine:**

| Books | Parts named | Display |
|---|---|---|
| XE195, XE295, XG400 | **CONSOLE** and **TENSION MOTOR** only | LCD |
| XE395, XE895 | Console, MAIN CONTROLLER (DC supply for console, incline or stride driver, tension motor driver), TENSION MOTOR, INCLINE or STRIDE MOTOR | LCD |
| XE395ENT | the same four, console with a TFT LCD touch panel | touch LCD |

The three entry-level books' general line still says "Main controller include power supply and
motor driver control circuit" - boilerplate, because those machines have **no driver board**: the
console drives the gear motor directly from a DC adapter
(`spirit-xe-2016-specs-unit-block-diagram-no-driver-board`).

**4.5 to 7.5 V is the XE figure.** The two CE850 books print **DC 4.0 ~ 6.0 V** for the same class
of motor (`spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v`) - and the XE895,
which is the CE850-2016 manual under another name, prints 4.5-7.5 V, so the two figures are the
two editors' choices rather than two motors. The troubleshooting tests expect about 5.5-6 VDC
across the motor while a level changes. The XB bikes print the same 4.5-7.5 V
(`spirit-xb-specs-gear-motor-working-voltage-dc-4-5-to-7-5-v`).

