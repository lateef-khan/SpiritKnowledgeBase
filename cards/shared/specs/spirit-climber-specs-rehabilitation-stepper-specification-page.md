---
id: spirit-climber-specs-rehabilitation-stepper-specification-page
title: The one specification page in the climber and stepper corpus, and the two things
  printed on it that are wrong
kind: fact
question: Does a Spirit rehabilitation recumbent stepper owner's manual print a specification
  table, and what is on it?
asked_as:
- is there a spec sheet in the recumbent stepper manual
- where do i find the specs for my rehab stepper
- what does the specifications page list
- does the stepper manual give dimensions and watts
keywords:
- specifications
- spec sheet
- specification page
- dimensions
- product weight
- workload
- watts
- certifications
- manufacturer
- rehabilitation
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - 85s-2025
  - 85s-fit-2026
  - ms300-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-bike-specs-no-specification-table
see_also:
- ms300-2021-specs-dimensions-and-weight
- 70s-2025-specs-dimensions-and-weight
- 75s-2025-specs-dimensions-and-weight
- spirit-climber-85s-specs-dimensions-and-weight
- spirit-climber-specs-medical-certification-list
- spirit-climber-specs-which-manuals-print-a-parts-list
source:
  ref: spirit-climber-ms300-2021-owners-manual
  locator: Specifications, printed p. 61 (PDF p. 61), read from a 300 dpi render because
    the page heading and one row are invisible to pdftotext; the same page is 7.0S-2025
    printed p. 41 (PDF p. 43), 7.5S-2025 printed p. 43 (PDF p. 45), 8.5S-2025 printed
    p. 59 (PDF p. 61) and 8.5S-FIT-2026 printed p. 50 (PDF p. 52)
  extracted_at: '2026-09-10'
---

**Seven Spirit rehabilitation recumbent stepper manuals print a specification
page. No other Spirit stepper, stair climber or vertical climber prints one at
all** - see
`spirit-climber-specs-no-specification-table`, which covers eleven machines that
do not.

The page is headed `SPECIFICATIONS` and carries, in some order:

| Row | Printed on |
|---|---|
| **Dimensions** - length, width, height | all seven |
| **Weight** or **Product weight** | six; the 8.5S-FIT prints the heading and no figure |
| **Patient weight capacity** | all seven, 440 lb (200 kg) on every one |
| **Work load** in watts | all seven |
| **Resistance** - the type and the level count | all seven |
| **Input power** or **Power supply** | all seven |
| **Fuse rating** | all seven |
| **External power supply** - a named Sinpro part | the MS300, the 2025 7.0S and 7.5S, and both MED books |
| **Readouts** - what the console can show | the MS300, the 2025 7.0S and 7.5S, and both MED books |
| **Disposal** | the MS300, the 2025 7.5S and both MED books |
| **Certifications** | six; the 8.5S-FIT prints none |
| **Manufacturer** - Dyaco International Inc., Changhua County, Taiwan | all seven; the two MED books add a Dyaco Europe GmbH authorised representative |

**No shipping weight, no carton size, no flywheel weight, no step height and no
seat travel** is printed on any of the seven. Those still have to come from Spirit
Fitness.

## Two things on the page are wrong as printed

**The height on the 8.5S and 8.5S-FIT does not convert.** Both print
`Height : 131 cm (44.4")`. **131 cm is 51.6 inches, not 44.4** - and 44.4 inches
is 112.8 cm. The two numbers cannot both be the height. Length and width on the
same page convert correctly (220 cm = 86.6", 86 cm = 33.8"), so the error is in
the height row alone. **Quote neither figure without checking the machine**, and
say the manual contradicts itself. This was read from a 300 dpi render of both
pages, not from the text extraction, so it is what the page prints.

**The 8.5S-FIT prints a `Product weight` heading with nothing under it.** The row
is blank on the page itself, confirmed on a 300 dpi render - it is not something
the extraction dropped. The 8.5S of the previous year prints **150.9 kgs
(332 lbs)** in that place. Do not carry that figure across: the two books differ
on the power supply row as well, so they are not the same build.

## The MS300's page hides a row from `pdftotext`

The MS300's specification page has a text layer, and **its heading
`Specifications` and its `Resistance` value are not in it.** `pdftotext` returns
`Resistance` followed immediately by `Work load`, so the extraction reads as
though the machine's resistance type was never printed. A 300 dpi render of the
same page read with `tesseract --psm 4` returns
**`Resistance / Isokinetic with 20 levels of effort`**, along with the page
heading and a medical-device `REF` symbol beside the model name.

**Read this page from a render.** A word count would pass it as healthy - the
page carries about 120 native words - and the missing line is the one a customer
asks for.

## The manufacturer row names Dyaco, and these are still Spirit machines

All seven pages give the manufacturer as **Dyaco International Inc., No.1, Gong 1st
Rd., Hemei Township, Changhua County 50843, Taiwan**. Five of the seven books are
Spirit-branded - the cover reads `SPIRIT powered by dyaco`, the support line is
Spirit Fitness's, and the warranty is Spirit Fitness's. **A Dyaco address in the
manufacturer row is not evidence that the machine is a Dyaco product**, and these
cards are Spirit cards.

**The other two are the MED-badged `7.0S` and `7.5S` books**, which say Dyaco
throughout and never say Spirit. They are carded here as Spirit machines all the
same, on the owner's ruling that only a manual saying XTERRA is a different brand.
Their specification pages add a second manufacturer block - **Dyaco Europe GmbH,
Friedrich-Ebert-Straße 75, 51429 Bergisch Gladbach, Germany, +49 (0) 2204 844300**,
against an authorised-representative symbol - which no Spirit-badged book prints.
The MED 7.0S's page is the MS300's, figure for figure; see
`spirit-rehab-stepper-specs-two-different-machines-are-called-7-0s`.
