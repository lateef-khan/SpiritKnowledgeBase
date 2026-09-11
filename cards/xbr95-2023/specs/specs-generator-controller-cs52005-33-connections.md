---
id: xbr95-2023-specs-generator-controller-cs52005-33-connections
title: 'Four sockets on the CS52005-33 generator controller: three-phase generator
  in, DC coil to the generator brake, main connect system cable, RPM sensor'
kind: spec
question: What plugs into the generator controller of a Spirit xbr95-2023 recumbent
  bike, and what are the two flywheel leads?
asked_as:
- what plugs into the xbr95 controller
- cs52005-33 board
- which socket is the brake on the xbr95 controller
- generator wire xbr95 2023
keywords:
- generator controller
- driver board
- cs52005-33
- j1
- j2
- j3
- j4
- 3-phase gen in
- dc coil
- main connect
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2023
  applies_to:
  - xbr95-2023
  section: specs
  code: '*'
  model_number:
  - '951123'
authority: 3
not_to_be_confused_with:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
see_also:
- xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
- spirit-cr800-cu800-2021-specs-generator-controller-connections
- xbr95-2023-specs-electrical-configuration-generator-brake
source:
  ref: spirit-bike-xbr95-2023-service-manual
  locator: 6.4 Generator Controller Wire Connections, PDF p. 11 (printed 11 of 28),
    text.md lines 169-173 (OCR supplement lines 887-893); 6.5 PCB component locations,
    6.6 connections and 6.7 Generator Brake Definition Function, PDF p. 12, lines
    175-190 (OCR 899-926). Photographs read from a 300 dpi render
  extracted_at: '2026-09-11'
---

**The board is drawn as CS52005-33** (CoreStar), and its photograph shows the sockets silkscreened
with their functions:

| Diagram | Silkscreen | Lead, as captioned on p. 12 |
|---|---|---|
| **J1** | 3-PHASE GEN IN | **Generator Power** - the three-wire lead off the stator |
| **J4** | DC COIL | **Generator Brake Resistance** - the two-wire lead off the brake coil |
| **J2** | MAIN CONNECT | **System Cable** to the console |
| **J3** | RPM | **RPM Sensor** |

**The flywheel (6.7)** is captioned **Generator Power** on the stator lead and **Generator
Resistance voltage** on the coil lead - the same two names the 2020-version CR800/CU800 books use
(`spirit-cr800-cu800-2021-specs-generator-controller-connections`), and the same flywheel unit is
photographed. No voltage is printed for either lead.

**The circuit diagram labels the leads by colour and the labels cross.** It sends a *WHITE, BLACK,
RED wire* "TO J1" under the caption *TO Brake*, and a *RED wire* "TO J4". J1 is the generator
input and J4 the coil, so the three-colour lead is the generator and the red lead the brake; the
*TO Brake* caption sits on the wrong lead.

The 2016 XBR95 controller was a different board, 031101B, with CN-numbered sockets:
`spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections`.

