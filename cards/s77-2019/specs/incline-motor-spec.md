---
id: s77-2019-incline-motor-spec
title: Incline motor voltage and wire colours
kind: spec
question: What voltage is the incline motor on a Sole S77-2019 treadmill and what
  are its wire colours?
asked_as:
- what colour wires go to the incline motor
- how many volts is the incline motor on my s77
- incline motor wiring on my treadmill
keywords:
- incline motor
- 110 volt
- 230 volt
- red up
- black down
- white com
- position sensor
- grounding
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2019-incline-position-sensor-test
- s77-2019-incline-motor-installation
- s77-2019-e3-incline-vr
source:
  ref: sole-tm-s77-2019-service-manual
  locator: Section 3 General Information, page 12, and section 11-9, page 85
  extracted_at: '2026-09-04'
---

| Field | Value |
|---|---|
| Type | AC motor |
| Voltage | **110 or 230 volt** |
| Power wires | red, black, white, green (green/yellow is the grounding wire) |
| Sensor | One 3-pin cable for the position sensor |

| Wire | Terminal | Effect |
|---|---|---|
| Red | UP | AC voltage here raises the incline |
| Black | DOWN | AC voltage here lowers the incline |
| White | COM | Neutral |
| Green / yellow | Ground | - |

**The manual's wire count does not match its own list.** It says "All of five wire connection: red, black, white, green" and then names four colours. The earlier ST725 manual says four wires and names the same four.

**Two different figures for the mains at the incline motor.** Section 3 says 110 or 230 volt; the E3 test procedure on page 48 says the voltage between the neutral (white) wire and the up or down wire "should be about the same as the mains voltage ~ 110VAC (230VAC)". Measure against the supply the machine is actually on.
