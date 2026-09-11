---
id: ce800-2021-specs-generator-controller-connections
title: 'Four leads on the generator controller of the 2020-version elliptical: system
  cable, RPM sensor, generator brake resistance and generator power'
kind: spec
question: What connects to the driver board on a Spirit ce800-2021 elliptical?
asked_as:
- what plugs into the ce800 driver board
- ce800 2020 generator controller connections
- where does the rpm sensor go on the ce800 lower board
- ce800 elliptical lower controller wiring
keywords:
- driver board
- generator controller
- system cable
- rpm sensor
- generator brake resistance
- generator power
- dc coil
- 3 phase gen in
- main connect
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
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
see_also:
- ce800-2021-specs-circuit-diagram-xe890e-se027
- ce800-2021-specs-unit-block-diagram
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
- spirit-cr800-cu800-2021-specs-generator-controller-connections
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: Section 6-1-4 DRIVER BOARD PCB COMPONENT LOCATIONS AND WIRE CONNECTIONS,
    PDF p. 22 (printed 21), text.md lines 328-334; the photograph was read from a
    300 dpi render (OCR supplement lines 1005-1016); socket names from the circuit
    diagram on PDF p. 30
  extracted_at: '2026-09-11'
---

One photograph of the controller on its heatsink plate, four call-outs:

| Call-out | Where on the board | Name on the circuit diagram |
|---|---|---|
| **SYSTEM CABLE** | the multi-way header at the top left | MAIN CONNECT, the 6-pin computer cable |
| **RPM SENSOR** | the small header beside it | RPM |
| **GENERATOR BRAKE RESISTANCE** | the two-way socket at the top right | DC COIL, red wire |
| **GENERATOR POWER** | the three-way socket at the right edge | 3 PHASE GEN IN, red/white/black wire |

**No board number is legible** on the photograph and none is printed in the text; the only marking
readable is the transformer label 2828 / AS1912.

**The RPM sensor lands on this board**, not on the console. That is the difference from the
2016-generation CE800, whose 031101B controller has no RPM socket and takes the speed sensor up
the mast in a 3-pin branch of the console cable
(`spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections`). The 2020-version
CR800/CU800 bikes photograph the same controller with the same four call-outs
(`spirit-cr800-cu800-2021-specs-generator-controller-connections`).

