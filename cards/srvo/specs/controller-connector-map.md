---
id: srvo-controller-connector-map
title: Connectors on an SRVO controller module
kind: spec
question: What connectors are on a controller module in the SOLE SRVO?
asked_as:
- what plugs into the srvo controller
- srvo controller board connectors
- where does the encoder plug into the srvo
keywords:
- controller module
- connectors
- ports
- motor control board
- ac port
- motor power
- rs485
- encoder port
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
- srvo-display-board-connector-map
- srvo-power-board-connector-map
see_also:
- srvo-controller-cn3-ac-pinout
- srvo-controller-cn2-motor-power-pinout
- srvo-controller-cn6-rs485-pinout
- srvo-controller-cn7-encoder-pinout
- srvo-disassembly-controller
- srvo-encoder-location
source:
  ref: sole-srvo-service-manual
  locator: page 34, section 8-2
  extracted_at: '2026-09-04'
---

**This is a controller module, the board that drives one servo motor. There are two of them. It is not the display main board and not the full range power board, both of which reuse these CN numbers for other things.**

| No | Port | Description |
|---|---|---|
| 1 | CN3 | AC port |
| 2 | CN2 | Motor power port |
| 3 | CN6 | RS485 communication interface |
| 4 | CN7 | Encoder port |

**Item 4 on this board is the encoder *port* - the socket the encoder cable plugs into - not the encoder itself.** The encoder is a sensor on the motor; the manual documents only its connector. An existing knowledge base card drawn from the SRVO seminar says the encoder *is* item 4 on the controller module. Read both before you tell a technician where to look.

Overlaps with the other boards: **CN3** here is a two pin AC port, while CN3 on the full range power board is a three pin AC input. **CN2** here is motor power, while CN2 on the power board is a DC output.
