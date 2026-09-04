---
id: f85-2021-ce-version
title: What is different about the CE version
kind: spec
question: What is the difference between the normal and CE versions of the Sole F85-2021
  ENT treadmill?
asked_as:
- difference between ce and normal treadmill
- why does my treadmill have a filter choke
- is my treadmill 110 or 230 volt
keywords:
- ce version
- filter choke
- 230 volt
- 110 volt
- european version
- circuit diagram
- power input
- export model
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2021-electrical-requirements
- f85-2021-grounding
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: Special Note on ST538 CE version, printed page 4
  extracted_at: '2026-09-04'
---

The platform ships in a normal version and a CE version. Quoting the manual:

> Besides normal version, ST535 treadmill is with a CE version. Both versions are with exactly the same in functions and outlines except that the power input is 110VAC for normal version versus 230VAC for CE version and an additional Filter Choke circuit is added for CE version as shown in the circuit diagram on next page.

| | Normal version | CE version |
|---|---|---|
| Power input | 110VAC | 230VAC |
| Filter choke circuit | no | yes |
| Functions and outlines | identical | identical |

**The heading and the sentence do not agree.** The heading reads "Special Note on **ST538** CE version" while the sentence under it describes the "**ST535** treadmill". ST535 is the platform code of the 2016 F85 manual, not of this one. The note appears to have been carried across from the older manual without the platform code being updated.

**The rest of the manual is not consistent with the voltages here either.** The safety and grounding sections call the machine a nominal **220 volt** product with a 10 amp outlet, and bracket the 120Vac system as 110 volt, 15 amp. Treat 220 and 230 as the same high voltage build when reading those pages.
