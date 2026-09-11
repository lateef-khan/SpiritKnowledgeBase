---
id: 85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
title: Firmware and LCB update from three named files in the root of a USB drive,
  and the Console APP from the same drive or over Wi-Fi
kind: procedure
question: How do I update the firmware, lower control board or console app on a Spirit
  85s-2025 recumbent stepper?
asked_as:
- how do i update the software on the 8.5s stepper
- what files go on the usb stick for the spirit 8.5s
- where is the usb port on the 8.5s console
- how do i update the lower control board on the 8.5s
keywords:
- software update
- firmware update
- lcb update
- lower control board
- console app
- apk
- usb drive
- root directory
- update.json
- wifi update
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: console
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-console-software-update-usb-root-and-automatic
- spirit-strength-csi-console-wifi-and-software-update
see_also:
- 85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 8.5S-785545 (MS2000-SB036-01) service manual 4.2.2.2 Software - Firmware
    and LCB Update Procedure, PDF p. 9, text.md lines 141-155, the file listing read
    from the OCR supplement lines 676-681; Console APP Update Options, PDF p. 10,
    lines 156-169, the Settings screenshot from the supplement lines 708-734
  extracted_at: '2026-09-11'
---

**Both updates run from the Software page of Maintenance Mode**
(`85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`), and both carry
the same note: **keep the machine powered on during the update process.**

**Firmware and LCB (Lower Control Board):**

1. Put these **three files in the root directory of a USB drive**: **`CS51009-01.bin`**,
   **`CS31003.bin`** and **`update.json`**. The book's screenshot of the drive shows the two `.bin`
   files as "FDT4 Data File", the `.json`, and the console APK beside them.
2. **Insert the USB drive into the USB port on the back of the console.**
3. On the Software page, press **Update** under **both** the Firmware and the LCB sections.

**Console APP - two methods, either one:**

- **Method 1 - USB.** Put the file **`DyacoV1.0.A1.22.0.xxxxA.10.apk`** in the root of the USB drive
  and follow the same steps as above; the Software page shows an **Update APK** button under Console
  APP. The `xxxx` is the book's own placeholder for the build.
- **Method 2 - Wi-Fi.** In **Settings**, connect the machine to a Wi-Fi network; return to the
  Software page and **the system detects a new version by itself**; press **Update APK**. The
  screenshot's Console APP panel reads *"Please make sure WiFi is working properly and then press
  Update APK to update it."*

**The page also shows the four versions** - Android, Firmware, LCB and Console APP - and the
troubleshooting chapter uses one of them: a software version reading **V255A255** means "update the
software", and if the version is not that the fix for a UART communication error is to replace both
the LCB and the console (held with the error cards).

**Which file does what is not printed.** The book never says which `.bin` is the firmware and which
the LCB, gives no version numbers to expect, no download source for the files, and no time the
update takes.

**The ENT bikes and the i-Strength console update differently** - a "Dyaco" folder or a bare root
with no named files on the CU1000ENT (`cu1000ent-2023-console-software-update-usb-root-and-automatic`),
and Wi-Fi only on the i-Strength console (`spirit-strength-csi-console-wifi-and-software-update`).
Do not carry these three file names to another machine.

