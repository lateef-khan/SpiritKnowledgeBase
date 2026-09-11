---
id: ct1000ent-2023-console-software-update-usb-root-and-automatic
title: 'Software update: automatic over a wired or WiFi network, or from the root
  of a USB stick through engineering mode'
kind: procedure
question: How do I update the software or firmware on a Spirit ct1000ent-2023 treadmill
  console?
asked_as:
- how do i update the ct1000 treadmill software
- where do i put the update file on the usb stick
- does the treadmill update itself over wifi
- what is tft os and lwr on the update screen
keywords:
- software update
- firmware
- automatic update
- usb
- root directory
- engineering mode
- tft os
- lwr
- app manager
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct1000ent-2023
  applies_to:
  - ct1000ent-2023
  section: console
  code: '*'
  model_number:
  - '210854'
authority: 3
not_to_be_confused_with:
- ct900ent-console-software-update-from-a-dyaco-usb-folder
- cu900ent-usb-software-update
- spirit-ent-console-software-update
see_also:
- ct1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
source:
  ref: spirit-treadmill-ct1000ent-2023-service-manual
  locator: Section 7 Software Update, 7.1 Software update manager and 7.2 Update Firmware,
    PDF pp. 21-22 (printed 21-22); text.md lines 543-564, and the Machine Setup rows
    on PDF p. 18, lines 404-410
  extracted_at: '2026-09-11'
---

**Two routes, and the manual prefers the automatic one.** Under Machine Setup, the Software, Firmware
and App Manager entries each say: *"Please keep wired network or connect to wifi network to update
software automatically"*, with USB as the alternative.

**USB route:**

1. Put the update data in the **root directory (topmost layer) of the USB Transcend stick**. No
   folder name is required - unlike the CT900ENT, which needs a `Dyaco` folder
   (`ct900ent-console-software-update-from-a-dyaco-usb-folder`).
2. Insert the stick, enter engineering mode (`ct1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups`)
   and update the software from there.

The Software update manager screenshot shows **Software**, **Automatic Update**, **TFT OS** and **LWR**
as its entries; the manual does not expand TFT OS or LWR. Section 7.2 Update Firmware is a heading
with an image and no text.

**No power-off wait, no file name and no version numbers are printed**, and the manual does not say
what the console shows while it updates.

The owner's manual for this machine is not in the repository; nothing here is corroborated by it.

