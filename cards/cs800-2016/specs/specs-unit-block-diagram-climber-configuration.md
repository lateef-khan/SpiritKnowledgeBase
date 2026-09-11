---
id: cs800-2016-specs-unit-block-diagram-climber-configuration
title: Unit block diagram titled Climber Configuration, with power through a power
  switch into the display board and no fan, USB or Bluetooth
kind: spec
question: What does the unit block diagram of the Spirit cs800-2016 stepper service
  manual show?
asked_as:
- block diagram of the cs800 2016
- climber configuration diagram xs200
- what feeds the display board on the 2016 cs800
- does the 2016 cs800 have bluetooth on the block diagram
keywords:
- block diagram
- climber configuration
- display board
- power switch
- hr handlebar
- key
- wireless hr receiver
- tension motor
- rpm sensor
- xs200-ss003
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: specs
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
see_also:
- cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
- cs800-2016-specs-circuit-diagram-xs200-ss003-with-an-external-ac-adapter
- crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 5. XS200-SS003 Unit Block Diagrams, 'CLIMBER Configuration', PDF p. 22
    (printed 22), text.md lines 365-370, a flattened image read from a 110 dpi render
    (OCR supplement 1170-1188 is rotated)
  extracted_at: '2026-09-11'
---

The generic Dyaco block diagram of the period - the same drawing the 2016 CRW800 rower book prints
(`crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar`), here titled **CLIMBER
Configuration**.

**Into the DISPLAY BOARD from the left:** WIRELESS HR RECEIVER, KEY, HR HANDLEBAR.

**Below it:** POWER -> **POWER SWITCH** -> DISPLAY BOARD; **TENSION MOTOR** <-> DISPLAY BOARD
(double-headed - drive out, position back); **RPM SENOR** [sic] -> DISPLAY BOARD.

**Seven blocks, and nothing else.** No cooling fan, USB charger or Bluetooth appears, although the
same book's display-board page has a FAN socket and its console has a fan key
(`cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections`). No adapter
is drawn either; the circuit diagram shows an external AC adapter and no switch
(`cs800-2016-specs-circuit-diagram-xs200-ss003-with-an-external-ac-adapter`). The 2020-version books
redraw the page with the fan, USB and Bluetooth blocks
(`spirit-crs800s-cs800-2021-specs-unit-block-diagram`).

