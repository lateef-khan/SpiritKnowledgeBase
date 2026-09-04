---
id: f60-2016-e0-error-code
title: 'E0 error: no safety device signal'
kind: troubleshooting
question: What does an E0 error mean on a Sole F60-2016?
asked_as:
- e0 error on my treadmill
- treadmill shows e0 when i pull the key
- what is error e0 on my sole
keywords:
- e0
- e0 error
- safety key
- safety device
- safety switch loop
- 2-pin safety wires
- main control line
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f60-2016-e1-error-code
- f60-2016-incline-er-message
- f60-2016-e2-error-code
- f60-2016-e4-error-code
- f60-2016-e5-error-code
- f60-2016-e6-error-code
see_also:
- f60-2016-error-code-list
- f60-2016-safety-key-continuity-test
- f60-2016-calibration-procedure
source:
  ref: sole-tm-f60-2016-service-manual
  locator: pages 38 to 39, 8.1 Error Message E0
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no speed feedback) and not E2 (over current).**

**Definition**: the display board CPU did not receive the safety device signal.

The lower controller sends a **+12V signal through the S/W line of the main control line** to form a safety switch loop. The safety module sits on that loop and connects to the display board on **2-pin safety wires**.

The troubleshooting form is printed under the heading "PLEASE INSTALL SAFETY KEY TO START".

| Possible cause | Things to check | Solution |
|---|---|---|
| Safety key is loose or unplugged | Check the position of the safety key device | Reset the safety key correctly |
| Bad cable connection | Check all cable connections | Reconnect all cables to make sure they are in good connection |

E0 is also the normal display when the safety key is pulled in idle mode; the calibration procedure starts from exactly that state.
