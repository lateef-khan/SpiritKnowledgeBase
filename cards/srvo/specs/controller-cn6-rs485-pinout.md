---
id: srvo-controller-cn6-rs485-pinout
title: Pinout of the SRVO controller RS485 communication interface
kind: spec
question: What is the pinout of the RS485 port on a SOLE SRVO controller module?
asked_as:
- srvo rs485 pinout
- srvo controller communication port pins
- which pin is rs485 a on the srvo controller
keywords:
- rs485
- communication interface
- pinout
- cn6
- 12v
- ground
- controller module
- data bus
- wiring
- contradiction
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn6
authority: 3
not_to_be_confused_with:
- srvo-display-board-speaker-port-pinout
- srvo-controller-cn7-encoder-pinout
see_also:
- srvo-controller-connector-map
- srvo-display-board-cn5-pinout
source:
  ref: sole-srvo-service-manual
  locator: page 37, section 8-2-3
  extracted_at: '2026-09-04'
---

**This is CN6 on a controller module, the RS485 communication interface. It is not CN6 on the display main board, which is the left speaker port.**

| Pin | Name | Description |
|---|---|---|
| 1 | 12V | +12V DC Power Supply |
| 2 | GND | Ground |
| 3 | RS485_B | RS485_A |
| 4 | RS485_A | RS485_B |
| 5 | GND | Ground |

**The manual contradicts itself on pins 3 and 4.** The Name column and the Description column give opposite answers for both pins, exactly as reproduced above. The manual offers nothing that settles it.

The far end of the same bus, CN5 on the display main board, is printed consistently: **pin 3 is RS485_A and pin 4 is RS485_B in both columns**. If the two connectors are wired pin for pin, that makes the controller's *Name* column the odd one out - but the manual does not say the cable is straight through. Ring the pair out before you make up or re-terminate this cable.
