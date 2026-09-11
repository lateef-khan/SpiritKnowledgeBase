---
id: spirit-climber-safety-outlet-110-volt-5-amp
title: A 110-volt 5-amp grounded outlet, the one stepper printing whose outlet and
  breaker figures agree
kind: spec
question: What outlet and circuit does a Spirit CS800-2021 stepper need?
asked_as:
- what outlet does the cs800 stepper need
- what amp breaker for the cs800
- does the 2021 stepper need its own circuit
- is the cs800 5 amp or 15 amp
keywords:
- outlet
- 110 volt
- 5 amp
- circuit breaker
- dedicated circuit
- grounded outlet
- extension cord
- 14awg
- stepper
- nominal 110-volt
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2021
  applies_to:
  - cs800-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-2024-safety-outlet-110-volt-15-amp-stepper
- spirit-ce850-safety-outlet-and-circuit-requirement
- cvc800-outlet-and-circuit-requirement
- spirit-xs895-safety-outlet-120-volt-15-amp
- spirit-climber-safety-outlet-100-to-240-volt-15-amp
see_also:
- spirit-climber-safety-instructions-list-2021-stepper-and-climber
- spirit-house-breaker-needs-a-high-inrush-type
- spirit-product-must-be-grounded
- spirit-temporary-adapter-for-a-two-pole-receptacle
- spirit-ct800-safety-outlet-120-volt-15-amp
- spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating
source:
  ref: spirit-climber-cs800-2021-owners-manual
  locator: 'IMPORTANT SAFETY INSTRUCTIONS WARNING header, printed page 4 (PDF page
    6); the circuit-breaker sentence closing IMPORTANT ELECTRICAL INSTRUCTIONS, printed
    page 5 (PDF page 7); GROUNDING INSTRUCTIONS, printed page 6 (PDF page 8). Read
    from a 300 dpi render of PDF page 6, not from the text layer. CS800-2016 (XS200-SS003)
    service manual: 7-1 to 7-3, PDF p. 30 (printed 30), text.md lines 418-447, in
    spirit-stepper-cs800-2016-service-manual. CS800 (2020) service manual: no safety
    chapter; the matrix row `Check AC power is 220-240V or 110-120V` is 7-7 Troubleshooting
    procedure matrix, PDF p. 33 (printed 32), text.md lines 526-555, in spirit-stepper-cs800-2021-service-manual.'
  extracted_at: '2026-09-10'
---

**110 volt, 5 amp. The CS800-2021 states it three times and all three agree.**

| Where | Printed as |
|---|---|
| Safety instructions, WARNING header | `a 110-volt, **5-amp** grounded outlet` |
| Circuit-breaker sentence | `The electrical outlet used should have a dedicated **5-amp** circuit breaker.` |
| Grounding instructions | `This product is for use on a nominal **110-volt/5-amp** dedicated circuit` |

The 5 in the header was checked on a 300 dpi render of the printed page, not taken from the
extraction.

- **Only the stepper on the circuit.**
- **An extension cord must be 14AWG or better with only one outlet on the end**
  (`xt-2015-safety-extension-cord-14-awg-or-better`).
- **A flat level surface.**

## This is the figure the 2024 CS800 changed, and its stablemate never had

**The 2024 CS800 owner's manual prints 15 amps in the same header** and leaves the breaker sentence
at 5, so the later book contradicts itself where this one does not
(`spirit-2024-safety-outlet-110-volt-15-amp-stepper`).

**The CRS800S-2021, printed five weeks earlier, already said 15.** Its header reads
`a 110-volt, 15-amp grounded outlet` above the same 5-amp breaker sentence. The two 2021 steppers of
the same range therefore give two different outlet ratings, and it is the CS800 that is internally
consistent.

| Machine | Header | Breaker sentence | Agree? |
|---|---|---|---|
| CS800-2021 | 110 V, **5 amp** | 5 amp | yes |
| CRS800S-2021 | 110 V, **15 amp** | 5 amp | no |
| CS800-2024, CRS800S-2024 | 110 V, **15 amp** | 5 amp | no |

**Never quote 15 amps for a CS800-2021.** Ask which year the machine is before answering.

## The 2016 CS800 asked for 120 volts at 15 amps, and the 2021 service manual asks for nothing

**The CS800-2016 (XS200-SS003) service manual prints `a 120-volt, 15-amp (230-volt, 10-amp)grounded outlet with only the
climber plugged into the circuit` and a `nominal 120-volt (230-volt) circuit`** - the figure on
`spirit-ct800-safety-outlet-120-volt-15-amp`, three times the amperage of this card and a different nominal voltage. It
is a different machine from the CS800-2021, five years earlier, so the table above gains a row:

| Machine | Header | Breaker sentence | Agree? |
|---|---|---|---|
| CS800-2016 (service manual) | 120 V, **15 amp** (230 V, 10 amp) | none printed | - |
| CS800-2021 | 110 V, 5 amp | 5 amp | yes |

**The CS800 (2020) service manual for this machine has no safety chapter.** Its contents run Outlines, Electronic Parts,
Electrical Configurations, Product Operation, Unit Block Diagrams, Basic Connections and Wiring, Error Messages, Circuit
diagram, Troubleshooting and Parts Replacement; the words *outlet*, *grounded* and *GFCI* do not appear in it. Its one
supply figure is the troubleshooting-matrix row `Check AC power is 220-240V or 110-120V`, a range and not a requirement.
The 110-volt, 5-amp figure for a CS800-2021 is its owner's manual's alone. The 2019 Spirit Fitness power sheet puts the
CS800 at 120V/15AMP, which is the 2016 machine's figure
(`spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating`).
