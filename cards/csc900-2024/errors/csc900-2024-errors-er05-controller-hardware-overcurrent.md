---
id: csc900-2024-errors-er05-controller-hardware-overcurrent
title: ER05 is a controller hardware over-current, and the burnt motor is checked first
kind: troubleshooting
question: What does ER05 mean on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber says er05
- csc900 console showing er05
- what does er05 mean on a spirit stair climber
keywords:
- er05
- over current
- overcurrent
- controller
- burned motor
- hardware
- stairclimber
- error code
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: er05
  model_number: '900665'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
see_also:
- csc900-2024-errors-error-code-table
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table on printed page
    35. That page is a flat picture with no text layer and was read from the rendered
    page at 500 dpi.
  extracted_at: '2026-09-10'
---

**This is ER05, not ER02, ER07, ER11 or ER12.**

**Condition:** The Console shows ER05.

| Reason | Method |
|---|---|
| Controller hardware overcurrent | 1. Check whether the motor is burned as a priority. 2. Check the controller. |

**The manual says to check the motor "as a priority", before the controller.** An over-current
reported by the controller is usually the load, not the board.

No measurement, no threshold and no part number is printed for either check.

The whole set of this machine's codes is on `csc900-2024-errors-error-code-table`.
