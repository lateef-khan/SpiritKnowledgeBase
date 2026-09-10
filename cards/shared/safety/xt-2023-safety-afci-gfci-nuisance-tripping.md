---
id: xt-2023-safety-afci-gfci-nuisance-tripping
title: Why an arc-fault or ground-fault breaker trips during a workout
kind: troubleshooting
question: Can a 2015 or 2023 Spirit XT treadmill (XT185, XT285, XT385, XT485, XT685), or a Spirit XE395-2023 elliptical, be plugged into an AFCI or GFCI breaker?
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
  product_line: '*'
  model: '*'
  applies_to:
  - cu800ent-2024
  - xbr25-2023
  - xbr55-2023
  - xbu55-2023
  - xe395-2023
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2015
  - xt685-2023
  - xt685ent-2023
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-never-use-a-gfci-wall-outlet
see_also:
- spirit-house-breaker-needs-a-high-inrush-type
- xt-2023-safety-supply-voltage-variation
- ct900-electrical-safety
- xt-2015-safety-outlet-and-circuit-requirement
- spirit-xe-safety-no-outlet-figure-printed
- spirit-bike-ent-safety-instructions-list
source:
  ref: spirit-treadmill-xt185-2023-owners-manual
  locator: page 6, ELECTRICAL SAFETY; the XT285, XT385, XT485 and XT685 manuals print the same page
    on page 7. The five 2015 XT owner's manuals print it across their Important Electrical
    and Important Grounding Instructions pages (XT185/XT285/XT485 pages 5-6, XT385/XT685
    pages 6-7) The CU800ENT-2024 bike owner's manual prints the same paragraph on its
    ELECTRICAL SAFETY page, printed page 6
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

**The five 2015 XT owner's manuals print this whole passage**, with the word `treadmill` where the
2023 manuals print `unit` - so the 2015 wording reads `the high inrush currents of the treadmill
drive electronics and motor`, `an issue that affects all treadmill brands`, and `Optimally the
treadmill should be the only device plugged into the circuit`.

**The same three breaker brands and series are named, and the same test result.** Eaton (Cutler
Hammer Series), Leviton (Smart lock pro) and Schneider Electric (Canadian home series), none of
which tripped in testing as long as no other device shared the circuit. The list of other devices
that may cause tripping is the same four: fluorescent lights with electronic ballasts, a coffee
maker, a space heater, a hair drier. The built-in surge suppressors are described the same way.

The 2015 manuals also name the circuit the treadmill should have to itself - 110 volt, 15 amp,
grounded, with only the treadmill plugged into it
(`xt-2015-safety-outlet-and-circuit-requirement`).

**The XT685ENT owner's manual prints this whole passage on its Electrical Safety page, page 7**,
in the `unit` wording, and the **XT485ENT owner's manual prints it on its Important Electrical
Instructions page, page 6**, in the `treadmill` wording the 2015 manuals use. The same three
breaker brands and series are named - Eaton (Cutler Hammer Series), Leviton (Smart lock pro) and
Schneider Electric (Canadian home series) - with the same test result, the same four example
devices, and the same built-in surge suppressors.

Both ENT manuals also repeat the check as the same troubleshooting row - "Circuit breaker trips,
but not the treadmill circuit breaker: check that the treadmill is the only appliance in the
circuit" - and add nothing to it.

## The Spirit XE395-2023 elliptical prints this passage on its ELECTRICAL SAFETY page

**In the `unit` wording**, page 6: the same three breaker brands and series - Eaton (Cutler Hammer
Series), Leviton (Smart lock pro) and Schneider Electric (Canadian home series) - with the same test
result, the same built-in surge suppressors, and the same sentence
`Optimally the unit should be the only device plugged into the circuit`.

**Its printing is shorter than the treadmill manuals'.** It carries no `avoid AFCI/GFCI if possible`
opening and **no list of other devices** - no fluorescent lights, coffee maker, space heater or hair
drier - and no troubleshooting row repeating the check. What it prints is the surge-suppressor
sentence, the tested brands and the only-device sentence.

**This is the XE395-2023's only statement about its circuit.** Its manual names no voltage and no
amp figure anywhere (`spirit-xe-safety-no-outlet-figure-printed`), so `Optimally` is as close as it
comes to a dedicated-circuit requirement.

**Its 2021 predecessors print the opposite advice.** The XE195, XE295, XG400 and XE395ENT manuals
carry the high-inrush breaker paragraph instead, with its Grainger and QO120HM part numbers and a
`dedicated 15 amp circuit breaker` (`spirit-house-breaker-needs-a-high-inrush-type`). Neither
passage appears in the other's manual.

**The XE795-2023 manual has no electrical page** and prints none of this.

**The Spirit CU800ENT-2024 upright bike prints the same paragraph in full**, on its ELECTRICAL SAFETY
page - avoid AFCI/GFCI breakers where possible, the high inrush current of the drive electronics as
the cause, that it affects all brands, that local law may require them, and the same examples of
other devices on the circuit that can also trip one: fluorescent lights with electronic ballasts, a
coffee maker, a space heater and a hair drier.

The paragraph names `motor` among the causes; **this bike has no motor**, so read that word as the
drive electronics.

**The CU800ENT-2022 and CR800ENT-2023 print a different breaker paragraph**, naming high-inrush house
breakers, the Grainger 1D237 and QO120HM replacements, and a dedicated 5 amp breaker
(`spirit-house-breaker-needs-a-high-inrush-type`). Different cause, different remedy, different
rating - do not swap the two.

## Three Spirit residential bikes print the same paragraph

**XBR25-2023, XBR55-2023 and XBU55-2023** print it on their ELECTRICAL SAFETY page, word for word,
with the same three tested brands - Eaton (Cutler Hammer Series), Leviton (Smart lock pro) and
Schneider Electric (Canadian home series) - and the same condition, that they do not trip as long as
no other device shares the circuit.

**Their own earlier printings print the opposite advice.** The XBR25-2019, XBR55-2019, XBR55-2021,
XBU55-2019 and XBU55-2021 manuals say a tripping house breaker must be replaced with a high-inrush
type and name Grainger part # 1D237 and QO120HM
(`spirit-house-breaker-needs-a-high-inrush-type`). The 2023 rewrite dropped that and put the surge
suppressor and the tested-breaker list in its place. Answer from the customer's own book.

**The XBR95-2023 manual has no ELECTRICAL SAFETY page and prints neither paragraph.**
