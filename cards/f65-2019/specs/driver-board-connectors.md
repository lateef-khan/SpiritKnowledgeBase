---
id: f65-2019-driver-board-connectors
title: Driver board sockets and what plugs into each
kind: spec
question: What are the sockets on the driver board of a Sole f65-2019 treadmill?
asked_as:
- what plugs into jk90 on the treadmill controller
- treadmill controller sockets explained
- where does the speed sensor plug into the controller
keywords:
- driver board
- lower controller
- jk50
- jk60
- jk80
- jk90
- socket
- wiring
- connector
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2019
  applies_to:
  - f65-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2019-console-to-driver-board-pinout
- f65-2019-lower-controller-replacement
source:
  ref: sole-tm-f65-2019-service-manual
  locator: Section 6.4, Driver Board Wire Connections
  extracted_at: '2026-09-04'
---

| Socket | What it connects |
|---|---|
| AC POWER INPUT | Mains in, 110V or 220V |
| M- | Black wire of the motor |
| M+ | Red wire of the motor |
| JK80 | Incline power output. **Com** is the common power, white incline power wire. **UP** raises the incline, red incline power wire. **DOWN** lowers the incline, black incline power wire. |
| JK60 | Incline VR socket, connected to the incline 3-pin VR wire |
| JK90 | MAIN socket, connected to the 6-pin control wire |
| JK50 | Speed sensor socket, connected to the 2-pin speed sensor wire |

The board itself carries a bridge rectifier, IGBT, varistor, X capacitor (safety cap), filter capacitor, fuse, transformer, relay, incline relay and the main IC.
