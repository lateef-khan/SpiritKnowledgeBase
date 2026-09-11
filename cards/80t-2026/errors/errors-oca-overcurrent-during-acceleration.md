---
id: 80t-2026-errors-oca-overcurrent-during-acceleration
title: ocA on the inverter is overcurrent during acceleration, and the check is the
  inverter-to-motor connections
kind: troubleshooting
question: What does inverter error ocA mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- oca error on treadmill
- overcurrent during acceleration 8.0t
- inverter says oca
- treadmill trips oca when speeding up
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- oca
- overcurrent
- acceleration
- motor terminals
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: oca
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-ocd-overcurrent-during-deceleration
- 80t-2026-errors-ocn-ac-fluctuation-or-impact-load
- 80t-2026-errors-ocbe-unbalanced-three-phase-motor-current
- 80t-2026-errors-oua-overvoltage-during-acceleration-motor-insulation
- ctsbs900-oc-inverter-output-overcurrent
- 70t-2026-errors-e10-over-i-accel
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 03 ocA, PDF p. 20; text.md lines
    245-289
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ocA`, row 03 of the 48-row table** - not `ocd`, `ocn`, `ocbE`, `ouA` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 03. ocA | Overcurrent during acceleration | Check for loose connections between the inverter output and the motor terminals. |

The three `oc` codes are told apart by when the overcurrent happened - accelerating (`ocA`), decelerating (`ocd`) or at constant speed (`ocn`) - and only `ocn` adds a supply-circuit remedy.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

