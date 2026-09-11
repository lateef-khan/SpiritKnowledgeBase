---
id: spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
title: 'The 031101B generator controller: generator in, generator brake out, system
  cable, and an unused fourth socket - photographed with GENERATOR POWER 1 printed
  twice'
kind: spec
question: What plugs into the 031101B driver board of a Spirit XBR95 2016 recumbent
  or CU800 2012 upright bike?
asked_as:
- what plugs into the xbr95 2016 lower board
- 031101b board
- cu800 2012 controller connections
- which socket is the brake on the xu878 controller
keywords:
- driver board
- generator controller
- 031101b
- cn1
- cn2
- cn3
- cn4
- generator input
- generator brake output
- system wire
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
- xbr95-2023-specs-generator-controller-cs52005-33-connections
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
see_also:
- spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
- cu800-2012-specs-electrical-configuration-and-display-board-leads
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: 'XBR95-2016: ''Driver Board Wire Connections'', PDF p. 31, text.md lines
    423-428 (OCR supplement lines 1460-1473), and ''Driver Board function'', PDF p.
    33, lines 435-449 (OCR 1483-1494). CU800-2012: ''Driver Board Wire Connections'',
    PDF p. 28, lines 417-446 (OCR 1064-1073), and ''Driver Board function'', PDF p.
    29, lines 447-467 (OCR 1076-1094). Photographs read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

Both books use the board marked **#031101B** (the XU878 photo shows the silkscreen; the XBR95
book prints it on its diagram and schematic). Sockets:

| Socket | XBR95-2016 name | CU800-2012 name | What it is |
|---|---|---|---|
| **CN1** | GENERATOR | GENERATOR POWER (3-pin red/white/black) | the stator lead in |
| **CN2** | GENERATOR BRAKE | GENERATOR BRAKE RESISTANCE VOLTAGE (2-pin red) | the brake coil out |
| **CN3** | SYSTEM CABLE | SYSTEM CABLE / SYSTEM CONTROL | the console cable |
| **CN4** | drawn on the schematic, nothing wired | - | spare |

The function photographs caption the same plugs **GENERATOR BRAKE OUTPUT**, **GENERATOR INPUT**
and **SYSTEM WIRE** in the XBR95 book, and **GENERATOR RESISTANCE VOLTAGE**, **SYSTEM CONTROL**
and - **twice** - **GENERATOR POWER 1** in the XU878 book, where the second "GENERATOR POWER 1"
points at the CN4 position. The schematic wires nothing to CN4; take the duplicated caption as a
labelling slip.

The console-cable pins on CN3 are listed on the XBR95 error page
(`xbr95-2016-specs-console-to-driver-board-6-pin-definition`). No voltage is printed on either
lead here; the brake's working voltage is on `xbr95-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v`.

