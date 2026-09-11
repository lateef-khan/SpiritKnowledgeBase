---
id: mt200-2022-errors-no-power-console-does-not-light-five-steps
title: 'No power and the console does not light: the breakers, the drive red LED,
  then 12 V DC on pins 4 and 12 at the console and at the low control board'
kind: troubleshooting
question: What do I check when there is no power and the console does not light on
  a Spirit mt200-2022 treadmill?
asked_as:
- 7.0t console dead no power
- medical treadmill will not power up
- no lights on the 7.0t console
keywords:
- no power
- console
- circuit breaker
- motor drive
- red led
- ac filter
- 12v dc
- pin 4
- pin 12
- 12 pin connector
facets:
  brand:
  - spirit
  product_line: treadmill
  model: mt200-2022
  applies_to:
  - mt200-2022
  section: errors
  code: no-power
  model_number:
  - '720080'
  - '720087'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-mt200-errors-error-code-table
- mt200-2022-errors-no-belt-movement-motor-two-ohms
source:
  ref: spirit-treadmill-mt200-2022-service-manual
  locator: 7.0T (MT200 2022) service manual 5. Troubleshooting and Problem solving,
    item 1 No power, console doesn't light, PDF p. 17-19, text.md lines 363-407
  extracted_at: '2026-09-11'
---

Section 5 of the 7.0T service manual, *Troubleshooting and Problem solving*, item 1, in the order printed:

1. Make sure there is no problem with the AC power.
2. Check the switch and **both circuit breakers - one on the back panel, the other inside the motor cover**. Press a breaker back in if it has popped out and make sure the power cord is plugged in properly.
3. Make sure AC power reaches the motor drive. **The red light on the drive lights when there is AC power**; check the voltage with a meter. Replace the drive if the input voltage is correct and the red LED does not light. If there is no AC at the drive, check both sides of the AC filter; no AC at the filter's input means the circuit breakers or the AC input module may be bad.
4. With the console disconnected from its 12-pin connector, **measure between pin 4 (Vin) and pin 12 (Gnd) at the back of the console. Replace the console if 12 V DC is measured** there and it still does not light.
5. If there is no voltage there, measure the **red 12-pin connector on the low control board between pin 4 and pin 12**. Replace the 12-pin cable from the low control board to the console if 12 V DC is present here but not at the console; replace the drive if there is no voltage here while the AC to the drive is fine.

The photographs beside each step show the breaker positions, the drive's red LED, the filter and the two connectors; they carry no further text. The 7.0T has two breakers where the CT and XT treadmills have one on the front grill.
