---
id: sole-bike-eeprom-error
title: "EEPROM error on the bike console"
kind: troubleshooting
question: "What does the EEPROM error (E1) mean on a Sole bike, and how do I fix it?"
asked_as:
- "bike says eeprom err"
- "e1 on my sole bike"
- "bike screen went dark with an error"
keywords:
- "eeprom err"
- "e1"
- "upper controller"
- "console error"
- "screens off"
- "bike"
- "eeprom failure"
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
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- sole-bike-tension-motor-error
- sole-e1-error
see_also:
- sole-bike-tension-motor-error
source:
  ref: sole-bike-b94-2016-service-manual
  locator: "Section 8, Error code items and 'Error Message: E1' (the same fault appears in all six bike service manuals)"
  extracted_at: '2026-09-03'
---

**This is the bike EEPROM fault. It is not the treadmill E1, and it is not the bike E2 (tension motor).**

**What happens:** the EEPROM is damaged or has failed. All screens go off and all outputs stop.

**Fix:** replace the upper controller.

**The two labels are printed inconsistently.** The manuals disagree about which text is the code and which is the screen message:

| Manual | Table calls the error | Detail page says the display shows |
|---|---|---|
| B94 2016, B94 2019, R92 2016 | E1 | EEPROM ERR |
| LCB 2016, LCB 2019, LCR 2016 | EEPROM ERR | E1 |

Treat "E1" and "EEPROM ERR" as the same fault on these bikes. The fix is the same either way.

Tool needed: a multi-meter.
