---
id: ct900ent-errors-04h-output-overcurrent
title: '04H: inverter output overcurrent'
kind: troubleshooting
question: What does error code 04H mean on a Spirit ct900ent treadmill?
asked_as:
- what does 04h mean on my spirit treadmill
- treadmill showing 04h
- ct900ent error 04h
keywords:
- 04h
- '0x04'
- output overcurrent
- inverter
- error code
- hex code
- ent
- touch screen
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: errors
  code: 04h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-04h-output-over-current
see_also:
- ct900ent-errors-error-code-messages-list
- ctsbs900-oc-inverter-output-overcurrent
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: CT900ENT service manual Error Code Messages, PDF p. 19, text.md lines 256-288
  extracted_at: '2026-09-11'
---

**This is 04H, and it is not any other code in the same table, and not the CT850's `E-04H` or the CT900's `E` codes.**

| Field | Value |
|---|---|
| Error Code | 04H |
| Description, word for word | Output overcurrent |
| Remarks Error | By Inverter Error |

**The manual prints no cause and no fix for this code.** The table has three columns and none of them is a solution column; the only tool the error chapter names is a multi-meter. Anything beyond the description above would be invention. The CT850 2020 prints the same number with an `E-` in front and an explanation and a solution of its own (`ct850-2020-e-04h-output-over-current`); different machine, different string, and the CT900ENT gives no solution. The CTSBS900 slat-belt treadmill explains the same fault under the inverter's own mnemonic, with a remedy (`ctsbs900-oc-inverter-output-overcurrent`); the CT1000ENT lists that mnemonic against a hex index (`ct1000ent-2023-errors-error-code-list-25-hex-codes`).

The whole table, and the three families it splits into, is on `ct900ent-errors-error-code-messages-list`. The console's Diagnostics screen logs these codes as `0x` values (`cu900ent-error-code-log`).
