---
id: crw800-2024-errors-lcd-display-does-not-shine
title: The display does not shine or is incomplete, on the row that asks for AC100 to 240V in and DC12V out
kind: troubleshooting
question: Why is the display dim, blank or partly lit on a Spirit CRW800-2024 rower?
asked_as:
- my rowing machine screen is dim
- crw800 display wont light up
- rower console backlight is faint
keywords:
- lcd
- backlight
- dim display
- ac100-240v
- dc12v
- cable tensioner
- control electronics
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- ct850-2020-led-dim-or-incomplete
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
- spirit-2024-errors-leds-not-bright-generator-power-connection
see_also:
- crw800-2024-errors-e2-cable-tension-communication-error
- spirit-lcd-dim-or-incomplete
- crw800h2o-console-shows-no-display
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING, Happening / Caused / Processing Step table on printed page
    32. That page is a flat picture with no text layer and was read from the rendered
    page.
  extracted_at: '2026-09-10'
---

The condition is printed as `LCD display does not shine, incomplete or imperfect`.

| Caused | Processing Step |
|---|---|
| LCD backlight damage | Replace the new LCD module or the control electronics |
| Console power is too low | 1. Check whether the AC power input is **AC100 ~ 240V** and the output is **DC12V**. 2. Check the power of the console. 3. Has the cable tensioner output **DC12V**, if not, please replace the new cable tensioner. |

**Three figures, and no other Spirit manual prints this set.** The rower takes a wide-input adapter -
`AC100 ~ 240V` in, `DC12V` out - where the mains-powered Spirit consoles ask for `110-120V`,
`120V` or `220-240V or 110-120V` at the wall
(`spirit-lcd-dim-or-incomplete`, `ct850-2020-led-dim-or-incomplete`,
`cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt`) and the generator-powered ones ask for
nothing at all
(`spirit-2024-errors-leds-not-bright-generator-power-connection`). **Do not carry a 120 V figure onto
this machine.**

**The third step is the odd one, and it is the only tensioner measurement in the book.** It asks
whether the *cable tensioner* is putting out DC12V, which makes the tensioner a source of console
power on this machine and not only a resistance unit. The error code `E2` is a cable tension
communication error and prints no check of its own
(`crw800-2024-errors-e2-cable-tension-communication-error`); this is the measurement to use.

**This machine has no second row for dead segments.** Every other Spirit troubleshooting matrix in
the repository carries one; this one goes straight from the backlight row to the heart rate rows.
