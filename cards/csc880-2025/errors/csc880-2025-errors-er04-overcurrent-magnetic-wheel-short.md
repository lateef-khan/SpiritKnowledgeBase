---
id: csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
title: ER04 is an over-current, and the manual says a shorted magnetic control wheel
  is most likely
kind: troubleshooting
question: What does ER04 mean on a Spirit CSC880-2025 stair climber?
asked_as:
- my stair climber says er04
- csc880 shows er04
- stair climber overcurrent error
- what does er 04 mean on a spirit stair climber
keywords:
- er04
- overcurrent
- over current
- magnetic control wheel
- short circuit
- controller
- power adapter
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: er04
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc880-2025-errors-er01-console-not-receiving-controller-data
- csc880-2025-errors-er03-controller-not-receiving-console-data
see_also:
- csc880-2025-errors-error-code-table
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING, row 4 of the No./Problem/Causes/Solution table, printed
    page 33 (PDF page 35), read from the native text layer and confirmed against a
    400 dpi render
  extracted_at: '2026-09-10'
---

**This is ER04, not ER01, ER02, ER03 or ER07.**

**Problem:** Console displays ER04.
**Cause:** Overcurrent protection, excessive current.

The manual, word for word:

> 1. Magnetic control wheel short circuit: After turning off the power, unplug the magnetic control
>    wheel connection cable, turn on the power again, and restart. If no error is reported, it means
>    that the magnetic control wheel is short-circuited and needs to be replaced.
> 2. Controller malfunction: The controller hardware is short-circuited and needs to be replaced.
> 3. Power adapter failure: Replace the adapter. Start troubleshooting from step 1.
>
> A magnetic control wheel short circuit is most likely.

**Step 1 is a substitution test, not a measurement.** Unplug the magnetic control wheel, power up
again, and see whether the code comes back. If it does not, the wheel is the fault. No multimeter
reading is given for any of the three steps.

**The manual names its own most likely cause**, which no other row in this table does. Start at the
wheel.

**On the CSC900 2024 stair climber the over-current code is `ER05`, not `ER04`**
(`csc900-2024-errors-er05-controller-hardware-overcurrent`), and that book blames the controller
hardware and tells you to check whether the motor is burned first - it does not mention the magnetic
control wheel in that row at all. It puts the wheel under `ER02` instead
(`csc900-2024-errors-er02-magnetic-wheel-or-control-board`). Two books, two numbers, two different
first suspects. The full renumbering is on `csc880-2025-errors-error-code-table`.
