---
id: 85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
title: 'The Service tab: a Machine Type switch shared by six models, a USB-to-DB9
  loopback communication test, NFC, keypad, beacon and crank sensor tests, and a crank
  calibration at six o''clock'
kind: procedure
question: What tests does the Service tab of maintenance mode hold on a Spirit 85s-2025
  recumbent stepper, and how do I run the communication test and the crank calibration?
asked_as:
- how do i run the communication test on the 8.5s
- how do i calibrate the crank on the spirit 8.5s stepper
- how do i test the nfc reader on the 8.5s
- how do i test the beacon lights on the 8.5s
keywords:
- service tab
- machine type
- communication test
- loopback
- db9
- nfc sensor test
- keypad test
- error log
- beacon test
- crank calibration
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: console
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-console-service-tab-key-nfc-communication-brake-sensor-tests-and-error-log
- spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
see_also:
- 85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 85s-2025-console-beacon-progress-indicator-colour-bands
- 85s-2025-console-login-by-qr-code-nfc-or-pin
- 85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 8.5S-785545 (MS2000-SB036-01) service manual 4.2.2.3 Service, items 4.2.2.3.1
    to 4.2.2.3.8, PDF p. 11, text.md lines 170-186; the tree on PDF p. 8, lines 112-134
  extracted_at: '2026-09-11'
---

The Service group of Maintenance Mode
(`85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`) holds eight
items. The book numbers them 4.2.2.3.1 to 4.2.2.3.8 and **prints 4.2.2.3.6 twice**, on Error Log and
on Beacon Test; there is no item 4.2.2.3.5.

| Item | What the book says |
|---|---|
| **Machine Type** | *"This series of six models shares the same app. You can switch the machine type on this page."* The six are Treadmill, Upright Bike, Recumbent Bike, **Recumbent Stepper**, UBE and Rehab UBE. |
| **Communication Test** | A built-in hardware loop test - the four steps below. |
| **NFC Sensor Test** | *"Place the NFC tag near the **bottom-right corner** of the console. Each detection cycle takes **three seconds**. If the tag is not detected, remove it for three seconds and try again."* |
| **Keypad Test** | Press the physical buttons to verify them; the tree lists **Resistance Increase, Resistance Decrease, Start/Stop, Enter** - four keys. |
| **Error Log** | Displays the history of system errors. |
| **Beacon Test** | Switches the beacon light bar through **White, Blue, Green, Yellow, Red** to verify it. |
| **Crank Sensors** | Displays the rotational speed; the tree names a **Crank Index Magnet Sensor** and a **Crank RPM Angle Sensor**. |
| **Crank Calibration** | *"Put the **right crank at a 6 o'clock position**, then press the button below to run the test."* |

**The Communication Test needs a cable and a wire you make up:**

1. Prepare a **1-meter USB-A (male) to USB-B (male)** cable.
2. Insert the USB-A end into the **USB-A port on the back of the console** and the USB-B end into
   the **USB-B port at the data output interface beneath the machine**.
3. Prepare a **5 cm single-core wire**, strip the PVC from both ends, and insert it into **pin 2 and
   pin 3 of the DB9 connector** at the same data output interface.
4. On the Service page press **Start**; the system checks the hardware loop by itself.

*"The maintenance video demonstrates the actual operation process"* - a video the book names and
does not supply. The USB Type B and UART ports the owner's manual labels for stress testing are the
same interface (`85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity`).

**Bottom-right, says this book; bottom-left, says the owner's manual.** The owner's manual's login
page puts the RFID reader at *"the symbol at the bottom left of the console"*
(`85s-2025-console-login-by-qr-code-nfc-or-pin`). Nothing reconciles the two; hold the tag to
whichever corner carries the symbol on the machine in front of you.

**No pass values are printed** for any test - no RPM figure, no sensor reading, no message the
loopback shows on success - and the troubleshooting chapter's "Sensor Test in Maintenance mode" with
SPM, CALORIES, TIME and STEPS windows is the 7.5S LED console's test pasted into this book
(`spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test`); this touchscreen has
no such windows.

