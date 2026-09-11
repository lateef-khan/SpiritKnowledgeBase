---
id: spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072
title: 'No revolutions on the touchscreen bike: the D13 indicator, then the Hall sensor
  set 2 to 3 mm from the drive pulley magnet and centred between the arrow marks,
  then its cable'
kind: troubleshooting
question: Why does a Spirit Medical 8.0U or 8.5R bike show no revolutions or RPM when
  the pedals are turned?
asked_as:
- 8.0u no rpm when pedaling
- rehab bike not counting revolutions
- hall sensor gap on the 8.5r
- spirit medical bike rpm sensor not working
keywords:
- no revolutions
- no rpm
- hall sensor
- magnet gap
- 2 to 3 mm
- d13
- cable 072
- lower control board
- drive pulley
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
  code: no-speed
authority: 3
not_to_be_confused_with:
- spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
- spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet
see_also:
- 85ue-2025-errors-no-revolutions-d13-then-hall-sensor-078-to-chain-wheel-208-at-2-to-3-mm
- spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor
- spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U (MU2000-SB036-01) service manual 5.3 No revolutions, steps 1-3 and
    the Check Procedure flow chart, PDF p. 26-27; text.md lines 420-442 and the OCR
    supplement for page 27; parts list items 24-1, 24-2 and 84, PDF p. 44-45, lines
    693-766. 8.5R (MR2000-SB036-01) service manual 5.3, PDF p. 25-26; text.md lines
    311-327 and the OCR supplement for page 26 - word for word
  extracted_at: '2026-09-11'
---

**"No revolutions" is the console showing nothing turning while the pedals is turned** - no RPM, so no watts, distance or symmetry either. The book gives three steps and one LED.

**Step 1.** While pedaling the crank, check the status of **indicator light D13** on the LCB. If the light **flashes**, confirm that both ends of the **#072 cable** are properly connected. If the light does not flash, proceed to the next step.

**Step 2.** Confirm that the gap between the **Hall sensor and the magnet on the drive pulley (#45-1)** is **2 to 3 mm**, and that the sensor is aligned with the **center point between the two arrow marks**. If the sensor is not installed correctly, reinstall it. If the installation is correct, proceed to the next step.

**Step 3.** Confirm that both ends of the **#072 cable** are properly connected. If the cable is not properly connected, reconnect both ends securely. If the cable is already properly connected, **replace both the LCB and the Hall sensor** (#091, #084).

**D13 flashing means the board is seeing the magnet, so the fault is downstream** - the cable that carries the count on to the console. D13 dark means the board is not seeing it: the sensor is checked first (gap and alignment), then its cable, and only then are the sensor and the LCB replaced together - the book does not say to try one before the other.

**The gap and the alignment are the only figures.** 2 to 3 mm, and the sensor centred between two arrow marks moulded beside it. The parts list calls the sensor the *Hall Module* (84) and puts the magnet at item 24-2 on the drive pulley 24-1; the procedure's *#45-1* follows the wiring diagram, which labels the magnet *#045-2*; no item 45 exists on the parts list. The 8.0U and 8.5R service manuals print the page identically. The 7.0R/7.0U of the range read an angle sensor at 3 mm and a reed switch at 5 mm instead (`spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm`), and the 8.5UE reads its Hall sensor off the chain wheel (`85ue-2025-errors-no-revolutions-d13-then-hall-sensor-078-to-chain-wheel-208-at-2-to-3-mm`).

