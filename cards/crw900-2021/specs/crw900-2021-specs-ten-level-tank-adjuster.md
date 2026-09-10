---
id: crw900-2021-specs-ten-level-tank-adjuster
title: A ten-position tank adjuster that moves water between a storage and an active
  chamber, in a tank holding at most 20 litres
kind: spec
question: How is the resistance set on a Spirit crw900-2021 water rower, and how many
  levels does it have?
asked_as:
- how many resistance levels does the crw900 have
- how do i make my spirit water rower harder
- how much water goes in the crw900 tank
- why does my water rower take so long to get easier
keywords:
- resistance
- water level
- adjuster knob
- tank
- ten levels
- storage chamber
- active chamber
- 20 litres
- paddle
- flywheel
facets:
  brand:
  - spirit
  product_line: rower
  model: crw900-2021
  applies_to:
  - crw900-2021
  section: specs
  code: '*'
  model_number: '900948'
authority: 3
not_to_be_confused_with:
- crw800h2o-specs-six-water-fill-levels
- crw800-2024-specs-level-range-1-to-16
- crw800h2o-console-water-level-button-six-steps
see_also:
- spirit-rower-specs-which-manuals-print-a-parts-list
- crw900-2021-maintenance-tank-filling-and-initial-water-treatment
- crw900-2021-errors-vr-setting-for-trouble-with-resistance
- spirit-crw800-specs-no-specification-table
source:
  ref: spirit-rower-crw900-2021-owners-manual
  locator: OPERATION INSTRUCTIONS printed p. 32 (PDF p. 32); TANK FILLING & WATER TREATMENT
    PROCEDURES printed p. 33 (PDF p. 33); REMOVING / CHANGING TANK WATER printed p.
    34 (PDF p. 34); EXPLODED VIEWS Assembly Overview printed p. 55 and the tank sheet
    printed p. 57
  extracted_at: '2026-09-10'
---

**Ten levels, set by a knob on the tank, not by the console.**

The machine has **no brake and no console resistance key**. Resistance is how much
water reaches the paddle, and an **Adjustment Knob, item [32]**, moves water
between the tank's two chambers:

> **1** : This setting keeps a portion of the water in reserve creating light
> resistance.
> **10** : This setting allows the maximum amount of water to reach the flywheel.

The exploded view names the whole unit **`A1078 - 10 Level Tank Complete
Assembly`** and marks it **`Not Sold Separately`** - so the level count is a
property of the tank, and the tank is not a spare part.

## The change is not symmetrical, and this is what customers report as a fault

> Your rower will adapt almost instantly to increases in resistance but will take
> **up to 10 strokes** to reduce the effort required, as the central "storage"
> tank fills up.

**Harder is immediate; easier takes ten strokes.** A caller who says the knob
"only works one way" is describing normal behaviour. Setting `MIN` also takes ten
strokes to fill the storage chamber, and the manual says that step "is always
required if minimum resistance is desired."

The adjustment can be made **while rowing** - the manual calls it changing "on the
fly".

## The tank holds 20 litres and the knob must be at 10 to fill it

> Resistance adjuster must be set to **"10"** to allow for accurate filling
> capacity. Do not overfill the tank beyond the maximum indicated level of
> **20 litres**. Refer to the tank level decal on the tank.

**To drain, the knob goes to "1"** and the user rows at least ten strokes first, to
push as much water as possible into the storage reservoir. Even then
**approximately 40% of the tank water will remain** - the manual says the tank
cannot be completely drained without disassembly. Water treatment and refilling
are `maintenance` questions -
`crw900-2021-maintenance-tank-filling-and-initial-water-treatment` and
`crw900-2021-maintenance-removing-and-changing-tank-water`.

## The console reads the level, it does not set it

The console display shows a **"Resistance value ... based on current water
level"**, and the 7-segment window shows the level "according to VR" - a variable
resistor on the tank adjuster. **There is no LEVEL key on this console**; that key
position is the Bluetooth button. If the displayed level does not follow the knob,
that is the VR setting and it is a fault, not a setup step - see
`crw900-2021-errors-vr-setting-for-trouble-with-resistance`.

## Two cross-references in this chapter are wrong

Step 5 of the draining procedure says to follow the Resistance Level Display guide
"in the Console set up page **(pg 53)**". **Printed p. 53 is the troubleshooting
table.** The console setup page is printed p. 46. The same two pages also carry
stray `P.28` and `P.29` markers in the margin, left over from the OEM book this
chapter was rebadged from.

The water-treatment paragraph on printed p. 34 refers to "Water Treatment Tablets
**[32]**" while [32] is the Adjuster Knob; the tablets are item **[16]** on the
facing page. **The manual uses [32] for two different parts.** Quote the item
number from the page that describes the part, not from the paragraph that mentions
it.

## Not the other Spirit water rower and not an air rower

The **CRW800H2O** is a different water rower with **six fill levels and no
adjuster knob at all** - you change its resistance by how much water you pour in.
See `crw800h2o-specs-six-water-fill-levels`. The **CRW800 and XRW600** air rowers
run a console scale of **1 to 16** against a fan and a motorised brake - see
`crw800-2024-specs-level-range-1-to-16`. **Three Spirit rowers, three scales, and
none of them converts into another.**

**No watt figure, no drag factor and no level-to-watts table is printed anywhere in
this book.** The Watts window reports the work the rower is doing, not the setting.
