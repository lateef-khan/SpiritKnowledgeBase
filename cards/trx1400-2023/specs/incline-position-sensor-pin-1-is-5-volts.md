---
id: trx1400-2023-specs-incline-position-sensor-pin-1-is-5-volts
title: 'The incline position sensor plug: pin 1 is 5 V DC, pin 2 the 0 to 5 V position
  signal, pin 3 ground, about 4.5 to 4.7 V on the signal at the lowest position'
kind: spec
question: What are the pins and voltages of the incline motor position sensor (VR)
  connector on an Xterra trx1400-2023 treadmill?
asked_as:
- trx1400 incline sensor pins
- which pin is 5 volts on the trx1400 incline plug
- trx1400 potentiometer voltage at lowest incline
keywords:
- incline position sensor
- vr
- potentiometer
- pin 1
- 5 volts
- position signal
- 4.5 to 4.7 v
- incline power
- up
- down
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
see_also:
- trx1400-2023-specs-electrical-configuration-incline-motor-110-or-230-volt-ac
- trx1400-2023-specs-driver-board-b307d-wire-connections
- spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM 'Test Configuration. Incline motor control function relate parts
    location', PDF p. 49, lines 797-815; 'Test Procedure' steps 5-7, PDF p. 50 (printed
    59), lines 815-865
  extracted_at: '2026-09-11'
---

**This is the T3 book's pin-numbered table; it prints no sensor wire colours.** The TR260 and TRX books print
colours instead (red ground, white signal, black 5 V) on their own card.

The test-configuration photograph labels the 3-pin VR plug **GND**, **SENSOR PIN (AD)**, **+5V VCC** ("Incline One of
3-pin VR wires (It is a position line)"), and the incline power terminals **Com-white**, **UP-Red**, **DOWN-black**.
The test procedure on the next page then states the pins the way the console sees them, "these connections are the
same on the incline board and at the console":

- **Pin 1 = 5vdc**
- **Pin 2 = position signal 0~5vdc**
- **Pin 3 = ground**

and the voltages to expect at the potentiometer: "There should be 5vdc between the black and red wire and there should
be a voltage between the red and white wire. This voltage will be about **4.5~4.7 Vdc when the motor is at the lowest
position** (the number isn't too critical, as long as it's somewhere in this neighborhood)". Those two sentences name
wire colours - black, red, white - without saying which is which pin; the drawing's plug order (GND, SENSOR, +5V) read
from the other end gives pin 1 = 5 V, which is what the procedure prints. The incline board passes the signal
straight through: "There are no electronic components on the board for this signal; there are just circuit
connections from the potentiometer connector to the console connector."

The rest of that procedure - relays clicking, ~110 VAC between white and red or black, the INCLINE window counting
0 to 15 - is the errors section's E3/Err material. The Spirit XT185/XT285-2015 books print the same pin-1-is-5-V order
(`spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v`); most other Spirit XT books print pin 1 as ground.
