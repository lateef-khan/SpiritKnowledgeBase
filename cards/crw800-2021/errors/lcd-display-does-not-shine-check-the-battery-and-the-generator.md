---
id: crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator
title: The display does not shine or is incomplete on the generator-powered rower,
  and the checks are the battery, the console power and the generator
kind: troubleshooting
question: Why is the display dim, blank or partly lit on a Spirit crw800-2021 rower?
asked_as:
- crw800 screen dead after rowing stops
- spirit rower display faint
- rower console wont light up no generator power
keywords:
- lcd
- backlight
- dim display
- battery
- generator
- generator controller
- console power
- rower
- no display
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2021
  applies_to:
  - crw800-2021
  section: errors
  code: no-display
  model_number:
  - '800940'
authority: 3
not_to_be_confused_with:
- crw800-2024-errors-lcd-display-does-not-shine
- spirit-lcd-dim-or-incomplete
see_also:
- crw800-2024-errors-lcd-display-does-not-shine
- crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller
- spirit-crw800-errors-count-not-shown-or-no-display-check-board-34-and-the-three-cables
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 7-5 Troubleshooting Quick Lookup Table, first row, PDF p. 37 (printed 36),
    text.md lines 536-541; and 7-6 Console (Electronic Desk) problem, PDF p. 38 (printed
    37), text.md lines 566-569
  extracted_at: '2026-09-11'
---

**This row is not the one the CRW800 2024 owner's manual and the 2016 book print.** Those ask for `AC100 ~ 240V` into an adapter and `DC12V` out of it (`crw800-2024-errors-lcd-display-does-not-shine`). The 2021 `800940` book is a generator-powered CRW800 and its row names no wall voltage at all.

The condition is printed as `LCD display does not shine, incomplete or imperfect`.

| Caused | Processing Step |
|---|---|
| 1. LCD backlight damage. 2. Console power is too low. | 1. Check the battery. 2. Replace the new LCD module or the control electronics. 3. Check the power of the console. 4. Check the generator. |

**A battery, a generator, and no adapter.** The console on this machine is kept alive by batteries (the book has a *Batteries replacement* page: one screw on the battery cover on the back of the console) and powered under way by the generator in the flywheel through its controller. So the first check is the cells, the last is the generator, and there is nothing to measure at a wall.

**The book's own paragraph on a dark console**, from 7-6, sends you along the same chain in more words:

> The normal operation of the console screen will be normal display, if not light up check the generator power is the normal power supply or change another one to check is work or check the generator controller is correctly, the controller have output voltage, and then check all the wire is indeed plug in the console, the console cover removed to check whether all the wires inserted in the correct location, and check whether the wire fracture.

So: generator supply, then generator controller output, then every wire into the console, then the wires inside the console cover for a fracture. **No figure is printed for the controller's output** here; the only voltages in the book are the tensioner test's 4 to 6 V (`crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller`).

**This book has no second row for dead segments**, as the 2024 owner's manual has none.

A console that lights but does not count is a different question in the same book's Q&A: `spirit-crw800-errors-count-not-shown-or-no-display-check-board-34-and-the-three-cables`.
