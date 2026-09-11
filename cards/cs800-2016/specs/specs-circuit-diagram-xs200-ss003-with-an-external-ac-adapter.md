---
id: cs800-2016-specs-circuit-diagram-xs200-ss003-with-an-external-ac-adapter
title: Circuit diagram of the 2016 stepper, with a fan-cooled console, an interface
  board, two hand-pulse grips, an external AC adapter and the M-100A gear motor
kind: spec
question: What does the circuit diagram of the Spirit cs800-2016 stepper service manual
  show?
asked_as:
- cs800 2016 wiring diagram
- xs200-ss003 climber circuit diagram
- what adapter is on the 2016 cs800 schematic
- does the 2016 cs800 have a power switch
keywords:
- circuit diagram
- schematic
- xs200-ss003
- ac adapter
- interface board
- hand pulse
- speed sensor
- m-100a
- gear motor
- console
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
- cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
- crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
see_also:
- cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
- cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
- cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: XS200-SS003 CLIMBER CIRCUIT DIAGRAM, PDF p. 39 (printed 39), text.md lines
    568-574 (the title is native; the drawing is a low-resolution flattened image
    read from a 170 dpi render, OCR supplement 1368-1373)
  extracted_at: '2026-09-11'
---

The sheet is titled **XS200-SS003 CLIMBER CIRCUIT DIAGRAM**. It is a low-resolution raster, and
most of its small labels cannot be read at any zoom.

**Top half:** the console face, drawn with its cooling-fan grille, the LCD window, a row of
program keys down each side and seven keys along the bottom.

**Bottom half:**

- A multi-way computer cable drops from the console into an **interface board** (drawn with its
  sockets - the J6 ten-way along the top edge, two hand-pulse sockets and two more below).
- Two **hand-pulse grips** hang off the interface board's two pulse sockets.
- From the ten-way, three leads go down: to an **AC ADAPTER** block with a mains plug (its model
  code is printed but illegible), to the **SPEED SENSOR**, and to the **M-100A** gear motor, which
  is drawn as a small photograph with its steel rope.

**What it establishes.** The 2016 CS800 runs from an **external adapter** - no appliance inlet,
switch or fuse is drawn, unlike the 2020-version book
(`cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse`) - and the
chain-cover procedure removes "the nut of DC power plug" from the cover, where the jack sits. No
voltage or rating is legible on the drawing; the troubleshooting matrix's "Check AC power is
110-120V" and the safety page's "120-volt, 15-amp (230-volt, 10-amp)" are the book's only mains
figures. The ten-way cable's pins are on
`cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down` and its wire colours
on `cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable`.

