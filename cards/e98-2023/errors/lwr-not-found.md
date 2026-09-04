---
id: e98-2023-lwr-not-found
title: LWR not found message
kind: troubleshooting
question: What does LWR not found mean on a Sole e98-2023 elliptical?
asked_as:
- console says lwr not found
- lwr not found on my sole elliptical
- e98 display shows lwr not found
keywords:
- lwr not found
- driver board
- lower controller
- 6 pin
- computer cable
- upper controller
- error message
- console
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2023
  applies_to:
  - e98-2023
  section: errors
  code: lwr
authority: 3
not_to_be_confused_with:
- e98-2023-lwr-not-match
- e98-2023-eeprom-err
see_also:
- e98-2023-lwr-not-match
source:
  ref: sole-elliptical-e98-2023-service-manual
  locator: Error code list and section 8.2, pages 16-17
  extracted_at: '2026-09-04'
---

**This is LWR not found, not LWR not match. They are two different faults with two different fixes.**

Definition: **the driver board controller is not found.**

Troubleshooting, in the manual's order:

1. Check the connector of the **6 PIN computer cable**.
2. Replace the **lower controller**.
3. Replace the **upper controller**.

"Not found" means the console cannot see a driver board at all. "Not match" means it sees one but the part number is wrong. Do not swap the fixes.
