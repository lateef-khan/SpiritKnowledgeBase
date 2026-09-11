---
id: 85ue-2025-specs-electrical-wiring-diagram-renumbered-parts
title: The wiring diagram is the touchscreen bike sheet with every part renumbered
  - LCB 084, power supply 075, brake 079 - and no cable numbers at all
kind: spec
question: What does the electrical wiring diagram of the Spirit 8.5UE upper body ergometer
  (85ue-2025) service manual show, and which item numbers does it use?
asked_as:
- 8.5ue wiring diagram
- what is part 084 on the 8.5ue
- ube wiring diagram lower control board
- 8.5ue data transfer board connection
keywords:
- wiring diagram
- cs31003
- cs51009
- lower control board
- lcb
- power supply module
- ac power entry module
- data transfer board
- item numbers
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
see_also:
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
- 85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v
- 85ue-2025-specs-component-description-nineteen-numbered-parts
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 4.3 Electrical Wiring Diagram, PDF p. 16 (printed 16), text.md lines 224-227
    (OCR supplement lines 721-757), and the same sheet as 10. 8.5UE Wiring Diagram,
    PDF p. 60, lines 612-613 (OCR 1228-1249); read from a 110 dpi render. Circuit
    Board text, PDF p. 17, lines 227-231
  extracted_at: '2026-09-11'
---

The sheet is the 8.0U/8.5R drawing - the same boxes, the same sockets, the same lines - but the
numbers on it are this book's own parts-list numbers and **no cable is numbered**.

| Part on the sheet | 8.5UE number | The same part on the 8.0U/8.5R sheet |
|---|---|---|
| Console, board CS31003-1 (USB, J6, J5, J9, J4, J3) | **#061** | #070 |
| Lower Control Board, CS51009 (J5, J6, J8, J4, J2, CN1, CN2) | **#084** | #091 |
| Power Supply Module (CN100, CN1) | **#75** | #081 |
| Brake and Angle Sensor | **#079** | #086 |
| Magnet Sensor | **#078** | #084 |
| Magnet | **#211** | #045-2 |
| AC Power Entry Module with Switch and Fuse | **#070** | #076 |
| earth / Neutral / Line leads at the entry module | **#073 / #071 / #072** | #079 / #077 / #078 |
| Data Transfer Board | **#065** | #071 |

The circuit-board text uses the same numbers: "Lower Control Board (#084) ... Power Supply #075
provides 24 VDC to the LCB ... Brake #079", and the parts list agrees (84 Generator/Brake Controller,
75 Switching Power Supply, 78 Hall Module, 79 Flywheel). **Do not carry an 8.0U number onto this
machine**: #084 is the Hall sensor on the 8.0U and the LCB here.

Because the cables are unnumbered, the troubleshooting chapter says only "check if cables are
properly connected" where the 8.0U book names #089 and #090 and #072. The parts list still has them
- 63 a 1300 mm connecting wire, 64 a 550 mm PHP-6, 66-69 the PHP-9 and XHP-4 pairs, 82-83 the two
XHP-6 wires - so the same inline pairs run to the console and the data transfer board.

The 8.0U/8.5R sheet with its cable numbers is
`spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards`; the boards are the
same (`85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds`,
`85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v`).

