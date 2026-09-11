---
id: xterra-tr-errors-e1-console-memory-or-cpu-fault
title: 'E1: console memory malfunction or a CPU problem, on the console that reports
  lost speed as LS'
kind: definition
question: What does E1 mean on an Xterra tr64-2024 or tr66-2021 treadmill?
asked_as:
- e1 on my tr66
- tr6.4 e1 console memory
- xterra e1 cpu problem
keywords:
- e1
- console memory
- cpu
- malfunction
- console
- error messages
- owner's manual
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr64-2024
  - tr66-2021
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-owner-checks-8-to-10-seconds-after-start
- xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
- f63-2023-e1-error-code
see_also:
- xterra-tr-errors-owner-error-messages-ls-console-memory-and-incline
- xterra-tr-errors-ls-no-speed-signal-for-8-seconds
source:
  ref: xterra-treadmill-tr66-2021-owners-manual
  locator: TR6.6 OM Error Messages, PDF p. 30 (printed 28); text.md lines 1178-1206;
    TR6.4 OM Error Messages, PDF p. 25 (printed 23); text.md lines 919-947
  extracted_at: '2026-09-11'
---

**On the TR6.6 and TR6.4, E1 is a console fault, not a speed fault.** The owner's manuals print: **E1: Console memory malfunction or CPU problem.** No remedy is printed against it; the book's general instruction for a fault it cannot resolve is to contact service.

Lost speed on these machines is LS (`xterra-tr-errors-ls-no-speed-signal-for-8-seconds`). On every other Xterra treadmill E1 is the lost-speed code (`xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`, `xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit`), so a reader who searches "E1" with a TR6.6 must not be sent to the RPM sensor. Neither machine has a service manual in the knowledge base.
