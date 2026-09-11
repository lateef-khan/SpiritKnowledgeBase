---
id: ct850-2020-unit-block-diagram
title: 2020 treadmill unit block diagram
kind: spec
question: What does the unit block diagram of a Spirit CT850-2020, CT800-2020 or CT900
  treadmill show?
asked_as:
- block diagram of the 2020 ct850
- how are the boards connected on the new ct850
- what feeds the driver board on a ct850
- treadmill signal flow diagram
keywords:
- block diagram
- display board
- driver board
- signal flow
- rpm sensor
- vr set
- fuse
- power switch
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct850-2020
  - ct900
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- 40t-2026-specs-unit-block-diagram
- spirit-ct-ent-specs-unit-block-diagram
- spirit-dc-treadmill-specs-unit-block-diagram
see_also:
- ct850-2016-unit-block-diagram
- ct800-2020-specs-circuit-diagram
- ct900-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: p. 18 (printed 17), section 5 Unit Block Diagrams. The CT800-2020 service manual
    prints the identical drawing under '5. CT800(2020) Unit Block Diagrams' at PDF p. 18
    (printed 17), text.md lines 274-280; the CT900 service manual prints it as 'Treadmill
    Configuration' at PDF p. 18 (printed 18), lines 265-270. All three are flattened images
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image.

**Into the display board**: KEY, HR HANDLEBAR, WIRELESS HR RECEIVER.
**Out of the display board**: COOLING FAN.
**Display board and driver board** exchange signals both ways.
**Into the driver board**: POWER through a POWER SWITCH and a FUSE; AC MOTOR RPM SENSOR; VR SET.
**Out of the driver board**: AC MOTOR and INCLINE MOTOR.

**The CT800-2020 book prints this drawing unchanged, AC MOTOR box and all, for a DC-motor
machine.** Its own circuit diagram and driver-board page show a Ya Cheng YC782 DC motor on M+ /
M- terminals; the block diagram was copied from the CT850 and not corrected. The CT900 book prints
the same drawing for a machine that really does have an AC motor, a lower control board and an
inverter, none of which the drawing separates.

The 2016 CT850 prints a fuller version of this diagram that adds a thumb switch, an amplifier
with line in / line out and speakers, and a tension-motor block that does not belong on a
treadmill.
