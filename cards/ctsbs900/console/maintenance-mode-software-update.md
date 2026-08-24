---
id: ctsbs900-maintenance-mode-software-update
title: Maintenance Mode — Service menu (USB software update, OTA MCU, OTA BLE/Wi-Fi
  module update)
kind: procedure
question: How do I update CTSBS900 software from USB or over the air?
asked_as:
- how do i update the console firmware
- how do i update via usb
- how do i update the wifi module
- console shows no wifi during update
keywords:
- software update
- usb update
- ota update
- ota mcu
- ota ble
- wifi module update
- console reset
facets:
  product_line: treadmill
  model: ctsbs900
  applies_to:
  - ctsbs900
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ctsbs900-maintenance-mode-key-and-display-test
- ctsbs900-maintenance-mode-function-settings
- ctsbs900-factory-mode-min-max-speed
see_also:
- ctsbs900-maintenance-mode-key-and-display-test
- ctsbs900-bluetooth-connectivity
source:
  ref: ctsbs900-om
  locator: p. 49
  extracted_at: '2026-08-24'
---

From the Maintenance Mode main menu, select **SERVICE >** and press **Enter**, then use **Up/Down** to select an option: USB UPDATE, OTA MCU (update software by OTA), or Update Wi-Fi Module (OTA BLE).

## USB UPDATE
After pressing Enter, the display shows "USB UPDATE > NO." Press the **Up** key to change it to "USB UPDATE > YES," then press **Enter**. Insert the USB flash drive into the USB port, then press **Enter** again. The display shows "CONSOLE RESET." After a few seconds, if an update file is found, the update begins. Once complete, the display shows "UPDATE SUCCESS."

## OTA MCU (update software by OTA)
The display shows "OTA MCU > XXX (version number)." Press Enter:
- If no Wi-Fi is available, it displays "NO WIFI."
- If no new version is available, it displays "NO NEW CODE."
- If a new version is available, it displays "HAVE NEW CODE XXX (version number)."

Then it shows "USB UPDATE > NO." Press the **Up** key to change it to "USB UPDATE > YES," then press Enter. The display shows "SW UPDATE…" and begins updating. After the update is successful, it displays "UPDATE SUCCESS."

## OTA BLE (Update Wi-Fi Module)
The display shows "OTA BLE > XXX (version number)." Press Enter:
- If no Wi-Fi is available, it displays "NO WIFI."
- If no new version is available, it displays "NO NEW CODE."
- If a new version is available, it displays "HAVE NEW CODE XXX (version number)."

Then it shows "USB UPDATE > NO." Press the **Up** key to change it to "USB UPDATE > YES," then press Enter. The display shows "SW UPDATE XXX PCT" and begins updating. Once complete, it displays "UPDATE SUCCESS."
