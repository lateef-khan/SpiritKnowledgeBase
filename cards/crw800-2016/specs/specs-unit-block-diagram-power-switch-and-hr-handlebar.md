---
id: crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar
title: Unit block diagram with power through a power switch into the display board,
  an HR handlebar, a key block and an RPM sensor
kind: spec
question: What does the unit block diagram of the Spirit crw800-2016 rower service
  manual show?
asked_as:
- block diagram of the 2016 crw800
- cw800-yr001 unit block diagram
- what feeds the display board on the crw800 2016
- does the crw800 2016 have a power switch
keywords:
- block diagram
- display board
- power switch
- hr handlebar
- key
- wireless hr receiver
- tension motor
- rpm sensor
- cw800-yr001
- power
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2016
  applies_to:
  - crw800-2016
  section: specs
  code: '*'
  model_number:
  - '800945'
authority: 3
not_to_be_confused_with:
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
- xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
see_also:
- spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
- spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack
- cs800-2016-specs-unit-block-diagram-climber-configuration
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: 5. CW800-YR001 Unit Block Diagrams, PDF p. 23 (printed 22), text.md line
    348; a flattened image read from a 110 dpi render (OCR supplement lines 1219-1231
    is rotated)
  extracted_at: '2026-09-11'
---

The generic Dyaco block diagram of the period, the same drawing the 2016 CS800 stepper book prints
under the title *CLIMBER Configuration* (`cs800-2016-specs-unit-block-diagram-climber-configuration`).

**Into the DISPLAY BOARD from above:** HR HANDLEBAR, KEY, WIRELESS HR RECEIVER.

**Below it:** POWER -> **POWER SWITCH** -> DISPLAY BOARD; **TENSION MOTOR** <-> DISPLAY BOARD (a
double-headed arrow - drive out, position back); **RPM SENOR** [sic] -> DISPLAY BOARD.

**What it does not match.** The circuit diagram in the same book draws no power switch: a 12 V
1.5 A adapter plugs into a DC jack (`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack`),
and the chain-cover replacement step removes "the Nut of DC Power Cord", not a switch. The
diagram also draws no RF handlebar, although the same book's circuit diagram and its
no-resistance troubleshooting both have one (a *Controller Assembly (36)* with an *RF Module (35)*
on a battery). Treat the block diagram as the template it is; the circuit diagram is the drawing
of this machine.

The 2020-version CRW800 replaces this page with a generator chain and an RF level-control block
(`crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control`).

