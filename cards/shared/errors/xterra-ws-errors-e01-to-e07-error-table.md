---
id: xterra-ws-errors-e01-to-e07-error-table
title: The walking treadmill's seven two-digit error codes, from poor communication
  to a safety lock out of place, and the abnormal-display row
kind: spec
question: What error codes can an Xterra ws200-2023 or ws300-2023 walking treadmill
  show, and what does each mean?
asked_as:
- ws200 error codes
- e01 on my xterra walking treadmill
- ws300 e03 meaning
keywords:
- error code list
- e01
- e02
- e03
- e04
- e05
- e06
- e07
- abnormal display
- walking treadmill
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - ws200-2023
  - ws300-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-owner-checklist-seven-codes-safety-key-to-abnormal-power
- f63-2026-error-code-list
- f80-2026-error-code-list
see_also:
- xterra-ws-errors-treadmill-does-not-work-five-causes
source:
  ref: xterra-treadmill-ws200-2023-owners-manual
  locator: WS200 OM Troubleshooting and Troubleshooting - Continued, two flat tables
    read from the render, PDF pp. 35-36 (printed 34-35); text.md lines 1029-1041 plus
    the OCR supplements for pages 35 and 36; WS300 OM Troubleshooting and Troubleshooting
    - Continued, two flat tables read from the render, PDF pp. 35-36 (printed 34-35);
    text.md lines 982-994 plus the OCR supplements for pages 35 and 36
  extracted_at: '2026-09-11'
---

The WS200 and WS300 owner's manuals print the same *Troubleshooting - Continued* table, a flat picture with no text layer, read from the render:

| Questions | Possible cause | Method |
|---|---|---|
| E01 | Poor communication | The signal line is not plugged, plug it again |
| E02 | Power assault | Power tube breakdown, replace the electronic controller |
| E03 | Non-sensing signal | Sensing wire is not plugged in properly. Plug it again correctly |
| E04 | Controller or motor abnormal | Overload, replace controller or motor |
| E05 | Overload protection | Overload, replace controller |
| E06 | System self-check failed | System failure, replace controller |
| E07 | Safety lock is not in place | Put the safety key in correct position |
| Abnormal display | External disturbance | Turn off power switch, turn it on after 1 minute |

These are two-digit codes. **They are not the E0 to E7 codes of the other Xterra treadmills** - here E01 is communication and E07 is the safety key, where the Dyaco-built treadmills use E5 and E0 - and they are not the Sole E01 to E06 family either, which numbers over current as E01. One card per code: `xterra-ws-errors-e01-poor-communication`, `xterra-ws-errors-e02-power-assault-power-tube`, `xterra-ws-errors-e03-non-sensing-signal`, `xterra-ws-errors-e04-controller-or-motor-abnormal`, `xterra-ws-errors-e05-overload-protection`, `xterra-ws-errors-e06-system-self-check-failed`, `xterra-ws-errors-e07-safety-lock-not-in-place`.

The first Troubleshooting page (no codes) is on `xterra-ws-errors-treadmill-does-not-work-five-causes`.
