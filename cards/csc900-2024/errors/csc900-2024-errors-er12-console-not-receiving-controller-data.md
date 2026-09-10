---
id: csc900-2024-errors-er12-console-not-receiving-controller-data
title: ER12 means the console is not receiving controller data, and the machine starts but cannot brake
kind: troubleshooting
question: What does ER12 mean on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber says er12
- csc900 wont brake and shows er12
- what does er12 mean on a spirit stair climber
keywords:
- er12
- communication line
- lower control
- can not brake
- multimeter
- conductivity
- stairclimber
- console
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: er12
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er07-emergency-stop-switch-failure
see_also:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-brake-does-not-turn-on
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING, Problem / Reason / Method table on printed page 34. That
    page is a flat picture with no text layer and was read from the rendered page at 500
    dpi.
  extracted_at: '2026-09-10'
---

**This is ER12, not ER11** - and the two are a matched pair pointing in opposite directions.

**Condition:** Press "START" to start, the electronic meter shows ER12 (can not brake).

| Reason | Method |
|---|---|
| The console not receive the controller data. Communication line failure (generally the communication line extrusion damage, you can use a multimeter to measure the upper and lower ends of the conductivity, not conductive is bad.) Lower control failure. | 1. Replace the communication line. 2. Replace the lower control. |

**ER12 is the console not hearing the controller; ER11 is the controller not hearing the console**
(`csc900-2024-errors-er11-controller-not-receiving-console-data`). Same two causes, same two
remedies. The practical difference is what the machine does: ER12 starts but cannot brake, ER11 will
not start at all.

**A machine that starts without a working brake is a safety matter, not only a data fault** - the
brake is what makes the steps resist the user. The manual does not say so, and does not tell the
reader to stop using the machine.

The whole set of this machine's codes is on `csc900-2024-errors-error-code-table`.
