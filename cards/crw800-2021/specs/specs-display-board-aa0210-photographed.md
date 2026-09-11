---
id: crw800-2021-specs-display-board-aa0210-photographed
title: The display board photographed is an AA0210-V1.0 with an on-board 2.4 GHz radio
  module, a WRITER header and no wire-connection drawing
kind: fact
question: What display board is in the Spirit crw800-2021 rower console, and which
  sockets does the service manual show on it?
asked_as:
- what board is in the crw800 console
- aa0210 display board
- crw800 pcb component locations
- where does the rf module sit on the crw800 console board
keywords:
- display board
- pcb
- aa0210
- console board
- rf module
- jk13
- jk4
- writer
- component locations
- 2.4 ghz
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2021
  applies_to:
  - crw800-2021
  section: specs
  code: '*'
  model_number:
  - '800940'
authority: 3
not_to_be_confused_with:
- spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module
see_also:
- crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 6-1 Display Board PCB Component Locations, 6-1-1 PCB BOARD TOP and 6-1-2
    PCB BOARD BOTTOM, PDF pp. 25-26 (printed 24-25), text.md lines 356-377; one photograph
    read from a 110 dpi render (OCR supplement lines 1379-1399 is rotated)
  extracted_at: '2026-09-11'
---

**One photograph, no diagram, no pin table.** Section 6-1 prints a single board photo under the
headings *PCB BOARD TOP* and *PCB BOARD BOTTOM*; the two headings share the one picture, and no
page draws what plugs into which socket. Identify the board from the silkscreen:

- **AA0210-V1.0-200619** (top right), fab code **SJ-2028**, RoHS mark.
- A **2.4 GHz radio module** soldered at the top left, with a **16.000** crystal and a printed
  antenna - this is the receiver for the handlebar's RF level control.
- Sockets, by their silkscreen: **JK4** (red two-way, bottom left), **JK13** (the long white
  multi-way socket at the bottom - the system cable), **JK5 WRITER** (programming header, right),
  **RF** (a white two-way at the right edge), and **U100** (a five-pin header, top right).
- The buzzer sits at the top left; the LCD's flex lands along the top edge.

The 2016 CRW800 and the XRW600 use an older **AA0127** board on which the same functions sit at
different socket names (`spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module`).
Which system-cable lines carry what is not defined anywhere in this book - the circuit diagram
names an 11-pin computer cable and stops there
(`crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable`).

