---
id: 80t-2026-errors-erp1-parameter-write-error
title: ErP1 on the inverter is a parameter write error, and the only fix printed is
  a new inverter
kind: troubleshooting
question: What does inverter error ErP1 mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- erp1 error on treadmill
- inverter shows erp1
- parameter write error erp1
- what is erp1
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- erp1
- parameter write
- replace inverter
- memory error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: erp1
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-erp0-eeprom-error-replace-the-inverter
- 80t-2026-errors-erp2-parameter-write-error-printed-on-two-rows
- 80t-2026-errors-epe1-eeprom-write-error
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 20 ErP1, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ErP1`, row 20 of the 48-row table** - not `ErP0`, `ErP2`, `EPE1` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 20. ErP1 | Parameter write error | Replace the inverter. |

Row 21 and row 22 both print `ErP2` next to it; see that card for the duplicate. `ErP0` is the EEPROM error and `EPE1` the EEPROM *write* error, all with the same one-line fix.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

