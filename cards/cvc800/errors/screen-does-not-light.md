---
id: cvc800-screen-does-not-light
title: The screen does not light at all
kind: troubleshooting
question: Why is there no display at all on a Spirit CVC800 climber?
asked_as:
- spirit climber screen is completely dead
- no lights on the climber console
- cvc800 will not power up
keywords:
- screen does not light
- no display
- dead console
- power adapter
- dc socket
- console wires
- output voltage
- climber
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-lcd-dim-or-incomplete
- spirit-lcd-displays-dim-or-incomplete
- cvc800-e-1-ram-error
- cvc800-tension-motor-voltage-test
source:
  ref: spirit-climber-cvc800-service-manual
  locator: Section 10-1 Troubleshooting For Console, page 48
  extracted_at: '2026-09-08'
---

Three steps, in the manual's order. The condition is printed as `The Screen doesn't lit`.

1. Check all the wires that connect to Console are plug well.
2. Check Power adapter connector is fully insert DC socket.
3. Check Power adapter output voltage is the same as its label shows.

That is the whole of it. **The manual names no voltage** - step 3 asks you to compare the adapter's
measured output against the figure on the adapter's own label, so read the label rather than
assuming a value from another Spirit machine.

This row is about a screen that shows **nothing at all**. A screen that lights but is dim or has
dead areas is covered by two different rows in the section 8-5 matrix:
`spirit-lcd-dim-or-incomplete` and `spirit-lcd-displays-dim-or-incomplete`. A screen that lights and
then prints a code is `cvc800-e-1-ram-error` or `cvc800-e-2-tension-motor-error`.

One wording difference worth knowing before you go looking for the part. This section calls the
supply a **power adapter** feeding a **DC socket**. The tension motor voltage test in section 8-2
ends at a **transformer** instead - step 5 there reads `If there is no voltage, check the
transformer, if there is no output, replace it`. The manual never says whether those are the same
part, so both names are reproduced as printed.

Unlike the CT850 treadmills, this manual prints no separate row for a power switch that will not
light and none for a safety key, and section 10-1 is the only place it deals with a dead console.
