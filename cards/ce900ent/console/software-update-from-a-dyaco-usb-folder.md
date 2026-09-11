---
id: ce900ent-console-software-update-from-a-dyaco-usb-folder
title: Software updates come from a Dyaco folder on a USB stick, in three passes with
  a three-second power-off between firmware updates
kind: procedure
question: How do I update the software on a Spirit ce900ent elliptical from a USB
  stick?
asked_as:
- how do i update the ce900ent software
- ce900ent firmware update usb
- what folder does the ce900ent update need on the usb
- ce900ent update app manager install apk
keywords:
- software update manager
- usb
- dyaco folder
- update os
- update app
- update firmware
- update app manager
- update bike firmware
- install apk
- power off three seconds
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: console
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with: []
see_also:
- ce900ent-console-maintenance-menu-six-buttons-and-twelve-languages
- cu900ent-usb-software-update
- cu900ent-50h-abnormal-mcu-firmware-update
- ce900ent-console-home-screen-four-tiles-and-the-start-key
- ce1000ent-2023-console-software-update-usb-root-and-automatic
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Software Update Manager and
    the three updating procedures, PDF pp. 29-31 (printed 29-31); text.md lines 446-508,
    with the screenshots in the OCR supplements for PDF pages 29 and 30, lines 1839-1897
  extracted_at: '2026-09-11'
---

**Preparing the stick.** Add a folder named **`Dyaco`** to a USB Transcend stick and copy each
software item to be updated - or video files for new web pages - into it. Insert the stick into the
**USB slot on the back of the console** and turn the machine's power on.

**Software Update Manager** offers five buttons: **Update OS**, **Update App**, **Update Firmware**,
**Update App Manager**, **Update Bike Firmware**. The fifth is printed so on the elliptical's page;
the book was made from the bike's.

The manual gives three updating procedures, in order:

1. **"Elliptical/Bike updating procedure 1"** - the Update Bike Firmware button. When the update is
   completed, **turn the power off, wait 3 seconds for the adapter to discharge, then power back
   on** and let it reach the first page. Press **Home ten times** to get back into engineering mode
   and go to the Elliptical / Bike updating page.
2. **Updating procedure 2 - Update Firmware.** Repeat the previous step - "turning off-on-first
   page-updating".
3. **Updating procedure 3 - Update App Manager.** Opens App Update Manager (screenshot shows V1.2)
   with **Install APK** and **Uninstall APK**. Press **Install APK** to run the APK software update.
   When it finishes press **Open** to open the APP software; once the first page appears the
   product is ready to operate.

**If a picture appears instead of the first page after updating**, "there is intermittence for the
console during transmitting so that the error message is shown". Press the button ten consecutive
times to reach the first page; whatever error message is shown, this clears it.

The manual's own note calls the machine "the treadmill" in the USB preparation step. The same page
block is reused across the range; the CU900ENT and CR900ENT bike books print it word for word
(`cu900ent-usb-software-update`). An update that does not complete raises error code **50H** on
those bikes and this elliptical alike (`cu900ent-50h-abnormal-mcu-firmware-update`).

**The CE1000ENT-2023 needs no folder** - its update data goes in the root of the stick
(`ce1000ent-2023-console-software-update-usb-root-and-automatic`).
