---
id: sc200-2019-tension-motor-spec
title: Tension motor working voltage
kind: spec
question: What voltage does the tension motor run on in a Sole sc200-2019?
asked_as:
- what voltage is the resistance motor on a sole climber
- tension motor spec sc200
- how much voltage should the tension motor get
keywords:
- tension motor
- working voltage
- 4v
- 5.5v
- dc
- resistance
- brake
- spec
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2019
  applies_to:
  - sc200-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2019-tension-motor-voltage-test
- sc200-2019-e2-tension-motor-failure
- sc200-2019-tension-motor-connector-pinout
source:
  ref: sole-elliptical-sc200-2019-service-manual
  locator: General Information, page 11
  extracted_at: '2026-09-04'
---

**Work voltage: DC 4~5.5V.** It controls resistance increases and decreases.

The console holds the key controls and the LCD display. The main controller includes the power supply and the motor driver control circuit. There is no separate incline driver: this machine has no incline motor.

The output during a level change is a different figure: **Level UP +2.5VDC, Level DOWN -2.5VDC**, with a normal meter reading of +2.2~2.7VDC and -2.2~2.7VDC. Those numbers live in the E2 cards.

**These figures are specific to this machine.** The 2019 Sole ellipticals run their tension motor at DC 4.5~7.5V with a +/-5VDC drive.
