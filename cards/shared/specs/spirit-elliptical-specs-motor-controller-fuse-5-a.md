---
id: spirit-elliptical-specs-motor-controller-fuse-5-a
title: The motor controller fuse is 5 A on the ellipticals with an AC actuator and
  a driver board in a tray
kind: spec
question: What fuse does the motor controller of a Spirit CE850-2016, XE395, XE395ENT
  or XE895 elliptical take?
asked_as:
- ce850 fuse rating
- what amp fuse is in the xe395 elliptical
- xe395ent fuse size
- xe895 controller fuse
keywords:
- fuse
- 5a
- 5 amp
- motor controller
- fuse holder
- appliance inlet
- rating
- replacement fuse
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce850-2020-specs-motor-controller-fuse-10-a-with-a-t2-0a-on-the-board
see_also:
- spirit-elliptical-safety-power-off-and-unplug-before-touching-the-fuse
- spirit-ce850-2016-errors-no-display-ac-adapter-wires-adapter-fuse-then-covers
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: 8.6 FUSE, PDF p. 55 (printed 55), text.md lines 957-973. XE895-2016:
    PDF p. 56, lines 957-973. XE395-2016: PDF p. 56, lines 950-966. XE395ENT-2021:
    PDF p. 45, lines 641-656. Each is a captioned photograph of the fuse and its holder'
  extracted_at: '2026-09-11'
---

Each book closes its wiring chapter with a photograph captioned **FUSE 5A** - the cartridge fuse in
the holder on the motor controller's AC side, fed from the appliance inlet.

| Book | Page | Rating |
|---|---|---|
| CE850-2016 | p. 55 | **5 A** |
| XE895-2016 | p. 56 | **5 A** |
| XE395-2016 | p. 56 | **5 A** |
| XE395ENT-2021 | p. 45 | **5 A** |

**No voltage rating, no size and no time/fast characteristic is printed** for the fuse - the
caption is the rating alone. The circuit diagrams draw the fuse in the **appliance inlet**
(`spirit-ce850-2016-xe395-xe895-specs-circuit-diagram`), and the driver board's AC HOT spade is
labelled *FUSE* because that is where the inlet's fused line lands
(`spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections`).

**The CE850-2020 prints a different figure, 10 A**, and its board carries a second on-board fuse
(`ce850-2020-specs-motor-controller-fuse-10-a-with-a-t2-0a-on-the-board`). Power off and unplug
before touching either (`spirit-elliptical-safety-power-off-and-unplug-before-touching-the-fuse`).

