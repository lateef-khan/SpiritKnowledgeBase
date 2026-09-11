---
id: spirit-cr900-cu900-2018-specs-circuit-diagram
title: Bike circuit diagram with an LED console and keypad, one console cable, a hybrid
  generator, an RPM sensor and the BLCB002A board
kind: spec
question: What does the circuit diagram of a Spirit CR900 or CU900 2018 bike show?
asked_as:
- wiring diagram for the cu900 2018
- cr900 schematic
- what cables run up the mast on the 2018 cr900
- sr8800 su8800 circuit diagram
keywords:
- circuit diagram
- wiring diagram
- schematic
- console cable
- hybrid generator
- rpm sensor
- blcb002a
- led console
- keypad button
- sr8800
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900-2018
  - cu900-2018
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-circuit-diagram
see_also:
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
- spirit-cr900-cu900-2018-specs-unit-block-diagram
- spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables
source:
  ref: spirit-bike-cr900-2018-service-manual
  locator: 'CR900-2018: ''SR8800/SU8800-SB008 BIKE CIRCUIT DIAGRAM'', PDF p. 29, text.md
    lines 405-411, flattened drawing read from a 300 dpi render (OCR supplement lines
    1363-1402). CU900-2018: ''CU900 BIKE CIRCUIT DIAGRAM'', PDF p. 30, lines 471-477
    (OCR lines 1335-1348). The drawings are identical apart from the title'
  extracted_at: '2026-09-11'
---

The CR900 book titles the page **SR8800/SU8800-SB008** - one drawing covers the recumbent (SR)
and the upright (SU) - and the CU900 book prints the same drawing under its own name.

Five things are drawn, and nothing else:

- **LED CONSOLE AND KEYPAD BUTTON** at the top.
- **CONSOLE CABLE** - a single multi-way cable from the console down the mast to the lower board,
  with a two-way branch spliced into it near the bottom.
- **Hybrid Generator** - the flywheel, drawn with its coil pack, wired to the lower board by two
  leads (the three-wire generator lead and the two-wire brake lead).
- **RPM SENSOR** - a three-way plug on a lead that joins the console cable near the lower board.
- **BLCB002A** - the lower board, with the two generator leads on its left edge and the console
  cable on its right.

**There is no adapter, no DC jack and no mains inlet on the drawing.** Compare
`cu900ent-circuit-diagram`, where the same frame carries a DYA-W10A board fed by a 24 V adapter.

No wire colours, connector numbers or pin numbers are printed on this page; the pin numbers are
on the display-board tables and the connector call-outs on the driver-board photo.

