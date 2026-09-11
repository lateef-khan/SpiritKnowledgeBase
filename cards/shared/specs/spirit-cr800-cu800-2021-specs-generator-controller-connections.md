---
id: spirit-cr800-cu800-2021-specs-generator-controller-connections
title: Four leads on the generator controller - system cable, RPM sensor, generator
  resistance voltage and generator power - and the two flywheel leads they meet
kind: spec
question: What plugs into the generator controller and the generator flywheel on a
  Spirit CR800 or CU800 2020-version bike?
asked_as:
- what plugs into the cu800 lower controller
- cr800 driver board connections
- which wire is the generator resistance voltage
- what are the two leads on the cu800 flywheel
keywords:
- driver board
- generator controller
- system cable
- rpm sensor
- generator resistance voltage
- generator power
- generator flywheel
- brake coil
- definition function
- connector
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
- spirit-cr800ent-cu800ent-specs-driver-board-connections
see_also:
- spirit-cr800-cu800-2021-specs-circuit-diagram
- spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel
- xbr95-2023-specs-generator-controller-cs52005-33-connections
source:
  ref: spirit-bike-cu800-2021-service-manual
  locator: 'CU800(2020): 6-1-5 Driver Board PCB Component Locations and Wire Connections,
    PDF p. 21 (printed 20), text.md lines 315-331; 6-1-6 Generator Flywheel Definition
    Function, PDF p. 22 (printed 21), lines 332-348. CR800(2020): PDF pp. 21-22, lines
    293-326. Photographs read from a 300 dpi render'
  extracted_at: '2026-09-11'
---

**The driver board (p. 21)** has four call-outs. On the left edge, two small headers: **SYSTEM
CABLE** (upper) and **RPM SENSOR** (lower). On the right edge, two more: **GENERATOR RESISTANCE
VOLTAGE** (upper, a two-way plug) and **GENERATOR POWER** (lower, a three-way plug). The board's
own silkscreen is not legible in the photograph; the schematic labels the same four sockets
MAIN CONNECT, RPM, DC COIL and 3 PHASE GEN IN.

**The generator flywheel (p. 22)** has two leads and the page names them: **GENERATOR POWER**, the
lead off the stator windings, and **GENERATOR RESISTANCE VOLTAGE**, the red-and-black pair off
the brake coil. Match them to the two right-hand sockets above.

**No voltage is printed for either lead.** The troubleshooting matrix lists a "generator brake
resistance voltage wire shedding" as a cause of lost resistance; that row belongs to the errors
section.

The 2023 XBR95 residential recumbent uses the same lead names on a controller marked CS52005-33 -
see `xbr95-2023-specs-generator-controller-cs52005-33-connections`.

