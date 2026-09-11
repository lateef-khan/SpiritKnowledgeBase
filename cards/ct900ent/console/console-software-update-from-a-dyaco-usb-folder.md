---
id: ct900ent-console-software-update-from-a-dyaco-usb-folder
title: 'Updating the software from a Dyaco folder on a USB stick: Update Firmware,
  a 10-second power-off for the inverter, then Install APK'
kind: procedure
question: How do I update the software on a Spirit ct900ent treadmill console?
asked_as:
- how do i update the treadmill software from usb
- what folder does the update go in
- the console shows an error picture after updating
- how long do i wait after turning the treadmill off
keywords:
- software update manager
- usb
- dyaco folder
- update firmware
- update app manager
- install apk
- inverter discharge
- 10 seconds
- home ten times
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-usb-software-update
- spirit-ent-console-software-update
- ct1000ent-2023-console-software-update-usb-root-and-automatic
see_also:
- ct900ent-maintenance-menu-overview
- ct900ent-settings-menu-access
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Maintenance / Software Update,
    PDF pp. 31-35 (printed 31-35); text.md lines 460-535
  extracted_at: '2026-09-11'
---

**Preparing the stick.** Add a folder named **`Dyaco`** to a USB Transcend stick and copy each
software item to be updated - or video files for new web pages - into it. Insert the stick into the
**USB slot on the back of the console** and turn the treadmill's power on.

Software Update Manager is reached from Maintenance in engineering mode
(`ct900ent-maintenance-menu-overview`). The treadmill procedure, in the manual's order:

1. **Update Firmware.** When the update completes, **turn the treadmill power off and wait 10
   seconds for the inverter to discharge**, then power it back on and let it reach the first page.
2. **Press Home ten times** to re-enter engineering mode and go to the treadmill updating page.
3. **Update App Manager.** Press **Install APK** to run the APK software update. When it finishes,
   press **Open** to open the APP software; once the first page appears the product is ready to
   operate.

**If a picture is shown instead of the first page after updating**, the console dropped frames during
the transfer and shows an error message. Press the button **ten consecutive times** to reach the
first page; whatever error message is shown, this clears it.

**The ten-second wait is the treadmill figure.** The same page prints the elliptical and bike
procedure beside it with **3 seconds** for the adapter to discharge and an extra "Update Ble
Firmware" step; that column is `cu900ent-usb-software-update`, not this machine.

**The owner's manual says only that Software Update Manager installs new versions of the application
software** (`ct900ent-maintenance-menu-overview`). It prints no stick preparation, no folder name and
no power-off wait.

