---
id: ce900-2021-specs-unit-block-diagram
title: Elliptical block diagram with the generator and RPM sensor into the driver
  board and the generator brake out, and no mains or adapter block
kind: spec
question: What does the unit block diagram of a Spirit ce900-2021 elliptical show?
asked_as:
- block diagram of the ce900 elliptical
- how are the boards connected on the ce900
- does the ce900 elliptical have an adapter
- ce900 signal flow
keywords:
- block diagram
- display board
- driver board
- generator
- generator brake
- rpm sensor
- cooling fan
- hr handlebar
- wireless hr receiver
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
- ce900ent-specs-unit-block-diagram
see_also:
- ce900-2021-specs-driver-board-blcb002a-connections
- ce900-2021-specs-display-board-connector-pin-tables
- spirit-cr900-cu900-2018-specs-unit-block-diagram
source:
  ref: spirit-elliptical-ce900-2021-service-manual
  locator: Section 5 Unit Block Diagrams, Elliptical Configuration, PDF p. 19 (printed
    19), text.md lines 336-342; the drawing is a flattened image read from a 300 dpi
    render (OCR supplement lines 1235-1255)
  extracted_at: '2026-09-11'
---

Read from the render; the page carries only its heading as text.

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

The 2018 CR900/CU900 bikes print the same diagram under the title *Bike Configuration*
(`spirit-cr900-cu900-2018-specs-unit-block-diagram`); the CE900ENT draws DC power in place of the
generator (`ce900ent-specs-unit-block-diagram`).

