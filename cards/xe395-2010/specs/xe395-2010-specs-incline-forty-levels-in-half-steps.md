---
id: xe395-2010-specs-incline-forty-levels-in-half-steps
title: The powered ramp has 40 incline levels, in half-level steps from 0 to 20
kind: spec
question: How many incline levels does a Spirit XE395 elliptical have, how big is
  each step, and what numbers does the readout run between?
asked_as:
- how high does the incline go on this elliptical
- how many incline levels are there
- what is the max ramp setting
- incline range on the xe395
keywords:
- incline levels
- incline range
- power incline
- ramp
- elevation
- half level
- increments
- maximum incline
- incline keys
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe395-2010
  - xe395-2016
  - xe395-2018
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-specs-which-machines-have-a-power-incline
- spirit-ce850-specs-stride-length-18-to-24-inches
see_also:
- spirit-ce850-specs-twenty-resistance-levels
- spirit-xe-specs-no-specification-table
- xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed
- xe395-2016-console-data-ranges-incline-0-to-20-in-half-steps-and-level-0-to-20
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
source:
  ref: spirit-elliptical-xe395-2010-owners-manual
  locator: 'p. 15, Console, POWER INCLINE; the 2010 book bands the same scale on p.
    16, Muscle Activation Figure, and the XE395-2018 printing carries that banding
    at p. 19 while omitting the POWER INCLINE paragraph entirely. XE395-2016 service
    manual: Function page PDF p. 18 (text.md lines 328-363) and Keys page PDF p. 22
    (420-446) print 0 to 20 in 0.5 steps; the incline-motor test on PDF p. 50 (828-864)
    prints 15 for max incline. XE395ENT-2021 service manual PDF p. 35 (461-497) prints
    20 for max incline'
  extracted_at: '2026-09-09'
---

**40 incline levels, in increments of 0.5, numbered 0 to 20.** The 2010 manual's
sentence is: "There are 40 (in increments of .5) different incline levels that can
be adjusted by pressing the Incline ^ or v buttons on the left swing arm."

The incline keys are **on the left swing arm**, not on the console face.

**Both XE395 printings band the scale 0 to 20 with a half level in the middle.**
The Muscle Activation Figure paragraph divides the range into "Levels 0-7.5
Incline" and "Levels 8-20 Incline", which is where the endpoints come from: 40
steps of 0.5 span 0 to 20, and 7.5 is one of them. The 2010 and 2018 books print
that banding word for word.

## The 2018 printing drops the count but keeps the scale

**The XE395-2018 owner's manual never prints the "40 (in increments of .5)"
sentence.** It has no POWER INCLINE paragraph at all - the words *increments*,
*motorized* and *uphill* do not appear anywhere in the book, and this was checked
against the PDF page by page, not only against the extracted text. What it does
keep is the 0-7.5 / 8-20 banding, and an assembly step that tells you to "elevate
the incline to level 8", so its scale is the same one.

Answer an XE395-2018 with 40 half levels only alongside that qualification: **the
figure is carried over from the 2010 book of the same model and corroborated by the
2018 book's own banding, not stated outright in the 2018 book.**

## The 2016 service manual prints the same scale, and one page contradicts it

The XE395-2016 service manual's Function page reads *Incline - Display the incline
position from 0 to 20. INCLINE preset value is 0 to 20. Press UP or DOWN to adjust
incline, each increment and decrement is 0.5*, and its Keys page repeats *the maximum
incline position is 20 ... the minimum incline position is 0*: **0 to 20 in half
steps, forty positions**, the owner's-manual figure stated outright for the 2016
machine. The incline motor behind it is
`spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor`.

The same book's incline-motor test page then says the INCLINE window, once speed
calibration ends, shows the sensor counter with **"15 for max incline, 0 for lowest
incline"**. That 15 disagrees with the 20 printed three times elsewhere in the book,
and the XE395ENT-2021 service manual's copy of the identical sentence reads **"20 for
max incline"** - so read the 15 as a slip carried from an older test text, not as a
different range (`xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`,
`xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`).

**This figure is for the XE395-2010, XE395-2016 and XE395-2018 only.** The XE395ENT-2021
and the XE395-2023 also have a powered ramp, and **neither of their owner's manuals
states a range** - not in levels, degrees or percent; the XE395ENT service manual
gives only the 0-20 counter on its test page and no step. Quoting 40 for either of them would be an invention: they run
different consoles, and the XE395-2023's direct-select button strip is printed as a
picture whose digits cannot be read reliably. See
`spirit-xe-specs-which-machines-have-a-power-incline`.

**The book gives no angle and no rise.** It states no degrees, no percent grade and
no height in inches for either end of the ramp, and no specification table anywhere
supplies them.

**These are incline levels, not resistance levels.** The same machine also has 20
resistance levels, set with a separate pair of Level keys - a different control and
a different number. Both printings state the 20 - see
`spirit-ce850-specs-twenty-resistance-levels`.

**Nor is this a stride adjustment.** The XE895-2018 is the one residential machine
in the family with a powered stride, and it has no incline at all - see
`xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed`.
