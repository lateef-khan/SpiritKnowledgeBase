---
id: 80t-2026-errors-erp2-parameter-write-error-printed-on-two-rows
title: ErP2 on the inverter is a parameter write error printed on two rows of the
  table
kind: troubleshooting
question: What does inverter error ErP2 mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- erp2 error on treadmill
- inverter shows erp2
- parameter write error erp2
- why is erp2 listed twice
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- erp2
- parameter write
- replace inverter
- duplicate row
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: erp2
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-erp0-eeprom-error-replace-the-inverter
- 80t-2026-errors-erp1-parameter-write-error
- 80t-2026-errors-epe1-eeprom-write-error
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 21 ErP2, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ErP2`, row 21 of the 48-row table** - not `ErP0`, `ErP1`, `EPE1` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 21. ErP2 | Parameter write error | Replace the inverter. |

**The table prints `ErP2` twice** - row 21 and row 22 both read `ErP2 - Parameter write error - Replace the inverter`. There is no `ErP3` anywhere in the table; row 22 is a printing duplicate, not a second code. The row sequence goes 19 `ErP0`, 20 `ErP1`, 21 `ErP2`, 22 `ErP2`, 23 `conF`.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

