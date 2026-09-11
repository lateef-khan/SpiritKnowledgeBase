---
id: ce800-2016-specs-circuit-diagram-xe890b-ae10m
title: 'Elliptical schematic around the 031101B controller: a 9-pin computer cable
  at the console that becomes a 6-pin cable at CN3, a 3-pin sensor, and generator
  and brake leads'
kind: spec
question: What does the circuit diagram of a Spirit ce800-2016 elliptical show?
asked_as:
- ce800 2016 wiring diagram
- xe890b schematic
- how many pins is the computer cable on the 2016 ce800
- where does the speed sensor plug in on the ce800 2016
keywords:
- circuit diagram
- schematic
- xe890b-ae10m
- 9 pin computer cable
- 6 pin computer cable
- 3 pin sensor
- generator flywheel
- 2 pin red wire brake
- 031101b
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2016
  applies_to:
  - ce800-2016
  section: specs
  code: '*'
  model_number:
  - '800045'
authority: 3
not_to_be_confused_with:
- ce800-2021-specs-circuit-diagram-xe890e-se027
see_also:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
source:
  ref: spirit-elliptical-ce800-2016-service-manual
  locator: XE890B-AE10M ELLIPTICAL SCHEMATIC, PDF p. 30 (printed 30), text.md lines
    518-519; the drawing is a flattened image read from a 300 dpi render (OCR supplement
    lines 1256-1288)
  extracted_at: '2026-09-11'
---

The drawing is headed **XE890B-AE10M ELLIPTICAL SCHEMATIC**. It has no title in the book's text
layer and sits inside the error chapter.

- **Console** at the top, with one **9 PIN COMPUTER CABLE** down the mast.
- At the bottom a **3 PIN SENSOR** branch leaves the cable, and the remainder enters the
  **GENERATOR CONTROLLER #031101B** at **CN3** as a **6 PIN COMPUTER CABLE**.
- The **GENERATOR FLYWHEET** (spelt so) sends **GENERATOR POWER, 3 PIN (RED/WHITE/BLACK WIRE)** to
  **CN1**, and the **BRAKE** a **2 PIN RED WIRE BRAKE** to **CN2**.

So 9 = 6 + 3: the console cable and the speed-sensor lead are one loom at the console end and split
at the controller. **Neither an adapter, a DC jack nor a mains inlet is drawn** - the generator is
the only power source.

**The book has no block-diagram chapter**; this schematic and the driver-board pages are its
only account of the wiring. The 2012 CU800 bike prints the same layout under XU878-AB04M, with
the same 9 = 6 + 3 split (`spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b`). The
2020-version CE800 redraws the machine with the RPM sensor on the controller and named hand-pulse
cables (`ce800-2021-specs-circuit-diagram-xe890e-se027`).

