---
id: e95s-2016-stride-motor-spec
title: Stride motor wiring and voltage
kind: spec
question: What are the stride motor wires and voltage on a Sole e95s-2016 elliptical?
asked_as:
- what colour wires does the stride motor have
- is the sole stride motor ac or dc
- stride motor wiring on a sole elliptical
keywords:
- stride motor
- 115 volt
- ac motor
- red wire
- black wire
- white wire
- green ground
- position sensor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2016
  applies_to:
  - e95s-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2016-stride-motor-test-procedure
- e95s-2016-stride-motor-replacement
source:
  ref: sole-elliptical-e95s-2016-service-manual
  locator: General Information, page 13, and the unnumbered Controller, Incline Motor,
    Tension Motor section, page 64
  extracted_at: '2026-09-04'
---

This is a **115 volt AC motor**. It has four wires: red, black, white and green, plus one 3-pin position sensor cable.

- AC voltage on the **red** wire (UP) makes the stride motor increase the stride.
- AC voltage on the **black** wire (DOWN) makes the stride motor decrease the stride.
- The **white** wire (COM) is neutral.
- The **green** wire is ground.

The position sensor wires are red = ground, white = position signal, black = 5vdc, with the signal running 0~5v depending on position.

**Zeroing distance for a replacement motor: 245 +/- 1mm** between the centres of the two holes, reached by turning the tubing clockwise to the end then counterclockwise **two and a half circles**.

This is **not** the 207 +/- 1mm and one and a half circles printed in the E35, E95 and E98 manuals of the same year for their incline motors. That figure is for a different mechanism and must not be used here.

Note the naming in the source: the General Information page calls it the STRIDE MOTOR, while the LED table, the disassembly section and the parts drawings head the same part Incline Motor.
