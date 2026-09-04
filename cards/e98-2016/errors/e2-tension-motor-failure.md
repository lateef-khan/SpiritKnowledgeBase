---
id: e98-2016-e2-tension-motor-failure
title: E2 in the error table, with no troubleshooting section
kind: troubleshooting
question: What does error E2 mean on a Sole e98-2016 elliptical?
asked_as:
- my sole e98 shows e2
- what is error code e2 on a sole elliptical
- resistance wont change and it says e2
keywords:
- e2
- tension motor
- error code
- ems brake
- no section
- resistance
- brake test
- error table
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2016
  applies_to:
  - e98-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e98-2016-e1-eeprom-failure
- e98-2016-e3-incline-vr-error
see_also:
- e98-2016-ems-brake-spec
- e98-2016-flywheel-no-resistance
- e98-2016-maintenance-menu
source:
  ref: sole-elliptical-e98-2016-service-manual
  locator: Error code items table, page 40
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (incline VR).**

The error code table prints: **E2 - "Tension motor is failure".** That is all this manual says about E2.

**The manual carries no E2 troubleshooting section for this machine.** The table of contents lists only 8.1 Error Message: E1 and 8.2 Error Message: E3, and the body follows it. Do not read across from the E25, E35, E55, E95 or E95S manuals: those machines drive a **tension motor at DC 4.5~7.5V**, while this one uses an **EMS brake at DC 0~23V**, so their +/-5VDC drive board test does not describe this machine.

What this manual does give for a resistance complaint: the Engineering Mode menu has a **BRAKE TEST** entry for testing the EMS brake, and section 9-3 says that if there is no resistance, take off both chain covers and check for disconnection or breakage of the electric cables to the inductive flywheel.
