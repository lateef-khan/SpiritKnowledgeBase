---
id: spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter
title: 'Measuring the cable tensioner drive voltage on the adapter-powered rowers:
  about 5.5 to 6.5 volts up, minus 5.5 to 6 down, then the power adapter'
kind: procedure
question: How do I test the cable tensioner (tension motor) voltage on a Spirit CRW800
  2016 or XRW600 rower?
asked_as:
- how to test the rower tension motor with a multimeter
- crw800 cable tensioner voltage check
- xrw600 resistance motor not moving what to measure
keywords:
- cable tensioner
- tension motor
- voltage test
- 12vdc
- level up
- level down
- power adapter
- blue wire
- green wire
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - xrw600-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller
- cvc800-tension-motor-voltage-test
see_also:
- crw800-2024-errors-e2-cable-tension-communication-error
- crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller
- sr500-2016-tension-motor-voltage-test
- crw800-2024-errors-lcd-display-does-not-shine
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: CRW800 2016 (CW800-YR001) service manual, Cable tensioner fault / Voltage
    measurement procedure under 8.2 Error Message Code E2, PDF p. 33-34; text.md lines
    446-454. XRW600 (DW400-YR002) service manual, Tension motor fault / Voltage measurement
    procedure under 8.2, PDF p. 33-34; text.md lines 437-446
  extracted_at: '2026-09-11'
---

**This is the test for the two adapter-powered rowers - the CRW800 of the 2016 `CW800-YR001` book and the XRW600.** The generator-powered CRW800 of the 2021 book prints the same test with different figures and a different last step (`crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller`). This is the test the `E2` code sends you to (`crw800-2024-errors-e2-cable-tension-communication-error`).

The steps, in the book's numbering (it prints no step 2):

1. Place the multifunction meter at **12VDC**. Place the probe in the motor control line on the drive board (**the red probe is blue wire and the black probe is green wire**).
3. Turn on the power of device. The console display lights.
4. Press the LEVEL UP measurement to the normal reading: **+5.5 ~ 6.5VDC**, motor action, resistance increases.
5. Press LEVEL DOWN. Normal reading: **-5.5 ~ 6.0VDC**. Motor work. Resistance decreases.
6. If there is no voltage, please check the **power adapter** socket terminals whether the voltage, if not please change another one the power adapter.
7. If the adapter power supply is work fine, replace the cable tensioner.

**The two directions have two different bands, and they are printed that way.** Up is 5.5 to 6.5 V; down is 5.5 to 6.0 V (the book writes the down band without a minus on the second figure - read it as -5.5 to -6.0 V). Neither book explains the asymmetry.

**No voltage at all sends you to the adapter, not to the console.** On these machines the console and the tensioner are fed by an external adapter (the LCD row of the same books asks for `AC100 ~ 240V` in and `DC12V` out, `crw800-2024-errors-lcd-display-does-not-shine`), so a dead adapter looks like a dead tensioner. Prove the adapter before ordering a tensioner.

**The XRW600 book says "tension motor" where the CRW800 book says "cable tensioner".** Same part, same figures, same order of steps; the XRW600's step 7 reads *replace the tension motor*.

The Sole SR500 2016 prints this procedure with the same figures for its own rower: `sr500-2016-tension-motor-voltage-test`.
