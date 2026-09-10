---
id: csc900-2024-errors-membrane-key-failure
title: A key that does not respond is a bad membrane key or a damaged wire
kind: troubleshooting
question: Why does a button not work on a Spirit stair climber console?
asked_as:
- buttons dont work on my stairclimber
- csc900 keypad not responding
- one key on my spirit stair climber is dead
- csc880 buttons not working
keywords:
- membrane key
- keypad
- button
- damaged wire
- console
- replace keys
- stairclimber
- key failure
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - csc880-2025
  - csc900-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-console-does-not-light-up-after-power-on
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
- csc880-2025-errors-error-code-table
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: 'CSC900 2024: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table
    on printed page 35; that page is a flat picture with no text layer and was read from
    the rendered page at 500 dpi. Extended 2026-09-10 with the CSC880 2025 owner''s manual,
    spirit-climber-csc880-2025-owners-manual, TROUBLESHOOTING - CONTINUED row 8 on printed
    page 34 (PDF page 36), read from the native text layer and confirmed against a 400
    dpi render.'
  extracted_at: '2026-09-10'
---

**Condition:** Key Failure.

| Reason | Method |
|---|---|
| Membrane key failure | Bad membrane key or damaged wire. Replace membrane keys. |

Two lines and one part. **The manual names no key test mode** - this console has nothing like the
`Key Test` entry the 2024 ENT consoles carry in their Service menu
(`cu800ent-2024-errors-error-code-log`), so there is no way to prove a key dead from the console
itself.

If no key works and the screen is dark as well, that is the power row instead:
`csc900-2024-errors-console-does-not-light-up-after-power-on`.

## The CSC880 2025 stair climber names a third cause: the cable in backwards

Its row reads `Button Malfunction` / `Membrane key failure`, and the solution adds a case the CSC900
book leaves out:

> The keypad cable is bend or damaged, or is inserted backwards. Replace the membrane keypad.

**A keypad cable can be inserted backwards.** That is a fault you can fix without a part, and it is
worth looking at before ordering a keypad - especially on a machine whose console has just been
opened or replaced. Neither book names a key test mode, so there is still no way to prove a key dead
from the console itself.

If the screen is dark as well, that is the power row instead - and the two machines print
**different voltages** for it, so use the caller's own book:
`csc900-2024-errors-console-does-not-light-up-after-power-on` for the CSC900 2024,
`csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks` for the CSC880 2025.
