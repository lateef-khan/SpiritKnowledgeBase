---
id: ce800ent-driver-board-connections
title: Driver board connections on the elliptical
kind: spec
question: What connects to the driver board on a Spirit ce800ent elliptical?
asked_as:
- what plugs into the ce800 driver board
- where does the brake coil wire go
- ac input on the elliptical controller
- ce800ent lower board wiring
keywords:
- driver board
- controller
- rpm sensor
- brake coil
- ac l
- ac n
- controller cable
- connector
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: specs
  code: '*'
  model_number:
  - '800054'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-console-transfer-board-connections
- ce800ent-unit-block-diagram
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: p. 19 (printed 19), section 6 'Driver Board PCB Component Locations and
    Wire Connections'
  extracted_at: '2026-09-08'
---

Five connections are called out:

- **RPM sensor**
- **Brake coil wire**
- **Controller cable**
- **AC L (input)**
- **AC N (input)**

The driver board takes AC directly, which is why the block diagram on p. 16 runs the on/off
switch module to both the power board and the controller.
