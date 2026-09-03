---
id: sole-bike-service-manual-model-numbers
title: "Model numbers for the bikes that have a service manual"
kind: spec
question: "What is the Sole model number for each bike service manual?"
asked_as:
- "what is the sku for the 2016 b94"
- "which sole bike is su610b"
- "model number for my sole recumbent bike"
- "what six digit number is my sole bike"
keywords:
- "model number"
- "sku"
- "part number"
- "dyaco code"
- "service manual"
- "six digit"
- "bike"
- "lookup"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - b94-2016
  - b94-2019
  - lcb-2016
  - lcb-2019
  - lcr-2016
  - r92-2016
  - sb700-2019
  - sb700-2020
  - sb900-2020
  section: specs
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also: []
source:
  ref: spirit-models-sole-bikes
  locator: "Models table rows for brand Sole, ModelType Bike"
  extracted_at: '2026-09-03'
---

The Sole model number is the six digit SKU in the Spirit database `Models` table. The service manuals carry a different code, the Dyaco factory code, on their cover.

| Model | Sole model number (SKU) | Code on the manual cover |
|---|---|---|
| B94 2016 | 594116 | SU410B-SB004 |
| B94 2019 | 594118 | SU415-SB021 |
| LCB 2016 | 511116 | SU610B-YB012 |
| LCB 2019 | 511118 | SU615-YB027 |
| LCR 2016 | 522116 | SR620B-YB012 |
| R92 2016 | 592116 | SR420-SB004 |
| SB700 2019 | 570119 | SB702EGS-3260N |
| SB700 2020 | 570120 | SB702HGS-3268 |
| SB900 2020 | 590320 | SB900CGS-3268 |

**How to read the number:** the last two digits are the model year. 16 is 2016, 18 is 2019, 20 is 2020, 22 is 2023. The SB700 and SB900 lines break that rule: 570119 is named "Sole SB700 2019" and 590319 is named "SOLE SB900 2019", so those two use 19 for 2019.

**Two rows are read from the pattern, not from a year in the name.** The database names 511116 only "LCB" and 522116 only "LCR". They are the only LCB and LCR rows ending in 16, so they are the 2016 machines, but the database does not say so in words.
