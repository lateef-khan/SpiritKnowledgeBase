---
id: spirit-cr800-cu800-2021-specs-unit-block-diagram
title: Block diagram with a USB charger, a CSAFE function outside and a program-upload
  USB port inside the console
kind: spec
question: What does the unit block diagram of a Spirit CR800 or CU800 2020-version
  bike show?
asked_as:
- block diagram of the cu800 2020
- how are the boards connected on the cr800
- where is the program upload usb port on the cu800
- cr800 configuration diagram
keywords:
- block diagram
- display board
- driver board
- generator
- brake
- rpm sensor
- usb charger
- program upload usb port
- csafe function
- cooling fan
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cu800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800ent-cu800ent-specs-unit-block-diagram
see_also:
- spirit-cr800-cu800-2021-specs-circuit-diagram
- spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
source:
  ref: spirit-bike-cu800-2021-service-manual
  locator: 'CU800(2020): section 5 Unit Block Diagrams, PDF p. 16 (printed 15), text.md
    line 263, a flattened image read from a 300 dpi render (OCR supplement lines 926-948,
    upside down). CR800(2020): PDF p. 16 (printed 15), line 243 (OCR lines 1163-1185).
    The same drawing in both'
  extracted_at: '2026-09-11'
---

Read from the render.

**Into the display board:** HR (WIRELESS), HR (HANDLEBAR), and one box split in two - **CSAFE
FUNCTION (OUTSIDE)** and **PROGRAM UPLOAD USB PORT (INSIDE)** - drawn with arrows both ways.
**Out of the display board:** COOLING FAN, USB CHARGER.
**Display board and driver board** exchange signals both ways.
**Into the driver board:** GENERATOR and RPM SENSOR. **Out of the driver board:** BRAKE, drawn as
the lower half of the same box as the generator.

Two things the picture tells you that the text does not:

- The console has **two USB ports**: a charger the rider sees, and a program-upload port inside
  the console that only a technician reaches.
- The RPM sensor is read by the **driver board**, not the console - the schematic confirms it,
  with the RPM lead on the generator controller.

No mains, adapter or switch block is drawn: the generator is the only power source.

