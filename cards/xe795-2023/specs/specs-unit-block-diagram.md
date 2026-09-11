---
id: xe795-2023-specs-unit-block-diagram
title: Block diagram of the 2023 generator elliptical with the RPM sensor and generator
  into the driver board, a USB charger and a speaker on the display board
kind: spec
question: What does the unit block diagram of a Spirit xe795-2023 elliptical show?
asked_as:
- xe795 2023 block diagram
- where does the rpm sensor go on the 2023 xe795
- xe795 signal flow
- does the xe795 block diagram show a usb charger
keywords:
- block diagram
- display board
- driver board
- generator
- generator brake
- rpm sensor
- usb charge
- speaker
- cooling fan
- hr handlebar
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2023
  applies_to:
  - xe795-2023
  section: specs
  code: '*'
  model_number:
  - '795023'
authority: 3
not_to_be_confused_with:
- xe795-2016-specs-unit-block-diagram
- xbr95-2023-specs-unit-block-diagram
see_also:
- xe795-2023-specs-generator-controller-cs52005-23-connections
- xe795-2023-specs-display-board-cs11039-and-interface-board-connections
- xe795-2023-specs-circuit-diagram-6-pin-computer-cable
source:
  ref: spirit-elliptical-xe795-2023-service-manual
  locator: Section 5 Unit Block Diagrams, PDF p. 9 (printed 9), text.md lines 185-191;
    the drawing is a flattened image read from a 300 dpi render (OCR supplement lines
    775-796)
  extracted_at: '2026-09-11'
---

**Into the DISPLAY BOARD:** KEY, HR HANDLEBAR, WIRELESS HR RECEIVER.
**Out of the display board:** COOLING FAN, **USB CHARGE**, **SPEAKER**.
**Display board and DRIVER BOARD** exchange signals both ways.
**Into the driver board:** **GENERATOR** and **RPM SENSOR**.
**Out of the driver board:** **GENERATOR BRAKE**.

Against the 2016 drawing (`xe795-2016-specs-unit-block-diagram`): the **RPM sensor now lands on
the driver board** (the CS52005-23's J3), the amplifier and line-in are replaced by a **speaker**
driven from the display board, and a **USB charge** output appears -
the port the electrical-configuration page calls a wireless charger. **No mains, adapter or fuse
block**: the generator powers everything.

The 2023 XBR95 bike prints the same drawing (`xbr95-2023-specs-unit-block-diagram`).

