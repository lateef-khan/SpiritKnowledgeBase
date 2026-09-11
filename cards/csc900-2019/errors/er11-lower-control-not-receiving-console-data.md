---
id: csc900-2019-errors-er11-lower-control-not-receiving-console-data
title: ER11 after a normal countdown means the lower control board is not receiving
  the console data
kind: troubleshooting
question: What does ER11 mean on a Spirit csc900-2019 stair climber?
asked_as:
- my climbmill counts down then shows er11
- csc900 er11 wont run
- what does er11 mean on the spirit stair climber
keywords:
- er11
- communication wire
- lower control board
- countdown
- console data
- climbmill
- stair climber
- alternator
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: er11
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2019-errors-er07-safety-switch-connector
- csc900-2019-errors-er12-console-not-receiving-controller-data
- csc900-2019-errors-er22-speed-out-of-control-alternator
- csc880-2025-errors-er03-controller-not-receiving-console-data
see_also:
- csc900-2019-errors-error-code-table
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2019-errors-communication-line-continuity-test
- csc900-2019-errors-er12-console-not-receiving-controller-data
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 1, PDF p. 9; text.md
    lines 291-299
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **This is ER11, not ER12, ER22 or ER07.** The magnetic-system book prints an `ER11` that means the same thing (`csc900-2024-errors-er11-controller-not-receiving-console-data`); the row below is this book's own wording.

**Issue:** When you press start, the countdown is normal, but the machine doesn't work. Display message will show "ER11".

| Analysis | Method |
|---|---|
| The lower control panel doesn't receive the data sent by the console. Explain: 1. Communication wire failure. 2. Lower control board failure. | 1. Check if the communication wire is damaged, replace the communication wire. 2. Replace the lower control board. |

**The countdown is the tell.** The console counts down normally, so the console is alive and has heard the start key; what fails is the message going *down* to the lower control board. ER12 is the same cable heard from the other end (`csc900-2019-errors-er12-console-not-receiving-controller-data`), and that one has a worse symptom - the machine cannot be stopped except by the emergency switch.

**How to test the wire before replacing it** is printed later in the book, under *Determination of defective accessories*: buzz each same-colour conductor end to end with a multimeter, near 0 ohms is good (`csc900-2019-errors-communication-line-continuity-test`).

The CSC880 2025 stair climber numbers this fault `ER03` (`csc880-2025-errors-er03-controller-not-receiving-console-data`). Do not carry that number here.
