---
id: spirit-xt-errors-e5-console-controller-communication-poor
title: 'E5: the console and the controller are not talking, most often the main control
  wire'
kind: troubleshooting
question: What does E5 mean on a Spirit XT 2015, XT 2023 or XT ENT treadmill, and
  what does the service manual say to check?
asked_as:
- what does e5 mean on my spirit treadmill
- console not communicating with the controller
- e5 communication error treadmill
keywords:
- e5
- communication
- main control wire
- computer cable
- console
- lower controller
- display board
- error code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e5-igbt-fault
- ct900-e5-thermal-overload
- f65-2023-e5-communication-error
- spirit-2024-errors-e5-console-to-driver-board-link-interrupted
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- f65-2023-e5-communication-error
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: 'XT185 2023 service manual 8.6 Error Message: E5, PDF p. 29, text.md lines
    594-616; XT285 2023 service manual 8.6 Error Message: E5, PDF p. 30, text.md lines
    596-618; XT385 2023 service manual 8.6 Error Message: E5, PDF p. 31, text.md lines
    540-559; XT485 2023 service manual 8.6 Error Message: E5, PDF p. 31, text.md lines
    540-559; XT685 2023 service manual 8.6 Error Message: E5, PDF p. 30, text.md lines
    598-621; XT185 2015 service manual Error Message: E5, PDF p. 54, text.md lines
    965-1005; XT285 2015 service manual Error Message: E5, PDF p. 55 (printed 54),
    text.md lines 1035-1075; XT385 2015 service manual Error Message: E5, PDF p. 55,
    text.md lines 837-856; XT485 2015 service manual Error Message: E5, PDF p. 55,
    text.md lines 840-859; XT485ENT 2023 service manual 8.6 Error Message: E5, PDF
    p. 51, text.md lines 755-774; XT685ENT 2023 service manual 8.6 Error Message:
    E5, PDF p. 35, text.md lines 578-602'
  extracted_at: '2026-09-11'
---

**This is the XT E5 - not E5 on a Spirit 7.0T or MT200, which is an inverter IGBT fault (`70t-2026-errors-e5-igbt-fault`), not the CT900's E5 thermal overload, and not Sole's E5 (`f65-2023-e5-communication-error`), which is the same Dyaco text filed for Sole machines.**

Definition: *The communication between the console and the controller is poor. It may be due to a faulty main control wire, but it's also possible that either the display board or the controller is malfunctioning.* Cause: *The main control wire is possibly broken. But E5 maybe has another problem, like a component of the controller or console.*

| Part | Troubleshooting |
|---|---|
| Lower controller board | Replace main control wire. |
| Main control wires | Reinsert or replace Main control wire. |
| Display board | Replace display board. |

The first row is printed as it stands - the part named is the lower controller board and the action is to replace the main control wire. All eleven XT service manuals print the same three rows; the 2015 books and the XT485ENT word the last as *Replace upper control board*, and the 2023 XT685 and the XT485ENT print *Replace main control wire* a second time under the main control wires row.
