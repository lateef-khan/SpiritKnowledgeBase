---
id: sole-speed-signal-path
title: How the speed signal travels
kind: fact
question: How does the speed signal travel through a Sole treadmill?
asked_as:
- how does the speed sensor work
- what path does the speed signal take
keywords:
- speed signal
- speed sensor
- front roller
- magnet
- computer cables
- drive motor
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
- sole-incline-signal-path
- sole-e1-error
source:
  ref: sole-tm-how-speed-signal-travels
  locator: whole document
  extracted_at: '2026-09-03'
---

The speed signal goes round a loop:

1. **Console** sends the command through the computer cables.
2. **Motor controller** sends power to the drive motor.
3. **Drive motor** turns the front roller.
4. **Speed sensor** reads the magnet as it passes.
5. **Motor controller** receives the sensor reading.
6. **Console** receives it back through the computer cables.

Use this to work out which part of the loop is broken when the speed misbehaves.
