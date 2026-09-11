---
id: csc900-2019-errors-er07-safety-switch-connector
title: ER07 or a machine that is out of order is the safety switch connector loose
  or the safety switch failed
kind: troubleshooting
question: What does ER07 mean on a Spirit csc900-2019 stair climber?
asked_as:
- climbmill shows er07
- csc900 er07 wont work
- safety switch error on my spirit stair climber
keywords:
- er07
- safety switch
- emergency stop
- connector
- replug
- climbmill
- stair climber
- out of order
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: er07
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2019-errors-er12-console-not-receiving-controller-data
- csc900-2019-errors-er22-speed-out-of-control-alternator
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
see_also:
- csc900-2019-errors-error-code-table
- csc900-2024-errors-er07-emergency-stop-switch-failure
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 4, PDF p. 9; text.md
    lines 319-321
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **This is ER07, not ER11, ER12 or ER22.** The magnetic-system CSC900 and the CSC880 both print an `ER07` for the same part - the emergency stop switch - so this is the one code the three stair climber books agree on (`csc900-2024-errors-er07-emergency-stop-switch-failure`).

**Issue:** The [machine is] out of order or console displays "ER07", the machine doesn't work. (The printed row has a word missing between *The* and *out of order*; it reads that way on the page.)

| Analysis | Method |
|---|---|
| Safety switch connector loosens and falls off, or safety switch failure. | 1. Check the safety switch connector and replug the test. 2. Replace the safety switch. |

**Replug first.** The book's first cause is a connector that has worked loose and fallen off the switch, and its first step is to plug it back and test - no meter, no part. Only a switch that still fails after that is replaced.

This book's safety switch is the emergency stop on the handrail. The **magnetic safety switch** inside the frame is a different part with a different symptom - speed and distance stuck at zero with no code - and its own test (`csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch`).
