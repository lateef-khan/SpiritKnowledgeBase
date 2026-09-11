---
id: ce1000ent-2023-console-software-update-usb-root-and-automatic
title: Software update is automatic over a wired or Wi-Fi network, or from the root
  of a USB stick through engineering mode
kind: procedure
question: How do I update the software or firmware on a Spirit ce1000ent-2023 elliptical?
asked_as:
- how do i update the ce1000ent software
- ce1000ent firmware update usb
- does the ce1000ent update over wifi
- where do i put the update file for the ce1000ent
keywords:
- software update
- firmware update
- app manager
- automatic update
- wifi
- wired network
- usb root directory
- usb transcend
- tft os
- lwr
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce1000ent-2023
  applies_to:
  - ce1000ent-2023
  section: console
  code: '*'
  model_number:
  - '210054'
authority: 3
not_to_be_confused_with: []
see_also:
- ce1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
- cu1000ent-2023-console-software-update-usb-root-and-automatic
- ce900ent-console-software-update-from-a-dyaco-usb-folder
source:
  ref: spirit-elliptical-ce1000ent-2023-service-manual
  locator: Section 9 Software update, 9.1 software update manager and 9.2 Update Firmware,
    PDF pp. 17-18 (printed 17-18); text.md lines 319-343, the screenshot in the OCR
    supplement for PDF page 17, lines 1062-1077, and the Software, Firmware and App
    Manager rows of the Machine Setup table on PDF p. 16, lines 1025-1033
  extracted_at: '2026-09-11'
---

**Two routes, and the manual prefers the automatic one.** Under Machine Setup
(`ce1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups`), the Software, Firmware
and App Manager rows each say: *"Please keep wired network or connect to wifi network to update
software automatically"*, with "USB update as follows" as the alternative.

**USB route:**

1. "First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the
   project data you want to update to the USB." No folder name is required - unlike the CE900ENT,
   which needs a `Dyaco` folder (`ce900ent-console-software-update-from-a-dyaco-usb-folder`).
2. "Then insert the USB Transcend, click the engineering mode and update the software."

The Software update manager screenshot shows **Software** with an **Automatic Update** switch, **TFT
OS** (Version 1.4, "Up to Date") and **LWR** (Version 3.0, with an Update button); the manual does
not expand TFT OS or LWR. A second screenshot shows "Software Update - Downloading. Estimated time:
2 min". Section 9.2 Update Firmware is a heading with an image and no text, captioned "Image for
Treadmill/ Elliptical / Bike Firmware Update".

**No power-off wait, no file name and no version numbers are printed**, and the manual does not say
what the console shows while it updates. The CU1000ENT-2023 bike prints the same two pages
(`cu1000ent-2023-console-software-update-usb-root-and-automatic`).

The owner's manual for this machine is not in the repository; nothing here is corroborated by it.
