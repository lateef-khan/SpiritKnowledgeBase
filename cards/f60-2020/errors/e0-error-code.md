---
id: f60-2020-e0-error-code
title: 'E0 error: safety key removed'
kind: troubleshooting
question: What does an E0 error mean on a Sole F60-2020?
asked_as:
- e0 error on my treadmill
- treadmill shows e0 when i pull the key
- what is error e0 on my sole
keywords:
- e0
- e0 error
- safety key
- safety device signal
- 5-pin main control wires
- safety socket
- tx rx
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2020
  applies_to:
  - f60-2020
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f60-2020-e1-error-code
- f60-2020-e2-error-code
- f60-2020-e3-error-code
- f60-2020-e4-error-code
- f60-2020-e5-error-code
- f60-2020-e6-error-code
see_also:
- f60-2020-error-code-list
- f60-2020-safety-key-continuity-test
- f60-2020-calibration-procedure
source:
  ref: sole-tm-f60-2020-service-manual
  locator: pages 32 to 35, 8.1 Error Message E0
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no RPM signal) and not E6 (lower control board).**

The code list and the error section describe this in two different ways.

- **Code list, page 32**: "The display appears E0. It means safety key is removed."
- **Section 8.1, page 33**: "Display board CPU did not receive the Safety device signal."

The safety key signal is carried on the **TX and RX lines of the 5-pin main control wires**, and the safety pin sits on the console board on a 3-pin connection.

The troubleshooting form is printed under the heading "PLEASE INSTALL SAFETY KEY TO START".

| Possible cause | Things to check | Solution |
|---|---|---|
| Safety key is loose or unplugged | Check the position of the safety key device | Reset the safety key correctly |
| Bad cable connection | Check all cable connections | Reconnect all cables to make sure they are in good connection |

E0 is also the normal display when the key is out, and the calibration procedure begins by removing the key.
