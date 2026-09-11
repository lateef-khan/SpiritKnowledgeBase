---
id: xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
title: The tension motor carries an 8-pin main-control plug, VIN to SPEED, and a 2-pin
  speed-sensor plug, GND and SPEED
kind: spec
question: What are the pins of the tension motor connectors on a Spirit xrw600-2019
  rower?
asked_as:
- xrw600 tension motor connector pinout
- 8 pin gear motor plug on the spirit rower
- which pin is count or zero on the xrw600 motor
- speed sensor plug pins xrw600
keywords:
- tension motor
- gear motor
- connector
- pinout
- 8-pin
- vin
- mt+
- mt-
- count
- zero
facets:
  brand:
  - spirit
  product_line: rower
  model: xrw600-2019
  applies_to:
  - xrw600-2019
  section: specs
  code: '*'
  model_number:
  - '600976'
authority: 3
not_to_be_confused_with:
- crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1
- spirit-xs895-specs-tension-motor-8-pin-plug-unnamed-and-2-pin-speed-sensor
see_also:
- xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
- spirit-crw800-2016-xrw600-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v
source:
  ref: spirit-rower-xrw600-2019-service-manual
  locator: Tension Motor connector definition function, PDF p. 27 (printed 26), text.md
    lines 365-367; the pin lists are inside the photograph and were read from a 110
    dpi render (OCR supplement lines 1211-1226 is rotated)
  extracted_at: '2026-09-11'
---

**Eight pins, not the five of the CRW800's motor** (`crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1`).
The XRW600's gear motor has two sockets on its side, a white eight-way at the top and a white
two-way below it.

**MAIN CONTROL (8-way)**

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **VIN** | 5 | **ZERO** |
| 2 | **MT+** | 6 | **VCC** |
| 3 | **MT-** | 7 | **GND** |
| 4 | **COUNT** | 8 | **SPEED** |

**SPEED SENSOR (2-way)**: 1 **GND**, 2 **SPEED**.

VIN is the adapter's 12 V coming in through the motor - the block diagram sends the adapter to the
motor and the motor to console socket J13, and the E2 page says the motor "supply the console DC12V
power". COUNT and ZERO replace the potentiometer of the five-pin motor: the console reads the
brake position as a count from a zero mark (the console's engineering-mode MANUAL test displays
"the motor COUNTER value"). SPEED on pin 8 is the same line as the two-way sensor plug's SPEED.

**No wire colours are printed.** The E2 test still tells you to meter "blue wire" and "green
wire" for MT+/MT-, copied from the CRW800 text.

The XS895 incline stepper's motor has the same two sockets, but its book numbers the eight pins
without naming them (`spirit-xs895-specs-tension-motor-8-pin-plug-unnamed-and-2-pin-speed-sensor`).

