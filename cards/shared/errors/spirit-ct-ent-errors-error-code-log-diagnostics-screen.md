---
id: spirit-ct-ent-errors-error-code-log-diagnostics-screen
title: The Diagnostics screen keeps an Error Code Log that names each stored code
  in a few words
kind: fact
question: Where are past error codes stored on a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill, and how are they labelled?
asked_as:
- where is the error log on my spirit treadmill
- diagnostics screen error code log
- what does no motor output signal mean in the log
keywords:
- error code log
- diagnostics
- engineering mode
- touch screen
- no motor output signal
- communication abnormal
- abnormal external voltage
- abnormal motor voltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-2024-errors-seven-code-table-with-no-hyphen
- spirit-2024-errors-e1-drive-motor-no-output-signal
- cu900ent-error-code-log
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT 2022 service manual Diagnostics, a picture read from the render,
    PDF p. 44, text.md lines 862-868; CT850ENT 2022 service manual Diagnostics, a
    picture read from the render, PDF p. 45, text.md lines 881-887; CT800ENT 2022
    service manual Engineering Mode Settings table, PDF p. 41, text.md lines 828-843
  extracted_at: '2026-09-11'
---

Engineering mode on the ENT touch screen has a **Diagnostics** entry, described in the settings table as *The Error Diagnostics*. Its page in both service manuals is a picture of the screen, headed **Error Code Log**, with a home button and a back arrow and six logged lines:

| Code | Log text |
|---|---|
| E1 | No motor output signal. |
| E5 | Communication abnormal. |
| E7 | Abnormal external voltage. |
| E4 | Abnormal motor voltage. |
| E7 | Abnormal external voltage. |
| E5 | Communication abnormal. |

So the log stores the DC-controller codes with a three-or-four-word label of its own, shorter than the 8-1 table's causes (`spirit-2024-errors-seven-code-table-with-no-hyphen`): E1 is the drive motor giving no output signal, E4 an abnormal motor voltage, E5 a broken console-to-board link, E7 an abnormal supply voltage. **The page prints no instruction for clearing the log** - the CT900ENT and CT1000ENT books say to press the Error Code Log button ten times (`cu900ent-error-code-log`); these two do not.

**The CT850ENT 2022 prints the same screenshot with the same DC codes**, although that machine's own 8-1 table is the `E-xxH` inverter list and the codes its log would hold are those. The picture is the CT800ENT's, reused. The way into engineering mode - ten presses on the Home icon - is a console fact.
