---
id: xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
title: 'E7: the incoming mains supply is too low, too high or unstable, checked with
  a meter on the wall outlet'
kind: troubleshooting
question: What does E7 mean on an Xterra treadmill, and what does each manual say
  to check?
asked_as:
- e7 on my xterra treadmill
- e7 abnormal power input
- treadmill e7 voltage
keywords:
- e7
- input power
- wall outlet
- unstable voltage
- 110v
- 220v
- multi-meter
- ac 1000v
- lower controller
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr200-2021
  - tr260-2023
  - tr65-2023
  - trx1000-2021
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- trx5500-2024-errors-e7-incline-calibration-error
- xterra-ws-errors-e07-safety-lock-not-in-place
- f63-2023-e7-error-code
see_also:
- xterra-treadmill-errors-e6-lower-controller-component-fault
- xterra-trx-errors-popping-sound-at-power-on-check-220-v
- spirit-xt-errors-e7-input-power-unstable
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.8 Error Message: E7, PDF p. 56 (printed 55); text.md lines
    1010-1036; TR150 SM 8.7 Error Message: E7, PDF p. 44; text.md lines 724-766; TRX1400
    SM 8.8 Error Message: E7, PDF p. 57 (printed 56); text.md lines 1031-1073; TRX3500/TRX4500
    SM 8.8 Error Message: E7, PDF p. 62 (printed 61); text.md lines 1051-1077; TR260
    SM 8-12 Err code troubleshooting check list, PDF pp. 48-50; text.md lines 738-794;
    TR150 OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md lines 619-677;
    TR200 OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md lines 648-706;
    TR260 OM Service Checklist - Diagnosis Guide, PDF p. 20; text.md lines 812-870;
    TRX1000 OM Service Checklist - Diagnosis Guide, PDF p. 18; text.md lines 662-720;
    TR65 OM Troubleshooting, Error Code Guide, PDF p. 43 (printed 42); text.md lines
    1431-1464'
  extracted_at: '2026-09-11'
---

**This is E7 on every Xterra treadmill that prints it except the TRX5500, where E7 is an incline calibration error** (`trx5500-2024-errors-e7-incline-calibration-error`).

*Service manuals (TR150, TRX1400, TRX2500, TRX3500, TRX4500).* Definition: input power anomaly, possibly too low or too high or unstable. The configuration drawing runs from the wall outlet (AC 110 V or AC 220 V) through the overload protection and power switch into the lower controller, with a "CE part or 220 V to match filter and choke" on the 220 V build. Cause: the wall outlet is possibly unstable, so the treadmill's working power is not stable; or the power section of the lower controller board is broken.

| Part | Troubleshooting |
|---|---|
| Wall outlet | Use a multi-meter switched to the AC 1000 V range to check whether the wall outlet is 110 V AC or 220 V AC, and whether the voltage is stable |
| Lower controller board | Replace lower controller board |

The TR260 service manual has no E7 section and its code table stops at E6, but its check list prints an E7 row: abnormal input voltage - check the input voltage fulfils the requirement; check the switch light is on after turning on and the power is normal (`tr260-2023-errors-err-code-troubleshooting-check-list`).

*Owner's manuals.* TR150, TR200, TR260, TRX1000 and TR65: **Abnormal Power Input - Check for proper voltage input for treadmill.** The TR300, TRX1400, TRX2500, TRX3500 and TRX4500 owner's manuals print no E7; their E6 "Power malfunction" line is the closest (`xterra-treadmill-errors-e6-lower-controller-component-fault`).
