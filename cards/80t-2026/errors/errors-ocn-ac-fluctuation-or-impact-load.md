---
id: 80t-2026-errors-ocn-ac-fluctuation-or-impact-load
title: ocn on the inverter is a sudden AC supply fluctuation or an impact load, and
  it wants a dedicated 20 amp or 15 amp circuit
kind: troubleshooting
question: What does inverter error ocn mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- ocn code on treadmill inverter
- ocn error 8.0t
- treadmill overcurrent at constant speed ocn
- does the 8.0t need a dedicated circuit
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- ocn
- overcurrent
- dedicated circuit
- impact load
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: ocn
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-oca-overcurrent-during-acceleration
- 80t-2026-errors-ocd-overcurrent-during-deceleration
- 80t-2026-errors-ocbe-unbalanced-three-phase-motor-current
- 80t-2026-errors-oun-overvoltage-at-constant-speed
- ctsbs900-oc-inverter-output-overcurrent
- 70t-2026-errors-e9-over-i-speed
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 05 ocn, PDF p. 20; text.md lines
    245-289
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `ocn`, row 05 of the 48-row table** - not `ocA`, `ocd`, `ocbE`, `oun` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 05. ocn | Sudden fluctuation in AC supply voltage | Ensure the equipment is used in an environment with stable AC mains voltage. For the 110 VAC model connect to a 20A dedicated AC power circuit; for the 220 VAC model connect to a 15A dedicated AC power circuit. Avoid sharing the power source with other electrical devices. |
| Inverter | 05. ocn | Impact load causing abrupt current variation | Check the load on transmission components related to the drive belt operation. |

**This is the one row that prints a circuit rating**: a dedicated 20 A circuit on the 110 VAC model, a dedicated 15 A circuit on the 220 VAC model, with nothing else on it. The second cause, an impact load, gets the transmission load check.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

