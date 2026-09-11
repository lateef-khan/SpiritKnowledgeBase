---
id: xterra-treadmill-errors-e1-check-rpm-sensor-procedure
title: 'Checking the RPM speed sensor after an E1: cable, magnet closest to the sensor,
  a gap under 3 mm, then sensor, computer cable and console'
kind: procedure
question: How do I check the speed sensor after an E1 on an Xterra tr150-2021, tr260-2023,
  trx1400-2023, trx2500-2024, trx3500-2024, trx4500-2024 or trx5500-2024 treadmill?
asked_as:
- how to check the speed sensor on my xterra treadmill
- rpm sensor gap for e1
- where is the speed sensor on an xterra treadmill
keywords:
- e1
- rpm sensor
- speed sensor
- reed switch
- magnet
- gap
- 3 mm
- front roller pulley
- computer cable
- motor cover hood
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
- ct850-2016-low-speed-check-rpm-sensor
see_also:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
- xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v
- trx5500-2024-errors-e1-lost-speed-console-has-no-speed-sensor-fitted
- spirit-xt-errors-e1-check-rpm-sensor-procedure
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM E1 solution follow chart - check RPM sensor device procedure
    (picture) and Checking the speed sensor, PDF pp. 43-44 (printed 42-43); text.md
    lines 701-726; TR150 SM E1 solution follow chart - check RPM sensor device procedure
    (picture, read from the render) and Checking the speed sensor, PDF pp. 37-38;
    text.md lines 536-562; TR260 SM E1 solution follow chart-check RPM sensor device
    procedure (picture; the OCR supplement is upside down) and Checking the speed
    sensor, PDF pp. 36-37; text.md lines 528-563; TRX1400 SM E1 solution follow chart
    - check RPM sensor device procedure (picture) and Checking the speed sensor, PDF
    pp. 42-43 (printed 41-42); text.md lines 666-692; TRX3500/TRX4500 SM E1 solution
    follow chart - check RPM sensor device procedure (picture) and Checking the speed
    sensor, PDF pp. 48-49 (printed 47-48); text.md lines 746-771; TRX5500 SM E1 solution
    follow chart - check RPM sensor device procedure (picture) and Checking the speed
    sensor, PDF pp. 41-42 (printed 40-41); text.md lines 615-642; TR150 MCB wiring
    photo (authority 2), the labels SPD / 'If you have speed sensor, then it plugs
    here', 'M+ Red lead from drive motor', 'M- Black lead from drive motor'; text.md
    lines 1-40
  extracted_at: '2026-09-11'
---

Every Dyaco service manual in this wave draws the same *E1 solution follow chart - check RPM sensor device procedure* and prints the same three-step *Checking the speed sensor* text under it. The chart is a picture (in the TR260 book its OCR supplement is upside down); it was read from the render.

*The chart*

1. **Is the sensor cable connected properly?** No -> connect properly. Yes -> step 2.
2. **Move the roller so that the magnet is closest to the sensor.**
3. **Make sure the gap between magnet and sensor is less than 3 mm.** No -> adjust the sensor position. Yes -> step 4.
4. **Replace the sensor with cable.** Turn the power back on, press "start" and count down: is function OK? Yes -> problem fixed. No -> step 5.
5. **Replace the computer cable.** Turn the power back on, press "start" and count down: is function OK? Yes -> problem fixed. No -> **replace the console.** (The TRX5500 chart omits the computer-cable step and goes from the sensor straight to the console.)

*Checking the speed sensor*

1. Remove the motor cover hood.
2. The speed sensor is located on the **left side of the frame, right next to the front roller pulley** (the pulley has a belt around it that also goes to the motor). The speed sensor is small and black with a wire connected to it. The books caption the part "Reed switch RPM speed sensor device" (TR150 and TRX1400: "Read switch").
3. Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley; make sure the sensor is aligned with the magnet. A screw holds the sensor in place and must be loosened to adjust the sensor. Re-tighten the screw when finished.

The 3 mm figure is the one on the chart and the E1 form; the older E1 solution chart says 2 mm, and the TR260 check list says 3~5 mm. On the TRX5500 there is no sensor on the machine until a technician fits one (`trx5500-2024-errors-e1-lost-speed-console-has-no-speed-sensor-fitted`); the TR150 board photo marks the 2-pin **SPD** socket "If you have speed sensor, then it plugs here", which is why the TR150 definition says the sensor is only needed for calibration.

The Spirit XT books print the identical procedure (`spirit-xt-errors-e1-check-rpm-sensor-procedure`).
