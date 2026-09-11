---
id: spirit-med-40-bike-specs-circuit-diagram-6-pin-computer-cable-to-a-cs52005-controller
title: Circuit diagram with a 6-pin computer cable to a CS52005 generator controller,
  a 3-pin red, white and black generator lead and a 2-pin red brake lead
kind: spec
question: What does the circuit diagram of a Spirit Medical 4.0R or 4.0U bike show,
  and how many pins is the computer cable?
asked_as:
- 4.0r wiring diagram
- 4.0u schematic
- how many pins is the computer cable on the spirit medical 4.0 bike
- what plugs into the controller on the 4.0r
keywords:
- circuit diagram
- wiring diagram
- schematic
- 6 pin computer cable
- cs52005
- generator ac in
- 3 pin
- 2 pin red wire brake
- 2 pin sensor
- generator flywheel
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40u-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables
- spirit-xbr55-xbu55-2023-specs-circuit-diagram-10-pin-computer-cable
see_also:
- spirit-med-40-bike-specs-unit-block-diagram
- spirit-med-40-bike-specs-driver-board-generator-in-brake-out-speed-sensor-and-system-wire
- spirit-med-40-bike-specs-electrical-configuration-generator-brake
- xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
- xbr95-2023-specs-generator-controller-cs52005-33-connections
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: '4.0R: "FR800/FU800-SB022 BIKE CIRCUIT DIAGRAM", PDF p. 29 (printed 29),
    text.md lines 330-336, a flattened drawing read from a 300 dpi render (OCR supplement
    lines 1041-1050 is noise). 4.0U: the same sheet, PDF p. 29 (printed 26), lines
    360-367. Q&A "Display won''t come on", 4.0U PDF p. 47, lines 633-645'
  extracted_at: '2026-09-11'
---

One sheet serves both bikes; it is titled **FR800/FU800-SB022 BIKE CIRCUIT DIAGRAM** in both books
(FR800 is the recumbent 4.0R, FU800 the upright 4.0U) and the recumbent's copy is printed sideways.

- **CONSOLE**, drawn with three side plugs - one lead and two paired boxes, the hand-pulse grips and
  the resistance buttons - joined by **one 6 PIN COMPUTER CABLE** to the controller's **J2**.
- **Controller CS52005** with four sockets: **J1** - *GENERATOR AC_IN, 3 PIN (RED/WHITE/BLACK WIRE)*
  from the stator of the **GENERATOR FLYWHEEL**; **J4** - *2 PIN RED WIRE BRAKE* from the flywheel's
  **BRAKE** coil; **J3** - *2 PIN SENSOR*, the speed sensor; **J2** - the 6-pin computer cable.
- **No mains block, no adapter and no DC jack.** The generator powers the bike; the parts lists name
  the controller *Generator/Brake Controller* and the lead lengths as a 1100 mm generator wire
  harness and an 850 mm (4.0R) or 200 mm (4.0U) red brake coil harness.

**The 4.0U Q&A says nine pins.** Its "Display won't come on" answer reads "Make sure the console and
9 PIN computer Cables are connected properly" and its RPM answer names a "9 PIN Hall Sensor cable".
The drawing, the block diagram and the parts list (a single *2100mm Computer Cable*) say six, and the
4.0R book has no Q&A chapter at all. Read the nine as text carried over from another book.

The same CS52005 board, drawn with the same four sockets and the same colour-labelled leads, is the
2023 XBR95's controller (`xbr95-2023-specs-circuit-diagram-6-pin-computer-cable`), which is why the
XBR95 book's socket photographs are the nearest thing to a pin map for this bike.

