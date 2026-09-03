---
id: cc81-2020-tension-motor-connector-pinout
title: "Tension motor connector pin-out on the driver board"
kind: spec
question: "What is the tension motor connector pin-out on a Sole CC81-2020 climber?"
asked_as:
- "tension motor wiring on my sole climber"
- "which pin is motor positive on the cc81"
- "driver board connector pinout for the climber"
keywords:
- "tension motor"
- "connector"
- "pinout"
- "driver board"
- "console"
- "wiring"
- "speed sensor"
- "rotary switch"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2020
  applies_to:
  - cc81-2020
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- sole-bike-tension-motor-connector-pinout
see_also:
- sole-bike-tension-motor-connector-pinout
- cc81-2020-tension-motor-voltage-test
source:
  ref: sole-climber-cc81-2020-service-manual
  locator: "Section 7-5, Test configuration and the console to driver board connector pin define function"
  extracted_at: '2026-09-03'
---

**The climber has pins 1 and 2 the other way round from the Sole bikes. Check this table, not the bike one.**

| Pin | Signal |
|---|---|
| 1 | M- |
| 2 | M+ |
| 3 | +5V |
| 4 | VR |
| 5 | GND |

The same page also names the other connectors on the console-to-driver-board test point: **Speed Sensor**, **Rotary Switch**, **Tension Motor**, **Tension Motor Power** and **HR Receiver**. The manual labels them on a photograph and gives a pin list for the tension motor connector only.

On the Sole B94 and R92 bikes the same five signals are printed as 1 = M+, 2 = M-, 3 = +5V, 4 = VR, 5 = GND. Pins 1 and 2 are swapped.
