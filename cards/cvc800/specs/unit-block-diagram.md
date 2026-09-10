---
id: cvc800-unit-block-diagram
title: Climber unit block diagram
kind: spec
question: What does the unit block diagram of a Spirit cvc800 climber show?
asked_as:
- block diagram of the cvc800
- how is the cvc800 wired up
- what connects to the climber console
- climber configuration diagram
keywords:
- block diagram
- climber configuration
- console
- power switch
- tension motor
- rpm sensor
- signal flow
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: specs
  code: '*'
  model_number:
  - '800440'
authority: 3
not_to_be_confused_with: []
see_also:
- cvc800-electronic-parts-locations
- cvc800-console-to-driver-board-connector-pin-map
source:
  ref: spirit-climber-cvc800-service-manual
  locator: p. 17 (printed 17), section 5 Unit Block Diagrams, titled 'Climber Configuration'
  extracted_at: '2026-09-08'
---

The whole diagram is four boxes around the console:

- **Power** into a **Power Switch**
- **Power Switch** and **Console** exchange both ways
- **Tension Motor** into the **Console**
- **RPM Sensor** into the **Console**

There is no driver board and no lower controller block. Everything that drives the machine is in
the console, which is why the connector pin map in section 8-4 is on the console's own display
board.
