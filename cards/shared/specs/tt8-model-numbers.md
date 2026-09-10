---
id: tt8-model-numbers
title: TT8 model numbers by year
kind: spec
question: What is the model number for the Sole TT8?
asked_as:
- TT8 SKU
- TT8 part number
- which years was the TT8 made
- what year is my TT8
keywords:
- model number
- sku
- year
- model year
facets:
  brand:
  - sole
  product_line: treadmill
  model:
  - tt8
  - tt8-2016
  - tt8-2016-ac
  - tt8-2019
  - tt8-2019-ac
  - tt8-2020
  - tt8-2023
  applies_to:
  - tt8-2016
  - tt8-2016-ac
  - tt8-2019
  - tt8-2019-ac
  - tt8-2020
  - tt8-2023
  section: specs
  code: '*'
  model_number:
  - '588816'
  - '588818'
  - '588822'
authority: 3
not_to_be_confused_with: []
see_also:
- tt8-2016-ac-drive-motor-spec
- tt8-2019-ac-drive-motor-spec
source:
  ref: custservice-model-numbers
  locator: rows tt8-2016 to tt8-2023; no row for tt8-2020
  extracted_at: '2026-09-10'
---

| Year | Model number | Tag |
|---|---|---|
| 2016 | 588816 | tt8-2016 |
| 2016 | 588816 | tt8-2016-ac |
| 2019 | 588818 | tt8-2019 |
| 2019 | 588818 | tt8-2019-ac |
| 2020 | not confirmed | tt8-2020 |
| 2023 | 588822 | tt8-2023 |

The numbers come from the customer-service model table (`dbo.MODEL` in `CustService`); a manual rarely prints one. A row reading *not confirmed* has no settled number yet. A tag ending `-ac` is the AC drive motor version of that year and shares the year's number; the plain tag is the DC drive motor machine.
