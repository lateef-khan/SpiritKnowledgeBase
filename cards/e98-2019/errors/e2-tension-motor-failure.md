---
id: e98-2019-e2-tension-motor-failure
title: E2 tension motor failure, table entry only
kind: troubleshooting
question: What does error E2 mean on a Sole e98-2019 elliptical?
asked_as:
- e2 on my sole elliptical
- resistance wont change and it shows e2
- what is error code e2 on an e98
keywords:
- e2
- tension motor
- ems brake
- resistance
- error code
- no troubleshooting
- elliptical
- brake test
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2019
  applies_to:
  - e98-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e98-2019-e1-eeprom-failure
- e98-2019-e3-incline-vr-error
see_also:
- e98-2019-ems-brake-spec
- e98-2019-maintenance-menu
- e98-2019-flywheel-no-resistance
source:
  ref: sole-elliptical-e98-2019-service-manual
  locator: Error code items table, page 38
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (incline VR).**

The error code table prints: **E2 - "Tension motor is failure".** That is all this manual says about E2.

**The manual carries no E2 troubleshooting section for this machine.** The table of contents lists only 8.1 Error Message: E1 and 8.2 Error Message: E3, and the body follows it. Do not read across from the E25, E35, E55 or E95s manuals: those machines drive a **tension motor at DC 4.5~7.5V**, while this one uses an **EMS brake at DC 0~23V**, so their +/-5VDC drive board test does not describe this machine.

What this manual does give for a resistance complaint: the Engineering Mode menu has a **BRAKE TEST** entry for testing the EMS brake, and section 9-3 says that if there is no resistance, take off both chain covers and check for disconnection or breakage of the electric cables to the inductive flywheel.
