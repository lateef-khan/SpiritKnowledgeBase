---
id: cu900ent-40h-unknown-mode
title: '40H: unknown mode'
kind: troubleshooting
question: What does error code 40H mean on a Spirit CU900ENT bike?
asked_as:
- what does 40h mean on my spirit bike
- bike console showing 40h
- spirit upright bike error 40h
keywords:
- 40h
- '0x40'
- unknown mode
- mcu board
- error code
- bike
- lower board
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: errors
  code: 40h
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-41h-inverter-no-response
- cu900ent-42h-bike-board-no-response
- cu900ent-44h-console-i2c-no-response
- cu900ent-50h-abnormal-mcu-firmware-update
- cu900ent-error-code-messages-list
- cu900ent-error-code-log
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Error Code Messages table, page 22
  extracted_at: '2026-09-08'
---

**This is 40H, and it is not any other code in the same table.** `Un-know mode` is the manual's spelling. This is the MCU board reporting a mode it does not recognise.

| Field | Value |
|---|---|
| Error Code | 40H |
| Description, word for word | Un-know mode |
| Remarks Error | By MCU Board Error |

**The manual prints no cause and no fix for this code.** The table has three columns and none of
them is a solution column; the only tool the manual names anywhere in the error section is a
multi-meter. Anything beyond the description above would be invention.

The whole printed table, and what the two families of code mean, is on `cu900ent-error-code-messages-list`.
