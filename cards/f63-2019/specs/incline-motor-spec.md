---
id: f63-2019-incline-motor-spec
title: Incline motor voltage and wiring
kind: spec
question: What are the incline motor specifications for a Sole F63-2019?
asked_as:
- what voltage is the incline motor
- which incline wire is up
- incline motor wiring on my sole treadmill
keywords:
- incline motor
- ac motor
- up wire
- down wire
- com
- position sensor
- vr wire
- grounding wire
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2019-e3-error-code
- f63-2019-incline-position-sensor-test
- f63-2019-incline-motor-replacement
source:
  ref: sole-tm-f63-2019-service-manual
  locator: page 11, GENERAL INFORMATION, and page 49
  extracted_at: '2026-09-04'
---

An **AC motor at 110 or 230 volt**, used to control the elevation through the console and the main controller.

**Five wire connection: red, black, white, green**, plus **one 3-pin cable for the position sensor**.

- AC voltage on the **red** wire (UP) increases the incline.
- AC voltage on the **black** wire (DOWN) decreases the incline.
- The **white** wire (COM) is neutral.
- The **green/yellow** wire is the grounding wire.

At the controller the same three power wires land on JK80: Com to white, UP to red, DOWN to black. The 3-pin VR wire lands on JK60 and carries GND, the sensor pin (AD) and +5V VCC.
