---
id: spirit-med-bike-errors-leds-not-bright-check-power-to-console-then-lower-controller
title: The display light is dim or incomplete on the generator bike, on the row that
  checks power to the console and names no voltage
kind: troubleshooting
question: Why is the display dim or partly lit on a Spirit Medical 4.0R or 4.0U bike?
asked_as:
- 4.0r display is dim
- some of the leds on my spirit medical bike dont light
- 4.0u console half lit
- bike display faint while pedaling
keywords:
- leds not bright
- display dim
- incomplete display
- power to console
- lower controller
- led light broken
- medical bike
- generator
- troubleshooting matrix
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40u-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct850-2020-led-dim-or-incomplete
- spirit-2024-errors-leds-not-bright-generator-power-connection
- spirit-xb-2023-errors-lcd-not-bright-replace-generator-controller
see_also:
- ct850-2020-led-displays-dim-or-incomplete
- spirit-erratic-pulse-display
- spirit-hand-pulse-not-working
- spirit-wireless-chest-belt-no-pulse
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: 4.0R (FR800-SB022-03) service manual 8-4 Troubleshooting procedure matrix,
    PDF p. 31; text.md lines 388-418. 4.0U (FU800-SB022-03) service manual 8-4 Troubleshooting
    Procedure Matrix, PDF p. 31; text.md lines 409-438
  extracted_at: '2026-09-11'
---

The condition is printed as `LEDs not bright, incomplete or imperfect`, the first row of the 8-4 Troubleshooting procedure matrix, and both books print it the same.

| Reason | Solve |
|---|---|
| LED light is broken | Replace with new LED or console |
| Power to console too low | Check power to console. Replace lower controller. |

**No voltage figure is printed.** These bikes have no mains cord - the console is fed by the pedal generator through the generator/brake controller (the book's *lower controller*) - so there is nothing at a wall to measure, and the row goes from "check power to console" straight to the controller. Do not borrow the `120V` the 4.0T treadmill prints on the same row (`ct850-2020-led-dim-or-incomplete`), nor the "check generator power connection" wording of the CU800/CR800 books (`spirit-2024-errors-leds-not-bright-generator-power-connection`) - the medical books name the lower controller as the part.

Dead segments rather than a dim light are the next row down, and that one the medical bikes share word for word with the CT850 2020 and the CR900/CU900 2025: `ct850-2020-led-displays-dim-or-incomplete`.

The other rows of the same matrix - erratic pulse, hand pulse lost, chest belt lost, chest belt too close - are the Spirit-wide rows `spirit-erratic-pulse-display`, `spirit-hand-pulse-not-working` and `spirit-wireless-chest-belt-no-pulse`.

