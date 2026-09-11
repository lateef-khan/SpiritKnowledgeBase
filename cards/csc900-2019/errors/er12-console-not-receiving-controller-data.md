---
id: csc900-2019-errors-er12-console-not-receiving-controller-data
title: ER12 after a normal countdown means the console cannot receive the controller
  data, and only the emergency switch will stop the machine
kind: troubleshooting
question: What does ER12 mean on a Spirit csc900-2019 stair climber?
asked_as:
- climbmill shows er12 and wont stop
- csc900 er12 after countdown
- what does er12 mean on a spirit stair climber
keywords:
- er12
- communication wire
- lower control board
- cannot stop
- emergency switch
- controller data
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
  code: er12
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2019-errors-er07-safety-switch-connector
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2019-errors-er22-speed-out-of-control-alternator
- csc880-2025-errors-er01-console-not-receiving-controller-data
see_also:
- csc900-2019-errors-error-code-table
- csc900-2024-errors-er12-console-not-receiving-controller-data
- csc900-2019-errors-communication-line-continuity-test
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 2, PDF p. 9; text.md
    lines 300-308
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **This is ER12, not ER11.** The magnetic-system book's `ER12` means the same fault (`csc900-2024-errors-er12-console-not-receiving-controller-data`); this is the alternator book's own row.

**Issue:** When you press start, the countdown is normal, but the machine doesn't work, display message will show "ER12". **The machine cannot be stopped except pulling the emergency switch.**

| Analysis | Method |
|---|---|
| Console cannot receive the controller data. Explain: 1. Communication wire failure. 2. Lower control board failure. | 1. Check if the communication wire is extruded or disconnected, replace the communication wire. 2. Replace the lower control board. |

**Same two causes and same two remedies as ER11**, pointing the other way along the same cable: ER11 is the lower board not hearing the console, ER12 is the console not hearing the lower board. What separates them on the floor is the stop behaviour - **with ER12 the stop key does nothing, and the emergency switch is the only way to halt the steps.** Treat a machine showing ER12 as one that must not be used until the cable or the board is replaced; the manual does not say so in words, but it says the machine will not stop.

"Extruded" is the book's word for a cable that has been crushed or pinched in the mast; the continuity test for it is `csc900-2019-errors-communication-line-continuity-test`.

On the CSC880 2025 the same fault is `ER01` (`csc880-2025-errors-er01-console-not-receiving-controller-data`).
