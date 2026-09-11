---
id: spirit-elliptical-errors-eeprom-err-replace-upper-controller
title: 'EEPROM ERR on an LCD or LED elliptical console: every screen off, every output
  stopped, and the fix is a new upper controller'
kind: troubleshooting
question: What does EEPROM ERR mean on a Spirit XE195-2016, XE295-2016, XE395-2016,
  XE795-2016 or XG400-2016 residential elliptical or a CE900-2021 commercial elliptical,
  and how is it fixed?
asked_as:
- my spirit elliptical says eeprom err
- elliptical screen went dark and shows eeprom err
- eeprom failure on a spirit xe elliptical
- what is eeprom err on an elliptical
keywords:
- eeprom err
- eeprom failure
- upper controller
- console
- all screens off
- outputs stop
- error message
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce900-2021
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe795-2016
  - xg400-2016
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- xe795-2023-errors-eeprom-err-replace-display-board
- cu900ent-eeprom-err
- spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller
- xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
see_also:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- spirit-bike-errors-eeprom-err-replace-upper-controller
- e35-2023-eeprom-err
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: 'CE900 (SE8800-SE026, ce900-2021) service manual Error code items and Error
    Message: EEPROM ERR, PDF p. 28-29, text.md lines 450-481; XE195 2016 (XE509S-SE021-01)
    service manual Error code items and Error Message: EEPROM ERR, PDF p. 34-35, text.md
    lines 505-537; XE295 2016 (XE519S-SE020-01) service manual Error code items and
    Error Message: EEPROM ERR, PDF p. 34-35, text.md lines 511-541; XE395 2016 (XE539S-SE019-01)
    service manual Error code items and Error Message: EEPROM ERR, PDF p. 40-41, text.md
    lines 640-673; XE795 2016 (XE815-SE024-01) service manual Error code items and
    Error Message: EEPROM ERR, PDF p. 37-38, text.md lines 518-550; XG400 2016 (SE551-SE023-01)
    service manual Error code items and Error Message: EEPROM ERR, PDF p. 32-33, text.md
    lines 448-478'
  extracted_at: '2026-09-11'
---

**This is `EEPROM ERR`, the message six elliptical service manuals define, and the fix every one of them prints is the upper controller** - not the display board the XE795 2023 names for the same message, and not "no fix" as the CE900ENT and CE1000ENT books leave it.

| Error Message | Explain |
|---|---|
| EEPROM ERR | EEPROM failure |

Definition, as printed: *All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "EEPROM ERR".*

Troubleshooting, the whole of it: **Replace upper controller.**

The only tool the error chapter lists is a multi-meter, and it is not used for this message - the book goes straight to the part.

**Six service manuals print this page word for word**: the XE195 2016 (whose troubleshooting line is printed first in Chinese, *因 EEPROM 已異常，請直接更換上控板*, and then in English), the XE295 2016, the XE395 2016, the XG400 2016 and the XE795 2016 among the residential books, and the CE900 (SE8800-SE026) commercial book. On the XE195, XE295, XE395 and XG400 the same table carries a second row, `--` for a tension motor that will not move (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`); the XE395 adds a third, `Err` for the incline VR (`xe395-2016-errors-err-incline-vr-out-of-range-or-not-read`). On the XE795 2016 and the CE900 the EEPROM row is the whole table - both brake with a generator and have no tension motor.

**The XG400 2016 contradicts itself eight pages later.** Its `Troubleshooting for Motor Error` page says the console shows `Er1` for an EEPROM problem and that the remedy is to remove power for a minute and then, if it recurs, replace the console: `xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console`. Both pages are in the same book; this card is the error chapter's answer.

**The same message gets a different answer on other Spirit ellipticals.** The XE795 2023 says *replace the Display Board directly* (`xe795-2023-errors-eeprom-err-replace-display-board`); the CE900ENT and CE1000ENT 2023 print the one-row table and no fix at all (`cu900ent-eeprom-err`); the CE800 2016, CE800 (2020) and CE850 (2020) books spell it `EEPROM ERROR` and replace the upper controller (`ce900-2025-errors-eeprom-error-replace-upper-controller`); the CE850 2016 and XE895 2016 call it `E1` (`spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller`). Match the machine before you name the part.

The Spirit residential and commercial bikes of the same years print this page with the same upper-controller fix - `spirit-bike-errors-eeprom-err-replace-upper-controller` - and Sole prints `EEPROM ERR` on its 2023 ellipticals, `e35-2023-eeprom-err`. Different product line and different brand; separate cards.
