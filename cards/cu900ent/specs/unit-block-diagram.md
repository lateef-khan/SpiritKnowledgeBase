---
id: cu900ent-unit-block-diagram
title: Unit block diagram titled Elliptical Configuration, with DC power and the RPM sensor into the driver board
kind: spec
question: What does the unit block diagram of a Spirit CU900ENT upright or CR900ENT recumbent bike show?
asked_as:
- block diagram of the cu900 bike
- how are the boards connected on the cu900ent
- what drives the brake flywheel on the bike
- bike signal flow diagram
keywords:
- block diagram
- display console
- driver board
- brake flywheel
- rpm sensor
- dc power
- cooling fan
- wireless hr
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900ent-2021
  - cu900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-ac-adapter-rating
- cu900ent-driver-board-connectors
- spirit-cr900-cu900-2018-specs-unit-block-diagram
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: "p. 16 (printed 16), section 5 CU900 ENT Unit Block Diagrams. CR900ENT-2021 (spirit-bike-cr900ent-2021-service-manual): PDF p. 15 (printed 15), text.md lines 143-148, the same drawing read from a 300 dpi render (OCR supplement lines 1403-1427)"
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image. The page is titled
**"Elliptical Configuration"** - a copy-paste error in a bike manual.

**Into the display console**: HR HANDLEBAR, KEY, WIRELESS HR RECEIVER.
**Out of the display console**: COOLING FAN.
**Display console and driver board** exchange signals both ways.
**Into the driver board**: RPM SENSOR and DC POWER.
**Out of the driver board**: BRAKE FLYWHEEL.

There is no mains block: the bike is fed from an external DC adapter.

The CR900ENT book prints the same drawing, "Elliptical Configuration" title included. The 2018
CR900/CU900 diagram has a generator in place of the DC power block
(`spirit-cr900-cu900-2018-specs-unit-block-diagram`).
