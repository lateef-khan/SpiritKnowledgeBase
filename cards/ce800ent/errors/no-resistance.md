---
id: ce800ent-no-resistance
title: The machine gives no resistance, and the control board is the first part to replace
kind: troubleshooting
question: Why is there no resistance on a Spirit CE800ENT elliptical or CU800ENT-2024 bike?
asked_as:
- no resistance on my spirit elliptical
- pedals feel loose with no load
- elliptical will not add resistance
keywords:
- no resistance
- control board
- generator brake
- resistance voltage wire
- driver ic
- console
- induction brake
- elliptical
- bike
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce800ent
  - cu800ent-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-no-resistance
see_also:
- cvc800-e-2-tension-motor-error
- ces880-2025-errors-no-resistance
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: 'CE800ENT service manual section 7-3 Troubleshooting procedure matrix, page
    27; CU800ENT 2024 owner''s manual TROUBLESHOOTING, printed page 50 (that page is
    a flat picture and was read from the rendered page)'
  extracted_at: '2026-09-08'
---

| Reason | Solve |
|---|---|
| Control board are broken | Replace with new Control board |
| Generator brake resistance voltage wire shedding | Please re-install wire |
| Driver IC broken | Replace the new console |

The CE800ENT elliptical service manual and the CU800ENT 2024 bike owner's manual print this row
word for word. On the bike the whole troubleshooting page is a flat picture with no text layer.

Note the split: the manuals blame the **control board** for the first cause but the **console** for
the third, because the driver IC they name sits in the console.

Both machines brake with a generator and an induction brake rather than a tension motor, so the
tension-motor tests written for the CVC800 climber do not apply here.

**The CES880 2025 elliptical answers the same symptom with a different list** - resistor, then
controller, then console: `ces880-2025-errors-no-resistance`. Do not carry one part order to the
other machine.
