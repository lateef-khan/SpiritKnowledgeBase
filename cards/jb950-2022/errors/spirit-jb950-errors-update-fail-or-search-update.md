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
  model_number: '950348'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-jb950-errors-limit-sensor-test-after-motor-error
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: MAINTENANCE MODE, UPDATE SOFTWARE, PDF page 57
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
