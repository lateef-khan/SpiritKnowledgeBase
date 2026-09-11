---
id: ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
title: The driver board is drawn as CS 62004 (110 V) and CS 51008 (220 V) but photographed
  as CS51007-00L, with J9 both the transformer input and the tension motor on the
  drawings
kind: spec
question: What connects where on the driver board of a Spirit ce850-2020 elliptical,
  and which board is it?
asked_as:
- ce850 2020 driver board part number
- cs51007 board
- which controller is in the 220 volt ce850
- ce850 2020 lower board connections
keywords:
- driver board
- controller
- cs 62004
- cs 51008
- cs51007-00l
- 110vac
- 220vac
- inc vr
- rpm sen
- t2.0a250v
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2020
  applies_to:
  - ce850-2020
  section: specs
  code: '*'
  model_number:
  - '850040'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
see_also:
- ce850-2020-specs-circuit-diagram-xe898d-se028
- ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v
- ce850-2020-specs-motor-controller-fuse-10-a-with-a-t2-0a-on-the-board
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- ce850-2020-specs-unit-block-diagram
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: Driver Board PCB Component Locations, CS 62004 (110Vac) on PDF p. 24 and
    CS 51008 (220Vac) on PDF p. 25 (printed 24-25), text.md lines 393-400 (OCR supplement
    lines 1262-1309); Driver Board function photograph, PDF p. 26, lines 400-440
  extracted_at: '2026-09-11'
---

**Two drawings, one photograph, three part numbers.**

The component-location pages are line drawings, one headed **CS 62004 (110Vac)** and the next
**CS 51008 (220Vac)**, each with the same labels: AC HOT and AC NEUTRAL spades, **J9** and **J13**
transformer, **UP - RED / COM - WHITE / DOWN - BLACK** spades to the stride motor, **J9 TENSION
MOTOR**, **J7 STRIDE MOTOR VR**, **J10 RPM SENSOR**, **J8 SYSTEM CABLE**. **J9 is printed twice** -
once as the transformer socket and once as the tension motor socket; the photograph settles it.

The function page photographs the board actually fitted, silkscreened **CS51007-00L** (labels
C10903110011 and 11-0110-0012, marked *110V*), and calls out:

| Socket | Lead |
|---|---|
| **J1 / J2 / J3** | UP red / COM white / DOWN black to the stride motor |
| **J5** | transformer in |
| **J12** | transformer out |
| **J7** | **INC VR** - the stride position sensor, 3-pin |
| **J8** | system cable, 14-pin |
| **J9** | **MOTOR** - the tension motor, 5-pin |
| **J10** | **RPM SEN**, 2-pin |
| **F1** | on-board fuse **T2.0A 250V** |

So on the fitted board the transformer is on **J5/J12** (not J9/J13), the RPM socket is **two
pins** (the 2016 board's J11 was four), and the tension motor is on J9. The circuit diagram agrees
with the photograph (transformer black wire to J5, blue to J12 -
`ce850-2020-specs-circuit-diagram-xe898d-se028`). Quote **CS51007-00L** for a 110 V machine; the
book gives **CS 51008** as the 220 V board's number and prints no photograph of it.

The 2016 CE850, XE395 and XE895 books photograph a genuine CS62004-00L with a different socket
map (`spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections`).

