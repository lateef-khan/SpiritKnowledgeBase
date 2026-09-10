---
id: cvc800-display-board-connectors
title: Display board connectors and the board's markings
kind: spec
question: What are the connectors on the display board of a Spirit cvc800 climber?
asked_as:
- what plugs into the cvc800 display board
- where does the system cable go on the climber console
- bluetooth module on the cvc800 board
- aa0209 board connectors
keywords:
- display board
- aa0209
- connector
- system cable
- wireless hr
- bluetooth
- jk1
- jk6
- u11
- pcb
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: specs
  code: '*'
  model_number:
  - '800440'
authority: 3
not_to_be_confused_with: []
see_also:
- cvc800-console-to-driver-board-connector-pin-map
- cvc800-console-interface-board
source:
  ref: spirit-climber-cvc800-service-manual
  locator: p. 20 (printed 20) 'Display Board wire Connections'; p. 21 (printed 21)
    'PCB Board Top'; p. 22 (printed 22) 'PCB Board Bottom'
  extracted_at: '2026-09-08'
---

The display board is silkscreened **AA0209-V1.0-191231**; the wire-connection drawing calls it
**AA0209**. A second marking **120925A-Y105-200102** sits near the bottom edge.

| Connector | What plugs in |
|---|---|
| JK1, JK14, JK12 | System cable |
| JK6 | Wireless HR |
| U11 | Bluetooth |

The board top (p. 21, a flattened image read from the 300 dpi render) carries the LCD module and
the key switches, each silkscreened with the key it serves: **CARDIO, STRENGTH, HIIT, UP, STOP,
ENTER, MANUAL, HILL, FAT BURN, DOWN, START**.

The tension motor, speed sensor, power and HR receiver connectors on the same board are mapped in
section 8-4.
