---
id: spirit-cr800ent-cu800ent-specs-driver-board-connections
title: Five leads on the mains-fed controller - RPM sensor, brake coil wire, controller
  cable, AC L and AC N - and the induction brake's resistance-voltage lead
kind: spec
question: What plugs into the driver board of a Spirit CR800ENT or CU800ENT bike,
  and what does the flywheel lead carry?
asked_as:
- what plugs into the cu800 ent lower controller
- cr800ent driver board connections
- where does the brake coil wire go on the cu800ent
- ac l ac n input on the spirit ent bike controller
keywords:
- driver board
- controller
- rpm sensor
- brake coil wire
- controller cable
- ac l input
- ac n input
- induction brake
- resistance voltage
- flywheel definition
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-generator-controller-connections
- cu900ent-driver-board-connectors
see_also:
- spirit-cr800ent-cu800ent-specs-circuit-diagram
- spirit-cr800ent-cu800ent-specs-power-bridge-board-and-converter
- spirit-xt-ent-specs-driver-board-connectors
source:
  ref: spirit-bike-cu800ent-2022-service-manual
  locator: 'CU800ENT: ''Driver Board PCB Component Locations and Wire Connections'',
    PDF p. 19 (printed 19), text.md lines 277-295, photograph read from a 300 dpi
    render; ''Flywheel definition function'', PDF p. 23, lines 361-376. CR800ENT:
    PDF p. 19, lines 284-302; PDF p. 23, lines 368-383'
  extracted_at: '2026-09-11'
---

**The driver board (p. 19)** is photographed on its heat-sink plate with five call-outs:

| Call-out | Where |
|---|---|
| **RPM Sensor** | small header, top centre |
| **Brake Coil Wire** | the red two-wire plug, left edge |
| **Controller Cable** | the red multi-way plug, top right, on the loom to the power bridge board |
| **AC L (input)** | spade terminal, right edge, upper |
| **AC N (input)** | spade terminal, right edge, lower |

The sticker on the board reads **PA-AE00550** with a barcode beneath it. **The board takes mains
directly** - the AC L and AC N spades are its power input - so it is not interchangeable with the
generator bikes' controller, which has no AC input at all.

**The flywheel (p. 23)** has one call-out on the unit, **Induction Brake**, and one on its lead,
**Resistance Voltage**. That lead is the *brake coil wire* above. No voltage figure is printed.

The treadmill ENT controller is photographed the same way: `spirit-xt-ent-specs-driver-board-connectors`.

