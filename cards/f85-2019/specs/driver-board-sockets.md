---
id: f85-2019-driver-board-sockets
title: Driver board sockets and what plugs into each
kind: spec
question: What plugs into each socket on the driver board of a Sole F85-2019 treadmill?
asked_as:
- what are the sockets on the treadmill controller
- where does the speed sensor plug into the board
- which connector is the incline power
keywords:
- driver board
- sockets
- connectors
- incline power output
- incline vr
- main socket
- speed sensor socket
- ac power input
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2019-main-control-cable-pinout
- f85-2019-incline-position-sensor-pinout
- f85-2019-driver-board-leds
source:
  ref: sole-tm-f85-2019-service-manual
  locator: section 6.4 Driver Board Wire Connections, printed page 45
  extracted_at: '2026-09-04'
---

| Socket | What it is | What plugs in |
|---|---|---|
| JK80 | Incline power output | The 3 incline power wires. **Com** is the common power, white incline power wire. **UP** raises the incline, red incline power wire. **DOWN** lowers it, black incline power wire. |
| JK60 | Incline VR socket | The incline 3 pin VR wire, the position sensor cable. |
| JK90 | MAIN socket | The 6 pin main control wire up to the console. |
| JK50 | Speed sensor socket | The 2 pin speed sensor wire. |
| M+ / M- | Drive motor terminals | **M+** takes the red motor wire, **M-** takes the black motor wire. |
| AC POWER INPUT | Mains in | Marked 110V or 220v. |

**The block diagram of the board** shows the mains path as L and N through a varistor, an X capacitor (safety CAP), a fuse and a bridge, then a filter capacitor to the IGBT and out to M+ and M-. A transformer feeds the main IC. Separate relays drive the incline UP and DOWN outputs. The main IC also takes the MAIN CONTROL connector, the SPEED SENSOR input and the INCLINE VR input.
