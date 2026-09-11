---
id: spirit-med-bike-specs-emc-declaration
title: The electromagnetic compatibility declaration and the recommended RF separation
  distances, printed as text in the Dyaco edition and as a picture in the Spirit ones
kind: spec
question: What are the EMC test levels and the recommended RF separation distances
  for a Spirit Medical 7.0R or 7.0U bike?
asked_as:
- how far should a phone be from the 7.0r
- is the 7.0u emc tested
- emc declaration spirit medical bike
- esd rating 7.0r
keywords:
- emc
- electromagnetic compatibility
- iec 60601-1-2
- cispr 11
- separation distance
- esd
- radiated rf
- electrical fast transient
- declaration
- immunity
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- 70t-2026-specs-emc-declaration
see_also:
- 70t-2026-specs-emc-declaration
- spirit-med-70r-specs-certifications-mdd-class-im-2007-editions
- 70u-2025-specs-certifications-mdd-class-im-nb-0123
source:
  ref: spirit-bike-70r-2021-owners-manual
  locator: '7.0R-2021: "Guidance and manufacturer''s declaration - electromagnetic
    compatibility", PDF pp. 87-88 (printed 87-88), text.md lines 2775-2872, native
    text. 7.0R-2025: SPECIFICATIONS - CONTINUED, PDF p. 50 (printed 48), lines 1413-1433,
    a flat image whose text layer holds only the Note bullets (OCR supplement lines
    1440-1500 partial). 7.0U-2025: PDF p. 48 (printed 46), lines 1343-1363 (OCR 1365-1410)'
  extracted_at: '2026-09-11'
---

**Three books print the same four tables.** The 2021 Dyaco MED book sets them as text; the two 2025
Spirit books print the page as one picture with only the closing Note bullets in the text layer, and
their renders agree row for row with the 2021 text. **The books write decimals with a comma** (0,12
m; 2,5 GHz); that is kept here.

**Guidance and manufacturer's declaration - electromagnetic compatibility.** The machine is intended
for use in the electromagnetic environment specified below; the customer or user should assure it is
used in such an environment.

| Emissions test | Compliance | Guidance |
|---|---|---|
| RF emissions CISPR 11 | Group 1 | uses RF energy only for its internal function; emissions very low, not likely to cause interference in nearby electronic equipment |
| RF emissions CISPR 11 | Class B | suitable for use in all establishments, including domestic establishments |

| Immunity test | IEC 60601 test level | Compliance level | Guidance |
|---|---|---|---|
| Electrostatic discharge (ESD) IEC 61000-4-2 | 6 kV contact, 8 kV air | 6 kV contact, 8 kV air | floors wood, concrete or ceramic tile; synthetic floors need at least 30 % RH |
| Power frequency (50/60 Hz) magnetic field IEC 61000-4-8 | 3 A/m | 3 A/m | levels characteristic of a typical commercial or hospital location |
| Radiated RF IEC 61000-4-3 | 3 V/m, 80 MHz to 2,5 GHz | 3 V/m | d = 1,2 sqrt(P) for 80 MHz to 800 MHz; d = 2,3 sqrt(P) for 800 MHz to 2,5 GHz; site-survey field strengths below the compliance level; interference may occur near equipment marked with the RF symbol |
| Electrical fast transient/burst IEC 61000-4-4 | +/-2 kV power supply lines, +/-1 kV input/output lines | the same | mains quality of a typical commercial or hospital environment |

The ESD row's polarity sign is a missing glyph on the printed pages, as on the treadmill declaration
(`70t-2026-specs-emc-declaration`); the figures are exact, the sign is not guessed at.

**Recommended separation distances**, in metres, for a transmitter of rated maximum output power P:

| P, W | 150 kHz to 80 MHz, d = 1,2 sqrt(P) | 80 MHz to 800 MHz, d = 1,2 sqrt(P) | 800 MHz to 2,5 GHz, d = 2,3 sqrt(P) |
|---|---|---|---|
| 0,01 | 0,12 | 0,12 | 0,23 |
| 0,1 | 0,38 | 0,38 | 0,73 |
| 1 | 1,2 | 1,2 | 2,3 |
| 10 | 3,8 | 3,8 | 7,3 |
| 100 | 12 | 12 | 23 |

Note 1: at 80 MHz and 800 MHz the higher frequency range's distance applies. Note 2: the guidelines
may not apply in all situations. The closing Note on every printing adds that interference from a
power or signal cable "may be reduced or abnormally displayed ... but wouldn't have any diagnostic
accuracy issue", and that a persistent interference frequency needs isolation or filtering of the
RF signal.

**The 8.0U and 8.5R books print no EMC declaration** - their second specification page is the
battery page.

