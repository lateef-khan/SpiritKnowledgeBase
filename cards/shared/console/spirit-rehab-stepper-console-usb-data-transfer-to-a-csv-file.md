---
id: spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file
title: Session data comes off the USB port on the back of the console as a .CSV file, over a type A to type B cable
kind: procedure
question: How do I get workout data off a Spirit rehabilitation recumbent stepper?
asked_as:
- how do i download data from my rehab stepper
- where do i get the software for the spirit stepper
- what cable do i need to connect the stepper to a pc
- can i export patient data from the stepper
keywords:
- data transfer
- usb port
- type a to type b
- csv
- windows 10
- net framework
- com port
- download software
- connect
- export
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-console-usb-port-charges-a-device-but-saves-no-data
- 85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity
see_also:
- spirit-rehab-stepper-console-seven-call-outs-and-the-spm-calories-time-steps-pulse-windows
- spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
source:
  ref: spirit-climber-ms300-2021-owners-manual
  locator: MS300-2021 printed p. 33-35, Data transfer software instructions; the 7.0S-2025 prints the same section on its printed p. 32-34 and the 7.5S-2025 on its printed p. 34-36
  extracted_at: '2026-09-10'
---

**This USB port carries data, unlike every other Spirit USB port**, which charges a phone
and saves nothing (`spirit-xe-console-usb-port-charges-a-device-but-saves-no-data`).

- The port is **on the back of the console**.
- The software runs on **Windows 10, 7 and XP series, with .Net Framework 2.0**.
- **The output is a `.CSV` file.**
- It is downloaded from **`http://www.dyaco.com/software`** - follow the website's instructions.
- The cable is a **USB type A to type B**.

**Step 1.** Download the software from the link and connect the console to the computer with the USB
cable. Click **Install** when the pop-up window appears during installation. The installer is signed
by an **Unknown Publisher** and Windows warns about it; the manual prints the warning dialog and
tells you to proceed.

**Step 2.** Click **Connect**, or **Change** to select the connecting port. If you click Change, or
connect to the wrong port, a **COM port selection window** pops up - choose the correct COM port and
click **Connect**.

**The list of consoles it works with is printed differently in each book, and one of them is
broken.**

| Manual | What the bullet says |
|---|---|
| **MS300-2021** | "Works with newer **MS300** consoles with USB ports on the back" |
| **7.0S-2025** | "Works with newer **7.0T, 7.0S, 7.5S, 7.0U and 7.0R** consoles with USB ports on the back" |
| **7.5S-2025** | "Works with newer **7.0T, 7.5S, 7.5S, 7.5S and 7.5S** consoles with USB ports on the back" |

**The 7.5S list names the same console four times.** It is the 7.0S list with the other model names
overwritten - a find-and-replace that ran too far, leaving only 7.0T untouched. **Read the 7.0S
list**: the software covers the 7.0T, 7.0S, 7.5S, 7.0U and 7.0R.

**The URL is a Dyaco address in a Spirit-branded book.** All five manuals print
`dyaco.com/software`; none of them prints a spiritfitness.com equivalent. Give the caller the address
the manual prints.

**No manual says what fields the .CSV contains**, how a session is identified in it, or whether the
console stores more than one session.

## The chapter names the consoles the software works with

The MED 7.0S and 7.5S books open it with:

> Works with newer **7.0T, 7.0S, 7.5S, 7.0R and 7.0U** consoles with USB ports on the back

The 2025 7.0S prints the same five names in a different order - *7.0T, 7.0S, 7.5S, **7.0U and
7.0R***. Both add that the software runs on **Windows 10, 7 and XP series with .Net Framework 2.0**.
So the same PC software serves a treadmill, a recumbent bike and an upper-body ergometer as well as
these steppers.

**Four of the five worked examples say `7.0S`.** The status line reads `Connected 7.0S` and the
sample CSV is headed `Model: 7.0S` in the MED 7.0S book, in the **MS300** book and in the 2025 7.0S
book. **Only the MED 7.5S re-took the screenshots** - `Connected 7.5S`, `Model: 75S`. That the
MS300's book shows a 7.0S is one of the things that identifies it as a 7.0S under another badge
(`spirit-rehab-stepper-specs-two-different-machines-are-called-7-0s`).

The sample rows are dated **2017/8/1** in every book, six years before the newest of them. It is a
stock screenshot, not a record from the machine in the carton.
