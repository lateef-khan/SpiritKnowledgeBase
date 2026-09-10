---
id: ct850-2020-display-board-connector-pinouts
title: Display board connector pin definitions
kind: spec
question: What are the display board connector pin definitions on a Spirit CT850-2020
  treadmill?
asked_as:
- ct850 2020 pin define table
- what are the pins on the c-safe connector
- usb connector pinout on the treadmill console
- keypad connector pins 2020 ct850
keywords:
- pin define
- pinout
- connector
- c-safe
- usb
- hand
- keypad
- safety
- esp
- ble
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: specs
  code: '*'
  model_number:
  - '850840'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2020-display-board-connector-locations
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: p. 30 (printed 29) and p. 31 (printed 30), section 6-1-6 'PCB BOARD PIN
    DEFINE'
  extracted_at: '2026-09-08'
---

| Connector | Pin definitions |
|---|---|
| **U4** BLE receiver | P1 N/C, P2 GND, P3 RXD, P4 TXD, P5 +3.3V, P6 BLE_REST |
| **JK2** C-Safe | P1 RX, P2 TX, P3 9V, P4 CTS, P5 GND |
| **JK3** USB | P1 +5V, P2 USB_DM, P3 USB_DP, P4 GND |
| **JK4** HAND | P1 HAND_R, P2 COM, P3 COM, P4 HAND_L |
| **JK6** Keypad | P1 SCAN1, P2 KEY1, P3 KEY2, P4 KEY3, P5 KEY4, P6 KEY5, P7 KEY6 |
| **JK8** Safety | +12v, X, S/W |
| **JK9** RM6T3 main (for CT850) | P1 DX+, P2 DX-, P3 GND, P4 WK_UP, P5 +12V, P6 GND |
| **JK10** ESP (for CT850) | P1 +12V, P2 S/W |
| **JK11** STD main (for CT800) | P1 GND, P2 RX, P3 TX, P4 +12V, P5 S/W, P6 SWD |
| **JK12** RF | P1 GND, P2 5V, P3 PULSE2_IN |
| **JK14** DC FAN | P1 +12v, P2 +12V, P3 GND, P4 GND |

Three defects in the printed tables, left as found:

- The **JK8** header reads "P1 P2 P2". Three signals are listed against two distinct pin
  numbers, so which of +12v, X and S/W sits on pin 3 is not recoverable from the manual.
- **JK9** is headed "RM6T3" here but the board drawings on pp. 22 and 26 label the same cable
  **RM6Y3**. The 2016 CT850's inverter is an RM6T3, so RM6T3 is the likelier spelling.
- **JK14** is tabled with four pins; the board drawing calls the fan plug 2 pins.
