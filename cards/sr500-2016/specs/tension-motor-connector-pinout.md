---
id: sr500-2016-tension-motor-connector-pinout
title: Tension motor connector pin definitions
kind: spec
question: What are the tension motor connector pinouts on a Sole sr500-2016 rower?
asked_as:
- 8 pin cable pinout on a sole rower
- what are the pins on the cable tensioner plug
- speed sensor connector wiring sr500
keywords:
- connector
- pinout
- 8-pin
- control socket
- power socket
- speed sensor
- m+
- m-
- count
- zero
facets:
  brand:
  - sole
  product_line: rower
  model: sr500-2016
  applies_to:
  - sr500-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sr500-2016-tension-motor-spec
- sr500-2016-e2-motor-error
source:
  ref: sole-rower-sr500-2016-service-manual
  locator: Section 6, Tension Motor connector definition function
  extracted_at: '2026-09-04'
---

The tension motor carries three sockets.

**POWER SOCKET, 3 pins**

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | / (printed as a slash, no signal named) |
| 3 | Vin |

**CONTROL SOCKET, 8 pins**

| Pin | Signal |
|---|---|
| 1 | SPEED |
| 2 | GND |
| 3 | VCC |
| 4 | ZERO |
| 5 | COUNT |
| 6 | M- |
| 7 | M+ |
| 8 | Vin |

**SPEED SENSOR SOCKET, 2 pins**

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | SPEED |

The drawing also labels the motor terminals **M+** and **M-** and shows the **steel rope** leaving the motor.

This 8-pin control cable is the one the E2 troubleshooting table tells you to check at the motherboard.
