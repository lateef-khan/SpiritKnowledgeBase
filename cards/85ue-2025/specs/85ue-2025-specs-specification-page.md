---
id: 85ue-2025-specs-specification-page
title: The only specification page in the rower and ergometer corpus, and the coin
  cell printed on its second half
kind: fact
question: Does the Spirit 8.5UE upper body ergometer (85ue-2025) owner's manual print
  a specification table, and what is on it?
asked_as:
- is there a spec sheet for the 8.5ue
- where do i find the specs for the upper body ergometer
- what does the 8.5ue specification page list
- what battery is inside the 8.5ue console
keywords:
- specifications
- spec sheet
- specification page
- dimensions
- product weight
- workload
- certifications
- manufacturer
- cr1220
- coin cell
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number: '785045'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-rehabilitation-stepper-specification-page
- spirit-crw800-specs-no-specification-table
- spirit-climber-specs-no-specification-table
see_also:
- 85ue-2025-specs-dimensions-and-weight
- 85ue-2025-specs-fuse-rating
- 85ue-2025-specs-certifications
- 85ue-2025-specs-eddy-current-brake-and-fifty-levels
- 85ue-2025-specs-workload-5-to-1000-watts
- 85ue-2025-specs-exploded-view-with-no-parts-list
- 85ue-2025-safety-outlet-100-to-240-volt-50-60-hz-15-amp
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: SPECIFICATIONS printed p. 55 (PDF p. 57) and SPECIFICATIONS - CONTINUED
    printed p. 56 (PDF p. 58). Both pages were read from a 300 dpi render with `tesseract
    --psm 4` as well as from the text layer; the render and the text layer agree row
    for row
  extracted_at: '2026-09-10'
---

**The 8.5UE prints a full specification page, over two pages.** It is the **only
machine in the rower and ergometer corpus that prints one at all** - the five
Spirit rowers print none, and their answer is
`spirit-crw800-specs-no-specification-table`.

| Row | Value |
|---|---|
| **Dimensions** | Length 170.8 cm (67.2"), Width 76 cm (29.9"), Height 167.5 cm (65.9") |
| **Product weight** | 149 kgs (328.5 lbs) |
| **Patient weight capacity** | 200 kgs (440 lbs) - a safety limit, see `85ue-2025-safety-user-weight-limit-440-lbs` |
| **Power supply** | 100 ~ 240 Vac, 1.76 ~ 0.71 Amps, 50/60Hz - see `85ue-2025-safety-outlet-100-to-240-volt-50-60-hz-15-amp` |
| **Fuse rating** | 250V, 5A glass fuse, fast acting, 5.2 x 20 mm - see `85ue-2025-specs-fuse-rating` |
| **Workload** | 5 watts up to 1000 watts - see `85ue-2025-specs-workload-5-to-1000-watts` |
| **Resistance** | Constant and Isokinetic with 50 levels of effort - see `85ue-2025-specs-eddy-current-brake-and-fifty-levels` |
| **Manufacturer** | Dyaco International Inc., No.1, Gong 1st Rd., Hemei Township, Changhua County 50843, Taiwan |
| **CERTIFICATIONS** | an IEC 60601 medical list under EU MDR 2017/745 Class I - see `85ue-2025-specs-certifications` |

## The page was read from a render, and it needed to be

Every hardware table in this manual is a flat image that `pdftotext` returns
nothing from. **This page is not one of them** - it carries a clean text layer,
and a 300 dpi render read with `tesseract --psm 4` returns the same rows, the same
figures and the same certification strings. **Both readings agree, so the figures
above are what is printed on paper**, not a ghost layer and not an OCR guess.

## The second page is about the coin cell, not about the machine

`SPECIFICATIONS - CONTINUED`, printed p. 56, is a battery-safety page:

- **Compatible battery type : CR1220**
- **Nominal battery voltage : 3V**
- Non-rechargeable, not to be recharged, not to be force-discharged,
  disassembled, heated above **85 C** or incinerated.
- **"Contains a non-removable battery. Only professionals are allowed to
  disassemble it."**

**This is a board-level cell, not a user-serviceable one.** A customer whose clock
or settings will not hold is not to open the console; that is a service call. The
machine itself runs from the mains and has **no user battery compartment
anywhere**, which is what separates it from every Spirit rower - the CRW800 takes
two C cells, the two water rowers four AA, and the XRW600 books name no power
source at all.

## What the page does not print

**No shipping weight, no carton size, no crank length, no seat travel, no console
screen size on this page, no readouts list and no disposal row.** The
rehabilitation steppers of the same Dyaco MED platform print a `Readouts` row and
some print an `External power supply` part number; the 8.5UE prints neither. Get
those figures from Spirit Fitness.

## The rehabilitation steppers print the same page and are a different product line

The MS300, 7.0S, 7.5S, 8.5S and 8.5S-FIT recumbent steppers print a page of this
shape - `spirit-climber-specs-rehabilitation-stepper-specification-page`. **Their
figures are not this machine's.** They are `product_line: climber` and this is
`product_line: ergometer`; the facets are single-valued and a card cannot span
both, so read across with the links and never merge the numbers. Where a figure
happens to agree - the workload range, the fuse - the card says so explicitly.
