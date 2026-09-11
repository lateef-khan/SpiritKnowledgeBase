---
id: spirit-bike-errors-eeprom-err-replace-upper-controller
title: 'EEPROM ERR on an LCD or LED bike console: every screen off, every output stopped,
  and the fix is a new upper controller'
kind: troubleshooting
question: What does EEPROM ERR mean on a Spirit XBR25-2016, XBR55-2016, XBU55-2016
  or XBR95-2016 residential bike or a CU900-2018 or CR900-2018 commercial bike, and
  how is it fixed?
asked_as:
- spirit bike says eeprom err
- screen went dark and shows eeprom err
- eeprom failure on my spirit recumbent
- what is eeprom err on a spirit upright bike
keywords:
- eeprom err
- eeprom failure
- upper controller
- console
- all screens off
- outputs stop
- error message
- bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900-2018
  - cu900-2018
  - xbr25-2016
  - xbr55-2016
  - xbr95-2016
  - xbu55-2016
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- spirit-xb-2023-errors-eeprom-err-replace-display-board
- cu900ent-eeprom-err
- spirit-xb-2016-errors-dashes-tension-motor-failure
see_also:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- sole-bike-eeprom-error
- spirit-xb-2016-errors-dashes-tension-motor-failure
- spirit-commercial-bike-errors-no-error-codes-printed
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: 'XBR25 2016 service manual Error code items and Error Message: EEPROM ERR,
    PDF p. 33-34, text.md lines 465-495; XBR55 2016 service manual Error code items
    and Error Message: EEPROM ERR, PDF p. 35-36, text.md lines 487-517; XBU55 2016
    service manual Error code items and Error Message: EEPROM ERR, PDF p. 33-34, text.md
    lines 466-496; XBR95 2016 service manual Error code items and Error Message: EEPROM
    ERR, PDF p. 37-38, text.md lines 496-528; CU900 2018 service manual Error code
    items and Error Message: EEPROM ERR, PDF p. 28-29, text.md lines 441-472; CR900
    2018 service manual Error code items and Error Message: EEPROM ERR, PDF p. 27-28,
    text.md lines 375-406'
  extracted_at: '2026-09-11'
---

**This is `EEPROM ERR`, the only message these six books define, and the fix they print is the upper controller - not the display board the 2023 residential books name, and not "no fix" as the CU900ENT and CR900ENT books leave it.**

| Error Message | Explain |
|---|---|
| EEPROM ERR | EEPROM failure |

Definition, as printed: *All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "EEPROM ERR".*

Troubleshooting, the whole of it: **Replace upper controller.**

The only tool the error chapter lists is a multi-meter, and it is not used for this message - there is nothing to measure, the book goes straight to the part.

**Six service manuals print this page word for word**: the XBR25 2016, XBR55 2016 and XBU55 2016 (whose error tables also carry a second row, `--` for a tension motor that will not move - `spirit-xb-2016-errors-dashes-tension-motor-failure`), the XBR95 2016 (whose table has this one row only), and the CU900 2018 and CR900 2018 commercial bikes (one row each, the `SR8800/SU8800` heading on the CR900 book covering both).

**The same message gets a different answer on other Spirit bikes.** The XBR55 2023, XBR95 2023 and XBU55 2023 say *replace the Display Board directly* (`spirit-xb-2023-errors-eeprom-err-replace-display-board`); the CU900ENT and CR900ENT print the one-row table and no fix at all (`cu900ent-eeprom-err`); the CU800 and CR800 2020 books and the CU800 2012 spell it `EEPROM ERROR` in the message window and, like this card, replace the upper controller (`ce900-2025-errors-eeprom-error-replace-upper-controller`). Match the machine before you name the part.

Sole prints `EEPROM ERR` / `E1` with the same upper-controller fix on its B94, R92, LCB and LCR bikes of the same years - `sole-bike-eeprom-error`. Different brand, separate card; do not serve it for a Spirit machine.
