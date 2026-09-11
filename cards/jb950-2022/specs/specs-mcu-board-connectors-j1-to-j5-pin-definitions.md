---
id: jb950-2022-specs-mcu-board-connectors-j1-to-j5-pin-definitions
title: 'The console MCU board: nine-pin system cable, LED display, icon backlight,
  USB update and keyboard connectors, with every pin named'
kind: spec
question: What plugs into the MCU board in the console of a Spirit jb950-2022 indoor
  cycle, and what is on each pin?
asked_as:
- jb950 console board connectors
- which pin is rpm on the jb950 system cable
- jb950 mcu board pinout
- what is the intrinity icon backlight plug on the jb950
keywords:
- mcu board
- upper control board
- pin definition
- j1 system cable
- 9 pin
- j2 led display
- j3 backlight
- j4 usb
- j5 key board
- mtr up
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: specs
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables
see_also:
- jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions
- jb950-2022-specs-circuit-diagram-9-pin-console-cable-and-6-pin-key-cable
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 4.2 MCU Board wire Connections / Function, PDF p. 29 (printed 29), text.md
    lines 384-399, photograph read from a 300 dpi render; Display Board PIN Definition,
    PDF p. 30, lines 402-432
  extracted_at: '2026-09-11'
---

The board behind the LED display is called the **MCU Board** on the wiring page, the **Display
Board** on the pin page and the *upper control board* in the error table. Five connectors:

| Connector | Lead |
|---|---|
| **J1** | System cable to lower board (9 pin) |
| **J2** | LED display |
| **J3** | Intrinity icon backlight |
| **J4** | USB software update |
| **J5** | Keyboard |

**J1 SYSTEM CABLE (9 PIN):** 1 GND, 2 **VDD +6v**, 3 **MTR UP**, 4 **MTR DN**, 5 **CHR**, 6 **OPT1**,
7 **OPT2**, 8 **RPM**, 9 **CNT**.
**J2 LED display:** 1 HT_CS, 2 HT_DATA, 3 HT_WR, 4 GND, 5 VLED.
**J3 LED backlight:** 1 VLED, 2 BL_CTRL.
**J4 USB software update:** 1 USB_VBUS, 2 USB_D-, 3 USB_D+, 4 GND.
**J5 KEY BOARD CABLE:** 1 KB_DATA1, 2 GND, 3 GND, 4 KB_DATA4, 5 KB_DATA3, 6 KB_DATA2.

**The console runs on 6 V from the lower board** - VDD +6v on pin 2 of the system cable - and
sends the brake motor its up/down commands over pins 3 and 4; the lower board's own copy of the
list names pin 2 plainly *VDD*. The keyboard's six wires are one ground pair and four data lines,
which is what the six-pin cable from the UP / DOWN / PLAY key on the circuit diagram carries.
The USB header is for software updates only.

