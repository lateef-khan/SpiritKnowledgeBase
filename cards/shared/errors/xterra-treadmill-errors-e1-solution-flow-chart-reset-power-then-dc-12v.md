---
id: xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v
title: Working through an E1 from a power reset to replacing the motor, on the chart
  that checks pin 2 and pin 5 for DC 12 V
kind: procedure
question: How do I diagnose an E1 step by step on an Xterra tr150-2021 or trx1400-2023
  treadmill?
asked_as:
- e1 troubleshooting steps xterra
- flow chart for e1 on my treadmill
- belt will not move e1 what do i check first
keywords:
- e1
- flow chart
- reset power
- countdown
- main control line
- rpm sensor
- 2 mm
- dc12v
- pin2 pin5
- replace motor
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - trx1400-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
- ct850-2016-low-speed-solution-flow-chart
see_also:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- spirit-xt-errors-e1-solution-flow-chart
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM E1 solution follow chart, a flat picture read from the render,
    PDF p. 36 (printed 40); text.md lines 530-536; TRX1400 SM E1 solution follow chart,
    a flat picture read from the render, PDF p. 41 (printed 40); text.md lines 660-666
  extracted_at: '2026-09-11'
---

**This is the older of the two E1 charts** - the one with a power reset, a DC 12 V check and no LED. The TR260, TRX2500, TRX3500, TRX4500 and TRX5500 books draw a different chart around the controller's PWM LED (`xterra-treadmill-errors-e1-solution-flow-chart-pwm-led`).

The chart is a flat picture with no text layer, read from the rendered page. In order:

1. **E1 showing up** -> reset power -> press start again.
2. **Does the display count down after pressing start?** No -> replace the upper console board, or update the program of the upper console board. Yes -> step 3.
3. **Did the belt move after start?**
   - No -> **is the main control line split?** Yes -> replace the main control line, then re-test from step 3. No -> step 4.
   - Yes -> step 4.
4. **Is the RPM sensor good?** No -> replace the RPM sensor. Yes -> **adjust the sensor gap distance to 2 mm**. Then: did the belt move after start? Yes -> problem solved. No -> step 5.
5. **Does the lower control driver board have enough power? (AC: 220V)** No -> check whether the power source from the wall is a stable AC 220 V. Yes -> **use a multi-meter to check main control line socket pin 2 and pin 5 for DC 12 V.** No -> replace the lower control driver board. Yes -> press start and use the multi-meter to check whether the driver board motor socket has voltage. No -> replace the lower control driver board. Yes -> **replace the motor** -> problem solved.

Two figures on the chart disagree with the text around it, in both books. The chart sets the sensor gap at **2 mm**; the E1 form on the facing pages and the sensor procedure chart say **less than 3 mm**. The chart tests for **AC 220 V**; these are 110 V machines in the US books and the same service manuals draw both 110 V and 220 V circuit diagrams. Test against the supply the machine is on.

The sensor branch is detailed on `xterra-treadmill-errors-e1-check-rpm-sensor-procedure`. The Spirit XT books draw this exact chart (`spirit-xt-errors-e1-solution-flow-chart`).
