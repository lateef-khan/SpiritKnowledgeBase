---
id: f63-2016-driver-board-sockets
title: What plugs into each socket on the driver board
kind: spec
question: What plugs into each socket on the Sole F63-2016 controller?
asked_as:
- what plugs into the controller on my treadmill
- which socket is the speed sensor on the board
- motor wires on the controller
keywords:
- driver board
- jk50
- jk60
- jk80
- jk90
- motor terminals
- incline power
- sockets
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2016
  applies_to:
  - f63-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2016-console-to-controller-pinout
- f63-2016-drive-motor-spec
source:
  ref: sole-tm-f63-2016-service-manual
  locator: page 28, 6.4 Driver Board Wire Connections
  extracted_at: '2026-09-04'
---

| Socket | What connects to it |
|---|---|
| AC POWER INPUT | Mains in, 110V or 220V |
| M+ | Red wire of the motor |
| M- | Black wire of the motor |
| JK80 | Incline power output. **Com** is the common power, connected to the white incline power wire. **UP** inclines up, connected to the red incline power wire. **DOWN** inclines down, connected to the black incline power wire. |
| JK60 | Incline VR socket, connected to the 3-pin VR wire of the incline motor |
| JK90 | MAIN socket, connected to the 6-pin control wire |
| JK50 | Speed sensor socket, connected to the 2-pin speed sensor wire |

The driver board block diagram also shows the bridge, X capacitor (safety cap), varistor, fuse, filter capacitor, IGBT, transformer, incline relay and main IC.
