---
id: f85-2019-model-number
title: The code on the service manual cover and where the model year comes from
kind: spec
question: What does the code on the F85-2019 service manual cover mean, and where does
  its model year come from?
asked_as:
- what does st538 mean on my f85 manual
- what year is my st538 treadmill
- what does st538 mean on my manual
keywords:
- model number
- sku
- st538
- dyaco factory code
- six digit
- cover code
- lookup
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: specs
  code: '*'
  model_number:
  - '585818'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2019-electrical-system-parts
- f85-2019-display-board-connections
- f85-model-numbers
source:
  ref: sole-tm-f85-2019-service-manual
  locator: cover page and every section heading, which all read ST538
  extracted_at: '2026-09-04'
---

| Field | Value |
|---|---|
| Name in the Spirit database | SOLE F85 2019 |
| Code on the service manual cover | ST538-YT034 |
| Name used inside the manual | ST538 Treadmill |

**The manual never prints the words "F85" or the six digit number.** Every heading inside it says ST538: "1. ST538 Treadmill Outlines", "4. ST538 Treadmill Product Operation", "8. ST538 Treadmill Error Messages". ST538 is the Dyaco factory code for the platform, not a Sole model name.

**ST538 covers more than one model year.** The 2021 F85 ENT service manual is ST538-YT056, the same platform code with a different suffix. The suffix after the dash, not ST538 itself, identifies the build.

The Spirit database row for this machine is named "SOLE F85 2019"; the year comes from that name. The model number is on the F85 model card, `f85-model-numbers`. There is no rule that decodes a Sole SKU\'s last two digits into a model year. That rule does not hold for every Sole line, so do not apply it blindly.
