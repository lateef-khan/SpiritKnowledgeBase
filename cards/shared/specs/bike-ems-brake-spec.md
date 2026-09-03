---
id: sole-bike-ems-brake-spec
title: "EMS brake working voltage"
kind: spec
question: "What is the EMS brake working voltage on a Sole LCB-2016, LCB-2019 or LCR-2016?"
asked_as:
- "what voltage does the ems brake use"
- "ems brake spec on my sole bike"
- "how does resistance work on the light commercial bike"
keywords:
- "ems brake"
- "working voltage"
- "21v"
- "resistance"
- "main controller"
- "driver board"
- "spec"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - lcb-2016
  - lcb-2019
  - lcr-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-ems-brake-resistance-not-changing
source:
  ref: sole-bike-lcb-2016-service-manual
  locator: "Section 3, Electrical Configurations, EMS BRAKE (same section in the LCB 2016, LCB 2019 and LCR 2016 manuals)"
  extracted_at: '2026-09-03'
---

These bikes change resistance with an **EMS brake**, not a tension motor.

- **Working voltage: DC 0 ~ 21 V.**
- The brake increases and decreases resistance.
- The console holds the key controls and the display. The main controller holds the DC power supply for the console and the EMS driver control circuit.
- The driver board takes a DC power input and drives the EMS brake output. The LCB 2016 and LCR 2016 manuals label that input **DC 24V INPUT**.
