---
id: spirit-cycle-specs-resistance-systems
title: Four different resistance systems across the indoor cycles and air bikes - a
  leather brake pad, a permanent-magnet brake, a motor-driven magnetic brake and a
  fan
kind: spec
question: What kind of resistance does a Spirit indoor cycle or air bike use, and is
  it magnetic or friction?
asked_as:
- is the spirit indoor cycle magnetic or friction
- how does the resistance work on the spirit spin bike
- does the air bike have resistance levels
- what is the brake pad on my spirit cycle
keywords:
- resistance
- brake pad
- leather pad
- magnetic
- permanent magnet
- eddy current
- fan resistance
- air resistance
- tension knob
- resistance knob
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - ab900-2018
  - ab950-2024
  - cb900-2013
  - cic800-2021
  - cic850-2022
  - jb950-2022
  - xic600-2018
  - xic600-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- spirit-ce-specs-forty-resistance-levels
see_also:
- spirit-jb950-specs-twenty-motor-driven-resistance-levels
- spirit-cycle-specs-which-manuals-print-a-parts-list
- spirit-cycle-specs-no-specification-table
- spirit-bike-programs-air-bike-has-no-resistance-levels-because-the-fan-sets-the-load
source:
  ref: spirit-bike-cic800-2021-owners-manual
  locator: 'CIC800-2021 RESISTANCE ADJUSTMENT printed p. 17 and parts list printed
    pp. 24-26 items 87-92, 96, 102, 104, 106-108; CIC850-2022 printed p. 19 and parts
    list printed pp. 40-42 items 71, 73-75, 78-82, 96, 99; CB900-2013 Basic Operation
    printed p. 11 and care schedule printed p. 12; XIC600-2018 and XIC600-2021 Basic
    Operation printed p. 17 and care schedule printed p. 25; JB950-2022 INSTRUCTIONS
    printed p. 26 and BRAKE TEST printed p. 55; AB900-2018 INSTRUCTIONS printed p.
    25; AB950-2024 USING YOUR BIKE printed p. 14'
  extracted_at: '2026-09-09'
---

**These eight machines use four different resistance systems. Nothing carries
across from one group to another.**

| Machines | Resistance | What the rider turns or presses | How the bike is stopped |
|---|---|---|---|
| CB900-2013, XIC600-2018, XIC600-2021 | a **friction brake pad** against the flywheel | a **tension knob** - clockwise for more | press **down** on the tension knob |
| CIC800-2021, CIC850-2022 | **permanent magnets carried on moving brake blocks** | a **resistance knob** - clockwise (+) | press **down** on the resistance knob |
| JB950-2022 | a **motor-driven magnetic brake** with 20 numbered levels | **+ and – keys**, on the forward control pad or the handlebar shifters | the Push Brake System / Dynamic Braking handle |
| AB900-2018, AB950-2024 | **air**, from a fan-shaped flywheel | **nothing** - there is no knob and no key | pedal more slowly |

**None of the eight has a generator brake or an induction brake.** Those belong
to the commercial CR and CU bikes - see
`spirit-bike-specs-generator-brake-or-induction-brake`. Do not quote a
Generator/Brake or EMS Controller item number for any machine on this card.

## The friction machines wear a pad, so the pad is a service item

The CB900 and both XIC600 printings brake by pressing a pad onto the flywheel.
The care schedules name it: the XIC600 books say to **inspect for excessive wear
or a dry leather brake pad**, weekly, and warn against silicone-based lubricants;
the CB900 book says only **check for wear**, monthly. There is no level scale on
any of the three - the knob is continuous and nothing on the machine reads it
out.

## The CIC800 and CIC850 are magnetic, but neither manual ever says so

Both books describe only a knob: *turn the knob clockwise (+) to increase
resistance*, and *press directly DOWN on the resistance knob* to stop the
flywheel. **The word "magnetic" appears nowhere in either manual.** The mechanism
is visible only in the parts lists, and both list the same set of parts:

- **six permanent magnets** (CIC800 item 104, CIC850 item 71)
- a **brake block, left and right** (CIC800 items 106 and 107, CIC850 items 73
  and 74) and a **brake gasket assembly** (CIC800 108, CIC850 75)
- the knob linkage - a brake knob, brake rod, compression spring and, on the
  CIC850, a brake line and a brake line turntable

So a CIC800 or CIC850 is a **permanent-magnet bike with a mechanical knob**, not
a felt-pad bike and not an electronically controlled one. **The knob has no
numbered levels**, and the CIC850's console does not display a level.

Each list also carries a single further **permanent magnet** near the flywheel
axis - CIC800 item 37, CIC850 item 47. The manuals do not say what it does, and
only the CIC850 has a console and a sensor board to read one. Do not present a
purpose the source does not state.

## The air bikes have no resistance control at all

Both air bike manuals print the same paragraph: *There are no resistance knobs to
adjust as the resistance comes from the isokinetic resistance created by the
movement of air with the fan-shaped flywheel*, and control comes from *simply
varying the pace of pedaling and of the push / pull on the movement arms*. The
2018 book spells it **isokenetic** and the 2024 book **isokinetic**; the sentence
is otherwise the same.

There is therefore **no level, no knob, no watt rating and nothing to adjust or
replace** on an air bike's resistance. For what this means for the console modes,
see
`spirit-bike-programs-air-bike-has-no-resistance-levels-because-the-fan-sets-the-load`.

## The JB950 is the only one of the eight with numbered levels

Twenty of them, driven by a motor rather than a knob, with an encoder and home
and limit sensors that the Maintenance Mode can test. See
`spirit-jb950-specs-twenty-motor-driven-resistance-levels`. **Do not quote 40
levels** for any machine on this card - 40 belongs to the commercial bikes and
the commercial ellipticals, see `spirit-ce-specs-forty-resistance-levels`.

## No resistance figure is printed anywhere

None of the eight manuals states resistance in watts, newtons or kilograms, and
none prints a level-to-watts table. Where a console shows Watts it is reporting
the work the rider is doing, not a setting. See
`spirit-cycle-specs-no-specification-table`.
