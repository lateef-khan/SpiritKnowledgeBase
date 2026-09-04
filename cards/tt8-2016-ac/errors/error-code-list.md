---
id: tt8-2016-ac-error-code-list
title: Inverter error code list
kind: spec
question: What are the error codes on a Sole tt8-2016-ac treadmill?
asked_as:
- list of error codes for my treadmill
- what do the e codes mean on the console
- inverter error code chart
keywords:
- error code list
- inverter
- e-01h
- e-52h
- e3
- ac drive
- fault code
- console message
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016-ac
  applies_to:
  - tt8-2016-ac
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- tt8-2016-error-code-list
see_also:
- tt8-2016-ac-e-01h-error-code
- tt8-2016-ac-e-02h-error-code
- tt8-2016-ac-e-04h-error-code
- tt8-2016-ac-e-06h-error-code
- tt8-2016-ac-e-07h-error-code
- tt8-2016-ac-e-08h-error-code
- tt8-2016-ac-e-09h-error-code
- tt8-2016-ac-e-0ah-error-code
- tt8-2016-ac-e-0bh-error-code
- tt8-2016-ac-e-0ch-error-code
- tt8-2016-ac-e-21h-error-code
- tt8-2016-ac-e-22h-error-code
- tt8-2016-ac-e-23h-error-code
- tt8-2016-ac-e-25h-error-code
- tt8-2016-ac-e-26h-error-code
- tt8-2016-ac-e-27h-error-code
- tt8-2016-ac-e-28h-error-code
- tt8-2016-ac-e-29h-error-code
- tt8-2016-ac-e-41h-error-code
- tt8-2016-ac-e-42h-error-code
- tt8-2016-ac-e-50h-error-code
- tt8-2016-ac-e-51h-error-code
- tt8-2016-ac-e-52h-error-code
- tt8-2016-ac-e-53h-error-code
- tt8-2016-ac-e3-error-code
source:
  ref: sole-tm-tt8-2016-ac-service-manual
  locator: Section 8.1 Error Message / Troubleshooting, pages 36-38
  extracted_at: '2026-09-04'
---

**AC model: TT8 2016 ST925A-YT030, AC drive motor driven by an inverter. The DC drive motor TT8 2016 (ST925-YT021) is a different machine and this card does not apply to it.**

Because the drive is an inverter, the codes are shaped **E-nnH** rather than the E0 to E7 set the DC-motor
TT8 uses. The two sets are not interchangeable.

| Code | Printed description |
|---|---|
| E-01H | Low voltage jump, confirm input power is too low |
| E-02H | Temperature sensing anomaly |
| E-04H | OC output overcurrent |
| E-06H | OE inverter Overvoltage |
| E-07H | PFC failure |
| E-08H | GF grounding failure |
| E-09H | OH inverter Overheating |
| E-0AH | OL Motor overload Abnormal |
| E-0BH | OL1 inverter overload anomaly |
| E-0CH | OLO System overload anomaly |
| E-21H | PrEr Flash Program failure |
| E-22H | EEPROM EEPROM failure |
| E-23H | Low voltage display |
| E-25H | Emergency shutdown display |
| E-26H | drvF Driver set error |
| E-27H | LP input low voltage |
| E-28H | HP input high voltage |
| E-29H | Ht High temperature display |
| E-41H | OLO System Overload Warning |
| E-42H | Ht High Temperature warning |
| E-50H | Error in communication between the console and inverter |
| E-51H | The console (internal) upper and lower communication error |
| E-52H | Error in calibration of the incline |
| E-53H | Machine (front) incline motor Error |
| E3 | Machine (rear) incline motor error |

There is no E-03H and no E-05H in this table, and no E0, E1, E2, E4, E5, E6 or E7 either.

The only tool the manual asks for is a multi-meter.

**The bare E3 is the odd one out.** On this machine E3 is the rear incline motor. On the DC-motor TT8 2016
(ST925-YT021) E3 means the incline VR voltage is out of range. Same two characters, different
machine, different fault.
