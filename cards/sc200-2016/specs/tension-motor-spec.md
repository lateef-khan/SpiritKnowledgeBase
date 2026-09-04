---
id: sc200-2016-tension-motor-spec
title: Tension motor working voltage
kind: spec
question: What voltage does the tension motor run on in a Sole sc200-2016 climber?
asked_as:
- what voltage is the resistance motor on my sole climber
- tension motor spec sole sc200
- how much voltage should the tension motor get
keywords:
- tension motor
- working voltage
- 4.5v
- 7.5v
- dc
- resistance
- brake
- spec
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2016
  applies_to:
  - sc200-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2016-tension-motor-voltage-test
- sc200-2016-e2-tension-motor-failure
- sc200-2016-tension-motor-connector-pinout
source:
  ref: sole-elliptical-sc200-2016-service-manual
  locator: General Information, page 12
  extracted_at: '2026-09-04'
---

**Work voltage: DC 4.5~7.5V.** It controls resistance increases and decreases.

The drive board output during a level change is a different figure: **Level UP +5VDC, Level DOWN -5VDC**, with a normal meter reading of **+5.5~6.0VDC** and **-5.5~6.0VDC** at the motor control wire. Those numbers live in the E2 tension motor cards.

Section 3 describes only the console and the tension motor for this machine: "Main controller Include power supply and motor driver control circuit". There is no incline driver.
