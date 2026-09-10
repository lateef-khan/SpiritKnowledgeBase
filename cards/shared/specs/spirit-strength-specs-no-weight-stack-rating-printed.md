---
id: spirit-strength-specs-no-weight-stack-rating-printed
title: No selectorized strength manual prints a weight-stack rating; the assembly parts list is the only place the stack is described, and the stacks run 170 lb to 330 lb
kind: fact
question: Where does a Spirit commercial strength owner's manual state the size of the weight stack?
asked_as:
- what size weight stack does my spirit machine have
- how much weight is on the spirit strength machine
- max weight on spirit commercial weight machine
- weight stack range for spirit strength equipment
keywords:
- weight stack
- stack size
- resistance
- maximum weight
- plates
- selectorized
- parts list
- not printed
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
- spirit-strength-specs-product-specifications-table-on-page-eleven
- spirit-strength-specs-five-pound-increment-weight
- spirit-strength-specs-effective-resistance-is-half-the-weight-selected
- spirit-strength-specs-i-strength-has-no-weight-stack
- spirit-strength-specs-no-weight-stack-on-the-benches-and-racks
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: 'Absence plus reconstruction. The Product Specifications box on printed page 11 of all 36 manuals that have one contains no stack row. The plate counts come from the weight-stack row of each manual''s assembly hardware table, read from the PDF text layer where it exists and from a 300 dpi tesseract --psm 4 render of that page where it does not; every OCR-only figure was then confirmed by eye against the rendered page.'
  extracted_at: '2026-09-10'
---

**The page 11 specification table has no weight-stack row.** Neither has the parts-of-your-unit page,
which labels the stack but gives no figure. On thirty-seven of the thirty-nine machines the manual
never states how much weight the machine holds.

**The only place the stack appears with numbers is the assembly hardware table** - the step that
tells the installer to slide the plates onto the guide rods. It lists each plate size and how many,
so the stack can be reconstructed:

> `092  20lb weight stack  12`

Only **ST800FT** breaks the pattern and prints a real resistance table -
`spirit-strength-specs-effective-resistance-is-half-the-weight-selected`.

## What the reconstructed stacks come to

Every total below is the **sum of the plate quantities the assembly table prints**, including the top
plate. The manual does not print these totals; say so when you quote one.

| Total | Machines | Card |
|---|---|---|
| 170 lb | CSD-ITOT | `spirit-strength-specs-stack-of-170-lb` |
| 180 lb | CSD-BCTE | `spirit-strength-specs-stack-of-180-lb` |
| 190 lb | CSS-BCUR, CSS-TEXT | `spirit-strength-specs-stack-of-190-lb` |
| 200 lb | CSD-ACBE, CSD-CPSP, CSD-LPSR, CSD-PFRD | `spirit-strength-specs-stack-of-200-lb` |
| 220 lb | CSD-LPCE | `spirit-strength-specs-stack-of-220-lb` |
| 225 lb | CSD-LELC | `spirit-strength-specs-stack-of-225-lb` |
| 240 lb | CSS-DELT, CSS-SCPR, CSS-SHPR, CSS-TROT | `spirit-strength-specs-stack-of-240-lb` |
| 250 lb | CSS-GLUT, LATP, LATR, LEXT, PRLC, SCEX, SLGC, SROW | `spirit-strength-specs-stack-of-250-lb` |
| 270 lb | CSS-ABDO, CSS-LROW, CSS-SQSC | `spirit-strength-specs-stack-of-270-lb` |
| 280 lb | CSS-BEXT | `spirit-strength-specs-stack-of-280-lb` |
| 330 lb | CSS-SLGP | `spirit-strength-specs-stack-of-330-lb-in-twenty-pound-plates` |
| 330 lb assist | CSD-PUDA | `spirit-strength-specs-assist-stack-of-330-lb` |
| 2 x 160 lb | CSF-FUNT | `spirit-strength-specs-functional-trainer-two-ten-pound-stacks` |
| 2 x 160 lb | ST800FT | `spirit-strength-specs-effective-resistance-is-half-the-weight-selected` |
| none | CSF-AABB, BEXT, HRAC, LEGP, UPRB; ST800DR3, ST800FI | `spirit-strength-specs-no-weight-stack-on-the-benches-and-racks` |
| none | CSI-CPSP, CSI-LROW | `spirit-strength-specs-i-strength-has-no-weight-stack` |

**The CSS machines are built from 20 lb and 10 lb plates; the CSD machines from 15 lb and 10 lb.**
That is the family difference worth knowing: a dual station steps in 15 lb, a single station in 20 lb.

## Two traps in reading these tables

- **Never take a plate quantity from an OCR pass without looking at the page.** On CSD-BCTE the OCR
  read the top plate quantity as `4`; the printed table says `1`, and the 4 the reader saw was a
  callout balloon in the drawing beside the table. On CSD-LELC the OCR dropped a whole row -
  `15 lb select iron components  1` - which changes the stack from 210 lb to 225 lb.
- **Three manuals label the plates in translated Chinese, not English.** CSS-SQSC calls them
  `20lb selection of iron components` and `10 pounds of counterweight`; CSD-ACBE and CSD-LELC call
  them `selected iron set` and `counterweight set`. They are weight plates. A search for
  *weight stack* or *weight plate* misses all three.
