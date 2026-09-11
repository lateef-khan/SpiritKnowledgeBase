---
id: ce900-2021-specs-driver-board-blcb002a-connections
title: 'Three leads on the BLCB002A lower board of the generator elliptical: system
  wire, generator input and generator brake output'
kind: spec
question: What connects to the driver board on a Spirit ce900-2021 elliptical, and
  what is the board marked?
asked_as:
- what plugs into the ce900 driver board
- blcb002a board elliptical
- where does the generator wire go on the ce900 lower board
- ce900 elliptical lower controller part
keywords:
- driver board
- lower controller
- blcb002a
- system wire
- generator input
- generator brake output
- cn-6
- cn-7
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
- ce900ent-specs-driver-board-dya-w10a-connectors
see_also:
- ce900-2021-specs-circuit-diagram-se8800-sb026
- ce900-2021-specs-display-board-connector-pin-tables
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
source:
  ref: spirit-elliptical-ce900-2021-service-manual
  locator: Driver Board PCB Component Locations, PDF p. 25, and Driver Board function,
    PDF p. 26 (printed 25-26), text.md lines 416-443; the photographs were read from
    a 300 dpi render (OCR supplement lines 1360-1366)
  extracted_at: '2026-09-11'
---

The driver board is photographed in place on its aluminium plate. Three call-outs:

| Call-out | Where on the board |
|---|---|
| **SYSTEM WIRE** | the multi-way connector at the left end, beside the silkscreen CN-6 / CN-7 |
| **GENERATOR BRAKE OUTPUT** | the red pair at the top right, next to the large capacitor |
| **GENERATOR INPUT** | the three-wire (red / white / black) connector at the bottom right |

The board silkscreen reads **BLCB002A-VA0.1**; the circuit diagram on p. 30 prints the same board
as **BLCB002A**. That is the part to ask for when a "lower controller" is quoted for this machine.

**The RPM sensor does not land on this board.** Its lead runs up the console cable to J16 on the
display board (see the pin tables), which is why the driver board has only three call-outs where
the CE900ENT board has five - see `ce900ent-specs-driver-board-dya-w10a-connectors`, a different
board (DYA-W10A-IMX6-R10) on a different machine. The 2018 CR900/CU900 bikes use this same
BLCB002A board (`spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections`).

