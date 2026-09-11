---
id: spirit-med-80-bike-console-wifi-ble-ftms-and-ant-plus
title: On the touchscreen bikes Wi-Fi uploads to the cloud, BLE carries FTMS for third-party
  apps, and BLE and ANT+ both read a heart rate sensor
kind: fact
question: What wireless connections does a Spirit Medical 8 series bike console have,
  and what is FTMS?
asked_as:
- does the 8.0u connect to zwift
- what is ftms on the 8.5r
- does the spirit medical bike have ant+
- can i use a bluetooth heart rate strap with the 8.0u
keywords:
- wifi
- ble
- bluetooth
- ant+
- ftms
- fitness machine service
- third party apps
- heart rate sensor
- cloud
- data streaming
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
- spirit-med-bike-console-chest-strap-5-khz-2500-hours-and-a-cr2032
see_also:
- spirit-med-80-bike-console-first-run-language-wifi-organization-account-registration-and-clock
- spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software
- 85ue-2025-console-wifi-ble-ftms-and-ant-plus
- 80t-2026-console-wireless-connectivity
source:
  ref: spirit-bike-80u-2025-owners-manual
  locator: 8.0U OM POWER ON & CONSOLE OPERATION, PDF p. 23 (printed 21), text.md lines
    592-625; 8.5R OM PDF p. 28 (printed 26), lines 753-786.
  extracted_at: '2026-09-11'
---

**Wireless connectivity: Wi-Fi, BLE, ANT+.**

| Radio | What the book says it is for |
|---|---|
| **Wi-Fi** | upload data to the cloud |
| **BLE** | FTMS protocol for 3rd party apps |
| **BLE and ANT+** | connect with a heart rate sensor - "This provides possibilities no matter what third part Heart Rate sensor unit the user wants to connect to" |

**ANT+** - "a communication protocol using very low energy and able to broadcast the signal to several
types of equipment at the same time. Dyaco 8 series products support ANT+ natively, having an
integrated ANT+ chipset."

**FTMS (FiTness Machine Service)** - "the FiTness Machine Service wireless communication protocol to
allow third party software to control exercise equipment, such as bike trainers, bikes and rowing
machines." The book explains why it matters - "making Bluetooth bike trainers and other exercise
machines available to connect is difficult because each sensor historically required a specific
protocol" - **but names no app**. Zwift, Kinomap and the like are not mentioned anywhere in either
book; FTMS is the protocol they use, and that is as far as the manual goes.

**Data transfer** - "Real-time streaming of patient's workout data is available for download", over
the USB Type B port
(`spirit-med-80-bike-console-usb-type-b-data-transfer-with-the-workout-management-software`).
**Login** - "Multiple access method login: NFC, PIN or QR Code"
(`spirit-med-80-bike-console-login-by-qr-code-nfc-or-pin-or-as-a-guest`).

**The heart rate transmitter page of the same two books says 5 kHz**, not BLE or ANT+
(`spirit-med-bike-console-chest-strap-5-khz-2500-hours-and-a-cr2032`). The two pages were written
for different consoles and nothing reconciles them; this page describes the radios this console has.

The 8.5UE ergometer and 8.0T treadmill print the same block (`85ue-2025-console-wifi-ble-ftms-and-ant-plus`,
`80t-2026-console-wireless-connectivity`).

