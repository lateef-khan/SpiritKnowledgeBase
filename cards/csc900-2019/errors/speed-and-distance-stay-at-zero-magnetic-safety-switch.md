---
id: csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch
title: The machine runs but speed and distance stay at zero for 10 to 30 seconds,
  and the magnetic safety switch has shifted or failed
kind: troubleshooting
question: Why does a Spirit csc900-2019 stair climber run with the speed and distance
  stuck at zero?
asked_as:
- climbmill runs but speed says 0
- csc900 distance not counting
- stair climber steps move but nothing counts
keywords:
- speed zero
- distance zero
- magnetic safety switch
- reed switch
- shifted
- no count
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
not_to_be_confused_with:
- csc900-2024-errors-speed-abnormal-then-data-resets
- csc900-2019-errors-er07-safety-switch-connector
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-magnetic-safety-switch-magnet-and-buzzer-test
- csc900-2019-errors-speed-buttons-change-the-display-not-the-speed-blue-feedback-wire
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 5, PDF p. 9; text.md
    lines 322-326
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **No code is printed for this fault.** The console shows zeros while the steps move.

**Issue:** After pressing the button, the machine can run. The speed and distance on the console is 0. There is no change after running for 10-30 seconds.

| Analysis | Method |
|---|---|
| The magnetic safety switch is out of position or the magnetic safety switch is faulty. | 1. Check if the position of the magnetic safety switch is shifted. If it is shifted, repair it. 2. Replace the magnetic safety switch. |

**On this machine the speed is counted by a magnetic switch, not a light sensor.** That is the opposite of the 2022 magnetic-system CSC900 and the CSC880, which read speed optically from a light sensor and a grating and print a different row for it (`csc900-2024-errors-speed-abnormal-then-data-resets`). Do not send a caller with this book looking for a grating.

**Position before part.** The first cause is a switch that has moved, and the fix is to put it back; only a switch that is correctly placed and still reads nothing is replaced. The book prints no gap figure for it.

**The switch can be proved with a magnet and a multimeter** before anything is moved: `csc900-2019-errors-magnetic-safety-switch-magnet-and-buzzer-test`.

This is not the safety switch of `ER07` - that is the emergency stop on the handrail, and it stops the machine rather than the count.
