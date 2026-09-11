---
id: cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
title: Four leads on the CS22002 display board and three on the CS11002-1 interface
  board of the 2016 stepper, whose photograph shows EMS, HP, H-INC and H-RES sockets
  too
kind: spec
question: What plugs into the display board and the console interface board on a Spirit
  cs800-2016 stepper?
asked_as:
- cs800 2016 display board connections
- cs22002 board sockets
- cs11002-1 interface board on the stepper
- what is the wp socket on the cs800 console board
keywords:
- display board
- cs22002
- interface board
- cs11002-1
- main key
- fan
- wp
- handgrip pulse sensor
- system wire
- ems
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: specs
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
- ce850-2016-specs-display-board-cs22002-and-interface-board-connections
see_also:
- cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
- cs800-2016-specs-unit-block-diagram-climber-configuration
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 6-1 Display Board wire Connections, PDF p. 24 (printed 24), text.md lines
    377-382 (flattened; read from a 110 dpi render, OCR supplement 1198-1210); 6-2
    PCB Board Top/Bottom photographs, PDF pp. 25-26, lines 383-395 (supplement 1213-1247);
    6-3 The console Interface Board wire Connections, PDF p. 27, lines 396-401 (supplement
    1250-1260); the interface-board photograph with silkscreen names, PDF p. 38, lines
    545-567
  extracted_at: '2026-09-11'
---

**Display board - CS22002, four leads drawn**

| Socket | Lead |
|---|---|
| **J4** | FAN |
| **J2** | MAIN KEY |
| **J1** | INTERFACE |
| **J6** | WP |

*WP* is the wireless pulse receiver. The photographs show the same **CS22002** board (silkscreen
CS22002, CoreStar) with an LED matrix and seven-segment windows.
**The system cable does not land on the display board**: J1 goes to the interface board, which
carries the cable.

**Interface board - CS11002-1, three leads drawn**

| Socket | Lead |
|---|---|
| **J2** | HANDGRIP PULSE SENSOR |
| **J1** | HANDGRIP PULSE SENSOR |
| **J6** | SYSTEM WIRE |

The photograph of the same board on the pin-definition page shows more silkscreen than the
drawing names: **J7 EMS**, **J3 HP**, **J1** and **J2 HP1**, **J5 H-INC**, **J4 H-RES** (a blue
socket), **J6 INTERFACE** (the 10-way system-wire socket, numbered 10 down to 1) and **J13**. The
H-INC and EMS sockets are unused on a stepper with no incline; the board is shared with the
ellipticals (`ce850-2016-specs-display-board-cs22002-and-interface-board-connections`, where the
same CS22002 carries seven leads). The 10-way socket's pins are on
`cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down`.

