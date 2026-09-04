---
id: f85-2019-driver-board-leds
title: Driver board indicator lights and what they mean
kind: spec
question: What do the indicator LEDs on the driver board of a Sole F85-2019 treadmill
  mean?
asked_as:
- what are the lights on the treadmill controller
- limit light is on my treadmill board
- power led off on the controller
keywords:
- driver board
- indicator led
- power led
- limit current led
- over current
- controller lights
- fuse
- transformer
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2019-e2-over-current
- f85-2019-driver-board-sockets
- f85-2019-lower-controller-replacement
source:
  ref: sole-tm-f85-2019-service-manual
  locator: sections 6.6 and 6.7, printed pages 47 to 48
  extracted_at: '2026-09-04'
---

This driver board carries **two** indicator LEDs: **Power** and **Limit current**.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | On whenever the DC voltage is normal. Off means a fault. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110VAC or 230VAC. Replace the fuse. Replace the controller. |
| LIMIT current | Over current protection warning light | Lights when the lower board detects over current. | Protection of the lower board and the motor. | Replace the controller. Replace the motor. Do not block the belt running. Smear silicone oil between the belt and the running board. |

**This build has fewer indicator LEDs than its neighbours.** The 2016 and 2021 manuals for the ST535 and ST538-YT056 builds list five LEDs — POWER, LIMIT, UP, DOWN and SPEED — and give the LIMIT trip currents as 18A on a 220Vac system and 28A on a 120Vac system. This manual lists neither the extra three LEDs nor any trip current.
