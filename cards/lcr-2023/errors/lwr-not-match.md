---
id: lcr-2023-lwr-not-match
title: LWR not match message
kind: troubleshooting
question: What does LWR not match mean on a Sole LCR-2023 bike?
asked_as:
- my 2023 lcr says lwr not match
- lwr not match on the light commercial recumbent
- wrong brake controller message on the bike console
keywords:
- lwr not match
- brake controller
- cs51012
- display board
- driver board
- error message
- recumbent bike
facets:
  brand:
  - sole
  product_line: bike
  model: lcr-2023
  applies_to:
  - lcr-2023
  section: errors
  code: lwr
authority: 3
not_to_be_confused_with:
- lcr-2023-lwr-not-found
- lcr-2023-eeprom-error
see_also:
- lcr-2023-lwr-not-found
- sole-lwr-not-match
source:
  ref: sole-bike-lcr-2023-service-manual
  locator: 'Section 8 Error Code List and Section 8.3 Error Message: LWR not match,
    page 18'
  extracted_at: '2026-09-04'
---

**This is LWR not match, not LWR not found.** Not match means the console sees a brake controller but it is the wrong one. Not found means it sees none at all.

Definition: the brake controller does not match the console. The error table describes it as "Driver board controller is not match with console."

Troubleshooting, in order:

1. Check that the **brake controller number is CS51012**.
2. Replace the **display board**.

The touchscreen machines also carry a Machine Type setting that produces this message when the console is set to the wrong model. This service manual does not mention it; the separate LWR Not Match note does.
