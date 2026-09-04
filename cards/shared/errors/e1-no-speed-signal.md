---
id: sole-e1-error
title: 'E1 error: no speed signal'
kind: troubleshooting
question: What does an E1 error mean on a Sole treadmill?
asked_as:
- e1 error on my treadmill
- treadmill shows e1 during calibration
keywords:
- e1
- e1 error
- speed sensor
- no speed signal
- calibration error
- speed sensor alignment
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f63
  - f63-2013
  - f65
  - f65-2026
  - f80
  - f80-2026
  - f83
  - f83-2026
  - f85
  - f85-2020
  - f85-2026
  - f89
  - tt8
  - tt8-2020
  section: errors
  code: e1
authority: 2
not_to_be_confused_with: []
see_also:
- sole-calibration-button-console
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-e1-error-treadmills
  locator: whole document
  extracted_at: '2026-09-03'
---

**Meaning**: the controller read no signal from the speed sensor. It is a software or speed sensor problem, and it normally shows up only during a calibration.

If the error appeared after the machine was assembled, replace the computer cables first.

The signal can fail at the sensor, in the software that reads it, or on the path from the sensor to the controller to the console.

1. Make sure the speed sensor is aligned correctly.
2. Watch the LED on the controller. It should light each time the magnet passes the sensor. Not every machine has this light, so use it only to confirm that the sensor works.
3. If the sensor works, replace the console display board or the console assembly.
4. If there is no light indicator, replace the speed sensor, and possibly the console display board or console assembly as well.
5. Last resort: replace the motor controller, because it is not passing the speed sensor signal to the console.

**Scope.** This card is the fallback for the Sole treadmills that have no service manual in this knowledge base. Every machine listed in `applies_to` is one of those. A machine with a service manual has its own card for this code, or its manual shows the code does not exist on it — check the model's own cards first. AC inverter machines (ST90, TT9, the AC TT8 variants), the F63 2026 and the C80 use different code families and are deliberately excluded.
