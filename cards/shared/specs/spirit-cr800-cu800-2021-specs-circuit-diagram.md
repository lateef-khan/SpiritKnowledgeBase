---
id: spirit-cr800-cu800-2021-specs-circuit-diagram
title: Schematic with a 6-pin computer cable, 3-pin and 4-pin hand-pulse cables, and
  a generator controller taking a red DC-coil wire and a red/white/black three-phase
  generator wire
kind: spec
question: What does the circuit diagram of a Spirit CR800 or CU800 2020-version bike
  show?
asked_as:
- cu800 2020 wiring diagram
- cr800 schematic
- how many pins is the cu800 computer cable
- what colour is the generator wire on the cr800
keywords:
- circuit diagram
- schematic
- xu880-sb023
- xr880-sb023
- 6 pin computer cable
- 3 pin cable
- 4 pin cable
- handpulse sensor
- dc coil
- 3 phase gen in
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cu800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800ent-cu800ent-specs-circuit-diagram
see_also:
- spirit-cr800-cu800-2021-specs-generator-controller-connections
- spirit-cr800-cu800-2021-specs-unit-block-diagram
source:
  ref: spirit-bike-cu800-2021-service-manual
  locator: 'CU800(2020): ''#XU880-SB023 BIKE SCHEMATIC'', section 8, PDF p. 29 (printed
    28), text.md line 457, a flattened drawing read from a 300 dpi render (OCR supplement
    lines 1080-1099). CR800(2020): ''#XR880-SB023 RECUMBENT SCHEMATIC'', PDF p. 29
    (printed 28), line 435 (OCR lines 1298-1316). Identical apart from the title'
  extracted_at: '2026-09-11'
---

The upright's drawing is headed **#XU880-SB023 BIKE SCHEMATIC** and the recumbent's
**#XR880-SB023 RECUMBENT SCHEMATIC** - the Dyaco factory codes, not the Spirit model names.
Everything below the title is the same on both.

**Console.** Two hand-pulse leads: **HP-RIGHT on a 3 PIN CABLE** and **HP-LEFT on a 4 PIN CABLE**,
each to one half of the **HANDPULSE SENSOR**. One **MAIN CONNECTOR** feeds the **6 PIN COMPUTER
CABLE** down the mast.

**Generator controller.** The computer cable arrives at **MAIN CONNECT**. Three more sockets:

| Socket | Lead | Colour |
|---|---|---|
| **DC COIL** | from the *Generator & Resistor* block | **Red wire** |
| **3 PHASE GEN IN** | from the same block, marked GEN | **Red/White/Black wire** |
| **RPM** | **RPM Sensor wire** to the RPM Sensor | not stated |

So the two-wire red lead is the brake coil and the three-wire lead is the generator - the same
pair the flywheel photo calls *generator resistance voltage* and *generator power*.

There is **no adapter, no DC jack and no mains inlet** on the drawing; pin numbers are not given.

