---
id: jb950-2022-errors-erratic-pulse-wrong-sensor-or-low-battery
title: 'The pulse reading jumps around: the bike is on the wrong sensor, the sensor
  battery is low, or the receiver has failed'
kind: troubleshooting
question: Why is the heart rate reading erratic on a Spirit jb950-2022 Johnny G bike?
asked_as:
- heart rate jumping around on the johnny g bike
- jb950 pulse reading all over the place
- spirit indoor bike erratic heart rate
- bike picking up the wrong heart rate strap
keywords:
- erratic pulse
- heart rate
- wrong sensor
- chest strap battery
- receiver
- ant+
- bluetooth
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: no-code
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-erratic-pulse-display
- jb950-2022-errors-hr-sensor-error-reset-console
see_also:
- jb950-2022-errors-cant-find-the-chest-strap-worn-or-battery
- spirit-erratic-pulse-display
- jb950-2022-errors-hr-sensor-error-reset-console
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.4 Troubleshooting procedure matrix, PDF p.
    45, text.md lines 839-868
  extracted_at: '2026-09-11'
---

The condition is printed as `Erratic pulse display`.

| Reason | Solving |
|---|---|
| 1. Bike connected to the wrong sensor. 2. Battery of the sensor is low. 3. Receiver malfunction. | 1. Make sure the bike is connect to the right sensor. 2. Change the battery of the sensor or charge the sensor. 3. Replace console. |

**This is not the three-cause row every other Spirit bike prints** (another belt in the room, a magnetic field, a broken receiver - `spirit-erratic-pulse-display`). The JB950 pairs digitally over BLE and ANT+, so its first cause is the console having latched onto *someone else's* sensor - which is also why the console has an `AUTO DETECT HR` on/off setting and a `BIKE ID` in maintenance mode - and its second is a strap that may be rechargeable (*change the battery or charge the sensor*) rather than the CR2032 the analogue-belt books name. The receiver is in the console, so the third fix is the console itself.

A strap the console cannot find at all is the next row: `jb950-2022-errors-cant-find-the-chest-strap-worn-or-battery`. `HR SENSOR ERROR` on the screen is a message, not this row: `jb950-2022-errors-hr-sensor-error-reset-console`.
