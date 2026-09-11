---
id: erg700-2022-errors-e2-cable-communication-abnormal-8-pin-cable-and-tension-motor
title: 'E2 means the communication with the cable is abnormal and every function is
  disabled: check the 8-pin cable between the console and the tension motor'
kind: troubleshooting
question: What does E2 mean on an Xterra erg700-2022 rower, and what do I check?
asked_as:
- my xterra rower says e2
- erg rower e2 resistance stopped working
- rowing machine e2 cable error
- what does e2 mean on a rower
keywords:
- e2
- communication error
- 8-pin cable
- tension motor
- motherboard
- cable undone
- error code
- rower
- beep
facets:
  brand:
  - xterra
  product_line: rower
  model: erg700-2022
  applies_to:
  - erg700-2022
  section: errors
  code: e2
  model_number:
  - '170918'
authority: 3
not_to_be_confused_with:
- erg700-2022-errors-e1-ram-error-console-eeprom-failed-replace-the-console
- xterra-errors-e2-computer-cannot-interface-with-the-eeprom-ic-chip
- xterra-treadmill-errors-e2-over-rated-current-for-3-seconds
- crw800-2024-errors-e2-cable-tension-communication-error
- sr500-2016-e2-motor-error
see_also:
- erg700-2022-errors-e1-ram-error-console-eeprom-failed-replace-the-console
- erg700-2022-errors-lcd-does-not-shine-backlight-or-console-power-ac-100-240-v-dc-12-v
- crw800-2024-errors-e2-cable-tension-communication-error
- sr500-2016-e2-motor-error
source:
  ref: xterra-rower-erg700-2022-owners-manual
  locator: ERG700 OM Troubleshooting - Error Codes, PDF p. 25 (printed 22), text.md
    lines 770-794
  extracted_at: '2026-09-11'
---

**This is E2 on the rower - the cable to the tension motor - not the recumbent bikes' E2 (the computer cannot interface with the EEPROM chip, which is this rower's E1) and not the treadmills' E2 (over-current).** The two Xterra product lines swap the meanings of E1 and E2, so the letter alone answers nothing.

The book, word for word:

> When the screen displays "E2", it means that the communication with the cable is abnormal and all functions are disabled. You'll need to determine if a cable has come undone or is damaged.

It then prints a check list by device, which is the only troubleshooting table in the range that names a part on the resistance side:

| Device | Check |
|---|---|
| Console | 1. Check the connection of motherboard's 8-pin cable. 2. When UP or DOWN is pressed, a beep sound is generated; if yes, it is determined that the signal has been sent. |
| 8-pin Cable | 1. Check the cable connections. 2. Check if the cable is broken or curled. 3. Replace the cable and retest. |
| Tension Motor | Check the 8-pin cable connection. |

**The beep is the console's own test**: a beep on UP or DOWN proves the console sent the level command, so a code after a beep points down the 8-pin cable to the tension motor, and the cable is the part the book replaces. The book names no voltage, no test point on the motor, and no motor replacement - the only figure it prints for the tension motor is on the display row, which asks whether the motor is putting out DC12V (`erg700-2022-errors-lcd-does-not-shine-backlight-or-console-power-ac-100-240-v-dc-12-v`); the book does not connect that check to this code.

The Spirit CRW800 and XRW600 service manuals print this same table under the same code and add a voltage test (`crw800-2024-errors-e2-cable-tension-communication-error`); Sole's SR500 prints it too (`sr500-2016-e2-motor-error`). Those are their brands' cards; nothing in them is printed in this book.
