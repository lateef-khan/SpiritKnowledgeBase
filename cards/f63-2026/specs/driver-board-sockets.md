---
id: f63-2026-driver-board-sockets
title: What plugs into each socket on the controller
kind: spec
question: What plugs into each socket on the Sole F63-2026 controller?
asked_as:
- what plugs into the controller on my treadmill
- where does the hall sensor plug in
- motor wires on the 2026 controller
keywords:
- driver board
- controller sockets
- hall sensor
- main socket
- incline vr
- u v w
- ac power input
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2026
  applies_to:
  - f63-2026
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2026-e22-error-code
- f63-2026-e02-error-code
- f63-2026-drive-motor-spec
source:
  ref: sole-tm-f63-2026-service-manual
  locator: pages 25, 29 and 33, 5.1, 5.3 and 5.7
  extracted_at: '2026-09-04'
---

| Socket | What connects to it |
|---|---|
| AC POWER INPUT | Mains in, 110V or 220V. The board diagram labels the two sides POWER IN (LINE) and POWER IN (NEUTRAL) |
| U | Red wire of the motor |
| V | Black wire of the motor |
| W | White wire of the motor |
| Incline power output | **Com** is the common power, connected to the white incline power wire. **UP** inclines up, connected to the red incline power wire. **DOWN** inclines down, connected to the black incline power wire |
| Incline VR socket | The 3-pin VR wire of the incline motor |
| MAIN socket | The **6-pin** control wire to the console |
| Hall sensor socket | The **5-pin** speed sensor wire |

The display board itself is documented separately: it takes a 5-pin upper control board link, a 5-pin display board link, the 6-pin main control wires, a USB Type-C, an NFC GEM4 module, the safety key, the fan, two speakers, and the quick speed and quick incline rotary switches.
