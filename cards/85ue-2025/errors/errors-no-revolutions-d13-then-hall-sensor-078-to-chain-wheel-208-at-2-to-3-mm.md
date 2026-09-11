---
id: 85ue-2025-errors-no-revolutions-d13-then-hall-sensor-078-to-chain-wheel-208-at-2-to-3-mm
title: 'No revolutions on the upper-body ergometer: the D13 indicator, then the Hall
  sensor set 2 to 3 mm from the chain wheel magnet and centred between the arrow marks,
  then its cable'
kind: troubleshooting
question: Why does a Spirit 85ue-2025 upper body ergometer show no revolutions or
  RPM when the handles are turned?
asked_as:
- 8.5ue no rpm when cranking
- arm ergometer not counting revolutions
- hall sensor gap on the 8.5ue
- ube rpm sensor not working
keywords:
- no revolutions
- no rpm
- hall sensor
- magnet gap
- 2 to 3 mm
- d13
- chain wheel
- lower control board
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: errors
  code: no-speed
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
see_also:
- spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072
- 85ue-2025-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
- 85ue-2025-errors-no-power-wake-then-cn1-d5-24-vdc-then-12-vdc
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 8.5UE (MZ2000-SB036-01) service manual 5.3 No revolutions, steps 1-3 and
    the Check Procedure flow chart, PDF p. 25-26; text.md lines 302-325 and the OCR
    supplement for page 26
  extracted_at: '2026-09-11'
---

**"No revolutions" is the console showing nothing turning while the hand cranks is turned** - no RPM, so no watts, distance or symmetry either. The book gives three steps and one LED.

**Step 1.** While pedaling the crank, check the status of **indicator light D13** on the LCB. If the light **flashes**, confirm that both ends of the cable are properly connected. If the light does not flash, proceed to the next step.

**Step 2.** Confirm that the gap between the **Hall sensor (078) and the magnet on the Chain Wheel (208)** is **2 to 3 mm**, and that the sensor is aligned with the **center point between the two arrow marks**. If the sensor is not installed correctly, reinstall it. If the installation is correct, proceed to the next step.

**Step 3.** Confirm that both ends of the cable are properly connected. If the cable is not properly connected, reconnect both ends securely. If the cable is already properly connected, **replace both the LCB and the Hall sensor**.

**D13 flashing means the board is seeing the magnet, so the fault is downstream** - the cable that carries the count on to the console. D13 dark means the board is not seeing it: the sensor is checked first (gap and alignment), then its cable, and only then are the sensor and the LCB replaced together - the book does not say to try one before the other.

**The gap and the alignment are the only figures.** 2 to 3 mm, and the sensor centred between two arrow marks moulded beside it. This is a chain-driven machine: the magnet sits on the chain wheel (208), read by the Hall module (078), and the drive belt and chain wheel come off together in the replacement chapter. The 8.0U/8.5R bikes print the same three steps with the magnet on the drive pulley and the cable numbered #072 (`spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072`).

