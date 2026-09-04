---
id: sc200-2016-console-connector-pinout
title: Which connectors the display board carries
kind: spec
question: What connectors are on the display board of a Sole sc200-2016 climber?
asked_as:
- what are the pins on the console cable of my sole sc200
- display board connectors on my sole climber
- 8 pin cable on the sc200
keywords:
- display board
- connector
- 8-pin cable
- console interface board
- amplifier board
- wiring
- tension motor
- speed sensor
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2016
  applies_to:
  - sc200-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2016-tension-motor-connector-pinout
- sc200-2016-e2-tension-motor-failure
source:
  ref: sole-elliptical-sc200-2016-service-manual
  locator: Sections 6-1 to 6-4 and the E2 troubleshooting table, pages 26-40
  extracted_at: '2026-09-04'
---

**This manual gives no pin-by-pin list for a console to driver board connector.** Sections 6-1 to 6-4 are drawings only: display board wire connections, display board PCB component locations (top and bottom), the console interface board wire connections and the amplifier board wire connections. Their text does not survive extraction as a list.

What the manual does name is the **8-pin cable** between the display board and the tension motor. The E2 troubleshooting table reads:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Inspect the 8-pin cable connections. |
| 8-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension motor | Inspect the display board 8-pin connections. |

The signal names for that 8-pin plug are on the tension motor connector card.

**There is no driver board section in this manual.** Unlike the 2016 Sole ellipticals it has no 6.5 to 6.10 driver board pages, no controller LED debugging table and no 14-pin system harness, because this machine has no incline motor and no separate lower controller.
