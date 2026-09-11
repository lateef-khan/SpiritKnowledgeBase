---
id: xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
title: 'E1: the display board got no RPM signal, a fault that is only raised during
  calibration, and the three-row form with the 8-second and 3 mm figures'
kind: troubleshooting
question: What does E1 mean on an Xterra tr150-2021, tr260-2023, trx1400-2023, trx2500-2024,
  trx3500-2024, trx4500-2024 or trx5500-2024 treadmill according to the service manual?
asked_as:
- e1 on my xterra treadmill during calibration
- belt does not move and console shows e1
- xterra e1 rpm signal
keywords:
- e1
- rpm signal
- rpm sensor
- speed sensor
- calibration
- lost speed
- 8 seconds
- 3 mm
- 5-pin main wires
- tx rx
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
  code: e1
authority: 3
not_to_be_confused_with:
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
- xterra-ws-errors-e01-poor-communication
- f63-2023-e1-error-code
- f85-2019-e1-no-rpm-signal
see_also:
- xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- trx5500-2024-errors-e1-lost-speed-console-has-no-speed-sensor-fitted
- xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.2 Error Message: E1 and Cause of E1, PDF pp. 40-41 (printed
    39-40); text.md lines 664-693; TRX2500 SM E1 issue troubleshooting form, PDF p.
    45 (printed 44); text.md lines 726-762; TR150 SM 8.2 Error Message: E1 and Cause
    of E1, PDF pp. 34-35; text.md lines 494-530; TR150 SM E1 issue troubleshooting
    form, PDF p. 39; text.md lines 562-602; TR260 SM 8-4 Error Message: E1 and Cause
    of E1, PDF pp. 33-34; text.md lines 489-522; TR260 SM E1 issue troubleshooting
    form, PDF p. 37; text.md lines 534-563; TRX1400 SM 8.2 Error Message: E1 and Cause
    of E1, PDF pp. 39-40 (printed 37-38); text.md lines 624-660; TRX1400 SM E1 issue
    troubleshooting form, PDF p. 44 (printed 43); text.md lines 692-732; TRX3500/TRX4500
    SM 8.2 Error Message: E1 and Cause of E1, PDF pp. 45-46 (printed 44-45); text.md
    lines 710-738; TRX3500/TRX4500 SM E1 issue troubleshooting form, PDF p. 50 (printed
    49); text.md lines 771-807; TRX5500 SM 7-4 Error Message: E1 / Lost Speed, PDF
    pp. 38-39 (printed 37-38); text.md lines 590-609; TRX5500 SM Troubleshooting Form
    under 7-4, PDF p. 43 (printed 42); text.md lines 642-653'
  extracted_at: '2026-09-11'
---

**This is E1 on the Dyaco-built Xterra treadmills, where it is a lost-speed fault.** On the TR6.6 and TR6.4 an E1 is a console memory fault (`xterra-tr-errors-e1-console-memory-or-cpu-fault`) and lost speed is LS; on the TR75H and TR95H E1 is a lost-speed or current-limit fault with different timings (`xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit`).

*Definition.* Display board CPU did not receive the RPM signal. **This only happens in calibration.** In general use the machine does not need the speed RPM sensor, but during calibration it is necessary. The TRX5500 book titles the code "E1 / Lost Speed".

*Configuration.* The speed signal is sent and received through TX/RX of the 5-pin main wires between the console display board and the driver board; the RPM sensor feeds the driver board on a 2-pin lead.

*Cause.* The motor doesn't turn and E1 appears: the drive board did not send voltage to the motor, so the motor didn't operate, and the display board didn't receive the RPM sensor signal.

*E1 issue troubleshooting form* (identical in all seven books)

| E1 message | Possible cause | Things to check | Solution |
|---|---|---|---|
| The motor cannot move | The upper console board (TR260 and TRX books: "the monitor") hasn't received any speed signal for **8 seconds** | Check the speed sensor cable is in good connection | Make sure the good connection for cables |
| | The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap-distance **less than 3 mm** |
| | Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or cables |

The form says 8 seconds; the same books' owner's manuals say 8~10 or 10 seconds, and the TR260 check list says the sensor gap "must be less than 3~5mm". All of those figures are printed; none is corrected here.

The step-by-step chart is `xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v` (TR150, TRX1400) or `xterra-treadmill-errors-e1-solution-flow-chart-pwm-led` (the other five); the sensor check the charts branch to is `xterra-treadmill-errors-e1-check-rpm-sensor-procedure`. On the TRX5500 the console ships without a speed sensor at all - `trx5500-2024-errors-e1-lost-speed-console-has-no-speed-sensor-fitted`.
