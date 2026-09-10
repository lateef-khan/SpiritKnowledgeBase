---
id: cc81-2020-model-number
title: "Cover code and model year for the climber service manual"
kind: spec
question: "What code is on the CC81-2020 climber service manual cover, and where does its model year come from?"
asked_as:
- "what does xs500 mean on my climber manual"
- "what year is my sole cc81 climber"
- "is the cc81 a 2019 or a 2020"
keywords:
- "model number"
- "sku"
- "part number"
- "dyaco code"
- "factory code"
- "six digit"
- "climber"
- "lookup"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2020
  applies_to:
  - cc81-2020
  section: specs
  code: '*'
  model_number:
  - '581519'
authority: 2
not_to_be_confused_with: []
see_also:
- cc81-2020-model-overview
- sole-ftms-bluetooth-app-support
- cc81-model-numbers
- sc200-model-numbers
source:
  ref: spirit-models-sole-climbers
  locator: "Models table rows for brand Sole, ModelType Climber and Stepper"
  extracted_at: '2026-09-03'
---

The service manual carries the Dyaco factory code on its cover, not the Sole model number. The model number is on the CC81 model card, `cc81-model-numbers`.

| Model | Code on the manual cover |
|---|---|
| CC81 2020 | XS500-YP002 |

**The model year is 2020, and neither source says so.** The database row is named only "SOLE CC81" and carries no year. The service manual carries no year either. Sole confirms this machine as the 2020 model, and that is where the `2020` in the model id comes from.

**This SKU breaks the year suffix rule.** The usual Sole convention is that the last two digits of the model number are the model year. This machine's number ends in `19`, but the machine is the 2020 model. Do not read the year off this number. It joins the SB700 and SB900 lines as a line whose suffix does not follow the treadmill pattern.

The two SC200 rows that sit near this one in the table are **not** this machine; their numbers are on the SC200 model card, `sc200-model-numbers`. A search for an SC300 row returned nothing, so the SC300 named in the 2021 Bluetooth tracker has no row in this table.
