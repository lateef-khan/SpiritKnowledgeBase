---
id: srvo-cooling-fan-specification
title: Cooling fan rating and part number
kind: spec
question: What cooling fan does the SOLE SRVO use?
asked_as:
- what fan is in the srvo
- srvo cooling fan part number
- how loud is the srvo fan
keywords:
- cooling fan
- fan spec
- 80mm
- 12v
- pwm
- airflow
- cfm
- noise
- part number
- dba
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- srvo-key-component-part-numbers
- srvo-disassembly-cooling-fan
- srvo-explosive-view-parts
source:
  ref: sole-srvo-service-manual
  locator: page 28, key component list row 10
  extracted_at: '2026-09-04'
---

Part number **004.039.0050054**. The machine has two, one behind each end cap.

| Item | Value |
|---|---|
| Model | CC8025H12D |
| Size | 80 × 80 × 25 mm |
| Voltage | 12 V |
| Current | 0.27 A |
| Control | PWM |
| Airflow | 37.48 CFM/min |
| Static pressure | 3.17 mmH2O |
| Noise | 32.5 dBA |
| Supplier code | QL |

The airflow unit is printed as "37.48CFM/ min". CFM is already a per minute figure, so the trailing "/min" is redundant in the source; the number is quoted as printed.

The fans are audible when the machine has power. The existing display-not-lighting-up card uses that: if the fans do not run, no electricity is reaching the unit.
