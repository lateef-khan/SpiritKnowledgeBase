---
id: ct850-2020-e-02h-igbt-temperature-sensor-feedback-low
title: 'E-02H: IGBT temperature sensor feedback too low'
kind: troubleshooting
question: What does E-02H mean on a Spirit CT850-2020 treadmill?
asked_as:
- what does e-02h mean on my treadmill
- treadmill showing e-02h
- how do i fix e-02h
keywords:
- e-02h
- e02h
- igbt
- temperature sensor
- inverter
- error code
- sensor feedback
- reboot
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: errors
  code: e-02h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-09h-inverter-over-heat
- ct850-2020-e-42h-high-temperature-warning
see_also:
- st90-2021-e-02h-abnormal-temperature
- ct850-2020-inverter-error-code-list
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36)
  extracted_at: '2026-09-08'
---

**This is E-02H, and it is not any other code printed with the same characters.** This is the sensor reading wrong, not the inverter actually being hot. Sole's ST90 prints E-02H as `Abnormal temperature`.

| Field | Value |
|---|---|
| Code | E-02H |
| Cause, word for word | Feedback voltage of IGBT temperature sensor is too low. |
| Solution, word for word | The Inverter temperature sensor is defective, try to reboot the treadmill that may restore the sensor. |

The whole printed table is on the card `ct850-2020-inverter-error-code-list`. The only tool section 8-2 asks for is a **multi-meter**.
