---
id: e95s-2019-tension-motor-connector-pinout
title: Tension motor connector pin definition
kind: spec
question: What is the tension motor connector pinout on a Sole e95s-2019 elliptical?
asked_as:
- tension motor connector pins on a sole elliptical
- what are the 5 pins on the resistance motor
- wiring for the gear motor plug e95s
keywords:
- tension motor
- connector
- pinout
- 5 pin
- mt+
- mt-
- vcc
- vr
- gnd
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2019
  applies_to:
  - e95s-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2019-tension-motor-spec
- e95s-2019-e2-tension-motor-failure
- e95s-2019-console-to-driver-board-pinout
source:
  ref: sole-elliptical-e95s-2019-service-manual
  locator: Configuration, stride motor control function relate parts location, page
    47
  extracted_at: '2026-09-04'
---

The 5-pin motor plug on the drawing is:

| Pin | Signal |
|---|---|
| 1 | MT- |
| 2 | MT+ |
| 3 | VCC |
| 4 | VR |
| 5 | GND |

Note this is **not** the pin order the E25, E35 and E55 manuals print for their tension motor plug. Those read 1.M+, 2.M-, 3.+5V, 4.VR, 5.GND, so pins 1 and 2 are the other way round and pin 3 is named differently. Read the plug on the machine.

The manual's own section 6 heading "Tension Motor connector definition function" (page 34) carries no readable pin list in the converted text; the list above is from the stride motor control drawing on page 47.
