---
id: 70t-2026-specs-emc-declaration
title: The electromagnetic compatibility declaration, and the recommended RF separation
  distances
kind: spec
question: What are the EMC test levels and the recommended RF separation distances
  for a Spirit 70t-2026, 70t-2025, mt200-2010 or mt200-2022 rehabilitation treadmill?
asked_as:
- how far should a phone be from the treadmill
- is this treadmill emc tested
- will wifi interfere with the display
- emc declaration for the 7.0t
keywords:
- emc
- electromagnetic compatibility
- cispr 11
- iec 61000-4-2
- iec 61000-4-3
- iec 61000-4-4
- separation distance
- rf immunity
- interference
- esd
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2025
  - 70t-2026
  - mt200-2010
  - mt200-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- 70t-2026-specs-certifications
- spirit-2026t-safety-intended-conditions-of-use
- mt200-2010-specs-certifications-and-classification
- mt200-2022-specs-certifications-and-classification
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'SPECIFICATIONS - CONTINUED p. 48 of the 2026 7.0T manual; the same four
    tables are printed as text in both MT200 manuals - "Guidance and manufacturer''s
    declaration - electromagnetic compatibility", printed pages 43-44 of the 2010
    manual and 68-70 of the 2022 manual. 7.0T-2025 (spirit-treadmill-70t-2025-owners-manual):
    SPECIFICATIONS - CONTINUED, PDF p. 50 (printed 48), text.md lines 1524-1544, a
    flat image checked on a render - the same four tables'
  extracted_at: '2026-09-09'
---

**Three manuals print these four tables and they agree row for row** - the 2026
7.0T, the MT200 manual of 2010 and the MT200 manual of 2022, with only the model
name changed. On the 7.0T the whole page is a flattened image in that PDF - a
text extraction returns only the Note bullets at the bottom right - and the four
tables below were read off the rendered page; both MT200 manuals print them as
text and confirm every figure. **The manuals write decimals with a comma**
(0,12 m; 2,5 GHz); that is kept here rather than converted.

**Guidance and manufacturer's declaration - electromagnetic compatibility.** The
machine is intended for use in the electromagnetic environment specified below.
The customer or the user should assure that it is used in such an environment.
Each manual prints its own model name where "the machine" stands here.

| Emissions test | Compliance | Electromagnetic environment - guidance |
|---|---|---|
| RF emissions CISPR 11 | Group 1 | The machine uses RF energy only for its internal function. Therefore, its RF emissions are very low and are not likely to cause any interference in nearby electronic equipment. |
| RF emissions CISPR 11 | Class B | The machine is suitable for use in all establishments, including domestic establishments |

| Immunity test | IEC 60601 test level | Compliance level | Electromagnetic environment - guidance |
|---|---|---|---|
| Electrostatic discharge (ESD) IEC 61000-4-2 | 6 kV contact, 8 kV air | 6 kV contact, 8 kV air | Floors should be wood, concrete or ceramic tile. If floors are covered with synthetic material, the relative humidity should be at least 30 %. |
| Power frequency (50/60 Hz) magnetic field IEC 61000-4-8 | 3 A/m | 3 A/m | Power frequency magnetic fields should be at levels characteristic of a typical location in a typical commercial or hospital environment. |
| Radiated RF IEC 61000-4-3 | 3 V/m, 80 MHz to 2,5 GHz | 3 V/m | d = 1,2 sqrt(P) for 80 MHz to 800 MHz; d = 2,3 sqrt(P) for 800 MHz to 2,5 GHz. Field strengths from fixed RF transmitters, as determined by an electromagnetic site survey, should be less than the compliance level in each frequency range. Interference may occur in the vicinity of equipment marked with the RF symbol. |
| Electrical fast transient/burst IEC 61000-4-4 | +/-2 kV for power supply lines, +/-1 kV for input/output lines | +/-2 kV for power supply lines, +/-1 kV for input/output lines | Mains power quality should be that of a typical commercial or hospital environment. |

**The ESD row's polarity sign is a missing glyph on the printed page of all
three manuals.** Where a plus-or-minus sign belongs the page shows an empty box, so it reads as a bare
"6 kV contact" and "8 kV air". The figures are exact; only the sign in front of
them is unreadable in the source, and it has not been guessed at here.

**Recommended separation distances between portable and mobile RF communications
equipment and the machine**, in metres:

| Rated maximum output power of transmitter, W | 150 kHz to 80 MHz, d = 1,2 sqrt(P) | 80 MHz to 800 MHz, d = 1,2 sqrt(P) | 800 MHz to 2,5 GHz, d = 2,3 sqrt(P) |
|---|---|---|---|
| 0,01 | 0,12 | 0,12 | 0,23 |
| 0,1 | 0,38 | 0,38 | 0,73 |
| 1 | 1,2 | 1,2 | 2,3 |
| 10 | 3,8 | 3,8 | 7,3 |
| 100 | 12 | 12 | 23 |

For transmitters rated at a maximum output power not listed above, the
recommended separation distance d in metres can be estimated using the equation
applicable to the frequency of the transmitter, where P is the maximum output
power rating of the transmitter in watts according to the transmitter
manufacturer. NOTE 1 At 80 MHz and 800 MHz, the separation distance for the
higher frequency range applies. NOTE 2 These guidelines may not apply in all
situations. Electromagnetic propagation is affected by absorption and reflection
from structures, objects and people.

**The page's own note.** If the device is interfered with by a power or signal
cable, image quality may be reduced or abnormally displayed; such interference
images are easily identified and differentiated from the physiological
characteristics of the patient, and cost clinical time but no diagnostic
accuracy. If there is a certain frequency of image interference, the RF signal
needs isolating or filtering.

**Where the three books stop agreeing.** The closing Note about cable
interference and image quality is printed in the 7.0T manual and in the 2022
MT200 manual, whose conversion drops several words mid-sentence; **the 2010
MT200 manual ends at the fast-transient table and prints no such Note.**
Everything above it is common to all three. The wording of the Note above is the
7.0T's, which is the only complete copy.

**The 8.0T manual prints no EMC declaration at all** - its Specifications -
Continued page is the battery page instead. Do not answer an 8.0T EMC question
from this table.

The 2025 7.0T owner's manual prints the same page, likewise as one flat image with only the Note bullets in its text layer.

