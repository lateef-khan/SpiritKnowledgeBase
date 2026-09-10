---
id: ct850-2016-inverter-board-connector-pinouts
title: Pin definitions for the inverter board's console, mains, incline and motor
  plugs
kind: spec
question: What are the inverter board connector pin definitions on a Spirit CT850-2016
  treadmill?
asked_as:
- what are the pins on the ct850 lower board console plug
- incline vr wire colours 2016 ct850
- which terminal is line on the treadmill controller
- ac motor u v w order
keywords:
- pin definition
- inverter
- cn10
- cn13
- tb1
- cn6
- incline vr
- wire colour
- u v w
- console connector
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
  model_number: '850845'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-inverter-board-connector-locations
- ct850-2016-incline-err-test-procedure
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 42 (printed 41) 'Pin definition'
  extracted_at: '2026-09-08'
---

**CN10 - connection to console (6 pins)**: P1 DX+/TXD, P2 DX-/RXD, P3 EXG, P4 Wk, P5 P12, P6 G12.

**TB1 - AC in (2 pins)**: P1 POWER N (white wire), P2 POWER L (black wire).

**CN6 - incline power (3 pins)**: P1 COM (white wire), P2 Up (red wire), P3 Down (black wire).

**CN13 - incline VR (3 pins)**: P1 GND (black wire), P2 VR-IN (white wire), P3 +5V (red wire).

**DT-69-B01W-03P - AC motor power (3 pins)**: P1 W, P2 V, P3 U.

Note the order of the motor block: pin 1 is **W**, not U.
