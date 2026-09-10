---
id: crw800-2024-specs-level-range-1-to-16
title: The rower has 16 resistance levels, shown as eight dots that each stand for
  two levels
kind: spec
question: How many resistance levels does a Spirit air rower have?
asked_as:
- how many resistance levels on the spirit rower
- what is the highest level on the rowing machine
- resistance range on the spirit rower
- why do the level dots only go up in twos
keywords:
- resistance levels
- level range
- workload
- intensity
- level up
- level down
- maximum level
- difficulty
- dots
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2021
  - crw800-2024
  - xrw600-2019
  - xrw600-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce-specs-forty-resistance-levels
- spirit-ce850-specs-twenty-resistance-levels
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- crw800h2o-specs-six-water-fill-levels
- crw900-2021-specs-ten-level-tank-adjuster
- 85ue-2025-specs-eddy-current-brake-and-fifty-levels
see_also:
- crw800-2024-specs-resistance-system
- spirit-crw800-specs-no-specification-table
- crw800-2024-console-window-functions
- spirit-xrw600-specs-resistance-mechanism-never-named
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: 'Features - Window Functions, printed p. 14 (PDF p. 16), the LEVEL bullets:
    "The Level window shows the current resistance level", "The level range is 1~16",
    "Level 1 and 2 would light the first dot, level 3 and 4 would light the second
    dot, etc." The same three bullets are printed on CRW800-2021 printed p. 14 (PDF
    p. 16) under the heading LEVEL, and on XRW600-2019 and XRW600-2021 printed p. 16
    (PDF p. 16) under the heading Level - word for word on all four'
  extracted_at: '2026-09-10'
---

**16 levels, on all four Spirit air rowers.** Level 1 is the easiest. Each manual
states the range once, in the LEVEL bullet of the window-functions list on printed
p. 14 of the CRW800 books and printed p. 16 of the XRW600 books:

> The Level window shows the current resistance level. The level range is 1~16.
> Level 1 and 2 would light the first dot, level 3 and 4 would light the second
> dot, etc.

**Eight dots cover sixteen levels, two levels per dot.** A customer who says the
display "only moves every other press" is describing that, not a fault: the
number in the Level window changes on every press, the dot changes on every
second one.

**This is the only place the book gives a level count.** There is no paragraph of
the "There are N levels of resistance available for plenty of variety" kind that
the Spirit ellipticals, bikes and steppers print, and no band description - the
book never says which levels are easy and which are hard.

**Do not answer this machine with 20 or 40.** The Spirit ellipticals and
commercial bikes run to 40 or to 20 on a different console with a different brake
- see `spirit-ce-specs-forty-resistance-levels` and
`spirit-ce850-specs-twenty-resistance-levels` - and the CSC900 stair climber's 20
run the other way round. Sixteen is this machine's own number.

**These are console levels, not a physical rating.** The manual states no
resistance figure in watts, newtons or kilograms and prints no level-to-watts
table; the Watts window reports the work the rower is doing, not the setting. The
level is carried out by a gear motor moving a brake against the fan-and-flywheel
unit - see `crw800-2024-specs-resistance-system`.

**The other five ranges in the same bullet list are console facts, not machine
facts.** Calories 0~999, Watts 0~2000, Time 00:00~99:59, Distance 0~9999 and
heart rate 40~220 bpm are what the display can show. Only the level range says
anything about the rower.

## Four books, one bullet list, and the XRW600 half of it is unexplained

The CRW800-2021, CRW800-2024, XRW600-2019 and XRW600-2021 print these three
bullets **word for word**, so the scale is one fact and this is one card. **The
mechanism behind it is not one fact.** The CRW800's parts list shows what the
sixteen levels move - a gear motor and a generator/brake controller against a fan
and flywheel (`crw800-2024-specs-resistance-system`) - and **the XRW600 books
print no parts list and never name their mechanism at all**
(`spirit-xrw600-specs-resistance-mechanism-never-named`). Answer an XRW600 owner's
"how many levels" from this card and their "what kind of resistance" from that
one.

**The window-function list this bullet sits in is a `console` card**, not this one:
`crw800-2024-console-window-functions` holds all seven windows and their ranges for
the same four machines. This card is the level range on its own, because that is
the figure customers ask for by name.

## The two water rowers do not have console levels at all

`crw800h2o` is set by **how much water you pour in, on a six-step gauge**
(`crw800h2o-specs-six-water-fill-levels`), and `crw900-2021` by a **ten-position
knob on the tank** (`crw900-2021-specs-ten-level-tank-adjuster`). Neither scale
converts into this one. The 8.5UE upper body ergometer runs to **50**
(`85ue-2025-specs-eddy-current-brake-and-fifty-levels`).
