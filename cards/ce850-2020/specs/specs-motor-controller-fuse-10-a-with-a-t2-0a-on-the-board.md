---
id: ce850-2020-specs-motor-controller-fuse-10-a-with-a-t2-0a-on-the-board
title: The fuse page says 10 A while the driver board photograph shows an on-board
  T2.0A 250V fuse
kind: spec
question: What fuse does the motor controller of a Spirit ce850-2020 elliptical take?
asked_as:
- ce850 2020 fuse rating
- what amp fuse is in the 2020 ce850
- t2.0a fuse on the ce850 board
- ce850 has two fuses
keywords:
- fuse
- 10a
- 10 amp
- t2.0a 250v
- f1
- motor controller
- appliance inlet
- rating
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
- spirit-elliptical-specs-motor-controller-fuse-5-a
see_also:
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- ce850-2020-specs-circuit-diagram-xe898d-se028
- spirit-elliptical-safety-power-off-and-unplug-before-touching-the-fuse
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: 8.6 FUSE, PDF p. 48 (printed 48), text.md lines 836-852, a captioned photograph;
    the on-board fuse is read from the Driver Board function photograph, PDF p. 26,
    lines 400-440 (silkscreen F1, T2.0A250V)
  extracted_at: '2026-09-11'
---

Two fuses appear in this book, in two places:

- **FUSE 10A** - the caption on the fuse page (p. 48), the cartridge fuse in the holder beside the
  appliance inlet, which the circuit diagram draws inside the inlet block.
- **F1 - T2.0A 250V** - a slow-blow 2 A fuse soldered onto the **CS51007-00L** driver board, legible
  on the function-page photograph and not mentioned in any text.

They are not the same fuse and they are not a contradiction: the 10 A part protects the mains
side, the 2 A part the board's own transformer secondary. When "the fuse" blows, check the inlet
one first and the board one second.

**The 2016 CE850, XE395, XE395ENT and XE895 print 5 A** for the inlet fuse
(`spirit-elliptical-specs-motor-controller-fuse-5-a`) - do not carry that figure across to this
machine. No voltage or size is printed for the 10 A part. Power off and unplug before touching
either (`spirit-elliptical-safety-power-off-and-unplug-before-touching-the-fuse`).

