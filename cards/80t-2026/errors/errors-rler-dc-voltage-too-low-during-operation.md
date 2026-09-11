---
id: 80t-2026-errors-rler-dc-voltage-too-low-during-operation
title: rLEr on the inverter is DC voltage too low during operation, checked at the
  AC supply range
kind: troubleshooting
question: What does inverter error rLEr mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- treadmill shows rler
- rler code on the inverter
- 8.0t drive says dc voltage too low
- medical treadmill rler error
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- rler
- dc voltage too low
- ac input voltage
- undervoltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: rler
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-lu-voltage-drop-or-sudden-overload
- 80t-2026-errors-pf-input-voltage-too-low
- 70t-2026-errors-e36-lv-bus-run
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 01 rLEr, PDF p. 20; text.md lines
    245-289
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `rLEr`, row 01 of the 48-row table** - not `Lu`, `PF` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 01. rLEr | DC voltage too low during operation | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |

**The voltage figures are the book's own.** 100-120 VAC at 60 Hz for the 110 VAC model, 200-240 VAC at 50 Hz for the 220 VAC model - measured at both the treadmill inlet and the inverter. The same range is the answer to `Hou` (too high) and `PF` (too low): all three send you to the wall before the drive.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.

