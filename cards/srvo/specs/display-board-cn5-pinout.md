---
id: srvo-display-board-cn5-pinout
title: Pinout of CN5 on the SRVO display main board
kind: spec
question: What is the pinout of CN5 on the SOLE SRVO display board?
asked_as:
- srvo cn5 pinout
- what are the pins on the srvo display power connector
- where does the srvo display get 12v
keywords:
- cn5
- pinout
- rs485
- 12v
- power connector
- ground
- display main board
- wiring
- five pin
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn5
authority: 3
not_to_be_confused_with:
- srvo-display-board-cn1-debug-pinout
- srvo-display-board-speaker-port-pinout
see_also:
- srvo-display-board-connector-map
- srvo-controller-cn6-rs485-pinout
source:
  ref: sole-srvo-service-manual
  locator: page 31, section 8-1-1
  extracted_at: '2026-09-04'
---

**CN5 is on the display main board and carries both the 12V supply and the RS485 bus. It is the only CN5 in the manual.**

| Pin | Name | Description |
|---|---|---|
| 1 | 12V | +12V DC Power Supply |
| 2 | GND | Ground |
| 3 | RS485_A | RS485_A |
| 4 | RS485_B | RS485_B |
| 5 | GND | Ground |

This is the display end of the bus that runs to the controller module. **The controller end of the same bus is printed with its name and description columns disagreeing on pins 3 and 4** - see the controller RS485 card before you make up a cable.
