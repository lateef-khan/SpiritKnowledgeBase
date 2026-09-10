---
id: csc900-2024-errors-er11-controller-not-receiving-console-data
title: ER11 means the controller is not receiving data from the console, and the machine will not start at all
kind: troubleshooting
question: What does ER11 mean on a Spirit CSC900-2024 stairclimber?
asked_as:
- my stairclimber says er11
- csc900 wont start and shows er11
- what does er11 mean on a spirit stair climber
keywords:
- er11
- communication line
- lower control
- console data
- multimeter
- conductivity
- stairclimber
- wont start
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: er11
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er12-console-not-receiving-controller-data
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er07-emergency-stop-switch-failure
see_also:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-er12-console-not-receiving-controller-data
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING, Problem / Reason / Method table on printed page 34. That
    page is a flat picture with no text layer and was read from the rendered page at 500
    dpi.
  extracted_at: '2026-09-10'
---

**This is ER11, not ER12** - and the two are a matched pair pointing in opposite directions.

**Condition:** After pressing "START" the machine does not start, and the electronic meter displays
ER11.

| Reason | Method |
|---|---|
| Controller can not receive the electronic meter data. 1. Communication line failure (generally for the communication line extrusion damage, you can use a multimeter to measure whether the upper and lower ends of the conductivity, not conductive for bad). 2. Lower control failure. | a. Replace the communication line. b. Replace the lower control. |

**ER11 is the controller not hearing the console; ER12 is the console not hearing the controller**
(`csc900-2024-errors-er12-console-not-receiving-controller-data`). The two codes have the same two
causes and the same two remedies, and the manual gives no way to tell from the codes which end of
the cable is at fault. The practical difference is what the machine does: ER11 will not start at
all, ER12 starts but will not brake.

**The test is a continuity check on the communication line, end to end, with a multimeter.** The
manual names no resistance figure - it says only that not conductive is bad.

The whole set of this machine's codes is on `csc900-2024-errors-error-code-table`.
