---
id: spirit-xe-2016-specs-unit-block-diagram-no-driver-board
title: 'Block diagram with no driver board: the power switch feeds the display board,
  which drives the tension motor and reads the RPM sensor directly'
kind: spec
question: What does the unit block diagram of a Spirit XE195, XE295 or XG400 elliptical
  show?
asked_as:
- xe195 block diagram
- does the xe295 have a lower control board
- xg400 signal flow between the boards
- where does the tension motor connect on the xe195
keywords:
- block diagram
- display board
- no driver board
- tension motor
- rpm sensor
- power switch
- cooling fan
- hr handlebar
- wireless hr receiver
- thumb switch
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram
see_also:
- spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
- spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor
- spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
- spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers
source:
  ref: spirit-elliptical-xe195-2016-service-manual
  locator: 'XE195-2016: section 5 Unit Block Diagrams, Elliptical Configuration, PDF
    p. 24 (printed 24), text.md lines 395-401. XE295-2016: PDF p. 24, lines 403-409.
    XG400-2016: PDF p. 22, lines 342-348. All flattened images read from 300 dpi renders
    (OCR supplement lines 1394-1412, 1389-1409, 1033-1053)'
  extracted_at: '2026-09-11'
---

Three books print one drawing with a single board:

**Into the DISPLAY BOARD:** HR HANDLEBAR, KEY, WIRELESS HR RECEIVER, **RPM SENOR** (spelt so), and
**POWER -> POWER SWITCH** straight into the board.
**Display board and TENSION MOTOR** - a double-headed arrow.

That is the whole drawing: seven blocks. **There is no driver board, no fuse, no transformer, no
thumb switch and no cooling fan block.** The console board is the only electronics
on the machine: the DC adapter's jack and the power switch feed it, and it drives the gear motor
and reads the speed sensor through the 14-pin loom down the mast. That is why these three books'
"driver board" pages photograph the console board, and why a dead console on them is an adapter or
connector fault before anything else (`spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers`).

The XE395 and CE850 add a mains-fed driver board for their AC actuator
(`spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram`).

