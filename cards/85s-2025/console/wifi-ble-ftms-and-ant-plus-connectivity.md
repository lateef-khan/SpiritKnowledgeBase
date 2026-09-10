---
id: 85s-2025-console-wifi-ble-ftms-and-ant-plus-connectivity
title: Wi-Fi uploads to the cloud, BLE carries FTMS for third-party apps, and BLE and ANT+ both read a heart rate sensor
kind: fact
question: What can a Spirit 85s-2025 recumbent stepper console connect to?
asked_as:
- does my stepper have wifi
- what heart rate straps work with the spirit stepper
- can i use a third party app with the stepper
- does the stepper support ant plus
keywords:
- wifi
- ble
- bluetooth low energy
- ant+
- ftms
- fitness machine service
- cloud
- heart rate sensor
- third party app
- data transfer
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
- csc880-2025-console-bluetooth-with-ftms-declared-with-no-pairing-procedure
- spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file
see_also:
- 85s-2025-console-login-by-qr-code-nfc-or-pin
- 85s-2025-console-beacon-progress-indicator-colour-bands
source:
  ref: spirit-climber-85s-2025-owners-manual
  locator: printed p. 28, POWER ON & CONSOLE OPERATION, the right-hand column; the USB and UART ports are call-outs R and S on printed p. 13
  extracted_at: '2026-09-10'
---

**Three radios and two wired ports, each with its own job.**

| Link | What it is for |
|---|---|
| **Wi-Fi** | **Uploads data to the cloud** |
| **BLE** | **FTMS protocol for third-party apps** |
| **BLE and ANT+** | **Connect with a heart rate sensor** |
| **USB Type B port** | **Stress Testing & Data Transfer** (call-out R, back of the machine) |
| **UART port** | **Stress Testing** (call-out S) |

**"This provides possibilities no matter what third-party Heart Rate sensor unit the user wants to
connect to."** That is the whole of the strap-compatibility claim; **the manual names no brand and no
pairing procedure** for the sensor - the status bar simply carries a **Heart Rate Sensor Connection**
icon.

**ANT+** is described as *"a communication protocol using very low energy and able to broadcast the
signal to several types of equipment at the same time"*, and the manual says **"Dyaco 8 series
products support ANT+ natively, having an integrated ANT+ chipset."**

**FTMS** is the **FiTness Machine Service** wireless protocol *"to allow third party software to
control exercise equipment, such as Stepper trainers, Steppers and rowing machines"*. The manual adds
that making Bluetooth machines available to connect **"is difficult because each sensor historically
required a specific protocol"** - it names no app that has been tested.

**Real-time streaming of the patient's workout data is available for download**, and login supports
**NFC, PIN or QR Code** (`85s-2025-console-login-by-qr-code-nfc-or-pin`).

**A Spirit book calling the machine a Dyaco product.** This manual says **"Dyaco 8 series"**,
**"Dyaco MED products"** and **"MED 8 series products (8.0T, 8.0U, 8.5R, 8.5S, 8.5UE)"**, and its
cover reads "Spirit, powered by Dyaco". Quote the Spirit model when you answer; the 8 series names
are the OEM's.

**This is not the rehab family's .CSV export.** The 7.0S, 7.5S and MS300 pull a `.CSV` off a USB port
with a Windows program (`spirit-rehab-stepper-console-usb-data-transfer-to-a-csv-file`); this console
streams to a cloud account instead, and its USB port is described for stress testing.
