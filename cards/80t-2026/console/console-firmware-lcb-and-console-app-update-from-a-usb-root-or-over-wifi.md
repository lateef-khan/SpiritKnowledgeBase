---
id: 80t-2026-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
title: Firmware and LCB update on the treadmill from three named files in the root
  of a USB drive - a different firmware file from the bikes - and the console app
  from an APK or over Wi-Fi
kind: procedure
question: How do I update the firmware or the console app on a Spirit 80t-2026 treadmill?
asked_as:
- how do i update the 8.0t software
- what files go on the usb stick for the 8.0t update
- the 8.0t says update apk
- my 8.0t shows version v255a255
keywords:
- software update
- firmware
- lcb
- lower control board
- apk
- usb drive
- root directory
- update.json
- wifi update
- v255a255
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: console
  code: '*'
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-console-software-update-usb-root-and-automatic
see_also:
- 80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 80t-2026-console-settings-menu
- spirit-med-80-bike-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
- 85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: 8.0T SM Maintenance Mode - Item Descriptions / Software, Firmware and LCB
    Update Procedure, PDF pp. 10-11, text.md lines 151-165, and Console APP Update
    Options, PDF p. 12, lines 165-179; USB-drive screenshot in the OCR supplement
    at lines 881-888, Settings and Software screenshots at lines 895-910.
  extracted_at: '2026-09-11'
---

**Both updates run from the Software page of Maintenance Mode** (`80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`), and both carry the same
note: **keep the machine powered on during the update process.**

**Firmware and LCB (Lower Control Board):**

1. Put these **three files in the root directory of a USB drive**: **`CS56018.bin`**, **`CS31003.bin`** and
   **`update.json`**. The screenshot of the drive shows the two `.bin` files as "FDT4 Data File", the
   `.json`, and the console APK beside them.
2. **Insert the USB drive into the USB port on the back of the console.**
3. On the Software page, press **Update** under **both** the Firmware and the LCB sections.

**Console APP - two methods, either one:**

- **Method 1 - USB.** Put **`DyacoV1.0.A1.22.0.xxxxA.10.apk`** in the root of the USB drive and follow
  the same steps; the `xxxx` is the book's own placeholder for the build.
- **Method 2 - Wi-Fi.** In **Settings**, connect the machine to a Wi-Fi network; return to the Software
  page and "the system will automatically detect if a new version is available"; press **Update APK**
  under the Console APP section. The screenshot's panel reads *"Please make sure WiFi is working properly
  and then press Update APK to update it."* The Software screenshot in this book shows live values - a Firmware line that OCR reads as **V10A15**, an LCB **V2A5** and a Console App **V1.0.A1.23.1.x**, each marked "Up to Date" - and a Settings page with an Account tile reading "Proclinic Inc" and a Heart rate line under Progress Beacon. They are the photographed unit's values read from a 300 dpi render, not targets, and the firmware digits carry OCR risk.

**The page also shows the four versions** - Android, Firmware, LCB and Console APP - and the
troubleshooting chapter uses one of them: a software version reading **V255A255** means "update the
software", and if it is not that, a UART communication error means replacing both the LCB and the
console (held with the error cards).

**Which file does what is not printed** - the book never says which `.bin` is the firmware and which the
LCB, gives no version to expect, no download source and no duration. **The firmware file is not the bikes' file.** The 8.0U, 8.5R, 8.5S and 8.5UE books name `CS51009-01.bin`; this book names **`CS56018.bin`**, with the same `CS31003.bin` and `update.json` beside it (`spirit-med-80-bike-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`, `85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`). Do not load a bike firmware file onto the treadmill.

