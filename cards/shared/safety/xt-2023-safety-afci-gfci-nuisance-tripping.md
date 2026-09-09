---
id: xt-2023-safety-afci-gfci-nuisance-tripping
title: Why an arc-fault or ground-fault breaker trips during a workout
kind: troubleshooting
question: Can a Spirit XT185-2023, XT285-2023, XT385-2023, XT485-2023 or XT685-2023 treadmill be plugged into an AFCI or GFCI breaker?
asked_as:
- my breaker trips when i run on the treadmill
- can a treadmill go on an arc fault breaker
- gfci keeps tripping with the treadmill
keywords:
- afci
- gfci
- arc fault
- ground fault
- nuisance tripping
- inrush current
- surge suppressor
- eaton
- leviton
- schneider
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2023
  - xt285-2023
  - xt385-2023
  - xt485-2023
  - xt685-2023
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-never-use-a-gfci-wall-outlet
see_also:
- spirit-house-breaker-needs-a-high-inrush-type
- xt-2023-safety-supply-voltage-variation
- ct900-electrical-safety
source:
  ref: spirit-treadmill-xt185-2023-owners-manual
  locator: page 6, ELECTRICAL SAFETY; the XT285, XT385, XT485 and XT685 manuals print the same page on page 7
  extracted_at: '2026-09-09'
---

**Avoid AFCI/GFCI circuit breakers if possible.** They may trip occasionally during exercise
because of the **high inrush currents of the unit drive electronics and motor**, an issue the
manual says **affects all unit brands**. New laws in your area may require these breakers.

If you have them and are getting nuisance tripping, **check whether any other device is
plugged into the same circuit**. The manual's examples of other devices that may cause
tripping: fluorescent lights with electronic ballasts, a coffee maker, a space heater, a hair
drier.

> Optimally the unit should be the only device plugged into the circuit.

The units have **surge suppressors built in** to help avoid nuisance tripping. Breakers and
outlets that have been tested with these products, and **did not trip in that testing as long
as no other devices were plugged into the same circuit**:

| Brand | Series tested |
|---|---|
| Eaton | Cutler Hammer Series |
| Leviton | Smart lock pro |
| Schneider Electric | Canadian home series |

The troubleshooting table later in these same manuals repeats the check as a symptom row -
"Circuit breaker trips, but not the treadmill: check that the treadmill is the only appliance
in the circuit" - and points the reader back to this Electrical Safety section. It adds no
new action.

**Do not answer this from the Spirit CT850 or CVC800 rule.** Those service manuals say
"Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill"
(`spirit-never-use-a-gfci-wall-outlet`), an outright ban with no tested brands. These five
owner's manuals say "avoid if possible" and name breakers that passed testing. Two different
instructions for two different machine families.
