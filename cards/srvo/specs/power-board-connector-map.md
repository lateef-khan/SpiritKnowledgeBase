---
id: srvo-power-board-connector-map
title: Connectors on the SRVO full range power board
kind: spec
question: What connectors are on the full range power board of the SOLE SRVO?
asked_as:
- what plugs into the srvo power board
- srvo power supply connectors
- srvo pfc board ports
keywords:
- full range power board
- pfc
- power supply
- connectors
- ports
- ac input
- dc output
- sockets
- controller module
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- srvo-controller-connector-map
- srvo-display-board-connector-map
see_also:
- srvo-power-board-cn3-ac-input-pinout
- srvo-power-board-dc-output-pinout
- srvo-power-module-specification
- srvo-disassembly-power-board
source:
  ref: sole-srvo-service-manual
  locator: page 39, section 8-3
  extracted_at: '2026-09-04'
---

**Section 8-3 of the manual is headed "Controller module", but the board it describes takes AC in and puts DC out - it is the full range power board, not one of the two motor controllers.** Both headings 8-2 and 8-3 carry the same title in the manual; only the port lists tell them apart.

| No | Port | Description |
|---|---|---|
| 1 | CN3 | AC input port |
| 2 | CN1 | DC output port |
| 3 | CN2 | DC output port |

Two DC outputs, one per controller and so one per servo motor.

Overlaps: **CN3** here has three pins including PE, while CN3 on a controller module has two. **CN1** here is a DC output, while CN1 on the display main board is the debug header. **CN2** here is a DC output, while CN2 on a controller module is the motor power port.
