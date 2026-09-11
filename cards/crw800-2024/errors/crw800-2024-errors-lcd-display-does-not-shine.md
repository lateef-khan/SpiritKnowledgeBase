---
id: crw800-2024-errors-lcd-display-does-not-shine
title: The display does not shine or is incomplete, on the row that asks for AC100
  to 240V in and DC12V out
kind: troubleshooting
question: Why is the display dim, blank or partly lit on a Spirit CRW800 2016, CRW800
  2024 or XRW600 rower?
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
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2024
  - xrw600-2019
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- ct850-2020-led-dim-or-incomplete
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
- spirit-2024-errors-leds-not-bright-generator-power-connection
- crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator
see_also:
- crw800-2024-errors-e2-cable-tension-communication-error
- spirit-lcd-dim-or-incomplete
- crw800h2o-console-shows-no-display
- crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator
- spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter
- sr500-2016-lcd-dim-or-incomplete
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING, Happening / Caused / Processing Step table on printed
    page 32. That page is a flat picture with no text layer and was read from the
    rendered page; CRW800 2016 (CW800-YR001) service manual 8.5 Troubleshooting Quick
    Lookup Table, PDF p. 38-39, text.md lines 487-519; XRW600 (DW400-YR002) service
    manual 8.5 Troubleshooting Quick Lookup Table, PDF p. 38-39, text.md lines 478-505;
    CRW800 2021 (800940) service manual 7-5 Troubleshooting Quick Lookup Table, PDF
    p. 37 (printed 36), text.md lines 536-561; CRW800 2016 8.6 Console (Electronic
    Desk) problem, PDF p. 39, text.md lines 523-526; XRW600 8.6 Console problem, PDF
    p. 39, text.md lines 507-510
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

## The 2016 CRW800 and the XRW600 service manuals print this row word for word

Same condition, same two causes, same four steps with `AC100 ~ 240V`, `DC12V` and the tensioner's `DC12V` - the XRW600 writing *tension motor* where the CRW800 writes *cable tensioner*. So the figures the 2024 owner's manual prints are the ones the 2016 service manual printed eight years earlier; the machine has always been an adapter-fed rower.

Both books add a paragraph the owner's manual does not, under **Console problem**:

> The normal operation of the console screen will be normal display, if not light up check the power adapter is the normal power supply or change another one to check is work or check the adapter is correctly inserted into the DC jack, and then check all the wire is indeed plug in the console, the console cover removed to check whether all the wires inserted in the correct location, and check whether the wire fracture.

So: substitute the adapter, check it is seated in the DC jack, then every wire into the console, then the wires under the console cover for a fracture.

**The CRW800 of the 2021 service manual is not on this card.** That machine is generator-powered and its row says *check the battery* and *check the generator* with no wall voltage: `crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator`. Establish which CRW800 the caller has - the 2016 and 2024 books are adapter machines, the 2021 book is a generator machine - before quoting a voltage. Sole's SR500 2016 prints this row for its own rower (`sr500-2016-lcd-dim-or-incomplete`).
