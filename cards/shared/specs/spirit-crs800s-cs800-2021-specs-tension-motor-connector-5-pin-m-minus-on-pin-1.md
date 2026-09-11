---
id: spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
title: 'The M-100A tension motor plug has five pins, M- on pin 1: M-, M+, +5V, VR,
  GND, headed Generator Flywheel on the upright''s page'
kind: spec
question: What are the five pins of the tension motor connector on a Spirit CRS800S
  or CS800 (2020 version) stepper?
asked_as:
- tension motor plug pins on the crs800s
- which pin is m minus on the cs800 gear motor
- m-100a motor connector
- generator flywheel definition function cs800
keywords:
- tension motor
- gear motor
- m-100a
- connector
- pinout
- 5-pin
- m-
- m+
- vr
- steel rope
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - cs800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1
- cvc800-tension-motor-connector-at-the-motor
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- sole-bike-tension-motor-connector-pinout
see_also:
- cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 'CRS800S: Tension Motor Connector definition function, PDF p. 17 (printed
    17), text.md lines 237-258, native pin list beside a photograph. CS800(2020):
    6-1-5 GENERATOR FLYWHEEL DEFINITION FUNCTION, PDF p. 24 (printed 23), lines 341-364,
    the same photograph and list'
  extracted_at: '2026-09-11'
---

**M- is pin 1.** The CRW800 rower and the Spirit ellipticals and XB bikes number the same five
signals with M+ on pin 1 (`crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1`,
`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`); the CVC800 vertical climber
prints this order on one page and VR1/VR2 on another (`cvc800-tension-motor-connector-at-the-motor`).

Both books photograph a blue **M-100A** gear motor with its **Steel Rope** on the white drum and a
five-way plug labelled **MAIN CONTROL**, numbered 1 at the top to 5 at the bottom:

| Pin | Signal |
|---|---|
| 1 | **M-** |
| 2 | **M+** |
| 3 | **+5V** (the CS800 page prints "+5") |
| 4 | **VR** |
| 5 | **GND** |

The wires visible in the photograph are brown, red, orange and yellow with one more hidden; **no
colour-to-pin order is printed**. The E2 test meters "blue wire" and "green wire" for the motor
pair in the text and "palm wire" and "black wire" in its own photo caption - the books do not
agree with themselves on colours, so identify M-/M+ by pin position.

**The CS800 (2020) book heads this page "GENERATOR FLYWHEEL DEFINITION FUNCTION".** There is no
generator on either machine; the heading is a template slip over a photograph of the same gear
motor, and the rest of that book calls it the tension motor or gear motor. At the console end the
same five lines are pins 1-5 of the system cable, MTR-, MTR+, 5V, MTR_AD, GND
(`crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines`).

