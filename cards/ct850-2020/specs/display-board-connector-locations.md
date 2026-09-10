---
id: ct850-2020-display-board-connector-locations
title: Display board connectors and what plugs into each
kind: spec
question: Which connector on the CT850-2020 display board takes which cable, and how
  many pins does it have?
asked_as:
- what plugs into jk9 on the 2020 ct850
- where is the c-safe connector on the display board
- ct850 2020 display board sockets
- how many pins is the keyboard plug
keywords:
- display board
- pcb
- connector
- socket
- ab0054
- c-safe
- keyboard
- esp
- ble receiver
- pin count
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: specs
  code: '*'
  model_number:
  - '850840'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2020-display-board-connector-pinouts
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: p. 21 (printed 20) and p. 22 (printed 21), '6-1-2 PCB BOARD BOTTOM'; the
    board top is p. 20 (printed 19)
  extracted_at: '2026-09-08'
---

Both pages are flattened images and were read from the 300 dpi renders. The board is silkscreened
**AB0054-V1.0-20200306** and carries a printed label **A512-200309005/900 / BN12AB00540087 /
PA-AB00540**.

Along the bottom edge, left to right:

| Connector | Cable | Pins |
|---|---|---|
| JK12 | RF | 3 |
| GND | ground pad | - |
| JK4 | HAND | 4 |
| JK14 | FAN | 2 |
| JK11 (YT057) | STD | 6 |
| JK8 | SAFETY | 2 |
| JK10 (YT058) | ESP | 2 |
| JK9 (YT058) | RM6Y3 | 6 |
| JK7 | N/C | - |
| JK3 | USB | 4 |
| JK6 | KEYBOARD | 7 |

On the right-hand edge: **U4** takes the **BLE receiver (6 pins)** and **JK2** takes
**C-SAFE (5 pins)**.

The YT057 and YT058 tags mark which driver variant a connector is fitted for.
The board top (p. 20) carries the display only: a dot-matrix panel, a row of 14-segment
characters and two three-digit seven-segment groups.

Two pin counts here disagree with the manual's own pin-definition tables: this drawing calls
JK14 a **2-pin** fan and JK8 a **2-pin** safety, while the tables list **4** pins for JK14 and
three descriptions for JK8. Count the ways on the connector first.
