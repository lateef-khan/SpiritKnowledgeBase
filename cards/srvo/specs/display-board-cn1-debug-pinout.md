---
id: srvo-display-board-cn1-debug-pinout
title: Pinout of CN1, the SRVO display board debug port
kind: spec
question: What is the pinout of the debug port on the SOLE SRVO display board?
asked_as:
- srvo debug port pinout
- srvo cn1 debug header
- how do i put the srvo display into boot mode
keywords:
- cn1
- debug port
- pinout
- uart
- serial
- 5v
- reset
- boot mode
- gpio0
- programming header
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn1
authority: 3
not_to_be_confused_with:
- srvo-power-board-dc-output-pinout
- srvo-display-board-cn5-pinout
see_also:
- srvo-display-board-connector-map
source:
  ref: sole-srvo-service-manual
  locator: page 32, section 8-1-2
  extracted_at: '2026-09-04'
---

**This is CN1 on the display main board, a six pin debug header. It is not CN1 on the full range power board, which is a DC output.**

| Pin | Name | Description | Default |
|---|---|---|---|
| 1 | 5V | DC5V | / |
| 2 | UART0_TX | TX | / |
| 3 | UART0_RX | RX | / |
| 4 | RES | MCU reset | / |
| 5 | GPIO0 | Enter 0BOOT mode | |
| 6 | GND | Ground | |

Pin 5's description is printed as **"Enter 0BOOT mode"**. That leading zero is almost certainly extraction damage for "BOOT mode", but the manual is quoted here as printed. The display MCU is an ESP32 according to the key component list, and GPIO0 is that part's normal boot-select pin.

The manual prints no default value for pins 5 and 6.
