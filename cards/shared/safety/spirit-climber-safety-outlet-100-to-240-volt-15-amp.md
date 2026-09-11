---
id: spirit-climber-safety-outlet-100-to-240-volt-15-amp
title: An outlet anywhere from 100 to 240 volts AC at 50/60 Hz on a 15-amp circuit,
  with nothing else on it
kind: spec
question: What outlet and circuit does a Spirit 7.0S, 7.5S or 8.5S stepper or an MS300
  rehabilitation recumbent stepper need?
asked_as:
- what outlet does the 8.5s stepper need
- is the 7.0s 110 or 220 volt
- what amp circuit for the ms300
- can i plug the stepper into a normal socket
keywords:
- outlet
- 100 to 240 volt
- 50/60 hz
- 15 amp
- dedicated circuit
- only appliance
- universal voltage
- mains
- power requirement
- grounded outlet
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - 85s-2025
  - ms300-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-safety-outlet-120-volt-15-amp-fit
- spirit-2024-safety-outlet-110-volt-15-amp-stepper
- spirit-climber-safety-outlet-110-volt-5-amp
- cvc800-outlet-and-circuit-requirement
- csc900-2024-safety-outlet-120-or-230-volt
- spirit-2026t-safety-outlet-and-circuit-requirement
see_also:
- spirit-climber-safety-instructions-list-nineteen-items
- spirit-climber-safety-instructions-list-twenty-four-items
- ms300-2021-safety-packaging-symbols-and-template-defects
- spirit-product-must-be-grounded
- spirit-climber-safety-product-labels-stepper
- spirit-climber-85s-specs-mains-power-supply
- spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating
source:
  ref: spirit-climber-85s-2025-owners-manual
  locator: 'SAFETY INSTRUCTIONS item 2, printed page 4 (PDF page 6). The 7.0S and
    7.5S print it as item 2 of their printed page 4, and the MS300 as the second Warning
    bullet of its Important safety instructions, printed page 5. 7.5S (RS9600-SS021)
    service manual: 5.2.3 Troubleshooting, No power, PDF p. 13 (printed 13), text.md
    lines 125-140, in spirit-stepper-7-5s-med-service-manual. 8.5S (MS2000-SB036-01)
    service manual: 5-1 No power, PDF p. 16 (printed 16), lines 216-234 and OCR supplement
    lines 809-840 (the figure captions are images), and the rating label photographed
    on PDF p. 4, in spirit-stepper-85s-2025-service-manual.'
  extracted_at: '2026-09-10'
---

**These six machines take any ordinary mains supply. The figure is a range, not a single voltage.**

> To reduce the risk of burns, fire, electric shock, or injury to persons, install the 8.5S on a flat
> level surface with access to a **100 to 240-volt AC, 50/60 Hz, 15-amp** grounded outlet. ... The
> 8.5S should be the only appliance in the electrical circuit.

- **100 to 240 volts AC, 50 or 60 Hz.** A universal-input supply; the same machine runs on a North
  American and a European socket.
- **15 amp.**
- **A flat level surface**, and **nothing else on the circuit**.

| Machine | Wording of item 2 |
|---|---|
| 7.0S, 7.5S | `100 to 240-volt AC, 50/60 Hz, 15-amp outlet` - the word *grounded* is not printed |
| 8.5S | `100 to 240-volt AC, 50/60 Hz, 15-amp grounded outlet` |
| MS300 | `100 to 240-volt AC, 50/60 Hz, 15-amp outlet`, and `The unit should be the only appliance in the electrical circuit` |

**Only the 8.5S adds the adapter and extension-cord rules** to the same item:

> Do not use an extension cord unless it is **16awg or larger**, with only one outlet on the end. ...
> Do not attempt to disable the grounded plug by using improper adapters, or in any way modify the
> cord set; a serious shock or fire hazard may result along with computer malfunctions.

The 7.0S, 7.5S and MS300 print no extension-cord gauge at all. Do not carry the 16awg figure onto
them, and do not carry the 14AWG figure of the older Spirit steppers onto any of these four
(`xt-2015-safety-extension-cord-14-awg-or-better`).

**The specification pages print a current draw, not a circuit rating.** The 7.0S, 7.5S and MS300
give `Input: 100-240V ~: 50/60 Hz: 0.6-0.4A` with a `12 VDC, 2.74 Amps` adapter, and the 8.5S gives
`100 ~ 240 Vac, 1.76 ~ 0.71 Amps, 50/60Hz`. Those are what the machine consumes. The 15 amps above
is what the outlet must be rated for; the two are not the same number and neither replaces the other.

**The MS300 contradicts this on its own packaging-symbols page**, which prints
`AC power 220-240 Volt, 10Amps, 50Hz` - a single European figure, half the amperage, and no 60 Hz.
The manual never reconciles the two (`ms300-2021-safety-packaging-symbols-and-template-defects`).

**The 8.5S-Fit is not one of these machines.** Its item 2 asks for a **120 Volt AC, 15-amp** outlet
and its grounding page names a nominal 120-volt circuit
(`spirit-climber-safety-outlet-120-volt-15-amp-fit`).

## The service manuals print no requirement, and two figures of their own

**Neither the 7.5S (RS9600-SS021) nor the 8.5S (MS2000-SB036-01) service manual prints an outlet requirement, a safety
list or a grounding page.** What each prints is a no-power test:

- **7.5S**: `Make sure the A.C. outlet has power (90~240VAC) and the line cord is plugged in securely to the AC adapter`,
  then `Make sure there is 12V DC at the DC plug of the adaptor and plug into the DC jack of the stepper`. **90, not
  100**, at the bottom of the range - a test threshold, not the requirement on this card - and the machine takes its
  power through an external **12 V DC adaptor**, which the owner's manual does not say.
- **8.5S**: measure the AC input at `CN1` of the power supply module, `110 VAC or 220 VAC depending on the mains voltage`
  in the figure captions, and check the power switch and the fuse. Its rating label, photographed on the serial-number
  page, reads `~100-240V, 50/60Hz, 1.76-0.71A` beside a `Replacement Fuse: 5A, 250V` label
  (`spirit-climber-safety-product-labels-stepper`, `spirit-climber-85s-specs-mains-power-supply`). The 8.5S has an IEC
  inlet and a rocker switch on its rear panel, not an adaptor.

The 15 amp circuit and the "only appliance" rule remain the owner's manuals' alone. The 2019 Spirit Fitness power sheet
says all medical equipment requires power and puts the MS300 at 120V/15AMP; it predates the 7.5S and 8.5S
(`spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating`).
