---
id: csc900-2024-errors-console-does-not-light-up-after-power-on
title: The console does not light after power on, and four measurements take you from
  the adapter to the console
kind: troubleshooting
question: Why will the console not light up on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber console is dead
- csc900 screen wont turn on
- no power to my spirit stair climber display
keywords:
- console does not light
- power adapter
- 24v
- controller
- connection wire
- multimeter
- stairclimber
- dead console
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: no-code
  model_number:
  - '900665'
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- ces880-2025-errors-lcd-screen-does-not-display-anything
see_also:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-membrane-key-failure
- ces880-2025-errors-lcd-screen-does-not-display-anything
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table on printed
    page 35. That page is a flat picture with no text layer and was read from the
    rendered page at 500 dpi; CSC900 2022 (Magnetic system) service manual, 6. Troubleshooting,
    Item / Problem / Reason / Method table row 7, PDF p. 10 - the page is a flat picture
    (text.md lines 261-266 hold only the heading; OCR supplement lines 464-536) and
    was read from a 200 dpi render
  extracted_at: '2026-09-10'
---

**Condition:** After power on, the console does not light up.

| Reason | Method |
|---|---|
| 1. Power adapter failure. 2. Controller failure. 3. Faulty connection wire. 4. Console failure. | Measure with a multimeter and exclude in turn: 1. measure whether the adapter has **24V** output; 2. measure whether the lower control has **24V** input and voltage output at the plug of the control line; 3. measure whether the communication line is on at both ends and whether there is power output. |

**Four causes, three measurements.** The manual lists the console as the fourth cause and gives it no
measurement - it is what is left when the other three pass.

**This machine runs on a 24 V external power adapter**, not on a mains supply into the frame. That
is why every figure in this row is 24 V and none of them is a mains voltage. Do not carry the
110-120 V checks written for the mains-powered Spirit consoles onto this machine.

If the screen lights but a button does not work, that is the key row:
`csc900-2024-errors-membrane-key-failure`.

**The CSC900 2022 service manual (the magnetic-system book) prints this row word for word**, as row 7 of the ten-row Troubleshooting table on its page 10. The owner's manual and the service manual print the same table; the service manual adds nothing to this row.
