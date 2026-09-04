---
id: cc81-2026-model-overview
title: What this machine is, and the year the manual disagrees with itself about
kind: fact
question: What is a Sole CC81-2026, and why does the manual say 2025?
asked_as:
- what model is my sole climber
- my sole climber manual says cc81 2025 but i bought a 2026
- is the cc81 a commercial machine
keywords:
- climber trainer
- model identity
- version stamp
- residential use
- model year
- owner's manual
- stepper
- warranty date
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2026
  applies_to:
  - cc81-2026
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-2026-what-this-machine-is-called
- cc81-2026-residential-use-only
- cc81-2026-warranty-coverage-periods
source:
  ref: sole-climber-cc81-2026-owners-manual
  locator: page 1, front cover, and page 2, version stamp and ATTENTION block
  extracted_at: '2026-09-04'
---

The cover calls this machine the **CC81 Climber Trainer**, and the manual is the owner's manual for it. Every page footer reads **CC81 CLIMBER**.

**Residential use only.** The ATTENTION block on page 2 reads: "THIS FITNESS CLIMBER IS INTENDED FOR RESIDENTIAL USE ONLY AND IS WARRANTED FOR THE APPLICATION. ANY OTHER APPLICATION VOIDS THIS WARRANTY IN ITS ENTIRETY."

**The year conflict, unresolved.** The version stamp at the foot of page 2 reads **"CC81-2025 Ver. A"**, while the warranty on page 20 is dated **January 1, 2026** and the file this was extracted from is the 2026 manual (SKU 581526). The knowledge base files this machine as CC81-2026. Both printed values are recorded here and neither is treated as the winner.

**How this was read.** The manual draws its body text as outlined glyphs, so `pdftotext` dropped pages 1 and 2 entirely — the whole cover, the table of contents and the ATTENTION block were missing from the text layer, leaving only the string "CC81-2025 Ver. A". This card was read from the rendered page image.
