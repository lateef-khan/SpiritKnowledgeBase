---
id: spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
title: 'Measuring the tension motor drive voltage on the incline stepper: 5.5 to 6
  volts either way, then the fuse in the power socket, then the drive-board power
  LED'
kind: procedure
question: How do I test the tension motor voltage on a Spirit XS895 stepper?
asked_as:
- xs895 tension motor voltage test
- incline stepper no resistance what to measure
- xs895 fuse location for the resistance motor
keywords:
- tension motor
- voltage test
- 20vdc
- level up
- level down
- fuse
- power socket
- power led
- drive board
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led
- cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
- crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
see_also:
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
- spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse
- sc200-2016-tension-motor-voltage-test
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE, PDF p. 30 (printed 29); text.md
    lines 437-457
  extracted_at: '2026-09-11'
---

**This is the test the `E2` page sends you to** (`spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor`). Its band is the highest of the four Spirit stepper books and it is the only one that ends at a fuse.

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading: **+5.5~6.0VDC**. Motor operates. Resistance increases.
4. Press LEVEL DOWN. Normal reading: **-5.5~6.0VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, inspect **power socket the holder FUSE**. If broke replace it.
6. Inspect the **drive board POWER LED** whether lit. If no lit the drive board is bad. Replace it.

**Fuse, then LED.** The XS895 is a mains machine with an incline motor, so it carries a fused AC inlet; no drive voltage sends you to that fuse first, and only a fused, lit drive board that still puts out nothing is condemned. The same fuse is the last check for a console that does not light (`spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse`).

**Four Spirit stepper books, three bands:** 4 to 5 V on the CS800 (2020), 4 to 5.5 V on the CRS800S, 4 to 6 V on the CS800 2016, 5.5 to 6.0 V here. The tables before this procedure quote 5 V; measure against the band. Sole's SC200 2016 prints the same 5.5 to 6.0 V band (`sc200-2016-tension-motor-voltage-test`).
