---
id: sole-bike-service-manual-model-numbers
title: Model numbers for the bikes that have a service manual
kind: spec
question: What is the Sole model number for each bike service manual?
asked_as:
- what is the sku for the 2016 b94
- which sole bike is su610b
- model number for my sole recumbent bike
- what six digit number is my sole bike
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
see_also: []
source:
  ref: spirit-models-sole-bikes
  locator: Models table rows for brand Sole, ModelType Bike
  extracted_at: '2026-09-03'
---
The Sole model number is the six digit SKU in the Spirit database `Models` table. The service manuals carry a different code, the Dyaco factory code, on their cover.

| Model | Sole model number (SKU) | Code on the manual cover |
|---|---|---|
| B94 2016 | 594116 | SU410B-SB004 |
| B94 2019 | 594118 | SU415-SB021 |
| B94 2023 | 594122 | SU415A-SB025 |
| LCB 2016 | 511116 | SU610B-YB012 |
| LCB 2019 | 511118 | SU615-YB027 |
| LCB 2023 | 511122 | SU615A-SB026 |
| LCR 2016 | 522116 | SR620B-YB012 |
| LCR 2023 | 522122 | SR625A-SB026 |
| R92 2016 | 592116 | SR420-SB004 |
| R92 2023 | 592122 | SR425A-SB025 |
| SB700 2019 | 570119 | SB702EGS-3260N |
| SB700 2020 | 570120 | SB702HGS-3268 |
| SB900 2020 | 590320 | SB900CGS-3268 |
| SB900 2023 | 590322 | SB910-3268T |
| SB1200 2023 | 512322 | SB950-SB027 |

**How to read the number: look up the row, do not decode the digits.** There is no rule that turns the last two digits into a model year. Take the year from the `ModelName` column of the `Models` row.

The digits often look like a year and often disagree with one:

- `511118` and `525018` end in 18 and are both named 2019. `570119` and `590319` end in 19 and are also named 2019.
- `589853` (SOLE F89) ends in 53, which is not a year at all.
- `595015` and `595016` are **both** named "SOLE E95 2016".

**Rows where the database gives no year.** `511116` is named only "LCB", `522116` only "LCR", `512322` only "SB1200" and `594122` only "SOLE B94". Their model year is not recorded anywhere in the database. Say the year is unconfirmed rather than reading it off the digits.

**The SB1200 2023 has no year printed anywhere** — not in the database and not on its manual cover, which prints only `SB1200` where its five 2023 siblings print `LCB(2023)`, `LCR(2023)`, `R92(2023)`, `B94(2023)` and `SB900(2023)`.

**`590321` is named "SOLE SB900 2022"** and no card in this knowledge base covers it.
