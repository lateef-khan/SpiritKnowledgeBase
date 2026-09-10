---
id: spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply
title: Twelve volts DC at 2.74 amps from a named 30 watt Sinpro external supply
kind: spec
question: What power supply does a Spirit MS300, 7.0S or 7.5S rehabilitation recumbent
  stepper use?
asked_as:
- what power supply does the ms300 use
- my 7.5s adapter is lost what do i order
- what voltage does the rehab stepper run on
- is the 7.0s stepper 12 volt
keywords:
- power supply
- adapter
- adaptor
- sinpro
- 12 vdc
- volts
- amps
- transformer
- wall wart
- mopp
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
  - ms300-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-85s-specs-mains-power-supply
see_also:
- spirit-climber-specs-fuse-rating
- spirit-climber-specs-rehabilitation-stepper-brake-magnets-on-a-disc
- spirit-climber-specs-rehabilitation-stepper-specification-page
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: SPECIFICATIONS, printed p. 41 (PDF p. 43), the Input power and External
    power supply rows; the same rows are 7.5S-2025 printed p. 43 (PDF p. 45) and MS300-2021
    printed p. 61 (PDF p. 61). All three read from 300 dpi renders as well as the text
    layer. The parts lists name the adapter as item 229
  extracted_at: '2026-09-10'
---

| Row | Printed on all five |
|---|---|
| Input power | **12 VDC, 2.74 Amps** |
| External power supply | **Sinpro model # HPU32A-105, 30 watt power supply** |
| its input | 100-240V ~ : 50/60 Hz : 0.6-0.4A |
| its output | 12 VDC, 2.74 A |
| isolation | Input to output: **2MOPP** |

**The machine itself takes 12 volts DC.** The mains work is done by an external
brick, and the manual names the exact part - **Sinpro HPU32A-105** - which is
unusual: no other Spirit climber manual names its power supply by manufacturer
and model. The parts lists carry it as **item 229, `Power Adapter`** on the 7.0S
and 7.5S and **`Power adapter, 12vdc`** on the MS300, which also lists a
`Power adapter line cord` as item 230 and a `Dc power cable` as 225.

**2MOPP is a medical-safety rating** - two Means Of Patient Protection between
mains and output. It is the reason a generic 12 V 3 A adapter is not a
substitute, even where the voltage and current match. **Replace it with the named
part.**

## The 8.5S pair are mains-powered and take a fuse

The 8.5S and 8.5S-FIT have no external brick. They run from the mains directly -
100 to 240 Vac on one printing, a 120 V 15 A outlet on the other - behind a
250 V 5 A glass fuse. See `spirit-climber-85s-specs-mains-power-supply`. **Do not
order a Sinpro adapter for an 8.5S.**

## These three have no fuse a user can change

All five print **`Fuse rating / No user replaceable fuse`**. See
`spirit-climber-specs-fuse-rating`, which holds both halves of that question.

## The outlet and circuit are a safety question

What socket the brick goes into, and on what circuit, is answered on each book's
electrical safety page and belongs to the `safety` section, not here.
