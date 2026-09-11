---
id: spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software
title: Workout data comes off the front USB Type B port as a .csv file, through the
  FTDI VCP driver and the Workout Management software from medical.dyaco.com
kind: procedure
question: How do I export workout data from a Spirit Medical 8 series bike to a computer?
asked_as:
- how do i get data off the 8.0u to a pc
- what driver does the 8.5r usb port need
- where do i download workout management for the spirit medical bike
- which com port is the 8.0u on
keywords:
- data transfer
- usb type b
- csv
- workout management
- vcp driver
- ftdi
- com port
- device manager
- medical.dyaco.com
- windows
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
- spirit-med-70-bike-console-usb-data-transfer-to-a-csv-file-with-the-windows-data-transfer-program
see_also:
- spirit-med-80-bike-console-ten-inch-touch-panel-on-a-360-degree-swivel-articulating-arm
- spirit-med-80-bike-console-wifi-ble-ftms-and-ant-plus
- 85ue-2025-console-usb-type-b-data-transfer-to-a-csv-file
- 80t-2026-console-data-transfer-usb
source:
  ref: spirit-bike-80u-2025-owners-manual
  locator: '8.0U OM DATA TRANSFER SOFTWARE INSTRUCTIONS, PDF pp. 49-52 (printed 47-50),
    text.md lines 1261-1340; 8.5R OM PDF pp. 54-57 (printed 52-55), lines 1427-1506.
    Port call-outs: 8.0U OM PDF p. 14, lines 361-363.'
  extracted_at: '2026-09-11'
---

**"A hard-wired USB connection to a PC provides detailed machine data of all significant parameter
from a workout to be saved in a .csv file after finishing a workout."** It "works with 8.0T, 8.0U,
8.5R, 8.5S and 8.5UE with USB type B ports on the front end of the product" - the 8.0U parts drawing
labels it **M. USB Type B Port; for Stress Testing & Data Transfer**, beside a UART port; the 8.5R
drawing does not label it.

**Before anything else, install the COM port driver**: download the **VCP driver from
https://ftdichip.com/drivers/vcp-drivers/**. Then download the **Workout Management Software from
http://medical.dyaco.com/support**. The software runs on **Windows 10, 7 and XP with .Net Framework
2.0**; the cable is **USB type A to type B**; the output is a **.CSV** that opens in Excel.

**Step 1.** Install; click **Install** on the pop-up, then open **Workout Management-Installer.exe**,
set the install location and press Next.

**Step 2.** Two files have to be open: first **Workout Management.exe** in the Workout Management
folder - "there will be a pop-up window and please don't close it" - then **UI.exe** in the
**UI-win32-x64** folder, which opens the Workout Management panel.

**Step 3.** Press **+ Add Machine**, enter a machine name and the **COM port**, click **Add**. Set the
data file path and the measurement unit on the **Settings** sheet. **To find the COM port, open the
PC's Device Manager and expand Port (COM & LPT).**

**Step 4.** The machine appears in the list. Click the icon under **Data process** to start or stop the
data streaming, and the icon under **Detail** to see the streaming detail.

**This is not the 7.0 series program.** Those bikes use a back-mounted port and the single-file "Data
Transfer V1.0" program from dyaco.com/software, with no driver step
(`spirit-med-70-bike-console-usb-data-transfer-to-a-csv-file-with-the-windows-data-transfer-program`).
The 8.5UE and 8.0T use this one (`85ue-2025-console-usb-type-b-data-transfer-to-a-csv-file`,
`80t-2026-console-data-transfer-usb`). The same USB-B port and the DB9 beside it are what the service
manual's loopback test plugs into
(`spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`).

