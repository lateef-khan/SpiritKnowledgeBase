---
id: xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
title: Working through an E1 by watching the PWM LED on the controller, then the M+
  and M- motor terminals, the cable, the console and the controller
kind: procedure
question: How do I diagnose an E1 step by step on an Xterra tr260-2023, trx2500-2024,
  trx3500-2024, trx4500-2024 or trx5500-2024 treadmill?
asked_as:
- e1 flow chart pwm led xterra
- belt does not move e1 which board is bad
- how to tell if the controller or motor is bad e1
keywords:
- e1
- flow chart
- pwm led
- power led
- motorhood
- m+ m-
- motor cable
- replace controller
- replace console
- replace motor
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v
- spirit-xt-errors-e1-solution-flow-chart
see_also:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- trx2500-2024-errors-controller-led-debugging-three-leds
- ct850-2016-low-speed-solution-flow-chart
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM E1 solution follow chart, a flat picture read from the render,
    PDF p. 42 (printed 41); text.md lines 693-701; TRX3500/TRX4500 SM E1 solution
    follow chart, a flat picture read from the render, PDF p. 47 (printed 46); text.md
    lines 738-746; TR260 SM E1 solution follow chart, a flat picture read from the
    render, PDF p. 35; text.md lines 522-528; TRX5500 SM E1 solution follow chart,
    a flat picture read from the render, PDF p. 40 (printed 39); text.md lines 609-615
  extracted_at: '2026-09-11'
---

**This is the newer of the two E1 charts** - the one built around the PWM LED on the controller. The TR150 and TRX1400 books draw the older reset-power chart (`xterra-treadmill-errors-e1-solution-flow-chart-reset-power-then-dc-12v`).

The chart is a flat picture with no text layer, read from the rendered page. The header box reads "E1 showing up" in the TR260 and TRX3500/TRX4500 books, "Er showing up" in the TRX2500 book (a misprint; the section is 8.2 E1) and "LS1/LOW SPEED showing up" in the TRX5500 book, whose code is titled E1 / Lost Speed. In order:

1. **Did the belt move after start?** Yes -> go to the check RPM sensor procedure (`xterra-treadmill-errors-e1-check-rpm-sensor-procedure`). No -> step 2.
2. **Open the motorhood and turn the power back on.** Press "start" to count down and **watch the PWM LED on the controller.**
3. **PWM LED on?**
   - **No** -> is the cable connection OK? No -> connect properly, turn the power back on: is function OK? Yes -> problem fixed. No -> replace the console, turn the power back on: is function OK? Yes -> problem fixed; no -> replace the controller. Cable connection OK -> replace the cable, then the same console-then-controller sequence.
   - **Yes** -> step 4.
4. **Are only the POWER LEDs on** (TRX books: "only POWER and PWM LEDs on")? The branch to *replace controller* is labelled NO in the TR260 book and YES in the TRX2500, TRX3500/TRX4500 and TRX5500 books, whose charts label both exits YES; read the chart as: if the LEDs are not as expected, replace the controller, otherwise step 5.
5. **Is the motor cable connected to the M+ and M- terminals properly?** No -> connect properly, turn the power back on and press "start" to count down: function OK? Yes -> problem fixed; no -> step 6. Yes -> step 6.
6. **Replace the controller.** Turn the power back on and press "start" to count down: is function OK? Yes -> problem fixed. No -> **replace the motor.**

The TR260 and TRX5500 charts name the LED step "Are only POWER LEDs on" / "POWER and PWM LEDs on" while the TRX2500 book's own LED table names its three LEDs LED1 (communication), LED2 (power) and LED3 (speed) with no PWM LED - see `trx2500-2024-errors-controller-led-debugging-three-leds`. The Spirit CT850 book draws the same PWM chart (`ct850-2016-low-speed-solution-flow-chart`).
