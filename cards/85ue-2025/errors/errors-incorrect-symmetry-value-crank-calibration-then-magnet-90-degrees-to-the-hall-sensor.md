---
id: 85ue-2025-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
title: An incorrect symmetry value on the upper-body ergometer is the crank calibration,
  then the right crank refitted at 6 o'clock with the chain wheel magnet at least
  90 degrees from the Hall sensor
kind: troubleshooting
question: What do I do when the symmetry value is wrong on a Spirit 85ue-2025 upper
  body ergometer?
asked_as:
- symmetry index wrong on my 8.5ue
- left right split off on the arm ergometer
- crank calibration 8.5ue
- magnet angle to the hall sensor ube
keywords:
- symmetry
- symmetry index
- crank calibration
- crank position
- magnet
- hall sensor
- 90 degrees
- chain wheel
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: errors
  code: no-code
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
see_also:
- spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
- 85ue-2025-errors-no-revolutions-d13-then-hall-sensor-078-to-chain-wheel-208-at-2-to-3-mm
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 8.5UE (MZ2000-SB036-01) service manual 5.4 Incorrect Symmetry Value, steps
    1-2, Figure 11 and the Check Procedure flow chart, PDF p. 27-28; text.md lines
    325-343 and the OCR supplement for page 28; 4.2.2.3.8 Crank Calibration, PDF p.
    15, lines 197-224
  extracted_at: '2026-09-11'
---

**A wrong symmetry value on the touchscreen ergometer gets two steps, and the second is a magnet angle.**

**Step 1.** **Calibrate the crank position** (see the Maintenance Mode section - *Service > Crank Calibration: put the right crank at a 6 o'clock position, then press the button below to run the test*). If the issue persists, proceed to the next step.

**Step 2.** Position the right crank at the **6 o'clock position**. Ensure that the **magnet on the Chain Wheel (208) maintains an angle of at least 90 degrees relative to the Hall sensor**. Once properly aligned, install the right crank. Then, recalibrate the crank position.

**The symmetry index is left against right, and the console knows which pedal is where from one magnet passing one sensor once per revolution.** Calibration tells it where the right crank is when the magnet passes; if the crank was pressed onto its axle at the wrong angle, the magnet passes the sensor while the crank is somewhere the console does not expect, and every left/right split is skewed. Step 2 is therefore a mechanical re-seat: right crank at 6 o'clock, magnet at least a quarter-turn away from the sensor, crank fitted, then calibrate again. The flow chart's two results are *problem corrected via calibration* and *reinstall the crank in the correct orientation*.

**No tolerance is printed** - nothing says how far from 50/50 the index has to be before it counts as incorrect. The 8.0U/8.5R bikes print the same two steps with the magnet on the drive pulley (`spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor`).

