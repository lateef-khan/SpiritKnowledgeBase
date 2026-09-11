---
id: cs800-2016-errors-e1-eeprom-failure-replace-the-upper-controller
title: E1 on the 2016 stepper is an EEPROM failure with every screen off, and the
  fix is a new upper controller
kind: troubleshooting
question: What does E1 mean on a Spirit cs800-2016 stepper?
asked_as:
- my stepper says e1
- cs800 screens went blank with e-1
- what does e1 mean on a spirit stepper
keywords:
- e1
- e-1
- eeprom failure
- upper controller
- screens off
- outputs stop
- stepper
- error code
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: errors
  code: e1
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
- cvc800-e-1-ram-error
- crw800-2024-errors-e1-console-eeprom-failure
- spirit-2024-errors-e1-no-speed-sensor-signal
- cs800-2024-errors-eeprom-error-replace-the-console
- spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board
see_also:
- cs800-2024-errors-eeprom-error-replace-the-console
- spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board
- sc200-2016-e1-eeprom-failure
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 8. Error Messages / Troubleshooting, Error code items table, PDF p. 32,
    text.md lines 454-459; 8-1 Error Message E-1, PDF p. 33, text.md lines 475-478
  extracted_at: '2026-09-11'
---

**This is the CS800 of the 2016 `XS200-SS003` book, and it prints a code where the later CS800 books print words.** The 2020-book and 2024 CS800 show `EEPROM ERROR` in the main window and condemn the console (`cs800-2024-errors-eeprom-error-replace-the-console`); this machine shows `E1` and condemns the upper controller. Same fault, different generation, different display.

| Error Message | Explain |
|---|---|
| E1 | EEPROM failure |

**8-1 Error Message: E-1.** Definition: All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "E-1". Troubleshooting: **Replace upper controller.**

**The book writes the code two ways** - `E1` in its table and `E-1` in the section heading and definition. It is one code; the console has no hyphen to print. The CVC800 climber's `E-1` is a RAM error answered with a display board (`cvc800-e-1-ram-error`); the XS895's `E1` is answered with a display board too (`spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board`); this book's answer is the upper controller. On consoles of this shape those are the same assembly, but order the part the caller's own book names.

**Look-alikes on other product lines:** `E1` on the 2024 treadmills is a speed sensor fault, on the CRW800 rower a console EEPROM failure with no remedy printed.

Sole prints this code for the SC200 2016, the same Dyaco book under another brand: `sc200-2016-e1-eeprom-failure`.
