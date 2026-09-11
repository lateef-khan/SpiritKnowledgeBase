---
id: spirit-xt-2015-errors-incline-window-shows-e3-power-cycle-then-calibrate
title: E3 in the incline window, on the matrix row that power-cycles and then calibrates
kind: troubleshooting
question: What do I do when the incline window shows E3 on a Spirit XT185 2015 or
  XT285 2015 treadmill?
asked_as:
- e3 in the incline window on my spirit treadmill
- incline err e3
- how to clear e3 incline error
keywords:
- e3
- incline err
- incline window
- position sensor
- power cycle
- calibrate
- incline motor
- vr
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt285-2015
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate
- ct850-2016-incline-err-shown-in-incline-window
see_also:
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- spirit-xt-2015-errors-e3-incline-err-during-incline-action
source:
  ref: spirit-treadmill-xt285-2015-service-manual
  locator: XT185 2015 service manual Troubleshooting procedure matrix, PDF p. 60-62
    (printed 55-57), text.md lines 1119-1221; XT285 2015 service manual Troubleshooting
    procedure matrix, PDF p. 61-63 (printed 55-57), text.md lines 1189-1291
  extracted_at: '2026-09-11'
---

This is the one-line matrix row, printed `INCLINE ERR, INCLINE window displays "E3"`.

| Reason | Solve |
|---|---|
| Position sensor value of incline motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

The 2015 XT185 and XT285 service manuals print it identically - one cause, a power cycle, then calibration. The 2015 XT385 and XT485 and the 2023 XT books check a connector first instead (`spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate`). The CT850 and CT800 books print this power-cycle version for the message `INCLINE ERR` (`ct850-2016-incline-err-shown-in-incline-window`).

The full E3 sections for these two machines are `spirit-xt-2015-errors-e3-incline-vr-out-of-range` and `spirit-xt-2015-errors-e3-incline-err-during-incline-action`.
