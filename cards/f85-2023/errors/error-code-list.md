---
id: f85-2023-error-code-list
title: Error codes the service manual lists
kind: spec
question: What error codes can a Sole f85-2023 treadmill show and what does each one
  mean?
asked_as:
- list of error codes for the f85
- what do the e codes mean on my treadmill
- treadmill error code list
keywords:
- error code list
- error codes
- e1
- e2
- e3
- e7
- fault codes
- multi-meter
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2023
  applies_to:
  - f85-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2023-safety-key-message
- f85-2023-e1-no-rpm-signal
- f85-2023-e2-over-current
- f85-2023-e3-incline-vr-voltage
- f85-2023-e4-motor-power-wire
- f85-2023-e5-communication-error
- f85-2023-e6-lower-controller-fault
- f85-2023-e7-input-power-error
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-f85-2023-service-manual
  locator: Section 8 Error Code List, page 32
  extracted_at: '2026-09-04'
---

The manual lists seven numbered codes plus one plain-language message. E1, E2, E3, E4, E5, E6 and E7 are seven different faults; look each one up on its own card.

| Code | Description, as printed |
|---|---|
| PLEASE REPLACE THE SAFETY KEY | The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed. |
| E1 | Display board CPU did not receive the RPM signal. |
| E2 | Over current, over limit current of lower controller and motor. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Power wire of motor error. |
| E5 | Communication signal error. |
| E6 | Lower controller error. |
| E7 | Input power error. |

The only tool the manual asks for is **a multi-meter**.

**There is no E0 in this manual.** The 2023 F65 manual prints E0 for the missing safety key. This console spells the same fault out in words instead.

**There is no E8 in this manual.** The company-wide DC digital controller list carries an E8 for a controller
EEPROM failure, and names the F85 as a machine that uses that controller. This manual does not print it.
