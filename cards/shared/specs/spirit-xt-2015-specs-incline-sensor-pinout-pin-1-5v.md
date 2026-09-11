---
id: spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v
title: 'Incline position sensor: pin 1 is 5 volts, pin 2 the position signal, pin
  3 ground'
kind: spec
question: What is the pinout of the 3-pin incline position sensor on a Spirit XT185-2015
  or XT285-2015 treadmill?
asked_as:
- incline vr pinout xt185
- which pin is 5 volts on the xt285 incline sensor
- incline potentiometer wires xt185 2015
- incline motor wire colours xt285
keywords:
- incline sensor
- position sensor
- vr
- potentiometer
- pinout
- 3 pin
- 5vdc
- position signal
- incline motor
- wire colour
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt285-2015
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
- f65-2016-incline-position-sensor-wiring
see_also:
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- spirit-xt-2015-errors-incline-buttons-vr-or-power-wires
source:
  ref: spirit-treadmill-xt185-2015-service-manual
  locator: 'XT185-2015: PDF p. 49 (printed 48), Incline motor wire define, text.md
    lines 797-812; incline test at PDF p. 50-51, lines 862-865. XT285-2015: p. 50,
    lines 855-870; test p. 52, lines 930-933'
  extracted_at: '2026-09-11'
---

**3-pin VR (position sensor) plug**: **GND**, **SENSOR PIN (AD)**, **+5V VCC**, in the order the drawing
numbers them. The incline test on the next page then says: **"Pin 1 = 5vdc, Pin 2 = position signal
0~5vdc, Pin 3 = ground"** - which is the drawing read from the other end.

**Incline power wires**: **Com - white**, **UP - red**, **DOWN - black**, on the driver board's JK80.

So in these two books pin 1 of the sensor plug is the 5-volt supply. **The XT385 / XT485 books of the
same year, every 2023 XT book and both ENT books print the opposite** - pin 1 ground, pin 3 5vdc - and the
CT850 books do too. Meter the plug before you trust either table; the position signal is on pin 2 in all
of them.
