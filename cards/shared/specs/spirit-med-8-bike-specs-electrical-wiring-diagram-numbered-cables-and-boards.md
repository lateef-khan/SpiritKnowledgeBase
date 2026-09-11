---
id: spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
title: Electrical wiring diagram with the CS31003-1 console board, the CS51009 lower
  control board, a Mean Well power supply module and a drive-pulley magnet sensor,
  every cable numbered the same on the upright and the recumbent
kind: spec
question: What does the electrical wiring diagram of the Spirit Medical 8.0U or 8.5R
  bike service manual show, and which cable number goes where?
asked_as:
- 8.0u wiring diagram
- 8.5r wiring diagram
- what is cable 089 and 090 on the 8.0u
- where does the data transfer board connect on the 8.5r
keywords:
- wiring diagram
- cs31003
- cs51009
- lower control board
- lcb
- power supply module
- ac power entry module
- data transfer board
- cable numbers
- magnet sensor
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
see_also:
- spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds
- spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v
- 85ue-2025-specs-electrical-wiring-diagram-renumbered-parts
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
- 80u-2025-specs-component-description-twenty-two-numbered-parts
- 85r-2025-specs-component-description-fourteen-numbered-parts
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: '8.0U: 4.3 Electrical Wiring Diagram, PDF p. 17 (printed 17/51), text.md
    lines 318-324, and the same sheet again as 8. Electrical System Wiring Diagram,
    PDF p. 51, lines 945-951; a flat drawing read from 130 and 300 dpi renders (OCR
    supplement lines 1126-1162 is partial). 8.5R: 4.3, PDF p. 16 (printed 16), lines
    249-250 (OCR 883-924), and 8., PDF p. 45, lines 687-688; the same sheet. Circuit
    Board text, 8.0U PDF p. 18, lines 324-328; 8.5R PDF p. 17, lines 250-254'
  extracted_at: '2026-09-11'
---

The upright and the recumbent print **one identical sheet**, and print it twice each - as section
4.3 and again as the last page. Every part and cable carries a **# number**, the book's own item
numbers, which the troubleshooting chapter uses again ("cables #089 and #090", "the #072 cable").

**Boards and parts**

| # | Part | Sockets drawn |
|---|---|---|
| #070 | **Console**, with its board **CS31003-1** | USB, J6, J5, J9, J4, **J3** |
| #091 | **Lower Control Board**, **CS51009** | J5, J6, J8, J4, J2, CN1, CN2; LEDs D14, D13, D12, D5 |
| #081 | **Power Supply Module** | CN100 (DC out), CN1 (AC in) |
| #076 | **AC Power Entry Module with Switch and Fuse** | #077 Neutral, #078 Line, #079 earth, #080 to the PSU |
| #084 | **Magnet Sensor** reading the **#045-2 Magnet** on the drive pulley | into LCB **J5** |
| #086 | **Brake and Angle Sensor** - the electromagnetic brake with its angle-sensor board | two leads into **CN1** and **CN2** |
| #071 | **Data Transfer Board** - a DB9 and a USB-B under the machine | cables #72 and #74 |

**Cables**

| # | From | To |
|---|---|---|
| **#089 / #090** | LCB **J4** | console **J3** - one lead with an inline join; the console's 12 V and UART |
| **#083** | LCB **J2** (DC 24V) | PSU **CN100** |
| **#072** | drawn inside the LCB from **J8** to **CN2** | - |
| **#73 / #72** and **#75 / #74** | the console (which two of its sockets is not legible on the sheet) | data transfer board, each an inline pair |
| **#080** | AC entry module | PSU **CN1** |

**How the power flows** (4.4.1): the power supply module makes **24 VDC** for the whole machine; the
LCB "converts it to 12 VDC for the console and supplies power to the angle and magnet sensors", and
"sensor readings are used to control resistance on Brake #086"
(`spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds`,
`spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v`).

**The numbers are the same numbers in both parts lists** - 70 Console Assembly, 72-75 the two
PHP-9 and two XHP-4 connecting wires, 76 AC Electronic Module, 81 Switching Power Supply, 84 Hall
Module, 86 Flywheel, 89-90 the two XHP-6 connecting wires, 91 Generator/Brake Controller - so here,
unlike the 8.5S stepper book, the circuit-board sentence and the diagram agree.

**One label to read carefully.** The no-revolutions procedure calls the Hall-sensor lead "the #072
cable", and the parts list makes 72 a 1350 mm PHP-9 wire; on the sheet **#072** is written on the
LCB's internal J8-to-CN2 line and the magnet sensor's lead into J5 carries no number. Trust the
procedure's meaning - the sensor lead - not the sheet's placement.

The 8.5UE prints the same topology with every part renumbered
(`85ue-2025-specs-electrical-wiring-diagram-renumbered-parts`); the 8.5S stepper sheet is the same
drawing on a climber (`85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards`).

