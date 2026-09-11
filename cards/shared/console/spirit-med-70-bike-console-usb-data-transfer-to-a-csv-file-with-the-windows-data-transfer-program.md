---
id: spirit-med-70-bike-console-usb-data-transfer-to-a-csv-file-with-the-windows-data-transfer-program
title: Session data comes off the USB port on the back of the console as a .CSV file,
  through the Windows Data Transfer program from dyaco.com/software
kind: procedure
question: How do I export workout data from a Spirit Medical 7.0 series bike to a
  computer?
asked_as:
- how do i get the data off the 7.0r
- what software reads the usb port on the 7.0u
- can i export a csv from my spirit medical bike
- which com port do i pick for the rehab bike
keywords:
- data transfer
- usb
- csv
- windows
- com port
- dyaco.com/software
- record
- type a to type b
- .net framework
- excel
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- 70t-2026-console-data-transfer-usb
- spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file
- spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: 7.0R OM DATA TRANSFER SOFTWARE INSTRUCTIONS, PDF pp. 40-42 (printed 38-40),
    text.md lines 1103-1165, screenshots read from the OCR supplements at lines 2200-2328;
    7.0U OM PDF pp. 38-40 (printed 36-38), lines 1066-1122; Dyaco MED 7.0R (2021)
    PDF pp. 56-58 (printed 56-58), lines 1888-1959.
  extracted_at: '2026-09-11'
---

**"Works with newer 7.0T, 7.0S, 7.5S, 7.0U and 7.0R consoles with USB ports on the back."** The
port is on the back of the console; the parts lists carry a **UART Adapter Board** in the console
assembly and nothing else names it.

- The software runs on **Windows 10, 7 and XP**, with **.Net Framework 2.0**.
- Download it from **http://www.dyaco.com/software** and follow the website instructions.
- Connect the console to the computer with a **USB cable, type A to type B**.
- The output is a **.CSV file**, which opens in Microsoft Excel.

**Step 1.** Download and install; click **Install** on the *Application Install - Security Warning*
pop-up. The screenshot shows the program name as **PDT** from an **Unknown Publisher** - that warning
is expected.

**Step 2.** Click **Connect** or **Change** to select the port. If you clicked Change or connected to
the wrong port, the *Please select COM port* window pops up; pick the right COM port (the screenshot
shows COM5) and click **Connect**.

**Step 3.** When the status shows **Connected** and the product model name (`7.0R` in the screenshots),
choose the file path and a file name, then click **Record**. Click **Stop**, or quit the program from
the console, to stop collecting. The file is at the destination you chose.

**What the CSV holds**, from the printed sample: a header of `Model`, `Date & Time` and `Program`,
then one row per second - **Program time, SPM, Steps, Level, Watt, Left Watt, Right Watt, Symmetry
L/R**. **SPM and Steps are stepper columns**; the sample is a 7.0R session (`Model: 7.0R ... Program:
MANUAL`) and the columns are shared with the 7.0S/7.5S steppers
(`spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file`).

**The books never say which COM port the console appears as** - the Windows Device Manager route is
printed only in the 8-series books
(`spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software`), which
use a different program and a front-mounted port. The 7.0T treadmill uses this same program
(`70t-2026-console-data-transfer-usb`).

