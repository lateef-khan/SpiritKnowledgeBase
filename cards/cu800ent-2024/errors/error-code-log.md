---
id: cu800ent-2024-errors-error-code-log
title: Error Code Log records faults while the machine runs, and it sits under Service
  in the maintenance menu
kind: procedure
question: Where do I find the logged error codes on a Spirit CU800ENT-2024 bike?
asked_as:
- where is the error log on my spirit upright bike
- how do i see past faults on the touchscreen
- diagnostics screen on a cu800ent
keywords:
- error code log
- diagnostics
- maintenance mode
- service menu
- fault history
- hello guest
- console
- technician
facets:
  brand:
  - spirit
  product_line: bike
  model: cu800ent-2024
  applies_to:
  - cu800ent-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-error-code-log
- ce800ent-error-code-log
see_also:
- cu900ent-error-code-log
- ce800ent-error-code-log
- ce800ent-e5-console-controller-communication
source:
  ref: spirit-bike-cu800ent-2024-owners-manual
  locator: ENGINEERING MODE MENU, printed page 47
  extracted_at: '2026-09-09'
---

**Enter maintenance mode from the Login page by pressing `Hello Guest` ten times.** `Error Code
Log` is then an entry under **Service**, alongside Key Test, Information, PWM Test and Ethernet
Setup.

The whole of what this manual says about the log:

> Records the error code on machine during running

**No worked example, no code list and no way to clear it is printed.** The only code this manual
documents anywhere is `E5` - `ce800ent-e5-console-controller-communication`.

Two sibling consoles put the same log somewhere else and say more about it, so do not carry a
menu path across:

- The **CU900ENT** bike reaches engineering mode by pressing `Home` ten times and puts the log
  under **Diagnostics**, and it *does* give a clearing instruction - press the `Error Code Log`
  button ten times in a row. See `cu900ent-error-code-log`.
- The **CE800ENT** elliptical also uses `Home` ten times and **Diagnostics**, and prints a
  screenshot of the log, but gives no way to clear it. See `ce800ent-error-code-log`.
