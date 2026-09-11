---
id: jb950-2022-errors-leds-not-bright-enough-30-v-at-30-rpm
title: 'The LEDs are not bright enough: brightness setting, board connections, then
  a generator that must give 30 V at 30 RPM'
kind: troubleshooting
question: Why is the display dim on a Spirit jb950-2022 Johnny G bike, and what should
  the generator put out?
asked_as:
- johnny g bike display is dim
- jb950 leds not bright
- spirit indoor bike screen too dark
- what voltage should the jb950 generator make
keywords:
- led brightness
- dim display
- generator output
- 30 v
- 30 rpm
- led board
- mcu board
- controller
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
- spirit-2024-errors-leds-not-bright-generator-power-connection
- ce900-2025-errors-leds-not-bright-incomplete-or-imperfect
see_also:
- ct850-2020-led-displays-dim-or-incomplete
- spirit-2024-errors-leds-not-bright-generator-power-connection
- jb950-2022-errors-no-resistance-control-board-wiring-then-brake-test
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.4 Troubleshooting procedure matrix, PDF p.
    45, text.md lines 839-868
  extracted_at: '2026-09-11'
---

The condition is printed as `LEDs not bright enough`.

| Reason | Solving |
|---|---|
| 1. LED brightness set to low. 2. LED board malfunction. 3. Generator Power to console too low. | 1. Check LED brightness setting in maintenance mode. 2. Check connection between LED board and MCU board. 3. Check connection between generator and controller. 4. Check generator output. If the output at 30 RPM is below 30 V, replace the generator. 5. Replace LED board. 6. Replace controller. |

**The one figure in the row: the generator must put out at least 30 V at 30 RPM.** Below that, replace the generator. No other Spirit bike prints a generator output figure for this symptom - the CU800 and CR800 books say only *check generator power connection* (`spirit-2024-errors-leds-not-bright-generator-power-connection`).

The first step is a setting, not a fault: `LED BRIGHTNESS` in maintenance mode runs 1 to 3 and defaults to 2 - a console fact. The LED board and the MCU board are the two boards inside the console (the wiring chapter shows the display cable at J2 of the MCU board); the controller is the lower board under the chain covers.

Dead segments rather than a dim display are the next row down: `ct850-2020-led-displays-dim-or-incomplete`.
