---
id: spirit-climber-specs-no-level-count-printed
title: Two climber manuals give Level Up and Level Down keys and never say how many
  levels there are
kind: fact
question: How many resistance levels does a Spirit CVC800 vertical climber or CSC880
  stair climber have?
asked_as:
- how many levels on the cvc800
- what is the top level on the vertical climber
- how many resistance levels does the csc880 have
- highest setting on the stair climber
keywords:
- resistance levels
- level range
- how many levels
- maximum level
- top level
- level up
- level down
- workload
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - csc880-2025
  - cvc800
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-specs-twenty-resistance-levels
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- spirit-climber-specs-isokinetic-twenty-levels
see_also:
- spirit-climber-specs-no-specification-table
- spirit-climber-2024-specs-resistance-system
- csc880-2025-specs-exploded-view-with-no-parts-list
source:
  ref: spirit-climber-cvc800-2021-owners-manual
  locator: Whole document, including the console chapter printed pp. 12-16 (PDF pp.
    14-18) and the CVC800 service manual; and the CSC880-2025 owner's manual whole
    document, including Features printed pp. 17-19 and Console Screen - Overview printed
    p. 20 (PDF pp. 19-22). Both books' console pages were rendered at 300 dpi and read
    with `tesseract --psm 4` as well as extracted
  extracted_at: '2026-09-10'
---

**Neither manual ever states a level count.** Both machines have Level Up and
Level Down keys, both have a resistance level display window, and neither book
says what the top of the scale is.

- The **CVC800-2021 Vertical Climber** owner's manual describes Quick Start as
  "the workload/resistance may be adjusted manually", says a program "will start
  at level 1 to warm up", and never gives a maximum. **The CVC800 service manual
  does not state one either** - it says only "Press these keys can adjust the
  resistance level" and "use the console to set resistance level to max".
- The **CSC880-2025 stair climber** owner's manual has a Features chapter, a
  Console Screen overview that labels a "Resistance level display window", and a
  PAUSE description that restarts the staircase "at resistance level one". It
  never says how many levels follow level one.

**Say the manual does not state it**, and get the figure from Spirit Fitness.

## Do not fill the gap from a neighbouring machine

Every plausible source of a number here is the wrong machine:

| Tempting answer | Why it is wrong |
|---|---|
| 20, from the CS800 or CRS800S | different machines; the CVC800 is a vertical climber and the CSC880 a stair climber |
| 20, from the CSC900 | the CSC900 is a different stair climber, and **its twenty run backwards** - a higher level brakes less. Assuming the CSC880 inherited that is a second guess on top of the first |
| 20 or 50, from a rehabilitation stepper | a different platform entirely |

The CSC880 is the successor to the CSC900 in the range, and it is exactly the
machine a reader will answer from the CSC900's card. **Do not.** See
`spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top`, which says the
same thing from the other side.

## The absence was checked against renders, not just the extraction

Both books' console and features pages were rendered at 300 dpi and read with
`tesseract --psm 4`. The CSC880's Console Screen overview page is largely a
picture - 34 native words against 162 in the render - and **the render adds no
level count**; it adds the callout labels around the console drawing, one of
which is "Resistance level display window". The CVC800's console pages extract
and render to within a few words of each other throughout.

A loose search of both whole documents for the word *level* returns only levelling
feet, "flat level surface", the Level Up and Level Down keys, and "resistance
level one". **There is no count to find.**

## Neither book prints a specification page either

So there is no second place to look. See
`spirit-climber-specs-no-specification-table`.
