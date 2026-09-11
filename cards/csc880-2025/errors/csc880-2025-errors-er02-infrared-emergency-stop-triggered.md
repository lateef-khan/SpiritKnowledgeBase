---
id: csc880-2025-errors-er02-infrared-emergency-stop-triggered
title: ER02 is the infrared emergency stop switch shutting the machine down, and the
  fix is a power cycle
kind: troubleshooting
question: What does ER02 mean on a Spirit CSC880-2025 stair climber?
asked_as:
- my stair climber says er02
- csc880 shows er02
- stair climber shut down and shows er 02
- what triggers the infrared switch on a spirit stair climber
keywords:
- er02
- infrared
- emergency stop
- shut down
- protection
- power cycle
- stair climber
- ir sensor
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: er02
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc880-2025-errors-er01-console-not-receiving-controller-data
- csc880-2025-errors-er03-controller-not-receiving-console-data
- csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
- csc900-2024-errors-er07-emergency-stop-switch-failure
see_also:
- csc880-2025-errors-error-code-table
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING, row 2 of the No./Problem/Causes/Solution table, printed
    page 33 (PDF page 35), read from the native text layer and confirmed against a
    400 dpi render; CSC880 service manual (Magnetic), 5. Troubleshooting, "CSC880
    electrical malfunction Troubleshooting" table row 2, PDF p. 8 - the page is a
    flat picture (text.md lines 123-128 hold only the heading; OCR supplement lines
    428-505) and was read from a 200 dpi render
  extracted_at: '2026-09-10'
---

**Read this first. `ER02` means something completely different on the other Spirit stair climber.**
On the CSC900 2024 it is the magnet wheel wiring or a short-circuited MOS on the control board
(`csc900-2024-errors-er02-magnetic-wheel-or-control-board`) - a parts job. Here it is a safety
switch doing its job, and the machine is not broken. Establish which machine the caller has before
you answer.

**Problem:** Console displays ER02.
**Cause:** Trigger infrared emergency stop switch.

The manual, word for word:

> The machine triggers the infrared emergency stop switch, causing the machine to shut down for
> protection. Turn off the power and then turn it back on again.

**This is the only row in the table whose remedy is not a measurement or a part.** The switch is an
infrared beam, so what tripped it is something that broke the beam - a user stepping off, or an
obstruction. The manual names no beam position, no reset button and no way to test the switch, and
it does not say to investigate what interrupted it.

`ER07` is the *other* emergency stop on this machine - the physical switch and its wiring
(`csc900-2024-errors-er07-emergency-stop-switch-failure`). A machine stuck in stop mode showing the
word `Safe` instead of a code is a third thing:
`csc880-2025-errors-safe-in-the-display-emergency-stop-wiring`.

**The CSC880 service manual prints this row word for word**, as row 2 of the eleven-row table on its page 8. Owner's manual and service manual carry the same table; the service manual adds nothing to this row.
