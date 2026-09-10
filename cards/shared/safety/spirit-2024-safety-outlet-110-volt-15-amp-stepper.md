---
id: spirit-2024-safety-outlet-110-volt-15-amp-stepper
title: The outlet is 110-volt, 15-amp but the breaker sentence on the next page asks for 5 amps
kind: spec
question: What outlet and circuit does a Spirit CRS800S-2024 semi-recumbent stepper or CS800-2024
  stepper need?
asked_as:
- what outlet does the stepper need
- what amp breaker for the crs800s or cs800
- does the stepper need its own circuit
- the manual says two different amp ratings
keywords:
- outlet
- 110 volt
- 15 amp
- 5 amp
- circuit breaker
- dedicated circuit
- grounded outlet
- contradiction
- extension cord
- dc power cord
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2024
  - cs800-2024
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-safety-outlet-and-circuit-requirement
- spirit-ct800-safety-outlet-110-volt-15-amp
- spirit-ct800-safety-outlet-120-volt-15-amp
- csc900-2024-safety-outlet-120-or-230-volt
- cvc800-outlet-and-circuit-requirement
see_also:
- spirit-2024-safety-instructions-list-stepper
- spirit-house-breaker-needs-a-high-inrush-type
- spirit-product-must-be-grounded
- spirit-2024-safety-grounding-page-says-110-volt
- xt-2015-safety-extension-cord-14-awg-or-better
source:
  ref: spirit-climber-crs800s-2024-owners-manual
  locator: SAFETY INSTRUCTIONS WARNING header, printed page 5 (PDF page 7), and the circuit-breaker
    paragraph closing ELECTRICAL SAFETY on printed page 6 (PDF page 8). The CS800-2024 owner's
    manual prints the same two sentences on its printed pages 5 and 6, and adds a GROUNDING
    page on its printed page 7
  extracted_at: '2026-09-10'
---

**Both manuals state it twice, and the two statements do not agree.**

The WARNING header of the safety instructions:

> To reduce the risk of burns, fire, electric shock, or injury to persons, install the stepper on a
> flat level surface with access to a **110-volt, 15-amp** grounded outlet with only the stepper
> plugged into the circuit.

The circuit-breaker paragraph closing the electrical page:

> The electrical outlet used should have a dedicated **5-amp** circuit breaker.

| Statement | Page | Figure |
|---|---|---|
| Install on a grounded outlet | printed 5 | 110 volt, **15 amp** |
| Dedicated circuit breaker | printed 6 | **5 amp** |

**Neither manual reconciles them**, and neither figure is retracted. Quote both and say which page
each is on. A 5-amp breaker on a 15-amp outlet is not the same circuit, and the manual does not say
which it means.

- **110 volt** is the only voltage figure. The CS800's grounding page confirms it:
  `This product is for use on a nominal 110-volt circuit`, with no amperage attached
  (`spirit-2024-safety-grounding-page-says-110-volt`).
- **Only the stepper on the circuit.** The header says so.
- **An extension cord must be 14AWG or better with only one outlet on the end**
  (`xt-2015-safety-extension-cord-14-awg-or-better`).

**The CRS800S has no grounding page at all.** Its safety chapter ends at the electrical page; the
CS800 book adds `GROUNDING & IMPORTANT OPERATION INSTRUCTIONS` on its printed page 7 and the
CRS800S does not.

**The CRS800S console is fed by a DC power cord.** Its setting-up page says `When the DC Power cord
is connected to the equipment, the console will automatically power up`, and a `Power Cord` is
listed among the parts in the carton. The 110-volt figure above is the wall supply, not the console
input; the manual prints no DC voltage figure.

**This is not the CE850 figure.** The CE850-2024 elliptical prints the same page word for word with
**5 amps** in the header, matching its own 5-amp breaker sentence
(`spirit-ce850-safety-outlet-and-circuit-requirement`). The steppers changed the header figure to 15
and left the breaker sentence at 5. Never quote 5 amps as a stepper's outlet rating or 15 amps as a
CE850's.
