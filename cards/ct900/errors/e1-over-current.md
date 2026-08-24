---
id: ct900-e1-over-current
title: Error E1 - Over Current
kind: troubleshooting
question: What does error E1 Over Current mean on a CT900 and how do I fix it?
asked_as:
- what does e1 mean on the treadmill
- error 1 over current
keywords:
- e1
- over current
- overcurrent
- hardware current
- console error
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- ct900-e10-accel-ovr-curr
- ct900-e11-decel-ovr-curr
- ct900-e12-over-current
- ct900-ocst-over-current-protection-warning
see_also:
- ct900-e10-accel-ovr-curr
- ct900-e11-decel-ovr-curr
- ct900-e12-over-current
- ct900-ocst-over-current-protection-warning
source:
  ref: ct900-om
  locator: p. 44
  extracted_at: '2026-08-24'
---

**This is E1, not E10 (ACCEL OVR CURR), not E11 (DECEL OVR CURR), and not E12 - which is also named "OVER CURRENT" in the source with no further distinction given.**

The manual's Error Codes table gives no distinct description or solution for E1 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

See the inverter driver's own over-current-related warning code, [ocSt - Over current protection warning](ocst-over-current-protection-warning.md), which does have a stated corrective action ("Verify if the motor is overload").
