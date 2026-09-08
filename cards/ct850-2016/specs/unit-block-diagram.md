---
id: ct850-2016-unit-block-diagram
title: 2016 treadmill unit block diagram
kind: spec
question: What does the unit block diagram of a Spirit CT850-2016 treadmill show?
asked_as:
- block diagram of the 2016 ct850
- how are the boards connected on the ct850
- treadmill configuration diagram
- what feeds the driver board
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- signal flow
- amplifier
- rpm sensor
- vr set
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2020-unit-block-diagram
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 21 (printed 20) 'Treadmill Configuration'
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image and its extracted text is garbled.

**Into the display board**: KEY, HR HANDLEBAR, WIRELESS HR RECEIVER, THUMB SWITCH.
**Out of the display board**: COOLING FAN, and a feed to an AMPLIFIER that also takes LINE IN
and drives SPEAKER L/R and LINE OUT.
**Display board and driver board** exchange signals both ways.
**Into the driver board**: POWER through a POWER SWITCH and a FUSE; AC MOTOR RPM SENSOR; VR SET.
**Out of the driver board**: TENSION MOTOR and INCLINE MOTOR.

The **TENSION MOTOR** box is a defect in the source: a CT850 has no tension motor, and the
block is absent from the 2020 CT850 version of the same diagram. So are the audio blocks.
