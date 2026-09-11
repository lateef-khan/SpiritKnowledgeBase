---
id: cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
title: 'Measuring the tension motor drive voltage on the 2020-book stepper: 4 to 5
  volts up, minus 4 to 5 down, then the transformer'
kind: procedure
question: How do I test the tension motor voltage on a Spirit cs800-2021 stepper?
asked_as:
- cs800 tension motor voltage test
- stepper shows err what do i measure
- how to check the resistance motor on a spirit stepper with a meter
keywords:
- tension motor
- voltage test
- 20vdc
- level up
- level down
- transformer
- blue wire
- green wire
- err
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2021
  applies_to:
  - cs800-2021
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
- cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
see_also:
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
- cvc800-tension-motor-voltage-test
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: 7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE, PDF p. 29 (printed 28); text.md
    lines 462-476
  extracted_at: '2026-09-11'
---

**This is the test behind `Err` in the LEVEL window** (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`), and its band is **4 to 5 V** - half a volt narrower than the CRS800S sold beside it (`crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer`) and the CVC800. The 2016 CS800 book prints yet another band, 4 to 6 V.

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading: **+4~5VDC**. Motor operates. Resistance increases.
4. Press LEVEL DOWN. Normal reading: **-4~5VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, check the **transformer**, if there is no output, replace it.

**The caption disagrees with step 1.** Under the photograph the same page reads *Place probes on the motor control wire (Red probe in palm wire, Black probe in black wire) on the drive board.* Both are reproduced because the book gives no way to choose; the connector pin map on the next page (`MTR-` pin 1, `MTR+` pin 2 of the 14-pin console-to-driver connector) is the way to identify the pair.

**Two tables before the test use the same band.** The tension motor operation and troubleshooting pages of this book both say `Level UP: +4~5VDC; Level DOWN: -4~5VDC`, and the troubleshooting page adds the sequence: if the key beeps the signal was sent; if there is power to the motor and it does not run, replace the motor; if there is no power, inspect whether the transformer has power.

**No test is printed for the feedback side.** `Err` is defined as the feedback signal missing; this procedure measures only the drive. Pin 4 of the same connector is `MTR_AD`, the feedback line, and the book prints no figure for it.
