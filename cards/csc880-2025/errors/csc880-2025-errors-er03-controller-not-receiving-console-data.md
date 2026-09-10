---
id: csc880-2025-errors-er03-controller-not-receiving-console-data
title: ER03 means the controller is not receiving data from the console, and the second
  cause is the adapter board
kind: troubleshooting
question: What does ER03 mean on a Spirit CSC880-2025 stair climber?
asked_as:
- my stair climber says er03
- csc880 shows er03
- what does er 03 mean on a spirit stair climber
keywords:
- er03
- wiring harness
- adapter board
- display board
- console
- controller
- communication
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: er03
authority: 3
not_to_be_confused_with:
- csc880-2025-errors-er01-console-not-receiving-controller-data
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
- csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
see_also:
- csc880-2025-errors-error-code-table
- csc880-2025-errors-er01-console-not-receiving-controller-data
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING, row 3 of the No./Problem/Causes/Solution table, printed
    page 33 (PDF page 35), read from the native text layer and confirmed against a
    400 dpi render
  extracted_at: '2026-09-10'
---

**This is ER03, not ER01, ER02, ER04 or ER07.**

**Problem:** Console displays ER03.
**Cause:** The controller cannot receive data from the console.

The manual, word for word:

> 1. If there are problems with the wiring harness, such as pinching or poor contact at the ports,
>    use a multimeter to measure whether the two ends of the wiring harness are conductive, and
>    replace the wiring harness if necessary.
> 2. Display board or adapter board malfunction: Data transmission and reception abnormalities.
>    Replace the console or adapter board.

**ER01 and ER03 are a matched pair pointing in opposite directions** - ER01 is the console not
hearing the controller, ER03 is the controller not hearing the console. Both start with the same
continuity check on the same harness. What differs is the second cause: ER01 condemns the
**controller**, ER03 condemns the **display board or adapter board**, which are in the console.

**This row names an adapter board.** No other Spirit climber troubleshooting table mentions one, and
the manual gives it no part number and no location.

**On the CSC900 2024 stair climber this same fault is `ER11`, not `ER03`**
(`csc900-2024-errors-er11-controller-not-receiving-console-data`), and that book adds that the
machine will not start at all. `ER03` does not exist on the CSC900 2024. The full renumbering is on
`csc880-2025-errors-error-code-table`.
