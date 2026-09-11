---
id: jb950-2022-errors-cant-find-the-chest-strap-worn-or-battery
title: 'The console can''t find the chest strap: it is not worn properly or its battery
  is weak, and the strap may be rechargeable'
kind: troubleshooting
question: Why can a Spirit jb950-2022 Johnny G bike not find the chest strap?
asked_as:
- johnny g bike wont find my chest strap
- jb950 not picking up heart rate strap
- spirit indoor bike chest strap not detected
- no heart rate from the strap on the jb950
keywords:
- chest strap
- cant find
- no pulse
- heart rate
- battery
- charge the sensor
- worn properly
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
- spirit-wireless-chest-belt-no-pulse
- jb950-2022-errors-hr-sensor-error-reset-console
see_also:
- jb950-2022-errors-erratic-pulse-wrong-sensor-or-low-battery
- spirit-wireless-chest-belt-no-pulse
- jb950-2022-errors-hr-sensor-error-reset-console
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.4 Troubleshooting procedure matrix, PDF p.
    45, text.md lines 839-868
  extracted_at: '2026-09-11'
---

The condition is printed as `Can't find the chest strap`.

| Reason | Solving |
|---|---|
| 1. Chest strap not worn properly. 2. Chest strap battery is weak or dead. | 1. Check chest strap has proper contact with skin and is oriented correctly. 2. Change the battery of the sensor or charge the sensor. |

**Two causes, not three, and no CR2032 and no three-foot range.** Every other Spirit bike matrix answers a silent chest belt with a third cause - too far from the receiver - and a named CR2032 lithium cell (`spirit-wireless-chest-belt-no-pulse`). The JB950 pairs digitally over BLE and ANT+, prints no range, and allows that the strap may be one you **charge** rather than open.

A strap that is found but reads wildly is the row above: `jb950-2022-errors-erratic-pulse-wrong-sensor-or-low-battery`. `HR SENSOR ERROR` on the screen is the heart-rate module failing to initialise after a short power-up, cleared with a reset: `jb950-2022-errors-hr-sensor-error-reset-console`. Turning the automatic strap search on and off is `AUTO DETECT HR` in maintenance mode, a console fact.
