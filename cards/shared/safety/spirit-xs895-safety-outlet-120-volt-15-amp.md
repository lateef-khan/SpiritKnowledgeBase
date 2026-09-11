---
id: spirit-xs895-safety-outlet-120-volt-15-amp
title: A 120-volt 15-amp outlet on the safety page and a nominal 110-volt circuit
  on the grounding page
kind: spec
question: What outlet and circuit does a Spirit XS895 incline stepper need?
asked_as:
- what outlet does the xs895 need
- what amp breaker for the incline stepper
- is the xs895 110 or 120 volt
- the manual says two different voltages
keywords:
- outlet
- 120 volt
- 110 volt
- 15 amp
- dedicated circuit
- circuit breaker
- grounded outlet
- extension cord
- 14awg
- contradiction
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-safety-outlet-120-volt-15-amp
- spirit-2024-safety-outlet-110-volt-15-amp-stepper
- spirit-climber-safety-outlet-110-volt-5-amp
- cvc800-outlet-and-circuit-requirement
- spirit-climber-safety-outlet-120-volt-15-amp-fit
see_also:
- spirit-xs895-safety-instructions-list
- spirit-house-breaker-needs-a-high-inrush-type
- spirit-temporary-adapter-for-a-two-pole-receptacle
- spirit-product-must-be-grounded
- spirit-treadmill-safety-outlet-220-volt-10-amp
- spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating
source:
  ref: spirit-climber-xs895-2018-owners-manual
  locator: 'Important Safety Instructions WARNING header, printed page 4 (PDF page
    4); Circuit Breakers and Grounding Instructions, printed page 6 (PDF page 6).
    The 2021 printing prints the same three sentences on the same printed pages. XS895
    (XS300B-YS006) service manual: no safety chapter; 4-2-1 POWER, PDF p. 12 (printed
    11), text.md lines 163-195, and the matrix row `Check AC power is 110-120V or
    220-240V`, 7-8 Troubleshooting procedure matrix, PDF p. 36 (printed 35), lines
    550-588, in spirit-stepper-xs895-2021-service-manual.'
  extracted_at: '2026-09-10'
---

**The manual states the supply three times and one of the three disagrees.**

| Where | Printed as |
|---|---|
| Safety instructions, WARNING header | `a **120-volt**, 15-amp grounded outlet` |
| Circuit Breakers paragraph | `a dedicated **15 amp** circuit breaker` |
| Grounding Instructions | `This product is for use on a nominal **110-volt**/15 amp dedicated circuit` |

**The amperage never moves - 15 amps in all three places.** Only the voltage changes, 120 on the
safety page and 110 on the grounding page. Neither figure is retracted and the manual does not say
which it means. Quote both and say which page each is on.

- **Only the Incline Stepper on the circuit.** The header says so.
- **An extension cord must be 14AWG or better with only one outlet on the end**
  (`xt-2015-safety-extension-cord-14-awg-or-better`).
- **A flat level surface.**

The assembly chapter states it a fourth time, in passing, and agrees with the safety page:
`connected directly to 120-volt,15-amp`, beside the power switch where the line cord enters the
machine.

**Both printings say the same thing.** The 2018 and 2021 XS895 safety chapters match at 99.8% on an
order-free word count of the printed pages, and every electrical figure on them is identical.

**15 amps here is not the 5 amps of the CS800 and CVC800.** Those two 2021 machines ask for a 5-amp
breaker and the CVC800 for a 1.5-amp outlet
(`spirit-climber-safety-outlet-110-volt-5-amp`, `cvc800-outlet-and-circuit-requirement`).

## The service manual prints no safety chapter, and adds a 220-volt alternative

**The XS895 (XS300B-YS006) service manual has no Product Safety Instructions chapter** - its contents run from Outlines
to Parts Replacement with no section 7 of that kind, and the words *outlet*, *grounded* and *GFCI* appear nowhere in it.
Its one supply statement is the POWER paragraph of Product Operation:

> These models are connected directly to 120-volt,15-amp or 220-volt,10-amp and there is a power switch located where
> the line cord plugs into the unit on the left side near the middle.

- **120 volt, 15 amp** - the safety-page figure of both owner's manuals, and the sentence the owner's assembly chapter
  prints without the alternative.
- **Or 220 volt, 10 amp** - a second build the owner's manuals never mention. It is the figure the treadmill service
  manuals give for a 230-volt supply (`spirit-treadmill-safety-outlet-220-volt-10-amp`).
- **The power switch is on the left side near the middle**, where the line cord enters.

Its troubleshooting matrix treats both as one acceptable range - `Check AC power is 110-120V or 220-240V` - and the
service manual prints no 110-volt grounding sentence, so the owner's-manual contradiction above is not repeated in it.
The 2019 Spirit Fitness power sheet puts the XS895 at 120V/15AMP
(`spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating`).
