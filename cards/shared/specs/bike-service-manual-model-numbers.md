---
id: sole-bike-service-manual-model-numbers
title: Factory codes on the Sole bike service manual covers
kind: spec
question: Which Sole bike does each service manual cover code belong to?
asked_as:
- which sole bike is su610b
- what does the code on my sole bike service manual mean
- what year is the sb702 manual for
keywords:
- model number
- sku
- part number
- dyaco code
- service manual
- six digit
- bike
- lookup
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - b94-2016
  - b94-2019
  - b94-2023
  - lcb-2016
  - lcb-2019
  - lcb-2023
  - lcr-2016
  - lcr-2023
  - r92-2016
  - r92-2023
  - sb1200-2023
  - sb700-2019
  - sb700-2020
  - sb900-2020
  - sb900-2023
  section: specs
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also:
- b94-model-numbers
- lcb-model-numbers
- lcr-model-numbers
- r92-model-numbers
- sb700-model-numbers
- sb900-model-numbers
- sb1200-model-numbers
source:
  ref: spirit-models-sole-bikes
  locator: Models table rows for brand Sole, ModelType Bike
  extracted_at: '2026-09-03'
---
The service manuals carry the Dyaco factory code on their cover, not the Sole model number. The model numbers are on each family's model card: `b94-model-numbers`, `lcb-model-numbers`, `lcr-model-numbers`, `r92-model-numbers`, `sb700-model-numbers`, `sb900-model-numbers` and `sb1200-model-numbers`.

| Model | Code on the manual cover |
|---|---|
| B94 2016 | SU410B-SB004 |
| B94 2019 | SU415-SB021 |
| B94 2023 | SU415A-SB025 |
| LCB 2016 | SU610B-YB012 |
| LCB 2019 | SU615-YB027 |
| LCB 2023 | SU615A-SB026 |
| LCR 2016 | SR620B-YB012 |
| LCR 2023 | SR625A-SB026 |
| R92 2016 | SR420-SB004 |
| R92 2023 | SR425A-SB025 |
| SB700 2019 | SB702EGS-3260N |
| SB700 2020 | SB702HGS-3268 |
| SB900 2020 | SB900CGS-3268 |
| SB900 2023 | SB910-3268T |
| SB1200 2023 | SB950-SB027 |

**Look up the number, do not decode the digits.** There is no rule that turns the last two digits of a Sole model number into a model year: several 2019 machines carry numbers ending in 18 or 19, the F89's ends in 53, and two rows share the name "SOLE E95 2016". Take the year from the `ModelName` column of the `Models` row.

**Rows where the database gives no year.** The LCB 2016, LCR 2016, SB1200 2023 and B94 2023 rows are named only "LCB", "LCR", "SB1200" and "SOLE B94". Their model year is not recorded anywhere in the database. Say the year is unconfirmed rather than reading it off the digits.

**The SB1200 2023 has no year printed anywhere** — not in the database and not on its manual cover, which prints only `SB1200` where its five 2023 siblings print `LCB(2023)`, `LCR(2023)`, `R92(2023)`, `B94(2023)` and `SB900(2023)`.

**One row is named "SOLE SB900 2022"** and no manual in this knowledge base describes that machine; the SB900 model card lists it as not confirmed.
