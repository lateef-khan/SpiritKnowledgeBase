---
id: spirit-cic-assembly-parts-diagram-labels
title: The thirteen callouts on the fitness bike drawing, three of them naming adjustments rather than parts
kind: definition
question: What are the labelled parts on the diagram in a Spirit CIC800 or CIC850 fitness bike manual?
asked_as:
- what are the parts of the cic800 called
- what is that part on the cic850 diagram
- where are the transport wheels on my spirit fitness bike
- diagram labels in the indoor cycle manual
keywords:
- parts diagram
- labelled diagram
- part names
- transport wheels
- levelers
- flywheel
- stabilizer
- fitness bike
- indoor cycle
facets:
  brand:
  - spirit
  product_line: 'bike'
  model: '*'
  applies_to:
  - cic800-2021
  - cic850-2022
  section: assembly
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xic600-assembly-parts-diagram-labels
- spirit-bike-assembly-parts-diagram-letters
see_also:
- spirit-cycle-assembly-transport-wheels-engage-when-the-rear-is-lifted
- cic800-2021-assembly-parts-included
- cic850-2022-assembly-parts-included
source:
  ref: spirit-bike-cic800-2021-owners-manual
  locator: p. 7, the unheaded labelled drawing before PRE-ASSEMBLY; the same
    thirteen callouts on PDF p. 8 of the CIC850 manual (`spirit-bike-
    cic850-2022-owners-manual`), which is a flattened image - `pdftotext`
    returns three words from it and the callouts were recovered by rendering
    the page at 300-400 dpi and reading it with `tesseract --psm 4`
  extracted_at: '2026-09-09'
---
The page carries no heading and no letters - each callout is the name itself:

**Parts:** SEAT, HANDLEBAR (via HANDLEBAR ADJUSTMENT), FLYWHEEL, PEDALS, MAIN FRAME,
FRONT STABILIZER, REAR STABILIZER, LEVELERS, TRANSPORT WHEELS.

**Adjustments, called out on the same drawing:** SEAT HEIGHT ADJ., SEAT FORWARD/AFT ADJ.,
HANDLEBAR FORWARD/AFT ADJ., HANDLEBAR ADJUSTMENT, RESISTANCE ADJUSTMENT.

Both books label the same drawing with the same callouts. **It is the only page in
either manual that shows where the levelers and the transport wheels are** - the
levelers under the stabilizers, the transport wheels on the front.

## The CIC850 page is a picture, not text

PDF page 8 of the CIC850 manual is a flattened image. `pdftotext` returns "8 Spirit
Fitness" and nothing else, so the page reads as blank and the diagram looks absent. It
is not: rendering it at 300 dpi and running `tesseract --psm 4` recovers every callout
above. The CIC800's equivalent page extracts natively.

## The CIC850 diagram promises a procedure the CIC850 does not print

SEAT HEIGHT ADJ. and SEAT FORWARD/AFT ADJ. are called out, but that manual contains no
seat-position procedure anywhere. See
[the absence card](../../cic850-2022/assembly/cic850-2022-assembly-no-seat-position-procedure.md).
