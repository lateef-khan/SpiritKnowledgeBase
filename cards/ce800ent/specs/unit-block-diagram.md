---
id: ce800ent-unit-block-diagram
title: Elliptical unit block diagram
kind: spec
question: What does the unit block diagram of a Spirit ce800ent elliptical show?
asked_as:
- block diagram of the ce800 elliptical
- how are the boards connected on the ce800ent
- what drives the induction brake
- elliptical configuration diagram
keywords:
- block diagram
- display board
- power board
- controller
- resistance control
- induction brake
- rpm sensor
- usb charger
- c-safe
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-electrical-part-descriptions
- ce800ent-flywheel-and-induction-brake
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: p. 16 (printed 16), section 5 Unit Block Diagrams
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image. The page is titled
**"Bike Configuration"** - a copy-paste error in an elliptical manual.

**Into the display board**: HEART RATE (WIRELESS), HR (HANDLEBAR), KEYBOARD.
**Out of the display board**: C-SAFE FUNCTION, COOLING FAN, USB CHARGER.
**Display board and power board (for TFT LCD touch panel)** exchange signals both ways.
**Power**: POWER to an **On/Off SWITCH MODULE**, which feeds both the power board and the
controller.
**Power board and controller (resistance control)** exchange signals both ways.
**Into the controller**: RPM SENSOR.
**Out of the controller**: INDUCTION BRAKE.

There is no incline block anywhere on this diagram.
