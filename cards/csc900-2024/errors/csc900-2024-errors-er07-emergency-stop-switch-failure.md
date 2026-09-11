---
id: csc900-2024-errors-er07-emergency-stop-switch-failure
title: ER07 is the emergency stop switch, its wiring, or a wire sequence plugged in
  the wrong order
kind: troubleshooting
question: What does ER07 mean on a Spirit stair climber?
asked_as:
- my stairclimber says er07
- emergency stop error on my csc900
- what does er07 mean on a spirit stair climber
- csc880 shows er07
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
  model: '*'
  applies_to:
  - csc880-2025
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
- csc880-2025-errors-error-code-table
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
- csc900-2019-errors-er07-safety-switch-connector
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: 'CSC900 2024: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table
    on printed page 35; that page is a flat picture with no text layer and was read
    from the rendered page at 500 dpi. Extended 2026-09-10 with the CSC880 2025 owner''s
    manual, spirit-climber-csc880-2025-owners-manual, TROUBLESHOOTING row 5 on printed
    page 33 (PDF page 35), read from the native text layer and confirmed against a
    400 dpi render; CSC900 2022 (Magnetic system) service manual, 6. Troubleshooting,
    Item / Problem / Reason / Method table row 8, PDF p. 10 - the page is a flat picture
    (text.md lines 261-266 hold only the heading; OCR supplement lines 464-536) and
    was read from a 200 dpi render; CSC880 service manual (Magnetic), 5. Troubleshooting,
    "CSC880 electrical malfunction Troubleshooting" table row 5, PDF p. 8 - the page
    is a flat picture (text.md lines 123-128 hold only the heading; OCR supplement
    lines 428-505) and was read from a 200 dpi render'
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

## The CSC880 2025 stair climber prints ER07 for the same fault

**This is the one code the two Spirit stair climbers agree on.** The CSC880 2025 book renumbers
ER11, ER12 and ER05 and adds an ER01 to ER04 of its own, but its `ER07` names the same three causes
as this one - see `csc880-2025-errors-error-code-table` for the whole mapping.

Its wording, word for word:

> 1. Emergency stop switch malfunction
> 2. Loose emergency stop switch connection wire
> 3. Incorrect wire sequence
>
> Check whether the emergency stop switch has been reset, whether the connecting wires are
> incorrectly connected, disconnected, damaged, or whether the emergency stop switch needs to be
> replaced.

**The CSC880 book adds one check the CSC900 book does not: whether the switch has been reset.** Try
that before reaching for a meter.

**The CSC880 has a second, separate emergency stop** - an infrared beam, which reports `ER02` and
clears with a power cycle (`csc880-2025-errors-er02-infrared-emergency-stop-triggered`) - and a third
state in which it sits in stop mode showing the word `Safe` because the stop switch line and the
handle pulse line have been swapped
(`csc880-2025-errors-safe-in-the-display-emergency-stop-wiring`). The CSC900 2024 book prints
neither of those.

**The CSC900 2022 service manual (the magnetic-system book) prints this row word for word**, as row 8 of the ten-row Troubleshooting table on its page 10. The owner's manual and the service manual print the same table; the service manual adds nothing to this row.

The alternator-drive CSC900 (the `V1.0` service manual) prints the same code for the same fault in its own words: `csc900-2019-errors-er07-safety-switch-connector`.

**The CSC880 service manual prints this row word for word**, as row 5 of the eleven-row table on its page 8. Owner's manual and service manual carry the same table; the service manual adds nothing to this row (this is the CSC880 half of the card).
