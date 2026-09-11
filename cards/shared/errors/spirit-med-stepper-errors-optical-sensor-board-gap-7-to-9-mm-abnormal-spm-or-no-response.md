---
id: spirit-med-stepper-errors-optical-sensor-board-gap-7-to-9-mm-abnormal-spm-or-no-response
title: An abnormal SPM reading or an optical sensor board that does not respond is
  its cable and a 7 to 9 mm gap to the barcode sticker on the cable wheel
kind: troubleshooting
question: What is the optical sensor board gap on a Spirit 7.5S or 8.5S recumbent
  stepper when the steps per minute read wrong or the sensor does not respond?
asked_as:
- stepper spm reading is wrong
- spirit rehab stepper optical sensor not responding
- what gap for the encoder sensor on the 7.5s
- 8.5s sensor board distance to the sticker
keywords:
- optical sensor board
- encoder
- barcode sticker
- 7-9mm
- abnormal spm
- no respond
- cable guide wheel
- rpm sensor
- 1-2mm
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-5s-med
  - 85s-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
source:
  ref: spirit-stepper-7-5s-med-service-manual
  locator: 7.5S (RS9600-SS021) service manual 7. Trouble Shooting, 7.3 Abnormal SPM
    Reading (7.3.1 and 7.3.2), PDF p. 45; text.md lines 586-604. 8.5S (MS2000-SB036-01)
    service manual 7. Troubleshooting, 7-4 Optical Sensor Board No Respond, PDF p.
    42; text.md lines 591-600, and 6-8 step 1 which repeats the 7-9 mm figure (PDF
    p. 35, lines 494-499)
  extracted_at: '2026-09-11'
---

Both books end their mechanical troubleshooting chapter with the same sensor and the same figure.

**7.5S - 7.3 Abnormal SPM Reading.**

- *7.3.1 Check for Optical Sensor Board of Encoder.* Check whether the connecting cable of the optical sensor board of encoder is loose or not. The distance between **bar code sticker** and the optical sensor board of encoder should be between **7 ~ 9mm**.
- *7.3.2 Check for Optical Sensor Board of RPM.* Check whether the connecting cable of the optical sensor board of RPM is loose or not. The distance between the optical sensor board of RPM and the **screw head** should be between **1 ~ 2mm**.

**8.5S - 7-4 Optical Sensor Board No Respond.**

> Check whether the wiring of the Optical Sensor Board is loose. The distance between the Optical Sensor Board and the barcode sticker on the Steel Cable Slide Wheel should be **7-9 mm**. Loosen the screws to adjust it (left and right).

**Two sensors on the 7.5S, one on the 8.5S.** The 7.5S has an encoder sensor reading a barcode sticker on the cable guide wheel (7 to 9 mm) *and* an RPM sensor reading the flywheel's bolt heads (1 to 2 mm); the 8.5S keeps the encoder sensor at the same 7 to 9 mm and replaces the RPM sensor with an angle sensor and magnet on the brake shaft, which has its own figure (`85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap`). Do not look for a 1 to 2 mm bolt-head gap on an 8.5S.

**Cable first, gap second, and the gap is set by slotted screws.** Neither page prints a voltage; the electrical checks for the same board (5 V on pins 1 and 3, the Sensor Test counters) are the step-graph procedure earlier in both books (`spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm`).

**The 7.5S contents page promises a section this chapter does not print.** It lists *7.3 Sway of Swivel Seat* and *7.4 Abnormal SPM Reading*; the body has no swivel-seat section and numbers Abnormal SPM Reading as 7.3. The swivel seat is covered by the CRS800S book instead, under maintenance.
