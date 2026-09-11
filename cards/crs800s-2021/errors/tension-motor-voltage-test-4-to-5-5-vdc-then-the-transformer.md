---
id: crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
title: 'Measuring the tension motor drive voltage on the semi-recumbent stepper: 4
  to 5.5 volts up, minus 4 to 5.5 down, then the transformer'
kind: procedure
question: How do I test the tension motor voltage on a Spirit crs800s-2021 semi-recumbent
  stepper?
asked_as:
- crs800s tension motor voltage test
- how to check the resistance motor on my spirit recumbent stepper
- stepper motor error what to measure with a multimeter
keywords:
- tension motor
- voltage test
- 20vdc
- level up
- level down
- transformer
- blue wire
- green wire
- 9-pin cable
- semi-recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: crs800s-2021
  applies_to:
  - crs800s-2021
  section: errors
  code: motor-error
authority: 3
not_to_be_confused_with:
- cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
- cs800-2016-errors-tension-motor-voltage-test-4-to-6-vdc-and-the-drive-board-power-led
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
see_also:
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cvc800-tension-motor-voltage-test
- cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: '8-2 Error Message: Err, Tension Motor Voltage Test Procedure and the Part
    / Troubleshooting table, PDF p. 30 (printed 29); text.md lines 402-427'
  extracted_at: '2026-09-11'
---

**This is the test the `MOTOR ERROR` / `Err` page sends you to** (`crs800s-2024-errors-motor-error-tension-motor-signal-wrong`). Its figures are the CVC800 climber's to the volt (`cvc800-tension-motor-voltage-test`); the CS800 of the 2020 book stops at 5 V, and the XS895 starts at 5.5 V - four steppers, three bands.

1. Put multi-meter to the **20VDC** setting. Place probes on the motor control wire (**Red probe in blue wire, Black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading: **+4~5.5V DC**. Motor operates. Resistance increases.
4. Press LEVEL DOWN. Normal reading: **-4~-5.5V DC**. Motor operates. Resistance decreases.
5. If there is no voltage, check the **transformer**, if there is no output, replace it.

| Part | Troubleshooting |
|---|---|
| Display board | Inspect the 9-pin cable connections. |
| 9-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension Motor | Inspect the display board 5-pin connections. |

**The page names two different wire pairs for the same probes.** Step 1 says red on the **blue** wire and black on the **green**; the caption under the photograph reads *Red probe in palm wire, Black probe in black wire*. The CVC800 book carries the same pair of captions. Identify the motor control pair from the connector pin map on the next page (`MTR-` pin 1, `MTR+` pin 2 of the console-to-driver connector) before probing.

**The book prints two bands for one signal.** The operation table two pages earlier says the console drives the motor at `+4~5VDC` up and `-4~5VDC` down; this procedure, the only one with a pass condition attached, says 4 to 5.5 V. Measure against 4 to 5.5 V.

**No voltage sends you to the transformer**, not to the console - on this machine the console is mains-fed through a transformer, and the drive voltage for the motor is made there.
