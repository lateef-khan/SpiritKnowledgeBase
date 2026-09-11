---
id: spirit-jb950-errors-update-fail-or-search-update
title: The console shows SEARCH UPDATE or UPDATE FAIL after a software update
kind: troubleshooting
question: What do SEARCH UPDATE and UPDATE FAIL mean on a Spirit JB950-2022 Johnny
  G bike console?
asked_as:
- johnny g bike says update fail
- jb950 console shows search update
- software update didnt work on my spirit bike
- usb update failed on the johnny g bike
keywords:
- update fail
- search update
- update done
- usb
- bootloader
- software update
- console reset
- memory stick
- firmware
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-jb950-errors-limit-sensor-test-after-motor-error
- jb950-2022-errors-error-message-table-four-messages
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: MAINTENANCE MODE, UPDATE SOFTWARE, PDF page 57; JB950 2022 service manual
    5.3 MAINTENANCE MENU, UPDATE SOFTWARE, PDF p. 39, text.md lines 606-646; JB950
    2022 service manual 6.1 Console software update, PDF p. 47, text.md lines 874-895
  extracted_at: '2026-09-09'
---

**`UPDATE DONE`, flashing, is success. `SEARCH UPDATE` or `UPDATE FAIL` means the console never
read the update.**

The manual's own remedy is one line: **check the USB stick is properly inserted and try again.**

Two things about the stick cause most of it:

- It must be a **blank USB memory stick**. The manual is explicit that **no other material
  besides the updates should be on the drive**.
- The port is **underneath the console**.

The messages appear after the console reset that ends the update - hold `Play` and `+` together
for 3 seconds, `CONSOLE RESET` displays, and then either `UPDATE DONE` or one of the two
failures. On success the console resets again with `JOHNNY G METHOD` flashing; remove the stick
then.

**These are display messages, not fault codes.** The JB950 prints no numbered error code
anywhere - `spirit-commercial-bike-errors-no-error-codes-printed`.

The update procedure itself, and the rest of Maintenance Mode, is carded under
`section: console`.

**The service manual prints the same three strings** - *Console shows SEARCH UPDATE. If successful, displays UPDATE DONE. If unsuccessful, displays UPDATE FAIL, check USB for proper insertion and attempt again* - and its own update chapter adds the mechanics: the .zip holds **two** update files, both go in the root of an otherwise empty USB disk, `BOOTLOADER` is switched to `ON` under UPDATE SOFTWARE, and the console is reset with `PLAY` and `+`, after which it shows `SEARCH UPDATE` and then `UPDATE DONE`. The same book says the GFIT (heart-rate) module must be updated *before* the console and cannot be rolled back. **The service manual also corrects the "no error code" line above**: the JB950 console prints four worded error messages, listed on `jb950-2022-errors-error-message-table-four-messages`.
