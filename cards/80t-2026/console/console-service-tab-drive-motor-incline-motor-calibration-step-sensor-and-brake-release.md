---
id: 80t-2026-console-service-tab-drive-motor-incline-motor-calibration-step-sensor-and-brake-release
title: 'The treadmill Service tab: a six-key keypad test, drive-motor speed and current,
  front and rear incline D/A values with automatic calibration, a step-sensor waveform
  and a brake release'
kind: procedure
question: What tests are in the Service tab of maintenance mode on a Spirit 80t-2026
  treadmill, and how do I calibrate the incline motors?
asked_as:
- how do i calibrate the incline on the 8.0t
- what is front motor d/a on the 8.0t
- how do i release the brake on the 8.0t motor
- how do i test the step sensor on the spirit 8.0t
keywords:
- service tab
- machine type
- communication test
- loopback
- db9
- nfc sensor test
- keypad test
- drive motor
- incline motor calibration
- step sensor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: console
  code: '*'
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- 70t-2026-console-service-mode-tests
- 70t-2026-console-step-sensor-calibration
see_also:
- 80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 80t-2026-console-user-login-methods
- 80t-2026-console-safe-steps
- 80t-2026-console-data-transfer-usb
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: '8.0T SM Maintenance Mode - Item Descriptions / Service, PDF pp. 13-14,
    text.md lines 179-212, Figures 1-3 in the OCR supplement at lines 921-940. Troubleshooting
    uses: 5 TROUBLESHOOTING, PDF pp. 30 and 33-34, lines 416-445 and 466-491.'
  extracted_at: '2026-09-11'
---

The Service group of Maintenance Mode
(`80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`) holds these items:

| Item | What the book says |
|---|---|
| **Machine Type** | *"This series of six models shares the same app. You can switch the machine type on this page."* Treadmill, Upright Bike, Recumbent Bike, Recumbent Stepper, UBE, Rehab UBE - this machine is the Treadmill |
| **Communication Test** | A built-in hardware loop test - the four steps below |
| **NFC Sensor Test** | *"Place the NFC tag near the **bottom-right corner** of the console. Each detection cycle takes **three seconds**. If the tag is not detected, remove it for three seconds and try again."* |
| **Keypad Test** | Press the physical buttons; the tree lists **Grade Increase, Grade Decrease, Start/Stop, Enter, Speed Down, Speed Up** - six keys |
| **Error Log** | Displays the history of system errors |
| **Beacon Test** | Switches the beacon light bar through White, Blue, Green, Yellow, Red |
| **Drive Motor** | "Displays the rotational speed and electric current of the drive motor to assess the condition of electrical and transmission components" - Figure 1 shows **Rotational Speed (rpm)**, **Electric Current (A)** and a **Belt Speed** setting in km/h |
| **Incline Motor** | "Press the **Calibrate** button for the front and rear incline motors to initiate automatic calibration. This page also allows manual input of a value to move the motors to a specific position. **Higher values correspond to steeper incline levels**." Figures 2 and 3 show **Front Motor D/A** and **Rear Motor D/A** fields with the prompt **"Input motor D/A (10-1020)"** |
| **Step Sensor** | "When stepping on the running deck, this page displays the waveform readings from the Step Sensor" |
| **Brake** | "By releasing the electromagnetic brake on the drive motor, you can check the condition of the transmission components" |

**The Communication Test needs a cable and a wire you make up:**

1. Prepare a **1-meter USB-A (male) to USB-B (male)** cable.
2. USB-A into the **USB-A port on the back of the console**, USB-B into the **USB-B port at the data
   output interface beneath the machine**.
3. Prepare a **5 cm single-core wire**, strip both ends, and insert it into **pin 2 and pin 3 of the
   DB9 connector** at the same interface.
4. Press **Start** on the page; the system checks the hardware loop by itself.

**Where the troubleshooting chapter sends you here.** The brake is released "in maintenance mode" so the
belt can be turned by hand and the motor "tested in maintenance mode without belt load"; an incline
fault begins with "calibrate the front and rear incline motor position", and if a motor is properly
connected but does not move, "enter a value higher than the current D/A value" to drive it. Those
paths, with their voltages, are held with the error cards.

**The owner's manual's login page puts the NFC symbol at the bottom left** (`80t-2026-console-user-login-methods`);
this book says bottom-right. Nothing reconciles them. The Step Sensor is the sensor behind Safe Steps
and the Symmetry screen (`80t-2026-console-safe-steps`). The 7.0T's LED Service Mode calibrates its
step sensors to an A/D target instead (`70t-2026-console-service-mode-tests`,
`70t-2026-console-step-sensor-calibration`); the MED 8 bikes replace the motor items with crank tests
(`spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`).

