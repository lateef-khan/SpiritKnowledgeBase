---
id: f63-2026-error-code-list
title: Error code list for the console and controller
kind: spec
question: What are the error codes on a Sole F63-2026?
asked_as:
- list of error codes for my 2026 treadmill
- what do the error codes mean on my sole
- error code chart for the 2026 f63
keywords:
- error code list
- e01
- e22
- e31
- error codes
- fault codes
- console codes
- brushless
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2026
  applies_to:
  - f63-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2026-e3-error-code
- f63-2026-e01-error-code
- f63-2026-e02-error-code
- f63-2026-e03-error-code
- f63-2026-e04-error-code
- f63-2026-e05-error-code
- f63-2026-e06-error-code
- f63-2026-e22-error-code
- f63-2026-e31-error-code
source:
  ref: sole-tm-f63-2026-service-manual
  locator: pages 47 to 48, 7.1 Error Message / Troubleshooting
  extracted_at: '2026-09-04'
---

The 2026 F63 uses a **brushless DC motor and a new controller**, and its error codes are **not** the E0 to E7 set used by the earlier F63. Each code has its own card.

| Code | Defect reason printed in the manual |
|---|---|
| E3 | Incline error, displaying in Incline window |
| E01 | Overload |
| E02 | Hall sensor error |
| E03 | Hardware overcurrent |
| E04 | Phase loss |
| E05 | Undervoltage |
| E06 | Overvoltage |
| E3 | Calibration error |
| E22 | Communication error between upper controller and lower controller |
| E31 | Overheat |

**Two rows in this table are both labelled E3**, one for the incline error and one for the calibration error. They are one code with two printed descriptions; both are covered on the E3 card.

The only tool the manual asks for is a multi-meter.

**Do not read E01 as E1, E02 as E2, or E03 as E3.** They are different faults on this machine.
