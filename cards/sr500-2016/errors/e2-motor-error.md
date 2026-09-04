---
id: sr500-2016-e2-motor-error
title: E2 motor error, cable tensioner communication
kind: troubleshooting
question: What does error E2 mean on a Sole sr500-2016 rower and how is it fixed?
asked_as:
- my sole rower says e2
- motor error on an sr500
- resistance stopped working and it shows e2
keywords:
- e2
- motor error
- cable tensioner
- communication
- 8-pin cable
- error code
- resistance
- rower
facets:
  brand:
  - sole
  product_line: rower
  model: sr500-2016
  applies_to:
  - sr500-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- sr500-2016-e1-eeprom-failure
see_also:
- sr500-2016-tension-motor-voltage-test
- sr500-2016-tension-motor-connector-pinout
- sr500-2016-no-adjustable-resistance
source:
  ref: sole-rower-sr500-2016-service-manual
  locator: Section 7, error code list, and section 7.2
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM / RAM ERROR).**

Definition: when the **"E2" "MOTOR ERROR"** message is displayed, communication with the cable tensioner is abnormal and **all functions are stopped**. The error code list prints the meaning as "Cable tension communication error".

How the circuit is meant to work:

| Device | Description |
|---|---|
| Console | Pressing UP or DOWN in program mode raises or lowers the LEVEL value on the display, and at the same time sends a command signal to the cable tensioner. |
| Cable tensioner | Receives the command signal from the console and actuates, and **supplies the console DC12V power**. |

Troubleshooting:

| Device | Troubleshooting |
|---|---|
| Console | 1. Check the connection of the motherboard's **8-pin cable**. 2. When UP or DOWN is pressed a beep is generated; if so, the signal has been sent. |
| 8-pin Cable | 1. Check the cable connections. 2. Check if the cable is broken or curled. 3. Replace the cable and retest. |
| Cable tensioner | Check the 8-pin cable connection. |

The numbered voltage measurement that confirms this is in a separate card.
