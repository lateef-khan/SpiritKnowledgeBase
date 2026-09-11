---
id: spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
title: 'Three leads on the BLCB002A lower board: system wire, generator input and
  generator brake output'
kind: spec
question: What plugs into the driver board of a Spirit CR900 or CU900 2018 bike, and
  what is the board called?
asked_as:
- what plugs into the cu900 lower controller
- cr900 driver board connections
- blcb002a board
- where does the generator wire go on the 2018 cu900
keywords:
- driver board
- lower controller
- blcb002a
- system wire
- generator input
- generator brake output
- cn6
- cn7
- connector
- component locations
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
- cu900ent-driver-board-connectors
see_also:
- spirit-cr900-cu900-2018-specs-circuit-diagram
- spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables
source:
  ref: spirit-bike-cr900-2018-service-manual
  locator: 'CR900-2018: ''Driver Board PCB Component Locations'' PDF p. 24 and ''Driver
    Board function'' PDF p. 25, text.md lines 340-366, both flattened photographs
    read from a 300 dpi render (OCR supplement lines 1340-1345). CU900-2018: PDF pp.
    25-26, lines 406-432 (OCR lines 1290-1309)'
  extracted_at: '2026-09-11'
---

The driver board is photographed in place on its aluminium plate. Three call-outs:

| Call-out | Where on the board |
|---|---|
| **SYSTEM WIRE** | the multi-way connector at the left end, beside the silkscreen CN-6 / CN-7 |
| **GENERATOR BRAKE OUTPUT** | the red pair at the top right, next to the large capacitor |
| **GENERATOR INPUT** | the three-wire (red / white / black) connector at the bottom right |

The board silkscreen reads **BLCB002A-VA0.1**; the circuit diagram on p. 29 / p. 30 prints the
same board as **BLCB002A**. That is the part to ask for when a "lower controller" is quoted for
these two bikes.

**The RPM sensor does not land on this board.** Its lead runs up the console cable to J16 on the
display board (see the pin tables), which is why the driver board has only three call-outs where
the CU900ENT board has five - see `cu900ent-driver-board-connectors`, a different board
(DYA-W10A-IMX6-R10) on a different machine.

