---
id: 80t-2026-errors-ocd-overcurrent-during-deceleration
title: ocd on the inverter is overcurrent during deceleration, and the check is the
  inverter-to-motor connections
kind: troubleshooting
question: What does inverter error ocd mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- ocd error on treadmill
- overcurrent during deceleration
- inverter says ocd when slowing down
- 8.0t ocd fault
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- ocd
- overcurrent
- deceleration
- motor terminals
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: ocd
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-oca-overcurrent-during-acceleration
- 80t-2026-errors-ocn-ac-fluctuation-or-impact-load
- 80t-2026-errors-ocbe-unbalanced-three-phase-motor-current
- 80t-2026-errors-oud-overvoltage-during-deceleration
- ctsbs900-oc-inverter-output-overcurrent
- 70t-2026-errors-e11-over-i-decel
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 04 ocd, PDF p. 20; text.md lines
    245-289
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ocd`, row 04 of the 48-row table** - not `ocA`, `ocn`, `ocbE`, `oud` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 04. ocd | Overcurrent during deceleration | Check for loose connections between the inverter output and the motor terminals. |

The three `oc` codes are told apart by when the overcurrent happened - accelerating (`ocA`), decelerating (`ocd`) or at constant speed (`ocn`) - and only `ocn` adds a supply-circuit remedy.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

