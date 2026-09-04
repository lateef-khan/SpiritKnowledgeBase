---
id: sb1200-2023-lwr-not-match
title: LWR not match message
kind: troubleshooting
question: What does LWR not match mean on a Sole SB1200-2023 spin bike?
asked_as:
- my sb1200 says lwr not match
- lwr not match on the spin bike
- wrong controller message on the spin bike console
keywords:
- lwr not match
- driver board controller
- cs51006-02
- upper controller
- machine type
- error message
- spin bike
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
- sb1200-2023-lwr-not-found
- sb1200-2023-eeprom-error
see_also:
- sb1200-2023-lwr-not-found
- sb1200-2023-machine-type-setting
- sole-lwr-not-match
source:
  ref: sole-bike-sb1200-2023-service-manual
  locator: 'Section 7 Error Code List and Section 7.3 Error Message: LWR not match,
    page 15'
  extracted_at: '2026-09-04'
---

**This is LWR not match, not LWR not found.** Not match means the console sees a driver board controller but it is the wrong one. Not found means it sees none at all.

Definition: the driver board controller does not match the console.

Troubleshooting, in order:

1. Check that the **driver board controller number is CS51006-02**.
2. Replace the **upper controller**.

The LCB 2023 and LCR 2023 bikes expect **CS51012** instead. Do not carry that part number to this machine.

**There is a second half to this fault that this manual does not print.** The console's Engineer Mode carries a **Machine Type** setting, and a console set to the wrong model gives the same message. Check Machine Type before replacing the upper controller. The separate LWR Not Match note covers that path.
