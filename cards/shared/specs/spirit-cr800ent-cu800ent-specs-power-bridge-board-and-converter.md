---
id: spirit-cr800ent-cu800ent-specs-power-bridge-board-and-converter
title: The console power bridge board with its 6+2+2-pin computer cable and a DC 13
  V / 4 A converter end, and the power converter's red V+ and black V- leads
kind: spec
question: What are the power bridge board and the power converter on a Spirit CR800ENT
  or CU800ENT bike, and what plugs into them?
asked_as:
- what is the power bridge board on the cu800 ent
- what voltage is the console converter on the cr800ent
- dc 13v 4a converter cu800ent
- which lead is v+ on the spirit ent bike converter
keywords:
- power bridge board
- power converter
- dc 13v
- 4a
- computer cable 6+2+2 pins
- controller cable
- ac_l
- ac_n
- v+ red
- v- black
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-cr800ent-cu800ent-specs-console-transfer-board-and-hdmi-csafe-board
- spirit-cr800ent-cu800ent-specs-circuit-diagram
- spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
source:
  ref: spirit-bike-cu800ent-2022-service-manual
  locator: 'CU800ENT: ''The console POWER BRIDGE PCB board and POWER CONVERTER'',
    PDF p. 20 (printed 20), text.md lines 296-325, photograph read from a 300 dpi
    render; ''Power Converter PCB board'', PDF p. 22, lines 338-360. CR800ENT: PDF
    p. 20, lines 303-332; PDF p. 22, lines 345-367'
  extracted_at: '2026-09-11'
---

**The power bridge board (p. 20)** sits on the converter's heat sink and has seven call-outs:

- **Computer Cable (6+2+2 Pins)** - the loom up to the console, on the two red headers marked
  JK2 (*Data Output*) and JK5
- **DC_13V/4A (Converter End)** - the red and black pair from the converter, on JK3 (silkscreen *12V*)
- **Controller Cable** - the loom down to the driver board, on the header marked *Data Input*
- **AC_L (Output)** and **AC_N (Output)** - spades feeding mains on to the converter
- **AC_N (Input)** and **AC_L (Input)** - spades taking mains in

**The power converter (p. 22)** has four: **POWER CONVERTER V+ (RED)**, **POWER CONVERTER V-
(BLACK)**, **AC_N (AC Output)**, **AC_L (AC Output)**.

**Two figures for one lead.** The photo caption says the converter delivers **DC 13 V / 4 A**; the
schematic labels the same socket on the bridge board **12V POWER INPUT**, and the silkscreen
beside it reads *12V*. The caption is the only place a current is printed. The treadmill ENT
converter carries the same DC 13 V / 4 A caption
(`spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter`).

The silkscreen on the bridge board is photographed but only partly legible; it is not quoted here.

