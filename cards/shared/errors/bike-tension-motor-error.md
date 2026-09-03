---
id: sole-bike-tension-motor-error
title: "Tension motor failure error on the bike console"
kind: troubleshooting
question: "What does E2 mean on a Sole B94-2016, B94-2019 or R92-2016 bike?"
asked_as:
- "bike shows e2"
- "resistance wont change and i get an error"
- "e2 error on my sole bike"
keywords:
- "e2"
- "tension motor"
- "resistance"
- "level up"
- "level down"
- "drive board"
- "gear motor"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - b94-2016
  - b94-2019
  - r92-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- sole-bike-eeprom-error
- sole-e2-error
see_also:
- sole-bike-tension-motor-voltage-test
- sole-bike-tension-motor-spec
source:
  ref: sole-bike-b94-2016-service-manual
  locator: "Section 8, 'Error Message: E2' (same section in the B94 2016, B94 2019 and R92 2016 manuals)"
  extracted_at: '2026-09-03'
---

**This is the bike tension motor fault. It is not the treadmill E2, and it is not the bike EEPROM error.**

**What happens:** you press Level Up or Level Down, the motor does not move, and "E2" appears on the display.

**How the parts should work**

| Part | What it does |
|---|---|
| Display | The key signal reaches the display. The main program IC then sends a command signal to the drive board. |
| Drive board | The drive board receives the signal and puts out power to the motor. Level UP: +5VDC. Level DOWN: -5VDC. |

**How to find the fault**

| Part | Check |
|---|---|
| Display | If the key beeps when pressed, assume the signal was sent. |
| Data cable | Inspect the cable and the connections. |
| Drive board | Inspect the drive board power output to the motor. Level Up is +5VDC, Level Down is -5VDC. If there is power at the motor but the motor does not run, replace the motor. If there is no power output, check whether the drive board itself has power. |
