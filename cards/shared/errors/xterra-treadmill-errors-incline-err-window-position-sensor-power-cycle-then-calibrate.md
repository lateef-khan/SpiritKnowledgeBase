---
id: xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
title: 'The INCLINE window shows the incline error: the position sensor value is wrong,
  so power-cycle at the AC switch and then calibrate'
kind: troubleshooting
question: What does it mean when the INCLINE window on an Xterra treadmill shows ERR,
  ER or Err, and what does the troubleshooting matrix say to do?
asked_as:
- incline window shows err xterra
- incline err power cycle then calibrate
- position sensor value wrong incline
keywords:
- incline err
- incline window
- position sensor
- incline motor
- ac switch
- power cycle
- calibrate
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- ct850-2020-incline-err
see_also:
- xterra-treadmill-errors-incline-position-does-not-match-console-calibrate
- xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
- xterra-trx-errors-incline-err-no-vr-change-when-incline-runs
- trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
- spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246; TR260 SM 8-13
    Troubleshooting procedure matrix, PDF pp. 51-53; text.md lines 794-900; TRX1400
    SM Troubleshooting procedure matrix, PDF pp. 61-63 (printed 55-57); text.md lines
    1102-1208
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix in four service manuals prints one row for the incline error shown in the INCLINE window. The label follows each book's code:

| Book | Condition as printed |
|---|---|
| TR260 | INCLINE ERR, INCLINE window displays "INCLINE ERR" |
| TRX1400 | INCLINE ERR, INCLINE window displays "Err" |
| TRX2500 | INCLINE ER, INCLINE window displays "ER" |
| TRX3500, TRX4500 | INCLINE ERR, INCLINE window displays "ERR" |

*Reason:* 1. Position sensor value of incline motor is wrong. *Solve:* 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. (The TR260 row prints only the power-cycle step; the calibrate step is on the next line of its table.)

The TR150 matrix has no incline row at all. The row above it in every book, "The incline position doesn't match console - console is not calibrated - calibrate the console", is `xterra-treadmill-errors-incline-position-does-not-match-console-calibrate`. What the code means and the full checks are on the per-code cards: `xterra-treadmill-errors-e3-incline-vr-out-of-range`, `trx2500-2024-errors-er-incline-vr-out-of-range`, `xterra-trx-errors-err-incline-vr-out-of-range`, `trx1400-2023-errors-err-or-e3-incline-vr-out-of-range`.
