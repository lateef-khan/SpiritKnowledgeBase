---
id: spirit-med-80-bike-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
title: Firmware and LCB update from three named files in the root of a USB drive,
  and the console app from an APK on the drive or over Wi-Fi
kind: procedure
question: How do I update the firmware or the console app on a Spirit Medical 8 series
  bike?
asked_as:
- how do i update the 8.0u software
- what files go on the usb stick for the 8.5r update
- the spirit medical bike says update apk
- my 8.0u shows version v255a255
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
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-console-software-update-usb-root-and-automatic
- spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting
see_also:
- spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- spirit-med-80-bike-console-settings-menu-and-the-four-viewing-modes-with-close-up-mode
- 85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
- 85ue-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
- 80t-2026-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U SM 4.2.2.2 Software / Firmware and LCB Update Procedure and Console
    APP Update Options, PDF pp. 12-14, text.md lines 216-266, USB-drive and Settings
    screenshots in the OCR supplements at lines 1053-1063 and 1090-1105; 8.5R SM PDF
    pp. 11-13, lines 164-203.
  extracted_at: '2026-09-11'
---

**Both updates run from the Software page of Maintenance Mode** (`spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`), and both carry the same
note: **keep the machine powered on during the update process.**

**Firmware and LCB (Lower Control Board):**

1. Put these **three files in the root directory of a USB drive**: **`CS51009-01.bin`**, **`CS31003.bin`** and
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
  and then press Update APK to update it."*

**The page also shows the four versions** - Android, Firmware, LCB and Console APP - and the
troubleshooting chapter uses one of them: a software version reading **V255A255** means "update the
software", and if it is not that, a UART communication error means replacing both the LCB and the
console (held with the error cards).

**Which file does what is not printed** - the book never says which `.bin` is the firmware and which the
LCB, gives no version to expect, no download source and no duration. **The same three files are named for the 8.5S stepper and the 8.5UE ergometer** (`85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`, `85ue-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`); **the 8.0T treadmill names a different firmware file** (`80t-2026-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`). The 4.0 series has only a bootloader switch and no update procedure at all (`spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting`).

