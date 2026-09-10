---
id: spirit-jb950-specs-twenty-motor-driven-resistance-levels
title: Twenty motor-driven resistance levels, adjusted from a forward control pad or
  the handlebar shifters
kind: spec
question: How many resistance levels does a Spirit jb950-2022 Johnny G Spirit Bike
  have, and how are they changed?
asked_as:
- how many levels does the johnny g bike have
- what is the highest resistance on the jb950
- where are the resistance buttons on the johnny g spirit bike
- does the johnny g bike have a resistance knob
keywords:
- resistance levels
- level range
- twenty levels
- l-20
- shifters
- control pad
- magnetic resistance
- brake motor
- intensity
- workload
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: specs
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-ce-specs-forty-resistance-levels
- spirit-ce850-specs-twenty-resistance-levels
see_also:
- spirit-cycle-specs-resistance-systems
- spirit-cycle-specs-console-display-type
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: 'INSTRUCTIONS printed p. 26; MAINTENANCE MODE - BRAKE TEST printed p. 55;
    KEY TEST printed p. 53; WARM UP MODE printed p. 34'
  extracted_at: '2026-09-09'
---

**Twenty levels, L-1 to L-20.** The resistance is magnetic and moved by a motor,
not by a knob.

The count is printed in one place only, on the **BRAKE TEST** page of Maintenance
Mode: the test displays `LEVEL TO 20` and then *auto-runs the motor in a loop
from L-1 to L-20 and back to L-1*. **The riding chapter never states a level
count**, so if a customer asks where it says twenty, that is the page.

## Where the rider changes level

There are **two + / – key positions**, and the manual says both were provided
deliberately:

- the **Forward Control Pad**, for when the rider is in the saddle with hands in
  home position;
- the **Handlebar Shifters** at the handlebar ends, for riding out of the saddle
  through a climb.

The Key Test page counts **five buttons in total** - a + key, a – key and a Play
key on the forward control pad, plus a right-side + key and a left-side – key on
the handlebar ends. The current level shows on the console as **LEVEL**, in the
top-left field of the home screen.

## What the level actually drives

A motor moves a magnetic brake. Maintenance Mode can drive it by hand
(MOTOR TEST MANUAL) and reports an **encoder count** together with a limit-sensor
condition of `1 = HOME`, `2 = ACTIVE RANGE` or `3 = END`, and a separate LIMIT
SENSOR test checks the flag travelling between the home sensor (S1) and the limit
sensor (S2). **These are service tests, not a rider setting** - see the `console`
section for how to enter Maintenance Mode.

## Twenty here is not the twenty on an elliptical, and it is not forty

- **`spirit-ce850-specs-twenty-resistance-levels`** also says twenty, but that is
  a Spirit **elliptical**, with a band description this manual does not print.
  Answering a Johnny G question from it gives the customer the wrong machine.
- **`spirit-ce-specs-forty-resistance-levels`** gives **40** for the Spirit
  commercial CR and CU bikes and commercial ellipticals. **Do not quote 40 for a
  JB950.**
- No other machine in the indoor cycle and air bike group has numbered levels at
  all - see `spirit-cycle-specs-resistance-systems`.

The manual states no watt value for any level, and prints no level-to-watts
table. The default FTP figure the console offers, 150 W, is a rider fitness
setting and not a resistance rating.
