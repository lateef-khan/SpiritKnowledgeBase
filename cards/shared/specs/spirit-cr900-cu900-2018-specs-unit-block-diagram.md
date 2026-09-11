---
id: spirit-cr900-cu900-2018-specs-unit-block-diagram
title: 'Bike Configuration block diagram: generator into the driver board, generator
  brake out, RPM sensor into the driver board'
kind: spec
question: What does the unit block diagram of a Spirit CR900 or CU900 2018 bike show?
asked_as:
- block diagram of the cu900 2018
- how are the boards connected on the cr900
- what feeds the driver board on the spirit 900 bike
- bike configuration diagram cu900
keywords:
- block diagram
- bike configuration
- display board
- driver board
- generator
- generator brake
- rpm sensor
- cooling fan
- wireless hr receiver
- signal flow
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
- cu900ent-unit-block-diagram
see_also:
- spirit-cr900-cu900-2018-specs-circuit-diagram
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
source:
  ref: spirit-bike-cr900-2018-service-manual
  locator: 'CR900-2018: section 5 ''Bike Configuration'', PDF p. 18, text.md lines
    263-268, flattened image read from a 300 dpi render (OCR supplement lines 1233-1254,
    upside down). CU900-2018: PDF p. 19, lines 325-330 (OCR lines 1165-1186). The
    same drawing in both'
  extracted_at: '2026-09-11'
---

Read from the render; the page is a picture and its extracted text is inverted.

**Into the display board:** HR HANDLEBAR, KEY, WIRELESS HR RECEIVER.
**Out of the display board:** COOLING FAN.
**Display board and driver board** exchange signals both ways.
**Into the driver board:** RPM SENOR (spelt so) and GENERATOR.
**Out of the driver board:** GENERATOR BRAKE.

There is **no mains block and no adapter block**: the generator is the only power source drawn.

**One contradiction inside the same book.** The block diagram takes the RPM sensor into the
*driver* board, but the display-board pin tables two pages later give it a connector of its own
(**J16 RPM**) on the *display* board, and the circuit diagram runs its lead up the console cable.
The pin table and circuit diagram agree with each other; the block diagram is the odd one out.

The page is titled *Bike Configuration*, unlike the CU900ENT book, whose diagram is titled
*Elliptical Configuration* - see `cu900ent-unit-block-diagram`.

