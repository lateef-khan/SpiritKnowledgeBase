---
id: spirit-cr800ent-cu800ent-specs-unit-block-diagram
title: 'Bike Configuration block diagram: mains through an on/off switch module to
  a power board for the touch panel and a controller for resistance control'
kind: spec
question: What does the unit block diagram of a Spirit CR800ENT or CU800ENT bike show?
asked_as:
- block diagram of the cu800 ent
- how are the boards connected on the cr800ent
- what does the power board feed on the cu800ent
- cr800 ent configuration diagram
keywords:
- block diagram
- bike configuration
- power board
- on/off switch module
- controller
- resistance control
- induction brake
- rpm sensor
- keyboard
- usb charger
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-unit-block-diagram
- cu900ent-unit-block-diagram
see_also:
- spirit-cr800ent-cu800ent-specs-circuit-diagram
- spirit-cr800ent-cu800ent-specs-power-bridge-board-and-converter
- spirit-ct-ent-specs-unit-block-diagram
source:
  ref: spirit-bike-cu800ent-2022-service-manual
  locator: 'CU800ENT: section 5 ''Bike Configuration'', PDF p. 16 (printed 16), text.md
    line 232, a flattened image read from a 300 dpi render (OCR supplement lines 834-891).
    CR800ENT: PDF p. 16, line 239 (OCR lines 919-976). The same drawing'
  extracted_at: '2026-09-11'
---

Read from the render.

**Power path (heavy line).** POWER goes into an **On/Off SWITCH MODULE**, which feeds two things:
the **POWER BOARD (FOR TFT LCD TOUCH PANEL)** and the **CONTROLLER (RESISTANCE CONTROL)**. The
power board and the controller also talk to each other.

**Console.** The display board exchanges signals with the power board. Into the display board:
HEART RATE (WIRELESS), HR (HANDLEBAR), KEYBOARD. Out of it: COOLING FAN, USB CHARGER, and the
**C-SAFE FUNCTION**.

**Drive.** Into the controller: RPM SENSOR. Out of it: **INDUCTION BRAKE**.

**Compared with the generator bike** (`spirit-cr800-cu800-2021-specs-unit-block-diagram`): the
generator block is gone, a mains power block and switch module appear, and a power board sits
between the console and the controller. The treadmill ENT diagram has the same shape with a
filter and a converter added - `spirit-ct-ent-specs-unit-block-diagram`.

