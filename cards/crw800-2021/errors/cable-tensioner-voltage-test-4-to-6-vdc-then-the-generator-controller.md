---
id: crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller
title: 'Measuring the cable tensioner drive voltage on the generator-powered rower:
  4 to 6 volts either way, then the generator controller'
kind: procedure
question: How do I test the cable tensioner voltage on a Spirit crw800-2021 rower?
asked_as:
- crw800 tension motor voltage test
- how to check the rower resistance motor with a meter
- spirit rower level up no voltage
keywords:
- cable tensioner
- tension motor
- voltage test
- 12vdc
- level up
- level down
- generator controller
- blue wire
- green wire
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2021
  applies_to:
  - crw800-2021
  section: errors
  code: e2
  model_number:
  - '800940'
authority: 3
not_to_be_confused_with:
- spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter
- cvc800-tension-motor-voltage-test
see_also:
- crw800-2024-errors-e2-cable-tension-communication-error
- spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter
- crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 7-3 Error Message, Cable tensioner fault / Voltage measurement procedure,
    PDF p. 35 (printed 34); text.md lines 485-503
  extracted_at: '2026-09-11'
---

**This is the CRW800 of the 2021 `800940` book, the generator-powered machine.** The 2016 CRW800 and the XRW600 print the same test with a 5.5 to 6.5 V band and a power adapter in the last step (`spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter`); the numbers here are this book's own. It is the test the `E2` code sends you to (`crw800-2024-errors-e2-cable-tension-communication-error`).

The steps, in the book's numbering (it prints no step 2):

1. Place the multifunction meter at **12VDC**. Place the probe in the motor control line on the drive board (**the red probe is blue wire and the black probe is green wire**).
3. Turn on the power of device to tension motor. The console display lights.
4. Press the LEVEL UP measurement to the normal reading: **+4.0 ~ 6.0VDC**, motor action, resistance increases.
5. Press LEVEL DOWN. Normal reading: **-4.0 ~ -6.0VDC**. Motor work. Resistance decreases.
6. If there is no voltage, please check the **generator controller** socket terminals whether the voltage, if not please change another one controller.
7. If the generator controller can work fine, replace the cable tensioner.

**The band is wider and lower than the 2016 book's** - 4 to 6 V against 5.5 to 6.5 V - and it is the same both ways. The electrical configuration page of this book rates the tension motor's working voltage at `DC 4.0~6.0V`, where the 2016 book says `DC 4.5~7.5V`; the test bands follow the ratings.

**No voltage at all sends you to the generator controller.** This rower has no mains adapter: the generator in the flywheel feeds a controller, and the controller feeds the console and the tensioner. That is why step 6 names the controller, why the LCD row of the same book says *check the battery* and *check the generator* rather than a wall voltage (`crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator`), and why a caller who quotes the 2024 owner's-manual figure of `DC12V` out of an adapter is reading the wrong book.
