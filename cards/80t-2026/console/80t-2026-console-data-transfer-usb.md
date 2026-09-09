---
id: 80t-2026-console-data-transfer-usb
title: Exporting workout data over USB, from the port on the front and a driver first
kind: procedure
question: How do I get workout data off a Spirit 80t-2026 treadmill onto a computer?
asked_as:
- how do i download workout data from the treadmill
- can i export results to excel
- what software reads the treadmill data
- where is the usb port on this treadmill
keywords:
- data transfer
- usb type b
- workout management software
- com port driver
- vcp
- csv
- dyaco
- stress testing
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- 70t-2026-console-data-transfer-usb
see_also: []
source:
  ref: spirit-treadmill-80t-2026-owners-manual
  locator: printed pages 54-55, DATA TRANSFER SOFTWARE INSTRUCTIONS; the port is labelled N on the parts diagram
  extracted_at: '2026-09-09'
---

**The USB type B port is on the FRONT end of the product, a COM port driver must be
installed first, and the download link is `http://medical.dyaco.com/support`.** The
7.0T of the same year puts its port on the back, needs no separate driver, and uses
a different link — see `70t-2026-console-data-transfer-usb`.

A hard-wired USB connection to a PC provides detailed machine data of every
significant parameter from a workout.

1. Download the **COM Port Driver (VCP)** from
   `https://ftdichip.com/drivers/vcp-drivers/` **before** the following steps.
2. Download the **Workout Management Software** from
   `http://medical.dyaco.com/support` and connect the product to the computer with
   a **USB type A to type B** cable.
3. Click **Install** on the pop-up window, then open
   `Workout Management-Installer.exe`, set the install location and press **Next**.

- The software runs on **Windows 10, 7 and XP series, with .Net Framework 2.0**.
- Output is a **.CSV file**, openable in Microsoft Excel.
- The parts diagram labels this port **N. USB Type B Port; for Stress Testing**.

**The manual says the same software works with the 8.0U, 8.5R, 8.5S and 8.5UE**,
which are other machines in this line. Those machines are not otherwise covered by
this card.
