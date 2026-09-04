---
id: sb1200-2023-lwr-not-found
title: LWR not found message
kind: troubleshooting
question: What does LWR not found mean on a Sole SB1200-2023 spin bike?
asked_as:
- my sb1200 says lwr not found
- lwr not found on the spin bike
- console cannot find the lower controller
keywords:
- lwr not found
- lower controller
- 7 pin
- computer cable
- upper controller
- driver board
- error message
facets:
  brand:
  - sole
  product_line: bike
  model: sb1200-2023
  applies_to:
  - sb1200-2023
  section: errors
  code: lwr
authority: 3
not_to_be_confused_with:
- sb1200-2023-lwr-not-match
- sb1200-2023-eeprom-error
see_also:
- sb1200-2023-lwr-not-match
source:
  ref: sole-bike-sb1200-2023-service-manual
  locator: 'Section 7 Error Code List, Section 7.2 Error Message: LWR not found (page
    15) and the Troubleshooting table on page 16'
  extracted_at: '2026-09-04'
---

**This is LWR not found, not LWR not match.** Not found means the console cannot see the driver board controller at all. Not match means it sees one but it is the wrong one.

Definition: the driver board controller is not found.

Troubleshooting, in order:

1. Check the connector of the **7 PIN computer cable**.
2. Replace the **lower controller**.
3. Replace the **upper controller**.

**The cable check is spelled out again in a second table on page 16:**

| Part | Troubleshooting |
|---|---|
| Display board | If not as above, inspect the cable and connections. |
| 7-pin cable | 1. Inspect whether the 7-PIN cable is connected well. 2. Test by replacing the cable with a good one. |

The LCB 2023 and LCR 2023 bikes use a **6-pin** cable for the same job. Do not carry that to this machine.
