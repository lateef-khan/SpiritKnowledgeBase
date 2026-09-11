---
id: xterra-treadmill-errors-e4-motor-power-wires-not-in-lower-controller
title: 'E4: the motor power wires are not plugged into the lower controller, on the
  90 or 180 V DC motor supply'
kind: troubleshooting
question: What does E4 mean on an Xterra treadmill, and what does each manual say
  to check?
asked_as:
- e4 on my xterra treadmill
- e4 motor not connected
- motor power wires error e4
keywords:
- e4
- motor power wires
- motor voltage
- m+ m-
- lower controller
- 90dcv
- 180dcv
- replace motor
- upper control board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr200-2021
  - tr260-2023
  - tr300-2021
  - tr65-2023
  - trx1000-2021
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: errors
  code: e4
authority: 3
not_to_be_confused_with:
- xterra-ws-errors-e04-controller-or-motor-abnormal
- f63-2023-e4-error-code
- f85-2019-e4-motor-power-wire-error
see_also:
- xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- spirit-xt-errors-e4-motor-power-wire-not-plugged
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.5 Error Message: E4, PDF p. 53 (printed 52); text.md lines
    897-937; TR150 SM 8.4 Error Message: E4, PDF p. 41; text.md lines 613-650; TR260
    SM 8-7 Error Message: E4, PDF p. 43; text.md lines 652-670; TRX1400 SM 8.5 Error
    Message: E4, PDF p. 54 (printed 53); text.md lines 919-956; TRX3500/TRX4500 SM
    8.5 Error Message: E4, PDF p. 59 (printed 58); text.md lines 942-977; TRX5500
    SM 7-8 Error Message: E4 and Cause of E4, PDF pp. 53-55 (printed 52-54); text.md
    lines 796-833; TR150 OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md
    lines 619-677; TR200 OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md
    lines 648-706; TR260 OM Service Checklist - Diagnosis Guide, PDF p. 20; text.md
    lines 812-870; TRX1000 OM Service Checklist - Diagnosis Guide, PDF p. 18; text.md
    lines 662-720; TR300 OM Error Messages, PDF p. 24 (printed 22); text.md lines
    876-895; TR65 OM Troubleshooting, Error Code Guide, PDF p. 43 (printed 42); text.md
    lines 1431-1464; TRX1400 OM Troubleshooting, Error Code Guide, PDF p. 39 (printed
    38); text.md lines 1285-1305; TRX2500 OM Error Messages, PDF p. 21 (printed 19);
    text.md lines 695-741; TRX3500 OM Error Messages, PDF p. 23 (printed 21); text.md
    lines 818-866; TRX4500 OM Error Messages, PDF p. 24 (printed 22); text.md lines
    901-948; TR150 MCB wiring photo (authority 2), the labels SPD / ''If you have
    speed sensor, then it plugs here'', ''M+ Red lead from drive motor'', ''M- Black
    lead from drive motor''; text.md lines 1-40'
  extracted_at: '2026-09-11'
---

E4 is a motor-wiring fault on every Xterra treadmill that prints it.

*Service manuals (TR150, TR260, TRX1400, TRX2500, TRX3500, TRX4500, TRX5500).* Definition: **Motor power wires error.** The configuration drawing shows the driver board feeding the motor its power - **90 V DC or 180 V DC** - while the console sends start and speed commands and receives the RPM or motor signal over the TX/RX main control wires. Cause: the power wires of the motor are not inserted in the lower controller.

| Part | Troubleshooting |
|---|---|
| Lower controller | Insert power wires of motor |
| Motor | Replace motor |
| Display board | Replace upper control board |

*Owner's manuals*

| Books | Printed meaning |
|---|---|
| TR150, TR200, TR260, TRX1000 | Improper motor input voltage. Motor is not connected properly. - Motor is not connected properly or not connected to the controller |
| TR65 | Improper motor input voltage - Motor is not connected properly or not connected to the controller |
| TR300, TRX2500, TRX3500, TRX4500 | Motor voltage surge or motor is disconnected |
| TRX1400 | Abnormal motor voltage or motor disconnected |

On the TR150 board the motor leads are marked on the photo as **M+ red** and **M- black**. The matrix row for a treadmill that does nothing at START names the same M+ / M- wires (`xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire`). The Spirit XT twin is `spirit-xt-errors-e4-motor-power-wire-not-plugged`.
