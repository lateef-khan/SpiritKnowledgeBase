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
  - f50-2026
  - f60-2016
  - f60-2020
  - f63
  - f63-2013
  - f63-2016
  - f63-2019
  - f63-2023
  - f63-2026
  - f65
  - f65-2016
  - f65-2019
  - f65-2023
  - f65-2026
  - f80
  - f80-2016
  - f80-2019
  - f80-2023
  - f80-2026
  - f83
  - f83-2026
  - f85
  - f85-2016
  - f85-2019
  - f85-2020
  - f85-2021
  - f85-2023
  - f85-2026
  - f89
  - f89-2023
  - s77-2016
  - s77-2019
  - st90
  - st90-2020
  - st90-2021
  - st90-2023
  - tt8
  - tt8-2016
  - tt8-2016-ac
  - tt8-2019
  - tt8-2019-ac
  - tt8-2020
  - tt8-2023
  - tt9
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
