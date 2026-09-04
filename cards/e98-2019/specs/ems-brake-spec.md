---
id: e98-2019-ems-brake-spec
title: EMS brake working voltage
kind: spec
question: What voltage does the EMS brake run on in a Sole e98-2019 elliptical?
asked_as:
- what voltage is the brake on a sole e98
- ems brake spec elliptical
- does the e98 have a tension motor
keywords:
- ems brake
- working voltage
- 0-23v
- dc
- resistance
- inductive flywheel
- ems controller
- spec
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2019
  applies_to:
  - e98-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e98-2019-e2-tension-motor-failure
- e98-2019-maintenance-menu
- e98-2019-flywheel-no-resistance
source:
  ref: sole-elliptical-e98-2019-service-manual
  locator: General Information, page 14
  extracted_at: '2026-09-04'
---

**Work voltage: DC 0 ~ 23V.** It controls resistance increases and decreases.

The console holds the key controls and TFT display. The main controller includes the power supply, the **EMS driver control circuit** and the incline control circuit.

**This is not the tension motor used on the other 2019 Sole ellipticals.** The E25, E35, E55 and E95s carry a tension motor at **DC 4.5~7.5V** pulling a steel cable, and their service manuals give a +/-5VDC drive board test for it. Those figures do not apply to this machine.

Engineering Mode has a **BRAKE TEST** entry for testing the EMS brake.
