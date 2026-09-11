---
id: csc900-2024-errors-er02-magnetic-wheel-or-control-board
title: ER02 after pressing START is the magnet wheel wiring or a short-circuited MOS
  on the control board
kind: troubleshooting
question: What does ER02 mean on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber says er02
- csc900 shows er02 when i press start
- what does er02 mean on a spirit stair climber
keywords:
- er02
- magnetic wheel
- magneto wheel
- control board
- mos
- short circuit
- lower control
- stairclimber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: er02
  model_number:
  - '900665'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
see_also:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-brake-does-not-turn-on
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING, Problem / Reason / Method table on printed page 34. That
    page is a flat picture with no text layer and was read from the rendered page
    at 500 dpi; CSC900 2022 (Magnetic system) service manual, 6. Troubleshooting,
    Item / Problem / Reason / Method table row 3, PDF p. 10 - the page is a flat picture
    (text.md lines 261-266 hold only the heading; OCR supplement lines 464-536) and
    was read from a 200 dpi render
  extracted_at: '2026-09-10'
---

**This is ER02, not ER05, ER07, ER11 or ER12.** All five of this machine's codes are written `ER`
and two digits, and no two of them mean the same thing.

**Condition:** After pressing "START" to start, the electronic meter shows ER02.

| Reason | Method |
|---|---|
| Control board failure - MOS short-circuited | Replace the controller |
| The magnetic wheel connection wire is disconnected | Check the magneto wheel and the lower control connection wire, reinsert it |

**Try the wire before the board.** The manual prints the board failure first, but the wire check
costs nothing and the board is the whole controller.

**The manual spells the same part two ways in two cells** - `magnetic wheel` in the reason and
`magneto wheel` in the method. It is one part.

This machine's codes are not shared with any other Spirit product. The whole set is on
`csc900-2024-errors-error-code-table`.

**The CSC900 2022 service manual (the magnetic-system book) prints this row word for word**, as row 3 of the ten-row Troubleshooting table on its page 10. The owner's manual and the service manual print the same table; the service manual adds nothing to this row.
