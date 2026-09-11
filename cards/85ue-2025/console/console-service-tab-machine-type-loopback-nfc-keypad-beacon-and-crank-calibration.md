---
id: 85ue-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
title: 'The ergometer Service tab: a Machine Type switch shared by six models, a USB-to-DB9
  loopback test, NFC, keypad and beacon tests, crank sensor readings and a crank calibration
  from 6 o''clock'
kind: procedure
question: What tests are in the Service tab of maintenance mode on a Spirit 85ue-2025
  upper body ergometer, and how do I calibrate the crank?
asked_as:
- how do i calibrate the crank on the 8.5ue
- what is the communication test on the ergometer
- how do i test the nfc reader on the 8.5ue
- the ergometer is set to the wrong machine type
keywords:
- service tab
- machine type
- rehab ube
- communication test
- loopback
- db9
- nfc sensor test
- keypad test
- beacon test
- crank calibration
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: console
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 80t-2026-console-service-tab-drive-motor-incline-motor-calibration-step-sensor-and-brake-release
see_also:
- 85ue-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 85ue-2025-console-login-by-qr-code-nfc-or-pin
- 85ue-2025-console-usb-type-b-data-transfer-to-a-csv-file
- spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- 85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 8.5UE SM 4.2.2.3 Service, PDF pp. 15-16, text.md lines 197-225, Figures
    1 and 2 named at lines 216-218.
  extracted_at: '2026-09-11'
---

The Service group of Maintenance Mode (`85ue-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`) holds eight items, numbered 4.2.2.3.1 to
4.2.2.3.8 - correctly, where the 8.5S book prints one number twice.

| Item | What the book says |
|---|---|
| **Machine Type** | *"This series of six models shares the same app. You can switch the machine type on this page."* The six are Treadmill, Upright Bike, Recumbent Bike, Recumbent Stepper, UBE and Rehab UBE - the 8.5UE is a UBE or Rehab UBE; the book does not say which of the two to pick. |
| **Communication Test** | A built-in hardware loop test - the four steps below. |
| **NFC Sensor Test** | *"Place the NFC tag near the **bottom-right corner** of the console. Each detection cycle takes **three seconds**. If the tag is not detected, remove it for three seconds and try again."* |
| **Keypad Test** | Press the physical buttons to verify them; the tree lists **Resistance Increase, Resistance Decrease, Start/Stop, Enter**. |
| **Error Log** | Displays the history of system errors. |
| **Beacon Test** | Switches the beacon light bar through **White, Blue, Green, Yellow, Red**. |
| **Crank Sensors** | Displays the rotational speed; the tree names a **Crank Index Magnet Sensor** and a **Crank RPM Angle Sensor**, and Figure 1 shows the magnet sensor reading **Off** and the angle sensor **0**. |
| **Crank Calibration** | *"Put the **right crank at a 6 o'clock position**, and then press the button below to run the test."* |

**The Communication Test needs a cable and a wire you make up:**

1. Prepare a **1-meter USB-A (male) to USB-B (male)** cable.
2. Insert the USB-A end into the **USB-A port on the back of the console** and the USB-B end into the
   **USB-B port at the data output interface beneath the machine**.
3. Prepare a **5 cm single-core wire**, strip the PVC from both ends, and insert it into **pin 2 and
   pin 3 of the DB9 connector** at the same data output interface.
4. Press **Start** on the page; the system checks the hardware loop by itself.

*"The maintenance video demonstrates the actual operation process"* - a video the book names and does
not supply. **Bottom-right, says this book; bottom left, says the owner's manual** (`85ue-2025-console-login-by-qr-code-nfc-or-pin`). Nothing reconciles the two; hold the tag to whichever corner carries the symbol on the machine in front of you.

**No pass values are printed** for any test - no RPM figure, no message the loopback shows on success.
The troubleshooting chapter runs the Crank Calibration first for an incorrect symmetry value, and if
that fails has the right crank set to 6 o'clock with the drive-pulley magnet at least 90 degrees from
the Hall sensor before recalibrating (held with the error cards). The USB-B port and the DB9 beside it are the ergometer's data output (`85ue-2025-console-usb-type-b-data-transfer-to-a-csv-file`). The bikes and the stepper print this tab word for word (`spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`, `85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`).

