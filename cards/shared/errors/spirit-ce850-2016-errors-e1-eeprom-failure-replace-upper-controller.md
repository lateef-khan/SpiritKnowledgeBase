---
id: spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller
title: 'E1, shown as E-1: every screen off and every output stopped by an EEPROM failure,
  and the fix is a new upper controller'
kind: troubleshooting
question: What does E1 mean on a Spirit CE850-2016 or XE895-2016 elliptical, and how
  is it fixed?
asked_as:
- my spirit elliptical shows e1
- e-1 on the elliptical console
- elliptical went blank with e1
- what is error 1 on a spirit ce850
keywords:
- e1
- e-1
- eeprom failure
- upper controller
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
  - ce850-2016
  - xe895-2016
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-e2-table-label-tension-motor
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- ce900-2025-errors-eeprom-error-replace-upper-controller
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
- crw800-2024-errors-e1-console-eeprom-failure
see_also:
- e35-2016-e1-eeprom-failure
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- ce900-2025-errors-eeprom-error-replace-upper-controller
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850 2016 (XE898-SE011) service manual Error code items and 8-1 Error
    Message: E1, PDF p. 39-40, text.md lines 647-680; XE895 2016 (XE895-SE022) service
    manual Error code items and 8-1 Error Message: E1, PDF p. 40-41, text.md lines
    648-680'
  extracted_at: '2026-09-11'
---

**This is E1, the EEPROM fault of the CE850 2016 (XE898-SE011) and XE895 2016 (XE895-SE022) books. It is not E2, the tension motor row on the same table, and not E3, the stride VR fault.** The later CE850 (2020) and CE850 2024 books call the same fault `EEPROM ERROR`, and the other XE 2016 books call it `EEPROM ERR`.

| Error Message | Explain |
|---|---|
| E1 | EEPROM failure |

Definition, as printed: *All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "E-1".* The table writes `E1`; the definition writes `E-1` with a hyphen. Same message.

Troubleshooting, the whole of it: **Replace upper controller.**

The only tool the chapter lists is a multi-meter, and it is not used for this message.

**The two books are the same document under two names** - the XE895 2016 residential book is the CE850 2016 commercial book with the residential model name - and they print this page word for word. The other rows of their table are `E2 | Tension motor is failure`, which the chapter never shows as `E2` (`spirit-ce850-2016-errors-e2-table-label-tension-motor`; the section that describes the fault is headed `--`, `spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`), and `E3` for the stride VR (`spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`).

**Sole prints the same E1 with the same fix on its E35, E55, E95 and E95S 2016 ellipticals** - `e35-2016-e1-eeprom-failure` - and the E95S 2016 book is this book's Sole twin page for page. Different brand; separate card. The Spirit CRW800 2024 rower's `E1` is a different console (`crw800-2024-errors-e1-console-eeprom-failure`).
