---
id: csc900-2019-errors-speed-buttons-change-the-display-not-the-speed-blue-feedback-wire
title: The speed keys change the number on the console but not the actual step speed,
  and the check is the blue motor feedback wire
kind: troubleshooting
question: Why do the speed plus and minus keys on a Spirit csc900-2019 stair climber
  change the display without changing the real speed?
asked_as:
- climbmill speed display changes but steps dont speed up
- csc900 speed buttons do nothing to the steps
- stair climber speed setting ignored
keywords:
- speed keys
- display changes
- actual speed
- motor signal feedback
- blue wire
- feedback line
- climbmill
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: no-code
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with: []
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 6, PDF p. 9; text.md
    lines 327-331
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **No code is printed for this fault.**

**Issue:** The machine can be started normally. Press the speed plus or minus button to increase the display without changing the actual running speed.

| Analysis | Method |
|---|---|
| Motor signal feedback wire is badly contacted or comes off. | Check the motor signal feedback line (blue). |

**One wire, and the book names its colour.** The console sends a speed command and expects a feedback signal back from the motor side; when the **blue** feedback line is loose or off, the console still shows the number you asked for, but nothing closes the loop and the steps keep their pace. The whole remedy is to find that blue wire and reseat it - the manual names no part to replace.

**A display that changes with no effect on the steps is this row. A display stuck at zero while the steps move is a different one** - the magnetic safety switch, `csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch`.
