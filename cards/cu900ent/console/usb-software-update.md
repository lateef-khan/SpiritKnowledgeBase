---
id: cu900ent-usb-software-update
title: Updating the software from a USB stick
kind: procedure
question: How do I update the software on a Spirit CU900ENT bike from USB?
asked_as:
- how do i update the firmware on my spirit bike
- usb update for the bike console
- bike console update failed
keywords:
- software update manager
- update firmware
- update bike firmware
- update app manager
- install apk
- usb
- dyaco folder
- power off
- 3 seconds
- transcend
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-maintenance-menu
- cu900ent-50h-abnormal-mcu-firmware-update
- cu900ent-internet-manager-add-website
- cu900ent-home-screen
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Maintenance / Software Update Manager pp. 28-31 (printed 28-31). Pages
    28 and 30 are flattened images and were read from raw/page-28.png and raw/page-30.png
  extracted_at: '2026-09-08'
---

**Preparing the stick.** Add a folder named **`Dyaco`** to a USB Transcend stick and copy each
software item to be updated - or video files for new web pages - into it. Insert the stick into the
**USB slot on the back of the console** and turn the machine's power on.

**Software Update Manager** offers five buttons: **Update OS**, **Update App**, **Update Firmware**,
**Update App Manager**, **Update Bike Firmware**.

The manual gives three updating procedures, in order:

1. **Update Bike Firmware.** The screen shows `Update firmware in progress...` with a percentage
   bar, then `Updated successfully and need to power off`. **Turn the machine's power off, wait 3
   seconds for the adapter to discharge, then power it back on** and let it reach the first page.
2. **Update Firmware.** Repeat the previous step - "turning off-on-first page-updating". Get back
   into engineering mode by pressing **Home ten times** from the first page.
3. **Update App Manager.** Opens App Update Manager (screenshot shows V1.2) with **Install APK** and
   **Uninstall APK**. Press **Install APK** to run the APK software update. When it finishes press
   **Open** to open the APP software; once the first page appears the product is ready to operate.

**If a picture appears instead of the first page after updating**, the console dropped frames during
the transfer and shows an error message. Press the button ten consecutive times to reach the first
page; whatever error message is shown, this clears it.

The manual's own note calls the machine "the treadmill" in the USB preparation step. It is the bike
manual; the same page block is reused across the range.

An update that does not complete raises error code **50H**.
