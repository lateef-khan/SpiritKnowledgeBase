---
id: xterra-specs-resistance-level-count-not-printed
title: The number of resistance levels is not printed
kind: fact
question: How many resistance levels does an Xterra FB folding bike, SB150, SB240,
  SB250, SB4.5r or SB500 bike, EU150 hybrid, or FS150, FS5.8e or FS5.9e elliptical
  have?
asked_as:
- how many resistance levels does the fb150 have
- sb250 resistance range
- fs150 number of levels
- sb500 max resistance level
keywords:
- resistance levels
- level count
- not printed
- tension knob
- max level
- default level
- level 20
- absence
facets:
  brand:
  - xterra
  product_line: '*'
  model: '*'
  applies_to:
  - eu150-2024
  - fb150-2021
  - fb160-2019
  - fb180-2025
  - fb350-2021
  - fb360-2019
  - fs150-2016
  - fs58e-2013
  - fs59e-2014
  - sb150-2018
  - sb240-2023
  - sb250-2024
  - sb45r-2013
  - sb500-2020
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-specs-resistance-has-24-levels
- xterra-specs-resistance-has-16-levels
- xterra-specs-manual-tension-knob-with-8-levels
- xterra-specs-resistance-set-from-the-console-by-a-gear-motor-on-a-magnetic-brake
source:
  ref: xterra-bike-sb500-2020-owners-manual
  locator: 'SB500 OM Engineering Mode ''Safety - Off; when turned on the machine automatically
    goes to Level 20 of Resistance'', PDF p. 22 (printed 20), text.md lines 815-816;
    Manual program ''level one'', p. 16 line 541. SB4.5r (scan) p. 22 OCR lines 925-926;
    FS5.9e (scan) p. 26 OCR, same sentence; FS5.8e (scan): the engineering-mode page
    is absent, the book ends at PDF p. 24 with the RPE page. SB150 ''The default resistance
    level is 3'', p. 18 (printed 16) lines 526-528; SB250 p. 17 lines 533-535; FS150
    (scan) p. 18 OCR lines 593-595; EU150 ''The default resistance level is 7'', p.
    20 (printed 17) lines 529-531; SB240 Manual p. 26 (printed 25) lines 820-824.
    FB160 parts list item 47 ''Tension knob'', p. 15 line 530; FB360 item 47, p. 17
    line 664; FB150 p. 5 and FB350 p. 5 checklists and FB180 p. 16 exploded view name
    no knob. A grep of all fourteen books for ''levels of'', ''level range'', ''1-'',
    ''to 20'', ''to 24'' and ''Max Level'' finds no count'
  extracted_at: '2026-09-11'
---

**None of these fourteen books prints how many resistance levels the machine has.** What each prints instead:

| Machine | What the book says about levels |
|---|---|
| FB150, FB350, FB180 | nothing - no resistance adjustment is named anywhere in the book |
| FB160, FB360 | parts list item 47 "Tension knob"; no levels, no adjustment paragraph |
| SB150, SB250, FS150 | "The default resistance level is 3" in the Manual program, "load 1" in the user programs |
| EU150 | "The default resistance level is 7" |
| SB240 | "adjust their workout to the desired resistance level (press UP/DOWN keys)"; no count |
| SB500, SB4.5r, FS5.9e | the manual program starts at "level one"; preset programs ask for a "Max Level"; the engineering-mode Safety lock "automatically goes to Level 20 of Resistance", which implies at least twenty levels without stating a range |
| FS5.8e | the manual program starts at "level one for both Incline and Resistance" and asks for a Max Level; the scan ends before the engineering-mode page |

Treat "Level 20" as a hint, not a specification: it is the level the child lock parks the brake at, and the book
never says it is the top. The SB2.5r, SB4500, FS2.5, FS3.5 and RSX1500 books do print a count (24), the FS1.5 and
SB600 print 16, and the EU100, SB120 and UB120 knobs are marked 1 to 8.

