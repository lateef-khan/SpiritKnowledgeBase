---
id: 85ue-2025-specs-certifications
title: An IEC 60601 medical list under EU MDR 2017/745 Class I, citing EN ISO 20957-5
  for crank training equipment
kind: fact
question: What safety and medical certifications does a Spirit 8.5UE upper body ergometer
  (85ue-2025) carry?
asked_as:
- is the 8.5ue a medical device
- what certifications does the upper body ergometer have
- is the spirit arm ergometer ce marked
- does the 8.5ue meet 60601
keywords:
- certification
- certifications
- '60601'
- medical device
- mdr
- ce mark
- csa
- iso 14971
- en iso 20957
- class i
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-medical-certification-list
see_also:
- 85ue-2025-specs-specification-page
- 85ue-2025-safety-operating-environment-iec-60601
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: SPECIFICATIONS, printed p. 55 (PDF p. 57), the CERTIFICATIONS block. Read
    from a 300 dpi render with `tesseract --psm 4` as well as from the text layer,
    and reproduced from the text layer because the render mangles `Class I` to `Class
    |`
  extracted_at: '2026-09-10'
---

The `CERTIFICATIONS` block, reproduced exactly as printed:

> CAN/CSA-C22.2No. 60601-1:14, ANSI/AAMI ES60601-1:2005+A2 (R2012)+A1,
> IEC 60601-1-2:2014, EN60601-1-2:2015, IEC60601-1:2015+A1:2012,
> EN60601-1:2006+A1:2013+A12:2014, **EN ISO 20957-1**, **EN ISO 20957-5**,
> **EU MDR 2017/745 Class I**, ISO 14971:2012

**It is declared under the current European medical device regulation**, MDR
2017/745, as a **Class I** device - not under the older MDD 93/42/EEC that the
7.0S and 7.5S steppers still print.

## The one string that is specific to this machine is `EN ISO 20957-5`

EN ISO 20957 is the stationary training equipment standard and its parts are
per-machine. **The 8.5S recumbent stepper of the same family cites part 8; the
8.5UE cites part 5**, which is the part covering stationary exercise bicycles and
**upper body crank training equipment**. Both cite part 1, the general
requirements.

**That single digit is the difference between the two lists**, and it is the tell
that a certification block belongs to the arm ergometer rather than to the
stepper. Everything else in the two blocks - the CSA, ANSI/AAMI, IEC and EN 60601
editions, the MDR Class I line and ISO 14971:2012 - is identical.

## Read `Class I` from the text layer, not the render

A 300 dpi render of this page reads the last line as `EU MDR 2017/745 Class |`,
turning the Roman numeral **I** into a pipe character. **The page has a clean text
layer and it says `Class I`.** This is the one row on the page where the render is
worse than the extraction; every other row agrees between the two.

## What the block does not say

**No notified body number, no UDI, no declaration of conformity date and no FDA
listing.** A customer or a purchasing department needing a formal conformity
document has to get it from Spirit Fitness; the manual prints the standards list
and nothing behind it.

The operating conditions the 60601 standards imply - **10 °C to 36 °C, 30% to 90%
RH non-condensing, no protection against ingress of water** - are on the safety
page, `85ue-2025-safety-operating-environment-iec-60601`.

## The steppers' lists are separate cards

`spirit-climber-specs-medical-certification-list` holds the MS300, 7.0S, 7.5S,
8.5S and 8.5S-FIT blocks. They are `product_line: climber` and the facet is
single-valued, so this card is the ergometer's own. **Do not quote the 7.0S's MDD
93/42/EEC route for this machine, and do not quote this machine's MDR Class I for
a 7.0S.**
