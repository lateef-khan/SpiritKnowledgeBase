---
id: cu1000ent-2023-console-software-update-usb-root-and-automatic
title: 'Software update on the upright bike: automatic over a wired or WiFi network,
  or from the root of a USB stick with no Dyaco folder'
kind: procedure
question: How do I update the software or firmware on a Spirit cu1000ent-2023 bike
  console?
asked_as:
- how do i update the cu1000 bike software
- where do i put the update file on the usb stick for the cu1000ent
- does the cu1000ent update itself over wifi
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
  product_line: bike
  model: cu1000ent-2023
  applies_to:
  - cu1000ent-2023
  section: console
  code: '*'
  model_number:
  - '210354'
authority: 3
not_to_be_confused_with:
- cu900ent-usb-software-update
- ct1000ent-2023-console-software-update-usb-root-and-automatic
see_also:
- cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
- ct1000ent-2023-console-software-update-usb-root-and-automatic
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: Section 9 Software update, 9.1 software update manager and 9.2 Update Firmware,
    PDF pp. 16-17 (printed 16-17); text.md lines 287-311 and the screenshot in the
    OCR supplement for PDF page 16, lines 1057-1073; the Machine Setup rows on PDF
    p. 15, supplement lines 1022-1030
  extracted_at: '2026-09-11'
---

**Two routes, and the manual prefers the automatic one.** Under Machine Setup, the Software, Firmware
and App Manager entries each say: *"Please keep wired network or connect to wifi network to update
software automatically"*, with USB as the alternative.

**USB route:**

1. Put the update data in the **root directory (topmost layer) of the USB Transcend stick**. No
   folder name is required - unlike the CU900ENT and CR900ENT, which need a `Dyaco` folder
   (`cu900ent-usb-software-update`).
2. Insert the stick, enter engineering mode
   (`cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups`) and update the software
   from there.

The Software update manager screenshot shows **Software**, **Automatic Update**, **TFT OS** and **LWR**
as its entries; the manual does not expand TFT OS or LWR. Section 9.2 Update Firmware is a heading
with an image and no text, captioned "Image for Treadmill/ Elliptical / Bike Firmware Update".

**No power-off wait, no file name and no version numbers are printed**, and the manual does not say
what the console shows while it updates. The CT1000ENT-2023 treadmill prints the same two pages
(`ct1000ent-2023-console-software-update-usb-root-and-automatic`).

The owner's manual for this machine is not in the repository; nothing here is corroborated by it.
