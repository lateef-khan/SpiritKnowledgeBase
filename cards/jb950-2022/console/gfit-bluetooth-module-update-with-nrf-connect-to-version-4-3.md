---
id: jb950-2022-console-gfit-bluetooth-module-update-with-nrf-connect-to-version-4-3
title: Updating the GFIT Bluetooth module with the nRF Connect phone app before the
  console, to firmware 4.3, which cannot be downgraded
kind: procedure
question: How do I update the Bluetooth module on a Spirit jb950-2022 bike, and in
  what order?
asked_as:
- how do i update the bluetooth on the jb950
- what is gfit on the johnny g bike
- the jb950 does not show myzone after the update
- which do i update first on the jb950 the console or the bluetooth
keywords:
- gfit
- bluetooth module
- nrf connect
- dfu
- firmware 4.3
- distribution packet
- myzone
- update order
- cannot downgrade
- ble
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: console
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-console-software-update-usb
see_also:
- jb950-2022-console-software-update-usb
- jb950-2022-console-ant-bluetooth-ftms-and-apps
- jb950-2022-console-power-and-wake-sequence
- jb950-2022-console-software-version
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 6.2 GFIT module update, PDF pp. 49-51 (printed 49-51); text.md lines 901-949,
    screenshots read from the OCR supplements for PDF pages 49-51
  extracted_at: '2026-09-11'
---

**Update the GFIT module before the console, and know that it cannot go back.** The manual's own
postscript: "GFIT module can't update to the previous version, please update the GFIT module before
update the console."

1. **Update GFIT before updating the console.**
2. Install **"nRF Connect"** on a smartphone and put the update **.zip** file on the phone. The
   manual links the Android Play Store listing (`no.nordicsemi.android.mcp`).
3. Turn the JB950 console on and open nRF Connect - **Bluetooth and location must be on** on the
   phone. Find **GFIT** in the scan list and connect.
4. Once connected, tap **DFU**.
5. Select **"Distribution packet (ZIP)"** and tap OK.
6. Select the file; the update begins.
7. **It takes about two minutes.** The GFIT page shows the progress.
8. Open **Device Information** and check the firmware version. **The update succeeded if the version
   reads 4.3.**
9. **Then update the console and reset it.** After scanning the heart-rate device, the console should
   show **Myzone plus a number**.

**GFIT is the bike's Bluetooth chip**, the one the owner's manual describes as carrying Bluetooth
FTMS alongside ANT+ (`jb950-2022-console-ant-bluetooth-ftms-and-apps`). The console's own software
is updated separately from a USB stick (`jb950-2022-console-software-update-usb`); this procedure
does not touch it.

**The phone is the tool.** Nothing here uses the console keys, the USB port or Maintenance Mode;
the module is flashed over the air from nRF Connect. The manual shows Android screens and names no
iOS route.

**The console must be awake to be found**, and this console is rider-powered - pedal above 30 RPM
or use the optional 9 V adapter (`jb950-2022-console-power-and-wake-sequence`).
