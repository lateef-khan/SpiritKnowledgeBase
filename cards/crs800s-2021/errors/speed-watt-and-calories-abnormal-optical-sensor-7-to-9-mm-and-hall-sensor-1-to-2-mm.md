---
id: crs800s-2021-errors-speed-watt-and-calories-abnormal-optical-sensor-7-to-9-mm-and-hall-sensor-1-to-2-mm
title: 'Abnormal speed, watts or calories on the semi-recumbent stepper: the optical
  sensor board 7 to 9 mm from the cable drive pulley and the hall sensor 1 to 2 mm
  from its magnet'
kind: troubleshooting
question: What do I check when the speed, watt or calorie readings are wrong on a
  Spirit crs800s-2021 semi-recumbent stepper?
asked_as:
- crs800s speed reading is wrong
- watts wrong on my spirit recumbent stepper
- crs800s sensor gap
- stepper calories reading nonsense
keywords:
- speed abnormal
- watts
- calories
- optical sensor board
- hall sensor
- magnet
- 7-9mm
- 1-2mm
- cable drive pulley
- semi-recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: crs800s-2021
  applies_to:
  - crs800s-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-med-stepper-errors-optical-sensor-board-gap-7-to-9-mm-abnormal-spm-or-no-response
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 9-3 The abnormality of Console Speed, Watt and Calories, PDF p. 39-40 (printed
    38-39); text.md lines 559-603 (the page prints 9-2, 9-3 and 9-4 in two columns
    and the extraction interleaves them; the render was read)
  extracted_at: '2026-09-11'
---

The section lists the sensor parts, then the checks:

1. **Optical Sensor Board components** - the cable drive pulley, the optical sensor board, the sensor bracket and the isolation column (a labelled photograph).
2. **Hall Sensor** - on the drive pulley, with its magnet (a second labelled photograph).
3. Check if the connection is proper.
4. Adjust Sensor Bracket and Optical Sensor Board position (Remark: **the distance between Optical Sensor Board and Cable Drive Pulley is 7~9mm**).
5. Adjust the position of Hall Sensor (Remark: **the distance between Hall Sensor and Magnet is 1~2mm**).

**Two sensors, two gaps, and the console's three readings depend on both.** The optical board reads the cable drive pulley - the step count and its direction; the hall sensor reads a magnet on the drive pulley - the flywheel speed. Speed, watts and calories are computed from the pair, so a wrong figure in any of the three windows sends you to both gaps. Connections come first; no voltage is printed for either sensor in this book.

**The same two figures appear on the medical steppers** - 7 to 9 mm for the optical encoder board and 1 to 2 mm for the RPM sensor on the 7.5S (`spirit-med-stepper-errors-optical-sensor-board-gap-7-to-9-mm-abnormal-spm-or-no-response`) - and the CRS800S's *Sensor test* under Maintenance Mode is described as testing *the speed sensor function*, which is the hall sensor here.

A stepper whose resistance rather than its readings is wrong is the `MOTOR ERROR` page (`crs800s-2024-errors-motor-error-tension-motor-signal-wrong`).
