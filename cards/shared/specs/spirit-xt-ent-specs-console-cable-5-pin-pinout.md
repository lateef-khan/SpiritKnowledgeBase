---
id: spirit-xt-ent-specs-console-cable-5-pin-pinout
title: 'The 5-pin computer cable: SW, +12V or VDD, TXD, RXD, GND'
kind: spec
question: What is the pinout of the 5-pin computer cable on a Spirit XT485ENT or XT685ENT
  treadmill?
asked_as:
- 5 pin computer cable pinout xt485 ent
- which pin is 12 volts on the xt685ent console cable
- ent treadmill system cable pins
- jk11 pinout
keywords:
- 5 pin
- computer cable
- system cable
- pinout
- pin define
- jk11
- txd
- rxd
- 12v
- vdd
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt485ent-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-console-cable-6-pin-pinout
see_also:
- spirit-xt-ent-specs-driver-board-connectors
- xt485ent-2023-specs-display-board-sockets
- xt685ent-2023-specs-display-board-sockets
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: 'XT485ENT-2023: PDF p. 57 (printed 57), section 8.7 Circuit Diagram, ''5
    PIN COMPUTER CABLE DEFINE'', text.md line 856 (render); the Pin define page, PDF
    p. 44, lines 621-634, is a drawing numbered 1-5 with no table. XT685ENT-2023:
    PDF p. 37, section 8.8 Circuit Diagram, line 626 (render); Pin define p. 31, lines
    502-508, drawing only'
  extracted_at: '2026-09-11'
---

| Pin | XT485ENT sheet | XT685ENT sheet |
|---|---|---|
| 1 | SW | SW |
| 2 | **+12V** | **VDD** |
| 3 | TXD | TXD |
| 4 | RXD | RXD |
| 5 | GND | GND |

The table is printed only on the circuit diagram; the "Pin define" page in each book is a drawing of the
plug numbered 1 to 5 with no signal names. The cable runs in three lengths - UPPER, MIDDLE and LOWER on
the XT485ENT sheet - and lands on **JK11** of the driver board.

Pin 2 is the console supply: "+12V" on the XT485ENT sheet, "VDD" on the XT685ENT sheet. The XT485ENT
display board has a "12Vdc TRANSFER BOARD" socket, which is the same supply. No wire colours are printed
for this cable.

The non-ENT XT machines use a 6-pin cable whose pin 2 is TXD; do not carry the numbering across.
