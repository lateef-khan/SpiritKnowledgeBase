---
id: ce900-2021-specs-circuit-diagram-se8800-sb026
title: Elliptical circuit diagram with an LED console and keypad, one console cable,
  a hybrid generator, an RPM sensor and the BLCB002A lower board
kind: spec
question: What does the circuit diagram of a Spirit ce900-2021 elliptical show?
asked_as:
- ce900 wiring diagram
- ce900 elliptical schematic
- what cable runs up the mast on the ce900
- does the ce900 circuit diagram show an adapter
keywords:
- circuit diagram
- wiring diagram
- schematic
- se8800-sb026
- console cable
- hybrid generator
- rpm sensor
- blcb002a
- led console
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900-2021
  applies_to:
  - ce900-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board
see_also:
- ce900-2021-specs-driver-board-blcb002a-connections
- ce900-2021-specs-display-board-connector-pin-tables
- spirit-cr900-cu900-2018-specs-circuit-diagram
source:
  ref: spirit-elliptical-ce900-2021-service-manual
  locator: SE8800-SB026 ELLIPTICAL CIRCUIT DIAGRAM, PDF p. 30 (printed 30), text.md
    lines 481-488; the drawing is a flattened image read from a 300 dpi render (OCR
    supplement lines 1391-1423)
  extracted_at: '2026-09-11'
---

The page is headed **SE8800-SB026** - the book's own cover code is SE8800-SE026, so the drawing
carries a different suffix from the manual. Five things are drawn, and nothing else:

- **LED CONSOLE AND KEYPAD BUTTON** at the top.
- **CONSOLE CABLE** - a single multi-way cable from the console down the mast to the lower board,
  with a two-way branch spliced into it near the bottom.
- **Hybrid Generator** - the flywheel, drawn with its coil pack, wired to the lower board by two
  leads (the three-wire generator lead and the two-wire brake lead).
- **RPM SENSOR** - a three-way plug on a lead that joins the console cable near the lower board.
- **BLCB002A** - the lower board, with the two generator leads on its left edge and the console
  cable on its right.

**There is no adapter, no DC jack and no mains inlet on the drawing.** Compare
`ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board`, where the same frame carries
a DYA-W10A board fed by a 24 V adapter.

No wire colours, connector numbers or pin numbers are printed on this page; the pin numbers are on
the display-board tables and the connector call-outs on the driver-board photo. The 2018 CR900 and
CU900 bikes print the same drawing under SR8800/SU8800-SB008
(`spirit-cr900-cu900-2018-specs-circuit-diagram`).

