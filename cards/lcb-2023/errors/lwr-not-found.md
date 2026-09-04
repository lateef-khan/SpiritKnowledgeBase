---
id: lcb-2023-lwr-not-found
title: LWR not found message
kind: troubleshooting
question: What does LWR not found mean on a Sole LCB-2023 bike?
asked_as:
- my 2023 lcb says lwr not found
- lwr not found on the light commercial bike
- console cannot find the brake controller
keywords:
- lwr not found
- brake controller
- 6 pin
- computer cable
- display board
- driver board
- error message
facets:
  brand:
  - sole
  product_line: bike
  model: lcb-2023
  applies_to:
  - lcb-2023
  section: errors
  code: lwr
authority: 3
not_to_be_confused_with:
- lcb-2023-lwr-not-match
- lcb-2023-eeprom-error
see_also:
- lcb-2023-lwr-not-match
source:
  ref: sole-bike-lcb-2023-service-manual
  locator: 'Section 8 Error Code List and Section 8.2 Error Message: LWR not found,
    page 18'
  extracted_at: '2026-09-04'
---

**This is LWR not found, not LWR not match.** Not found means the console cannot see the brake controller at all. Not match means it sees one but it is the wrong one.

Definition: the brake controller is not found. The error table describes it as "Driver board controller is not found."

Troubleshooting, in order:

1. Check the connector of the **6 PIN computer cable**.
2. Replace the **brake controller**.
3. Replace the **display board**.
