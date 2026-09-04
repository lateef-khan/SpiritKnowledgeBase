---
id: tt8-2023-error-code-list
title: Error code list on the DC controller console
kind: spec
question: What are the error codes on a Sole tt8-2023 treadmill?
asked_as:
- list of error codes for my treadmill
- what do the e codes mean on the console
- sole treadmill error code chart
keywords:
- error code list
- e1
- e3
- e7
- dc controller
- fault code
- console message
- troubleshooting
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2023
  applies_to:
  - tt8-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- tt8-2023-e1-error-code
- tt8-2023-e2-error-code
- tt8-2023-e3-error-code
- tt8-2023-e4-error-code
- tt8-2023-e5-error-code
- tt8-2023-e6-error-code
- tt8-2023-e7-error-code
source:
  ref: sole-tm-tt8-2023-service-manual
  locator: Error Code List, page 34 of 69
  extracted_at: '2026-09-04'
---

**TT8 2023 ST738-YT066, DC drive motor.**

| Code | Meaning |
|---|---|
| PLEASE REPLACE THE SAFETY KEY | The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed. |
| E1 | Display board CPU did not receive the RPM signal. |
| E2 | Over current, over limit current of lower controller and motor. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Power wire of motor error. |
| E5 | Communication signal error. |
| E6 | Lower controller error. |
| E7 | Input power error. |

There is no E0 on this machine. Where the older TT8 manuals show **E0** for a missing safety key, this console prints the words **PLEASE REPLACE THE SAFETY KEY** instead.

The only tool the manual asks for is a multi-meter.
