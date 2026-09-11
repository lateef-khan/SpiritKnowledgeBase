---
id: spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration
title: A wrong Symmetry reading on the rehabilitation bike is the Unit Type setting,
  the Sensor Test and the Crank Position calibration - and the recumbent book says
  to set Unit Type to upright
kind: troubleshooting
question: What do I check when the symmetry measurement is wrong on a Spirit Medical
  7.0R or 7.0U bike?
asked_as:
- symmetry index wrong on my 7.0r
- left right watts dont match on the rehab bike
- crank position calibration 7.0u
- unit type setting on spirit medical bike
keywords:
- symmetry
- symmetry index
- unit type
- sensor test
- crank position calibration
- left and right watts
- rehabilitation bike
- maintenance mode
- mu100 mr100
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
- spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
see_also:
- spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R (MR490-SB018-03) service manual 5.2.4 Troubleshooting, 4. Symmetry
    Measurement is Incorrect, PDF p. 13, text.md lines 158-177, and 5.2.1 xiii Unit
    Type, PDF p. 8, lines 92-120. 7.0U (MU470-SB018) service manual 5.2.4, 4., PDF
    p. 13, text.md lines 209-223. Owner''s manual row, with the "upright" defect on
    the recumbent: ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48 (printed 46); text.md
    lines 1328-1377; 7.0U 2025 owner''s manual ERROR MESSAGE & TROUBLESHOOTING, PDF
    p. 46 (printed 44); text.md lines 1285-1329; Dyaco MED 7.0R 2021 owner''s manual
    (Rev. 1.2.1) Error messages and Troubleshooting, PDF p. 84-85; text.md lines 2642-2730'
  extracted_at: '2026-09-11'
---

The service manuals, in three steps:

> **Symmetry Measurement is Incorrect**
> i. Check the **Unit Type** is setting to the right model.
> ii. Check the sensors by the **Sensor Test** in Maintenance mode.
> iii. Run the **Crank Calibration** in Maintenance mode.

The owner's manuals put the same three the other way round:

> - Perform the sensor tests in Maintenance Mode
> - If sensors are functioning then perform Crank Position Calibration
> - If calibration is ok then check the Unit Type is set to ...

**And here the recumbent book is wrong.** The 7.0R 2025 owner's manual ends that line *check the Unit Type is set to **upright*** - on a recumbent bike. The 7.0U 2025 owner's manual says the same, correctly, for the upright. The Dyaco MED 7.0R 2021 edition says *set to 7.0R*, and the 7.0R service manual's Maintenance Mode page lists the choices as **MU100 for the upright bike and MR100 for the recumbent bike**, with the 7.0R owner's manual's own Maintenance Mode page saying *Unit type: select on the console: Recumbent*. The troubleshooting line is a copy from the upright book. On a 7.0R set the Unit Type to **Recumbent (MR100)**; on a 7.0U to **Upright (MU100)**.

**Why the setting matters to symmetry.** The symmetry index compares left and right pedal work, and the console works out which pedal is where from the reed switch on the crank plus the crank position calibration (*set right pedal to 6 o'clock, press start, rotate clockwise until the console beeps*). The book does not say what the Unit Type changes inside the calculation, only that it must match the machine. The Sensor Test reads `ANGLE 0 REED 0` and the REED figure should flip 0 to 1 once per revolution with a beep; a reed switch that does not flip has no crank position to give the symmetry index.

**No tolerance is printed** - nothing says how far apart left and right have to read before the measurement counts as incorrect. The steppers answer the same symptom with the sensor test alone (`spirit-med-stepper-errors-symmetry-or-watt-reading-wrong`); the 8.0U/8.5R answer it with a magnet angle (`spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor`).

