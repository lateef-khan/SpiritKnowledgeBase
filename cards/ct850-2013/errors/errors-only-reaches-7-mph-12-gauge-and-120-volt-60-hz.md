---
id: ct850-2013-errors-only-reaches-7-mph-12-gauge-and-120-volt-60-hz
title: The belt only reaches about 7 mph while the display shows more, on the row
  that demands 12 gauge and a minimum of 120 volt AC at 60 Hz
kind: troubleshooting
question: Why does a Spirit ct850-2013 treadmill only reach about 7 mph when the display
  shows a higher speed?
asked_as:
- 2013 ct850 tops out at 7 mph
- treadmill shows 10 mph but only runs about 7
- extension cord gauge for the 2013 ct850
- low voltage treadmill slow belt
keywords:
- 7 mph
- speed mismatch
- low ac voltage
- extension cord
- 12 gauge
- 120 volt
- 60 hz
- display shows higher speed
- commercial treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2013
  applies_to:
  - ct850-2013
  section: errors
  code: no-code
  model_number:
  - '850813'
authority: 3
not_to_be_confused_with:
- ct850-2016-only-reaches-7-mph
- ct800-2020-errors-speed-caps-at-7-mph
- ct900ent-speed-display-mismatch-caps-at-7mph
- ct850-2020-only-reaches-7-mph
see_also:
- ct850-2016-display-does-not-light
- ct850-2016-motor-not-responsive-after-start
- ct850-2020-trips-onboard-20-amp-circuit
source:
  ref: spirit-treadmill-ct850-2013-owners-manual
  locator: Troubleshooting table (Problem / Solution/Cause), PDF p. 28 (printed 24);
    the book is a scan with no text layer, read from the OCR supplement for page 28,
    text.md lines 1100-1160
  extracted_at: '2026-09-11'
---

The 2013 owner's manual, word for word (from a scan, so the punctuation is the OCR's):

> **Treadmill will only achieve approximately 7 mph but shows higher speed on display**
> This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord. If an extension cord is required it should be as short as possible and heavy duty **12 gauge minimum**. Low facility/household voltage. Contact an electrician or your Spirit Fitness dealer. **A minimum of 120 volt AC current, 60hz is required.**

**Two numbers, and no other CT850 book prints this pair.** 12 gauge for the cord and 120 volt AC at 60 Hz at the outlet:

| Book | Cord | Outlet |
|---|---|---|
| **CT850 2013 owner's manual** (this card) | **12 gauge** | **120 volt AC, 60 Hz** |
| CT850 2016 service manual (`ct850-2016-only-reaches-7-mph`) | 12 gauge | 110 volt AC, 60 Hz |
| CT850 2016 and 2020 owner's manuals (`ct800-2020-errors-speed-caps-at-7-mph`) | 16 gauge | 120 volt AC |
| CT850 2018 owner's manual (`ct900ent-speed-display-mismatch-caps-at-7mph`) | 16 gauge | 110 volt AC |
| CT850 2020 service manual (`ct850-2020-only-reaches-7-mph`) | 16 gauge | 100 volt AC |

The 2013 book is the heavier-cord, higher-voltage end of that spread. Nothing in any of the books reconciles them; quote the figure printed in the caller's own manual.

**The cause is the same in every version**: the motor is getting power, but not enough of it. The belt is doing what a starved motor does - turning, but not at the commanded speed - which is why the display can read higher than the belt runs.

