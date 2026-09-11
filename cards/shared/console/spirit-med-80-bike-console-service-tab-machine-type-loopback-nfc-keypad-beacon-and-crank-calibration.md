---
id: spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
title: 'The Service tab: a Machine Type switch shared by six models, a USB-to-DB9
  loopback test, NFC, keypad and beacon tests, crank sensor readings and a crank calibration
  from 6 o''clock'
kind: procedure
question: What tests are in the Service tab of maintenance mode on a Spirit Medical
  8 series bike, and how do I calibrate the crank?
asked_as:
- how do i calibrate the crank on the 8.0u
- what is the communication test on the 8.5r
- how do i test the nfc reader on my spirit medical bike
- the 8.0u is set to the wrong machine type
keywords:
- service tab
- machine type
- communication test
- loopback
- db9
- nfc sensor test
- keypad test
- beacon test
- crank sensors
- crank calibration
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
- spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration
- 80t-2026-console-service-tab-drive-motor-incline-motor-calibration-step-sensor-and-brake-release
see_also:
- spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- spirit-med-80-bike-console-login-by-qr-code-nfc-or-pin-or-as-a-guest
- spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software
- 85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- 85ue-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U SM 4.2.2.3 Service, PDF pp. 15-16, text.md lines 266-312, Figures
    1 and 2 in the OCR supplement at lines 1094-1103; 8.5R SM PDF pp. 14-15, lines
    203-245.
  extracted_at: '2026-09-11'
---

The Service group of Maintenance Mode (`spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`) holds eight items, numbered 4.2.2.3.1 to
4.2.2.3.8.

| Item | What the book says |
|---|---|
| **Machine Type** | *"This series of six models shares the same app. You can switch the machine type on this page."* The six are Treadmill, Upright Bike, Recumbent Bike, Recumbent Stepper, UBE and Rehab UBE - the 8.0U is the Upright Bike, the 8.5R the Recumbent Bike. |
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
not supply. **Bottom-right, says this book; bottom left, says the owner's manual.** The owner's manuals' login page puts the RFID reader at "the symbol located on the bottom left of the console" (`spirit-med-80-bike-console-login-by-qr-code-nfc-or-pin-or-as-a-guest`). Nothing reconciles the two; hold the tag to whichever corner carries the symbol on the machine in front of you.

**No pass values are printed** for any test - no RPM figure, no message the loopback shows on success.
The troubleshooting chapter runs the Crank Calibration first for an incorrect symmetry value, and if
that fails has the right crank set to 6 o'clock with the drive-pulley magnet at least 90 degrees from
the Hall sensor before recalibrating (held with the error cards). The 7.0 series does the same crank calibration from an LED menu, with a brake test beside it (`spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration`); the 8.5S and 8.5UE print this tab word for word (`85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`, `85ue-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`); the 8.0T replaces the crank items with motor, incline and step-sensor tests (`80t-2026-console-service-tab-drive-motor-incline-motor-calibration-step-sensor-and-brake-release`).

