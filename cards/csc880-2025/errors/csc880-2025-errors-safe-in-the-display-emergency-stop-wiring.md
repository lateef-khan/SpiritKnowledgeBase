---
id: csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
title: The word Safe in the display means the machine is stuck in emergency stop mode
  because two lines are swapped
kind: troubleshooting
question: What does Safe in the display mean on a Spirit CSC880-2025 stair climber?
asked_as:
- my stair climber says safe on the screen
- csc880 stuck in emergency stop
- spirit stair climber wont come out of stop mode
- what does safe mean on the stair climber display
keywords:
- safe
- emergency stop mode
- stuck
- handle pulse line
- stop switch wiring
- swapped wires
- reinstall
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: safe
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with:
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc880-2025-errors-no-pulse-data-pulse-cable-insulation
see_also:
- csc880-2025-errors-error-code-table
- csc880-2025-errors-no-pulse-data-pulse-cable-insulation
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, row 11 of the No./Problem/Causes/Solution
    table, printed page 34 (PDF page 36), read from the native text layer and confirmed
    against a 400 dpi render; CSC880 service manual (Magnetic), 5. Troubleshooting,
    "CSC880 electrical malfunction Troubleshooting" table row 11, PDF p. 8 - the page
    is a flat picture (text.md lines 123-128 hold only the heading; OCR supplement
    lines 428-505) and was read from a 200 dpi render
  extracted_at: '2026-09-10'
---

**`Safe` is a word, not a code.** It appears in the display where a code would, and the
troubleshooting table lists it in the Problem column with no `ER` number against it.

**Problem:** Machine is in emergency stop mode, console display "Safe".
**Cause:** Wrong emergency stop switch connection.

> Please check whether the handle pulse line and emergency stop switch line are connected
> incorrectly, and reinstall the emergency stop switch line.

**The named mistake is that the handle pulse line and the emergency stop switch line have been put
in each other's places.** Both connectors reach the same area of the console, and the manual says
the remedy is to reinstall the stop switch line - not to replace anything.

**So this is an assembly or service fault, not a failed part.** Expect it on a machine that has just
been built, moved, or had its console off. A machine that ran correctly for months and then showed
`Safe` has had something disturbed.

**It is not `ER07`.** `ER07` is the stop switch itself failing, or its wire loose, damaged, or in the
wrong sequence, and the console prints the code (`csc900-2024-errors-er07-emergency-stop-switch-failure`).
It is not `ER02` either - that is the separate **infrared** emergency stop beam being broken, and it
clears with a power cycle (`csc880-2025-errors-er02-infrared-emergency-stop-triggered`). This machine
has two emergency stops and three ways of complaining about them.

**Check the pulse readout while you are in there.** The same swap explains a console showing no
pulse data (`csc880-2025-errors-no-pulse-data-pulse-cable-insulation`).

**The CSC900 2024 book prints no `Safe` row.** Do not tell a CSC900 owner to look for it.

**The CSC880 service manual prints this row word for word**, as row 11 of the eleven-row table on its page 8. Owner's manual and service manual carry the same table; the service manual adds nothing to this row.
