---
id: ce800-2021-specs-circuit-diagram-xe890e-se027
title: Elliptical schematic with a 3-pin right and 4-pin left hand-pulse cable, a
  6-pin computer cable, and DC coil, 3-phase generator and RPM leads on the generator
  controller
kind: spec
question: What does the circuit diagram of a Spirit ce800-2021 elliptical show?
asked_as:
- ce800 2020 wiring diagram
- xe890e schematic
- how many pins is the computer cable on the ce800
- which hand pulse cable is 4 pin on the ce800
keywords:
- circuit diagram
- schematic
- xe890e-se027
- 6 pin computer cable
- hand pulse
- 3 pin cable
- 4 pin cable
- dc coil
- 3 phase gen in
- rpm sensor wire
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2021
  applies_to:
  - ce800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800-2016-specs-circuit-diagram-xe890b-ae10m
see_also:
- ce800-2021-specs-generator-controller-connections
- ce800-2021-specs-unit-block-diagram
- spirit-cr800-cu800-2021-specs-circuit-diagram
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: Section 8 Circuit diagram(CE800(2020)), PDF p. 30 (printed 29), text.md
    lines 443-444; the drawing is a flattened image read from a 300 dpi render (OCR
    supplement lines 1086-1104)
  extracted_at: '2026-09-11'
---

The drawing is headed **#XE890E-SE027 ELLIPITICAL SCHEMATIC** (spelt so) - a different suffix from
the CE800-2016's XE890B-AE10M, and neither code is printed anywhere else in its book.

- **CONSOLE**, with **HP-RIGHT** on a **3 PIN CABLE** and **HP-LEFT** on a **4 PIN CABLE** down to the
  two **HANDPULSE SENSOR** plates. The left grip carries the extra wire.
- **MAIN CONNECTOR** on the console to **MAIN CONNECT** on the **GENERATOR CONTROLLER** by one
  **6 PIN COMPUTER CABLE**.
- On the controller: **DC COIL** takes the **Red wire** from the *Generator & Braking resistor*;
  **3 PHASE GEN IN** takes its **Red/White/Black wire** (marked GEN); **RPM** takes the **RPM Sensor
  wire**.

**No adapter, DC jack or mains inlet is drawn.** The RPM sensor lands on the controller here, where
the 2016 book routed it up the mast as a 3-pin branch of a 9-pin cable
(`ce800-2016-specs-circuit-diagram-xe890b-ae10m`). The 2020-version CR800/CU800 bikes print the
same schematic (`spirit-cr800-cu800-2021-specs-circuit-diagram`).

