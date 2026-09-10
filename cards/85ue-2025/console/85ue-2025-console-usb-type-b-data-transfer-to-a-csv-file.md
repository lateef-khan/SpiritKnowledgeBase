---
id: 85ue-2025-console-usb-type-b-data-transfer-to-a-csv-file
title: Workout data comes off the front USB Type B port as a .csv file, over a driver and a Windows program from medical.dyaco.com
kind: procedure
question: How do I get workout data off a Spirit 85ue-2025 upper body ergometer?
asked_as:
- how do i download data from my spirit upper body ergometer
- where do i get the software for the 8.5ue
- what cable do i need to connect the ergometer to a pc
- can i export patient data from the upper body ergometer
keywords:
- data transfer
- usb type b
- csv
- com port
- vcp driver
- ftdi
- workout management
- windows
- add machine
- export
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: console
  code: '*'
  model_number: '785045'
authority: 3
not_to_be_confused_with:
- spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file
- 85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity
- spirit-xe-console-usb-port-charges-a-device-but-saves-no-data
see_also:
- 85ue-2025-console-wifi-ble-ftms-and-ant-plus
- 85ue-2025-console-ten-inch-touch-panel-on-a-360-degree-articulating-arm
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: printed pp. 46-48 (PDF pp. 48-50), DATA TRANSFER SOFTWARE INSTRUCTIONS and CONTINUED
  extracted_at: '2026-09-10'
---

**"A hard-wired USB connection to a PC provides detailed machine data of all significant
parameter from a workout to be saved in a .csv file after finishing a workout."**

**What you need:**

- **The port.** **USB Type B**, call-out **U**, **on the front end of the product** - not on the
  console.
- **The cable.** **USB type A to type B.**
- **The COM port driver (VCP)**, downloaded **before anything else**, from
  **`https://ftdichip.com/drivers/vcp-drivers/`**.
- **The Workout Management Software**, from **`http://medical.dyaco.com/support`**.
- **Windows 10, 7 or XP series, with .Net Framework 2.0.**

**The procedure, in the manual's own three steps:**

1. **Step 1.** Download the Workout Management Software from the link and connect the product to the
   computer via USB cable. **Click "Install"** when the pop-up window appears during installation.
   After installing, **open `Workout Management-Installer.exe`** to set the destination install
   location, then press **Next**.
2. **Step 2.** **Open two files, in this order.** First **`Workout Management.exe`** in the Workout
   Management folder - *"there will be a pop-up window and please don't close it"*. Second
   **`UI.exe`** in the **`UI-win32-x64`** folder, and the Workout Management panel pops up.
3. **Step 3.** Press **+ Add Machine**, input the **machine name** and **COM port**, then click
   **Add**. Use the **Settings sheet** to set the **data file path** and **measurement unit**.

**To find the COM port:** *"access your PC's Device Manager, scroll down to find the Port (COM & LPT)
item, and click to explore it to see more detail."*

**The output is a `.CSV` file**, *"which can be opened by Microsoft Excel"*.

**Leaving that first pop-up open is the step people miss.** The manual says so in the same sentence
that tells you to open the file; closing it stops the UI finding the machine.

**Two ways off this machine, and they are not the same.** This USB route is the offline one. The
console **also** uploads to a cloud account over **Wi-Fi** and streams patient data in real time
(`85ue-2025-console-wifi-ble-ftms-and-ant-plus`). **The USB port is described for "Stress Testing &
Data Transfer"; the UART port beside it is "Stress Testing" only.**

**This is not the rehab steppers' procedure, and the links differ.** The 7.0S, 7.5S and MS300 use
**`http://www.dyaco.com/software`** and need no separate driver
(`spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file`); this book uses
**`http://medical.dyaco.com/support`** plus the **FTDI VCP** driver. **Do not send an 8.5UE owner to
the older link.**

**The compatibility line in this section disagrees with the rest of the book.** It says the software
*"works with 8.0T, 8.0U, 8.5R, 8.5S and 8.5UE"*, while the console and machine-care pages name
*"8.0T, 8.0R, 8.0U, 8.5S, 8.5UE"* - **8.5R in one list, 8.0R in the other**. Both are reproduced as
printed.
