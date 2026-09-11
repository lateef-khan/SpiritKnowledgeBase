---
id: ce900ent-specs-unit-block-diagram
title: Unit block diagram with DC power and the RPM sensor into the driver board and
  a brake flywheel out, on the ENT elliptical
kind: spec
question: What does the unit block diagram of a Spirit ce900ent elliptical show?
asked_as:
- block diagram of the ce900 ent
- how are the boards connected on the ce900ent
- what feeds the driver board on the ce900ent
- ce900ent signal flow
keywords:
- block diagram
- display console
- driver board
- dc power
- rpm sensor
- brake flywheel
- cooling fan
- hr handlebar
- wireless hr receiver
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: specs
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with:
- ce900-2021-specs-unit-block-diagram
see_also:
- ce900ent-specs-driver-board-dya-w10a-connectors
- ce900ent-specs-ac-adapter-fsp100-rtaan2-24-v-4-17-a
- cu900ent-unit-block-diagram
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Section 5 Unit Block Diagrams, Elliptical Configuration, PDF p. 16 (printed
    16), text.md lines 222-228; the drawing is a flattened image read from a 300 dpi
    render (OCR supplement lines 1449-1474)
  extracted_at: '2026-09-11'
---

Read from the render; the page carries only its heading as text.

**Into the DISPLAY CONSOLE**: HR HANDLEBAR, KEY, WIRELESS HR RECEIVER.
**Out of the display console**: COOLING FAN.
**Display console and DRIVER BOARD** exchange signals both ways.
**Into the driver board**: RPM SENSOR and DC POWER.
**Out of the driver board**: BRAKE FLYWHEEL.

There is no mains block: the elliptical is fed from an external DC adapter. The CU900ENT and
CR900ENT bike books print this drawing unchanged, *Elliptical Configuration* title included
(`cu900ent-unit-block-diagram`). The generator-powered CE900-2021 draws a generator in place of the
DC power block (`ce900-2021-specs-unit-block-diagram`).

