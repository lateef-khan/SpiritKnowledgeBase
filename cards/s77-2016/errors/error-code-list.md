---
id: s77-2016-error-code-list
title: The error code list from the service manual
kind: spec
question: What are all the error codes for a Sole S77-2016 treadmill?
asked_as:
- list of error codes for my s77
- what do the e codes mean on my treadmill
- s77 error code chart
keywords:
- error code list
- e0
- e7
- code table
- display board
- lower controller
- treadmill
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2016
  applies_to:
  - s77-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-dc-controller-error-code-list
- s77-2016-controller-led-debugging
source:
  ref: sole-tm-s77-2016-service-manual
  locator: Section 8 Error code items, page 36
  extracted_at: '2026-09-04'
---

This machine uses a DC lower controller, so its codes are the E0 to E7 set. **It has an E0 that most Sole treadmills do not.**

| Code | Explanation, as printed |
|---|---|
| E0 | Safety keys dose not insert the safety module. Or safety module is broken. |
| E1 | Display board CPU did not receive the RPM signal. |
| E2 | Over current, over limit current of lower controller and motor. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Power wire of motor error. |
| E5 | Communication signal error. |
| E6 | Lower controller error. |
| E7 | Input power error. |

**The only tool the manual asks for is a multimeter.**

**These are not the same faults as the company-wide Sole E-code list.** The company-wide list has no E0 and gives E8 as a controller EEPROM fault; this manual has no E8. The E1 to E7 meanings do line up with the company-wide list.
