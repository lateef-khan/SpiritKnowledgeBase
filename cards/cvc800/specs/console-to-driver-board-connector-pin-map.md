---
id: cvc800-console-to-driver-board-connector-pin-map
title: Console-to-driver-board connector map and the tension motor pins
kind: spec
question: What is the console to driver board connector pin map on a Spirit cvc800
  climber?
asked_as:
- console to driver board pins on the cvc800
- which plug is the speed sensor on the climber board
- tension motor pins at the console board
- cvc800 test configuration connectors
keywords:
- connector
- pin map
- tension motor
- speed sensor
- hr receiver
- power
- display board
- aa0209
- test configuration
- pinout
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: specs
  code: '*'
  model_number: '800440'
authority: 3
not_to_be_confused_with:
- cvc800-tension-motor-connector-at-the-motor
- e25-2016-tension-motor-connector-pinout
- sole-bike-tension-motor-connector-pinout
see_also:
- cvc800-display-board-connectors
- cvc800-tension-motor-voltage-test
source:
  ref: spirit-climber-cvc800-service-manual
  locator: 'p. 33 (printed 33), section 8-4 ''Test configuration: The console to driver
    board connector pin defines function'''
  extracted_at: '2026-09-08'
---

The board is the console's own display board, silkscreened **AA0209-V1.0-191231**. Four
connections are called out:

- **Speed Sensor**
- **Power**
- **HR Receiver** - the five-way header, numbered 1 to 5 down the board
- **Tension Motor**

**Tension motor connector, as printed here:**

| Pin | Signal |
|---|---|
| 1 | M- |
| 2 | M+ |
| 3 | +5V |
| 4 | VR |
| 5 | GND |

**The same connector is printed differently on p. 18**, where pins 3 and 4 are **VR1 and VR2**
rather than +5V and VR. Pins 1, 2 and 5 agree. The manual never reconciles the two.

Sole's ellipticals and bikes print a five-pin tension-motor connector with the same signal names
but **M+ on pin 1 and M- on pin 2** - the opposite way round from Spirit's. Do not carry a Sole
pinout onto this machine.
