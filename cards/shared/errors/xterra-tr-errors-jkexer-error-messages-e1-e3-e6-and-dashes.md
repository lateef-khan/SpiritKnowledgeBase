---
id: xterra-tr-errors-jkexer-error-messages-e1-e3-e6-and-dashes
title: 'The JKEXER console''s error messages: a speed code, a communication code,
  an incline code and three dashes for the safety key'
kind: spec
question: What error messages can an Xterra tr75h-2025 or tr95h-2024 treadmill show,
  and what does each mean?
asked_as:
- tr95h error codes
- tr75h e1 e3 e6
- xterra treadmill shows dashes
keywords:
- error messages
- error code list
- speed signal
- communication
- incline vr
- safety key
- dashes
- jkexer
- current limit
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- xterra-tr-errors-owner-error-messages-ls-console-memory-and-incline
see_also:
- xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
- xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller
- xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: TR95H SM 11. Explanation and troubleshooting of error messages, PDF pp.
    16-17; text.md lines 209-258; TR75H SM 12. Explanation and troubleshooting of
    error messages, PDF pp. 16-17; text.md lines 346-421; TR95H OM Troubleshooting,
    PDF p. 53 (printed 52); text.md lines 1920-1939; TR75H OM Troubleshooting, PDF
    p. 49 (printed 48); text.md lines 1845-1864
  extracted_at: '2026-09-11'
---

The TR75H and TR95H are JKEXER-built machines with their own code set. The owner's manual prints three codes; the service manual explains those three plus two symptoms with no code:

| Shown | Meaning | Detail card |
|---|---|---|
| E1 | The console does not receive the speed signal (owner's manual: for 7 seconds; service manual: about 6 seconds), **or** current-limit protection has shut the machine down | `xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit` |
| E3 | Poor communication between upper and lower controllers (the cable from computer to control box) | `xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller` |
| E6 | The console did not receive the change in the VR value of the incline motor (owner's manual: for 6 seconds) | `xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change` |
| - - - | The safety key connection of the console is abnormal | `xterra-tr-errors-jkexer-console-shows-three-dashes-safety-key` |
| console dark | The console has no power supply | `xterra-tr-errors-jkexer-console-does-not-light-up` |

**On these two machines E3 is a communication fault and E6 an incline fault** - the reverse of the Dyaco-built Xterra treadmills, where E3/ER is the incline code and E5 the communication code, and E6 is a controller fault. Neither JKEXER book prints E0, E2, E4, E5, E7 or E9: the owner's Troubleshooting page lists only E1, E6, E3 and a SMELL row, and the service manual's error chapter numbers its items 1 to 5 as above. That absence was checked in the text layer and in the OCR supplements of both books.

The owner's SMELL row (spray silicone on the running board, then consult the distributor) is a care remedy and belongs with maintenance.
