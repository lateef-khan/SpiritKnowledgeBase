---
id: xterra-treadmill-errors-stops-immediately-after-start-controller
title: 'The treadmill stops immediately after START is pressed: a broken controller,
  so power-cycle at the AC switch, then replace the controller and calibrate'
kind: troubleshooting
question: Why does an Xterra treadmill start and then stop immediately, and what is
  the fix?
asked_as:
- treadmill stops right after start xterra
- belt starts then stops immediately
- controller broken stops immediately
keywords:
- stops immediately
- start button
- controller broken
- ac switch
- replace controller
- calibrate
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-stops-or-shuts-off-by-itself-breaker-fuse-controller
- xterra-treadmill-errors-e1-owner-checks-8-to-10-seconds-after-start
see_also:
- xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire
- xterra-treadmill-errors-stops-or-shuts-off-by-itself-breaker-fuse-controller
- f65-2023-stops-immediately-after-start
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246; TR150 SM 8.11
    Troubleshooting procedure matrix, PDF pp. 49-50 (printed 57-58); text.md lines
    826-906; TR260 SM 8-13 Troubleshooting procedure matrix, PDF pp. 51-53; text.md
    lines 794-900; TRX1400 SM Troubleshooting procedure matrix, PDF pp. 61-63 (printed
    55-57); text.md lines 1102-1208
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints this row **twice** in every one of the five service manuals, a few lines apart:

*Condition:* After pressing "START" button, the treadmill stops immediately. *Reason:* 1. Controller is broken. *Solve:* 1. Turn off the AC switch and turn on power again. 2. Replace controller and calibrate it.

The second printing reads: *Reason:* Controller was broken. *Solve:* Replace with new controller and calibrate it.

A belt that runs for about ten seconds and then stops with E1 is the speed-sensor fault (`xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`); a belt that never moves at all is `xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire`; a machine that runs for some time and then shuts off is `xterra-treadmill-errors-stops-or-shuts-off-by-itself-breaker-fuse-controller`.
