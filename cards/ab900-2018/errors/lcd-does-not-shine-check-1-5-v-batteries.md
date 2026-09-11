---
id: ab900-2018-errors-lcd-does-not-shine-check-1-5-v-batteries
title: 'The LCD does not shine or is incomplete: the backlight, or batteries that
  must each read 1.5 V'
kind: troubleshooting
question: Why is the display dark or incomplete on a Spirit ab900-2018 air bike?
asked_as:
- air bike display is dark
- ab900 lcd not lighting up
- spirit air bike screen incomplete
- what battery voltage does the air bike console need
keywords:
- lcd
- backlight
- dim display
- incomplete
- batteries
- 1.5 v
- console power
- air bike
facets:
  brand:
  - spirit
  product_line: bike
  model: ab900-2018
  applies_to:
  - ab900-2018
  section: errors
  code: no-code
  model_number:
  - '900748'
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- spirit-2024-errors-leds-not-bright-generator-power-connection
see_also:
- ab900-2018-errors-console-without-display-check-the-four-batteries
- spirit-erratic-pulse-display
- spirit-wireless-chest-belt-no-pulse
source:
  ref: spirit-bike-ab900-2018-service-manual
  locator: AB900 2018 service manual Troubleshooting Quick Lookup Table, PDF p. 31,
    text.md lines 545-571
  extracted_at: '2026-09-11'
---

The condition is printed as `LCD display does not shine, incomplete or imperfect`, in the book's `Troubleshooting Quick Lookup Table` - the AB900's version of the Condition / Reason / Solve matrix, headed `Happening / Caused / Processing Step`.

| Caused | Processing Step |
|---|---|
| 1. LCD backlight damage. 2. Console power is too low. | 1. Replace the new LCD module or the control electronics. 2. Check whether the battery is 1.5V/each. 3. Check the power of the console. |

**The figure is 1.5 V per battery.** The AB900 console runs on batteries, not a generator or an adapter, so the "power too low" cause the other Spirit bike matrices answer with a wall voltage or a generator connection is answered here with a battery check. The Q&A chapter of the same book says there are **four** batteries under the battery cover: `ab900-2018-errors-console-without-display-check-the-four-batteries`.

The table has no row for dead segments. Its other three rows are heart rate: a wrong reading (`spirit-erratic-pulse-display`), a chest strap that reads nothing (`spirit-wireless-chest-belt-no-pulse`) and one that only reads very close to the console.
