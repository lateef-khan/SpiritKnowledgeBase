---
id: spirit-ce-safety-no-mains-outlet-needed
title: The elliptical has a built-in generator and needs no mains outlet at all
kind: fact
question: What outlet, voltage and amperage does a self-powered Spirit CE800 or CE900
  commercial elliptical need (ce800-2016, ce800-2021 or ce900-2021)?
asked_as:
- does the ce800 elliptical need to be plugged in
- what outlet does the commercial elliptical need
- there is no power cord on my elliptical
- what voltage does the spirit ce900 run on
keywords:
- outlet
- power cord
- plug
- voltage
- amperage
- built-in generator
- self powered
- no plug
- mains
- pedal to power up
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce800-2016
  - ce800-2021
  - ce900-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-safety-outlet-and-circuit-requirement
- spirit-xe-safety-outlet-115-volt-15-amp
- spirit-xe-safety-no-outlet-figure-printed
- ce1000ent-2023-safety-mains-powered-through-a-100-w-adapter
- xe795-2023-safety-outlet-220-volt-15-amp
see_also:
- spirit-ce-safety-generator-produces-ac-power
- spirit-bike-safety-no-mains-outlet-needed
- spirit-xe795-console-power-up-by-pedalling
- spirit-ce800-safety-instructions-list
- spirit-ce900-safety-instructions-list
- spirit-ce-safety-serial-number-location
- xt-2015-safety-no-user-weight-limit-printed
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: 'CE800 (2020) service manual: 4-2-1 POWER, PDF p. 14 (printed 13); text.md
    lines 231-236; 3 Electrical Configurations, PDF p. 11 (printed 10), lines 170-189.
    CE900 (SE8800-SE026) service manual: Operation / POWER, PDF p. 14 (printed 14),
    lines 209-214; the Stop-key paragraph PDF p. 15 (printed 15), lines 253-258; 3
    Electrical Configurations, PDF p. 11 (printed 11), lines 177-190; 2 Component
    Description item 19 Power Switch Cover, PDF p. 34, lines 568-612. CE800-2016 (XE890B-AE10M)
    service manual: 3 Electrical Configurations, PDF p. 10 (printed 10), lines 173-189;
    Driver Board Wire Connections GENERATOR POWER, PDF pp. 25-26, lines 423-471; the
    matrix row `Generator Power to console too low`, PDF p. 32, lines 549-551. The
    absences are the whole of each book, native text and OCR supplements: CE800 (2020)
    52 PDF pages, lines 1-1117; CE900 61 pages, lines 1-1479; CE800-2016 65 pages,
    lines 1-1309.'
  extracted_at: '2026-09-11'
---

**These three service manuals describe a self-powered machine: there is no power cord, no outlet
requirement, no voltage figure and no amperage figure, because the console runs off a generator the
pedals drive.**

> CE800 elliptical trainers have a built-in generator for power and do not need to be plugged into an
> AC outlet. To power up the elliptical trainer simply start to pedal, the console will turn on
> automatically.

The CE800 (2020) service manual prints that under 4-2-1 POWER; the CE900 (SE8800-SE026) service manual
prints the same paragraph with `Spirit Fitness commercial elliptical trainers` as its subject. Both go
on: the console self-tests for a few seconds, the display may stay dark until you keep pedalling, and
then the start-up message scrolls.

- **The rider is the power supply.** Both books' Electrical Configurations page says the main
  controller `consist[s] of the generator power supply for console`, and the CE900 book's Stop-key
  paragraph adds that `when you stop pedaling without AC power the display will turn off but the
  memory will be saved for 5 minutes`.
- **No Product Safety Instructions chapter at all.** None of the three books has the chapter 7 that
  the plug-in ellipticals carry: no outlet bullet, no extension-cord gauge, no GFCI rule, no breaker
  paragraph, no grounding page. The words *outlet* and *volt* appear only in the sentences quoted
  here and on the driver-board labels; *GFCI*, *AWG*, *ground* (as a mains term) and *amp* appear
  nowhere. That is an absence, not a figure of zero.
- **The CE800-2016 book (titled XE890B-AE10M) prints no POWER paragraph**, but its Electrical
  Configurations page says the same thing in fewer words - `Main controller Include power
  supply(generator power)` - and its driver-board pages label the feed `GENERATOR POWER`. Its
  troubleshooting matrix treats a dim display as `Generator Power to console too low` and sends the
  technician to the generator connection, never to a wall socket.

**The generator is still a live AC source while the flywheel turns.** The owner's manuals print a
shock warning about that; these service manuals print none, and none states a wait time before
touching the machine (`spirit-ce-safety-generator-produces-ac-power`). Stopping the flywheel and
letting it come to rest is the safe state, not pulling a plug there is none of.

**A `Power Switch Cover` is nevertheless in the CE900 parts list** (item 19 of its Component
Description) and the same book's replacement guide has a 6.5 Power Cover Replacement step. The
manual never says what sits under that cover, and nothing else in the book gives the machine a
mains inlet; do not read the part name as a plug.

**Not every Spirit elliptical is self-powered**, and the service manuals split the range the same
way the owner's manuals do:

| Machine | Power | Card |
|---|---|---|
| CE850-2016, CE850-2020 | 115-volt, 15-amp grounded outlet in the service manual | `spirit-xe-safety-outlet-115-volt-15-amp` |
| CE900ENT | plugs in through an FSP100-RTAAN2 adapter; no outlet figure printed | `spirit-xe-safety-no-outlet-figure-printed` |
| CE1000ENT-2023 | plugs in through a 100 W adapter on a diagram titled 230V | `ce1000ent-2023-safety-mains-powered-through-a-100-w-adapter` |
| XE795-2016, XE795-2023 | hybrid generator, and the book prints an outlet chapter anyway | `spirit-xe-safety-outlet-115-volt-15-amp`, `xe795-2023-safety-outlet-220-volt-15-amp` |

The dividing line is the console. The touchscreen ENT machines and the plug-in CE850 draw mains
power; the LED-console CE800 and CE900 do not. The commercial bikes divide the same way
(`spirit-bike-safety-no-mains-outlet-needed`).

