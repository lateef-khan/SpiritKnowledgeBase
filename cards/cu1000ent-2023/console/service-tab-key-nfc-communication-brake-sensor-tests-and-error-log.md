---
id: cu1000ent-2023-console-service-tab-key-nfc-communication-brake-sensor-tests-and-error-log
title: 'The Service tab: a Key Test, an NFC Test, a Communication Test, a Brake Test,
  Sensor Tests and an Error Code Log cleared by ten presses'
kind: procedure
question: What tests does the Service tab hold on a Spirit CU1000ENT or CR1000ENT 2023 bike,
  and how do I clear the error log?
asked_as:
- how do i test the buttons on the cu1000 console
- how do i test the brake on the cu1000ent
- how do i clear the error log on the cu1000ent
- is there a calibration on the cu1000 bike
keywords:
- service
- key test
- nfc test
- communication test
- brake test
- sensor test
- error code log
- ten presses
- maintenance mode
- rs232
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr1000ent-2023
  - cu1000ent-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ct1000ent-2023-console-incline-only-calibration-and-service-tests
see_also:
- cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
- ct1000ent-2023-console-incline-only-calibration-and-service-tests
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: Section 8 Setting and Operation for Engineering Mode, Service, PDF p. 16
    (printed 16); the page is a flattened image read from the OCR supplement for PDF
    page 16, text.md lines 1037-1055. CR1000(2023) SR8880-SB028 service manual, Service
    Introduction, PDF p. 16 (printed 16), text.md line 297; the page is a flattened image
    read from the OCR supplement lines 1298-1317
  extracted_at: '2026-09-11'
---

The Service group of Maintenance Mode (`cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups`)
holds six items, word for word:

| Item | What the manual says |
|---|---|
| Key Test | Press the "button" to start calibration. The corresponding screen display of the physical button flashes. |
| NFC Test | Correspond to the location of the NFC sensor; when the sensor is detected, the information is displayed on the screen. |
| Communication Test | Perform hardware tests such as RS232 or USB. (If testing, please contact the relevant personnel or maintenance personnel) |
| Brake Test | **Resistance output test.** (If testing, please contact the relevant personnel or maintenance personnel) |
| Sensor Tests | Test that the sensor is working. (If testing, please contact the relevant personnel or maintenance personnel) |
| Error Code Log | Diagnoses and saves malfunction error messages for a technician. **Press "Error Code Log" ten consecutive times to clear** the error messages. |

**There is no calibration on this bike.** The CT1000ENT-2023 treadmill's Service tab has an Incline
Motor entry with a Calibration button in this position
(`ct1000ent-2023-console-incline-only-calibration-and-service-tests`); the bike has a Brake Test - a
resistance output test - and a Communication Test instead, and no Drive Motor Test. The Key Test
line's "to start calibration" is a copy-and-paste from that treadmill page; the test flashes the
on-screen copy of each physical button pressed.

**Three of the six tell you to call someone.** Communication Test, Brake Test and Sensor Tests each
carry the note "please contact the relevant personnel or maintenance personnel"; the manual gives no
readings, pass values or steps for any of them.

**The Error Code Log is the console's fault history** and its entries are held with the error cards;
this card records only how to reach and clear it.

**The CR1000ENT-2023 recumbent bike's service manual (SR8880-SB028) prints the same six rows word
for word** - Key Test with its pasted "to start calibration", NFC Test, Communication Test, Brake
Test, Sensor Tests and the Error Code Log cleared by ten presses - so this card covers that machine
too, and it too has no calibration and no Drive Motor Test. Its p. 14 screenshot lists the six under
a Service heading in the same order. Neither bike's owner's manual is in the repository; nothing
here is corroborated by one.
