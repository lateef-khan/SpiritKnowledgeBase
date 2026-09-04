---
id: sole-dc-controller-error-code-list
title: DC digital controller error code list
kind: spec
question: What are the error codes for a Sole treadmill with a DC digital controller?
asked_as:
- list of treadmill error codes
- what do the e codes mean
keywords:
- error code list
- e1
- e8
- dc digital controller
- error codes
- console codes
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
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-inverter-error-code-list
source:
  ref: sole-tm-console-error-code-list
  locator: DC digital controller table
  extracted_at: '2026-09-03'
---

Applies to the F63, F65, F80, F85, F89 and TT8, which use the DC digital controller.

| Code | Cause | Solution |
|---|---|---|
| E1 | No speed signal read by the controller in calibration mode | Check or replace the speed sensor; replace the controller (needs recalibration); replace the main motor |
| E2 | Overload trips the control board overcurrent protection | Check the main motor and running belt for a blockage; make sure there is enough lubricant between belt and deck; check the front and rear rollers for noise and replace if needed; replace the controller (needs recalibration) |
| E3 | Incline abnormality | Check the incline motor cable; replace the elevation motor (needs recalibration); replace the controller (needs recalibration) |
| E4 | Abnormal voltage at the motor terminals, or motor cable fault | Check the main motor cable; check for loose or corroded motor terminals; replace the controller (needs recalibration); replace the main motor |
| E5 | Communication between console and control board is broken | Check the console to controller connection; check all control wires; replace the controller (needs recalibration); replace the console |
| E6 | Controller malfunction | Check for abnormal resistance in the drivetrain; replace the controller (needs recalibration) |
| E7 | External voltage abnormality | Check the external AC input; check the AC terminals on the controller for looseness or corrosion; replace the controller if damaged by an E4 or E6 fault |
| E8 | Controller EEPROM malfunction | Replace the controller (needs recalibration) |
| No Display | Console does not light up when powered on | Check plug, fuse and control wires; if the power light is on, replace the control wire between console and controller; if it is off, replace the controller; replace the console |
| Safety Key | Safety key setup and detection | Check the key is inserted; check the key cable; replace the console; replace the controller |

**Scope.** This card is the fallback for the Sole treadmills that have no service manual in this knowledge base. Every machine listed in `applies_to` is one of those. A machine with a service manual has its own card for this code, or its manual shows the code does not exist on it — check the model's own cards first. AC inverter machines (ST90, TT9, the AC TT8 variants), the F63 2026 and the C80 use different code families and are deliberately excluded.
