---
id: tt8-2019-ac-drive-motor-spec
title: Drive motor type, voltage and wire colours
kind: spec
question: What kind of drive motor does a Sole tt8-2019-ac treadmill have and how
  is it wired?
asked_as:
- what voltage is the treadmill drive motor
- which wire is positive on the drive motor
- is my treadmill motor ac or dc
keywords:
- drive motor
- motor wires
- m+
- m-
- red wire
- black wire
- ground
- motor voltage
- ac motor
- dc motor
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2019-ac
  applies_to:
  - tt8-2019-ac
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tt8-2019-drive-motor-spec
see_also:
- tt8-2019-ac-drive-motor-replacement
- tt8-2019-ac-e-04h-error-code
source:
  ref: sole-tm-tt8-2019-ac-service-manual
  locator: General Information, page 13
  extracted_at: '2026-09-04'
---

**AC model: TT8 2019 ST928A-YT037, AC drive motor driven by an inverter. The DC drive motor TT8 2019 (ST928-YT035) is a different machine and this card does not apply to it.**

**The drive motor is an AC motor fed by an inverter: no M+ / M- pair, no 0-180 V DC feed.** Do not
test it against the DC figures of the ST928-YT035.

- It is a variable speed **AC motor**.
- **Three wires — red, white and black — carry power to drive the motor.**
- The **green** wire is grounding.
- The main controller supplies DC power for the console, the incline driver and the **AC motor driver**, and
  links the console to the motor.

The lower assembly is drawn as SPEED SENSOR, MOTOR CONTROLLER, **POWER BOARD**, AC MOTOR, DECLINE
CONTROLLER and INCLINE MOTOR.

**One contradiction to be aware of inside this manual**: the motor replacement section still names "motor
wire (+) red and motor wire (-) black" and tells you to reconnect "red M+, black M-", which is DC wording
carried over from the DC manual and does not match the three-wire AC motor described here.
