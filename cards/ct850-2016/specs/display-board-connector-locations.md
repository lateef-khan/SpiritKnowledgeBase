---
id: ct850-2016-display-board-connector-locations
title: Display board connectors and what plugs into each
kind: spec
question: Which connector on the CT850-2016 display board takes which cable?
asked_as:
- what plugs into jk13 on the ct850
- where is the safety connector on the display board
- ct850 2016 display board connectors
- which socket is the keyboard on the console board
keywords:
- display board
- pcb
- connector
- socket
- jk10
- jk13
- jk21
- keyboard
- safety
- wireless hr
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
  model_number:
  - '850845'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-console-12-pin-connector-pinout
- ct850-2016-display-board-small-connector-pinouts
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 24 (printed 23) 'PCB Board Bottom' under 6.1, and the same photo with
    pin numbering on p. 39 (printed 38)
  extracted_at: '2026-09-08'
---

The display board sits behind the console. Its bottom side carries every cable connector; the
top side carries only the display (a dot-matrix panel, a row of 14-segment characters and three
seven-segment groups). The board is marked **ST8100-U23-B** on a DYACO label.

| Connector | Cable | Pin numbering as drawn |
|---|---|---|
| JK13 | Cooling fan | 1 2 3 4, left to right |
| JK21 | Contact HR handlebar | 4 3 2 1, left to right |
| JK10 | System cable, 12 pins | 1 at the bottom up to 12 |
| JK9 | Safety | 1 at the bottom up to 3 |
| JK5 | Wireless HR | 1 2 3 |
| JK6 | Key board | 1 at the top down to 9 |
| JK19 | Writer (programming header) | not numbered |

Signal names for JK10 are on their own card. Signal names for the rest are on the
small-connector pin-definition card.
