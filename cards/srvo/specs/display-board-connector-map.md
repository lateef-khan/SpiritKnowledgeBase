---
id: srvo-display-board-connector-map
title: Connectors on the SRVO display main board
kind: spec
question: What connectors are on the display main board of the SOLE SRVO?
asked_as:
- what plugs into the srvo display board
- srvo display board connectors
- what is cn5 on the srvo display
keywords:
- display main board
- connectors
- ports
- console board
- speaker port
- debug port
- rs485
- 12v
- sockets
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
- srvo-power-board-connector-map
see_also:
- srvo-display-board-cn5-pinout
- srvo-display-board-cn1-debug-pinout
- srvo-display-board-speaker-port-pinout
- srvo-controller-connector-map
- srvo-disassembly-display-module
source:
  ref: sole-srvo-service-manual
  locator: page 30, section 8-1
  extracted_at: '2026-09-04'
---

**This is the display main board. The SRVO also has two controller modules and a full range power board, and their connectors reuse the same CN numbers for different things.**

| No | Port | Description |
|---|---|---|
| 1 | CN5 | RS485 and 12V power connector |
| 2 | CN1 | Debug port |
| 3 | CN6 | Left speaker port |
| 4 | CN7 | Right speaker port |

Watch the overlaps before you plug anything in:

- **CN1** here is a debug header. On the full range power board CN1 is a DC output.
- **CN6** here is the left speaker. On a controller module CN6 is the RS485 communication interface.
- **CN7** here is the right speaker. On a controller module CN7 is the encoder port.
