---
id: crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1
title: 'The tension motor plug has five pins, M+ on pin 1: M+, M-, +5V, VR, GND, and
  the later book prints no pin list at all'
kind: spec
question: What are the five pins of the tension motor connector on a Spirit crw800-2016
  rower?
asked_as:
- tension motor connector pins on the crw800
- which pin is m plus on the spirit rower gear motor
- 5 pin gear motor plug crw800
- does the crw800 2020 manual give the motor pinout
keywords:
- tension motor
- gear motor
- connector
- pinout
- 5-pin
- m+
- m-
- +5v
- vr
- steel rope
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2016
  applies_to:
  - crw800-2016
  section: specs
  code: '*'
  model_number:
  - '800945'
authority: 3
not_to_be_confused_with:
- xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
- sole-bike-tension-motor-connector-pinout
see_also:
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-xb-specs-gear-motor-connector-5-pin-definition
- spirit-crw800-2016-xrw600-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: Tension Motor connector definition function, PDF p. 27 (printed 26), text.md
    lines 352-369, native pin list beside a photograph. The 2020-version CRW800 book
    (spirit-rower-crw800-2021-service-manual) heads the same section 6-1-3 TENSION
    MOTOR (GEAR MOTOR) CONNECTOR DEFINITION FUNCTION at the foot of PDF p. 27 (lines
    378-383), prints a photograph cut off by the page edge, and leaves PDF p. 28 blank;
    the embedded image (pdfimages) is the bare motor with no pin labels
  extracted_at: '2026-09-11'
---

**M+ is pin 1 here.** The CRS800S and CS800 stepper books number the same five signals the other
way round, M- on pin 1 (`spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1`);
the XRW600's motor has eight pins and no VR (`xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor`).

The photograph shows the gear motor with its **STEEL ROPE** on the white drum and a five-way plug
labelled **MAIN CONTROL**, numbered 5 down to 1 on the housing:

| Pin | Signal |
|---|---|
| 1 | **M+** |
| 2 | **M-** |
| 3 | **+5V** |
| 4 | **VR** |
| 5 | **GND** |

M+ and M- are the motor windings - the pair the E2 test meters as "blue wire" and "green wire"; +5V,
VR and GND are the position potentiometer. **No wire colours are printed on this page**; the
five wires in the photo are brown, red, orange, yellow and one more under the sleeve, in no
stated order.

This is the same pin order as the Spirit ellipticals and XB bikes of the period
(`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`,
`spirit-xb-specs-gear-motor-connector-5-pin-definition`).

## The 2020-version book has the heading and not the table

The CRW800 (2020) book (800940) carries the same section heading, *6-1-3 TENSION MOTOR (GEAR
MOTOR) CONNECTOR DEFINITION FUNCTION*, at the very bottom of its p. 26, with a photograph that
runs off the page; the next page is blank. The embedded picture is the motor alone - no numbers,
no labels. **That book defines no motor pins**, and its motor is photographed with a five-way plug
of the same shape. Do not tell a caller with the 2020 machine that the book gives a pinout.

