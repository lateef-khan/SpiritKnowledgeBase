---
id: f60-2016-console-to-controller-pinout
title: Pinout of the connector between console and controller
kind: spec
question: What is the console to controller pinout on a Sole F60-2016?
asked_as:
- pinout of the computer cable on my treadmill
- what are the pins on the main control wire
- wiring of the console connector
keywords:
- pinout
- 5-pin
- main signal wires
- txd
- rxd
- vdd
- gnd
- sw
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f60-2016-e5-error-code
- f60-2016-incline-position-sensor-test
source:
  ref: sole-tm-f60-2016-service-manual
  locator: page 48, Test configuration under 8.3
  extracted_at: '2026-09-04'
---

The console connects to the driver board on a **5-pin main control wire**.

| Pin | Signal |
|---|---|
| 1 | SW |
| 2 | VDD |
| 3 | TXD |
| 4 | RXD |
| 5 | GND |

The SW line carries the +12V safety switch loop from the lower controller up to the display board. The TXD/RXD pair carries the speed and incline signals. A pressured or fractured 5-pin wire, or slid pins, is the usual cause of a communication error.

The 3-pin incline position connector is a different connector, and its wiring is on the incline sensor test card.
