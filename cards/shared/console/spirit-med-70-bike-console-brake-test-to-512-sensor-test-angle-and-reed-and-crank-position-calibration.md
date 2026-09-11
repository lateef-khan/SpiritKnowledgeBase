---
id: spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration
title: 'Factory settings: a Brake Test through 512 levels, a Sensor test reading ANGLE
  and REED, and a crank position calibration from 6 o''clock'
kind: procedure
question: How do I test the brake and sensors, or calibrate the crank position, on
  a Spirit Medical 7.0 series bike?
asked_as:
- how do i test the resistance brake on the 7.0r
- what does angle 0 reed 0 mean on the 7.0u
- how do i calibrate the crank on my spirit medical bike
- symmetry reading is wrong on the rehab bike
keywords:
- brake test
- 512 levels
- sensor test
- angle sensor
- reed switch
- crank position calibration
- 6 o clock
- 12 o clock
- watts calibration
- factory settings
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
see_also:
- spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings
- spirit-med-70-bike-console-unit-type-recumbent-or-upright-and-the-model-codes-the-service-manual-names
- 70t-2026-console-service-mode-tests
- spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: '7.0R OM MACHINE CARE / Console Software, PDF p. 47 (printed 45), text.md
    lines 1294-1328; 7.0U OM PDF p. 45 (printed 43), lines 1251-1285; Dyaco MED 7.0R
    (2021) "Maintenance menu in console software", PDF pp. 82-84 (printed 82-84),
    lines 2592-2659. 7.0R SM (MR490-SB018-03) 5.2.1 Maintenance Mode, PDF pp. 7-8,
    lines 73-109; 7.0U SM (MU470-SB018) 5.2.1, PDF pp. 7-8, lines 124-160. Troubleshooting
    uses: 7.0R OM p. 48, lines 1330-1341 and 1366-1373; 7.0R SM 5.2.4 items 3-5, PDF
    pp. 12-13, lines 145-177.'
  extracted_at: '2026-09-11'
---

These four entries sit under **Factory settings** in the maintenance menu
(`spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings`).

**Brake Test** - "allows you to manually change resistance levels one bit at a time to test whether the
brake is functioning properly. **There are 512 levels.**" The service manuals add a caution: **"512 is
the maximum resistance, don't stay in high level (more than 400) for too long."** In the no-resistance
fault path the service manuals run this test at 512 and expect the **orange LED on the control board**
to light; if it does not, the control board is replaced.

**Sensor test** - "The [bike] has two sensors, one **angle sensor** for speed/velocity measurements
located on the brake, and one **reed switch** that measures crank rotation which we use to determine
crank position."

- The message window shows **`ANGLE 0 REED 0`**.
- "When sensors operate correctly: rotate the crank and the Angle reading will show pedal RPM measurement
  and the Reed will change from 0 to 1 once per pedal revolution" - the service manuals add "and beep".

**Crank position cali** - "Software calibration to set the position of the right pedal at 12 o'clock."

1. Set the right pedal to the **6 o'clock** position, then press **Start**.
2. **Rotate the right pedal clockwise until the console beeps.**

**Watts calibration** - "(Factory use only)". Nothing else is printed about it.

**When to use them, from the troubleshooting pages.** "Program starts but no data registers when
pedaled" - run the Sensor tests; if one sensor fails it needs replacing, if both fail it could be the
console or both sensors. "Symmetry measurement is incorrect" - run the sensor tests, then the Crank
Position Calibration, then check the **Unit Type**
(`spirit-med-70-bike-console-unit-type-recumbent-or-upright-and-the-model-codes-the-service-manual-names`).
The service manuals' gap figures for the two sensors - **3 mm** magnet to angle sensor, **about 5 mm** at
the reed switch, and **2 mm** on reassembly - are held with the maintenance and error cards.

The 7.0T treadmill's Service Mode tests incline and drive motors instead
(`70t-2026-console-service-mode-tests`); the steppers' Sensor test lights five windows
(`spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test`).

