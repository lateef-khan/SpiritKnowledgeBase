---
id: xterra-treadmill-errors-service-manual-error-code-tables-by-book
title: 'The service manuals'' error code tables side by side: the same codes in six
  books, and the two books where the seventh and ninth codes change meaning'
kind: spec
question: What error codes does the service manual list for an Xterra tr150-2021,
  tr260-2023, trx1400-2023, trx2500-2024, trx3500-2024, trx4500-2024 or trx5500-2024
  treadmill?
asked_as:
- xterra service manual error code table
- e9 on xterra treadmill
- which error codes does the trx service manual list
keywords:
- error code items
- error code table
- service manual
- safety key
- rpm signal
- over current
- vr voltage
- communication
- calibration error
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
  - trx5500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-errors-error-code-list-eight-codes
- xt485ent-2023-errors-error-code-list-nine-codes
- f63-2023-error-code-list
- xterra-tr-errors-jkexer-error-messages-e1-e3-e6-and-dashes
see_also:
- xterra-treadmill-errors-owner-checklist-seven-codes-safety-key-to-abnormal-power
- xterra-treadmill-errors-owner-error-messages-seven-codes-incline-printed-three-ways
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TR150 SM 8. Error code items, PDF p. 32 (printed 33); text.md lines 432-461;
    TR260 SM 8-1 Error code items, PDF p. 29; text.md lines 416-436; TRX1400 SM 8.
    Error code items, PDF p. 37 (printed 35); text.md lines 564-591; TRX2500 SM 8.
    Error code items, PDF p. 34 (printed 33); text.md lines 558-586; TRX3500/TRX4500
    SM 8. Error code items, PDF p. 39 (printed 38); text.md lines 604-632; TRX5500
    SM 7-1 Error Codes, PDF p. 31 (printed 30); text.md lines 474-504
  extracted_at: '2026-09-11'
---

Every Dyaco service manual opens its error chapter with an *Error code items* table. Read across the six books:

| Code | TR150 | TR260 | TRX1400 | TRX2500 | TRX3500 / TRX4500 | TRX5500 |
|---|---|---|---|---|---|---|
| E0 | Safety keys dose not insert the safety module. Or safety module is broken | The display appears E0. It means safety key is removed | as TR150 | as TR260 | as TR260 | The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed |
| E1 | Display board CPU did not receive the RPM signal | same, "(Only calibration)" | as TR150 | same, "(only calibration)" | same | same |
| E2 | Over current, over limit current of lower controller and motor | Treadmill motor is overload | as TR150 | Treadmill motor is over load | same | same |
| E3 / Err / ER / ERR | not listed | **E3**: the console board is not detecting the VR voltage value, or the voltage value has exceeded the range | **Err**: same, "or the incline's motor no power" | **ER**: same as TR260 | **ERR**: same | **E3**: same |
| E4 | Power wires of motor error | Treadmill motor wires or volt possible abnormal | as TR150 | as TR260 | same | same |
| E5 | Communication signal error | Communication single is abnormal | as TR150 | as TR260 | same | same |
| E6 | Lower controller error | Lower Control board possible broken | as TR150 | as TR260 | same | same |
| E7 | Input power error | not listed (but the 8-12 check list prints an E7 "Abnormal input voltage" row) | as TR150 | Low volt or abnormal unstable volt | same | **Incline Calibration Error** |
| E9 | Calibration error | not listed | not listed | not listed | not listed | **Speed Calibration Error** |

Two codes change meaning between books. **E7 is an input-power fault everywhere except the TRX5500, where it is an incline calibration error.** **E9 is a general calibration error on the TR150 and a speed calibration error on the TRX5500.** The incline VR fault is one fault printed under four labels.

One card per code per family holds the definition, cause and troubleshooting table: `xterra-treadmill-errors-e0-safety-module-plus-12v-loop`, `xterra-treadmill-errors-e0-safety-key-device-buzzer-test`, `xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`, `xterra-treadmill-errors-e2-over-current-silicone-oil-then-board-or-motor`, `xterra-treadmill-errors-e3-incline-vr-out-of-range`, `trx2500-2024-errors-er-incline-vr-out-of-range`, `xterra-trx-errors-err-incline-vr-out-of-range`, `trx1400-2023-errors-err-or-e3-incline-vr-out-of-range`, `xterra-treadmill-errors-e4-motor-power-wires-not-in-lower-controller`, `xterra-treadmill-errors-e5-console-controller-communication-poor`, `xterra-treadmill-errors-e6-lower-controller-component-fault`, `xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable`, `trx5500-2024-errors-e7-incline-calibration-error`, `tr150-2021-errors-e9-calibration-error-five-causes`, `trx5500-2024-errors-e9-speed-calibration-error`.
