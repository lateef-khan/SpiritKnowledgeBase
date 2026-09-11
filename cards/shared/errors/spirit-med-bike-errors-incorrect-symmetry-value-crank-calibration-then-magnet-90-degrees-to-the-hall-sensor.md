---
id: spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
title: An incorrect symmetry value on the touchscreen bike is the crank calibration,
  then the right crank refitted at 6 o'clock with the magnet at least 90 degrees from
  the Hall sensor
kind: troubleshooting
question: What do I do when the symmetry value is wrong on a Spirit Medical 8.0U or
  8.5R bike?
asked_as:
- symmetry index wrong on my 8.0u
- left right split off on the rehab bike
- crank calibration 8.5r
- magnet angle to the hall sensor spirit medical bike
keywords:
- symmetry
- symmetry index
- crank calibration
- crank position
- magnet
- hall sensor
- 90 degrees
- 6 o clock
- touchscreen bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
see_also:
- 85ue-2025-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
- spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U (MU2000-SB036-01) service manual 5.4 Incorrect Symmetry Value, steps
    1-2, Figure 11 and the Check Procedure flow chart, PDF p. 28-29; text.md lines
    442-457 and the OCR supplements for pages 28-29; 4.2.2.3.8 Crank Calibration,
    PDF p. 16, lines 300-318. 8.5R (MR2000-SB036-01) service manual 5.4, PDF p. 27-28;
    text.md lines 327-336 and the OCR supplements for pages 27-28 - word for word
  extracted_at: '2026-09-11'
---

**A wrong symmetry value on the touchscreen bike gets two steps, and the second is a magnet angle.**

**Step 1.** **Calibrate the crank position** (see the Maintenance Mode section - *Service > Crank Calibration: put the right crank at a 6 o'clock position, then press the button below to run the test*). If the issue persists, proceed to the next step.

**Step 2.** Position the right crank at the **6 o'clock position**. Ensure that the **magnet on the drive pulley (#45-1) maintains an angle of at least 90 degrees relative to the Hall sensor**. Once properly aligned, install the right crank. Then, recalibrate the crank position.

**The symmetry index is left against right, and the console knows which pedal is where from one magnet passing one sensor once per revolution.** Calibration tells it where the right crank is when the magnet passes; if the crank was pressed onto its axle at the wrong angle, the magnet passes the sensor while the crank is somewhere the console does not expect, and every left/right split is skewed. Step 2 is therefore a mechanical re-seat: right crank at 6 o'clock, magnet at least a quarter-turn away from the sensor, crank fitted, then calibrate again. The flow chart's two results are *problem corrected via calibration* and *reinstall the crank in the correct orientation*.

**No tolerance is printed** - nothing says how far from 50/50 the index has to be before it counts as incorrect. The 8.0U and 8.5R service manuals print the page identically; the 8.5UE prints it with the magnet on the chain wheel (`85ue-2025-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor`). The 7.0R/7.0U answer the same symptom with the Unit Type and a reed switch (`spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration`); the symmetry screen itself is carded under `section: console`.

