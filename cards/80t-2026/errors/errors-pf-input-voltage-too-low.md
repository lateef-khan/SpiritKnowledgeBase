---
id: 80t-2026-errors-pf-input-voltage-too-low
title: PF on the inverter is input voltage too low, checked against the AC supply
  range
kind: troubleshooting
question: What does inverter error PF mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- pf error on treadmill
- inverter shows pf
- input voltage too low 8.0t
- what is pf on the drive
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- pf
- input voltage too low
- ac supply
- undervoltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: pf
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-rler-dc-voltage-too-low-during-operation
- 80t-2026-errors-lu-voltage-drop-or-sudden-overload
- ctsbs900-lp-inverter-low-voltage-warning
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 40 PF, PDF p. 22; text.md lines
    331-358
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `PF`, row 40 of the 48-row table** - not `rLEr`, `Lu` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 40. PF | Input voltage too low | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |

**Same voltage range as `rLEr` and `Hou`** - 100-120 VAC 60 Hz on the 110 VAC model, 200-240 VAC 50 Hz on the 220 VAC model - and `LP`, the row the CTSBS900 uses for low voltage, is printed here as *Not applicable to this model*.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

