---
id: cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led
title: 'Measuring the tension motor drive voltage on the 2016 stepper: 4 to 6 volts
  either way on the black and brown wires, and a dark drive-board power LED condemns
  the console'
kind: procedure
question: How do I test the tension motor voltage on a Spirit cs800-2016 stepper?
asked_as:
- cs800 2016 tension motor voltage test
- stepper e2 what to measure
- drive board power led not lit on my spirit stepper
keywords:
- tension motor
- voltage test
- 12vdc
- level up
- level down
- black wire
- brown wire
- power led
- drive board
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: errors
  code: e2
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
- crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
see_also:
- cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
- sc200-2016-tension-motor-voltage-test
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 8-2 Error Message E2, Tension Motor Voltage Test Procedure and the probe
    caption, PDF p. 35-36; text.md lines 514-531
  extracted_at: '2026-09-11'
---

**This is the test the `E2` page sends you to** (`cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable`), and three things about it are this book's alone: the meter range, the wire colours and the LED.

1. Put multi-meter to the **12VDC** setting. Place probes on the motor control wire (**red probe in black wire, Black probe in brown wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading: **+4.0~6.0VDC**. Motor operates. Resistance increases.
4. Press LEVEL DOWN. Normal reading: **-4.0~6.0VDC**. Motor operates. Resistance decreases.
5. Inspect the **drive board POWER LED** whether lit. If no lit the console is bad. Replace it.

**Black and brown, not blue and green.** Every later Dyaco stepper book puts the red probe on a blue wire and the black on a green one; this book says black and brown, and its photograph (a connector labelled with the wire colours black and yellow among others) does not settle it. Identify the motor pair from the 10-pin map on the E2 page (pins 3 UP and 5 DOWN, or the motor's own leads) before probing.

**The last step is a light, not a measurement.** Where the 2020-book CS800 and the CRS800S send you to a transformer when there is no voltage, this book has you look at the POWER LED on the drive board: dark means the console (which carries the drive board on this generation) is bad. The XS895 book prints the same LED check and adds a fuse before it.

**The band is wider than the tables before it.** The operation and troubleshooting tables say 5 V; this procedure passes 4 to 6 V. Sole's SC200 2016 prints the same procedure (`sc200-2016-tension-motor-voltage-test`).
