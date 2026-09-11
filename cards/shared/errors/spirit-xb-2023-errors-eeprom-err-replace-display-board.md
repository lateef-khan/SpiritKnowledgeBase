---
id: spirit-xb-2023-errors-eeprom-err-replace-display-board
title: 'EEPROM ERR, listed as E1 in two of the three tables: every screen off, every
  output stopped, and the fix is a new display board'
kind: troubleshooting
question: What does EEPROM ERR or E1 mean on a Spirit XBR55-2023, XBR95-2023 or XBU55-2023
  residential bike, and how is it fixed?
asked_as:
- my 2023 spirit bike says eeprom err
- e1 on my spirit xbr55
- bike screen went off with an eeprom message
- spirit bike e1 code
keywords:
- eeprom err
- e1
- eeprom failure
- display board
- console
- all screens off
- outputs stop
- residential bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbr95-2023
  - xbu55-2023
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
- spirit-bike-errors-eeprom-err-replace-upper-controller
- cu900ent-eeprom-err
see_also:
- spirit-xb-errors-e2-motor-does-not-move-on-level-key
- b94-2023-e1-eeprom-failure
- lcb-2023-eeprom-error
- spirit-residential-bike-errors-2023-troubleshooting-chapter-three-rows
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55 2023 service manual 8. Error Code List (E1 = EEPROM failure) and
    8.1 Error Message: E1, PDF p. 12, text.md lines 212-242; XBR95 2023 service manual
    8. Error Code List and 8.1 Error Message: EEPROM ERR, PDF p. 14, text.md lines
    229-252; XBU55 2023 service manual 8. Error Code List (E1 = EEPROM failure) and
    8.1 Error Message: EEPROM ERR, PDF p. 12-13, text.md lines 209-277'
  extracted_at: '2026-09-11'
---

**This is the EEPROM fault on the 2023 residential bikes, and the part it names is the display board.** It is not the `E2` gear motor fault on the same two tables, and it is not the 2016 books' `EEPROM ERR`, which ends at the upper controller instead.

| Code (as the table prints it) | Description |
|---|---|
| E1 (XBR55 2023, XBU55 2023) / EEPROM ERR (XBR95 2023) | EEPROM failure |

Definition, as printed: *All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "EEPROM ERR".*

Troubleshooting: **The EEPROM is abnormal, please replace the Display Board directly.**

**The label is inconsistent inside two of the books.** The XBR55 2023 lists the code as `E1` and heads its section `8.1 Error Message: E1`, yet the definition says the display shows `EEPROM ERR`. The XBU55 2023 lists `E1` in the code table and heads the very same section `8.1 Error Message: EEPROM ERR`. The XBR95 2023 lists `EEPROM ERR` and never prints `E1`. Treat `E1` and `EEPROM ERR` as one fault on these three machines: what the rider sees is `EEPROM ERR`, `E1` is only the table's name for it, and the fix is the same either way.

**The XBR95 2023 has this one message and nothing else** - it brakes with a generator and has no gear motor to fault. The XBR55 2023 and XBU55 2023 add `E2` for the gear motor: `spirit-xb-errors-e2-motor-does-not-move-on-level-key`.

The 2016 residential books answer the same message with *replace upper controller*
(`spirit-bike-errors-eeprom-err-replace-upper-controller`); the 2023 answer is the display board. Do not carry one across. Sole's 2023 bikes print the same display-board answer under `E1` - `b94-2023-e1-eeprom-failure` - and its 2023 light-commercial bikes under `EEPROM ERR` - `lcb-2023-eeprom-error`; both are Sole machines and separate cards.
