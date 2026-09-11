---
id: xterra-tr-specs-brake-board-four-callouts
title: 'The brake board between the driver board and the motor: a 3-pin signal and
  power cable to socket 10 of the driver board, an IGBT, and doubled M- and M+ terminals,
  one pair to the driver board and one to the motor'
kind: spec
question: What is the brake board on an Xterra TR hiking treadmill, and what connects
  to it?
asked_as:
- tr95h brake board
- what is the brake module on the tr75h
- tr95h motor wires go to the brake board
- brake board 3 pin cable
keywords:
- brake board
- brake module
- igbt
- m plus
- m minus
- motor wires
- driver board
- 3-pin
- jkexer
- resistor bank
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-tr-specs-driver-board-td-65hs-seventeen-callouts
- xterra-tr-specs-wiring-diagram-with-a-brake-module-and-a-7-pin-computer-cable
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: 'TR95H SM (JKEXER 337) ''9. Brake board PCB main parts & sockets'', PDF
    p. 14, lines 182-193. TR75H SM ''9.'', PDF p. 12 (printed 12), lines 246-264:
    the same photograph and list'
  extracted_at: '2026-09-11'
---

The hiking treadmills put a second board between the controller and the drive motor. Both books photograph it - a
tan PCB on an aluminium plate carrying two rows of six white ceramic power resistors, taped in yellow, with a
"110V / 120V" sticker at the right - and number four things:

| No. | Description |
|---|---|
| 1 | Brake board signal and power cable (3 PIN) - Connect to socket #10 of the driver board. |
| 2 | IGBT (Insulated Gate Bipoler). |
| 3 | M- (2 connectors. One is connected to the M- of the driver board and the other is connected to the negative (-) wire of the driver motor). |
| 4 | M+ (2 connectors, one is connected to the M+ of the driver board, and the other is connected to the positive (+) wire of the driver motor). |

Callout 1 is the small white 3-pin socket at the right edge (silkscreen P1); 2 is the grey IGBT module on the plate
at the top; 3 and 4 are the paired spade terminals at the left edge, silkscreened **M-** (upper pair) and **M+**
(lower pair, J1/J2).

So the motor's two leads land on this board, not on the controller: the wiring diagram draws MOTOR → BRAKE MODULE →
CONTROLLER, with the motor's red wire on the brake module's M+ and its black wire on M-, and a white wire and a black
wire carrying M+ and M- on to the controller. Neither book says what the board does beyond its name; the resistor
bank and IGBT are what the photograph shows.
