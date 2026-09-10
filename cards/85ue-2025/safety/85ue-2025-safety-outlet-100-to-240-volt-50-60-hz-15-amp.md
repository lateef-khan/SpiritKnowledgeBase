---
id: 85ue-2025-safety-outlet-100-to-240-volt-50-60-hz-15-amp
title: A 100 to 240 volt AC, 50/60 Hz, 15-amp grounded outlet with nothing else on the circuit,
  for a machine that draws under 2 amps
kind: spec
question: What outlet, circuit and extension cord does a Spirit 8.5UE upper body ergometer
  (85ue-2025) need?
asked_as:
- what outlet does the 8.5ue need
- can i plug the upper body ergometer into a normal socket
- can i use an extension cord with the 8.5ue
- what voltage does the arm ergometer run on
keywords:
- outlet
- voltage
- amperage
- 100 to 240 volt
- 50/60 hz
- 15 amp
- extension cord
- 16awg
- dedicated circuit
- power supply
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: safety
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- spirit-climber-safety-outlet-100-to-240-volt-15-amp
- spirit-xe-safety-outlet-110-volt-15-amp
- spirit-water-rower-safety-four-aa-batteries-and-no-electrical-page
- crw800-2024-safety-console-runs-on-two-c-batteries
see_also:
- spirit-product-must-be-grounded
- 85ue-2025-safety-instructions-list
- 85ue-2025-safety-operating-environment-iec-60601
- spirit-extension-cord-16-awg-or-better
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: SAFETY INSTRUCTIONS item 2 and item 3, printed page 4 (PDF page 6); ELECTRICAL SAFETY,
    printed page 6 (PDF page 8); and the Power supply block of SPECIFICATIONS, printed page 55
    (PDF page 57)
  extracted_at: '2026-09-10'
---

> To reduce the risk of burns, fire, electric shock, or injury to persons, install this equipment on
> a flat level surface with access to a **100 to 240-volt AC, 50/60 Hz, 15-amp grounded outlet**. Do
> not use an extension cord unless it is **16awg or larger**, with only one outlet on the end. This
> equipment should be the only appliance in the electrical circuit. Do not attempt to disable the
> grounded plug by using improper adapters, or in any way modify the cord set; a serious shock or
> fire hazard may result along with computer malfunctions.

| Requirement | Figure |
|---|---|
| Nominal supply | **100 to 240 volt AC** - a range, not a single voltage |
| Frequency | **50/60 Hz** |
| Circuit | **15 amp**, and the ergometer the only appliance on it |
| Outlet | grounded, and the supply main must have **protective earth** (item 3) |
| Extension cord | **16awg or larger**, one outlet on the end |
| Surface | flat and level |

**The machine itself draws far less than 15 amps.** The specification page states the actual load:

> Power supply: 100 ~ 240 Vac, **1.76 ~ 0.71 Amps**, 50/60Hz

So it draws 1.76 A at 100 V falling to 0.71 A at 240 V. **The 15 amp figure is the circuit the
manual requires, not the current the machine takes** - both are printed and the book never puts them
side by side. Give the customer both when they ask about a breaker.

**No NEMA plug type is printed anywhere**, and no dedicated-breaker sentence. The ELECTRICAL SAFETY
page adds the supply-tolerance rule instead:

> Never remove any cover without first disconnecting AC power. If voltage varies by 10% or more
> outside the specified range (100 to 240V), the performance of your equipment may be affected. Such
> conditions are not covered under your warranty.

**A wide-range supply is what makes this a 100-240 V machine rather than a 110 V one.** Do not
answer from the Spirit rower or elliptical cards - the two XRW600 rowers need a 110-volt, 15-amp
outlet and a 14AWG cord (`spirit-xe-safety-outlet-110-volt-15-amp`), and no other rower needs a
socket at all (`spirit-water-rower-safety-four-aa-batteries-and-no-electrical-page`,
`crw800-2024-safety-console-runs-on-two-c-batteries`).

**The Spirit 7.0S, 7.5S and 8.5S steppers and the MS300 print the same block**, with the same
100-240 V, 50/60 Hz, 15-amp figures and the same 16awg cord rule
(`spirit-climber-safety-outlet-100-to-240-volt-15-amp`). They are the same Dyaco MED platform and a
different product line; the figures agree, but quote this card for an ergometer and that one for a
stepper.

**Grounding has a page of its own**, printed page 7, and it is mandatory
(`spirit-product-must-be-grounded`). Its illustration shows a two-pole adapter the text never
permits.
