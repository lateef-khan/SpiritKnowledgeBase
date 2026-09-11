---
id: ce800-2021-specs-unit-block-diagram
title: Elliptical block diagram with a CSAFE function port outside, a program-upload
  USB port inside, a USB charger, and a generator and brake on the driver board
kind: spec
question: What does the unit block diagram of a Spirit ce800-2021 elliptical show?
asked_as:
- block diagram of the ce800 2020 elliptical
- how are the boards connected on the ce800
- where is the program upload usb port on the ce800
- ce800 signal flow
keywords:
- block diagram
- display board
- driver board
- generator
- brake
- rpm sensor
- csafe function
- program upload usb port
- usb charger
- cooling fan
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2021
  applies_to:
  - ce800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-ce800-2016-2021-specs-electrical-configuration-generator-flywheel
- ce800-2021-specs-display-board-cs24005-connections
- ce800-2021-specs-generator-controller-connections
- ce800-2021-specs-circuit-diagram-xe890e-se027
- spirit-cr800-cu800-2021-specs-unit-block-diagram
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: Section 5 CE800(2020) Unit Block Diagrams, PDF p. 17 (printed 16), text.md
    lines 299-300; the drawing is a flattened image read from a 300 dpi render (OCR
    supplement lines 923-944). The CE800-2016 book has no block-diagram chapter at
    all (its contents list on PDF p. 2, lines 10-44, runs from Outlines to Basic Connections
    with no Unit Block Diagrams entry)
  extracted_at: '2026-09-11'
---

Read from the render; the page carries only the footer as text.

**Into the display board:** HR (WIRELESS), PROGRAM UPLOAD USB PORT (INSIDE), HR (HANDLEBAR).
**Out of the display board:** CSAFE FUNCTION (OUTSIDE), COOLING FAN, USB CHARGER.
**Display board and driver board** exchange signals both ways.
**Into the driver board:** GENERATOR and RPM SENSOR.
**Out of the driver board:** BRAKE.

**Two USB ports, one inside and one outside.** The *program upload* port is inside the console and
is an input to the display board; the *USB charger* is the outlet on the console face. The CSAFE
port is marked "outside" - the socket on the back of the console the C-SAFE feature text describes.

There is **no mains block and no adapter**: the generator is the only power source drawn. **The
CE800-2016 book prints no block diagram at all** - its contents run straight from Electrical
Configurations to Basic Connections and Wiring. The 2020-version CR800/CU800 bikes print this
drawing with the same ten blocks (`spirit-cr800-cu800-2021-specs-unit-block-diagram`).

