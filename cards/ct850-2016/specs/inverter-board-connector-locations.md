---
id: ct850-2016-inverter-board-connector-locations
title: Inverter board connectors, and the board's own markings
kind: spec
question: Where are the connectors on the CT850-2016 inverter board, and what is the
  board marked?
asked_as:
- where does the console plug into the ct850 inverter
- which plug is the incline vr on the lower board
- ct850 2016 inverter board layout
- what board number is the lower controller
keywords:
- inverter
- lower controller
- driver board
- incline board
- connector
- cn10
- cn13
- tb1
- ac motor power
- rm6t3
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-inverter-board-connector-pinouts
- ct850-2016-treadmill-circuit-diagram
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 25 (printed 24) '6.2 Inverter PCB Component Locations', and the same
    photo with pin numbering on p. 41 (printed 40)
  extracted_at: '2026-09-08'
---

The lower controller is an **RM6T3-1003B** inverter with an incline board on the same heatsink.
The incline board silkscreen reads **PCB:P01818 (RM6T3 INCLINE BOARD) 2013.09.23 V1.1**, and an
RS-485 marking sits beside CN10.

| Connector | What it is | Pin numbering as drawn |
|---|---|---|
| TB1 | AC in | 1 at the bottom up to 2 |
| CN6 | Incline power | 1 at the bottom up to 3 |
| CN10 | Connection to console | 1 2 3 4 5 6 |
| CN13 | Incline VR | 1 2 3 |
| CN4 | Engineering use | not numbered |
| DT-69-B01W-03P | AC motor power U / V / W | 1 at the bottom up to 3 |

The manual prints the motor terminal block as **DT-69-B01W-03** on p. 25 and
**DT-69-B01W-03P** on p. 41. Both call-outs point at the same three-way block.
