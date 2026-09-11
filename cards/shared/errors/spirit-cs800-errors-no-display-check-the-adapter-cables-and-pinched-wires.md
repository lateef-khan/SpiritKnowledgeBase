---
id: spirit-cs800-errors-no-display-check-the-adapter-cables-and-pinched-wires
title: 'No display on the stepper console: the power adapter and its position, every
  computer cable, then the wires inside the console and chain cover for a pinch or
  a break'
kind: troubleshooting
question: What do I check when the console on a Spirit CS800 stepper shows nothing?
asked_as:
- cs800 console blank
- no display on my spirit stepper
- stepper screen dead after moving it
- cs800 power adapter check
keywords:
- no display
- power adapter
- computer cable
- pinched wires
- chain cover
- console wires
- broken wire
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - cs800-2016
  - cs800-2021
  section: errors
  code: no-display
authority: 3
not_to_be_confused_with:
- spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse
see_also:
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
- spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse
- sc200-2016-no-display
- sc200-2019-no-display
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: CS800 (2020) service manual 9-1 Troubleshooting for the console, PDF p.
    37 (printed 36); text.md lines 568-584. CS800 2016 (XS200-SS003) service manual
    10-1 Console Problem, PDF p. 64; text.md lines 910-926
  extracted_at: '2026-09-11'
---

Both CS800 service manuals answer a blank console with the same three checks; the 2016 book's wording is longer.

**CS800 (2020) book - 9-1.** *Situation: No display on monitor.*

1. Check the power supply or test with a new one.
2. Check all computer cables are plug well.
3. Check all wires inside the console and the chain cover are plug well. And check there are no pinched wires.

**CS800 2016 (XS200-SS003) book - 10-1.**

1. Under normal use console screen will display, if there is no display, first check **power adapter** to make sure it is in the correct position. Check all connectors, including those in the console, on the controller and wire harness, are connected properly.
2. Next, check if all the wires are inserted in the firmly and securely on to the console.
3. Remove console cover, left and right chain covers, check if all the wires are inserted in the correct positions and check if whether the wires broken.

**These are adapter-powered machines, and the adapter is the first check** - "in the correct position" means seated in its jack, and "test with a new one" means substitution. No voltage is printed here; the matrix row for a dim display in the same books is where the supply figure lives (`cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt` for the 2020 book's `220-240V or 110-120V`).

**The chain covers come off in step 3.** The DC power wire runs through the right chain cover on this machine (the cover replacement steps have you unmount the DC socket nut from it), which is why a pinched wire behind the covers can kill the console.

The XS895 answers the same symptom with an AC switch and a fuse instead, because it is a mains machine (`spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse`). Sole prints this page for its SC200 steppers: `sc200-2016-no-display`, `sc200-2019-no-display`.
