---
id: sole-inverter-error-code-list
title: AC inverter error code list
kind: spec
question: What are the AC inverter error codes on a Sole TT9 or ST90?
asked_as:
- what does e-04h mean
- inverter error codes on my treadmill
keywords:
- inverter error codes
- rhymebus
- ac inverter
- e-01h
- e-52h
- tt9
- st90
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - st90
  - tt9
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-dc-controller-error-code-list
- st90-parts-and-wiring
source:
  ref: sole-tm-console-error-code-list
  locator: AC inverter table
  extracted_at: '2026-09-03'
---

The TT9 and the ST90 use a Rhymebus AC inverter instead of a DC digital controller, so they have their own code set.

Unless a row names its own fix, the solution is: follow the inverter troubleshooting, then replace the inverter.

| Code | Cause | Solution |
|---|---|---|
| E-01H | Low voltage | Follow the inverter troubleshooting; replace the inverter |
| E-02H | Abnormal temperature | as above |
| E-04H | Output overcurrent (OC) | as above |
| E-06H | Converter overvoltage (OE) | as above |
| E-07H | Abnormal PFC | as above |
| E-08H | GF abnormal | as above |
| E-09H | Converter overheat (OH) | as above |
| E-0AH | Motor overload (OL) | as above |
| E-0BH | Converter overload (OL1) | as above |
| E-0CH | System overload (OLO) | as above |
| E-21H | PrEr flash program fault | as above |
| E-22H | EEPROM error | as above |
| E-23H | Low voltage display | as above |
| E-25H | Emergency stop | Check the 2-pin control cable is intact; replace the inverter |
| E-26H | drvF driver setting error | Follow the inverter troubleshooting; replace the inverter |
| E-27H | Low power input voltage (LP) | as above |
| E-28H | High power input voltage (HP) | as above |
| E-29H | High temperature alert (Ht) | as above |
| E-41H | System overload alert (OLO) | as above |
| E-42H | High temperature alert (Ht) | as above |
| E-50H | Console to inverter communication error | Check the control cable; replace the inverter; replace the console (needs recalibration) |
| E-51H | Console internal communication error | Check internal console wiring; replace the console (needs recalibration) |
| E-52H | Incline calibration error, front or rear | Check the front and rear incline motor wiring; check the incline motor for a jam or fault; replace the inverter |
| E3 red, E-53H | Front incline error | Check the incline motor wiring at the inverter terminal; check the incline motor; replace the inverter |
| E3 green | Rear incline error | Check the incline motor wiring at the incline adapter board; check the incline motor; replace the incline adapter board; replace the console |
