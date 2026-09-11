---
id: 70t-2026-console-service-mode-tests
title: 'Service Mode: the incline, drive-motor, brake and step-sensor tests and the
  readings each shows'
kind: procedure
question: What do the Service Mode tests do on a Spirit 7.0T or MT200 treadmill and
  what readings do they show?
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
  - 70t-2025
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
  locator: p. 43, MACHINE CARE - CONTINUED - Service Mode. MT200-2022 service manual
    section 4.2.1 d.vii Service Mode, PDF pp. 8-10 (printed 8-10), text.md lines 121-173;
    the 2025 E27 support email (spirit-treadmill-mt200-e27-encoder-error-email), pages
    2-3. 7.0T 2025 owner's manual PDF p. 45 (printed 43), text.md lines 1386-1421.
    The 770885 re-export of the same MT8000 book (spirit-treadmill-70t-2026-service-manual,
    MT8000-ST024-01 on the file, ST021-01 on its cover) prints this section at the
    same PDF page and text.md lines; only its cover and component call-outs differ.
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

**The MT200-2022 service manual prints the same four tests with figures the owner's manual does not
have.** For the Drive Motor test it gives nominal no-load readings - belt running, nobody on it:

| Speed | RPM | AMP |
|---|---|---|
| 0.8 KPH (0.5 MPH) | 190 | 4.30 |
| 1.6 KPH (1.0 MPH) | 373 | 2.95 |
| 4.8 KPH (3.0 MPH) | 1106 | 1.83 |
| 8.0 KPH (5.0 MPH) | 1840 | 1.82 |

"These values are nominal and can vary slightly from machine to machine. If there is a problem with
the treadmill, the numbers would be very different." The Speed window shows the actual belt speed;
the RPM is motor RPM, not belt speed.

For the Motor Brake test: **the brake is working if you hear a "click" when Enter turns it off and
the belt can then move freely. When the brake is off the coil is energized and there is 18 Vdc at the
two brake wires; when ON there is no power to the coil.** The 2025 support email on the E27 encoder
error sends the technician to this same test ("section 4.2.1 maintenance mode (engineering mode) in
service manual ... Motor Brake test under Service Mode") and adds that the inverter-to-brake supply
should measure a **stable DC 12 to 19 V at least** - a range that brackets the manual's 18 Vdc.

For the Step Sensors test the manual adds pictures captioned "Step on left", "No Step", "Step on
right"; the calibration that follows is `70t-2026-console-step-sensor-calibration`.

**The 2025 printing of the 7.0T owner's manual (Revision 01.10.25, warranty effective October 23, 2024) prints this section word for word on the same page**, so this card covers the 70t-2025 as well.

