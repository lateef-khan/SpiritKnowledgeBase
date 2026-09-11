---
id: spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
title: Circuit diagram with an AA01270 console, a computer cable that splits to the
  speed sensor and a YJ-9900 gear motor, and a 12 V 1.5 A adapter into a DC jack
kind: spec
question: What does the circuit diagram of the Spirit CRW800 (2016) or XRW600 rower
  service manual show?
asked_as:
- xrw600 wiring diagram
- crw800 2016 circuit diagram
- what is the yj-9900 on the spirit rower
- how is the adapter wired on the xrw600
keywords:
- circuit diagram
- schematic
- aa01270
- yj-9900
- gear motor
- dc jack
- 12v 1.5a
- speed sensor
- computer cable
- tx/rx
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - xrw600-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable
see_also:
- spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack
- spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module
- xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: 'CW800-YR001: 8.3 Circuit Diagram, PDF p. 35 (printed 34), text.md line
    455; a flattened drawing read at 300 dpi. DW400-YR002 (XRW600): 8.3 Circuit Diagram,
    PDF p. 35, line 446, the same drawing without the handlebar module; both have
    no OCR supplement because the labels are too small for tesseract'
  extracted_at: '2026-09-11'
---

One drawing in both books, differing in a single item.

**Console.** A five-key console drawn with the board code **AA01270** beside it. A multi-way
**computer cable** drops from it and forks into two plugs.

**Below the fork.** The left plug goes to the **SPEED SENSOR** (a small sensor block with a code
under it that is too small to read even at 500 dpi - the drawing is a low-resolution raster); the
right plug goes to the gear motor, which is drawn as a photograph-style block labelled
**YJ-9900**.

**Power.** A separate lead from the motor runs to a **DC JACK**, into which the barrel plug of an
adapter block marked **12V/1.5A** fits. The adapter is the only power source drawn; nothing goes
straight to the console (`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack`).

**The one difference.** The CRW800-2016 sheet adds a handlebar grip at the top right, labelled
with a code ending **-RF** (the rest is illegible), with a double **TX/RX** arrow to the console -
the wireless resistance buttons. The
XRW600 sheet has no handlebar at all, matching its radio-less board
(`spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module`).

**No pin is defined and no wire colour is printed on the drawing.** The motor's pins are on their
own page in each book, and they differ: five on the CRW800, eight on the XRW600
(`crw800-2016-specs-tension-motor-connector-5-pin-m-plus-on-pin-1`,
`xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor`) - the drawing is a
template that does not show which.

The 2020-version CRW800 book draws a generator-powered circuit instead
(`crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable`).

