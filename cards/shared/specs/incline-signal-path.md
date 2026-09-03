---
id: sole-incline-signal-path
title: How the incline signal travels
kind: fact
question: How does the incline signal travel through a Sole treadmill?
asked_as:
- how does the incline work on a treadmill
- what path does the incline signal take
keywords:
- incline signal
- potentiometer
- computer cables
- incline motor
- motor controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - '*'
  section: specs
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also:
- sole-speed-signal-path
- sole-e3-error
source:
  ref: sole-tm-how-incline-signal-travels
  locator: whole document
  extracted_at: '2026-09-03'
---

The incline signal goes round a loop:

1. **Console** sends the command through the computer cables.
2. **Motor controller** sends power to the incline motor.
3. **Incline motor** moves, and reports its position back through the potentiometer wire.
4. **Motor controller** receives that position.
5. **Console** receives it back through the computer cables.

Use this to work out which part of the loop is broken when the incline misbehaves.
