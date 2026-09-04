---
id: f63-2019-console-to-controller-pinout
title: Pinout of the connector between console and controller
kind: spec
question: What is the console to controller pinout on a Sole F63-2019?
asked_as:
- pinout of the computer cable on my treadmill
- what are the pins on the main control wire
- wiring of the console connector
keywords:
- pinout
- main control wire
- 6-pin
- txd
- rxd
- vcc
- gnd
- sw
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2019-e5-error-code
- f63-2019-incline-position-sensor-test
- f63-2019-driver-board-sockets
source:
  ref: sole-tm-f63-2019-service-manual
  locator: page 47, Test configuration under 8.3
  extracted_at: '2026-09-04'
---

The console connects to the driver board on a **6-pin main control wire**, into socket JK90.

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | TXD |
| 3 | RXT |
| 4 | VCC |
| 5 | SW |
| 5 | N/A |

**The table as printed is faulty**: it numbers two rows "Pin 5", while the drawing beside it labels the connector 1, 2, 3, 4, 5, 6. The row shown as the second Pin 5 is pin 6. Confirm on the connector before you rely on it.

The SW line carries the +12V safety switch loop from the lower controller up to the display board. The TX/RX pair carries the speed signal and the incline VR signal.

The 3-pin incline position connector is a different connector, and its wiring is on the incline sensor test card.
