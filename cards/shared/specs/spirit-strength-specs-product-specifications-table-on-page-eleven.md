---
id: spirit-strength-specs-product-specifications-table-on-page-eleven
title: Thirty-six of the thirty-nine strength manuals print a four-row Product Specifications table on page 11, the first Spirit commercial line that prints one at all
kind: fact
question: Do the Spirit commercial strength owner's manuals print a specification table, and what is in it?
asked_as:
- does the spirit strength manual have a spec sheet
- where are the specs for my spirit weight machine
- what size is the spirit strength machine
- spec table for spirit commercial strength equipment
keywords:
- specification table
- product specifications
- spec sheet
- dimensions
- machine weight
- page 11
- strength
- commercial
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csd-acbe
  - csd-bcte
  - csd-cpsp
  - csd-itot
  - csd-lelc
  - csd-lpce
  - csd-lpsr
  - csd-pfrd
  - csd-puda
  - csf-aabb
  - csf-bext
  - csf-funt
  - csf-hrac
  - csf-legp
  - csf-uprb
  - csi-cpsp
  - csi-lrow
  - css-abdo
  - css-bcur
  - css-bext
  - css-delt
  - css-glut
  - css-latp
  - css-latr
  - css-lext
  - css-lrow
  - css-prlc
  - css-scex
  - css-scpr
  - css-shpr
  - css-slgc
  - css-slgp
  - css-sqsc
  - css-srow
  - css-text
  - css-trot
  - st800dr3
  - st800fi
  - st800ft
  section: specs
  code: '*'
authority: 3
see_also:
- spirit-strength-specs-machine-weight-and-overall-dimensions
- spirit-strength-specs-no-shipping-or-carton-weight-printed
- spirit-strength-specs-no-weight-stack-rating-printed
- spirit-bike-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-climber-specs-no-specification-table
- spirit-crw800-specs-no-specification-table
- spirit-cycle-specs-no-specification-table
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: Printed page 11 of every CSS, CSD, CSF and CSI manual (page 10 of CSF-FUNT), header "Product Specifications", read from the PDF text layer of all 39 files and from a 300 dpi tesseract --psm 4 render where the text layer was empty or font-corrupted.
  extracted_at: '2026-09-10'
---

**Yes - and this is the first Spirit commercial line in the repository that prints one.** Every
cardio family checked so far prints none (see the `see_also` list). Thirty-six of the thirty-nine
strength books carry a boxed **Product Specifications** table in the top right of the printed
**page 11**, beside the unpacking instructions. The three ST800 books print no such table anywhere.

## What the table holds

Four rows at most, and never more:

| Row | What it says |
|---|---|
| A load limit | Labelled differently on almost every machine - see below |
| `Weight` | The **assembled machine** weight, in lb and kg |
| `Overall Dimensions` | Length x width x height, in inches **and** millimetres on most, millimetres only on five |
| Two extra rows on the i-Strength pair | `Minimum Resistance` and `Maximum Resistance` |

**There is no model number, no serial format, no frame material, no upholstery, no cable size, no
electrical rating and no shipping weight.** For what is missing see
`spirit-strength-specs-no-shipping-or-carton-weight-printed` and
`spirit-strength-specs-only-component-dimensions-are-the-pulley-and-two-bumpers`.

## The load-limit row is labelled seven different ways

The label changes with what the machine is, and it is **not always a user weight limit**:

| Label printed | Machines |
|---|---|
| `Maximum User Weight` | the nine CSD dual stations, the two CSI |
| `Max User Weight` | CSS-ABDO, BCUR, BEXT, DELT, LEXT, SCPR, SHPR, SLGC, SLGP, SROW, TEXT, TROT; CSF-FUNT |
| `User Weight Limit` | CSS-GLUT, LATP, LATR, PRLC, SCEX, SQSC |
| `Smith Bar Max Load` | CSS-LROW |
| `Maximum Loading Capacity` | CSF-AABB, CSF-BEXT, CSF-UPRB |
| `Safety Catches Max Load` | CSF-HRAC |
| `Maximum Carriage Capacity` | CSF-LEGP |

The **figures** on that row are carded under `section: safety`, where this repository puts user
weight limits; this card is only about the table's existence and shape.

## Where the table is missing or unreadable

- **ST800DR3, ST800FI and ST800FT print no specification table at all.** Their contents pages run
  Product Registration, Safety, Assembly, Adjusting, Training Tips, Maintenance, Warranty and stop.
  A loose whole-word search for *specification* and *dimension* over all three returns only the
  warranty boilerplate *"Product features or specifications ... subject to change"*. ST800FT does
  print an effective-resistance table instead - see
  `spirit-strength-specs-effective-resistance-is-half-the-weight-selected`.
- **CSF-FUNT prints the table on page 10, not 11**, and as a flat image: `pdftotext` returns nothing
  from that page, so the figures had to be read from a render.
- **CSS-SLGC's table is font-corrupted in the PDF.** `pdftotext` returns `Max User Weight OENJ`,
  `Weight OENJ`, `Overall Dimensions [[`. The page itself is perfectly legible; only the embedded
  encoding is broken. Read the render, never the extraction, for this one file.
