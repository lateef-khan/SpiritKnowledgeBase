---
id: 80t-2026-errors-ocbe-unbalanced-three-phase-motor-current
title: ocbE on the inverter is an unbalanced three-phase motor output current
kind: troubleshooting
question: What does inverter error ocbE mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- ocbe error on treadmill
- inverter shows ocbe
- unbalanced motor current ocbe
- 8.0t ocbe code
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- ocbe
- unbalanced current
- three-phase
- motor terminals
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: ocbe
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-oca-overcurrent-during-acceleration
- 80t-2026-errors-ocd-overcurrent-during-deceleration
- 80t-2026-errors-ocn-ac-fluctuation-or-impact-load
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 14 ocbE, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ocbE`, row 14 of the 48-row table** - not `ocA`, `ocd`, `ocn` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 14. ocbE | Unbalanced three-phase output current of the motor | Check for loose connections between the inverter output and the motor terminals. |

A three-phase motor drawing unequal current on its three legs is read as a loose leg, so the check is the inverter-to-motor terminals.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

