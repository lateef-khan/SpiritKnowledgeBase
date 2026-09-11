---
id: 40t-2026-specs-display-board-and-transfer-board-connectors
title: Display board sockets and the two faces of the console back-cover transfer
  board
kind: spec
question: Which connector on the display board and the console transfer board of a
  Spirit 40t-2026 treadmill takes which cable?
asked_as:
- what plugs into the display board on the 4.0t
- where is the csafe socket on the 4.0t console
- cs24002 transfer board connectors
- where does the safety key plug in on the 4.0t
keywords:
- display board
- transfer board
- connector
- socket
- gfit
- csafe
- usb charger
- key pad
- hp/wp
- safety key
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 40t-2026
  applies_to:
  - 40t-2026
  section: specs
  code: '*'
  model_number:
  - '740885'
authority: 3
not_to_be_confused_with:
- ct900-specs-console-back-cover-transfer-board
- ct850-2020-display-board-connector-locations
see_also:
- 40t-2026-specs-unit-block-diagram
- 40t-2026-specs-circuit-diagram
source:
  ref: spirit-treadmill-40t-2026-service-manual
  locator: 'PDF p. 20 (printed 20) ''PCB Board Bottom'', text.md lines 268-296; PDF
    p. 21 ''The console back cover transfer PCB board, Front of the board'', lines
    297-306; PDF p. 22 ''Behind the board'', lines 307-314; OCR supplement lines 1104-1146;
    board marking and J numbers read from the renders. ST8700A-ST026-01 revision (spirit-treadmill-40t-2026-service-manual-st8700a):
    PDF pp. 21-23 (printed 20-22), text.md lines 299-345, the same three photographs'
  extracted_at: '2026-09-11'
---

**Display board, bottom face (p. 20)** - the call-outs printed on the photograph: **GFIT**, **FAN**, **USB
Charger**, **CSAFE**, **KEY PAD**, **HP/WP**, **SAFETY KEY**, **INTERFACE** and **USB**. The top face (p.
19) is a bare photograph. No pin definitions are printed for any of them.

**Console back-cover transfer board (pp. 21-22)** - silkscreened **CS24002-1 V1.0**. The photographs
carry no printed call-outs; the connector names below are the board's own silkscreen, read from the
300 dpi render.

| Front of the board | Behind the board |
|---|---|
| J7 HP-RIGHT | MAIN CONNECTOR |
| J8 HP-LFET (as silkscreened) | R1 |
| J2 MAIN CONNECTOR | HP-SALUTRON |
| J10 EARTH GND | J15 HP-CS |
| J6 HP | J1 EARTH GND |
| J14 & J4 HAND-KEY | J12 KEYPAD |
| J17 SAFETY | J9 SAFETY |
| J3 KEYPAD | J13 & J5 HAND-KEY |

The CT900's transfer board (CS26002-1) uses different J numbers for the same jobs; do not read one board's
J number against the other.

The ST8700A-ST026-01 revision of the same book (spirit-treadmill-40t-2026-service-manual-st8700a) prints this page unchanged; only the product photographs in chapter 2 were replaced by the black Spirit-branded machine.

