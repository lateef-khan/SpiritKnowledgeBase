---
id: f60-2020-console-to-controller-pinout
title: Pinout of the connector between console and controller
kind: spec
question: What is the console to controller pinout on a Sole F60-2020?
asked_as:
- pinout of the computer cable on my treadmill
- what are the pins on the main control wire
- wiring of the console connector
keywords:
- pinout
- 5-pin
- main control wires
- txd
- rxd
- gnd
- sw
- 12v
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2020
  applies_to:
  - f60-2020
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f60-2020-e5-error-code
- f60-2020-incline-position-sensor-wiring
- f60-2020-no-display-with-safety-key
source:
  ref: sole-tm-f60-2020-service-manual
  locator: page 45, Test Configuration under 8.4
  extracted_at: '2026-09-04'
---

The console connects to the driver board on a **5-pin main control wire**.

| Pin | Signal |
|---|---|
| 1 | SW |
| 2 | +12V |
| 3 | TXD |
| 4 | RXD |
| 5 | GND |

The SW line carries the safety key signal, and the TX/RX pair carries the speed and incline signals.

**Caution**: the troubleshooting matrix names a **12 PIN** computer cable in its cause column for a dead display, while its solution column and the rest of the manual say 5-pin. Check the connector on the machine before ordering.
