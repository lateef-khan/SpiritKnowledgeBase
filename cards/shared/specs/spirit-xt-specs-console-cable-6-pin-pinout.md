---
id: spirit-xt-specs-console-cable-6-pin-pinout
title: 'The 6-pin console cable: GND, TXD, RXT, VCC, SW and a sixth pin that is N/A
  or AC FAN E/D, with the schematic wire colours'
kind: spec
question: What is the pinout of the 6-pin console cable on a Spirit XT185, XT285,
  XT385, XT485 or XT685 treadmill, and what colour is each wire?
asked_as:
- 6 pin computer cable pinout xt385
- which pin is the safety key on the xt console cable
- wire colours of the xt485 main control wire
- what is pin 6 on the xt685 system cable
keywords:
- 6 pin
- console cable
- computer cable
- system cable
- main control wire
- pinout
- pin define
- wire colour
- txd
- rxd
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt685-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-ent-specs-console-cable-5-pin-pinout
- ct800-2016-specs-console-12-pin-cable-pinout
- f63-2016-console-to-controller-pinout
see_also:
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
- spirit-xt-specs-circuit-diagram-codes-and-contents
- spirit-xt-errors-no-display-with-safety-key-6-pin-computer-cable
- spirit-xt-2015-errors-no-display-with-safety-key-6-pin-main-control-wires
source:
  ref: spirit-treadmill-xt185-2015-service-manual
  locator: 'Pin tables: XT185-2015 PDF p. 47 (printed 46), section 8 Pin define, text.md
    lines 779-796; XT285-2015 p. 48, line 853; XT385-2023 p. 27, line 469 (OCR); XT485-2023
    p. 27; XT685-2023 p. 26, line 517 (OCR). Drawing only, no table: XT385-2015 p.
    48, line 712; XT485-2015 p. 48, line 713; XT185-2023 p. 25, line 512; XT285-2023
    p. 26, line 514. Schematic tables: XT185-2015 p. 57, line 1081 (render); XT385-2015
    p. 58, line 894 (render); XT185-2023 pp. 32-33, line 659 (OCR lines 1880-1982)'
  extracted_at: '2026-09-11'
---

Every non-ENT XT service manual from 2015 on has a 6-pin cable between console and driver board. The
books print its definition three different ways.

**Pin-define table (XT185-2015, XT285-2015, and the 2023 XT385 / XT485 / XT685):**

| Pin | 2015 XT185 / XT285 | 2023 XT385 / XT485 / XT685 |
|---|---|---|
| 1 | GND | GND |
| 2 | TXD | TXD |
| 3 | RXT (as printed) | RXT (as printed) |
| 4 | VCC | VCC |
| 5 | SW | SW |
| 6 | **N/A** | **FAN E/D** |

**Schematic table with wire colours (XT185-2015 and XT385-2015 sheets, repeated on the 2023 XT185 /
XT285 sheets):**

| Pin | Colour | XT185-2015 sheet | XT385-2015 and 2023 sheets |
|---|---|---|---|
| 1 | Black | GND | GND |
| 2 | Brown | **RX** | RXD |
| 3 | Red | **TX** | TXD |
| 4 | Orange | VCC | VCC |
| 5 | Yellow | SAFTY KEY (as printed) | SAFETY KEY |
| 6 | Green | N/A | **AC FAN E/D** |

**Drawing only.** The XT385-2015, XT485-2015, XT185-2023 and XT285-2023 pin-define pages show the plug
numbered 1 to 6 and print no signal names at all.

**Two disagreements to know about.** The pin-define table puts TXD on pin 2 and RXT on pin 3; the
XT185-2015 schematic puts RX on 2 and TX on 3 - the same cable named from the other end. And pin 6 is
"N/A" in the XT185 / XT285 books but "AC FAN E/D" (fan enable / disable) on the XT385-family boards,
which drive two AC fans from FAN121 / FAN120.

The ENT machines use a 5-pin cable with +12V and no fan line; the CT800-2016 a 12-pin one. The Sole F63
prints the same six names for its own cable (`f63-2016-console-to-controller-pinout`); it is a
different brand and board.
