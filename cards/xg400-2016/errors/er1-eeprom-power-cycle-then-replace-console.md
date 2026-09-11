---
id: xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console
title: 'Er1 in the message window is an EEPROM problem: remove power for a minute,
  and if it comes back the console must be replaced'
kind: troubleshooting
question: What does Er1 mean on a Spirit xg400-2016 elliptical, and what do I do about
  it?
asked_as:
- xg400 shows er1
- er1 on my spirit elliptical
- elliptical console stopped and says er1
- eeprom error er1
keywords:
- er1
- eeprom err
- eeprom
- console
- power cycle
- replace console
- message window
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xg400-2016
  applies_to:
  - xg400-2016
  section: errors
  code: er1
  model_number:
  - '400415'
authority: 3
not_to_be_confused_with:
- xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
see_also:
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
- xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
source:
  ref: spirit-elliptical-xg400-2016-service-manual
  locator: XG400 2016 (SE551-SE023-01) service manual Troubleshooting for Motor Error,
    EEPROM ERR paragraph, PDF p. 41, text.md lines 628-661
  extracted_at: '2026-09-11'
---

**This is `Er1`, the code the XG400 2016 book's motor-error page gives to an EEPROM fault. It is not `Err`, the gear-motor fault on the same page, and it is not the `EEPROM ERR` of the same book's error chapter - which is the same fault under another name with a different fix.**

As printed, under the heading `EEPROM ERR`:

> When there is a problem with EEPROM in the console, the message window will show the error message "Er1" and the console will stop functioning at all.
>
> EEPROM ERR(Er1) Remedy: Remove the power and wait for 1 minute then resume the power to start the console. If the console does the same, then it fails and must be replaced.

So the remedy is a **one-minute power cycle first**, and a **new console** if the message returns.

**The same book contradicts itself.** Eight pages earlier its error chapter lists the message as `EEPROM ERR`, defines it as *All screens are off, and outputs are stop when EEPROM damaged or malfunction*, and prints the one-line fix *Replace upper controller* with no power cycle - the page shared with the other XE 2016 books (`spirit-elliptical-errors-eeprom-err-replace-upper-controller`). The `Er1` spelling appears nowhere else in the book, and the `Troubleshooting for Motor Error` page it sits on is a different document pasted in after the matrix - it speaks of batteries, which this mains-powered machine does not have. Treat `Er1` and `EEPROM ERR` as one fault: try the power cycle, then replace the console (the upper controller).

The gear-motor `Err` on the same page is `xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback`.
