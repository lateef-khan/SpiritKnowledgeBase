---
id: spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
title: 'Circuit diagrams around the 031101B controller: a 9-pin computer cable from
  the console that arrives as 6 pins plus a 3-pin sensor, a 3-pin generator lead and
  a 2-pin red brake wire'
kind: spec
question: What does the circuit diagram of a Spirit XBR95 2016 recumbent or CU800
  2012 upright bike show?
asked_as:
- xbr95 2016 wiring diagram
- xu878 upright schematic
- how many pins is the cu800 2012 computer cable
- 2 pin red wire brake xu878
keywords:
- circuit diagram
- wiring diagram
- schematic
- 031101b
- 9 pin computer cable
- 6 pin computer cable
- 3 pin sensor
- 2 pin red wire brake
- generator power
- hybrid generator
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cu800-2012
  - xbr95-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-circuit-diagram
- spirit-cr800-cu800-2021-specs-circuit-diagram
see_also:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: 'XBR95-2016: ''XR829-SB012-01 BIKE CIRCUIT DIAGRAM'', PDF p. 42, text.md
    lines 585-587, flattened drawing read from a 300 dpi render (OCR supplement lines
    1585-1603). CU800-2012: ''XU878-AB04M UPRIGHT SCHEMATIC'', PDF p. 33, lines 513,
    read from the render (OCR lines 1118-1135, upside down)'
  extracted_at: '2026-09-11'
---

Two drawings of the same electrical layout; the XU878 one is the labelled version.

**CU800-2012, "XU878-AB04M UPRIGHT SCHEMATIC":** the console sends a **9 PIN COMPUTER CABLE** down
the mast; at the bottom a **3 PIN SENSOR** branch leaves it and the remaining **6 PIN COMPUTER
CABLE** enters the **GENERATOR CONTROLLER #031101B** at **CN3**. The **GENERATOR FLYWHEET** (spelt
so) sends **GENERATOR POWER, 3 PIN (RED/WHITE/BLACK WIRE)** to **CN1** and a **2 PIN RED WIRE
BRAKE** to **CN2**.

**XBR95-2016, "XR829-SB012-01 BIKE CIRCUIT DIAGRAM":** the same parts drawn without pin counts or
colours - the console ("XR829 電子錶"), its mast cable and hand-pulse leads, the hybrid generator
with two leads to **CN1** and **CN2**, an **RPM sensor** lead, and the board **#031101B** with
**CN1, CN4, CN2** down its left edge and **CN3** on the right. **CN4 is drawn with nothing on it.**

So 9 = 6 + 3: the console cable and the sensor lead are one loom at the console end, and the
six-pin part is the cable whose pins are defined on
`xbr95-2016-specs-console-to-driver-board-6-pin-definition`. Neither drawing shows an adapter,
DC jack or mains inlet.

