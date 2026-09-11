---
id: xterra-tr-errors-owner-error-messages-ls-console-memory-and-incline
title: 'Three error messages on the console that reports lost speed as LS: a memory
  or CPU fault and an incline position error follow it'
kind: spec
question: What do the LS, E1 and E2 error messages mean on an Xterra tr64-2024 or
  tr66-2021 treadmill?
asked_as:
- ls on my xterra treadmill
- tr66 error messages
- tr6.4 e1 e2 meaning
keywords:
- ls
- error messages
- speed signal
- console memory
- cpu
- incline position
- error code list
- lost speed
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr64-2024
  - tr66-2021
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-owner-checklist-seven-codes-safety-key-to-abnormal-power
- sole-ls-error
- f60-2016-ls-message
see_also:
- xterra-tr-errors-ls-no-speed-signal-for-8-seconds
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- xterra-tr-errors-e2-incline-position-error
source:
  ref: xterra-treadmill-tr66-2021-owners-manual
  locator: TR6.6 OM Error Messages, PDF p. 30 (printed 28); text.md lines 1178-1206;
    TR6.4 OM Error Messages, PDF p. 25 (printed 23); text.md lines 919-947
  extracted_at: '2026-09-11'
---

**This code family is different from every other Xterra treadmill's.** The TR6.6 and TR6.4 owner's manuals print three error messages:

| Message | Printed meaning |
|---|---|
| LS | The treadmill hasn't received a speed signal for 8 seconds |
| E1 | Console memory malfunction or CPU problem |
| E2 | Incline position error |

On these two machines **E1 is not a speed fault and E2 is not over current**, which is what those codes mean on every other Xterra treadmill. The lost-speed message is LS. A reader with an E1 on a TR6.6 must not be sent to the RPM-sensor cards.

Detail: `xterra-tr-errors-ls-no-speed-signal-for-8-seconds`, `xterra-tr-errors-e1-console-memory-or-cpu-fault`, `xterra-tr-errors-e2-incline-position-error`. The same page prints the Engineering Mode entry (Start and Speed 5 keys for 5 seconds) and the calibration values (wheel 63, 0.5 to 12.0 mph, incline 15); those are console facts.
