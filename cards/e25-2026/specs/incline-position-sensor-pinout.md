---
id: e25-2026-incline-position-sensor-pinout
title: Position sensor connector pin definition
kind: spec
question: What is the incline position sensor connector pinout on a Sole e25-2026
  elliptical?
asked_as:
- 3 pin incline connector pins on a sole elliptical
- potentiometer wiring for the incline board
- what is pin 1 on the incline sensor plug
keywords:
- position sensor
- potentiometer
- 3-pin
- connector
- pinout
- 5vdc
- ground
- incline board
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2026
  applies_to:
  - e25-2026
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e25-2026-incline-motor-test-procedure
- e25-2026-incline-motor-spec
source:
  ref: sole-elliptical-e25-2026-service-manual
  locator: Section 8.3, incline test procedure step 6, page 32
  extracted_at: '2026-09-04'
---

The wiring is the same at the incline board connector and at the console connector.

| Pin | Signal |
|---|---|
| 1 | 5vdc |
| 2 | position signal 0~5vdc |
| 3 | ground |

At the potentiometer itself the manual tests **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc when the motor is at the lowest position**.

**Check the pin order before you rely on it.** The 2019 generation of this manual numbers the same three signals in the opposite order (pin 3 = 5vdc, pin 1 = ground). Only the 2026 numbering is stated here.
