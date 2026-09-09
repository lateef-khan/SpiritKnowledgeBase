---
id: 70t-2026-console-service-mode-tests
title: "Service Mode: the incline, drive-motor, brake and step-sensor tests and the readings each shows"
kind: procedure
question: What do the Service Mode tests do on a Spirit 7.0T or MT200 treadmill and what readings do they show?
asked_as:
- how do i test the incline motors
- what do the f and r numbers mean in service mode
- how do i check the drive motor amps
- how do i test the step sensors
keywords:
- service mode
- incline test
- drive motor test
- rpm
- amp
- motor brake
- step sensors
- a/d values
- position sensor
- limit switch
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2026
  - mt200-2010
  - mt200-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- 70t-2026-console-step-sensor-calibration
see_also:
- 70t-2026-console-maintenance-mode-menu
- 70t-2026-console-step-sensor-calibration
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: p. 43, MACHINE CARE - CONTINUED - Service Mode
  extracted_at: '2026-09-09'
---

Service Mode is the last item in the maintenance Functions menu; see
`70t-2026-console-maintenance-mode-menu` for how to reach it. `MW` below is the
message window, `DM` the dot matrix.

**Incline**
- MW scrolls "Use incline keys for front use speed keys for rear", then switches
  to the value display.
- **Incline keys operate the front motor, speed keys operate the rear motor.**
  Hold an up/down key to run a motor; it stops when the key is released. The motor
  is allowed to move until its limit switch is activated.
- MW displays **A/D values for both position sensors**, for example `F 920 R 70`.
  **F = front incline sensor, R = rear incline sensor.** **The readings are
  opposite**: at lowest incline the front shows a large number and the rear a small
  one.

**Drive Motor**
- MW displays "Use speed keys to move motor". **Each key press increases motor
  speed 0.1 mph/kph.**
- MW then shows `RPM 000 AMP 00.0`. **The sensor reading indicates motor RPM, not
  belt speed.** The AMP figure is measuring motor current.

**Motor Brake**
- **Brake ON (brake coil turned off).** The user presses enter to turn the Brake
  OFF.

**Step Sensors Test**
- Uses the sensor outputs to light the dot matrix, similar to the Symmetry
  display. **This test only confirms the sensors are functioning; it does not test
  accuracy.** The DM graph shows left and right sensor activity when stepping on
  the deck. **Both sides of the graph light at the same time**, but the side the
  user steps with shows more segments lit.

Calibrating those step sensors is a separate routine; see
`70t-2026-console-step-sensor-calibration`.

**Both MT200 manuals print every one of these tests word for word**, including the
`F 920 R 70` example - the 2010 manual on its p. 39, the 2022 manual on its
pp. 62-63.
