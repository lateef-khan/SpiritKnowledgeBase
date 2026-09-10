---
id: csc900-2024-errors-er07-emergency-stop-switch-failure
title: ER07 is the emergency stop switch, its wiring, or a wire sequence plugged in the wrong order
kind: troubleshooting
question: What does ER07 mean on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber says er07
- emergency stop error on my csc900
- what does er07 mean on a spirit stair climber
keywords:
- er07
- emergency stop
- stop switch
- wire sequence
- loose wire
- connection wire
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
  code: er07
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
- ct850-2020-e-25h-emergency-stop-warning
see_also:
- csc900-2024-errors-error-code-table
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table on printed page
    35. That page is a flat picture with no text layer and was read from the rendered
    page at 500 dpi.
  extracted_at: '2026-09-10'
---

**This is ER07, not ER02, ER05, ER11 or ER12.**

**Condition:** Emergency stop switch failure, or ER07 is displayed. The manual prints the symptom and
the code as one condition, so a machine that simply will not run from the stop switch and a machine
showing ER07 get the same answer.

| Reason | Method |
|---|---|
| The emergency stop switch is faulty, or the emergency stop switch connection wire is loose or the wire sequence is wrong | Check if the connection wire is wrongly plugged and damaged, or replace the emergency stop switch |

**"The wire sequence is wrong" is the cause worth reading twice.** It says the connector can be
plugged in an order that looks seated and is not correct, so a wire that is *present* is not
evidence the fault is elsewhere.

The whole set of this machine's codes is on `csc900-2024-errors-error-code-table`.
