---
id: csc880-2025-specs-controller-seven-cables-named
title: 'Seven cables on the controller: DC 24 V power, brake, proximity switch, communication,
  infrared emergency stop, light sensor and motor, with red to positive and black
  to negative'
kind: spec
question: Which cables plug into the controller of a Spirit csc880-2025 stair climber,
  and which way round is the power lead?
asked_as:
- csc880 controller wiring
- what plugs into the csc880 lower board
- which wire is positive on the csc880 controller
- csc880 controller replacement cables
keywords:
- controller
- lower control board
- cables
- dc 24v power cable
- brake cable
- proximity switch
- communication cable
- infrared emergency stop
- light sensor cable
- motor cable
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: specs
  code: '*'
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with:
- csc900-2019-specs-controller-ev60-k2412-dc-dc-converter-and-ai3-console-board
see_also:
- spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system
- spirit-climber-2024-specs-resistance-system
source:
  ref: spirit-climber-csc880-2025-service-manual
  locator: 7. Part Replacement, 1. Replace the controller, PDF p. 12 (printed 12),
    text.md lines 222-275, the numbered legend beside a photograph of the controller
    with seven arrows; the photograph checked on a 110 dpi render
  extracted_at: '2026-09-11'
---

The controller-replacement page photographs the green controller board on its tray in the base
and numbers seven leads:

| No. | Cable |
|---|---|
| 1 | **DC 24V power cable** |
| 2 | **Brake cable** |
| 3 | **Proximity switch cable** |
| 4 | **Communication cable** (communication, upper control power supply) |
| 5 | **Infrared emergency stop cable** |
| 6 | **light sensor cable** |
| 7 | **Motor cable** |

Three notes printed with the list:

- "When plugging or unplugging the wiring harness, check whether there is a latch at the
  connector. If there is a latch, press it while pulling the wire."
- "The power cord has positive and negative poles. **Connect the red wire to + and the black wire
  to -.**"
- "Before disconnecting the wiring harness, take a photo to record the wiring position."

**What the list adds to the wire diagram.** The diagram
(`spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system`) draws five of these; the
**proximity switch** and the **infrared emergency stop** appear only here. The communication cable
carries the console's 12 V as well as data - "upper control power supply" - which is why a
console that stays dark is checked at this plug for DC 12V in the troubleshooting table. The light
sensor's plug is "the red plug" on the controller, per the light-sensor replacement step.

**No connector numbers, pin counts or wire colours beyond red/black are printed.** The 2019
CSC900's controller is a different board with different leads
(`csc900-2019-specs-controller-ev60-k2412-dc-dc-converter-and-ai3-console-board`).

