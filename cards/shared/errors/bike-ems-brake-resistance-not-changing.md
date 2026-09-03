---
id: sole-bike-ems-brake-resistance-not-changing
title: "Resistance does not change on an EMS brake bike"
kind: troubleshooting
question: "Why does resistance not change on a Sole LCB-2016, LCB-2019 or LCR-2016?"
asked_as:
- "resistance wont change on my light commercial bike"
- "level up does nothing on the sole bike"
- "ems brake not working"
keywords:
- "resistance"
- "ems brake"
- "driver board"
- "cn3"
- "display board"
- "7-pin cable"
- "6-pin cable"
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
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-ems-brake-spec
- sole-bike-7-pin-console-cable-pinout
source:
  ref: sole-bike-lcb-2016-service-manual
  locator: "Section 8, Troubleshooting table (Display board / cable) in the LCB 2016, LCB 2019 and LCR 2016 manuals"
  extracted_at: '2026-09-03'
---

Check in this order.

**Display board**

1. Press the **UP** key. The driver board **CN3** output must go **higher** than the previous step.
2. Press the **DOWN** key. The CN3 output must go **lower** than the previous step.
3. If it does not behave that way, inspect the cable and the connections.

Note: the LCB 2016 manual prints only "The driver board CN3 OUTPUT" for steps 1 and 2, with no direction. The LCB 2019 and LCR 2016 manuals print the higher/lower wording shown above.

**Console cable**

1. Check the cable is seated well. It is a **7-pin** cable on the LCB 2016 and LCR 2016, and a **6-pin** cable on the LCB 2019.
2. Test by swapping in a known good cable.
