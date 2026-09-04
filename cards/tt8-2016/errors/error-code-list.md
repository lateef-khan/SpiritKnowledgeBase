---
id: tt8-2016-error-code-list
title: Error code list on the DC controller console
kind: spec
question: What are the error codes on a Sole tt8-2016 treadmill?
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
  model: tt8-2016
  applies_to:
  - tt8-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- tt8-2016-ac-error-code-list
see_also:
- tt8-2016-e1-error-code
- tt8-2016-e2-error-code
- tt8-2016-e3-error-code
- tt8-2016-e4-error-code
- tt8-2016-e5-error-code
- tt8-2016-e6-error-code
- tt8-2016-e7-error-code
source:
  ref: sole-tm-tt8-2016-service-manual
  locator: Error code items, page 37
  extracted_at: '2026-09-04'
---

**DC model: TT8 2016 ST925-YT021, DC drive motor. The AC inverter TT8 2016 (ST925A-YT030) is a different machine and this card does not apply to it.**

| Code | Meaning |
|---|---|
| E0 | Safety keys dose not insert the safety module. Or safety module is broken. |
| E1 | Display board CPU did not receive the RPM signal. |
| E2 | Over current, over limit current of lower controller and motor. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Power wire of motor error. |
| E5 | Communication signal error. |
| E6 | Lower controller error. |
| E7 | Input power error. |

The AC-inverter TT8 2016 (ST925A-YT030) does **not** use this list. Its codes are shaped E-01H to E-53H plus a bare E3, and the same-looking E3 means something else there. Check the drive type before reading a code off this table.

The only tool the manual asks for is a multi-meter.
