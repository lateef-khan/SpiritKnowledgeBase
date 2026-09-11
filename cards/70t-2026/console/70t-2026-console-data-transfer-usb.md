---
id: 70t-2026-console-data-transfer-usb
title: Exporting workout data over USB, from the port on the back of the console
kind: procedure
question: How do I get workout data off a Spirit 7.0T or MT200 treadmill onto a computer?
asked_as:
- how do i download workout data from the treadmill
- can i export results to excel
- what software reads the treadmill data
- where is the usb port on this treadmill
keywords:
- data transfer
- usb type b
- workout management software
- csv
- dyaco
- export
- windows
- net framework
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2025
  - 70t-2026
  - mt200-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- 80t-2026-console-data-transfer-usb
see_also:
- spirit-med-70-bike-console-usb-data-transfer-to-a-csv-file-with-the-windows-data-transfer-program
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: printed page 32, DATA TRANSFER SOFTWARE INSTRUCTIONS. 7.0T 2025 owner's
    manual PDF pp. 36-38 (printed 34-36), text.md lines 1044-1106
  extracted_at: '2026-09-09'
---

**The USB ports are on the BACK of the console, and the download link is
`http://www.dyaco.com/software`.** The 8.0T of the same year puts its port on the
front and uses a different link — see `80t-2026-console-data-transfer-usb`.

A hard-wired USB connection to a PC exports the workout data.

- Works with **newer 7.0T consoles**, which have USB ports on the back. The manual
  does not say how to tell a newer console from an older one.
- Download the software from `http://www.dyaco.com/software` and follow the
  website instructions.
- Connect the console to the computer with a **USB type A to type B** cable.
- The software runs on **Windows 10, 7 and XP series, with .Net Framework 2.0**.
- Output is a **.CSV file**.

During installation, click **Install** on the pop-up window.

**The 2022 MT200 manual describes the same software on its pp. 36-39**, with the same
link, the same type A to type B cable, the same Windows and .Net requirement, the
same .CSV output, and the same wording that it *works with newer MT200 consoles with
USB ports on the back*. It also prints two steps the 7.0T manual leaves out:

- **Click "Connect", or "Change" to pick the port.** Connecting to the wrong port
  pops up a COM port selection window; choose the correct COM port and click
  **Connect**.
- Once the status shows **Connected** with the model name beside it, **choose the
  file path and file name, then click Record** to start collecting. **Click Stop, or
  quit the program from the console, to stop.** The saved data is at the path you
  chose.

**The 2010 MT200 manual has no data transfer section at all** and never mentions a
USB port, so that machine is not on this card.

**The 2025 printing of the 7.0T owner's manual prints the same three pages**, so this card covers the 70t-2025 - with one damaged line: its first bullet reads "Works with newer **7.0T, 7.0T, 7.0T, 7.0T and 7.0T** consoles with USB ports on the back", a find-and-replace that overwrote the 7.0S, 7.5S, 7.0U and 7.0R the 2026 book and the medical bike books list (`spirit-med-70-bike-console-usb-data-transfer-to-a-csv-file-with-the-windows-data-transfer-program`).

