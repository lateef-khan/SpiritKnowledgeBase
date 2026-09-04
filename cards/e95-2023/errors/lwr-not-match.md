---
id: e95-2023-lwr-not-match
title: LWR not match message
kind: troubleshooting
question: What does LWR not match mean on a Sole e95-2023 elliptical?
asked_as:
- console says lwr not match
- lwr not match on my sole elliptical
- how do i clear lwr not match on a e95
keywords:
- lwr not match
- driver board
- controller number
- upper controller
- console
- machine type
- error message
- part number
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95-2023
  applies_to:
  - e95-2023
  section: errors
  code: lwr
authority: 3
not_to_be_confused_with:
- e95-2023-lwr-not-found
- e95-2023-eeprom-err
see_also:
- e95-2023-engineer-mode
source:
  ref: sole-elliptical-e95-2023-service-manual
  locator: Error code list and section 8.3, pages 17-18
  extracted_at: '2026-09-04'
---

**This is LWR not match, not LWR not found. They are two different faults with two different fixes.**

Definition: **the driver board controller does not match the console.**

Troubleshooting, in the manual's order:

1. **Check that the driver board controller number is CS51005-21S.**
2. Replace the **upper controller**.

**The controller number is model-specific.** This manual prints **CS51005-21S**. The other 2023 elliptical service manuals do not all print the same number: the E35 and E95s manuals give CS51005-11S, and the E95 and E98 manuals give CS51005-21S. Read the number off the manual for the machine in front of you.

A separate, lower-authority company note (`sole-lwr-not-match`) covers the same message and adds a step this manual does not have: setting **Machine Type** in the settings menu to the correct model, and replacing the Computer Cables on a machine that was recently assembled and does not pass calibration.
