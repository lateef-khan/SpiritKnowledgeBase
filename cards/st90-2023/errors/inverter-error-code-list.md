---
id: st90-2023-inverter-error-code-list
title: Inverter error code list from the service manual
kind: spec
question: What are all the error codes for a Sole ST90-2023 treadmill?
asked_as:
- list of error codes for my sole slat treadmill
- what do the e dash codes mean
- st90 error code chart
keywords:
- error code list
- inverter
- e-01h
- e-52h
- code table
- slat belt
- treadmill
- ent
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2023
  applies_to:
  - st90-2023
  section: errors
  code: '*'
  model_number:
  - '590822'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-inverter-error-code-list
- sole-dc-controller-error-code-list
- st90-parts-and-wiring
source:
  ref: sole-tm-st90-2023-service-manual
  locator: Section 7 Error Code List, page 15; owner checklist sole-tm-st90-2023-owners-manual PDF pp. 27-28 (printed 25-26)
  extracted_at: '2026-09-04'
---

This machine uses an AC inverter, so its codes are the `E-nnH` set, not the E1 to E8 set used by the DC digital controller in the F63, F65, F80, F85, F89 and TT8.

| Code | Description | Cause, as printed |
|---|---|---|
| E-01H | Low voltage | Low voltage, please check outlet Voltage. Please check extension cord. |
| E-02H | Abnormal temperature | Abnormal inverter temperature. Contact your SOLE dealer. |
| E-04H | Overcurrent | Please check if motor, drive belt, roller, running belt are stuck. |
| E-06H | Converter overvoltage | Please check Braking resistor. |
| E-07H | Abnormal PFC | Make sure cables are connected securely. |
| E-08H | GF abnormal | Please check motor cable. |
| E-09H | Converters overheat | Please check and clean cooling fan. |
| E-0AH | Motor overload | Please lubricate running belt or check for bad bearing. |
| E-0BH | Converter overload | Please lubricate running belt or check for bad bearing. |
| E-21H | Abnormal PrEr Flash | Please lubricate running belt or check for bad bearing |
| E-22H | EEPROM error | Malfunction Contact your SOLE dealer. |
| E-23H | Low voltage | Low voltage, please check outlet voltage. Please check extension cord. |
| E-25H | Emergency Stop | Safety key pulled, please attach safety key. |
| E-29H | High temperature alert | Abnormal temperature, please clean dusk on cooling fan. |
| E-50H | Communication error | Please check all cables. |
| E-51H | Inter-communication error | Internal communication error. Contact your SOLE dealer. |
| E-52H | Incline calibration error | Is the cable between incline motor and controller connected correctly and properly? Check if incline mechanism being stock or defective? Is VR connected properly or with intermittence? |
| E-3H | Incline error | Same three checks as E-52H. |

**The table is identical to the earlier ST90 manual** except that E-09H is printed "Converters overheat" rather than "Converter overheat".

**Codes this manual does not list.** The company-wide inverter list (`sole-inverter-error-code-list`) also carries E-0CH, E-26H, E-27H, E-28H, E-41H, E-42H, E-53H and a green and red E3 split. This manual prints none of them.

**The owner's manual prints the same code set as an OK/NG checklist** (sole-tm-st90-2023-owners-manual PDF pp. 27-28, printed 25-26), headed "ERROR MESSAGES FOR DIGITAL-CONTROL SYSTEM TREADMILLS", each row shaped "Console showing <meaning> / Error E-nnH" with OK/NG tick boxes — word for word identical to the ST90-2021 owner's table, including the "Converter oberload" misprint. Code shapes verified against the render: zeros, not the letter O. Against the service table above: the owner says "Converter overheat" where the service table says "Converters overheat" (E-09H), "Please clean cooling fan" where it says "Please check and clean cooling fan", and "Please check running belt or check bearing for damage" where it says "Please lubricate running belt or check for bad bearing" (E-0AH, E-0BH, E-21H) — follow the service manual's fix; the owner's "check" is its customer-facing first step.
