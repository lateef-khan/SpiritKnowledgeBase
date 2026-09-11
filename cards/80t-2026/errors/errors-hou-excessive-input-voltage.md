---
id: 80t-2026-errors-hou-excessive-input-voltage
title: Hou on the inverter is excessive input voltage, checked against the AC supply
  range
kind: troubleshooting
question: What does inverter error Hou mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- hou error on treadmill
- inverter shows hou
- treadmill input voltage too high hou
- 8.0t hou code
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- hou
- overvoltage
- input voltage
- ac supply
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: hou
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-hoc1-output-short-loose-wiring-or-poor-grounding
- 80t-2026-errors-hoc3-short-circuit-at-the-output
- 80t-2026-errors-oua-overvoltage-during-acceleration-motor-insulation
- ctsbs900-oe-inverter-overvoltage
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 12 Hou, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `Hou`, row 12 of the 48-row table** - not `Hoc1`, `Hoc3`, `ouA` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 12. Hou | Excessive input voltage | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |

**Same voltage range as `rLEr` and `PF`** - 100-120 VAC 60 Hz on the 110 VAC model, 200-240 VAC 50 Hz on the 220 VAC model - measured at both the treadmill inlet and the inverter.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

